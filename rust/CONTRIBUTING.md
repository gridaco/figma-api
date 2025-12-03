## Prerequisites

- `brew install openapi-generator`
- `pip3 install ruamel.yaml click`

**/v1/file only**

### Quick Start

Run the full pipeline:

```bash
cd openapi
./pipe.sh
```

This runs both steps automatically and generates the final Rust-ready spec.

### Manual Steps

#### Step 1: Extract Inline Schemas

Extract inline schemas from the filtered spec to named schemas:

```bash
cd openapi
python3 pipe_outline.py openapi.file.yaml piped/scope=file/openapi.file.outline.yaml
```

This generates `piped/scope=file/openapi.file.outline.yaml` by:

- Extracting all inline response schemas to named schemas in `components.schemas`
- Extracting nested inline objects from schema properties
- Extracting shared enums (Role, EditorType, etc.) to avoid duplication
- This eliminates `InlineObject*` types in generated code

#### Step 2: Pre-process for Rust/Serde Compatibility

Process the outlined spec for Rust/Serde compatibility:

```bash
cd openapi
python3 pipe_rust_rm_type.py \
  piped/scope=file/openapi.file.outline.yaml \
  piped/scope=file/openapi.file.outline.rust.yaml \
  --overrides openapi.rust.overrides.yaml
```

This generates `piped/scope=file/openapi.file.outline.rust.yaml` by:

- Applying overrides from `openapi.rust.overrides.yaml`
- Removing discriminator fields from variant schemas
- Removing problematic fields that cause deserialization failures

**Note:** All pipeline-processed files are stored in `piped/scope=file/`.

### Step 3: Generate Rust Code

```bash
cd ..
openapi-generator-cli generate \
  -i openapi/piped/scope=file/openapi.file.outline.rust.yaml \
  -c openapi/config.json \
  -g rust \
  -t ./templates \
  -o figma_rest_api_file
```

**Note:** Always use `piped/scope=file/openapi.file.outline.rust.yaml` (the processed version), not `openapi.file.yaml`.

### Pipeline Files

All pipeline-processed files are stored in `openapi/piped/scope=file/`:

- `openapi.file.outline.yaml` - Spec with extracted inline schemas (from `pipe_outline.py`)
- `openapi.file.outline.rust.yaml` - Rust-compatible processed spec (from `pipe_rust_rm_type.py`)

Source files in `openapi/`:

- `openapi.file.yaml` - File-only spec (manually created or filtered)
- `openapi.rust.overrides.yaml` - Schema overrides for Rust compatibility (manually authored)
