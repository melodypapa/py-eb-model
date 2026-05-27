# xdm-schema-req

EB Tresos XDM schema to AUTOSAR model-layer requirements generator for the py-eb-model project. v1.0.0

## Purpose

Generate structured software requirements markdown (`SWR_*_MODELS.md`) from EB Tresos XDM schema files, following the conventions in `docs/requirements/`.

**Core principle:** Run the extractor first. Never parse raw XML manually.

## When to Use

- Generating `SWR_*_MODELS.md` requirements documents for AUTOSAR modules
- Creating or updating model-layer requirements from XDM schema files
- Extracting AUTOSAR configuration parameter specifications
- Analyzing EB Tresos schema definitions to produce structured output

## What It Does

- Runs `scripts/extract_xdm_schema.py` to parse XDM schema into compact JSON (~10x smaller than raw XML)
- Maps schema types to Python types (`INTEGER` → `int`, `ENUMERATION` → class name, `REFERENCE` → `EcucRefType`)
- Generates numbered requirements (`SWR_<MODULE_ABBR>_MODELS_<NNNNN>`) for each model class
- Handles MAP containers, choice containers, sub-containers, and the root module class
- Writes output to the pre-computed `output_path` from the JSON (e.g., `docs/requirements/core/models/swr_os_models.md`)
- Produces a traceability table linking each requirement to its implementation and test cases

## Quick Start

```bash
# Extract schema data first
python .claude/skills/xdm-schema-req/scripts/extract_xdm_schema.py data/Os_schema.xdm --pretty

# Then ask the agent to generate the requirements document
# The agent will run the extractor and write the .md file automatically
```

## Input

An EB Tresos XDM schema file (`.xdm`). Pass its path when invoking the skill.

## Output

A markdown requirements document written to `docs/requirements/<stack>/models/swr_<module>_models.md`.

| Module | Output Path |
|--------|-------------|
| Os | `docs/requirements/core/models/swr_os_models.md` |
| CanIf | `docs/requirements/can_stack/models/swr_canif_models.md` |
| NvM | `docs/requirements/mem_stack/models/swr_nvm_models.md` |
| EthIf | `docs/requirements/eth_stack/models/swr_ethif_models.md` |

The `output_path` is pre-computed in the JSON — the agent uses it directly.

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Main skill instructions (loaded by AI agent) |
| `scripts/extract_xdm_schema.py` | XDM schema extractor — produces compact JSON from raw XDM |
| `templates/requirements_template.md` | Document, entity, choice, root, and traceability templates |
| `references/mistakes.md` | Anti-patterns that produce incorrect requirements docs |
| `references/type_mapping.md` | Schema type → Python type mapping with description format rules |
| `references/stack_mapping.md` | AUTOSAR module → stack directory + abbreviation mapping |
| `evals/evals.json` | Evaluation test cases with assertions |

## Changelog

### v1.0.0 — 2026-05-27

- Initial skill with 9-step workflow: extract → type-map → describe → path → generate → choice → root → traceability → write
- `scripts/extract_xdm_schema.py` handles all XML complexity (namespaces, ENABLE, RANGE, DESC, ORIGIN)
- Support for MAP containers, choice containers (`is_choice`), sub-containers, and enabled/disabled fields
- Common mistakes reference and type mapping reference extracted to `references/`
- Requirements templates extracted to `templates/`
