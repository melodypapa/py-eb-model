from eb_model.parser.core.os_xdm_parser import OsXdmParser
from eb_model.models.core.eb_doc import EBModel
from eb_model.models.core.os_xdm import OsAlarmActivateTask, OsAlarmSetEvent, OsAlarmIncrementCounter, OsAlarmCallback

import xml.etree.ElementTree as ET
import pytest


class TestOsXdmParser:
    def test_parser_initialization(self):
        """
        Test that OsXdmParser can be instantiated correctly.

        Implements: TC_UNIT_OS_00001
        """
        parser = OsXdmParser()
        assert parser is not None
        assert parser.os is None

    def test_module_name_validation(self):
        """
        Test that parser validates module name is 'Os' and rejects other modules.

        Implements: TC_UNIT_OS_00001
        """
        # Create XML with Os module
        os_xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:chc type="AR-ELEMENT" value="MODULE-CONFIGURATION" name="Os"/>
            <d:ctr name="CommonPublishedInformation">
                <d:var name="ArMajorVersion" type="INTEGER" value="4"/>
                <d:var name="ArMinorVersion" type="INTEGER" value="3"/>
                <d:var name="ArPatchVersion" type="INTEGER" value="0"/>
                <d:var name="SwMajorVersion" type="INTEGER" value="1"/>
                <d:var name="SwMinorVersion" type="INTEGER" value="2"/>
                <d:var name="SwPatchVersion" type="INTEGER" value="3"/>
            </d:ctr>
        </datamodel>
        """
        os_element = ET.fromstring(os_xml_content)

        # Create XML with invalid module name
        invalid_xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:chc type="AR-ELEMENT" value="MODULE-CONFIGURATION" name="CanIf"/>
            <d:ctr name="CommonPublishedInformation">
                <d:var name="ArMajorVersion" type="INTEGER" value="4"/>
                <d:var name="ArMinorVersion" type="INTEGER" value="3"/>
                <d:var name="ArPatchVersion" type="INTEGER" value="0"/>
                <d:var name="SwMajorVersion" type="INTEGER" value="1"/>
                <d:var name="SwMinorVersion" type="INTEGER" value="2"/>
                <d:var name="SwPatchVersion" type="INTEGER" value="3"/>
            </d:ctr>
        </datamodel>
        """
        invalid_element = ET.fromstring(invalid_xml_content)

        model = EBModel.getInstance()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Should accept Os module without error
        parser.parse(os_element, model)

        # Should raise ValueError for non-Os module
        with pytest.raises(ValueError, match="Invalid.*Os"):
            parser.parse(invalid_element, model)

    def test_version_information_extraction(self):
        """
        Test that parser correctly extracts AUTOSAR and software version information.

        Implements: TC_UNIT_OS_00001
        """
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CommonPublishedInformation">
                <d:var name="ArMajorVersion" type="INTEGER" value="4"/>
                <d:var name="ArMinorVersion" type="INTEGER" value="3"/>
                <d:var name="ArPatchVersion" type="INTEGER" value="0"/>
                <d:var name="SwMajorVersion" type="INTEGER" value="1"/>
                <d:var name="SwMinorVersion" type="INTEGER" value="2"/>
                <d:var name="SwPatchVersion" type="INTEGER" value="3"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        os = model.getOs()

        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_version(element, os)

        # Verify AUTOSAR version
        ar_version = os.getArVersion()
        assert ar_version.getMajorVersion() == 4
        assert ar_version.getMinorVersion() == 3
        assert ar_version.getPatchVersion() == 0
        assert ar_version.getVersion() == "4.3.0"

        # Verify software version
        sw_version = os.getSwVersion()
        assert sw_version.getMajorVersion() == 1
        assert sw_version.getMinorVersion() == 2
        assert sw_version.getPatchVersion() == 3
        assert sw_version.getVersion() == "1.2.3"

    def test_read_os_resources(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsResource" type="MAP">
                <d:ctr name="Resource1">
                    <a:a name="IMPORTER_INFO" value="@CALC(SvcAs,os.resources,1)"/>
                    <d:var name="OsResourceProperty" type="ENUMERATION" value="STANDARD">
                        <d:lst name="OsResourceAccessingApplication">
                            <d:ref type="REFERENCE" value="ASPath:/Os/Os/OsApplication_C0">
                                <a:a name="IMPORTER_INFO" value="@CALC(SvcAs,os.resources,1)"/>
                            </d:ref>
                        </d:lst>
                    </d:var>
                </d:ctr>
                <d:ctr name="Resource2">
                    <d:var name="OsResourceProperty" type="ENUMERATION" value="INTERNAL"/>
                    <d:lst name="OsResourceAccessingApplication"/>
                    <d:ref name="OsResourceLinkedResourceRef" type="REFERENCE" >
                        <a:a name="ENABLE" value="false"/>
                        <a:a name="IMPORTER_INFO" value="@DEF"/>
                    </d:ref>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock Os object
        model = EBModel.getInstance()
        os = model.getOs()

        # Create parser instance
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_os_resources(element, os)

        # Assertions
        resources = os.getOsResourceList()
        assert len(resources) == 2

        resource1 = resources[0]
        assert resource1.getName() == "Resource1"
        assert resource1.getImporterInfo() == "@CALC(SvcAs,os.resources,1)"
        assert resource1.isCalculatedSvcAs() is True
        assert resource1.getOsResourceProperty() == "STANDARD"
        assert len(resource1.getOsResourceAccessingApplicationRefs()) == 1
        for ref in resource1.getOsResourceAccessingApplicationRefs():
            assert ref.getValue() == "/Os/Os/OsApplication_C0"

        resource2 = resources[1]
        assert resource2.getName() == "Resource2"
        assert resource2.getImporterInfo() is None
        assert resource2.isCalculatedSvcAs() is False
        assert resource2.getOsResourceProperty() == "INTERNAL"
        assert len(resource2.getOsResourceAccessingApplicationRefs()) == 0

    def test_read_os_tasks(self):
        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsTask" type="MAP">
                <d:ctr name="Task1">
                    <d:var name="OsTaskActivation" type="INTEGER" value="1">
                    <a:a name="IMPORTER_INFO" value="@DEF"/>
                  </d:var>
                  <d:var name="OsTaskPriority" type="INTEGER" value="250"/>
                  <d:var name="OsTaskPeriod" type="FLOAT" >
                    <a:a name="ENABLE" value="false"/>
                    <a:a name="IMPORTER_INFO" value="@DEF"/>
                  </d:var>
                  <d:var name="OsMeasure_Max_Runtime" type="BOOLEAN" value="false">
                    <a:a name="ENABLE" value="false"/>
                    <a:a name="IMPORTER_INFO" value="@DEF"/>
                  </d:var>
                  <d:lst name="OsTaskAccessingApplication">
                    <d:ref type="REFERENCE" value="ASPath:/Os/Os/Partition_01"/>
                  </d:lst>
                  <d:lst name="OsTaskEventRef"/>
                  <d:lst name="OsTaskResourceRef">
                    <d:ref type="REFERENCE" value="ASPath:/Os/Os/Res_Core0"/>
                    <d:ref type="REFERENCE" value="ASPath:/Os/Os/Res_Core1"/>
                  </d:lst>
                  <d:ctr name="OsTaskAutostart" type="IDENTIFIABLE">
                    <a:a name="ENABLE" value="true"/>
                    <d:lst name="OsTaskAppModeRef">
                      <d:ref type="REFERENCE" value="ASPath:/Os/Os/OSDEFAULTAPPMODE"/>
                    </d:lst>
                  </d:ctr>
                  <d:var name="OsTaskUse_Hw_Fp" type="BOOLEAN" >
                    <a:a name="ENABLE" value="false"/>
                    <a:a name="IMPORTER_INFO" value="@DEF"/>
                  </d:var>
                  <d:var name="OsTaskCallScheduler" type="ENUMERATION" >
                    <a:a name="ENABLE" value="false"/>
                    <a:a name="IMPORTER_INFO" value="@DEF"/>
                  </d:var>
                  <d:var name="OsTaskType" type="ENUMERATION" value="BASIC">
                    <a:a name="ENABLE" value="true"/>
                  </d:var>
                  <d:var name="OsStacksize" type="INTEGER" value="1024"/>
                  <d:ctr name="OsTaskTimingProtection" type="IDENTIFIABLE">
                    <a:a name="ENABLE" value="false"/>
                    <d:var name="OsTaskAllInterruptLockBudget" type="FLOAT">
                      <a:a name="ENABLE" value="false"/>
                      <a:a name="IMPORTER_INFO" value="@DEF"/>
                    </d:var>
                    <d:var name="OsTaskExecutionBudget" type="FLOAT" >
                      <a:a name="ENABLE" value="false"/>
                      <a:a name="IMPORTER_INFO" value="@DEF"/>
                    </d:var>
                    <d:var name="OsTaskOsInterruptLockBudget" type="FLOAT" >
                      <a:a name="ENABLE" value="false"/>
                      <a:a name="IMPORTER_INFO" value="@DEF"/>
                    </d:var>
                    <d:var name="OsTaskTimeFrame" type="FLOAT" >
                      <a:a name="ENABLE" value="false"/>
                      <a:a name="IMPORTER_INFO" value="@DEF"/>
                    </d:var>
                    <d:lst name="OsTaskResourceLock" type="MAP"/>
                    <d:var name="OsTaskCountLimit" type="INTEGER" value="1">
                      <a:a name="ENABLE" value="false"/>
                      <a:a name="IMPORTER_INFO" value="@DEF"/>
                    </d:var>
                  </d:ctr>
                  <d:var name="OsTaskSchedule" type="ENUMERATION" value="FULL"/>
                  <d:var name="OsTaskMkCreateMemoryRegion" type="BOOLEAN" value="false"/>
                  <d:var name="OsTaskMkExcludeAppRegions" type="BOOLEAN" value="false">
                    <a:a name="IMPORTER_INFO" value="@DEF"/>
                  </d:var>
                  <d:lst name="OsTaskMkMemoryRegionRef">
                    <d:ref type="REFERENCE" value="ASPath:/Os/Os/OsMicrokernel/MkMemoryProtection/MPU_01"/>
                    <d:ref type="REFERENCE" value="ASPath:/Os/Os/OsMicrokernel/MkMemoryProtection/MPU_02"/>
                  </d:lst>
                  <d:var name="OsTaskMkThreadModeOverride" type="ENUMERATION"
                         value="USER1">
                    <a:a name="ENABLE" value="true"/>
                  </d:var>
                  <d:var name="OsTaskSafetyIdentifier" type="BOOLEAN" value="false">
                    <a:a name="IMPORTER_INFO" value="@DEF"/>
                  </d:var>
                  <d:var name="OsTaskFastPartition" type="BOOLEAN" value="false">
                    <a:a name="IMPORTER_INFO" value="@DEF"/>
                  </d:var>
                  <d:var name="OsPswCallDepthCounting" type="BOOLEAN" value="false">
                    <a:a name="IMPORTER_INFO" value="@DEF"/>
                  </d:var>
                  <d:var name="OsPswCallDepthCounter" type="INTEGER" >
                    <a:a name="IMPORTER_INFO" value="@DEF"/>
                  </d:var>
                </d:ctr>
                <d:ctr name="Task2">
                    <d:var name="OsTaskPriority" type="INTEGER" value="3"/>
                    <d:var name="OsTaskActivation" type="INTEGER" value="2"/>
                    <d:var name="OsTaskSchedule" type="ENUMERATION" value="NON"/>
                    <d:var name="OsStacksize" type="INTEGER" value="2048"/>
                </d:ctr>
                <d:ctr name="Idle_Task_C0" type="IDENTIFIABLE">
                  <d:var name="OsTaskPeriod" type="FLOAT" >
                    <a:a name="ENABLE" value="false"/>
                    <a:a name="IMPORTER_INFO" value="@DEF"/>
                  </d:var>
                  <d:ref name="OsMemoryMappingCodeLocationRef" type="REFERENCE" >
                    <a:a name="ENABLE" value="false"/>
                    <a:a name="IMPORTER_INFO" value="@DEF"/>
                  </d:ref>
                  <d:lst name="OsTaskEventRef"/>
                  <d:lst name="OsTaskResourceRef"/>
                  <d:ctr name="OsTaskTimingProtection" type="IDENTIFIABLE">
                    <a:a name="ENABLE" value="false"/>
                    <d:var name="OsTaskAllInterruptLockBudget" type="FLOAT" >
                      <a:a name="ENABLE" value="false"/>
                      <a:a name="IMPORTER_INFO" value="@DEF"/>
                    </d:var>
                    <d:var name="OsTaskExecutionBudget" type="FLOAT" >
                      <a:a name="ENABLE" value="false"/>
                      <a:a name="IMPORTER_INFO" value="@DEF"/>
                    </d:var>
                    <d:var name="OsTaskOsInterruptLockBudget" type="FLOAT" >
                      <a:a name="ENABLE" value="false"/>
                      <a:a name="IMPORTER_INFO" value="@DEF"/>
                    </d:var>
                    <d:var name="OsTaskTimeFrame" type="FLOAT" >
                      <a:a name="ENABLE" value="false"/>
                      <a:a name="IMPORTER_INFO" value="@DEF"/>
                    </d:var>
                    <d:lst name="OsTaskResourceLock" type="MAP"/>
                    <d:var name="OsTaskCountLimit" type="INTEGER" value="1">
                      <a:a name="ENABLE" value="false"/>
                      <a:a name="IMPORTER_INFO" value="@DEF"/>
                    </d:var>
                  </d:ctr>
                  <d:var name="OsMeasure_Max_Runtime" type="BOOLEAN" value="false">
                    <a:a name="ENABLE" value="false"/>
                    <a:a name="IMPORTER_INFO" value="@DEF"/>
                  </d:var>
                  <d:var name="OsTaskCallScheduler" type="ENUMERATION" >
                    <a:a name="ENABLE" value="false"/>
                    <a:a name="IMPORTER_INFO" value="@DEF"/>
                  </d:var>
                  <d:var name="OsTaskType" type="ENUMERATION" >
                    <a:a name="ENABLE" value="false"/>
                    <a:a name="IMPORTER_INFO" value="@DEF"/>
                  </d:var>
                  <d:var name="OsStacksize" type="INTEGER" value="800"/>
                  <d:var name="OsTaskActivation" type="INTEGER" value="1"/>
                  <d:var name="OsTaskPriority" type="INTEGER" value="1"/>
                  <d:var name="OsTaskSchedule" type="ENUMERATION" value="FULL"/>
                  <d:var name="OsTaskUse_Hw_Fp" type="BOOLEAN" value="true">
                    <a:a name="ENABLE" value="true"/>
                  </d:var>
                  <d:lst name="OsTaskAccessingApplication">
                    <d:ref type="REFERENCE" value="ASPath:/Os/Os/OsApplication_C0"/>
                  </d:lst>
                  <d:ctr name="OsTaskAutostart" type="IDENTIFIABLE">
                    <a:a name="ENABLE" value="true"/>
                    <d:lst name="OsTaskAppModeRef">
                      <d:ref type="REFERENCE" value="ASPath:/Os/Os/OSDEFAULTAPPMODE"/>
                    </d:lst>
                  </d:ctr>
                  <d:var name="OsTaskMkCreateMemoryRegion" type="BOOLEAN" value="true">
                    <a:a name="IMPORTER_INFO" value="@DEF"/>
                  </d:var>
                  <d:var name="OsTaskMkExcludeAppRegions" type="BOOLEAN" value="false">
                    <a:a name="IMPORTER_INFO" value="@DEF"/>
                  </d:var>
                  <d:lst name="OsTaskMkMemoryRegionRef"/>
                  <d:var name="OsTaskMkThreadModeOverride" type="ENUMERATION" value="USER">
                    <a:a name="ENABLE" value="false"/>
                    <a:a name="IMPORTER_INFO" value="@DEF"/>
                  </d:var>
                  <d:ctr name="OsCORTEXMMemoryRegions" type="IDENTIFIABLE">
                    <d:var name="OsCORTEXMPrivateDataRegionSize" type="ENUMERATION" value="SIZE_4K">
                      <a:a name="ENABLE" value="false"/>
                      <a:a name="IMPORTER_INFO" value="@DEF"/>
                    </d:var>
                  </d:ctr>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock Os object
        model = EBModel.getInstance()
        os = model.getOs()

        # Create parser instance
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_os_tasks(element, os)

        # Assertions
        tasks = os.getOsTaskList()
        assert len(tasks) == 3

        task1 = tasks[0]
        assert task1.getName() == "Idle_Task_C0"
        assert task1.getOsTaskPriority() == 1
        assert task1.getOsTaskActivation() == 1
        assert task1.getOsTaskSchedule() == "FULL"
        assert task1.getOsTaskType() is None
        assert task1.getOsStacksize() == 800
        assert len(task1.getOsTaskResourceRefList()) == 0
        assert task1.getOsTaskAutostart() is not None
        assert task1.getOsTaskAutostart().getOsTaskAppModeRefList() is not None

        task2 = tasks[1]
        assert task2.getName() == "Task1"
        assert task2.getOsTaskPriority() == 250
        assert task2.getOsTaskActivation() == 1
        assert task2.getOsTaskSchedule() == "FULL"
        assert task2.getOsTaskType() == "BASIC"
        assert task2.getOsStacksize() == 1024
        assert len(task2.getOsTaskResourceRefList()) == 2
        assert task2.getOsTaskResourceRefList()[0].getValue() == "/Os/Os/Res_Core0"
        assert task2.getOsTaskResourceRefList()[1].getValue() == "/Os/Os/Res_Core1"
        autostart = task2.getOsTaskAutostart()
        assert autostart is not None
        assert len(autostart.getOsTaskAppModeRefList()) == 1
        assert autostart.getOsTaskAppModeRefList()[0].getValue() == "/Os/Os/OSDEFAULTAPPMODE"

        task3 = tasks[2]
        assert task3.getName() == "Task2"
        assert task3.getOsTaskPriority() == 3
        assert task3.getOsTaskActivation() == 2
        assert task3.getOsTaskSchedule() == "NON"
        assert task3.getOsTaskType() is None
        assert task3.getOsStacksize() == 2048
        assert len(task3.getOsTaskResourceRefList()) == 0
        assert task3.getOsTaskAutostart() is None

    def test_read_os_applications(self):
        """
        Test parsing OsApplication containers from XDM.

        Implements: TC_UNIT_OS_00006
        """
        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsApplication" type="MAP">
                <d:ctr name="App1">
                    <d:var name="OsTrusted" type="BOOLEAN" value="true"/>
                    <d:var name="OsApplicationCoreAssignment" type="INTEGER" value="0"/>
                    <d:ref name="OsAppEcucPartitionRef" type="REFERENCE" value="ASPath:/Os/OsPartition1"/>
                    <d:lst name="OsAppAlarmRef">
                        <d:ref type="REFERENCE" value="ASPath:/Os/Alarm1"/>
                    </d:lst>
                    <d:lst name="OsAppCounterRef">
                        <d:ref type="REFERENCE" value="ASPath:/Os/Counter1"/>
                    </d:lst>
                    <d:lst name="OsAppResourceRef">
                        <d:ref type="REFERENCE" value="ASPath:/Os/OsResource1"/>
                        <d:ref type="REFERENCE" value="ASPath:/Os/OsResource2"/>
                    </d:lst>
                    <d:lst name="OsAppScheduleTableRef">
                        <d:ref type="REFERENCE" value="ASPath:/Os/Schedule1"/>
                    </d:lst>
                    <d:lst name="OsAppTaskRef">
                        <d:ref type="REFERENCE" value="ASPath:/Os/OsTask1"/>
                    </d:lst>
                    <d:lst name="OsAppIsrRef">
                        <d:ref type="REFERENCE" value="ASPath:/Os/OsIsr1"/>
                    </d:lst>
                </d:ctr>
                <d:ctr name="App2">
                    <d:var name="OsTrusted" type="BOOLEAN" value="false"/>
                    <d:var name="OsApplicationCoreAssignment" type="INTEGER" value="1"/>
                    <d:ref name="OsAppEcucPartitionRef" type="REFERENCE" value="ASPath:/Os/OsPartition2"/>
                    <d:lst name="OsAppResourceRef"/>
                    <d:lst name="OsAppTaskRef"/>
                    <d:lst name="OsAppIsrRef"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock Os object
        model = EBModel.getInstance()
        os = model.getOs()

        # Create parser instance
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_os_applications(element, os)

        # Assertions
        applications = os.getOsApplicationList()
        assert len(applications) == 2

        app1 = applications[0]
        assert app1.getName() == "App1"
        assert app1.getOsTrusted() is True
        assert len(app1.getOsAppAlarmRefs()) == 1
        assert app1.getOsAppAlarmRefs()[0].getValue() == "/Os/Alarm1"
        assert len(app1.getOsAppCounterRefs()) == 1
        assert app1.getOsAppCounterRefs()[0].getValue() == "/Os/Counter1"
        assert app1.getOsAppEcucPartitionRef().getValue() == "/Os/OsPartition1"
        assert len(app1.getOsAppResourceRefs()) == 2
        assert app1.getOsAppResourceRefs()[0].getValue() == "/Os/OsResource1"
        assert app1.getOsAppResourceRefs()[1].getValue() == "/Os/OsResource2"
        assert len(app1.getOsAppScheduleTableRefs()) == 1
        assert app1.getOsAppScheduleTableRefs()[0].getValue() == "/Os/Schedule1"
        assert len(app1.getOsAppTaskRefs()) == 1
        assert app1.getOsAppTaskRefs()[0].getValue() == "/Os/OsTask1"
        assert len(app1.getOsAppIsrRefs()) == 1
        assert app1.getOsAppIsrRefs()[0].getValue() == "/Os/OsIsr1"

        app2 = applications[1]
        assert app2.getName() == "App2"
        assert app2.getOsTrusted() is False
        assert len(app2.getOsAppResourceRefs()) == 0
        assert len(app2.getOsAppTaskRefs()) == 0
        assert len(app2.getOsAppIsrRefs()) == 0

    def test_read_os_isrs(self):
        """
        Test parsing OsIsr containers with TriCore and ARM specific attributes.

        Implements: TC_UNIT_OS_00003
        """
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsIsr" type="MAP">
                <d:ctr name="Isr1_Tricore">
                    <d:var name="OsIsrCategory" type="ENUMERATION" value="2"/>
                    <d:var name="OsIsrPeriod" type="FLOAT" value="0.001"/>
                    <d:var name="OsStacksize" type="INTEGER" value="512"/>
                    <d:var name="OsTricoreIrqLevel" type="INTEGER" value="42"/>
                    <d:var name="OsTricoreVector" type="INTEGER" value="256"/>
                </d:ctr>
                <d:ctr name="Isr2_ARM">
                    <d:var name="OsIsrCategory" type="ENUMERATION" value="1"/>
                    <d:var name="OsStacksize" type="INTEGER" value="256"/>
                    <d:var name="OsARMIrqLevel" type="INTEGER" value="32"/>
                    <d:var name="OsARMVector" type="INTEGER" value="128"/>
                </d:ctr>
                <d:ctr name="Isr3_Basic">
                    <d:var name="OsIsrCategory" type="ENUMERATION" value="2"/>
                    <d:var name="OsStacksize" type="INTEGER" value="1024"/>
                    <d:var name="OsIsrPriority" type="INTEGER" value="15"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        os = model.getOs()

        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_os_isrs(element, os)

        # Assertions
        isrs = os.getOsIsrList()
        assert len(isrs) == 3

        # Test Tricore-specific ISR
        isr1 = isrs[0]
        assert isr1.getName() == "Isr1_Tricore"
        assert isr1.getOsIsrCategory() == "2"
        assert isr1.getOsIsrPeriod() == 0.001
        assert isr1.getOsStacksize() == 512
        assert isr1.getOsIsrPriority() == 42  # Set by OsTricoreIrqLevel
        assert isr1.getOsTricoreIrqLevel() == 42
        assert isr1.getOsTricoreVector() == 256

        # Test ARM-specific ISR
        isr2 = isrs[1]
        assert isr2.getName() == "Isr2_ARM"
        assert isr2.getOsIsrCategory() == "1"
        assert isr2.getOsStacksize() == 256
        assert isr2.getOsIsrPriority() == 32  # Set by OsARMIrqLevel
        assert isr2.getOsARMIrqLevel() == 32
        assert isr2.getOsARMVector() == 128

        # Test basic ISR without hardware-specific attributes
        isr3 = isrs[2]
        assert isr3.getName() == "Isr3_Basic"
        assert isr3.getOsIsrCategory() == "2"
        assert isr3.getOsStacksize() == 1024
        assert isr3.getOsIsrPriority() == 15

    def test_error_handling_malformed_xml(self):
        """
        Test that parser handles malformed XML gracefully.

        Implements: TC_UNIT_OS_00012
        """
        # Test with missing required attribute
        xml_missing_name = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsTask" type="MAP">
                <d:ctr>
                    <d:var name="OsTaskPriority" type="INTEGER" value="10"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_missing_name)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Should raise KeyError for missing name attribute
        with pytest.raises(KeyError):
            parser.read_os_tasks(element, os)

        # Test with missing mandatory value
        xml_missing_value = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsTask" type="MAP">
                <d:ctr name="Task1">
                    <d:var name="OsTaskPriority" type="INTEGER" value="10"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_missing_value)

        # Should raise KeyError for missing OsTaskActivation
        with pytest.raises(KeyError, match="OsTaskActivation"):
            parser.read_os_tasks(element, os)

    def test_read_os_isrs_with_memory_region_refs(self):
        """
        Test ISR parsing with MkMemoryRegionRef references.

        Implements: TC_UNIT_OS_00003 (ISR with memory region refs)
        """
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsIsr" type="MAP">
                <d:ctr name="Isr_Safety">
                    <d:var name="OsIsrCategory" type="ENUMERATION" value="2"/>
                    <d:var name="OsStacksize" type="INTEGER" value="2048"/>
                    <d:var name="OsIsrPriority" type="INTEGER" value="31"/>
                    <d:lst name="OsIsrMkMemoryRegionRef">
                        <d:ref type="REFERENCE" value="ASPath:/Os/OsMicrokernel/MkMemoryProtection/Region_Safety"/>
                        <d:ref type="REFERENCE" value="ASPath:/Os/OsMicrokernel/MkMemoryProtection/Region_App"/>
                    </d:lst>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_os_isrs(element, os)

        isrs = os.getOsIsrList()
        assert len(isrs) == 1
        isr = isrs[0]
        assert isr.getName() == "Isr_Safety"
        assert isr.getOsIsrCategory() == "2"
        assert isr.getOsStacksize() == 2048
        assert isr.getOsIsrPriority() == 31

        memory_refs = isr.getOsIsrMkMemoryRegionRefs()
        assert len(memory_refs) == 2
        assert memory_refs[0].getValue() == "/Os/OsMicrokernel/MkMemoryProtection/Region_Safety"
        assert memory_refs[1].getValue() == "/Os/OsMicrokernel/MkMemoryProtection/Region_App"

    def test_read_os_alarm_action_missing_raises_error(self):
        """
        Test that missing OsAlarmAction choice value raises KeyError.

        When the d:chc element exists but has no 'value' attribute,
        read_choice_value raises KeyError.

        Implements: TC_UNIT_OS_00013
        """
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsAlarm" type="MAP">
                <d:ctr name="AlarmNoAction">
                    <d:ref name="OsAlarmCounterRef" type="REFERENCE" value="ASPath:/Os/Counter1"/>
                    <d:chc name="OsAlarmAction">
                        <d:ctr name="OsAlarmActivateTask"/>
                        <d:ctr name="OsAlarmIncrementCounter"/>
                    </d:chc>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        with pytest.raises(KeyError):
            parser.read_os_alarms(element, os)

    def test_read_os_alarm_action_unsupported_raises_error(self):
        """
        Test that unsupported OsAlarmAction value raises ValueError.

        Implements: TC_UNIT_OS_00013
        """
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsAlarm" type="MAP">
                <d:ctr name="AlarmBadAction">
                    <d:ref name="OsAlarmCounterRef" type="REFERENCE" value="ASPath:/Os/Counter1"/>
                    <d:chc name="OsAlarmAction" value="OsAlarmInvalidAction">
                        <d:ctr name="OsAlarmActivateTask"/>
                        <d:ctr name="OsAlarmIncrementCounter"/>
                        <d:ctr name="OsAlarmSetEvent"/>
                        <d:ctr name="OsAlarmCallback"/>
                    </d:chc>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        with pytest.raises(ValueError, match="Unsupported OsAlarmAction"):
            parser.read_os_alarms(element, os)

    def test_error_handling_required_elements(self):
        """
        Test that parser validates required elements and references.

        Implements: TC_UNIT_OS_00013
        """
        # Test with invalid enum value (this won't be caught by parser, just stored)
        xml_invalid_enum = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsTask" type="MAP">
                <d:ctr name="Task1">
                    <d:var name="OsTaskActivation" type="INTEGER" value="1"/>
                    <d:var name="OsTaskPriority" type="INTEGER" value="10"/>
                    <d:var name="OsStacksize" type="INTEGER" value="1024"/>
                    <d:var name="OsTaskSchedule" type="ENUMERATION" value="INVALID_SCHEDULE"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_invalid_enum)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Parser should accept the value (validation happens at a different layer)
        parser.read_os_tasks(element, os)
        tasks = os.getOsTaskList()
        assert len(tasks) == 1
        assert tasks[0].getOsTaskSchedule() == "INVALID_SCHEDULE"

        # Test that required fields are validated
        xml_missing_required = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsTask" type="MAP">
                <d:ctr name="Task2">
                    <d:var name="OsTaskPriority" type="INTEGER" value="10"/>
                    <d:var name="OsStacksize" type="INTEGER" value="1024"/>
                    <d:var name="OsTaskSchedule" type="ENUMERATION" value="FULL"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_missing_required)

        # Should raise KeyError for missing required OsTaskActivation
        with pytest.raises(KeyError, match="OsTaskActivation"):
            parser.read_os_tasks(element, os)

    def test_read_os_schedule_tables(self):
        """
        Test schedule table parsing with expiry points and actions.

        Implements: TC_UNIT_OS_00004
        """
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsScheduleTable" type="MAP">
                <d:ctr name="Schedule1">
                    <d:var name="OsScheduleTableDuration" type="INTEGER" value="100"/>
                    <d:var name="OsScheduleTableRepeating" type="BOOLEAN" value="true"/>
                    <d:ref name="OsScheduleTableCounterRef" type="REFERENCE" value="ASPath:/Os/Counter1"/>
                    <d:lst name="OsScheduleTableExpiryPoint">
                        <d:ctr name="ExpiryPoint0">
                            <d:var name="OsScheduleTblExpPointOffset" type="INTEGER" value="0"/>
                            <d:lst name="OsScheduleTableTaskActivation">
                                <d:ctr name="TaskActivation0">
                                    <d:ref name="OsScheduleTableActivateTaskRef" type="REFERENCE" value="ASPath:/Os/Task1"/>
                                </d:ctr>
                            </d:lst>
                            <d:ctr name="OsScheduleTblAdjustableExpPoint">
                                <d:ref name="OsScheduleTableMaxLengthen" type="REFERENCE" value="ASPath:/Os/Counter1"/>
                                <d:ref name="OsScheduleTableMaxShorten" type="REFERENCE" value="ASPath:/Os/Counter2"/>
                            </d:ctr>
                        </d:ctr>
                        <d:ctr name="ExpiryPoint50">
                            <d:var name="OsScheduleTblExpPointOffset" type="INTEGER" value="50"/>
                            <d:lst name="OsScheduleTableEventSetting">
                                <d:ctr name="EventSetting0">
                                    <d:ref name="OsScheduleTableSetEventRef" type="REFERENCE" value="ASPath:/Os/Event1"/>
                                    <d:ref name="OsScheduleTableSetEventTaskRef" type="REFERENCE" value="ASPath:/Os/Task2"/>
                                </d:ctr>
                            </d:lst>
                        </d:ctr>
                    </d:lst>
                </d:ctr>
                <d:ctr name="Schedule2">
                    <d:var name="OsScheduleTableDuration" type="INTEGER" value="200"/>
                    <d:var name="OsScheduleTableRepeating" type="BOOLEAN" value="false"/>
                    <d:ref name="OsScheduleTableCounterRef" type="REFERENCE" value="ASPath:/Os/Counter2"/>
                    <d:var name="OsTimeUnit" type="ENUMERATION" value="NANOSECONDS"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_os_schedule_tables(element, os)

        schedule_tables = os.getOsScheduleTableList()
        assert len(schedule_tables) == 2

        # Test Schedule1 with expiry points
        schedule1 = schedule_tables[0]
        assert schedule1.getName() == "Schedule1"
        assert schedule1.getOsScheduleTableDuration() == 100
        assert schedule1.getOsScheduleTableRepeating() is True
        assert schedule1.getOsScheduleTableCounterRef().getValue() == "/Os/Counter1"
        assert schedule1.getOsTimeUnit() is None

        expiry_points = schedule1.getOsScheduleTableExpiryPointList()
        assert len(expiry_points) == 2

        # Test first expiry point with task activation
        expiry0 = expiry_points[0]
        assert expiry0.getName() == "ExpiryPoint0"
        assert expiry0.getOsScheduleTblExpPointOffset() == 0

        task_activations = expiry0.getOsScheduleTableTaskActivationList()
        assert len(task_activations) == 1
        assert task_activations[0].getName() == "TaskActivation0"
        assert task_activations[0].getOsScheduleTableActivateTaskRef().getValue() == "/Os/Task1"

        # Test adjustable expiry point
        adjustable_point = expiry0.getOsScheduleTblAdjustableExpPoint()
        assert adjustable_point is not None
        assert adjustable_point.getName() == "OsScheduleTblAdjustableExpPoint"
        assert adjustable_point.getOsScheduleTableMaxLengthen().getValue() == "/Os/Counter1"
        assert adjustable_point.getOsScheduleTableMaxShorten().getValue() == "/Os/Counter2"

        # Test second expiry point with event setting
        expiry50 = expiry_points[1]
        assert expiry50.getName() == "ExpiryPoint50"
        assert expiry50.getOsScheduleTblExpPointOffset() == 50

        event_settings = expiry50.getOsScheduleTableEventSettingList()
        assert len(event_settings) == 1
        assert event_settings[0].getName() == "EventSetting0"
        assert event_settings[0].getOsScheduleTableSetEventRef().getValue() == "/Os/Event1"
        assert event_settings[0].getOsScheduleTableSetEventTaskRef().getValue() == "/Os/Task2"

        # Test Schedule2 without expiry points
        schedule2 = schedule_tables[1]
        assert schedule2.getName() == "Schedule2"
        assert schedule2.getOsScheduleTableDuration() == 200
        assert schedule2.getOsScheduleTableRepeating() is False
        assert schedule2.getOsScheduleTableCounterRef().getValue() == "/Os/Counter2"
        assert schedule2.getOsTimeUnit() == "NANOSECONDS"

        assert len(schedule2.getOsScheduleTableExpiryPointList()) == 0

    def test_read_os_alarms(self):
        """
        Test alarm parsing with different action types.

        Implements: TC_UNIT_OS_00007
        """
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsAlarm" type="MAP">
                <d:ctr name="Alarm1">
                    <d:ref name="OsAlarmCounterRef" type="REFERENCE" value="ASPath:/Os/Counter1"/>
                    <d:lst name="OsAlarmAccessingApplication">
                        <d:ref type="REFERENCE" value="ASPath:/Os/App1"/>
                        <d:ref type="REFERENCE" value="ASPath:/Os/App2"/>
                    </d:lst>
                    <d:chc name="OsAlarmAction" value="OsAlarmActivateTask">
                        <d:ctr name="OsAlarmActivateTask">
                            <d:ref name="OsAlarmActivateTaskRef" type="REFERENCE" value="ASPath:/Os/Task1"/>
                        </d:ctr>
                        <d:ctr name="OsAlarmIncrementCounter"/>
                        <d:ctr name="OsAlarmSetEvent"/>
                        <d:ctr name="OsAlarmCallback"/>
                    </d:chc>
                </d:ctr>
                <d:ctr name="Alarm2">
                    <d:ref name="OsAlarmCounterRef" type="REFERENCE" value="ASPath:/Os/Counter2"/>
                    <d:chc name="OsAlarmAction" value="OsAlarmSetEvent">
                        <d:ctr name="OsAlarmActivateTask"/>
                        <d:ctr name="OsAlarmIncrementCounter"/>
                        <d:ctr name="OsAlarmSetEvent">
                            <d:ref name="OsAlarmSetEventRef" type="REFERENCE" value="ASPath:/Os/Event1"/>
                            <d:ref name="OsAlarmSetEventTaskRef" type="REFERENCE" value="ASPath:/Os/Task2"/>
                        </d:ctr>
                        <d:ctr name="OsAlarmCallback"/>
                    </d:chc>
                </d:ctr>
                <d:ctr name="Alarm3">
                    <d:ref name="OsAlarmCounterRef" type="REFERENCE" value="ASPath:/Os/Counter3"/>
                    <d:chc name="OsAlarmAction" value="OsAlarmIncrementCounter">
                        <d:ctr name="OsAlarmActivateTask"/>
                        <d:ctr name="OsAlarmIncrementCounter">
                            <d:ref name="OsAlarmIncrementCounterRef" type="REFERENCE" value="ASPath:/Os/Counter4"/>
                        </d:ctr>
                        <d:ctr name="OsAlarmSetEvent"/>
                        <d:ctr name="OsAlarmCallback"/>
                    </d:chc>
                </d:ctr>
                <d:ctr name="Alarm4">
                    <d:ref name="OsAlarmCounterRef" type="REFERENCE" value="ASPath:/Os/Counter5"/>
                    <d:chc name="OsAlarmAction" value="OsAlarmCallback">
                        <d:ctr name="OsAlarmActivateTask"/>
                        <d:ctr name="OsAlarmIncrementCounter"/>
                        <d:ctr name="OsAlarmSetEvent"/>
                        <d:ctr name="OsAlarmCallback">
                            <d:var name="OsAlarmCallbackName" type="STRING" value="Alarm4Callback"/>
                        </d:ctr>
                    </d:chc>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_os_alarms(element, os)

        alarms = os.getOsAlarmList()
        assert len(alarms) == 4

        # Test Alarm1 with ActivateTask action and accessing application refs
        alarm1 = alarms[0]
        assert alarm1.getName() == "Alarm1"
        assert alarm1.getOsAlarmCounterRef().getValue() == "/Os/Counter1"
        assert alarm1.getOsAlarmAction() is not None
        assert isinstance(alarm1.getOsAlarmAction(), OsAlarmActivateTask)
        assert alarm1.getOsAlarmAction().getOsAlarmActivateTaskRef().getValue() == "/Os/Task1"

        accessing_apps = alarm1.getOsAlarmAccessingApplicationRefList()
        assert len(accessing_apps) == 2
        assert accessing_apps[0].getValue() == "/Os/App1"
        assert accessing_apps[1].getValue() == "/Os/App2"

        # Test Alarm2 with SetEvent action
        alarm2 = alarms[1]
        assert alarm2.getName() == "Alarm2"
        assert alarm2.getOsAlarmCounterRef().getValue() == "/Os/Counter2"
        assert alarm2.getOsAlarmAction() is not None
        assert isinstance(alarm2.getOsAlarmAction(), OsAlarmSetEvent)
        assert alarm2.getOsAlarmAction().getOsAlarmSetEventRef().getValue() == "/Os/Event1"
        assert alarm2.getOsAlarmAction().getOsAlarmSetEventTaskRef().getValue() == "/Os/Task2"

        # Test Alarm3 with IncrementCounter action
        alarm3 = alarms[2]
        assert alarm3.getName() == "Alarm3"
        assert alarm3.getOsAlarmCounterRef().getValue() == "/Os/Counter3"
        assert alarm3.getOsAlarmAction() is not None
        assert isinstance(alarm3.getOsAlarmAction(), OsAlarmIncrementCounter)
        assert alarm3.getOsAlarmAction().getOsAlarmIncrementCounterRef().getValue() == "/Os/Counter4"

        # Test Alarm4 with Callback action
        alarm4 = alarms[3]
        assert alarm4.getName() == "Alarm4"
        assert alarm4.getOsAlarmCounterRef().getValue() == "/Os/Counter5"
        assert alarm4.getOsAlarmAction() is not None
        assert isinstance(alarm4.getOsAlarmAction(), OsAlarmCallback)
        assert alarm4.getOsAlarmAction().getOsAlarmCallbackName() == "Alarm4Callback"

    def test_read_os_counters(self):
        """
        Test counter parsing including software and hardware counters.

        Implements: TC_UNIT_OS_00005
        """
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsCounter" type="MAP">
                <d:ctr name="Counter1">
                    <d:var name="OsCounterMaxAllowedValue" type="INTEGER" value="65535"/>
                    <d:var name="OsCounterMinCycle" type="INTEGER" value="1"/>
                    <d:var name="OsCounterTicksPerBase" type="INTEGER" value="1000"/>
                    <d:var name="OsCounterType" type="ENUMERATION" value="SOFTWARE"/>
                </d:ctr>
                <d:ctr name="Counter2">
                    <d:var name="OsCounterMaxAllowedValue" type="INTEGER" value="255"/>
                    <d:var name="OsCounterMinCycle" type="INTEGER" value="5"/>
                    <d:var name="OsCounterTicksPerBase" type="INTEGER" value="500"/>
                    <d:var name="OsCounterType" type="ENUMERATION" value="HARDWARE"/>
                    <d:var name="OsHwModule" type="STRING" value="GptChannel1"/>
                    <d:var name="OsSecondsPerTick" type="FLOAT" value="0.001"/>
                    <d:var name="OsCounterWindowsTimer" type="BOOLEAN" value="true"/>
                    <d:var name="OsWindowsIrqLevel" type="INTEGER" value="7"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_os_counters(element, os)

        counters = os.getOsCounterList()
        assert len(counters) == 2

        # Test software counter
        counter1 = counters[0]
        assert counter1.getName() == "Counter1"
        assert counter1.getOsCounterMaxAllowedValue() == 65535
        assert counter1.getOsCounterMinCycle() == 1
        assert counter1.getOsCounterTicksPerBase() == 1000
        assert counter1.getOsCounterType() == "SOFTWARE"
        assert counter1.getOsHwModule() is None  # Software counter: no driver
        assert counter1.getOsSecondsPerTick() is None

        # Test hardware counter
        counter2 = counters[1]
        assert counter2.getName() == "Counter2"
        assert counter2.getOsCounterMaxAllowedValue() == 255
        assert counter2.getOsCounterMinCycle() == 5
        assert counter2.getOsCounterTicksPerBase() == 500
        assert counter2.getOsCounterType() == "HARDWARE"
        assert counter2.getOsHwModule() == "GptChannel1"
        assert counter2.getOsSecondsPerTick() == 0.001
        assert counter2.getOsCounterWindowsTimer() is True
        assert counter2.getOsWindowsIrqLevel() == 7

    def test_read_os_memory_protection(self):
        """
        Test microkernel and memory region parsing.

        Implements: TC_UNIT_OS_00009
        """
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
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
                        <d:ctr name="Region2">
                            <d:var name="MkMemoryRegionFlags" type="INTEGER" value="0"/>
                            <d:var name="MkMemoryRegionInitialize" type="BOOLEAN" value="false"/>
                            <d:var name="MkMemoryRegionGlobal" type="BOOLEAN" value="true"/>
                            <d:var name="MkMemoryRegionInitThreadAccess" type="BOOLEAN" value="false"/>
                            <d:var name="MkMemoryRegionIdleThreadAccess" type="BOOLEAN" value="false"/>
                            <d:var name="MkMemoryRegionOsThreadAccess" type="BOOLEAN" value="true"/>
                            <d:var name="MkMemoryRegionErrorHookAccess" type="BOOLEAN" value="false"/>
                            <d:var name="MkMemoryRegionProtHookAccess" type="BOOLEAN" value="false"/>
                            <d:var name="MkMemoryRegionShutdownHookAccess" type="BOOLEAN" value="false"/>
                            <d:var name="MkMemoryRegionShutdownAccess" type="BOOLEAN" value="false"/>
                            <d:var name="MkMemoryRegionInitializePerCore" type="BOOLEAN" value="false"/>
                        </d:ctr>
                    </d:lst>
                </d:ctr>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_os_microkernel(element, os)

        kernel = os.getOsMicrokernel()
        assert kernel is not None
        assert kernel.getName() == "OsMicrokernel"

        protection = kernel.getMkMemoryProtection()
        assert protection is not None

        regions = protection.getMkMemoryRegionList()
        assert len(regions) == 2

        # Test Region1
        region1 = regions[0]
        assert region1.getName() == "Region1"
        assert region1.getMkMemoryRegionFlags() == 1
        assert region1.getMkMemoryRegionInitialize() is True
        assert region1.getMkMemoryRegionGlobal() is False
        assert region1.getMkMemoryRegionInitThreadAccess() is True
        assert region1.getMkMemoryRegionOsThreadAccess() is True

        # Test Region2
        region2 = regions[1]
        assert region2.getName() == "Region2"
        assert region2.getMkMemoryRegionFlags() == 0
        assert region2.getMkMemoryRegionInitialize() is False
        assert region2.getMkMemoryRegionGlobal() is True
        assert region2.getMkMemoryRegionOsThreadAccess() is True

    def test_appmode_parsing(self):
        """
        Test OsAppMode parsing.

        Implements: UTS_OS_PARSER_00023
        """
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsAppMode" type="MAP">
                <d:ctr name="AppMode1"/>
                <d:ctr name="AppMode2"/>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_os_appmodes(element, os)

        appmodes = os.getOsAppModeList()
        assert len(appmodes) == 2

        appmode1 = appmodes[0]
        assert appmode1.getName() == "AppMode1"
        assert appmode1.getParent() == os

        appmode2 = appmodes[1]
        assert appmode2.getName() == "AppMode2"

    def test_peripheral_area_parsing_complete(self):
        """
        Test OsPeripheralArea parsing with all fields including OsPeripheralAreaId.

        Implements: UTS_OS_PARSER_00024
        """
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsPeripheralArea" type="MAP">
                <d:ctr name="PeripheralArea1">
                    <d:var name="OsPeripheralAreaStartAddress" type="INTEGER" value="4096"/>
                    <d:var name="OsPeripheralAreaEndAddress" type="INTEGER" value="8191"/>
                    <d:var name="OsPeripheralAreaId" type="INTEGER" value="1"/>
                    <d:var name="OsPeripheralAreaAccessPermission" type="ENUMERATION" value="READ-WRITE"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_os_peripheral_areas(element, os)

        areas = os.getOsPeripheralAreaList()
        assert len(areas) == 1

        area = areas[0]
        assert area.getName() == "PeripheralArea1"
        assert area.getOsPeripheralAreaStartAddress() == 4096
        assert area.getOsPeripheralAreaEndAddress() == 8191
        assert area.getOsPeripheralAreaId() == 1
        assert area.getOsPeripheralAreaAccessPermission() == "READ-WRITE"
