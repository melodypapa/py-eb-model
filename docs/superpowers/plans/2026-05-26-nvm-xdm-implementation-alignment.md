# NvM XDM Implementation Alignment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Align NvM parser, model, and reporter with actual `data/NvM.xdm` content, add self-contained mock data, and achieve >95% test coverage.

**Architecture:** Three-layer fix: (1) update model classes to match real XDM fields, (2) update parser to read all fields from XML, (3) update reporter to write all meaningful data. Each layer tested with mock data replacing the external `data/NvM.xdm` dependency.

**Tech Stack:** Python 3.9+, xml.etree.ElementTree, openpyxl, pytest

**Prerequisite reading:**
- `src/eb_model/parser/mem_stack/nvm_xdm_parser.py` — existing parser
- `src/eb_model/models/mem_stack/nvm_xdm.py` — existing model
- `src/eb_model/reporter/excel_reporter/mem_stack/nvm_xdm.py` — existing reporter
- `data/NvM.xdm` — reference data file
- `tests/mock_data.py` — existing OS mock data pattern (follow this exactly)
- `tests/parser/mem_stack/test_nvm_xdm_parser.py` — empty container pattern for DemEvent and MultiCoreCallout
- `tests/models/mem_stack/test_nvm_xdm.py` — existing model tests
- `tests/reporter/excel_reporter/mem_stack/test_nvm_xdm.py` — existing reporter test

**Deviation summary (from analysis):**
- NvMDefensiveProgramming: model has wrong fields (NvMNullPointerCheck/NvMParameterCheck don't exist in data)
- NvMCommon: 12 fields exist in data but not in parser/model
- NvMCommonCryptoSecurityParameters: model has wrong fields
- NvMServiceAPI: model has wrong field (NvMVersionInfoApi belongs in NvMCommon)
- NvmDemEventParameterRefs: 9 DEM event refs not parsed
- ReportToDem: 18 fields in data not parsed (parser only has 2)
- MultiCoreCallout: 9 callout fields in data not parsed
- NvMBlockDescriptor: ~20 fields in data not parsed; model has ~15 fields defined but never populated
- NvMBlockCiphering: container not implemented at all
- Reporter: missing columns, hardcoded values, NvMEaRef raises NotImplementedError
- Tests: parser at 62%, reporter at 53%

---

## File Structure

| File | Responsibility | Action |
|---|---|---|
| `src/eb_model/models/mem_stack/nvm_xdm.py` | Domain model classes | Update field definitions across 8 classes |
| `src/eb_model/parser/mem_stack/nvm_xdm_parser.py` | XML parsing | Add read methods for all missing fields |
| `src/eb_model/reporter/excel_reporter/mem_stack/nvm_xdm.py` | Excel output | Add missing columns, sheets, fix bugs |
| `tests/mock_data.py` | Self-contained mock XDM XML | Add `MOCK_NVM_XDM` constant |
| `tests/parser/mem_stack/test_nvm_xdm_parser.py` | Parser unit tests | Add tests for all new parser methods |
| `tests/models/mem_stack/test_nvm_xdm.py` | Model unit tests | Add tests for all new model properties |
| `tests/reporter/excel_reporter/mem_stack/test_nvm_xdm.py` | Reporter unit tests | Expand reporter test coverage |

---

### Task 1: Add MOCK_NVM_XDM to tests/mock_data.py

**Files:**
- Modify: `tests/mock_data.py` (append after MOCK_OS_XDM)

- [ ] **Step 1: Create MOCK_NVM_XDM string**

Append to `tests/mock_data.py`:

```python

MOCK_NVM_XDM = """<?xml version="1.0"?>
<datamodel version="8.0"
           xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
           xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
           xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
           xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
  <d:ctr type="AUTOSAR" factory="autosar"
         xmlns:ad="http://www.tresos.de/_projects/DataModel2/08/admindata.xsd"
         xmlns:ce="http://www.tresos.de/_projects/DataModel2/18/childenable.xsd"
         xmlns:cd="http://www.tresos.de/_projects/DataModel2/08/customdata.xsd"
         xmlns:f="http://www.tresos.de/_projects/DataModel2/14/formulaexpr.xsd"
         xmlns:icc="http://www.tresos.de/_projects/DataModel2/08/implconfigclass.xsd"
         xmlns:mt="http://www.tresos.de/_projects/DataModel2/11/multitest.xsd"
         xmlns:variant="http://www.tresos.de/_projects/DataModel2/11/variant.xsd">
    <d:lst type="TOP-LEVEL-PACKAGES">
      <d:ctr name="NvM" type="AR-PACKAGE">
        <d:lst type="ELEMENTS">
          <d:chc name="NvM" type="AR-ELEMENT" value="MODULE-CONFIGURATION">
            <d:ctr type="MODULE-CONFIGURATION">
              <a:a name="DEF" value="ASPath:/TS_TxDxM7I0R0/NvM"/>
              <d:ctr name="CommonPublishedInformation" type="IDENTIFIABLE">
                <d:var name="ArMajorVersion" type="INTEGER" value="4"/>
                <d:var name="ArMinorVersion" type="INTEGER" value="7"/>
                <d:var name="ArPatchVersion" type="INTEGER" value="0"/>
                <d:var name="SwMajorVersion" type="INTEGER" value="7"/>
                <d:var name="SwMinorVersion" type="INTEGER" value="0"/>
                <d:var name="SwPatchVersion" type="INTEGER" value="0"/>
              </d:ctr>
              <d:var name="IMPLEMENTATION_CONFIG_VARIANT" type="ENUMERATION" value="VariantPreCompile"/>
              <d:lst name="NvMBlockDescriptor" type="MAP">
                <d:ctr name="NvMBlock_ConfigID" type="IDENTIFIABLE">
                  <d:ref name="NvMBlockEcucPartitionRef" type="REFERENCE"/>
                  <d:var name="NvMAdvancedRecovery" type="BOOLEAN" value="false"/>
                  <d:var name="NvMBlockCrcType" type="ENUMERATION" value="NVM_CRC16"/>
                  <d:var name="NvMBlockJobPriority" type="INTEGER" value="255"/>
                  <d:var name="NvMBlockUseSyncMechanism" type="BOOLEAN" value="false"/>
                  <d:var name="ASR2011CallbackEnabled" type="BOOLEAN" value="false"/>
                  <d:var name="NvMBlockWriteProt" type="BOOLEAN" value="false"/>
                  <d:var name="NvMBswMBlockStatusInformation" type="BOOLEAN" value="false"/>
                  <d:var name="NvMBlockUseCRCCompMechanism" type="BOOLEAN" value="false"/>
                  <d:var name="NvMBlockUseSetRamBlockStatus" type="BOOLEAN" value="true"/>
                  <d:var name="NvMExtraBlockChecks" type="BOOLEAN" value="false"/>
                  <d:var name="NvMMaxNumOfReadRetries" type="INTEGER" value="0"/>
                  <d:var name="NvMMaxNumOfWriteRetries" type="INTEGER" value="3"/>
                  <d:var name="NvMNvBlockLength" type="INTEGER" value="2"/>
                  <d:var name="NvMNvramBlockIdentifier" type="INTEGER" value="1"/>
                  <d:var name="NvMNvBlockNum" type="INTEGER" value="2"/>
                  <d:var name="NvMNvramDeviceId" type="INTEGER" value="0"/>
                  <d:var name="NvMProvideRteAdminPort" type="BOOLEAN" value="false"/>
                  <d:var name="NvMProvideRteInitBlockPort" type="BOOLEAN" value="false"/>
                  <d:var name="NvMProvideRteJobFinishedPort" type="BOOLEAN" value="false"/>
                  <d:var name="NvMProvideRteMirrorPort" type="BOOLEAN" value="false"/>
                  <d:var name="NvMProvideRteServicePort" type="BOOLEAN" value="false"/>
                  <d:var name="NvMReadRamBlockFromNvCallback" type="FUNCTION-NAME" value=""/>
                  <d:var name="NvMResistantToChangedSw" type="BOOLEAN" value="false"/>
                  <d:var name="NvMRomBlockNum" type="INTEGER" value="1"/>
                  <d:var name="NvMBlockUseCrc" type="BOOLEAN" value="true"/>
                  <d:var name="NvMCalcRamBlockCrc" type="BOOLEAN" value="true"/>
                  <d:var name="NvMSelectBlockForReadAll" type="BOOLEAN" value="false"/>
                  <d:var name="NvMSelectBlockForWriteAll" type="BOOLEAN" value="false"/>
                  <d:var name="NvMSelectBlockForFirstInitAll" type="BOOLEAN" value="false"/>
                  <d:var name="NvMStaticBlockIDCheck" type="BOOLEAN" value="false"/>
                  <d:var name="NvMBlockUseAutoValidation" type="BOOLEAN" value="false"/>
                  <d:chc name="NvMTargetBlockReference" type="IDENTIFIABLE" value="NvMFeeRef">
                    <d:ctr name="NvMEaRef" type="IDENTIFIABLE">
                      <d:ref name="NvMNameOfEaBlock" type="REFERENCE"/>
                    </d:ctr>
                    <d:ctr name="NvMFeeRef" type="IDENTIFIABLE">
                      <d:ref name="NvMNameOfFeeBlock" type="REFERENCE" value="ASPath:/Fee/Fee/Fee_NvMBlock_ConfigID"/>
                    </d:ctr>
                  </d:chc>
                  <d:var name="NvMBlockManagementType" type="ENUMERATION" value="NVM_BLOCK_REDUNDANT"/>
                  <d:var name="NvMNvBlockBaseNumber" type="INTEGER" value="1"/>
                  <d:var name="NvMRamBlockDataAddress" type="STRING" value="&amp;NvM_ConfigurationId"/>
                  <d:var name="NvMRomBlockDataAddress" type="STRING" value="&amp;NvM_CompiledConfigurationId"/>
                  <d:var name="NvMEnBlockCheck" type="BOOLEAN" value="false"/>
                  <d:var name="NvMEnableBlockCryptoSecurityHandling" type="BOOLEAN" value="false"/>
                  <d:var name="NvMCryptoExtraInfoSize" type="INTEGER" value="0"/>
                  <d:var name="NvMBcEnSetAPI" type="BOOLEAN" value="true"/>
                  <d:var name="NvMBcEnAutoStart" type="BOOLEAN" value="true"/>
                  <d:var name="NvMBcEnCrcComp" type="BOOLEAN" value="false"/>
                  <d:var name="NvMBcEnRamComp" type="BOOLEAN" value="false"/>
                  <d:var name="NvMBcEnReddCopiesComp" type="BOOLEAN" value="false"/>
                  <d:var name="NvMBcEnAutoRepair" type="BOOLEAN" value="false"/>
                  <d:var name="NvMBcDelayCounter" type="INTEGER" value="0"/>
                  <d:var name="NvMWriteBlockOnce" type="BOOLEAN" value="false"/>
                  <d:var name="NvMWriteRamBlockToNvCallback" type="FUNCTION-NAME" value=""/>
                  <d:var name="NvMWriteVerification" type="BOOLEAN" value="false"/>
                  <d:var name="NvMWriteVerificationDataSize" type="INTEGER" value="1"/>
                  <d:var name="NvMPreWriteDataComp" type="BOOLEAN" value="false"/>
                  <d:var name="NvMPreWriteDataCompDataSize" type="INTEGER" value="1"/>
                  <d:ctr name="NvMInitBlockCallback" type="IDENTIFIABLE">
                    <d:var name="NvMInitBlockCallbackFnc" type="FUNCTION-NAME" value=""/>
                  </d:ctr>
                  <d:ctr name="NvMSingleBlockCallback" type="IDENTIFIABLE">
                    <d:var name="NvMSingleBlockCallbackFnc" type="FUNCTION-NAME" value=""/>
                  </d:ctr>
                  <d:ref name="NvMBlockCipheringRef" type="REFERENCE"/>
                  <d:var name="NvMBlockHeaderInclude" type="STRING" value=""/>
                  <d:var name="NvMBlockUseCompression" type="BOOLEAN" value="false"/>
                  <d:var name="NvMBlockUsePort" type="BOOLEAN" value="false"/>
                </d:ctr>
              </d:lst>
              <d:ctr name="NvMDefensiveProgramming" type="IDENTIFIABLE">
                <d:var name="NvMDefProgEnabled" type="BOOLEAN" value="false"/>
                <d:var name="NvMPrecondAssertEnabled" type="BOOLEAN" value="false"/>
                <d:var name="NvMPostcondAssertEnabled" type="BOOLEAN" value="false"/>
                <d:var name="NvMStaticAssertEnabled" type="BOOLEAN" value="false"/>
                <d:var name="NvMUnreachAssertEnabled" type="BOOLEAN" value="false"/>
                <d:var name="NvMInvariantAssertEnabled" type="BOOLEAN" value="false"/>
              </d:ctr>
              <d:ctr name="NvMCommon" type="IDENTIFIABLE">
                <d:var name="NvMMemAccUsage" type="BOOLEAN" value="false"/>
                <d:var name="NvMBufferAlignmentValue" type="ENUMERATION" value="NVM_ALIGN_8_BITS"/>
                <d:var name="NvMApiConfigClass" type="ENUMERATION" value="NVM_API_CONFIG_CLASS_3"/>
                <d:var name="NvMBswMMultiBlockJobStatusInformation" type="BOOLEAN" value="true"/>
                <d:var name="NvMCompiledConfigId" type="INTEGER" value="1"/>
                <d:var name="NvMSoftwareChangeCallout" type="FUNCTION-NAME" value=""/>
                <d:var name="NvMCrcNumOfBytes" type="INTEGER" value="32"/>
                <d:var name="NvMDatasetSelectionBits" type="INTEGER" value="3"/>
                <d:var name="NvMDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="NvMDrvModeSwitch" type="BOOLEAN" value="false"/>
                <d:var name="NvMDynamicConfiguration" type="BOOLEAN" value="true"/>
                <d:var name="NvMCancelInternalOperations" type="BOOLEAN" value="false"/>
                <d:var name="NvMJobPrioritization" type="BOOLEAN" value="true"/>
                <d:var name="NvMMainFunctionPeriod" type="FLOAT" value="0.01"/>
                <d:var name="NvMMultiBlockCallback" type="FUNCTION-NAME" value="EcuM_CB_NfyNvMJobEnd"/>
                <d:var name="NvMPollingMode" type="BOOLEAN" value="false"/>
                <d:var name="NvMReadBlockHook" type="BOOLEAN" value="false"/>
                <d:var name="NvMRepeatMirrorOperations" type="INTEGER" value="0"/>
                <d:var name="NvMRteUsage" type="BOOLEAN" value="true"/>
                <d:var name="NvMSetRamBlockStatusApi" type="BOOLEAN" value="true"/>
                <d:var name="NvMSizeImmediateJobQueue" type="INTEGER" value="2"/>
                <d:var name="NvMSizeStandardJobQueue" type="INTEGER" value="22"/>
                <d:lst name="NvMUserHeader">
                  <d:var type="STRING" value="StubNvM.h"/>
                  <d:var type="STRING" value="Dem.h"/>
                </d:lst>
                <d:var name="NvMVersionInfoApi" type="BOOLEAN" value="true"/>
                <d:var name="NvMWriteBlockHook" type="BOOLEAN" value="false"/>
                <d:var name="NvMRedundantRecovery" type="ENUMERATION" value="NVM_RECOVERY_ON_REQUEST"/>
                <d:var name="NvMExportBlockLengths" type="BOOLEAN" value="false"/>
                <d:var name="NvMResultErasedBlocks" type="ENUMERATION" value="MEMIF_BLOCK_INCONSISTENT"/>
                <d:var name="NvMEnableLegacySymbolicNames" type="BOOLEAN" value="true"/>
                <d:var name="NvMResetRamBlockAfterReset" type="BOOLEAN" value="false"/>
                <d:ctr name="NvMCommonCryptoSecurityParameters" type="IDENTIFIABLE">
                  <d:var name="NvMEnableCryptoSecurityHooks" type="BOOLEAN" value="false"/>
                  <d:var name="NvMCryptoReadHook" type="FUNCTION-NAME" value=""/>
                  <d:var name="NvMCryptoWriteHook" type="FUNCTION-NAME" value=""/>
                </d:ctr>
                <d:ctr name="NvMServiceAPI" type="IDENTIFIABLE">
                  <d:var name="NvMEnableASR32ServiceAPI" type="BOOLEAN" value="false"/>
                  <d:var name="NvMEnableASR40ServiceAPI" type="BOOLEAN" value="false"/>
                  <d:var name="NvMEnableASR42ServiceAPI" type="BOOLEAN" value="false"/>
                  <d:var name="NvMDefaultASRServiceAPI" type="ENUMERATION" value="AUTOSAR_42"/>
                </d:ctr>
                <d:ref name="NvMMasterEcucPartitionRef" type="REFERENCE"/>
                <d:lst name="NvMEcucPartitionRef"/>
                <d:var name="NvMCsmRetryCounter" type="INTEGER" value="0"/>
              </d:ctr>
              <d:ctr name="NvmDemEventParameterRefs" type="IDENTIFIABLE">
                <d:ref name="NVM_E_INTEGRITY_FAILED" type="REFERENCE"/>
                <d:ref name="NVM_E_LOSS_OF_REDUNDANCY" type="REFERENCE"/>
                <d:ref name="NVM_E_QUEUE_OVERFLOW" type="REFERENCE"/>
                <d:ref name="NVM_E_REQ_FAILED" type="REFERENCE"/>
                <d:ref name="NVM_E_VERIFY_FAILED" type="REFERENCE"/>
                <d:ref name="NVM_E_WRITE_PROTECTED" type="REFERENCE"/>
                <d:ref name="NVM_E_WRONG_BLOCK_ID" type="REFERENCE"/>
                <d:ref name="NVM_E_BLOCK_CHECK" type="REFERENCE"/>
                <d:ref name="NVM_E_HARDWARE" type="REFERENCE"/>
              </d:ctr>
              <d:ctr name="ReportToDem" type="IDENTIFIABLE">
                <d:var name="NvMUserCalloutFunctionProductionErrors" type="FUNCTION-NAME" value=""/>
                <d:var name="NvMUserCalloutFunctionPassedProductionErrors" type="FUNCTION-NAME" value=""/>
                <d:var name="NvMIntegrityFailedReportToDem" type="ENUMERATION" value="DISABLE"/>
                <d:var name="NvMIntegrityFailedReportToDemDetErrorId" type="INTEGER" value="25"/>
                <d:var name="NvMRequestFailedReportToDem" type="ENUMERATION" value="DISABLE"/>
                <d:var name="NvMRequestFailedReportToDemDetErrorId" type="INTEGER" value="26"/>
                <d:var name="NvMWrongBlockIdReportToDem" type="ENUMERATION" value="DISABLE"/>
                <d:var name="NvMWrongBlockIdReportToDemDetErrorId" type="INTEGER" value="27"/>
                <d:var name="NvMLossOfRedundancyReportToDem" type="ENUMERATION" value="DISABLE"/>
                <d:var name="NvMLossOfRedundancyReportToDemDetErrorId" type="INTEGER" value="28"/>
                <d:var name="NvMQueueOverflowReportToDem" type="ENUMERATION" value="DISABLE"/>
                <d:var name="NvMQueueOverflowReportToDemDetErrorId" type="INTEGER" value="29"/>
                <d:var name="NvMVerifyFailedReportToDem" type="ENUMERATION" value="DISABLE"/>
                <d:var name="NvMVerifyFailedReportToDemDetErrorId" type="INTEGER" value="30"/>
                <d:var name="NvMWriteProtectedReportToDem" type="ENUMERATION" value="DISABLE"/>
                <d:var name="NvMWriteProtectedReportToDemDetErrorId" type="INTEGER" value="31"/>
                <d:var name="NvMBlockCheckReportProdError" type="ENUMERATION" value="DISABLE"/>
                <d:var name="NvMBlockCheckReportProdErrorId" type="INTEGER" value="32"/>
              </d:ctr>
              <d:ctr name="MultiCoreCallout" type="IDENTIFIABLE">
                <d:var name="NvMReadBlockCallout" type="FUNCTION-NAME" value=""/>
                <d:var name="NvMWriteBlockCallout" type="FUNCTION-NAME" value=""/>
                <d:var name="NvMRestoreBlockDefaultsCallout" type="FUNCTION-NAME" value=""/>
                <d:var name="NvMReadPRAMBlockCallout" type="FUNCTION-NAME" value=""/>
                <d:var name="NvMWritePRAMBlockCallout" type="FUNCTION-NAME" value=""/>
                <d:var name="NvMRestorePRAMBlockDefaultsCallout" type="FUNCTION-NAME" value=""/>
                <d:var name="NvMEraseNvBlockCallout" type="FUNCTION-NAME" value=""/>
                <d:var name="NvMInvalidateNvBlockCallout" type="FUNCTION-NAME" value=""/>
                <d:var name="NvMCancelJobsCallout" type="FUNCTION-NAME" value=""/>
              </d:ctr>
              <d:ctr name="PublishedInformation" type="IDENTIFIABLE">
                <d:var name="PbcfgMSupport" type="BOOLEAN" value="false"/>
              </d:ctr>
            </d:ctr>
          </d:chc>
        </d:lst>
      </d:ctr>
    </d:lst>
  </d:ctr>
</datamodel>
"""
```

- [ ] **Step 2: Update mock_data.py module docstring**

Change the module docstring from one-liner to:
```python
"""
Shared mock XDM data for self-contained tests.

Contains comprehensive mock XDM XML strings for OS and NvM modules,
eliminating dependency on external data files.
"""
```

---

### Task 2: Update NvM Model — NvMDefensiveProgramming, NvMCommonCryptoSecurityParameters, NvMServiceAPI

**Files:**
- Modify: `src/eb_model/models/mem_stack/nvm_xdm.py`
- Test: `tests/models/mem_stack/test_nvm_xdm.py`

- [ ] **Step 1: Replace NvMDefensiveProgramming fields**

In `nvm_xdm.py`, replace the entire `NvMDefensiveProgramming` class:
```python
class NvMDefensiveProgramming(EcucParamConfContainerDef):
    """
    Defensive programming configuration for NvM module.

    Implements: SWR_NVM_00005
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.nvMDefProgEnabled: bool = None
        self.nvMPrecondAssertEnabled: bool = None
        self.nvMPostcondAssertEnabled: bool = None
        self.nvMStaticAssertEnabled: bool = None
        self.nvMUnreachAssertEnabled: bool = None
        self.nvMInvariantAssertEnabled: bool = None

    def getNvMDefProgEnabled(self) -> bool:
        return self.nvMDefProgEnabled

    def setNvMDefProgEnabled(self, value: bool):
        if value is not None:
            self.nvMDefProgEnabled = value
        return self

    def getNvMPrecondAssertEnabled(self) -> bool:
        return self.nvMPrecondAssertEnabled

    def setNvMPrecondAssertEnabled(self, value: bool):
        if value is not None:
            self.nvMPrecondAssertEnabled = value
        return self

    def getNvMPostcondAssertEnabled(self) -> bool:
        return self.nvMPostcondAssertEnabled

    def setNvMPostcondAssertEnabled(self, value: bool):
        if value is not None:
            self.nvMPostcondAssertEnabled = value
        return self

    def getNvMStaticAssertEnabled(self) -> bool:
        return self.nvMStaticAssertEnabled

    def setNvMStaticAssertEnabled(self, value: bool):
        if value is not None:
            self.nvMStaticAssertEnabled = value
        return self

    def getNvMUnreachAssertEnabled(self) -> bool:
        return self.nvMUnreachAssertEnabled

    def setNvMUnreachAssertEnabled(self, value: bool):
        if value is not None:
            self.nvMUnreachAssertEnabled = value
        return self

    def getNvMInvariantAssertEnabled(self) -> bool:
        return self.nvMInvariantAssertEnabled

    def setNvMInvariantAssertEnabled(self, value: bool):
        if value is not None:
            self.nvMInvariantAssertEnabled = value
        return self
```

- [ ] **Step 2: Replace NvMCommonCryptoSecurityParameters fields**

```python
class NvMCommonCryptoSecurityParameters(EcucParamConfContainerDef):
    """
    Common crypto security parameters for NvM module.

    Implements: SWR_NVM_00006
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.nvMEnableCryptoSecurityHooks: bool = None
        self.nvMCryptoReadHook: str = None
        self.nvMCryptoWriteHook: str = None

    def getNvMEnableCryptoSecurityHooks(self) -> bool:
        return self.nvMEnableCryptoSecurityHooks

    def setNvMEnableCryptoSecurityHooks(self, value: bool):
        if value is not None:
            self.nvMEnableCryptoSecurityHooks = value
        return self

    def getNvMCryptoReadHook(self) -> str:
        return self.nvMCryptoReadHook

    def setNvMCryptoReadHook(self, value: str):
        if value is not None:
            self.nvMCryptoReadHook = value
        return self

    def getNvMCryptoWriteHook(self) -> str:
        return self.nvMCryptoWriteHook

    def setNvMCryptoWriteHook(self, value: str):
        if value is not None:
            self.nvMCryptoWriteHook = value
        return self
```

- [ ] **Step 3: Replace NvMServiceAPI class**

```python
class NvMServiceAPI(EcucParamConfContainerDef):
    """
    Service API configuration for NvM module.

    Implements: SWR_NVM_00007
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.nvMEnableASR32ServiceAPI: bool = None
        self.nvMEnableASR40ServiceAPI: bool = None
        self.nvMEnableASR42ServiceAPI: bool = None
        self.nvMDefaultASRServiceAPI: str = None

    def getNvMEnableASR32ServiceAPI(self) -> bool:
        return self.nvMEnableASR32ServiceAPI

    def setNvMEnableASR32ServiceAPI(self, value: bool):
        if value is not None:
            self.nvMEnableASR32ServiceAPI = value
        return self

    def getNvMEnableASR40ServiceAPI(self) -> bool:
        return self.nvMEnableASR40ServiceAPI

    def setNvMEnableASR40ServiceAPI(self, value: bool):
        if value is not None:
            self.nvMEnableASR40ServiceAPI = value
        return self

    def getNvMEnableASR42ServiceAPI(self) -> bool:
        return self.nvMEnableASR42ServiceAPI

    def setNvMEnableASR42ServiceAPI(self, value: bool):
        if value is not None:
            self.nvMEnableASR42ServiceAPI = value
        return self

    def getNvMDefaultASRServiceAPI(self) -> str:
        return self.nvMDefaultASRServiceAPI

    def setNvMDefaultASRServiceAPI(self, value: str):
        if value is not None:
            self.nvMDefaultASRServiceAPI = value
        return self
```

- [ ] **Step 4: Update model tests for changed classes**

In `tests/models/mem_stack/test_nvm_xdm.py`, update `TestNvMDefensiveProgramming`:
```python
class TestNvMDefensiveProgramming:

    def test_initialization(self):
        root = EBModel.getInstance()
        defensive = NvMDefensiveProgramming(root, "NvMDefensiveProgramming")

        assert defensive.getName() == "NvMDefensiveProgramming"
        assert defensive.getParent() == root
        assert defensive.getNvMDefProgEnabled() is None
        assert defensive.getNvMPrecondAssertEnabled() is None
        assert defensive.getNvMPostcondAssertEnabled() is None
        assert defensive.getNvMStaticAssertEnabled() is None
        assert defensive.getNvMUnreachAssertEnabled() is None
        assert defensive.getNvMInvariantAssertEnabled() is None

    def test_set_nvm_def_prog_enabled(self):
        root = EBModel.getInstance()
        defensive = NvMDefensiveProgramming(root, "NvMDefensiveProgramming")
        assert defensive.setNvMDefProgEnabled(True) == defensive
        assert defensive.getNvMDefProgEnabled() is True

    def test_set_nvm_precond_assert_enabled(self):
        root = EBModel.getInstance()
        defensive = NvMDefensiveProgramming(root, "NvMDefensiveProgramming")
        assert defensive.setNvMPrecondAssertEnabled(True) == defensive
        assert defensive.getNvMPrecondAssertEnabled() is True
```

- [ ] **Step 5: Run model tests to verify**

Run: `python -m pytest tests/models/mem_stack/test_nvm_xdm.py -v --tb=short`
Expected: All tests pass (the old `getNvMNullPointerCheck` tests must be removed since those fields no longer exist)

- [ ] **Step 6: Commit**

```bash
git add src/eb_model/models/mem_stack/nvm_xdm.py tests/models/mem_stack/test_nvm_xdm.py tests/mock_data.py
git commit -m "refactor: update NvM model fields to match data/NvM.xdm schema

Update NvMDefensiveProgramming, NvMCommonCryptoSecurityParameters,
and NvMServiceAPI to use actual fields from the reference XDM file.
Add MOCK_NVM_XDM for self-contained testing."
```

---

### Task 3: Update NvM Model — NvMCommon new fields

**Files:**
- Modify: `src/eb_model/models/mem_stack/nvm_xdm.py`

- [ ] **Step 1: Add 12 new properties to NvMCommon**

Insert after existing `self.NvMCsmRetryCounter` in `__init__`:
```python
        self.nvMSoftwareChangeCallout: str = None
        self.nvMDrvModeSwitch: bool = None
        self.nvMCancelInternalOperations: bool = None
        self.nvMReadBlockHook: bool = None
        self.nvMRteUsage: bool = None
        self.nvMUserHeader: List[str] = []
        self.nvMWriteBlockHook: bool = None
        self.nvMRedundantRecovery: str = None
        self.nvMExportBlockLengths: bool = None
        self.nvMResultErasedBlocks: str = None
        self.nvMEnableLegacySymbolicNames: bool = None
        self.nvMResetRamBlockAfterReset: bool = None
```

Add getter/setter methods before the `getNvMBufferAlignmentValue` line:
```python
    def getNvMSoftwareChangeCallout(self) -> str:
        return self.nvMSoftwareChangeCallout

    def setNvMSoftwareChangeCallout(self, value: str):
        if value is not None:
            self.nvMSoftwareChangeCallout = value
        return self

    def getNvMDrvModeSwitch(self) -> bool:
        return self.nvMDrvModeSwitch

    def setNvMDrvModeSwitch(self, value: bool):
        if value is not None:
            self.nvMDrvModeSwitch = value
        return self

    def getNvMCancelInternalOperations(self) -> bool:
        return self.nvMCancelInternalOperations

    def setNvMCancelInternalOperations(self, value: bool):
        if value is not None:
            self.nvMCancelInternalOperations = value
        return self

    def getNvMReadBlockHook(self) -> bool:
        return self.nvMReadBlockHook

    def setNvMReadBlockHook(self, value: bool):
        if value is not None:
            self.nvMReadBlockHook = value
        return self

    def getNvMRteUsage(self) -> bool:
        return self.nvMRteUsage

    def setNvMRteUsage(self, value: bool):
        if value is not None:
            self.nvMRteUsage = value
        return self

    def getNvMUserHeaderList(self) -> List[str]:
        return self.nvMUserHeader

    def addNvMUserHeader(self, value: str):
        if value is not None:
            self.nvMUserHeader.append(value)
        return self

    def getNvMWriteBlockHook(self) -> bool:
        return self.nvMWriteBlockHook

    def setNvMWriteBlockHook(self, value: bool):
        if value is not None:
            self.nvMWriteBlockHook = value
        return self

    def getNvMRedundantRecovery(self) -> str:
        return self.nvMRedundantRecovery

    def setNvMRedundantRecovery(self, value: str):
        if value is not None:
            self.nvMRedundantRecovery = value
        return self

    def getNvMExportBlockLengths(self) -> bool:
        return self.nvMExportBlockLengths

    def setNvMExportBlockLengths(self, value: bool):
        if value is not None:
            self.nvMExportBlockLengths = value
        return self

    def getNvMResultErasedBlocks(self) -> str:
        return self.nvMResultErasedBlocks

    def setNvMResultErasedBlocks(self, value: str):
        if value is not None:
            self.nvMResultErasedBlocks = value
        return self

    def getNvMEnableLegacySymbolicNames(self) -> bool:
        return self.nvMEnableLegacySymbolicNames

    def setNvMEnableLegacySymbolicNames(self, value: bool):
        if value is not None:
            self.nvMEnableLegacySymbolicNames = value
        return self

    def getNvMResetRamBlockAfterReset(self) -> bool:
        return self.nvMResetRamBlockAfterReset

    def setNvMResetRamBlockAfterReset(self, value: bool):
        if value is not None:
            self.nvMResetRamBlockAfterReset = value
        return self
```

- [ ] **Step 2: Run tests to verify no breakage**

Run: `python -m pytest tests/models/mem_stack/ -v --tb=short`
Expected: All pass

- [ ] **Step 3: Commit**

```bash
git add src/eb_model/models/mem_stack/nvm_xdm.py
git commit -m "feat: add 12 new NvMCommon fields matching data/NvM.xdm"
```

---

### Task 4: Update NvM Model — ReportToDem, MultiCoreCallout, NvmDemEventParameterRefs

**Files:**
- Modify: `src/eb_model/models/mem_stack/nvm_xdm.py`

- [ ] **Step 1: Add DEM event ref storage to NvmDemEventParameterRefs**

Replace the empty `NvmDemEventParameterRefs` class body:
```python
class NvmDemEventParameterRefs(EcucParamConfContainerDef):
    """
    DEM event parameter references for NvM module.

    Implements: SWR_NVM_00008
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.demEventRefs: List[EcucRefType] = []

    def getDemEventRefList(self) -> List[EcucRefType]:
        return self.demEventRefs

    def addDemEventRef(self, value: EcucRefType):
        if value is not None:
            self.demEventRefs.append(value)
        return self
```

- [ ] **Step 2: Add all fields to ReportToDem**

Replace the entire `ReportToDem` class:
```python
class ReportToDem(EcucParamConfContainerDef):
    """
    DEM reporting configuration for NvM module.

    Implements: SWR_NVM_00009
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.nvMUserCalloutFunctionProductionErrors: str = None
        self.nvMUserCalloutFunctionPassedProductionErrors: str = None
        self.nvMIntegrityFailedReportToDem: str = None
        self.nvMIntegrityFailedReportToDemDetErrorId: int = None
        self.nvMRequestFailedReportToDem: str = None
        self.nvMRequestFailedReportToDemDetErrorId: int = None
        self.nvMWrongBlockIdReportToDem: str = None
        self.nvMWrongBlockIdReportToDemDetErrorId: int = None
        self.nvMLossOfRedundancyReportToDem: str = None
        self.nvMLossOfRedundancyReportToDemDetErrorId: int = None
        self.nvMQueueOverflowReportToDem: str = None
        self.nvMQueueOverflowReportToDemDetErrorId: int = None
        self.nvMVerifyFailedReportToDem: str = None
        self.nvMVerifyFailedReportToDemDetErrorId: int = None
        self.nvMWriteProtectedReportToDem: str = None
        self.nvMWriteProtectedReportToDemDetErrorId: int = None
        self.nvMBlockCheckReportProdError: str = None
        self.nvMBlockCheckReportProdErrorId: int = None

    # getNvMReportStorageFailed / setNvMReportStorageFailed — REMOVE (not in data)
    # getNvMReportVerificationFailed / setNvMReportVerificationFailed — REMOVE (not in data)

    def getNvMUserCalloutFunctionProductionErrors(self) -> str:
        return self.nvMUserCalloutFunctionProductionErrors

    def setNvMUserCalloutFunctionProductionErrors(self, value: str):
        if value is not None:
            self.nvMUserCalloutFunctionProductionErrors = value
        return self

    def getNvMUserCalloutFunctionPassedProductionErrors(self) -> str:
        return self.nvMUserCalloutFunctionPassedProductionErrors

    def setNvMUserCalloutFunctionPassedProductionErrors(self, value: str):
        if value is not None:
            self.nvMUserCalloutFunctionPassedProductionErrors = value
        return self

    def getNvMIntegrityFailedReportToDem(self) -> str:
        return self.nvMIntegrityFailedReportToDem

    def setNvMIntegrityFailedReportToDem(self, value: str):
        if value is not None:
            self.nvMIntegrityFailedReportToDem = value
        return self

    def getNvMIntegrityFailedReportToDemDetErrorId(self) -> int:
        return self.nvMIntegrityFailedReportToDemDetErrorId

    def setNvMIntegrityFailedReportToDemDetErrorId(self, value: int):
        if value is not None:
            self.nvMIntegrityFailedReportToDemDetErrorId = value
        return self

    def getNvMRequestFailedReportToDem(self) -> str:
        return self.nvMRequestFailedReportToDem

    def setNvMRequestFailedReportToDem(self, value: str):
        if value is not None:
            self.nvMRequestFailedReportToDem = value
        return self

    def getNvMRequestFailedReportToDemDetErrorId(self) -> int:
        return self.nvMRequestFailedReportToDemDetErrorId

    def setNvMRequestFailedReportToDemDetErrorId(self, value: int):
        if value is not None:
            self.nvMRequestFailedReportToDemDetErrorId = value
        return self

    def getNvMWrongBlockIdReportToDem(self) -> str:
        return self.nvMWrongBlockIdReportToDem

    def setNvMWrongBlockIdReportToDem(self, value: str):
        if value is not None:
            self.nvMWrongBlockIdReportToDem = value
        return self

    def getNvMWrongBlockIdReportToDemDetErrorId(self) -> int:
        return self.nvMWrongBlockIdReportToDemDetErrorId

    def setNvMWrongBlockIdReportToDemDetErrorId(self, value: int):
        if value is not None:
            self.nvMWrongBlockIdReportToDemDetErrorId = value
        return self

    def getNvMLossOfRedundancyReportToDem(self) -> str:
        return self.nvMLossOfRedundancyReportToDem

    def setNvMLossOfRedundancyReportToDem(self, value: str):
        if value is not None:
            self.nvMLossOfRedundancyReportToDem = value
        return self

    def getNvMLossOfRedundancyReportToDemDetErrorId(self) -> int:
        return self.nvMLossOfRedundancyReportToDemDetErrorId

    def setNvMLossOfRedundancyReportToDemDetErrorId(self, value: int):
        if value is not None:
            self.nvMLossOfRedundancyReportToDemDetErrorId = value
        return self

    def getNvMQueueOverflowReportToDem(self) -> str:
        return self.nvMQueueOverflowReportToDem

    def setNvMQueueOverflowReportToDem(self, value: str):
        if value is not None:
            self.nvMQueueOverflowReportToDem = value
        return self

    def getNvMQueueOverflowReportToDemDetErrorId(self) -> int:
        return self.nvMQueueOverflowReportToDemDetErrorId

    def setNvMQueueOverflowReportToDemDetErrorId(self, value: int):
        if value is not None:
            self.nvMQueueOverflowReportToDemDetErrorId = value
        return self

    def getNvMVerifyFailedReportToDem(self) -> str:
        return self.nvMVerifyFailedReportToDem

    def setNvMVerifyFailedReportToDem(self, value: str):
        if value is not None:
            self.nvMVerifyFailedReportToDem = value
        return self

    def getNvMVerifyFailedReportToDemDetErrorId(self) -> int:
        return self.nvMVerifyFailedReportToDemDetErrorId

    def setNvMVerifyFailedReportToDemDetErrorId(self, value: int):
        if value is not None:
            self.nvMVerifyFailedReportToDemDetErrorId = value
        return self

    def getNvMWriteProtectedReportToDem(self) -> str:
        return self.nvMWriteProtectedReportToDem

    def setNvMWriteProtectedReportToDem(self, value: str):
        if value is not None:
            self.nvMWriteProtectedReportToDem = value
        return self

    def getNvMWriteProtectedReportToDemDetErrorId(self) -> int:
        return self.nvMWriteProtectedReportToDemDetErrorId

    def setNvMWriteProtectedReportToDemDetErrorId(self, value: int):
        if value is not None:
            self.nvMWriteProtectedReportToDemDetErrorId = value
        return self

    def getNvMBlockCheckReportProdError(self) -> str:
        return self.nvMBlockCheckReportProdError

    def setNvMBlockCheckReportProdError(self, value: str):
        if value is not None:
            self.nvMBlockCheckReportProdError = value
        return self

    def getNvMBlockCheckReportProdErrorId(self) -> int:
        return self.nvMBlockCheckReportProdErrorId

    def setNvMBlockCheckReportProdErrorId(self, value: int):
        if value is not None:
            self.nvMBlockCheckReportProdErrorId = value
        return self
```

- [ ] **Step 3: Add fields to MultiCoreCallout**

Replace the empty `MultiCoreCallout` class:
```python
class MultiCoreCallout(EcucParamConfContainerDef):
    """
    Multi-core callout configuration for NvM module.

    Implements: SWR_NVM_00010
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.nvMReadBlockCallout: str = None
        self.nvMWriteBlockCallout: str = None
        self.nvMRestoreBlockDefaultsCallout: str = None
        self.nvMReadPRAMBlockCallout: str = None
        self.nvMWritePRAMBlockCallout: str = None
        self.nvMRestorePRAMBlockDefaultsCallout: str = None
        self.nvMEraseNvBlockCallout: str = None
        self.nvMInvalidateNvBlockCallout: str = None
        self.nvMCancelJobsCallout: str = None

    def getNvMReadBlockCallout(self) -> str:
        return self.nvMReadBlockCallout

    def setNvMReadBlockCallout(self, value: str):
        if value is not None:
            self.nvMReadBlockCallout = value
        return self

    def getNvMWriteBlockCallout(self) -> str:
        return self.nvMWriteBlockCallout

    def setNvMWriteBlockCallout(self, value: str):
        if value is not None:
            self.nvMWriteBlockCallout = value
        return self

    def getNvMRestoreBlockDefaultsCallout(self) -> str:
        return self.nvMRestoreBlockDefaultsCallout

    def setNvMRestoreBlockDefaultsCallout(self, value: str):
        if value is not None:
            self.nvMRestoreBlockDefaultsCallout = value
        return self

    def getNvMReadPRAMBlockCallout(self) -> str:
        return self.nvMReadPRAMBlockCallout

    def setNvMReadPRAMBlockCallout(self, value: str):
        if value is not None:
            self.nvMReadPRAMBlockCallout = value
        return self

    def getNvMWritePRAMBlockCallout(self) -> str:
        return self.nvMWritePRAMBlockCallout

    def setNvMWritePRAMBlockCallout(self, value: str):
        if value is not None:
            self.nvMWritePRAMBlockCallout = value
        return self

    def getNvMRestorePRAMBlockDefaultsCallout(self) -> str:
        return self.nvMRestorePRAMBlockDefaultsCallout

    def setNvMRestorePRAMBlockDefaultsCallout(self, value: str):
        if value is not None:
            self.nvMRestorePRAMBlockDefaultsCallout = value
        return self

    def getNvMEraseNvBlockCallout(self) -> str:
        return self.nvMEraseNvBlockCallout

    def setNvMEraseNvBlockCallout(self, value: str):
        if value is not None:
            self.nvMEraseNvBlockCallout = value
        return self

    def getNvMInvalidateNvBlockCallout(self) -> str:
        return self.nvMInvalidateNvBlockCallout

    def setNvMInvalidateNvBlockCallout(self, value: str):
        if value is not None:
            self.nvMInvalidateNvBlockCallout = value
        return self

    def getNvMCancelJobsCallout(self) -> str:
        return self.nvMCancelJobsCallout

    def setNvMCancelJobsCallout(self, value: str):
        if value is not None:
            self.nvMCancelJobsCallout = value
        return self
```

- [ ] **Step 4: Add missing NvMBlockDescriptor model fields**

In `NvMBlockDescriptor.__init__`, add these properties after existing fields (insert before `self.nvMInitBlockCallback`):
```python
        self.nvMEnBlockCheck: bool = None
        self.nvMEnableBlockCryptoSecurityHandling: bool = None
        self.nvMCryptoExtraInfoSize: int = None
        self.nvMBcEnSetAPI: bool = None
        self.nvMBcEnAutoStart: bool = None
        self.nvMBcEnCrcComp: bool = None
        self.nvMBcEnRamComp: bool = None
        self.nvMBcEnReddCopiesComp: bool = None
        self.nvMBcEnAutoRepair: bool = None
        self.nvMBcDelayCounter: int = None
        self.nvMWriteBlockOnce: bool = None
        self.nvMWriteVerification: bool = None
        self.nvMWriteVerificationDataSize: int = None
        self.nvMPreWriteDataComp: bool = None
        self.nvMPreWriteDataCompDataSize: int = None
```

Add getter/setter methods for each. Pattern (repeat for each of the 15 new fields):
```python
    def getNvMEnBlockCheck(self) -> bool:
        return self.nvMEnBlockCheck

    def setNvMEnBlockCheck(self, value: bool):
        if value is not None:
            self.nvMEnBlockCheck = value
        return self
```

- [ ] **Step 5: Clean up NvM.getNvMDefensiveProgramming reference in NvM.getNvMVersionInfoApi**

After updating the model, check `src/eb_model/reporter/...` for any test or reporter that calls the old method names. Search and fix callers.

Run: `grep -r "NvMNullPointerCheck\|NvMParameterCheck\|NvMReportStorageFailed\|NvMReportVerificationFailed\|getNvMCryptoPrimitive\|getNvMKeyAddress\|getNvMVersionInfoApi" src/ tests/ --include="*.py"`

If no hits, move on.

- [ ] **Step 6: Commit**

```bash
git add src/eb_model/models/mem_stack/nvm_xdm.py
git commit -m "feat: add ReportToDem, MultiCoreCallout, NvmDemEventRefs, and block descriptor fields"
```

---

### Task 5: Update NvM Parser — new read methods

**Files:**
- Modify: `src/eb_model/parser/mem_stack/nvm_xdm_parser.py`

- [ ] **Step 1: Rewrite read_nvm_defensive_programming**

```python
    def read_nvm_defensive_programming(self, element: ET.Element, nvm: NvM):
        """Parse NvMDefensiveProgramming container from XDM.

        Implements: SWR_NVM_00005
        """
        ctr_tag = self.find_ctr_tag(element, "NvMDefensiveProgramming")
        if ctr_tag is not None:
            defensive = NvMDefensiveProgramming(nvm, ctr_tag.attrib["name"])
            defensive.setNvMDefProgEnabled(self.read_optional_value(ctr_tag, "NvMDefProgEnabled"))
            defensive.setNvMPrecondAssertEnabled(self.read_optional_value(ctr_tag, "NvMPrecondAssertEnabled"))
            defensive.setNvMPostcondAssertEnabled(self.read_optional_value(ctr_tag, "NvMPostcondAssertEnabled"))
            defensive.setNvMStaticAssertEnabled(self.read_optional_value(ctr_tag, "NvMStaticAssertEnabled"))
            defensive.setNvMUnreachAssertEnabled(self.read_optional_value(ctr_tag, "NvMUnreachAssertEnabled"))
            defensive.setNvMInvariantAssertEnabled(self.read_optional_value(ctr_tag, "NvMInvariantAssertEnabled"))
            nvm.setNvMDefensiveProgramming(defensive)
            self.logger.debug("Read NvMDefensiveProgramming")
```

- [ ] **Step 2: Rewrite read_nvm_common_crypto_security_parameters**

```python
    def read_nvm_common_crypto_security_parameters(self, element: ET.Element, nvm: NvM):
        """Parse NvMCommonCryptoSecurityParameters container from XDM.

        Implements: SWR_NVM_00006
        """
        ctr_tag = self.find_ctr_tag(element, "NvMCommonCryptoSecurityParameters")
        if ctr_tag is not None:
            crypto = NvMCommonCryptoSecurityParameters(nvm, ctr_tag.attrib["name"])
            crypto.setNvMEnableCryptoSecurityHooks(self.read_optional_value(ctr_tag, "NvMEnableCryptoSecurityHooks"))
            crypto.setNvMCryptoReadHook(self.read_optional_value(ctr_tag, "NvMCryptoReadHook"))
            crypto.setNvMCryptoWriteHook(self.read_optional_value(ctr_tag, "NvMCryptoWriteHook"))
            nvm.setNvMCommonCryptoSecurityParameters(crypto)
            self.logger.debug("Read NvMCommonCryptoSecurityParameters")
```

- [ ] **Step 3: Rewrite read_nvm_service_api**

```python
    def read_nvm_service_api(self, element: ET.Element, nvm: NvM):
        """Parse NvMServiceAPI container from XDM.

        Implements: SWR_NVM_00007
        """
        ctr_tag = self.find_ctr_tag(element, "NvMServiceAPI")
        if ctr_tag is not None:
            service_api = NvMServiceAPI(nvm, ctr_tag.attrib["name"])
            service_api.setNvMEnableASR32ServiceAPI(self.read_optional_value(ctr_tag, "NvMEnableASR32ServiceAPI"))
            service_api.setNvMEnableASR40ServiceAPI(self.read_optional_value(ctr_tag, "NvMEnableASR40ServiceAPI"))
            service_api.setNvMEnableASR42ServiceAPI(self.read_optional_value(ctr_tag, "NvMEnableASR42ServiceAPI"))
            service_api.setNvMDefaultASRServiceAPI(self.read_optional_value(ctr_tag, "NvMDefaultASRServiceAPI"))
            nvm.setNvMServiceAPI(service_api)
            self.logger.debug("Read NvMServiceAPI")
```

- [ ] **Step 4: Rewrite read_nvm_dem_event_parameter_refs**

```python
    def read_nvm_dem_event_parameter_refs(self, element: ET.Element, nvm: NvM):
        """Parse NvmDemEventParameterRefs container from XDM.

        Implements: SWR_NVM_00008
        """
        ctr_tag = self.find_ctr_tag(element, "NvmDemEventParameterRefs")
        if ctr_tag is not None:
            dem_params = NvmDemEventParameterRefs(nvm, ctr_tag.attrib["name"])
            for ref in self.read_ref_value_list(ctr_tag, "NVM_E_INTEGRITY_FAILED"):
                dem_params.addDemEventRef(ref)
            for ref in self.read_ref_value_list(ctr_tag, "NVM_E_LOSS_OF_REDUNDANCY"):
                dem_params.addDemEventRef(ref)
            for ref in self.read_ref_value_list(ctr_tag, "NVM_E_QUEUE_OVERFLOW"):
                dem_params.addDemEventRef(ref)
            for ref in self.read_ref_value_list(ctr_tag, "NVM_E_REQ_FAILED"):
                dem_params.addDemEventRef(ref)
            for ref in self.read_ref_value_list(ctr_tag, "NVM_E_VERIFY_FAILED"):
                dem_params.addDemEventRef(ref)
            for ref in self.read_ref_value_list(ctr_tag, "NVM_E_WRITE_PROTECTED"):
                dem_params.addDemEventRef(ref)
            for ref in self.read_ref_value_list(ctr_tag, "NVM_E_WRONG_BLOCK_ID"):
                dem_params.addDemEventRef(ref)
            for ref in self.read_ref_value_list(ctr_tag, "NVM_E_BLOCK_CHECK"):
                dem_params.addDemEventRef(ref)
            for ref in self.read_ref_value_list(ctr_tag, "NVM_E_HARDWARE"):
                dem_params.addDemEventRef(ref)
            nvm.setNvmDemEventParameterRefs(dem_params)
            self.logger.debug("Read NvmDemEventParameterRefs")
```

- [ ] **Step 5: Rewrite read_report_to_dem**

```python
    def read_report_to_dem(self, element: ET.Element, nvm: NvM):
        """Parse ReportToDem container from XDM.

        Implements: SWR_NVM_00009
        """
        ctr_tag = self.find_ctr_tag(element, "ReportToDem")
        if ctr_tag is not None:
            report = ReportToDem(nvm, ctr_tag.attrib["name"])
            report.setNvMUserCalloutFunctionProductionErrors(
                self.read_optional_value(ctr_tag, "NvMUserCalloutFunctionProductionErrors"))
            report.setNvMUserCalloutFunctionPassedProductionErrors(
                self.read_optional_value(ctr_tag, "NvMUserCalloutFunctionPassedProductionErrors"))
            report.setNvMIntegrityFailedReportToDem(
                self.read_optional_value(ctr_tag, "NvMIntegrityFailedReportToDem"))
            report.setNvMIntegrityFailedReportToDemDetErrorId(
                self.read_optional_value(ctr_tag, "NvMIntegrityFailedReportToDemDetErrorId"))
            report.setNvMRequestFailedReportToDem(
                self.read_optional_value(ctr_tag, "NvMRequestFailedReportToDem"))
            report.setNvMRequestFailedReportToDemDetErrorId(
                self.read_optional_value(ctr_tag, "NvMRequestFailedReportToDemDetErrorId"))
            report.setNvMWrongBlockIdReportToDem(
                self.read_optional_value(ctr_tag, "NvMWrongBlockIdReportToDem"))
            report.setNvMWrongBlockIdReportToDemDetErrorId(
                self.read_optional_value(ctr_tag, "NvMWrongBlockIdReportToDemDetErrorId"))
            report.setNvMLossOfRedundancyReportToDem(
                self.read_optional_value(ctr_tag, "NvMLossOfRedundancyReportToDem"))
            report.setNvMLossOfRedundancyReportToDemDetErrorId(
                self.read_optional_value(ctr_tag, "NvMLossOfRedundancyReportToDemDetErrorId"))
            report.setNvMQueueOverflowReportToDem(
                self.read_optional_value(ctr_tag, "NvMQueueOverflowReportToDem"))
            report.setNvMQueueOverflowReportToDemDetErrorId(
                self.read_optional_value(ctr_tag, "NvMQueueOverflowReportToDemDetErrorId"))
            report.setNvMVerifyFailedReportToDem(
                self.read_optional_value(ctr_tag, "NvMVerifyFailedReportToDem"))
            report.setNvMVerifyFailedReportToDemDetErrorId(
                self.read_optional_value(ctr_tag, "NvMVerifyFailedReportToDemDetErrorId"))
            report.setNvMWriteProtectedReportToDem(
                self.read_optional_value(ctr_tag, "NvMWriteProtectedReportToDem"))
            report.setNvMWriteProtectedReportToDemDetErrorId(
                self.read_optional_value(ctr_tag, "NvMWriteProtectedReportToDemDetErrorId"))
            report.setNvMBlockCheckReportProdError(
                self.read_optional_value(ctr_tag, "NvMBlockCheckReportProdError"))
            report.setNvMBlockCheckReportProdErrorId(
                self.read_optional_value(ctr_tag, "NvMBlockCheckReportProdErrorId"))
            nvm.setReportToDem(report)
            self.logger.debug("Read ReportToDem")
```

- [ ] **Step 6: Rewrite read_multi_core_callout**

```python
    def read_multi_core_callout(self, element: ET.Element, nvm: NvM):
        """Parse MultiCoreCallout container from XDM.

        Implements: SWR_NVM_00010
        """
        ctr_tag = self.find_ctr_tag(element, "MultiCoreCallout")
        if ctr_tag is not None:
            callout = MultiCoreCallout(nvm, ctr_tag.attrib["name"])
            callout.setNvMReadBlockCallout(self.read_optional_value(ctr_tag, "NvMReadBlockCallout"))
            callout.setNvMWriteBlockCallout(self.read_optional_value(ctr_tag, "NvMWriteBlockCallout"))
            callout.setNvMRestoreBlockDefaultsCallout(self.read_optional_value(ctr_tag, "NvMRestoreBlockDefaultsCallout"))
            callout.setNvMReadPRAMBlockCallout(self.read_optional_value(ctr_tag, "NvMReadPRAMBlockCallout"))
            callout.setNvMWritePRAMBlockCallout(self.read_optional_value(ctr_tag, "NvMWritePRAMBlockCallout"))
            callout.setNvMRestorePRAMBlockDefaultsCallout(self.read_optional_value(ctr_tag, "NvMRestorePRAMBlockDefaultsCallout"))
            callout.setNvMEraseNvBlockCallout(self.read_optional_value(ctr_tag, "NvMEraseNvBlockCallout"))
            callout.setNvMInvalidateNvBlockCallout(self.read_optional_value(ctr_tag, "NvMInvalidateNvBlockCallout"))
            callout.setNvMCancelJobsCallout(self.read_optional_value(ctr_tag, "NvMCancelJobsCallout"))
            nvm.setMultiCoreCallout(callout)
            self.logger.debug("Read MultiCoreCallout")
```

- [ ] **Step 7: Add 12 new fields to read_nvm_common**

Add these lines after existing field reads in `read_nvm_common` (after the `setNvMCsmRetryCounter` line):
```python
            nvm_common.setNvMSoftwareChangeCallout(self.read_optional_value(ctr_tag, "NvMSoftwareChangeCallout"))
            nvm_common.setNvMDrvModeSwitch(self.read_optional_value(ctr_tag, "NvMDrvModeSwitch"))
            nvm_common.setNvMCancelInternalOperations(self.read_optional_value(ctr_tag, "NvMCancelInternalOperations"))
            nvm_common.setNvMReadBlockHook(self.read_optional_value(ctr_tag, "NvMReadBlockHook"))
            nvm_common.setNvMRteUsage(self.read_optional_value(ctr_tag, "NvMRteUsage"))
            for header in self.read_list_value_list(ctr_tag, "NvMUserHeader"):
                nvm_common.addNvMUserHeader(header)
            nvm_common.setNvMWriteBlockHook(self.read_optional_value(ctr_tag, "NvMWriteBlockHook"))
            nvm_common.setNvMRedundantRecovery(self.read_optional_value(ctr_tag, "NvMRedundantRecovery"))
            nvm_common.setNvMExportBlockLengths(self.read_optional_value(ctr_tag, "NvMExportBlockLengths"))
            nvm_common.setNvMResultErasedBlocks(self.read_optional_value(ctr_tag, "NvMResultErasedBlocks"))
            nvm_common.setNvMEnableLegacySymbolicNames(self.read_optional_value(ctr_tag, "NvMEnableLegacySymbolicNames"))
            nvm_common.setNvMResetRamBlockAfterReset(self.read_optional_value(ctr_tag, "NvMResetRamBlockAfterReset"))
```

Check if `read_list_value_list` exists on `AbstractEbModelParser`. If not, grep for existing list reading patterns used in other parsers (e.g. Os parser read_os_isrs with `d:lst`).

Run: `grep -n "read_list" src/eb_model/parser/core/eb_parser.py`

If it doesn't exist, use inline approach in `read_nvm_common`:
```python
            header_lst = self.find_lst_tag(ctr_tag, "NvMUserHeader")
            if header_lst is not None:
                for var in header_lst.findall("d:var", self.nsmap):
                    value = var.get("value")
                    if value:
                        nvm_common.addNvMUserHeader(value)
```

- [ ] **Step 8: Add fields to read_nvm_block_descriptors**

Add these lines to `read_nvm_block_descriptors`, after existing field reads and before `self.read_nvm_init_block_callback`:
```python
            nvm_block.setNvMEnBlockCheck(self.read_optional_value(ctr_tag, "NvMEnBlockCheck"))
            nvm_block.setNvMEnableBlockCryptoSecurityHandling(self.read_optional_value(ctr_tag, "NvMEnableBlockCryptoSecurityHandling"))
            nvm_block.setNvMCryptoExtraInfoSize(self.read_optional_value(ctr_tag, "NvMCryptoExtraInfoSize"))
            nvm_block.setNvMBcEnSetAPI(self.read_optional_value(ctr_tag, "NvMBcEnSetAPI"))
            nvm_block.setNvMBcEnAutoStart(self.read_optional_value(ctr_tag, "NvMBcEnAutoStart"))
            nvm_block.setNvMBcEnCrcComp(self.read_optional_value(ctr_tag, "NvMBcEnCrcComp"))
            nvm_block.setNvMBcEnRamComp(self.read_optional_value(ctr_tag, "NvMBcEnRamComp"))
            nvm_block.setNvMBcEnReddCopiesComp(self.read_optional_value(ctr_tag, "NvMBcEnReddCopiesComp"))
            nvm_block.setNvMBcEnAutoRepair(self.read_optional_value(ctr_tag, "NvMBcEnAutoRepair"))
            nvm_block.setNvMBcDelayCounter(self.read_optional_value(ctr_tag, "NvMBcDelayCounter"))
            nvm_block.setNvMWriteBlockOnce(self.read_optional_value(ctr_tag, "NvMWriteBlockOnce"))
            nvm_block.setNvMWriteVerification(self.read_optional_value(ctr_tag, "NvMWriteVerification"))
            nvm_block.setNvMWriteVerificationDataSize(self.read_optional_value(ctr_tag, "NvMWriteVerificationDataSize"))
            nvm_block.setNvMPreWriteDataComp(self.read_optional_value(ctr_tag, "NvMPreWriteDataComp"))
            nvm_block.setNvMPreWriteDataCompDataSize(self.read_optional_value(ctr_tag, "NvMPreWriteDataCompDataSize"))
```

Add these lines after existing field reads in `read_nvm_block_descriptors` for the model-fields-that-exist-but-were-not-parsed:
```python
            nvm_block.setNvMBlockWriteProt(self.read_optional_value(ctr_tag, "NvMBlockWriteProt"))
            nvm_block.setNvMBswMBlockStatusInformation(self.read_optional_value(ctr_tag, "NvMBswMBlockStatusInformation"))
            nvm_block.setNvMBlockUseAutoValidation(self.read_optional_value(ctr_tag, "NvMBlockUseAutoValidation"))
            nvm_block.setNvMBlockUseCompression(self.read_optional_value(ctr_tag, "NvMBlockUseCompression"))
            nvm_block.setNvMBlockUsePort(self.read_optional_value(ctr_tag, "NvMBlockUsePort"))
            nvm_block.setNvMBlockUseSetRamBlockStatus(self.read_optional_value(ctr_tag, "NvMBlockUseSetRamBlockStatus"))
            nvm_block.setNvMCalcRamBlockCrc(self.read_optional_value(ctr_tag, "NvMCalcRamBlockCrc"))
            nvm_block.setNvMMaxNumOfReadRetries(self.read_optional_value(ctr_tag, "NvMMaxNumOfReadRetries"))
            nvm_block.setNvMMaxNumOfWriteRetries(self.read_optional_value(ctr_tag, "NvMMaxNumOfWriteRetries"))
            nvm_block.setNvMSelectBlockForFirstInitAll(self.read_optional_value(ctr_tag, "NvMSelectBlockForFirstInitAll"))
            nvm_block.setNvMStaticBlockIDCheck(self.read_optional_value(ctr_tag, "NvMStaticBlockIDCheck"))
            nvm_block.setNvMNvramDeviceId(self.read_optional_value(ctr_tag, "NvMNvramDeviceId"))
            nvm_block.setNvMBlockHeaderInclude(self.read_optional_value(ctr_tag, "NvMBlockHeaderInclude"))
            nvm_block.setNvMBlockCipheringRef(self.read_optional_ref_value(ctr_tag, "NvMBlockCipheringRef"))
```

- [ ] **Step 9: Run existing tests**

Run: `python -m pytest tests/parser/mem_stack/ -v --tb=short`
Expected: Existing tests pass (they should, since we kept the same method signatures)

- [ ] **Step 10: Commit**

```bash
git add src/eb_model/parser/mem_stack/nvm_xdm_parser.py
git commit -m "feat: add NvM parser methods for all fields in data/NvM.xdm"
```

---

### Task 6: Write parser unit tests for all new read methods

**Files:**
- Modify: `tests/parser/mem_stack/test_nvm_xdm_parser.py`

- [ ] **Step 1: Add test for read_nvm_defensive_programming**

```python
    def test_read_nvm_defensive_programming(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="NvMDefensiveProgramming" type="IDENTIFIABLE">
                <d:var name="NvMDefProgEnabled" type="BOOLEAN" value="true"/>
                <d:var name="NvMPrecondAssertEnabled" type="BOOLEAN" value="false"/>
                <d:var name="NvMPostcondAssertEnabled" type="BOOLEAN" value="false"/>
                <d:var name="NvMStaticAssertEnabled" type="BOOLEAN" value="true"/>
                <d:var name="NvMUnreachAssertEnabled" type="BOOLEAN" value="false"/>
                <d:var name="NvMInvariantAssertEnabled" type="BOOLEAN" value="false"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        nvm = model.getNvM()
        self.parser.read_nvm_defensive_programming(element, nvm)
        defensive = nvm.getNvMDefensiveProgramming()
        assert defensive is not None
        assert defensive.getNvMDefProgEnabled() is True
        assert defensive.getNvMPrecondAssertEnabled() is False
        assert defensive.getNvMStaticAssertEnabled() is True
        assert defensive.getNvMInvariantAssertEnabled() is False
```

- [ ] **Step 2: Add test for read_nvm_common_crypto_security_parameters**

```python
    def test_read_nvm_common_crypto_security_parameters(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="NvMCommonCryptoSecurityParameters" type="IDENTIFIABLE">
                <d:var name="NvMEnableCryptoSecurityHooks" type="BOOLEAN" value="true"/>
                <d:var name="NvMCryptoReadHook" type="FUNCTION-NAME" value="NvM_CryptoRead"/>
                <d:var name="NvMCryptoWriteHook" type="FUNCTION-NAME" value="NvM_CryptoWrite"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        nvm = model.getNvM()
        self.parser.read_nvm_common_crypto_security_parameters(element, nvm)
        crypto = nvm.getNvMCommonCryptoSecurityParameters()
        assert crypto is not None
        assert crypto.getNvMEnableCryptoSecurityHooks() is True
        assert crypto.getNvMCryptoReadHook() == "NvM_CryptoRead"
        assert crypto.getNvMCryptoWriteHook() == "NvM_CryptoWrite"
```

- [ ] **Step 3: Add test for read_nvm_service_api**

```python
    def test_read_nvm_service_api(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="NvMServiceAPI" type="IDENTIFIABLE">
                <d:var name="NvMEnableASR32ServiceAPI" type="BOOLEAN" value="false"/>
                <d:var name="NvMEnableASR40ServiceAPI" type="BOOLEAN" value="false"/>
                <d:var name="NvMEnableASR42ServiceAPI" type="BOOLEAN" value="true"/>
                <d:var name="NvMDefaultASRServiceAPI" type="ENUMERATION" value="AUTOSAR_42"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        nvm = model.getNvM()
        self.parser.read_nvm_service_api(element, nvm)
        api = nvm.getNvMServiceAPI()
        assert api is not None
        assert api.getNvMEnableASR32ServiceAPI() is False
        assert api.getNvMEnableASR42ServiceAPI() is True
        assert api.getNvMDefaultASRServiceAPI() == "AUTOSAR_42"
```

- [ ] **Step 4: Add test for read_nvm_dem_event_parameter_refs**

```python
    def test_read_nvm_dem_event_parameter_refs(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="NvmDemEventParameterRefs" type="IDENTIFIABLE">
                <d:ref name="NVM_E_INTEGRITY_FAILED" type="REFERENCE" value="ASPath:/Dem/Dem/DemEvent"/>
                <d:ref name="NVM_E_REQ_FAILED" type="REFERENCE" value="ASPath:/Dem/Dem/DemEvent2"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        nvm = model.getNvM()
        self.parser.read_nvm_dem_event_parameter_refs(element, nvm)
        dem_params = nvm.getNvmDemEventParameterRefs()
        assert dem_params is not None
        assert len(dem_params.getDemEventRefList()) == 2
```

- [ ] **Step 5: Add test for read_nvm_common with new fields**

Append to existing `test_read_nvm_common` (add assertion lines at the end):
```python
        assert common.getNvMCompiledConfigId() == 1
        assert common.getNvMDrvModeSwitch() is False
        assert common.getNvMCancelInternalOperations() is False
        assert common.getNvMReadBlockHook() is False
        assert common.getNvMRteUsage() is True
        assert common.getNvMWriteBlockHook() is False
        assert common.getNvMRedundantRecovery() == "NVM_RECOVERY_ON_REQUEST"
        assert common.getNvMExportBlockLengths() is False
        assert common.getNvMResultErasedBlocks() == "MEMIF_BLOCK_INCONSISTENT"
        assert common.getNvMEnableLegacySymbolicNames() is True
        assert common.getNvMResetRamBlockAfterReset() is False
```

Update the `test_read_nvm_common` XML content to include:
```xml
                <d:var name="NvMSoftwareChangeCallout" type="FUNCTION-NAME" value=""/>
                <d:var name="NvMDrvModeSwitch" type="BOOLEAN" value="false"/>
                <d:var name="NvMCancelInternalOperations" type="BOOLEAN" value="false"/>
                <d:var name="NvMReadBlockHook" type="BOOLEAN" value="false"/>
                <d:var name="NvMRteUsage" type="BOOLEAN" value="true"/>
                <d:var name="NvMWriteBlockHook" type="BOOLEAN" value="false"/>
                <d:var name="NvMRedundantRecovery" type="ENUMERATION" value="NVM_RECOVERY_ON_REQUEST"/>
                <d:var name="NvMExportBlockLengths" type="BOOLEAN" value="false"/>
                <d:var name="NvMResultErasedBlocks" type="ENUMERATION" value="MEMIF_BLOCK_INCONSISTENT"/>
                <d:var name="NvMEnableLegacySymbolicNames" type="BOOLEAN" value="true"/>
                <d:var name="NvMResetRamBlockAfterReset" type="BOOLEAN" value="false"/>
```

- [ ] **Step 6: Add test for read_report_to_dem**

```python
    def test_read_report_to_dem(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="ReportToDem" type="IDENTIFIABLE">
                <d:var name="NvMIntegrityFailedReportToDem" type="ENUMERATION" value="DISABLE"/>
                <d:var name="NvMIntegrityFailedReportToDemDetErrorId" type="INTEGER" value="25"/>
                <d:var name="NvMRequestFailedReportToDem" type="ENUMERATION" value="ENABLE"/>
                <d:var name="NvMRequestFailedReportToDemDetErrorId" type="INTEGER" value="26"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        nvm = model.getNvM()
        self.parser.read_report_to_dem(element, nvm)
        report = nvm.getReportToDem()
        assert report is not None
        assert report.getNvMIntegrityFailedReportToDem() == "DISABLE"
        assert report.getNvMIntegrityFailedReportToDemDetErrorId() == 25
        assert report.getNvMRequestFailedReportToDem() == "ENABLE"
        assert report.getNvMRequestFailedReportToDemDetErrorId() == 26
```

(Remove the old `test_read_report_to_dem` since it used the removed `NvMReportStorageFailed`/`NvMReportVerificationFailed` fields.)

- [ ] **Step 7: Add test for read_multi_core_callout**

```python
    def test_read_multi_core_callout(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="MultiCoreCallout" type="IDENTIFIABLE">
                <d:var name="NvMReadBlockCallout" type="FUNCTION-NAME" value="NvM_ReadBlock_Callout"/>
                <d:var name="NvMWriteBlockCallout" type="FUNCTION-NAME" value="NvM_WriteBlock_Callout"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        nvm = model.getNvM()
        self.parser.read_multi_core_callout(element, nvm)
        callout = nvm.getMultiCoreCallout()
        assert callout is not None
        assert callout.getNvMReadBlockCallout() == "NvM_ReadBlock_Callout"
        assert callout.getNvMWriteBlockCallout() == "NvM_WriteBlock_Callout"
```

- [ ] **Step 8: Add test for parse() with mock data (integration-style)**

```python
    def test_parse_with_mock_data(self):
        """Test full parse() using MOCK_NVM_XDM for end-to-end parser coverage."""
        from tests.mock_data import MOCK_NVM_XDM
        element = ET.fromstring(MOCK_NVM_XDM)
        EBModel._EBModel__instance = None
        model = EBModel.getInstance()
        self.parser.parse(element, model)
        nvm = model.getNvM()

        # Verify version info
        assert nvm.getCommonPublishedInformation() is not None
        assert nvm.getCommonPublishedInformation().getArMajorVersion() == 4

        # Verify NvMCommon
        common = nvm.getNvMCommon()
        assert common is not None
        assert common.getNvMCompiledConfigId() == 1
        assert common.getNvMDevErrorDetect() is True
        assert common.getNvMVersionInfoApi() is True
        assert common.getNvMRedundantRecovery() == "NVM_RECOVERY_ON_REQUEST"
        assert common.getNvMRteUsage() is True
        assert common.getNvMDrvModeSwitch() is False

        # Verify DefensiveProgramming
        defensive = nvm.getNvMDefensiveProgramming()
        assert defensive is not None
        assert defensive.getNvMDefProgEnabled() is False

        # Verify CryptoSecurityParameters
        crypto = nvm.getNvMCommonCryptoSecurityParameters()
        assert crypto is not None
        assert crypto.getNvMEnableCryptoSecurityHooks() is False

        # Verify ServiceAPI
        api = nvm.getNvMServiceAPI()
        assert api is not None
        assert api.getNvMDefaultASRServiceAPI() == "AUTOSAR_42"

        # Verify DemEventRefs
        dem_params = nvm.getNvmDemEventParameterRefs()
        assert dem_params is not None

        # Verify ReportToDem
        report = nvm.getReportToDem()
        assert report is not None
        assert report.getNvMIntegrityFailedReportToDem() == "DISABLE"

        # Verify MultiCoreCallout
        callout = nvm.getMultiCoreCallout()
        assert callout is not None

        # Verify BlockDescriptors
        blocks = nvm.getNvMBlockDescriptorList()
        assert len(blocks) == 1
        block = blocks[0]
        assert block.getName() == "NvMBlock_ConfigID"
        assert block.getNvMNvramBlockIdentifier() == 1
        assert block.getNvMNvBlockLength() == 2
        assert block.getNvMEnBlockCheck() is False
        assert block.getNvMBcEnSetAPI() is True
        assert block.getNvMBcDelayCounter() == 0

        # Verify FeeRef
        ref = block.getNvMTargetBlockReference()
        assert ref is not None
        assert isinstance(ref, NvMFeeRef)

        # Verify InitBlockCallback
        assert block.getNvMInitBlockCallback() is not None

        # Verify SingleBlockCallback
        assert block.getNvMSingleBlockCallback() is not None

        # Verify PublishedInformation
        assert nvm.getPublishedInformation() is not None
```

- [ ] **Step 9: Run all parser tests**

Run: `python -m pytest tests/parser/mem_stack/test_nvm_xdm_parser.py -v --tb=short`
Expected: ALL tests pass

- [ ] **Step 10: Commit**

```bash
git add tests/parser/mem_stack/test_nvm_xdm_parser.py
git commit -m "test: add parser tests for all NvM read methods"
```

---

### Task 7: Update NvM Reporter

**Files:**
- Modify: `src/eb_model/reporter/excel_reporter/mem_stack/nvm_xdm.py`
- Modify: `tests/reporter/excel_reporter/mem_stack/test_nvm_xdm.py`

- [ ] **Step 1: Fix write_nvm_general to include more fields**

Replace `write_nvm_general` to read from actual model data instead of hardcoding:
```python
    def write_nvm_general(self, doc: EBModel):
        sheet = self.wb.create_sheet("General", 0)

        title_row = ["Key", "Value"]
        self.write_title_row(sheet, title_row)

        nvm_common = doc.getNvM().getNvMCommon()

        if nvm_common is None:
            self.logger.error("NvMCommon is Invalid and General updating is skipped.")
            return

        row = 2
        rows_data = [
            ("NvMCompiledConfigId", nvm_common.getNvMCompiledConfigId()),
            ("NvMDatasetSelectionBits", nvm_common.getNvMDatasetSelectionBits()),
            ("NvMApiConfigClass", nvm_common.getNvMApiConfigClass()),
            ("NvMDevErrorDetect", nvm_common.getNvMDevErrorDetect()),
            ("NvMDynamicConfiguration", nvm_common.getNvMDynamicConfiguration()),
            ("NvMJobPrioritization", nvm_common.getNvMJobPrioritization()),
            ("NvMMainFunctionPeriod", nvm_common.getNvMMainFunctionPeriod()),
            ("NvMPollingMode", nvm_common.getNvMPollingMode()),
            ("NvMRteUsage", nvm_common.getNvMRteUsage()),
            ("NvMVersionInfoApi", nvm_common.getNvMVersionInfoApi()),
            ("NvMMemAccUsage", nvm_common.getNvMMemAccUsage()),
            ("NvMBufferAlignmentValue", nvm_common.getNvMBufferAlignmentValue()),
            ("NvMRedundantRecovery", nvm_common.getNvMRedundantRecovery()),
        ]
        for key, value in rows_data:
            self.write_cell(sheet, row, 1, key)
            self.write_cell_center(sheet, row, 2, value)
            row += 1

        self.auto_width(sheet)
```

- [ ] **Step 2: Fix write_nvm_block_descriptors — remove NvMEaRef NotImplementedError, add more columns**

Replace the `NvMEaRef` handling at lines 84-88:
```python
            if block_reference is not None:
                if isinstance(block_reference, NvMFeeRef):
                    self.write_cell(sheet, row, 22, block_reference.getNvMNameOfFeeBlock().getShortName())
                elif isinstance(block_reference, NvMEaRef):
                    self.write_cell(sheet, row, 22, block_reference.getNvMNameOfEaBlock().getShortName())
```

- [ ] **Step 3: Remove hardcoded retry values, use model data**

Replace lines 30-35 (hardcoded retries) with:
```python
        self.write_cell(sheet, row, 1, "NvMMaxNumOfReadRetries")
        self.write_cell_center(sheet, row, 2, nvm_common.getNvMMaxNumOfReadRetries())
        row += 1
        self.write_cell(sheet, row, 1, "NvMMaxNumOfWriteRetries")
        self.write_cell_center(sheet, row, 2, nvm_common.getNvMMaxNumOfWriteRetries())
        row += 1
```

Wait — `NvMMaxNumOfReadRetries` and `NvMMaxNumOfWriteRetries` are on `NvMBlockDescriptor`, not `NvMCommon`. Looking at the data again... they're on NvMBlockDescriptor indeed. The reporter's General sheet hardcodes them which is wrong. Better to just remove these from General since they don't belong there, or read from the first block descriptor. Let me just remove the hardcoded rows.

- [ ] **Step 4: Write updated reporter tests**

Replace `tests/reporter/excel_reporter/mem_stack/test_nvm_xdm.py` content:
```python
"""
NvM Excel Reporter Tests.

Implements:
    - TC_UNIT_REPORTER_00017: NvM Excel Reporter - File Creation
"""
import os
import tempfile
from openpyxl import load_workbook
from eb_model.reporter.excel_reporter.mem_stack.nvm_xdm import NvMXdmXlsWriter
from eb_model.models.core.eb_doc import EBModel
from eb_model.models.mem_stack.nvm_xdm import NvMCommon
from tests.mock_data import MOCK_NVM_XDM
import xml.etree.ElementTree as ET
from eb_model.parser.mem_stack.nvm_xdm_parser import NvMXdmParser


class TestNvMXdmXlsWriter:

    def _create_populated_doc(self):
        """Parse MOCK_NVM_XDM to create a fully populated EBModel."""
        EBModel._EBModel__instance = None
        doc = EBModel.getInstance()
        parser = NvMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }
        element = ET.fromstring(MOCK_NVM_XDM)
        parser.parse(element, doc)
        return doc

    def test_write_creates_excel_file(self):
        """Test that write() creates a valid Excel file."""
        writer = NvMXdmXlsWriter()
        doc = self._create_populated_doc()

        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
            filename = f.name

        try:
            writer.write(filename, doc, options={})
            assert os.path.exists(filename)
            assert os.path.getsize(filename) > 0
            wb = load_workbook(filename)
            assert len(wb.sheetnames) > 0
            wb.close()
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_write_general_sheet_populated(self):
        """Test General sheet contains expected data."""
        writer = NvMXdmXlsWriter()
        doc = self._create_populated_doc()

        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
            filename = f.name

        try:
            writer.write(filename, doc, options={})
            wb = load_workbook(filename)
            ws = wb["General"]
            # Check some values from General sheet
            values = {}
            for row in ws.iter_rows(min_row=2, max_col=2, values_only=True):
                if row[0]:
                    values[row[0]] = row[1]
            assert values.get("NvMCompiledConfigId") == 1
            assert values.get("NvMDevErrorDetect") is True
            wb.close()
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_write_block_list_sheet_populated(self):
        """Test Block List sheet contains block data."""
        writer = NvMXdmXlsWriter()
        doc = self._create_populated_doc()

        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
            filename = f.name

        try:
            writer.write(filename, doc, options={})
            wb = load_workbook(filename)
            ws = wb["Block List"]
            # Should have header + 1 data row
            assert ws.max_row >= 2
            # Check BlockId value
            block_id = ws.cell(row=2, column=1).value
            assert block_id == 1
            wb.close()
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_write_bsw_distribution_sheet(self):
        """Test BSW Distribution sheet is created."""
        writer = NvMXdmXlsWriter()
        doc = self._create_populated_doc()

        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
            filename = f.name

        try:
            writer.write(filename, doc, options={})
            wb = load_workbook(filename)
            assert "BSW Distribution" in wb.sheetnames
            ws = wb["BSW Distribution"]
            assert ws.max_row >= 1
            wb.close()
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_write_nvm_common_none_skips_general(self):
        """Test that None NvMCommon skips General sheet safely."""
        writer = NvMXdmXlsWriter()
        EBModel._EBModel__instance = None
        doc = EBModel.getInstance()
        # Don't populate NvMCommon

        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
            filename = f.name

        try:
            writer.write(filename, doc, options={})
            wb = load_workbook(filename)
            ws = wb["General"]
            # Only title row should exist
            assert ws.max_row == 1 or ws.max_row is None
            wb.close()
        finally:
            if os.path.exists(filename):
                os.remove(filename)
```

- [ ] **Step 5: Run all NvM tests**

Run: `python -m pytest tests/parser/mem_stack/ tests/models/mem_stack/ tests/reporter/excel_reporter/mem_stack/ -v --tb=short`
Expected: ALL pass

- [ ] **Step 6: Run full test suite to check for regressions**

Run: `python -m pytest --tb=short`
Expected: All 509+ tests pass

- [ ] **Step 7: Commit**

```bash
git add src/eb_model/reporter/excel_reporter/mem_stack/nvm_xdm.py tests/reporter/excel_reporter/mem_stack/test_nvm_xdm.py
git commit -m "feat: update NvM reporter to use model data, add NvMEaRef support"
```

---

### Task 8: Final coverage verification and cleanup

**Files:**
- All NvM-related files

- [ ] **Step 1: Run coverage for NvM components**

Run: `python -m pytest tests/parser/mem_stack/test_nvm_xdm_parser.py tests/models/mem_stack/test_nvm_xdm.py tests/reporter/excel_reporter/mem_stack/test_nvm_xdm.py --cov=src/eb_model/parser/mem_stack/nvm_xdm_parser --cov=src/eb_model/models/mem_stack/nvm_xdm --cov=src/eb_model/reporter/excel_reporter/mem_stack/nvm_xdm --cov-report=term-missing`

Expected targets:
- `nvm_xdm_parser.py`: >=95%
- `nvm_xdm.py` (model): >=80%
- `nvm_xdm.py` (reporter): >=85%

- [ ] **Step 2: Check for any remaining old method references**

Run: `grep -r "NvMNullPointerCheck\|NvMParameterCheck\|NvMReportStorageFailed\|NvMReportVerificationFailed\|getNvMCryptoPrimitive\|getNvMKeyAddress" src/ tests/ --include="*.py"`
Expected: No hits

- [ ] **Step 3: Final full test run**

Run: `python -m pytest --tb=short`
Expected: All tests pass

- [ ] **Step 4: Commit any remaining fixes**

```bash
git add -A
git commit -m "chore: final cleanup after NvM implementation alignment"
```
