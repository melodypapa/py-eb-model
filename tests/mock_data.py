"""
Shared mock XDM data for self-contained tests.

Contains comprehensive mock XDM XML strings for OS and NvM modules,
eliminating dependency on external data files.
"""

MOCK_OS_XDM = """<?xml version="1.0"?>
<datamodel version="7.0"
           xmlns="http://www.tresos.de/_projects/DataModel2/16/root.xsd"
           xmlns:a="http://www.tresos.de/_projects/DataModel2/16/attribute.xsd"
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
      <d:ctr name="Os" type="AR-PACKAGE">
        <d:lst type="ELEMENTS">
          <d:chc name="Os" type="AR-ELEMENT" value="MODULE-CONFIGURATION">
            <d:ctr type="MODULE-CONFIGURATION">
              <a:a name="DEF" value="ASPath:/Mock/Os"/>
              <a:a name="MODULE-DESCRIPTION-REF" value="ASPath:/BswModule_Os/BswImpl_Os"/>
              <a:a name="UUID" value="00000000-0000-0000-0000-000000000001"/>
              <d:ctr name="CommonPublishedInformation" type="IDENTIFIABLE">
                <a:a name="UUID" value="00000000-0000-0000-0000-000000000002"/>
                <d:var name="ArMajorVersion" type="INTEGER" value="4"/>
                <d:var name="ArMinorVersion" type="INTEGER" value="3"/>
                <d:var name="ArPatchVersion" type="INTEGER" value="0"/>
                <d:var name="SwMajorVersion" type="INTEGER" value="1"/>
                <d:var name="SwMinorVersion" type="INTEGER" value="2"/>
                <d:var name="SwPatchVersion" type="INTEGER" value="3"/>
              </d:ctr>
              <d:ctr name="PublishedInformation">
                <d:var name="PbcfgMSupport" type="BOOLEAN" value="true"/>
              </d:ctr>
              <d:lst name="OsTask" type="MAP">
                <d:ctr name="Task1">
                  <d:var name="OsTaskPriority" type="INTEGER" value="5"/>
                  <d:var name="OsTaskActivation" type="INTEGER" value="1"/>
                  <d:var name="OsTaskSchedule" type="ENUMERATION" value="FULL"/>
                  <d:var name="OsStacksize" type="INTEGER" value="1024"/>
                  <d:var name="OsTaskType" type="ENUMERATION" value="BASIC"/>
                </d:ctr>
                <d:ctr name="Task2">
                  <d:var name="OsTaskPriority" type="INTEGER" value="3"/>
                  <d:var name="OsTaskActivation" type="INTEGER" value="2"/>
                  <d:var name="OsTaskSchedule" type="ENUMERATION" value="FULL"/>
                  <d:var name="OsStacksize" type="INTEGER" value="2048"/>
                  <d:var name="OsTaskType" type="ENUMERATION" value="EXTENDED"/>
                </d:ctr>
              </d:lst>
              <d:lst name="OsIsr" type="MAP">
                <d:ctr name="Isr1">
                  <d:var name="OsIsrCategory" type="INTEGER" value="1"/>
                  <d:var name="OsStacksize" type="INTEGER" value="512"/>
                  <d:var name="OsIsrPriority" type="INTEGER" value="10"/>
                  <d:var name="OsIsrVector" type="INTEGER" value="100"/>
                </d:ctr>
                <d:ctr name="Isr2">
                  <d:var name="OsIsrCategory" type="INTEGER" value="2"/>
                  <d:var name="OsStacksize" type="INTEGER" value="1024"/>
                  <d:var name="OsIsrPriority" type="INTEGER" value="8"/>
                  <d:var name="OsIsrVector" type="INTEGER" value="200"/>
                </d:ctr>
              </d:lst>
              <d:lst name="OsScheduleTable" type="MAP">
                <d:ctr name="ScheduleTable1">
                  <d:var name="OsScheduleTableDuration" type="INTEGER" value="1000"/>
                  <d:var name="OsScheduleTableRepeating" type="BOOLEAN" value="true"/>
                  <d:ref name="OsScheduleTableCounterRef" type="REFERENCE" value="ASPath:/Os/Counter1"/>
                  <d:lst name="OsScheduleTableExpiryPoint" type="MAP">
                    <d:ctr name="ExpiryPoint1">
                      <d:var name="OsScheduleTblExpPointOffset" type="INTEGER" value="100"/>
                      <d:lst name="OsScheduleTableTaskActivation" type="MAP">
                        <d:ctr name="Activation1">
                          <d:ref name="OsScheduleTableActivateTaskRef" type="REFERENCE" value="ASPath:/Os/Task1"/>
                        </d:ctr>
                      </d:lst>
                    </d:ctr>
                  </d:lst>
                </d:ctr>
              </d:lst>
              <d:lst name="OsCounter" type="MAP">
                <d:ctr name="Counter1">
                  <d:var name="OsCounterMaxAllowedValue" type="INTEGER" value="65535"/>
                  <d:var name="OsCounterMinCycle" type="INTEGER" value="1"/>
                  <d:var name="OsCounterTicksPerBase" type="INTEGER" value="1000"/>
                  <d:var name="OsCounterType" type="ENUMERATION" value="SOFTWARE"/>
                </d:ctr>
                <d:ctr name="Counter2">
                  <d:var name="OsCounterMaxAllowedValue" type="INTEGER" value="255"/>
                  <d:var name="OsCounterMinCycle" type="INTEGER" value="1"/>
                  <d:var name="OsCounterTicksPerBase" type="INTEGER" value="100"/>
                  <d:var name="OsCounterType" type="ENUMERATION" value="HARDWARE"/>
                </d:ctr>
              </d:lst>
              <d:lst name="OsAlarm" type="MAP">
                <d:ctr name="Alarm1">
                  <d:ref name="OsAlarmCounterRef" type="REFERENCE" value="ASPath:/Os/Counter1"/>
                  <d:chc name="OsAlarmAction" value="OsAlarmActivateTask">
                    <d:ctr name="OsAlarmActivateTask">
                      <d:ref name="OsAlarmActivateTaskRef" type="REFERENCE" value="ASPath:/Os/Task1"/>
                    </d:ctr>
                  </d:chc>
                </d:ctr>
              </d:lst>
              <d:lst name="OsApplication" type="MAP">
                <d:ctr name="App1">
                  <d:var name="OsTrusted" type="BOOLEAN" value="true"/>
                  <d:var name="OsApplicationCoreAssignment" type="INTEGER" value="0"/>
                  <d:ref name="OsAppEcucPartitionRef" type="REFERENCE" value="ASPath:/Os/Partition0"/>
                  <d:lst name="OsAppAlarmRef">
                    <d:ref type="REFERENCE" value="ASPath:/Os/Alarm1"/>
                  </d:lst>
                  <d:lst name="OsAppTaskRef">
                    <d:ref type="REFERENCE" value="ASPath:/Os/Task1"/>
                  </d:lst>
                  <d:lst name="OsAppIsrRef">
                    <d:ref type="REFERENCE" value="ASPath:/Os/Isr1"/>
                  </d:lst>
                </d:ctr>
                <d:ctr name="App2">
                  <d:var name="OsTrusted" type="BOOLEAN" value="false"/>
                  <d:var name="OsApplicationCoreAssignment" type="INTEGER" value="1"/>
                  <d:ref name="OsAppEcucPartitionRef" type="REFERENCE" value="ASPath:/Os/Partition1"/>
                  <d:lst name="OsAppTaskRef">
                    <d:ref type="REFERENCE" value="ASPath:/Os/Task2"/>
                  </d:lst>
                  <d:lst name="OsAppIsrRef">
                    <d:ref type="REFERENCE" value="ASPath:/Os/Isr2"/>
                  </d:lst>
                </d:ctr>
              </d:lst>
              <d:lst name="OsResource" type="MAP">
                <d:ctr name="Resource1">
                  <d:var name="OsResourceProperty" type="ENUMERATION" value="STANDARD"/>
                </d:ctr>
                <d:ctr name="Resource2">
                  <d:var name="OsResourceProperty" type="ENUMERATION" value="LINKED"/>
                </d:ctr>
              </d:lst>
              <d:lst name="OsSpinlock" type="MAP">
                <d:ctr name="Spinlock1">
                  <d:var name="OsSpinlockLockMethod" type="ENUMERATION" value="STANDARD"/>
                  <d:ref name="OsSpinlockSuccessor" type="REFERENCE" value="ASPath:/Os/Spinlock2"/>
                </d:ctr>
                <d:ctr name="Spinlock2">
                  <d:var name="OsSpinlockLockMethod" type="ENUMERATION" value="SCHEDULER"/>
                </d:ctr>
              </d:lst>
              <d:ctr name="OsHwIncrementer">
                <d:var name="OsHwIncrementerBase" type="INTEGER" value="0"/>
                <d:var name="OsHwIncrementerMax" type="INTEGER" value="65535"/>
              </d:ctr>
              <d:lst name="OsEvent" type="MAP">
                <d:ctr name="Event1">
                  <d:var name="OsEventMask" type="INTEGER" value="1"/>
                </d:ctr>
                <d:ctr name="Event2">
                  <d:var name="OsEventMask" type="INTEGER" value="2"/>
                </d:ctr>
              </d:lst>
              <d:lst name="OsPeripheralArea" type="MAP">
                <d:ctr name="Peripheral1">
                  <d:var name="OsPeripheralAreaStartAddress" type="INTEGER" value="1073741824"/>
                  <d:var name="OsPeripheralAreaEndAddress" type="INTEGER" value="1073750015"/>
                  <d:var name="OsPeripheralAreaAccessPermission" type="ENUMERATION" value="READ_WRITE"/>
                </d:ctr>
              </d:lst>
              <d:ctr name="OsOS">
                <d:var name="OsScalabilityClass" type="ENUMERATION" value="SC1"/>
                <d:var name="OsNumberOfCores" type="INTEGER" value="2"/>
                <d:var name="OsStackMonitoring" type="BOOLEAN" value="true"/>
                <d:var name="OsUseGetServiceId" type="BOOLEAN" value="false"/>
                <d:var name="OsUseParameterAccess" type="BOOLEAN" value="true"/>
                <d:var name="OsUseResScheduler" type="BOOLEAN" value="true"/>
                <d:var name="OsStatus" type="ENUMERATION" value="STANDARD"/>
              </d:ctr>
              <d:ctr name="OsHooks">
                <d:var name="OsErrorHook" type="BOOLEAN" value="true"/>
                <d:var name="OsShutdownHook" type="BOOLEAN" value="false"/>
                <d:var name="OsStartupHook" type="BOOLEAN" value="true"/>
                <d:var name="OsPreTaskHook" type="BOOLEAN" value="false"/>
                <d:var name="OsPostTaskHook" type="BOOLEAN" value="true"/>
                <d:var name="OsProtectionHook" type="BOOLEAN" value="false"/>
              </d:ctr>
              <d:ctr name="OsMicrokernel">
                <d:ctr name="MkMemoryProtection">
                  <d:lst name="MkMemoryRegion" type="MAP">
                    <d:ctr name="Region1">
                      <d:var name="MkMemoryRegionFlags" type="INTEGER" value="1"/>
                      <d:var name="MkMemoryRegionInitialize" type="BOOLEAN" value="true"/>
                      <d:var name="MkMemoryRegionGlobal" type="BOOLEAN" value="false"/>
                      <d:var name="MkMemoryRegionInitThreadAccess" type="BOOLEAN" value="true"/>
                      <d:var name="MkMemoryRegionIdleThreadAccess" type="BOOLEAN" value="false"/>
                      <d:var name="MkMemoryRegionOsThreadAccess" type="BOOLEAN" value="true"/>
                      <d:var name="MkMemoryRegionErrorHookAccess" type="BOOLEAN" value="true"/>
                      <d:var name="MkMemoryRegionProtHookAccess" type="BOOLEAN" value="true"/>
                      <d:var name="MkMemoryRegionShutdownHookAccess" type="BOOLEAN" value="false"/>
                      <d:var name="MkMemoryRegionShutdownAccess" type="BOOLEAN" value="false"/>
                      <d:var name="MkMemoryRegionInitializePerCore" type="BOOLEAN" value="true"/>
                    </d:ctr>
                  </d:lst>
                </d:ctr>
              </d:ctr>
              <d:lst name="OsCoreConfig" type="MAP">
                <d:ctr name="Core0">
                  <d:var name="OsCoreId" type="INTEGER" value="0"/>
                  <d:var name="OsCoreMainFunction" type="STRING" value="Main_Core0"/>
                  <d:var name="OsCoreStackStartAddress" type="INTEGER" value="536870912"/>
                  <d:var name="OsCoreStackSize" type="INTEGER" value="4096"/>
                </d:ctr>
                <d:ctr name="Core1">
                  <d:var name="OsCoreId" type="INTEGER" value="1"/>
                  <d:var name="OsCoreMainFunction" type="STRING" value="Main_Core1"/>
                  <d:var name="OsCoreStackStartAddress" type="INTEGER" value="536875008"/>
                  <d:var name="OsCoreStackSize" type="INTEGER" value="4096"/>
                </d:ctr>
              </d:lst>
              <d:ctr name="OsAutosarCustomization">
                <d:var name="OsScalableClass" type="ENUMERATION" value="BCC"/>
                <d:var name="OsApplicationType" type="ENUMERATION" value="SYSTEM"/>
              </d:ctr>
            </d:ctr>
          </d:chc>
        </d:lst>
      </d:ctr>
    </d:lst>
  </d:ctr>
</datamodel>
"""

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
