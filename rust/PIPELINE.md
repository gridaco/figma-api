# Figma API Rust Client Generation Pipeline

## Overview

This project generates a Rust API client for the Figma REST API based on its OpenAPI specification. The generation process involves pre-processing the OpenAPI spec to fix compatibility issues with Rust/Serde before running the code generator.

## Full Pipeline

### Step 1: Pre-process OpenAPI Specification

The raw OpenAPI spec (`openapi/openapi.file.yaml`) cannot be directly used because it contains schema definitions that cause deserialization failures in Rust. A Python script (`openapi/rust_rm_type.py`) pre-processes the spec:

```bash
cd openapi
python3 rust_rm_type.py
```

**What the script does:**

1. Loads `openapi.file.yaml`
2. Applies overrides from `openapi.rust.overrides.yaml` (fixes for specific schemas)
3. Removes discriminator fields (like `type`) from schemas used as enum variants
   - Serde consumes the discriminator field at the enum level, so it shouldn't be in the inner structs
4. Removes hard-coded problematic fields:
   - `fillOverrideTable` - uses oneOf + nullable object maps that don't generate clean Rust types
   - `absoluteBoundingBox` - often appears as null but typed as non-optional struct
   - `absoluteRenderBounds` - same issue
   - `interactions` - structurally inconsistent
5. Outputs `openapi.file.rust.yaml` (the processed spec ready for generation)

### Step 2: Generate Rust Code

Run the OpenAPI Generator with the processed spec:

```bash
openapi-generator-cli generate \
  -i openapi/openapi.file.rust.yaml \
  -c openapi/config.json \
  -g rust \
  -t ./templates \
  -o generated-client
```

**Note:** The `CONTRIBUTING.md` currently says to use `openapi.file.yaml`, but it should use `openapi.file.rust.yaml` (the processed version).

### Step 3: Manual Adjustments

After generation, the following manual adjustments are made to `figma-api`:

1. **Cargo.toml updates:**

   - Version bumped from `0.31.0` to `0.31.3`
   - Authors updated to include `universe@grida.co`
   - License changed from `Unlicense` to `MIT`
   - Added repository, documentation, keywords, and categories
   - Made `reqwest` optional with feature flags
   - Added dev-dependencies (`serde_path_to_error`, `tokio`)

2. **Test files:**

   - Added `tests/serialization_test.rs` - tests deserialization of example JSON files
   - Added `tests/files_api_integration.rs` - integration tests for API calls

3. **Stale file cleanup:**
   - `has_geometry_trait_all_of_fill_override_table.rs` exists in `figma-api` but is not generated anymore (removed by the Python script). It's not referenced anywhere and can be safely deleted.

## Why Pre-processing is Necessary

The Figma API spec uses discriminators extensively (e.g., `Node` enum with variants like `RectangleNode`, `TextNode`, etc.). In Rust with Serde:

- The discriminator field (`type`) is consumed at the enum level: `#[serde(tag = "type")]`
- If the inner structs also require `type` as a field, deserialization fails with "missing field `type`"
- Solution: Remove `type` from all variant schemas, keeping it only at the enum level

Additionally, some fields in the spec are:

- Structurally inconsistent (nullable vs non-nullable)
- Too complex for clean Rust type generation
- Not currently needed in our usage

These are removed via the `HARD_REMOVED_PROPS` list in the Python script.

## Current State

- **Generated code matches existing code:** The model and API files are identical between `generated-client` and `figma-api` (except for the stale `has_geometry_trait_all_of_fill_override_table.rs`)
- **Only differences are:**
  1. `Cargo.toml` - manual metadata updates
  2. Test files - manually added
  3. One stale model file that should be removed

## Recommended Workflow

1. Update `openapi/openapi.file.yaml` if the Figma spec changes
2. Update `openapi/openapi.rust.overrides.yaml` if schema fixes are needed
3. Run the pre-processing script: `cd openapi && python3 rust_rm_type.py`
4. Generate fresh code: `openapi-generator-cli generate -i openapi/openapi.file.rust.yaml -c openapi/config.json -g rust -t ./templates -o generated-client`
5. Copy generated code to `figma-api/src/` (excluding tests)
6. Update `figma-api/Cargo.toml` with manual metadata
7. Keep test files in `figma-api/tests/`
8. Remove any stale files that are no longer generated

## Files to Update in CONTRIBUTING.md

The `CONTRIBUTING.md` should be updated to reflect the correct pipeline:

```bash
# Step 1: Pre-process the OpenAPI spec
cd openapi
python3 rust_rm_type.py

# Step 2: Generate Rust code
cd ..
openapi-generator-cli generate \
  -i openapi/openapi.file.rust.yaml \
  -c openapi/config.json \
  -g rust \
  -t ./templates \
  -o generated-client
```
