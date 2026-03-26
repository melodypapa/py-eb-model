# Requirement Management

Manage AUTOSAR project requirements with traceability to code, tests, and documentation.

## Actions

When the user runs `/req`, help manage requirements based on `$ARGUMENTS`:

### Add New Requirement
- Add requirement to `docs/requirements/requirements.md`
- Assign stable ID: `SWR_<MODULE>_<NUMBER>` (next available number per module)
- Include required sections:
  - Title
  - Maturity (draft/accept/invalid)
  - Description
- Link to related code and tests

### Update Requirement Maturity
- Change maturity level (draft → accept → invalid)
- Document why the change was made
- Never change the requirement ID

### Traceability Check
- Search code for requirement ID references in docstrings
- Verify tests reference requirements they validate
- Check CLAUDE.md for requirement listings
- Report any orphaned requirements or missing traceability

### Requirement Formats

**Requirements**: `SWR_<MODULE>_<NUMBER>`
- Example: `SWR_OS_00001`, `SWR_RTE_00001`, `SWR_CANIF_00001`
- Each module has its own sequence starting from 00001

**Tests**: `SWUT_<MODULE>_<NUMBER>`
- Example: `SWUT_MODEL_00001`, `SWUT_PARSER_00002`

**Coding Rules**: `CODING_RULE_<CATEGORY>_<NUMBER>`
- Example: `CODING_RULE_IMPORT_00001`, `CODING_RULE_STYLE_00003`

**Maturity Levels**:
- **draft**: Newly created, under review, or not yet implemented
- **accept**: Accepted, implemented, and validated
- **invalid**: Deprecated, superseded, or no longer applicable

## Critical Rules

**STABLE IDs ARE PERMANENT**
- Once assigned, requirement IDs must NEVER be changed
- Even if the requirement is removed or superseded
- Use the next available number for new requirements
- Never reuse a deleted ID

## Usage Examples

```
/req add SWR_OS_00021 "Add support for memory protection regions"
/req update SWR_RTE_00005 maturity accept
/req check traceability
/req list draft
/req search parser
```

## Requirements by Module

### Core Modules
- **OS**: SWR_OS_00001+
- **RTE**: SWR_RTE_00001+
- **NvM**: SWR_NVM_00001+
- **EcuC**: SWR_ECUC_00001+
- **BswM**: SWR_BSWM_00001+

### CAN Communication Stack
- **CanIf**: SWR_CANIF_00001+
- **CanNm**: SWR_CANNM_00001+
- **CanSm**: SWR_CANSM_00001+
- **CanTp**: SWR_CANTP_00001+

### LIN Communication Stack
- **LinIf**: SWR_LINIF_00001+
- **LinSm**: SWR_LINSM_00001+
- **LinTp**: SWR_LINTP_00001+

### System Modules
- **Det**: SWR_DET_00001+
- **EcuM**: SWR_ECUM_00001+
- **Tm**: SWR_TM_00001+
- **PbcfgM**: SWR_PBCFGM_00001+

### Infrastructure Layers
- **Parser**: SWR_PARSER_00001+
- **Reporter**: SWR_REPORTER_00001+
- **CLI**: SWR_CLI_00001+

## References

- Requirements registry: `docs/requirements/requirements.md`
- Project instructions: `CLAUDE.md`