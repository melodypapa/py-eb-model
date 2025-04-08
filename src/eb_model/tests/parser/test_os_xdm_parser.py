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
