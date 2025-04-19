from ...parser.os_xdm_parser import OsXdmParser
from ...models.os_xdm import Os, OsResource
from ...models.eb_doc import EBModel

import xml.etree.ElementTree as ET
import pytest


class TestOsXdmParser:
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

    '''
    def test_read_os_applications(self):
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
                    <d:lst name="OsAppResourceRef">
                        <d:ref type="REFERENCE" value="/Os/OsResource1"/>
                        <d:ref type="REFERENCE" value="/Os/OsResource2"/>
                    </d:lst>
                    <d:lst name="OsAppTaskRef">
                        <d:ref type="REFERENCE" value="/Os/OsTask1"/>
                    </d:lst>
                    <d:lst name="OsAppIsrRef">
                        <d:ref type="REFERENCE" value="/Os/OsIsr1"/>
                    </d:lst>
                </d:ctr>
                <d:ctr name="App2">
                    <d:var name="OsTrusted" type="BOOLEAN" value="false"/>
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
        assert app1.getOsTrusted() == "true"
        assert len(app1.getOsAppResourceRefs()) == 2
        assert app1.getOsAppResourceRefs()[0].getValue() == "/Os/OsResource1"
        assert app1.getOsAppResourceRefs()[1].getValue() == "/Os/OsResource2"
        assert len(app1.getOsAppTaskRefs()) == 1
        assert app1.getOsAppTaskRefs()[0].getValue() == "/Os/OsTask1"
        assert len(app1.getOsAppIsrRefs()) == 1
        assert app1.getOsAppIsrRefs()[0].getValue() == "/Os/OsIsr1"

        app2 = applications[1]
        assert app2.getName() == "App2"
        assert app2.getOsTrusted() == "false"
        assert len(app2.getOsAppResourceRefs()) == 0
        assert len(app2.getOsAppTaskRefs()) == 0
        assert len(app2.getOsAppIsrRefs()) == 0
     noqa: E501 '''
