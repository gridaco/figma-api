#!/bin/bash
# Pipeline script to process OpenAPI specs for Rust code generation
#
# This script orchestrates all preprocessing steps in order:
# 1. pipe_outline.py - Extract inline schemas to named schemas
# 2. pipe_rust_rm_type.py - Process spec for Rust/Serde compatibility

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Configuration
INPUT_FILE="openapi.file.yaml"
OUTPUT_DIR="piped/scope=file"
OUTLINE_OUTPUT="${OUTPUT_DIR}/openapi.file.outline.yaml"
RUST_OUTPUT="${OUTPUT_DIR}/openapi.file.outline.rust.yaml"
OVERRIDES_FILE="openapi.rust.overrides.yaml"

echo "🚀 Starting OpenAPI pipeline..."
echo ""

# Step 1: Extract inline schemas
if [ ! -f "$INPUT_FILE" ]; then
    echo "❌ Error: $INPUT_FILE not found"
    echo "   This file is required for the pipeline"
    exit 1
fi

echo "📋 Step 1: Extracting inline schemas..."
python3 pipe_outline.py "$INPUT_FILE" "$OUTLINE_OUTPUT"
echo ""

# Step 2: Process for Rust compatibility
if [ ! -f "$OUTLINE_OUTPUT" ]; then
    echo "❌ Error: $OUTLINE_OUTPUT not found after Step 1"
    exit 1
fi

echo "🔧 Step 2: Processing for Rust/Serde compatibility..."
if [ -f "$OVERRIDES_FILE" ]; then
    python3 pipe_rust_rm_type.py "$OUTLINE_OUTPUT" "$RUST_OUTPUT" --overrides "$OVERRIDES_FILE"
else
    python3 pipe_rust_rm_type.py "$OUTLINE_OUTPUT" "$RUST_OUTPUT"
fi
echo ""

echo "✅ Pipeline complete!"
echo ""
echo "📁 Output files:"
echo "   - piped/scope=file/openapi.file.outline.rust.yaml (ready for code generation)"
if [ -f "piped/scope=file/openapi.file.outline.yaml" ]; then
    echo "   - piped/scope=file/openapi.file.outline.yaml (with extracted schemas)"
fi
echo ""
echo "🎯 Next step: Generate Rust code with:"
echo "   openapi-generator-cli generate \\"
echo "     -i openapi/piped/scope=file/openapi.file.outline.rust.yaml \\"
echo "     -c openapi/config.json \\"
echo "     -g rust \\"
echo "     -t ./templates \\"
echo "     -o figma_rest_api_file"

