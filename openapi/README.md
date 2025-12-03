# openapi spec

> From https://github.com/figma/rest-api-spec/blob/main/openapi/

## Files

- `openapi.yaml`: original spec from Figma
- `openapi.file.yaml`: document (node types) only spec (manually filtered)
- `openapi.rust.overrides.yaml`: manual schema overrides for Rust compatibility

## Pipeline Scripts

- `pipe.sh`: Main pipeline script (runs all steps)
- `pipe_outline.py`: Extract inline schemas from `openapi.file.yaml` → `piped/scope=file/openapi.file.outline.yaml`
- `pipe_rust_rm_type.py`: Process outlined spec for Rust/Serde compatibility → `piped/scope=file/openapi.file.outline.rust.yaml`

## Usage

Run the full pipeline:
```bash
cd openapi
./pipe.sh
```

Or run individual steps:
```bash
python3 pipe_outline.py        # Extract inline schemas from openapi.file.yaml
python3 pipe_rust_rm_type.py   # Process openapi.file.yaml for Rust
```

## Output Files

All processed files are written to `piped/scope=file/`:
- `openapi.file.outline.yaml`: Spec with extracted inline schemas (from `pipe_outline.py`)
- `openapi.file.outline.rust.yaml`: Rust-compatible spec ready for code generation (from `pipe_rust_rm_type.py`)

## Pipeline Flow

```
openapi.file.yaml
    ↓ [pipe_outline.py]
openapi.file.outline.yaml
    ↓ [pipe_rust_rm_type.py]
openapi.file.outline.rust.yaml (ready for code generation)
```

## Filtered Spec Details

**/v1/file only removed paths & models**

- /v1/analytics/\*
- /v1/payments/\*
- /v1/activity_logs/\*
- /v2/webhooks/\*
- /v2/teams/\*
- /v1/projects/\*
- /v1/me
- /v1/dev_resources
- /v1/files/{file_key}/variables/\*
- /v1/files/{file_key}/dev_resources/\*
- /v1/files/{file_key}/comments/\*
- /v1/files/{file_key}/versions/\*

Removed models:

- "_LibraryAnalytics_"
- "_DevResource_"
- "_Payment_"
- "_ActivityLog_"
- "_Webhook_"
- "_Comment_"
- "_Team_"
- "_Project_"
- "_DevStatus_"
- "Me"
