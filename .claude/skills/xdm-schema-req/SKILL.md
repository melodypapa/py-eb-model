---
name: xdm-schema-req
description: "Use when asked to generate requirements documents from XDM schema files; create or update SWR_*_MODELS.md documentation; extract AUTOSAR configuration parameter specifications from .xdm schema files; analyze EB Tresos schema definitions to produce structured requirements output. Designed for the py-eb-model project."
license: MIT
metadata:
  author: melodypapa
  repository: https://github.com/melodypapa/py-eb-model
  version: "1.0.0"
  keywords:
    - AUTOSAR
    - EB-Tresos
    - XDM
    - requirements
    - py-eb-model
    - schema
    - automotive
---

# XDM Schema Requirements Generator

Generates structured software requirements markdown from EB Tresos XDM schema files, following the conventions in `docs/requirements/`.

## Workflow

### 1. Extract Schema Data (token-efficient)

Run the project's XDM extractor tool to get compact JSON instead of parsing raw XML:

```bash
python .claude/skills/xdm-schema-req/scripts/extract_xdm_schema.py <path/to/schema.xdm>
```

The tool outputs JSON with all containers, fields, types, ranges, and enable conditions already resolved. Use `--pretty` for readable output during development.

**JSON structure you'll receive:**
```json
{
  "module": "Os",
  "stack": "core",
  "module_abbr": "OS",
  "output_path": "docs/requirements/core/models/swr_os_models.md",
  "containers": [
    {
      "name": "OsTask",
      "is_map": true,
      "fields": [
        {
          "name": "OsTaskPriority",
          "field_type": "var",
          "schema_type": "INTEGER",
          "req_type": "int",
          "origin": "AUTOSAR",
          "desc": "...",
          "enabled": true,
          "range": {"min": 0, "max": 2147483647}
        },
        {
          "name": "OsTaskSchedule",
          "field_type": "var",
          "schema_type": "ENUMERATION",
          "req_type": "OsTaskSchedule",
          "origin": "AUTOSAR",
          "desc": "...",
          "enabled": true,
          "enum_values": ["NON", "FULL"],
          "enum_default": "NON"
        },
        {
          "name": "OsTaskPeriod",
          "field_type": "var",
          "schema_type": "FLOAT",
          "req_type": "float",
          "origin": "AUTOSAR",
          "desc": "...",
          "enabled": true,
          "enable_xpath": "../OsTaskType = 'PERIODIC'",
          "range": {"min": 0.001, "max": 86400.0}
        }
      ],
      "sub_containers": [...]
    }
  ]
}
```

**Key JSON fields:**
- `enabled: false` → skip this field entirely (do NOT include it in the requirements table)
- `enabled: true` + `enable_xpath` → conditionally enabled; include it (without annotation)
- `req_type` → already mapped to Python type (use this directly)
- `range` → `{"min": N, "max": M}` already extracted
- `enum_values` / `enum_default` → already extracted
- `bool_default` → already extracted
- `output_path` → the file to write (do not compute it yourself)

### 2. Type Mapping (pre-resolved in JSON)

The `req_type` field in the JSON is already mapped. **Use it directly.** See `references/type_mapping.md` for the full mapping table and description formatting rules.

### 3. Generate Descriptions and Format Constraints

The `desc` field from JSON is the raw DESC text. **Never copy it verbatim.**

**Always synthesize a fresh 3–8 word description** using the field name and `req_type`:
- `OsTaskPriority (int)` → `"Relative task priority"`
- `OsCounterMaxAllowedValue (int)` → `"Max counter value in ticks"`
- `OsAlarmCounterRef (EcucRefType)` → `"Associated counter reference"`

If the DESC contains a useful 2–4 word phrase, reuse it. If it is a long specification paragraph, **ignore it entirely** and derive from the field name. Never use `...`.

**Format constraints in the description column:**
- Integer/float with range: append `(min-max)` — e.g., `"Task priority (0-2147483647)"`
- Enum: append `(VAL1/VAL2)` with default if present — e.g., `"Schedule type (NON/FULL, default NON)"`
- Boolean with default: append `(default true/false)`
- Ref: append `(reference to <target>)` if useful

### 4. Determine Output Path

Use the `output_path` field from the JSON directly. It is already computed.

### 5. Generate the Requirements Document

Follow the exact markdown templates in `templates/requirements_template.md`:
- **Document header** — title, document information table, overview
- **Entity requirement** — one per container (4-column field table: Field, Type, Description, Origin)
- **Choice container** — grouped summary (Step 6a) + per-variant requirements (Step 6b)
- **Root module requirement** — last requirement, with `**Methods:**` section only here
- **Traceability table** — final section linking requirement IDs to implementation and test cases

**Description formatting rules:**
- For integers with range: `"Field description (min-max)"`, e.g., `"Task priority (0-2147483647)"`
- For floats with range: `"Description (min-max)"`
- For enums: `"Description (VAL1/VAL2/VAL3)"` with default noted if present: `"Description (VAL1/VAL2, default VAL1)"`
- For booleans with default: `"Description (default true/false)"`
- For refs: `"Description (reference to target type)"`
- For ref lists: `"Description (list of target type)"`

**Type column rules — use `req_type` from JSON directly:**
- JSON `req_type` is already the correct Python class name — use it
- Sub-container → `<SubContainerName>` (its `name` from JSON)
- MAP sub-container in parent table → `List[<ContainerName>]`

**Skip fields** where JSON `enabled: false` (no `enable_xpath`). Fields with `enable_xpath` are conditionally enabled — include them silently (no annotation about the condition).

### 6. Handle Choice Containers (is_choice: true in JSON)

When a sub-container in JSON has `"is_choice": true` with a `variants` array, generate **one grouped summary requirement** listing all variant classes (Step 6a), followed by **individual requirements** for each variant that has fields (Step 6b). See `templates/requirements_template.md` for the exact template.

### 7. Add the Root Module Requirement

The last numbered requirement should be the root module container (e.g., `Os`) with methods for accessing all entity lists. See `templates/requirements_template.md`. The root methods follow the pattern `get<EntityName>List()` for each top-level entity.

### 8. Generate Traceability Table

See `templates/requirements_template.md`. Test case IDs follow the pattern `UTS_<MODULE_ABBR>_MODEL_<NNNNN>`.

### 9. Write the Output

Write the generated markdown to the determined output path. Create the directory if it doesn't exist. Display a summary at the end: number of requirements generated, output path, and any notable findings (skipped fields, unusual types, etc.).

## Edge Cases

- **Empty schemas**: If `containers` list is empty, report that no entity containers were detected.
- **Parameters without ORIGIN**: JSON defaults to `EB` if origin is absent — use the JSON value.
- **Descriptions**: The JSON `desc` has HTML already stripped. Still synthesize fresh 3-8 word description.
- **Unknown types**: Use the `req_type` value from JSON as-is (it will be the raw schema type).
- **Fields with `enabled: false`**: Skip — the JSON already resolved this. Do not include in table.

## Common Mistakes

See `references/mistakes.md` for the full anti-pattern catalogue.

## Reference Files

- `scripts/extract_xdm_schema.py` — The XDM schema extractor. **Always run this first** to get JSON input.
- `templates/requirements_template.md` — Exact markdown templates for all document sections.
- `references/type_mapping.md` — Schema type → Python type mapping and description format rules.
- `references/mistakes.md` — Anti-patterns and common errors to avoid.
- `references/stack_mapping.md` — AUTOSAR module → stack directory + abbreviation mapping (rarely needed; `output_path` in JSON is pre-computed).
