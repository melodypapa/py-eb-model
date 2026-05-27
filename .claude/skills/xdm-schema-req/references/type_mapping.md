# Type Mapping Reference

The `req_type` field in the JSON output from `scripts/extract_xdm_schema.py` is already mapped to the correct Python type. **Use it directly — do not remap.**

## Schema Type → Python Type

| schema_type in JSON | req_type in JSON |
|---------------------|-----------------|
| `ENUMERATION` | `<FieldName>` (e.g., `OsTaskSchedule`) or `<Container><Field>` if field lacks container prefix |
| `INTEGER` | `int` |
| `FLOAT` | `float` |
| `BOOLEAN` | `bool` |
| `REFERENCE` | `EcucRefType` or `List[EcucRefType]` |
| `FOREIGN-REFERENCE` | `EcucRefType` |
| `STRING` / `MULTILINE-STRING` / `FUNCTION-NAME` | `str` |

## Sub-containers

Sub-containers appear in `sub_containers` (not `fields`). If a sub-container `is_map: true`, its type in the parent requirements table is `List[<ContainerName>]`.

## Description Formatting Rules

| Field Type | Description Format |
|-----------|-------------------|
| Integer/float with range | `"Description (min-max)"` — e.g., `"Task priority (0-2147483647)"` |
| Enum | `"Description (VAL1/VAL2)"` with default if present: `"Description (VAL1/VAL2, default VAL1)"` |
| Boolean with default | `"Description (default true/false)"` |
| Reference | `"Description (reference to target type)"` if useful |
| Reference list | `"Description (list of target type)"` |
