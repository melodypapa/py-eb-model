"""
Shared mock XDM data for self-contained OS tests.

Contains a comprehensive mock Os.xdm XML string with all major
entity types, eliminating dependency on external data files.
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
</datamodel>"""
