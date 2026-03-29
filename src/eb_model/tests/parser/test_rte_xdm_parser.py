from ...parser.rte_xdm_parser import RteXdmParser
from ...models.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestRteXdmParser:
    def test_read_rte_bsw_module_instances(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="RteBswModuleInstance" type="MAP">
                <d:ctr name="BswInstance1">
                    <d:ref name="RteBswImplementationRef" type="REFERENCE" value="ASPath:/Rte/Rte/Impl1"/>
                    <d:ref name="RteMappedToOsApplicationRef" type="REFERENCE" value="ASPath:/Os/Os/App1">
                        <a:a name="ENABLE" value="true"/>
                    </d:ref>
                </d:ctr>
                <d:ctr name="BswInstance2">
                    <d:ref name="RteBswImplementationRef" type="REFERENCE" value="ASPath:/Rte/Rte/Impl2"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock Rte object
        model = EBModel.getInstance()
        rte = model.getRte()

        # Create parser instance
        parser = RteXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }
        parser.rte = rte

        # Call the method
        parser.read_rte_bsw_module_instances(element, rte)

        # Assertions
        instances = rte.getRteBswModuleInstanceList()
        assert len(instances) == 2

        instance1 = instances[0]
        assert instance1.getName() == "BswInstance1"
        assert instance1.getRteBswImplementationRef().getValue() == "/Rte/Rte/Impl1"
        assert instance1.getRteMappedToOsApplicationRef().getValue() == "/Os/Os/App1"

        instance2 = instances[1]
        assert instance2.getName() == "BswInstance2"
        assert instance2.getRteBswImplementationRef().getValue() == "/Rte/Rte/Impl2"
        assert instance2.getRteMappedToOsApplicationRef() is None

    def test_read_rte_sw_component_instances(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="RteSwComponentInstance" type="MAP">
                <d:ctr name="SwComponent1">
                    <d:ref name="MappedToOsApplicationRef" type="REFERENCE" value="ASPath:/Os/Os/App1">
                        <a:a name="ENABLE" value="true"/>
                    </d:ref>
                    <d:ref name="RteSoftwareComponentInstanceRef" type="REFERENCE" value="ASPath:/Rte/Rte/Comp1">
                        <a:a name="ENABLE" value="true"/>
                    </d:ref>
                </d:ctr>
                <d:ctr name="SwComponent2">
                    <d:ref name="MappedToOsApplicationRef" type="REFERENCE" value="ASPath:/Os/Os/App2"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock Rte object
        model = EBModel.getInstance()
        rte = model.getRte()

        # Create parser instance
        parser = RteXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }
        parser.rte = rte

        # Call the method
        parser.read_rte_sw_component_instances(element, rte)

        # Assertions
        instances = rte.getRteSwComponentInstanceList()
        assert len(instances) == 2

        instance1 = instances[0]
        assert instance1.getName() == "SwComponent1"
        assert instance1.getMappedToOsApplicationRef().getValue() == "/Os/Os/App1"
        assert instance1.getRteSoftwareComponentInstanceRef().getValue() == "/Rte/Rte/Comp1"

        instance2 = instances[1]
        assert instance2.getName() == "SwComponent2"
        assert instance2.getMappedToOsApplicationRef().getValue() == "/Os/Os/App2"
        assert instance2.getRteSoftwareComponentInstanceRef() is None
