#!/bin/bash
# Generate OS XDM test file from schema

mkdir -p "tests/integration/data_files/generated"

model-xdm-generator "doc/os/schema/Os.xdm" -o "tests/integration/data_files/generated/Os.xdm" --variant defaults
model-xdm-generator "doc/canif/schema/CanIf.xdm" -o "tests/integration/data_files/generated/CanIf.xdm" --variant defaults

