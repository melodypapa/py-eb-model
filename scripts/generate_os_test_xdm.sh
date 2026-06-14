#!/bin/bash
# Generate OS XDM test file from schema
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

mkdir -p "$PROJECT_ROOT/tests/integration/data_files/generated_os"

model-xdm-generator \
    "$PROJECT_ROOT/doc/os/schema/Os.xdm" \
    -o "$PROJECT_ROOT/tests/integration/data_files/generated_os/Os.xdm" \
    --variant defaults

echo "Generated: tests/integration/data_files/generated_os/Os.xdm"
