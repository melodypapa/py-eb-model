# System Modules Unit Test Cases

This document contains all unit test cases for the System modules (Det, EcuM, Tm, PbcfgM) following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_UNIT_DET_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_DET_00001 |
| Title | Det Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Det parser correctly validates the module name and extracts Default Error Tracer configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid Det.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid Det.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "Det" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_DET_00001 | Det Module Parsing | Covered |

---

# Test Case: TC_UNIT_DET_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_DET_00002 |
| Title | Det Model - General Configuration Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Det parser correctly extracts DetGeneral configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | DetGeneral configuration is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse DetGeneral configuration | Object created successfully |
| 2 | Verify configuration parameters | Values extracted correctly |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_DET_00002 | Det General Configuration | Covered |

---

# Test Case: TC_UNIT_ECUM_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_ECUM_00001 |
| Title | EcuM Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the EcuM parser correctly validates the module name and extracts ECU State Manager configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid EcuM.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid EcuM.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "EcuM" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ECUM_00001 | EcuM Module Parsing | Covered |

---

# Test Case: TC_UNIT_ECUM_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_ECUM_00002 |
| Title | EcuM Model - General Configuration Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the EcuM parser correctly extracts EcuMGeneral configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | EcuMGeneral configuration is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse EcuMGeneral configuration | Object created successfully |
| 2 | Verify configuration parameters | Values extracted correctly |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ECUM_00002 | EcuM General Configuration | Covered |

---

# Test Case: TC_UNIT_TM_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_TM_00001 |
| Title | Tm Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Tm parser correctly validates the module name and extracts Timer module configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid Tm.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid Tm.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "Tm" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_TM_00001 | Tm Module Parsing | Covered |

---

# Test Case: TC_UNIT_PBCFGM_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_PBCFGM_00001 |
| Title | PbcfgM Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the PbcfgM parser correctly validates the module name and extracts Post-Build Configuration Manager configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid PbcfgM.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid PbcfgM.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "PbcfgM" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_PBCFGM_00001 | PbcfgM Module Parsing | Covered |

---

# Test Case: TC_UNIT_DET_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_DET_00003 |
| Title | Det Reporter - Excel Worksheet Generation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Det reporter correctly generates Excel worksheets.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Det model objects are populated |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Generate Excel output | File created successfully |
| 2 | Verify worksheet content | All data populated correctly |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_DET_00003 | Det Excel Generation | Covered |

---

# Test Case: TC_UNIT_ECUM_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_ECUM_00003 |
| Title | EcuM Reporter - Excel Worksheet Generation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the EcuM reporter correctly generates Excel worksheets.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | EcuM model objects are populated |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Generate Excel output | File created successfully |
| 2 | Verify worksheet content | All data populated correctly |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ECUM_00003 | EcuM Excel Generation | Covered |