# Requirements Traceability Guide

## Overview

This document explains the requirements traceability system for py-eb-model, which implements ISO/IEC/IEEE 29148 compliant bidirectional traceability between software requirements and code implementations.

## Key Documents

| Document | Purpose |
|----------|---------|
| [requirements.md](requirements.md) | Central registry of all SWR documents |
| [traceability_matrix.md](traceability_matrix.md) | Complete requirements-to-code traceability |
| Individual SWR documents | Detailed requirements per module |

## Traceability Format

### Matrix Format
```
Requirement ID | Implementation Location | Files | Status | Last Validated
---------------|------------------------|-------|--------|---------------
SWR_OS_00001  | src/.../os_xdm_parser.py:OsXdmParser:46-80 | src/.../os_xdm_parser.py | Implemented | 2026-04-05
```

### Implementation Location Format
`file_path.py:ClassName:start_line-end_line`

### Status Values
- **Implemented**: Code meets requirement, verified
- **Pending**: Code exists but doesn't fully meet requirement
- **Draft**: Requirement written, not yet implemented
- **Deprecated**: Requirement no longer applies
- **Blocked**: Dependency not met

## Requirements ID Format

`SWR_<MODULE>_<NUMBER>`

| Component | Description | Examples |
|-----------|-------------|----------|
| SWR | Software Requirement identifier | All requirements |
| MODULE | Module abbreviation | OS, RTE, CANIF, etc. |
| NUMBER | 5-digit sequential number | 00001, 00002, etc. |

## Module Coverage

### Implemented (255 requirements)

| Category | Count | Modules |
|----------|-------|---------|
| Parser Layer | 6 | Abstract parser infrastructure |
| Core Modules | 45 | OS, RTE, NvM, EcuC, BswM, Det, EcuM, Tm, PbcfgM |
| CAN Stack | 20 | CanIf, CanNm, CanSM, CanTp |
| LIN Stack | 15 | LinIf, LinSM, LinTp |
| FlexRay Stack | 25 | FrIf, FrNm, FrSM, FrTp, FrArTp |
| Ethernet Stack | 45 | EthIf, EthSM, SoAd, TcpIp, UdpNm, DoIP, SomeIpTp |
| COM Stack | 16 | Com, ComM, PduR, IpduM, Nm, LdCom |
| Memory Stack | 28 | NvM, Ea, Fee, MemIf, MemMap, MemAcc, Crc |
| Crypto Stack | 16 | Crypto, CryIf, Csm, SecOC |
| Diagnostics Stack | 16 | FiM, Dcm, Dem, Dlt |
| J1939 Stack | 16 | J1939Dcm, J1939Nm, J1939Rm, J1939Tp |
| CLI Layer | 3 | Unified and module-specific commands |
| Reporter Layer | 4 | Excel reporter infrastructure |

## Usage

### Finding Code for a Requirement

1. Look up the requirement ID in [traceability_matrix.md](traceability_matrix.md)
2. Navigate to the implementation location
3. Use the line numbers to find the specific code

### Finding Requirements for Code

1. Use grep to search for the requirement ID in code
2. Check docstrings for "Implements: SWR_*" references
3. Cross-reference with traceability matrix

### Updating Traceability After Code Changes

1. Identify affected requirements using traceability matrix
2. Update `Implementation` field with new location
3. Update `Last Validated` date
4. Add entry to `Change Log` in requirement document

### Creating New Requirements

1. Generate new requirement ID using format above
2. Document in appropriate SWR file
3. Add to [requirements.md](requirements.md) registry
4. Add entry to traceability matrix
5. Update code with `Implements: SWR_*` docstring

## Verification Process

### Manual Verification

For each requirement:

1. Verify code location exists and is accessible
2. Verify code behavior matches requirement description
3. Execute verification criteria from requirement document
4. Check edge cases and error conditions
5. Update `Last Validated` date

### Automated Verification

The traceability matrix can be validated using:

```bash
# Check that all implementations exist
grep -E "^SWR_" docs/requirements/traceability_matrix.md | while read line; do
  # Extract and validate file paths
done
```

## Best Practices

### When Modifying Code

1. Check traceability matrix for affected requirements
2. Update requirement implementation locations if code moves
3. Re-verify affected requirements after changes
4. Document changes in requirement Change Log

### When Modifying Requirements

1. Identify code locations from traceability matrix
2. Update code to match new requirement
3. Update implementation location if needed
4. Re-verify all related requirements

### During Code Review

1. Verify code implements all referenced requirements
2. Check that `Implements:` docstrings are accurate
3. Ensure traceability matrix is updated
4. Verify change log entries are complete

## Common Patterns

### Docstring Reference
```python
class OsXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR OS module configuration from EB Tresos XDM files.

    Implements: SWR_OS_00001 (OS Module Parser)
    """

    def read_os_tasks(self, element: ET.Element, os: Os):
        """
        Parse all OsTask containers from XDM.

        Implements: SWR_OS_00002 (Task parsing)
        """
```

### Requirement Document Section
```markdown
### REQ-001: User Authentication

**Type:** Functional
**Priority:** Critical
**Status:** Implemented
**Implementation:** src/auth.py:authenticate_user (line 45)
**Last Validated:** 2026-04-05

**Description:**
System shall authenticate users using email and password credentials.

**Verification:**
1. Verify authenticate_user() function exists in src/auth.py:45
2. Verify email validation is performed
3. Verify password verification against stored hash
```

## Change Management

### Change Log Format
```markdown
## Change Log

### 2026-04-05

**SWR_OS_00001:** Updated parser to handle new XDM format
**Change Type:** Modified
**Previous:** Parser handled version 1.0 XDM format
**Updated:** Parser now handles version 2.0 XDM format
**Reason:** EB Tresos updated XDM schema
**Impact:** Requires updated test files
**Affected Files:** src/eb_model/parser/core/os_xdm_parser.py
**Dependencies:** SWR_PARSER_00003 (Value reading)
```

## Tools and Automation

### Verification Script
A verification script can be created to:

1. Validate all file paths exist
2. Check line numbers are accurate
3. Verify docstring references match matrix
4. Identify orphan code (code without requirements)
5. Identify requirements without implementation

### Export Formats

The traceability matrix can be exported to:

- **CSV**: For import into DOORS or other RM tools
- **Excel**: For non-technical stakeholders
- **JSON**: For automated processing
- **Markdown**: For documentation

## Related Standards

- **ISO/IEC/IEEE 29148**: Systems and software engineering — Life cycle processes — Requirements engineering
- **AUTOSAR**: Automotive open system architecture
- **EB Tresos**: Elektronikbit automotive configuration tool

## Questions

For questions about traceability, contact:

- Requirements Engineering Team
- Development Team
- Quality Assurance Team

---

**Document Version:** 1.0
**Last Updated:** 2026-04-05
**Maintained By:** py-eb-model Project