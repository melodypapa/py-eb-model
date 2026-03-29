from ...parser.ecum_xdm_parser import EcuMXdmParser
from ...models.core.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestEcuMXdmParser:
    def test_read_ecum_general(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="EcuMGeneral" type="IDENTIFIABLE">
                <d:var name="EcuMDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="EcuMConfigurationVariant" type="ENUMERATION" value="PBcfg"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock EcuM object
        model = EBModel.getInstance()
        ecum = model.getEcuM()

        # Create parser instance
        parser = EcuMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_ecum_general(element, ecum)

        # Assertions
        general = ecum.getEcumGeneral()
        assert general is not None
        assert general.getEcumDevErrorDetect() is True
        assert general.getEcumConfigurationVariant() == "PBcfg"

    def test_read_ecum_startup(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="EcuMStartup" type="IDENTIFIABLE">
                <d:var name="EcuMEnableUserMcuStartup" type="BOOLEAN" value="true"/>
                <d:ref name="EcuMUserMcuStartupRef" type="REFERENCE" value="ASPath:/Rte/Rte/StartupHook">
                    <a:a name="ENABLE" value="true"/>
                </d:ref>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock EcuM object
        model = EBModel.getInstance()
        ecum = model.getEcuM()

        # Create parser instance
        parser = EcuMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_ecum_startup(element, ecum)

        # Assertions
        startup = ecum.getEcumStartup()
        assert startup is not None
        assert startup.getEcumEnableUserMcuStartup() is True
        assert startup.getEcumUserMcuStartupRef().getValue() == "/Rte/Rte/StartupHook"

    def test_read_ecum_shutdown(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="EcuMShutdown" type="IDENTIFIABLE">
                <d:var name="EcuMEnableUserMcuShutdown" type="BOOLEAN" value="true"/>
                <d:ref name="EcuMUserMcuShutdownRef" type="REFERENCE" value="ASPath:/Rte/Rte/ShutdownHook">
                    <a:a name="ENABLE" value="true"/>
                </d:ref>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock EcuM object
        model = EBModel.getInstance()
        ecum = model.getEcuM()

        # Create parser instance
        parser = EcuMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_ecum_shutdown(element, ecum)

        # Assertions
        shutdown = ecum.getEcumShutdown()
        assert shutdown is not None
        assert shutdown.getEcumEnableUserMcuShutdown() is True
        assert shutdown.getEcumUserMcuShutdownRef().getValue() == "/Rte/Rte/ShutdownHook"

    def test_read_ecum_alarms(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="EcuMAlarm" type="MAP">
                <d:ctr name="Alarm1">
                    <d:ref name="EcuMAlarmCounterRef" type="REFERENCE" value="ASPath:/Os/Os/Counter1"/>
                    <d:ref name="EcuMAlarmActionRef" type="REFERENCE" value="ASPath:/Os/Os/Alarm1"/>
                </d:ctr>
                <d:ctr name="Alarm2">
                    <d:ref name="EcuMAlarmCounterRef" type="REFERENCE" value="ASPath:/Os/Os/Counter2"/>
                    <d:ref name="EcuMAlarmActionRef" type="REFERENCE" value="ASPath:/Os/Os/Alarm2"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock EcuM object
        model = EBModel.getInstance()
        ecum = model.getEcuM()

        # Create parser instance
        parser = EcuMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_ecum_alarms(element, ecum)

        # Assertions
        alarms = ecum.getEcumAlarmList()
        assert len(alarms) == 2

        alarm1 = alarms[0]
        assert alarm1.getName() == "Alarm1"
        assert alarm1.getEcumAlarmCounterRef().getValue() == "/Os/Os/Counter1"
        assert alarm1.getEcumAlarmActionRef().getValue() == "/Os/Os/Alarm1"

        alarm2 = alarms[1]
        assert alarm2.getName() == "Alarm2"
        assert alarm2.getEcumAlarmCounterRef().getValue() == "/Os/Os/Counter2"
        assert alarm2.getEcumAlarmActionRef().getValue() == "/Os/Os/Alarm2"
