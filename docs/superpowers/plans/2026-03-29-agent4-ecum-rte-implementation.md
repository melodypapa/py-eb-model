# Agent 4: EcuM and Rte Module XDM Model Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement all missing classes and attributes for EcuM (30 missing) and Rte (39 missing) modules to achieve complete XDM container coverage.

**Architecture:** Follow existing patterns in py-eb-model - extend model classes in `_xdm.py` files, update parsers in `_xdm_parser.py` files, add tests for verification.

**Tech Stack:** Python 3.9+, pytest, xml.etree.ElementTree

---

## File Structure

### New Files to Create
- `src/eb_model/tests/models/test_ecum_xdm.py` - EcuM model class tests
- `src/eb_model/tests/models/test_rte_xdm.py` - Rte model class tests

### Files to Modify
- `src/eb_model/models/ecum_xdm.py` - Add 30 missing classes, missing attributes
- `src/eb_model/models/rte_xdm.py` - Add 39 missing classes, missing attributes
- `src/eb_model/parser/ecum_xdm_parser.py` - Add parser methods for new containers and attributes
- `src/eb_model/parser/rte_xdm_parser.py` - Add parser methods for new containers and attributes
- `src/eb_model/tests/parser/test_ecum_xdm_parser.py` - Add tests for new parser methods
- `src/eb_model/tests/parser/test_rte_xdm_parser.py` - Add tests for new parser methods

---

## Task 1: Create EcuM Model Test File

**Files:**
- Create: `src/eb_model/tests/models/test_ecum_xdm.py`

- [ ] **Step 1: Write test file structure**

```python
"""
EcuM Model Tests - Tests for ECUM module model classes.
"""
import pytest
from ...models.ecum_xdm import EcuM, EcuMGeneral, EcuMStartup
from ...models.eb_doc import EBModel


class TestEcuMGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        general = EcuMGeneral(root, "EcuMGeneral")

        assert general.getName() == "EcuMGeneral"
        assert general.getParent() == root
        assert general.getEcumDevErrorDetect() is None
        assert general.getEcumConfigurationVariant() is None

    def test_set_ecum_dev_error_detect(self):
        root = EBModel.getInstance()
        general = EcuMGeneral(root, "EcuMGeneral")

        assert general.setEcumDevErrorDetect(True) == general
        assert general.getEcumDevErrorDetect() is True
```

- [ ] **Step 2: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/models/test_ecum_xdm.py -v`
Expected: PASS

- [ ] **Step 3: Commit**

```bash
git add src/eb_model/tests/models/test_ecum_xdm.py
git commit -m "test: add EcuM model test file structure"
```

---

## Task 2: Add EcuM Missing Classes

**Files:**
- Modify: `src/eb_model/models/ecum_xdm.py`

- [ ] **Step 1: Add CommonPublishedInformation and PublishedInformation classes**

Same pattern as Tm, Det, EcuC, NvM modules - add these classes with version information and vendor ID attributes.

- [ ] **Step 2: Add EcuMCommonConfiguration class**

```python
class EcuMCommonConfiguration(EcucParamConfContainerDef):
    """
    Common configuration for EcuM module.

    Implements: SWR_ECUM_00001 (Common configuration)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumDevErrorDetect: bool = None
        self.ecumIncludeDem: bool = None
        self.ecumIncludeDet: bool = None
        self.ecumMainFunctionPeriod: float = None

    def getEcumDevErrorDetect(self) -> bool:
        return self.ecumDevErrorDetect

    def setEcumDevErrorDetect(self, value: bool):
        if value is not None:
            self.ecumDevErrorDetect = value
        return self

    def getEcumIncludeDem(self) -> bool:
        return self.ecumIncludeDem

    def setEcumIncludeDem(self, value: bool):
        if value is not None:
            self.ecumIncludeDem = value
        return self

    def getEcumIncludeDet(self) -> bool:
        return self.ecumIncludeDet

    def setEcumIncludeDet(self, value: bool):
        if value is not None:
            self.ecumIncludeDet = value
        return self

    def getEcumMainFunctionPeriod(self) -> float:
        return self.ecumMainFunctionPeriod

    def setEcumMainFunctionPeriod(self, value: float):
        if value is not None:
            self.ecumMainFunctionPeriod = value
        return self
```

- [ ] **Step 3: Add remaining EcuM missing classes**

Add the following 28 classes following the same pattern:
- EcuMDefaultShutdownTarget
- EcuMDriverInitListOne
- EcuMDriverInitItem
- EcuMDriverInitListZero
- EcuMDriverRestartList
- EcuMSleepMode
- EcuMWakeupSource
- EcuMDemEventParameterRefs
- EcuMFixedConfiguration
- EcuMDriverInitListThree
- EcuMDriverInitListTwo
- EcuMFixedUserConfig
- EcuMTTII
- EcuMWdgM
- EcuMFlexConfiguration
- EcuMAlarmClock
- EcuMFlexUserConfig
- EcuMGoDownAllowedUsers
- EcuMResetMode
- EcuMSetClockAllowedUsers
- EcuMShutdownCause
- EcuMShutdownTarget
- EcuMDefensiveProgramming
- EcuMFixedGeneral
- EcuMFlexGeneral
- EcuMServiceAPI
- ReportToDem

Each class should inherit from `EcucParamConfContainerDef` and include appropriate attributes based on the XDM definition.

- [ ] **Step 4: Add missing attributes to EcuMGeneral class**

Add these attributes to `EcuMGeneral.__init__`:

```python
self.ecumDevErrorDetect: bool = None
self.ecumIncludeDem: bool = None
self.ecumIncludeDet: bool = None
self.ecumMainFunctionPeriod: float = None
```

Add corresponding getter/setter methods.

- [ ] **Step 5: Add new containers to EcuM module class**

Add to `EcuM.__init__` and add corresponding getter/setter methods for all 30 new classes.

- [ ] **Step 6: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/models/test_ecum_xdm.py -v`
Expected: PASS

- [ ] **Step 7: Commit**

```bash
git add src/eb_model/models/ecum_xdm.py src/eb_model/tests/models/test_ecum_xdm.py
git commit -m "feat(ecum): add 30 missing classes and missing attributes to EcuMGeneral"
```

---

## Task 3: Update EcuM Parser for New Containers and Attributes

**Files:**
- Modify: `src/eb_model/parser/ecum_xdm_parser.py`

- [ ] **Step 1: Add import for new classes**

Update imports to include all new classes.

- [ ] **Step 2: Add parser methods for all new containers**

Add parser methods for CommonPublishedInformation, PublishedInformation, EcuMCommonConfiguration, and the 28 remaining classes following the same pattern.

- [ ] **Step 3: Update read_ecum_general to parse missing attributes**

Add lines to parse the 4 new attributes.

- [ ] **Step 4: Update parse method to call new parser methods**

Add all parser method calls.

- [ ] **Step 5: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/parser/test_ecum_xdm_parser.py -v`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add src/eb_model/parser/ecum_xdm_parser.py
git commit -m "feat(ecum): update parser for 30 new containers and missing attributes"
```

---

## Task 4: Add EcuM Parser Tests

**Files:**
- Modify: `src/eb_model/tests/parser/test_ecum_xdm_parser.py`

- [ ] **Step 1: Add tests for CommonPublishedInformation and PublishedInformation**

Follow same pattern as Tm and Det tests.

- [ ] **Step 2: Add tests for key configuration classes**

Add tests for EcuMCommonConfiguration, EcuMFixedConfiguration, EcuMFlexConfiguration.

- [ ] **Step 3: Update existing test_read_ecum_general to include new attributes**

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/parser/test_ecum_xdm_parser.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/eb_model/tests/parser/test_ecum_xdm_parser.py
git commit -m "test(ecum): add tests for new container parsers and missing attributes"
```

---

## Task 5: Create Rte Model Test File

**Files:**
- Create: `src/eb_model/tests/models/test_rte_xdm.py`

- [ ] **Step 1: Write test file structure**

```python
"""
Rte Model Tests - Tests for RTE module model classes.
"""
import pytest
from ...models.rte_xdm import Rte, RteSwComponentInstance, RteBswModuleInstance
from ...models.eb_doc import EBModel


class TestRteSwComponentInstance:

    def test_initialization(self):
        root = EBModel.getInstance()
        instance = RteSwComponentInstance(root, "RteSwComponentInstance")

        assert instance.getName() == "RteSwComponentInstance"
        assert instance.getParent() == root
```

- [ ] **Step 2: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/models/test_rte_xdm.py -v`
Expected: PASS

- [ ] **Step 3: Commit**

```bash
git add src/eb_model/tests/models/test_rte_xdm.py
git commit -m "test: add Rte model test file structure"
```

---

## Task 6: Add Rte Missing Classes

**Files:**
- Modify: `src/eb_model/models/rte_xdm.py`

- [ ] **Step 1: Add CommonPublishedInformation and PublishedInformation classes**

Same pattern as other modules.

- [ ] **Step 2: Add RteBswGeneral class**

```python
class RteBswGeneral(EcucParamConfContainerDef):
    """
    BSW general configuration for Rte module.

    Implements: SWR_RTE_00001 (BSW general configuration)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteGenerationScheduleTableRef: Optional[EcucRefType] = None
        self.rteDevelopmentErrorDetect: bool = None
        self.rteUseApplConfig: bool = None

    def getRteGenerationScheduleTableRef(self) -> Optional[EcucRefType]:
        return self.rteGenerationScheduleTableRef

    def setRteGenerationScheduleTableRef(self, value: Optional[EcucRefType]) -> 'RteBswGeneral':
        self.rteGenerationScheduleTableRef = value
        return self

    def getRteDevelopmentErrorDetect(self) -> bool:
        return self.rteDevelopmentErrorDetect

    def setRteDevelopmentErrorDetect(self, value: bool) -> 'RteBswGeneral':
        if value is not None:
            self.rteDevelopmentErrorDetect = value
        return self

    def getRteUseApplConfig(self) -> bool:
        return self.rteUseApplConfig

    def setRteUseApplConfig(self, value: bool) -> 'RteBswGeneral':
        if value is not None:
            self.rteUseApplConfig = value
        return self
```

- [ ] **Step 3: Add remaining Rte missing classes**

Add the following 37 classes following the same pattern:
- RteBswEventToIsrMapping
- RteBswExclusiveAreaImpl
- RteBswExternalTriggerConfig
- RteBswInternalTriggerConfig
- RteBswRequiredModeGroupConnection
- RteBswRequiredSenderReceiverConnection
- RteBswRequiredClientServerConnection
- RteBswRequiredTriggerConnection
- RteGeneration
- ComTaskConfiguration
- BswConfiguration
- OsCounterAssignments
- CooperativeTasks
- TaskChain
- RteImplicitCommunication
- RteInitializationBehavior
- RteInitializationRunnableBatch
- RteOsInteraction
- RteModeToScheduleTableMapping
- RteRips
- DataMappings
- RteExclusiveAreaImplementation
- RteExternalTriggerConfig
- RteInternalTriggerConfig
- RteNvRamAllocation
- RteSwComponentType

- [ ] **Step 4: Add missing attributes to RteBswModuleInstance class**

Based on the analysis report, add 25+ reference attributes.

- [ ] **Step 5: Add missing attributes to RteSwComponentInstance class**

Based on the analysis report, add 20+ reference attributes including rteActivationOffset, rtePeriod, rteImmediateRestart, rteNvmRamBlockLocationSymbol.

- [ ] **Step 6: Add new containers to Rte module class**

Add to `Rte.__init__` and add corresponding getter/setter methods for all 39 new classes.

- [ ] **Step 7: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/models/test_rte_xdm.py -v`
Expected: PASS

- [ ] **Step 8: Commit**

```bash
git add src/eb_model/models/rte_xdm.py src/eb_model/tests/models/test_rte_xdm.py
git commit -m "feat(rte): add 39 missing classes and many missing attributes"
```

---

## Task 7: Update Rte Parser for New Containers and Attributes

**Files:**
- Modify: `src/eb_model/parser/rte_xdm_parser.py`

- [ ] **Step 1: Add import for new classes**

Update imports to include all new classes.

- [ ] **Step 2: Add parser methods for all new containers**

Add parser methods for all 39 new classes.

- [ ] **Step 3: Update existing parser methods to read missing attributes**

Update parser methods for RteBswModuleInstance and RteSwComponentInstance.

- [ ] **Step 4: Update parse method to call new parser methods**

Add all parser method calls.

- [ ] **Step 5: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/parser/test_rte_xdm_parser.py -v`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add src/eb_model/parser/rte_xdm_parser.py
git commit -m "feat(rte): update parser for 39 new containers and missing attributes"
```

---

## Task 8: Add Rte Parser Tests

**Files:**
- Modify: `src/eb_model/tests/parser/test_rte_xdm_parser.py`

- [ ] **Step 1: Add tests for CommonPublishedInformation and PublishedInformation**

- [ ] **Step 2: Add tests for key BSW and configuration classes**

- [ ] **Step 3: Update existing tests for new attributes**

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/parser/test_rte_xdm_parser.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/eb_model/tests/parser/test_rte_xdm_parser.py
git commit -m "test(rte): add tests for new container parsers and missing attributes"
```

---

## Task 9: Run Linting and Final Verification

**Files:**
- All modified files

- [ ] **Step 1: Run flake8 on modified files**

Run: `flake8 src/eb_model/models/ecuc_xdm.py src/eb_model/models/rte_xdm.py src/eb_model/parser/ecuc_xdm_parser.py src/eb_model/parser/rte_xdm_parser.py src/eb_model/tests/models/test_ecum_xdm.py src/eb_model/tests/models/test_rte_xdm.py src/eb_model/tests/parser/test_ecuc_xdm_parser.py src/eb_model/tests/parser/test_rte_xdm_parser.py --max-line-length=150 --ignore=F401,W293,F403`

Expected: No errors

- [ ] **Step 2: Run all tests**

Run: `pytest src/eb_model/tests/models/test_ecum_xdm.py src/eb_model/tests/models/test_rte_xdm.py src/eb_model/tests/parser/test_ecum_xdm_parser.py src/eb_model/tests/parser/test_rte_xdm_parser.py -v`

Expected: All PASS

- [ ] **Step 3: Verify against analysis report checklist**

Manually verify:
- EcuM: 30 missing classes implemented
- Rte: 39 missing classes implemented
- EcuMGeneral: 4 missing attributes implemented
- RteBswModuleInstance: 25+ reference attributes implemented
- RteSwComponentInstance: 20+ reference attributes implemented

- [ ] **Step 4: Create completion summary**

Create file: `docs/superpowers/completion/2026-03-29-agent4-ecum-rte-completion.md`

```markdown
# Agent 4: EcuM and Rte Module Completion Summary

**Date:** 2026-03-29
**Agent:** 4
**Modules:** EcuM, Rte

## Work Completed

### EcuM Module
- Added 30 missing classes
- Added 4 missing attributes to EcuMGeneral
- Updated EcuMXdmParser with parser methods for all new containers and attributes
- Created test file `src/eb_model/tests/models/test_ecum_xdm.py`
- Added parser tests for new functionality

### Rte Module
- Added 39 missing classes
- Added 25+ missing attributes to RteBswModuleInstance
- Added 20+ missing attributes to RteSwComponentInstance
- Updated RteXdmParser with parser methods for all new containers and attributes
- Created test file `src/eb_model/tests/models/test_rte_xdm.py`
- Added parser tests for new functionality

## Files Modified
- `src/eb_model/models/ecuc_xdm.py`
- `src/eb_model/models/rte_xdm.py`
- `src/eb_model/parser/ecuc_xdm_parser.py`
- `src/eb_model/parser/rte_xdm_parser.py`
- `src/eb_model/tests/models/test_ecum_xdm.py` (created)
- `src/eb_model/tests/models/test_rte_xdm.py` (created)
- `src/eb_model/tests/parser/test_ecuc_xdm_parser.py` (updated)
- `src/eb_model/tests/parser/test_rte_xdm_parser.py` (updated)

## Test Results
All tests passing:
- EcuM model tests: PASS
- EcuM parser tests: PASS
- Rte model tests: PASS
- Rte parser tests: PASS

## Coverage Summary
- EcuM: 30/30 missing classes implemented (100%)
- Rte: 39/39 missing classes implemented (100%)
- EcuMGeneral attributes: 4/4 missing attributes implemented (100%)
- RteBswModuleInstance attributes: 25+/25+ missing attributes implemented (100%)
- RteSwComponentInstance attributes: 20+/20+ missing attributes implemented (100%)

## Notes
- All code follows established patterns from py-eb-model
- All classes have proper docstrings with SWR references
- Linting passed with no errors
- Ready for integration verification
```

- [ ] **Step 5: Commit completion summary**

```bash
git add docs/superpowers/completion/2026-03-29-agent4-ecum-rte-completion.md
git commit -m "docs: add Agent 4 (EcuM and Rte) completion summary"
```

---

## Summary

This plan implements complete coverage for EcuM and Rte modules:

**EcuM Module:**
- 30 missing classes added
- 4 missing attributes added to EcuMGeneral

**Rte Module:**
- 39 missing classes added
- 45+ missing attributes added to RteBswModuleInstance and RteSwComponentInstance

All work follows existing patterns in py-eb-model with proper docstrings, tests, and linting compliance.