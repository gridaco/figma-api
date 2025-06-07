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

yaml = YAML()
yaml.preserve_quotes = True
path = Path("openapi.file.yaml")

data = yaml.load(path)

schemas = data["components"]["schemas"]
node_discriminator = schemas.get("Node", {}).get("discriminator", {})
mapping = node_discriminator.get("mapping", {})

for tag, ref in mapping.items():
    schema_name = ref.split("/")[-1]
    schema = schemas.get(schema_name)

    if not schema:
        print(f"⚠️ Schema {schema_name} not found.")
        continue

    print(f"✂️  Cleaning discriminator target: {schema_name}")

    all_of = schema.get("allOf", [])
    for item in all_of:
        if isinstance(item, dict) and item.get("type") == "object":
            props = item.get("properties", {})
            props.pop("type", None)

            if "required" in item and isinstance(item["required"], list):
                item["required"] = [r for r in item["required"] if r != "type"]

layer_trait = schemas.get("IsLayerTrait")
if layer_trait and isinstance(layer_trait, dict):
    print("✂️  Cleaning IsLayerTrait")
    props = layer_trait.get("properties", {})
    props.pop("type", None)
    if "required" in layer_trait:
        layer_trait["required"] = [
            r for r in layer_trait["required"] if r != "type"]

yaml.dump(data, Path("openapi.file.rust.yaml"))
print("✅ Done. Discriminator 'type' fields removed.")
