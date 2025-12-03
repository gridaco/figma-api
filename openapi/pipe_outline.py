#!/usr/bin/env python3
"""
Extract inline schemas from OpenAPI spec to named schemas.

This script processes an OpenAPI spec and extracts all inline schema definitions
from response definitions into named schemas in components.schemas, then
updates the response definitions to reference these named schemas.

This eliminates InlineObject* types and produces cleaner, more maintainable code.
"""

from ruamel.yaml import YAML
from pathlib import Path
from typing import Dict, Any, Optional, Set, Tuple
import re
from copy import deepcopy
import click

yaml = YAML()
yaml.preserve_quotes = True
yaml.width = 120
yaml.indent(mapping=2, sequence=4, offset=2)


def sanitize_name(name: str) -> str:
    """Convert a response name to a schema name."""
    # Remove "Response" suffix
    if name.endswith("Response"):
        name = name[:-8]

    # Remove invalid characters (brackets, etc.) that violate OpenAPI naming
    # OpenAPI schema names must match: ^[a-zA-Z0-9\.\-_]+$
    name = re.sub(r"[\[\]]+", "", name)  # Remove brackets

    # Handle camelCase/PascalCase - split on capital letters
    # e.g., "GetFileResponse" -> ["Get", "File"]
    parts = re.findall(r"[A-Z][a-z]*|[a-z]+", name)
    if not parts:
        # Fallback: split on any non-alphanumeric
        parts = re.split(r"[-_\s\.]+", name)

    # Convert to PascalCase and ensure valid characters only
    result = "".join(word.capitalize() for word in parts if word)
    # Final sanitization: remove any remaining invalid characters
    result = re.sub(r"[^a-zA-Z0-9\.\-_]", "", result)
    return result


def get_enum_name(prop_name: str, enum_values: list) -> str:
    """Generate a meaningful enum name from property name and values."""
    # Sanitize prop_name first (remove brackets and other invalid chars)
    prop_name = re.sub(r"[\[\]]+", "", prop_name)

    # Common enum patterns
    if prop_name.lower() in ["role", "roles"]:
        return "Role"
    elif prop_name.lower() in ["editortype", "editor_type"]:
        return "EditorType"
    elif prop_name.lower() in ["linkaccess", "link_access"]:
        return "LinkAccess"
    elif "status" in prop_name.lower():
        return "Status"
    elif "error" in prop_name.lower():
        return "Error"
    else:
        # Default: capitalize property name and sanitize
        parts = re.split(r"[-_\s\.]+", prop_name)
        result = "".join(word.capitalize() for word in parts if word)
        # Ensure valid characters only (OpenAPI: ^[a-zA-Z0-9\.\-_]+$)
        result = re.sub(r"[^a-zA-Z0-9\.\-_]", "", result)
        return result


def extract_schema_recursive(
    schema: Dict[str, Any],
    base_name: str,
    schemas: Dict[str, Any],
    extracted_enums: Set[str],
    path: str = "",
    visited_refs: Set[str] = None,
) -> Dict[str, Any]:
    """
    Recursively process a schema, extracting nested objects and enums.
    Returns the processed schema (may contain $ref instead of inline definitions).
    """
    if visited_refs is None:
        visited_refs = set()

    if not isinstance(schema, dict):
        return schema

    # If already a reference, return as-is (but track to avoid circular processing)
    if "$ref" in schema:
        ref = schema["$ref"]
        if ref.startswith("#/components/schemas/"):
            ref_name = ref.split("/")[-1]
            if ref_name in visited_refs:
                # Circular reference detected - return as-is to avoid infinite loop
                return schema
            visited_refs.add(ref_name)
        return schema

    result = {}

    # Copy type and description
    if "type" in schema:
        result["type"] = schema["type"]
    if "description" in schema:
        result["description"] = schema["description"]
    if "format" in schema:
        result["format"] = schema["format"]
    if "default" in schema:
        result["default"] = schema["default"]

    # Handle enums
    if schema.get("type") == "string" and "enum" in schema:
        enum_name = get_enum_name(
            path.split(".")[-1] if path else base_name, schema["enum"]
        )

        # Check if we should extract this enum (if it's used in multiple places)
        # For now, extract all enums to avoid duplication
        if enum_name not in schemas:
            enum_schema = {"type": "string", "enum": schema["enum"]}
            if "description" in schema:
                enum_schema["description"] = schema["description"]
            schemas[enum_name] = enum_schema
            extracted_enums.add(enum_name)

        return {"$ref": f"#/components/schemas/{enum_name}"}

    # Handle object types
    if schema.get("type") == "object":
        if "properties" in schema:
            properties = {}
            for prop_name, prop_schema in schema["properties"].items():
                prop_path = f"{path}.{prop_name}" if path else prop_name

                if isinstance(prop_schema, dict):
                    # Check if it's a nested object that should be extracted
                    if (
                        prop_schema.get("type") == "object"
                        and "properties" in prop_schema
                    ):
                        # Extract nested object (e.g., "meta" objects)
                        nested_name = f"{base_name}{prop_name.capitalize()}"
                        if nested_name not in schemas:
                            nested_schema = extract_schema_recursive(
                                prop_schema,
                                nested_name,
                                schemas,
                                extracted_enums,
                                prop_path,
                            )
                            schemas[nested_name] = nested_schema
                        properties[prop_name] = {
                            "$ref": f"#/components/schemas/{nested_name}"
                        }
                    elif prop_schema.get("type") == "array" and "items" in prop_schema:
                        # Handle array items
                        items = prop_schema["items"]
                        if (
                            isinstance(items, dict)
                            and items.get("type") == "object"
                            and "properties" in items
                        ):
                            # Extract array item schema
                            item_name = f"{base_name}{prop_name.capitalize()}Item"
                            if item_name not in schemas:
                                item_schema = extract_schema_recursive(
                                    items,
                                    item_name,
                                    schemas,
                                    extracted_enums,
                                    f"{prop_path}[]",
                                )
                                schemas[item_name] = item_schema
                            properties[prop_name] = {
                                "type": "array",
                                "items": {"$ref": f"#/components/schemas/{item_name}"},
                            }
                            if "description" in prop_schema:
                                properties[prop_name]["description"] = prop_schema[
                                    "description"
                                ]
                        else:
                            # Process items but keep inline if simple
                            processed_items = extract_schema_recursive(
                                items,
                                f"{base_name}{prop_name.capitalize()}",
                                schemas,
                                extracted_enums,
                                f"{prop_path}[]",
                            )
                            properties[prop_name] = {
                                "type": "array",
                                "items": processed_items,
                            }
                            if "description" in prop_schema:
                                properties[prop_name]["description"] = prop_schema[
                                    "description"
                                ]
                    else:
                        # Process other property types recursively
                        properties[prop_name] = extract_schema_recursive(
                            prop_schema, base_name, schemas, extracted_enums, prop_path
                        )
                else:
                    properties[prop_name] = prop_schema

            result["properties"] = properties

        # Handle additionalProperties
        if "additionalProperties" in schema:
            additional_props = schema["additionalProperties"]
            if isinstance(additional_props, dict):
                if (
                    additional_props.get("type") == "object"
                    and "properties" in additional_props
                ):
                    # Extract nested schema for additionalProperties
                    nested_name = f"{base_name}Value"
                    if nested_name not in schemas:
                        nested_schema = extract_schema_recursive(
                            additional_props,
                            nested_name,
                            schemas,
                            extracted_enums,
                            f"{path}.<key>",
                        )
                        schemas[nested_name] = nested_schema
                    result["additionalProperties"] = {
                        "$ref": f"#/components/schemas/{nested_name}"
                    }
                else:
                    result["additionalProperties"] = extract_schema_recursive(
                        additional_props,
                        base_name,
                        schemas,
                        extracted_enums,
                        f"{path}.<key>",
                    )
            else:
                result["additionalProperties"] = additional_props

        # Copy required fields
        if "required" in schema:
            result["required"] = schema["required"]

    # Handle array types
    elif schema.get("type") == "array" and "items" in schema:
        items = schema["items"]
        if (
            isinstance(items, dict)
            and items.get("type") == "object"
            and "properties" in items
        ):
            # Extract array item schema
            item_name = f"{base_name}Item"
            if item_name not in schemas:
                item_schema = extract_schema_recursive(
                    items, item_name, schemas, extracted_enums, f"{path}[]"
                )
                schemas[item_name] = item_schema
            result["type"] = "array"
            result["items"] = {"$ref": f"#/components/schemas/{item_name}"}
            if "description" in schema:
                result["description"] = schema["description"]
        else:
            result = extract_schema_recursive(
                items, base_name, schemas, extracted_enums, f"{path}[]"
            )
            result = {"type": "array", "items": result}
            if "description" in schema:
                result["description"] = schema["description"]

    # Handle oneOf, anyOf, allOf
    for union_type in ["oneOf", "anyOf", "allOf"]:
        if union_type in schema:
            result[union_type] = [
                extract_schema_recursive(
                    item, base_name, schemas, extracted_enums, path
                )
                if isinstance(item, dict)
                else item
                for item in schema[union_type]
            ]

    return result


def extract_response_schema(
    response_name: str,
    response_def: Dict[str, Any],
    schemas: Dict[str, Any],
    extracted_enums: Set[str],
) -> Optional[str]:
    """Extract inline schema from a response definition."""
    content = response_def.get("content", {})
    json_content = content.get("application/json", {})
    schema = json_content.get("schema")

    if not schema:
        return None

    # If it's already a reference, return as-is
    if "$ref" in schema:
        return schema["$ref"]

    # Generate schema name from response name
    schema_name = sanitize_name(response_name)

    # If schema already exists, use it
    if schema_name in schemas:
        return f"#/components/schemas/{schema_name}"

    # Extract the schema recursively
    extracted_schema = extract_schema_recursive(
        schema, schema_name, schemas, extracted_enums, ""
    )

    # Save the extracted schema
    schemas[schema_name] = extracted_schema

    return f"#/components/schemas/{schema_name}"


def process_openapi(input_path: Path, output_path: Path):
    """Process OpenAPI spec and extract inline schemas."""
    print(f"📖 Reading {input_path}...")
    data = yaml.load(input_path)

    if "components" not in data:
        data["components"] = {}
    if "schemas" not in data["components"]:
        data["components"]["schemas"] = {}

    schemas = data["components"]["schemas"]
    original_schema_count = len(schemas)
    responses = data.get("components", {}).get("responses", {})

    extracted_enums: Set[str] = set()

    print(f"🔍 Processing {len(responses)} responses...")

    # Process each response
    extracted_count = 0
    for response_name, response_def in responses.items():
        schema_ref = extract_response_schema(
            response_name, response_def, schemas, extracted_enums
        )

        if schema_ref:
            # Update response to reference the extracted schema
            content = response_def.get("content", {})
            json_content = content.get("application/json", {})
            json_content["schema"] = {"$ref": schema_ref}
            print(f"  ✓ Extracted {response_name} → {schema_ref}")
            extracted_count += 1

    # Note: We don't process existing schemas recursively to avoid issues with circular references.
    # The extract_schema_recursive function already handles inline objects when processing responses.
    # Additional inline objects in existing schemas are left as-is to maintain compatibility.

    new_schemas = len(schemas) - original_schema_count
    print(f"\n📝 Writing {output_path}...")
    yaml.dump(data, output_path)
    print(
        f"✅ Done! Extracted {extracted_count} responses and {new_schemas} new schemas ({len(extracted_enums)} enums)."
    )


@click.command()
@click.argument("input_file", type=click.Path(exists=True, path_type=Path))
@click.argument("output_file", type=click.Path(path_type=Path))
def main(input_file: Path, output_file: Path):
    """
    Extract inline schemas from OpenAPI spec to named schemas.

    INPUT_FILE: Path to the input OpenAPI YAML file

    OUTPUT_FILE: Path where the output YAML file will be written
    """
    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)

    process_openapi(input_file, output_file)


if __name__ == "__main__":
    main()
