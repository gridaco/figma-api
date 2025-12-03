"""
WHY TYPE FIELD IS REMOVED FROM SCHEMAS IN THIS PROJECT
========================================================

Context
-------

In the OpenAPI spec for the Figma API (and similar structured APIs), many node schemas (e.g. RectangleNode, TextNode, etc.)
contain a field called `type`, which represents the node type as a string literal (e.g. "RECTANGLE", "TEXT").

The top-level `Node` schema uses a discriminator:

  discriminator:
    propertyName: type
    mapping:
      RECTANGLE: '#/components/schemas/RectangleNode'
      TEXT: '#/components/schemas/TextNode'
      ...

In Rust, we deserialize this using Serde with:

  #[serde(tag = "type")]
  enum Node {
      #[serde(rename = "RECTANGLE")]
      Rectangle(RectangleNode),
      ...
  }

Issue
-----

Serde will consume the `"type"` field to determine which variant of the `Node` enum to instantiate.
Once it's consumed at the enum level, it will not be passed to the inner struct (e.g. `RectangleNode`).

If the inner struct also requires `"type"` as a required field (e.g. `pub r#type: String`), deserialization will fail with:

  missing field `type`

Workaround
----------

The only clean and correct solution is to:

1. Keep `"type"` only at the enum (discriminator) level
2. **Remove `"type"` from all variant schemas**, including:
   - `RectangleNode`
   - `TextNode`
   - Shared traits like `IsLayerTrait`

This matches Serde's design and avoids redundant or conflicting field expectations.

Specifically, we have removed:

  components.schemas.IsLayerTrait.properties.type
  and also removed "type" from its "required" list

Effect
------

- The OpenAPI spec is still valid — the discriminator works fine
- Rust Serde works without runtime panics
- The inner structs no longer include `r#type: String`, which was redundant anyway
- Downstream consumers who rely on `node.type` should use pattern matching on the enum instead

Alternative Considered
-----------------------

We also considered:
- Post-processing the generated Rust files to delete the field manually
- Keeping `type` and using `#[serde(skip)]` in the struct

These were more brittle and harder to maintain.

This change is the simplest, safest, and most spec-compliant.
"""

from ruamel.yaml import YAML
from pathlib import Path
import click

yaml = YAML()
yaml.preserve_quotes = True


def process_rust_spec(input_path: Path, output_path: Path, override_path: Path = None):
    """Process OpenAPI spec for Rust/Serde compatibility."""
    if not input_path.exists():
        raise click.FileError(str(input_path), hint="Input file not found")

    data = yaml.load(input_path)

    # Merge in overrides if provided
    if override_path and override_path.exists():
        override_data = yaml.load(override_path)

        # Set of keys that should be FULLY replaced (not merged) even if both values are dicts
        FULL_REPLACE_KEYS = {
            "GetImageFillsResponse",
            "HasLayoutTrait.properties.layoutGrow",
            "TextureEffect",
            "BaseNoiseEffect",
            "NoiseEffect",
        }

        def deep_merge(a, b, path=""):
            for key, value in b.items():
                full_key = f"{path}.{key}" if path else key
                if (
                    full_key in FULL_REPLACE_KEYS
                    or not isinstance(value, dict)
                    or key not in a
                    or not isinstance(a[key], dict)
                ):
                    a[key] = value
                else:
                    deep_merge(a[key], value, full_key)

        # Handle components.schemas overrides
        for k, v in override_data.get("components", {}).get("schemas", {}).items():
            print(f"🔁 Overriding schema: {k}")
            if k in FULL_REPLACE_KEYS:
                data["components"]["schemas"][k] = v
            else:
                base = data["components"]["schemas"].setdefault(k, {})
                deep_merge(base, v, k)

        # Handle components.responses overrides
        for k, v in override_data.get("components", {}).get("responses", {}).items():
            print(f"🔁 Overriding response: {k}")
            if k in FULL_REPLACE_KEYS:
                data["components"]["responses"][k] = v
            else:
                base = data["components"]["responses"].setdefault(k, {})
                deep_merge(base, v, k)
    elif override_path:
        print(f"⚠️  Warning: {override_path} not found, skipping overrides")

    schemas = data["components"]["schemas"]
    #
    # Find all discriminator definitions across all schemas
    discriminator_targets = {}
    for schema_name, schema in schemas.items():
        if "discriminator" in schema:
            discriminator = schema["discriminator"]
            prop_name = discriminator.get("propertyName")
            mapping = discriminator.get("mapping", {})
            for ref in mapping.values():
                variant_name = ref.split("/")[-1]
                discriminator_targets.setdefault(variant_name, []).append(prop_name)

    # Remove discriminator fields from all target schemas
    for schema_name, prop_names in discriminator_targets.items():
        schema = schemas.get(schema_name)
        if not schema:
            print(f"⚠️ Schema {schema_name} not found.")
            continue
        print(f"✂️  Cleaning discriminator target: {schema_name}")
        all_of = schema.get("allOf", [])
        for item in all_of:
            if isinstance(item, dict) and item.get("type") == "object":
                props = item.get("properties", {})
                for prop_name in prop_names:
                    props.pop(prop_name, None)
                if "required" in item and isinstance(item["required"], list):
                    item["required"] = [
                        r for r in item["required"] if r not in prop_names
                    ]

    layer_trait = schemas.get("IsLayerTrait")
    if layer_trait and isinstance(layer_trait, dict):
        print("✂️  Cleaning IsLayerTrait")
        props = layer_trait.get("properties", {})
        props.pop("type", None)
        if "required" in layer_trait:
            layer_trait["required"] = [
                r for r in layer_trait["required"] if r != "type"
            ]

    # HARD_REMOVED_PROPS
    # -------------------
    # This is a list of field names that will be forcibly and unconditionally removed from *all* schemas.
    # It is used as a last-resort solution for fields that are:
    #   - consistently causing deserialization failures (e.g. invalid type: null, expected struct ...)
    #   - too structurally inconsistent across the API
    #   - not currently needed in our Rust model usage
    #
    # Examples:
    # - "fillOverrideTable" uses oneOf + nullable object maps that do not generate clean Rust types
    # - "absoluteRenderBounds" often appears as null but is typed as a non-optional struct
    #
    # These will be removed from every `properties` object in all matching schemas regardless of context.
    #
    # Rust errors typically look like:
    #     Error("invalid type: null, expected struct Rectangle")
    #
    # Which happens when a struct like this:
    #     pub absolute_render_bounds: Rectangle,
    #
    # is fed `null` in the JSON:
    #     "absoluteRenderBounds": null
    #
    # But we currently do not use this field, so it is safer to exclude it from generation entirely.
    HARD_REMOVED_PROPS = {
        "fillOverrideTable",
        "absoluteBoundingBox",
        "absoluteRenderBounds",
        "interactions",
    }

    # Apply HARD_REMOVED_PROPS to every schema
    for schema_name, schema in schemas.items():
        targets = []
        if schema.get("type") == "object":
            targets.append(schema)
        if "allOf" in schema:
            for item in schema["allOf"]:
                if isinstance(item, dict) and item.get("type") == "object":
                    targets.append(item)
        for target in targets:
            props = target.get("properties", {})
            for key in HARD_REMOVED_PROPS:
                if key in props:
                    print(f"❌ Hard removing `{key}` from {schema_name}")
                    props.pop(key)

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    yaml.dump(data, output_path)
    print(f"✅ Done. Discriminator 'type' fields removed.")
    print(f"   Output written to: {output_path}")


@click.command()
@click.argument("input_file", type=click.Path(exists=True, path_type=Path))
@click.argument("output_file", type=click.Path(path_type=Path))
@click.option(
    "--overrides",
    "-o",
    type=click.Path(exists=True, path_type=Path),
    default=None,
    help="Path to override YAML file (default: openapi.rust.overrides.yaml in current directory)",
)
def main(input_file: Path, output_file: Path, overrides: Path = None):
    """
    Process OpenAPI spec for Rust/Serde compatibility.

    INPUT_FILE: Path to the input OpenAPI YAML file (typically the outlined spec)

    OUTPUT_FILE: Path where the output YAML file will be written
    """
    # Default override path if not provided
    if overrides is None:
        overrides = Path("openapi.rust.overrides.yaml")

    process_rust_spec(input_file, output_file, overrides)


if __name__ == "__main__":
    main()
