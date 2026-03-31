import xml.etree.ElementTree as ET
from eb_model.parser.lin_stack.linif_xdm_parser import LinIfXdmParser
from eb_model.models.lin_stack.linif_xdm import LinIf, LinIfGeneral, LinIfChannel, LinIfFrame
from eb_model.models.core.eb_doc import EBModel


class TestLinIfXdmParser:
    def test_read_linif_general(self):
        model = EBModel.getInstance()
        linif = model.getLinIf()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="LinIfGeneral" type="IDENTIFIABLE">
                <d:var name="LinIfDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="LinIfMaxChannels" type="INTEGER" value="2"/>
                <d:var name="LinIfTpSupported" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = LinIfXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_linif_general(element, linif)

        general = linif.getLinIfGeneral()
        assert general is not None
        assert general.getLinIfDevErrorDetect() is True
        assert general.getLinIfMaxChannels() == 2
        assert general.getLinIfTpSupported() is True

    def test_read_linif_channels(self):
        model = EBModel.getInstance()
        linif = model.getLinIf()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="LinIfGlobalConfig" type="IDENTIFIABLE">
                <d:lst name="LinIfChannel" type="MAP">
                    <d:ctr name="LinIfChannel_0" type="IDENTIFIABLE">
                        <d:var name="LinIfChannelId" type="INTEGER" value="0"/>
                        <d:ref name="LinIfChannelRef" type="REFERENCE" value="ASPath:/Lin/LinConfig/LinChannel_0"/>
                        <d:ref name="LinIfComMNetworkHandleRef" type="REFERENCE" value="ASPath:/ComM/ComMConfig/ComMChannel_0"/>
                    </d:ctr>
                </d:lst>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = LinIfXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_linif_channels(element, linif)

        channels = linif.getLinIfChannelList()
        assert len(channels) == 1

        assert channels[0].getLinIfChannelId() == 0
        assert channels[0].getLinIfChannelRef().getValue() == "/Lin/LinConfig/LinChannel_0"
        assert channels[0].getLinIfComMNetworkHandleRef().getValue() == "/ComM/ComMConfig/ComMChannel_0"

    def test_read_linif_frames(self):
        model = EBModel.getInstance()
        linif = model.getLinIf()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="LinIfGlobalConfig" type="IDENTIFIABLE">
                <d:lst name="LinIfFrame" type="MAP">
                    <d:ctr name="LinIfFrame_0" type="IDENTIFIABLE">
                        <d:var name="LinIfFrameId" type="INTEGER" value="32"/>
                        <d:var name="LinIfFrameType" type="ENUMERATION" value="LINIF_UNCONDITIONAL"/>
                        <d:var name="LinIfChecksumType" type="ENUMERATION" value="LINIF_CLASSIC"/>
                        <d:var name="LinIfLength" type="INTEGER" value="8"/>
                    </d:ctr>
                </d:lst>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = LinIfXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_linif_frames(element, linif)

        frames = linif.getLinIfFrameList()
        assert len(frames) == 1

        assert frames[0].getLinIfFrameId() == 32
        assert frames[0].getLinIfFrameType() == "LINIF_UNCONDITIONAL"
        assert frames[0].getLinIfChecksumType() == "LINIF_CLASSIC"
        assert frames[0].getLinIfLength() == 8
