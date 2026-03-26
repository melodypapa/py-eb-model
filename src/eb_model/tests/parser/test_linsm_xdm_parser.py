import xml.etree.ElementTree as ET
from ...parser.linsm_xdm_parser import LinSMXdmParser
from ...models.linsm_xdm import LinSM, LinSMGeneral, LinSMChannel
from ...models.eb_doc import EBModel


class TestLinSMXdmParser:
    def test_read_linsm_general(self):
        model = EBModel.getInstance()
        linsm = model.getLinSM()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="LinSMGeneral" type="IDENTIFIABLE">
                <d:var name="LinSMDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="LinSMMainProcessingPeriod" type="FLOAT" value="0.01"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = LinSMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_linsm_general(element, linsm)

        general = linsm.getLinSMGeneral()
        assert general is not None
        assert general.getLinSMDevErrorDetect() is True
        assert general.getLinSMMainProcessingPeriod() == 0.01

    def test_read_linsm_channels(self):
        model = EBModel.getInstance()
        linsm = model.getLinSM()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="LinSMConfigSet" type="IDENTIFIABLE">
                <d:lst name="LinSMChannel" type="MAP">
                    <d:ctr name="LinSMChannel_0" type="IDENTIFIABLE">
                        <d:var name="LinSMConfirmationTimeout" type="FLOAT" value="5.0"/>
                        <d:var name="LinSMSleepSupport" type="BOOLEAN" value="true"/>
                        <d:ref name="LinSMComMNetworkHandleRef" type="REFERENCE" value="ASPath:/ComM/ComMConfig/ComMChannel_0"/>
                        <d:var name="LinSMNodeType" type="ENUMERATION" value="LIN_MASTER"/>
                    </d:ctr>
                </d:lst>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = LinSMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_linsm_channels(element, linsm)

        channels = linsm.getLinSMChannelList()
        assert len(channels) == 1

        assert channels[0].getLinSMConfirmationTimeout() == 5.0
        assert channels[0].getLinSMSleepSupport() is True
        assert channels[0].getLinSMComMNetworkHandleRef().getValue() == "/ComM/ComMConfig/ComMChannel_0"
        assert channels[0].getLinSMNodeType() == "LIN_MASTER"
