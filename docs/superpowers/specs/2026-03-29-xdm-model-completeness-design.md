# XDM Model Completeness Implementation Design

**Date:** 2026-03-29
**Status:** Approved
**Approach:** Parallel Multi-Module Implementation

## Executive Summary

This design implements complete coverage for seven AUTOSAR modules (Os, Rte, NvM, EcuC, EcuM, Det, Tm) to address 108 missing classes and 345 missing attributes identified in the XDM Model Analysis Report. The approach uses parallel agents working on independent modules simultaneously to maximize efficiency while maintaining quality.

## Architecture Overview

The implementation uses a three-layer architecture:

### Coordination Layer
- Master spec defining standardized patterns and conventions
- Work breakdown assigning modules to parallel agents
- Integration tests for cross-module consistency

### Implementation Layer (Parallel Agents)
- Each agent works on 1-2 modules independently
- Agents follow the master spec for consistency
- Each agent produces: model classes, parser updates, tests, completion metrics

### Verification Layer
- Integration verification that all modules parse successfully
- Analysis script re-run to confirm deviation reduction
- Cross-module reference validation

## Standardized Patterns Convention

### Model Class Patterns
- Classes inherit from `EcucParamConfContainerDef` (containers) or `EcucObject` (leaf objects)
- All attribute names use camelCase (matching XDM)
- Getter: `getAttributeName()` with return type hint
- Setter: `setAttributeName(value)` returns `self` for fluent chaining
- Reference attributes use `List[EcucRefType]` for 0..* multiplicity
- Multiplicity 0..1 uses Optional type
- Multiplicity 1 uses plain type

### Parser Patterns
- Each parser inherits from `AbstractEbModelParser`
- Use `read_value()` for mandatory attributes
- Use `read_optional_value()` for optional attributes
- Use `read_ref_value()` for single references
- Use `read_ref_value_list()` for 0..* references
- Use `find_ctr_tag()` and `find_ctr_tag_list()` for containers
- Register new container parsers in the module's `parse()` method

### Testing Patterns
- Unit tests for each model class: instantiation, getters/setters
- Parser tests: verify XDM → model object mapping
- Integration tests: parse complete XDM, verify all containers found

### Docstring Patterns
- Google-style docstrings
- Module-level: List all SWR IDs implemented in that module
- Class-level: Include the primary SWR ID for that class
- Method-level: Include SWR ID only for significant features
- SWR ID format: `SWR_<MODULE>_<NUMBER>` (e.g., `SWR_OS_00001`)
- Focus on **WHY** and non-obvious behavior

## Module Assignment Strategy

### Agent 1: Tm and Det
**Files:**
- `src/eb_model/models/tm_xdm.py`
- `src/eb_model/models/det_xdm.py`
- `src/eb_model/parser/tm_xdm_parser.py`
- `src/eb_model/parser/det_xdm_parser.py`
- `src/eb_model/tests/models/test_tm_xdm.py`
- `src/eb_model/tests/parser/test_tm_xdm_parser.py`
- `src/eb_model/tests/models/test_det_xdm.py`
- `src/eb_model/tests/parser/test_det_xdm_parser.py`

**Scope:**
- Tm: 3 XDM containers, 5 model classes, 2 missing classes
- Det: 8 XDM containers, 4 model classes, 7 missing classes
- Total: 11 containers, ~9 missing classes

### Agent 2: EcuC and NvM
**Files:**
- `src/eb_model/models/ecuc_xdm.py`
- `src/eb_model/models/nvm_xdm.py`
- `src/eb_model/parser/ecuc_xdm_parser.py`
- `src/eb_model/parser/nvm_xdm_parser.py`
- `src/eb_model/tests/models/test_ecuc_xdm.py`
- `src/eb_model/tests/parser/test_ecuc_xdm_parser.py`
- `src/eb_model/tests/models/test_nvm_xdm.py`
- `src/eb_model/tests/parser/test_nvm_xdm_parser.py`

**Scope:**
- EcuC: 14 XDM containers, 4 model classes, 12 missing classes
- NvM: 12 XDM containers, 8 model classes, 8 missing classes
- Total: 26 containers, ~20 missing classes

### Agent 3: Os
**Files:**
- `src/eb_model/models/os_xdm.py`
- `src/eb_model/parser/os_xdm_parser.py`
- `src/eb_model/tests/models/test_os_xdm.py`
- `src/eb_model/tests/parser/test_os_xdm_parser.py`

**Scope:**
- Os: 38 XDM containers, 36 model classes, 10 missing classes
- Most existing structure is in place, primarily adding attributes

### Agent 4: EcuM and Rte
**Files:**
- `src/eb_model/models/ecum_xdm.py`
- `src/eb_model/models/rte_xdm.py`
- `src/eb_model/parser/ecum_xdm_parser.py`
- `src/eb_model/parser/rte_xdm_parser.py`
- `src/eb_model/tests/models/test_ecum_xdm.py`
- `src/eb_model/tests/parser/test_ecum_xdm_parser.py`
- `src/eb_model/tests/models/test_rte_xdm.py`
- `src/eb_model/tests/parser/test_rte_xdm_parser.py`

**Scope:**
- EcuM: 31 XDM containers, 5 model classes, 30 missing classes
- Rte: 44 XDM containers, 12 model classes, 39 missing classes
- Total: 75 containers, ~69 missing classes

## Detailed Work Breakdown

Each agent executes these steps:

### Step 1: Preparation
- Read the analysis report to identify missing classes for assigned modules
- Read existing model file and parser file to understand current state
- Read XDM definition file to verify container structure
- Plan implementation order

### Step 2: Model Class Implementation
- For each missing class: create class definition, add attributes with getters/setters
- For each existing class with missing attributes: add missing attributes
- Follow patterns convention strictly
- Add type hints and docstrings

### Step 3: Parser Implementation
- For each new container: add parsing method
- For each new attribute in existing containers: add value reading
- Register container parsing in main `parse()` method
- Handle optional/mandatory/enable attributes correctly

### Step 4: Testing
- Create/update unit tests for model classes
- Create/update parser tests with sample XDM fragments
- Verify all tests pass

### Step 5: Verification
- Run linter and fix any issues
- Manually verify against analysis report checklist
- Run tests: `pytest`

### Step 6: Deliverable
- Create completion summary document

## Verification and Quality Gates

### Code Quality Gates
- All new classes follow the patterns convention
- No linting errors (flake8 passes with project standard)
- Type hints on all public methods
- Docstrings on all classes and significant methods (Google style)

### Functional Verification
- All XDM containers from analysis report are implemented
- Parser successfully parses reference XDM file without errors
- All container elements are accessible via model hierarchy
- Reference attributes properly use `EcucRefType`

### Cross-Module Validation
- No naming conflicts between modules
- Consistent multiplicity handling (0..* → List, 0..1 → Optional)
- Imports organized correctly per project convention
- Module exports updated in `__init__.py` if needed

### Integration Verification (After All Agents Complete)
- Re-run analysis script: missing classes should drop from 108 to 0
- Re-run analysis script: missing attributes should drop from 345 to target (near 0)
- All module parsers successfully parse their respective XDM files
- Unit tests pass: `pytest src/eb_model/tests/`

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Pattern divergence across agents | Master spec defines conventions upfront; integration verification catches issues |
| XDM definition differences between EB Tresos versions | Use reference XDM files from analysis report; handle version-specific attributes as optional |
| Cross-module reference dependencies | Implement basic classes first; add reference parsing after all modules are complete |
| Missing edge cases in existing code | Document discovered issues; create tracking issues for future fixes |

### Contingency Plans
- If an agent discovers a blocking issue: pause that module, document the issue, continue with other modules
- If integration reveals conflicts: prioritize analytical completeness (parser works) over code perfection
- If timeline extends: complete high-priority modules first (Tm, Det, EcuC, NvM)

## Success Metrics

### Primary Metrics
- Missing classes: 108 → 0 (100% coverage)
- Missing attributes: 345 → <10 (near 100% coverage)
- All module parsers: 7/7 successfully parse XDM files

### Secondary Metrics
- Test coverage: >90% for new code
- Linting: 0 errors, 0 warnings
- Documentation: All new classes have docstrings

### Definition of Done
- Analysis script confirms 108 missing classes resolved
- Analysis script confirms <10 missing attributes remaining
- All tests pass: `pytest`
- All lint checks pass

## Tools and Resources

### Required Resources
- Access to XDM definition files (locations specified in analysis report)
- Reference XDM files for each module (for testing)
- Analysis script for verification

### Tools Used
- `superpowers:dispatching-parallel-agents` for coordination
- `pytest` for testing
- `flake8` for linting
- Existing analysis script for verification

### Documentation Resources
- Analysis report: `XDM_MODEL_ANALYSIS_REPORT.md`
- Project conventions: `CLAUDE.md`
- Existing code patterns in `src/eb_model/models/` and `src/eb_model/parser/`

## Documentation and Handoff

### Per Agent Deliverables
- Updated model class file
- Updated parser file
- Updated/created test file
- Completion summary document

### Master Deliverables
- Updated analysis report with post-implementation results
- Integration test suite covering all modules
- Patterns convention document (this spec)

### Documentation Locations
- Each new class gets Google-style docstring with "Implements: SWR_*" reference
- Parsing logic documented in parser methods
- Completion summaries stored in `docs/superpowers/completion/`

## Missing Class Reference

### Os Module (10 missing classes)
1. OsHwIncrementer - Hardware incrementer configuration
2. OsEvent - Event synchronization primitive
3. OsSpinlock - Spinlock synchronization primitive
4. OsPeripheralArea - Peripheral memory area configuration
5. OsOS - OS-level configuration
6. OsHooks - OS hook configuration
7. OsCoreConfig - Multi-core configuration
8. OsAutosarCustomization - AUTOSAR-specific customizations
9. CommonPublishedInformation - Published metadata
10. PublishedInformation - Module-specific metadata

### Rte Module (39 missing classes)
RteBswGeneral, RteBswEventToIsrMapping, RteBswExclusiveAreaImpl, RteBswExternalTriggerConfig, RteBswInternalTriggerConfig, RteBswRequiredModeGroupConnection, RteBswRequiredSenderReceiverConnection, RteBswRequiredClientServerConnection, RteBswRequiredTriggerConnection, RteGeneration, ComTaskConfiguration, BswConfiguration, OsCounterAssignments, CooperativeTasks, TaskChain, RteImplicitCommunication, RteInitializationBehavior, RteInitializationRunnableBatch, RteOsInteraction, RteModeToScheduleTableMapping, RteRips, DataMappings, RteExclusiveAreaImplementation, RteExternalTriggerConfig, RteInternalTriggerConfig, RteNvRamAllocation, RteSwComponentType, CommonPublishedInformation, PublishedInformation, plus other metadata classes.

### NvM Module (8 missing classes)
CommonPublishedInformation, NvMDefensiveProgramming, NvMCommonCryptoSecurityParameters, NvMServiceAPI, NvmDemEventParameterRefs, ReportToDem, MultiCoreCallout, PublishedInformation.

### EcuC Module (12 missing classes)
CommonPublishedInformation, EcucGeneral, EcucHardware, EcucCoreDefinition, EcucPduCollection, MetaDataType, MetaDataItem, Pdu, EcucPduDedicatedPartition, EcucPostBuildVariants, EcucVariationResolver, PublishedInformation.

### EcuM Module (30 missing classes)
EcuMCommonConfiguration, EcuMDefaultShutdownTarget, EcuMDriverInitListOne, EcuMDriverInitItem, EcuMDriverInitListZero, EcuMDriverRestartList, EcuMSleepMode, EcuMWakeupSource, EcuMDemEventParameterRefs, EcuMFixedConfiguration, EcuMDriverInitListThree, EcuMDriverInitListTwo, EcuMFixedUserConfig, EcuMTTII, EcuMWdgM, EcuMFlexConfiguration, EcuMAlarmClock, EcuMFlexUserConfig, EcuMGoDownAllowedUsers, EcuMResetMode, EcuMSetClockAllowedUsers, EcuMShutdownCause, EcuMShutdownTarget, EcuMDefensiveProgramming, EcuMFixedGeneral, EcuMFlexGeneral, EcuMServiceAPI, ReportToDem, CommonPublishedInformation, PublishedInformation.

### Det Module (7 missing classes)
CommonPublishedInformation, DetServiceAPI, DetNotification, DetDefensiveProgramming, SoftwareComponentList, InstanceIdList, PublishedInformation.

### Tm Module (2 missing classes)
CommonPublishedInformation, PublishedInformation.

## Notes

- This design prioritizes analytical completeness for parsing and data extraction
- Timeline is flexible to ensure quality over speed
- All work follows existing codebase patterns and conventions
- No refactoring unrelated to missing classes/attributes
- Each agent works independently with minimal coordination needed
- Integration phase validates cross-module consistency after all agents complete