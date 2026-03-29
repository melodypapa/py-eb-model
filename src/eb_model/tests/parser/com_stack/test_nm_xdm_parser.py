import xml.etree.ElementTree as ET
from ....parser.nm_xdm_parser import NmXdmParser
from ....models.com_stack.nm_xdm import Nm, NmChannel
from ....models.core.eb_doc import EBModel


class TestNmXdmParser:
    def test_read_nm_channels(self):
        model = EBModel.getInstance()
        nm = model.getNm()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="NmChannel" type="MAP">
                <d:ctr name="NmChannel_Can" type="IDENTIFIABLE">
                    <d:var name="NmChannelId" type="INTEGER" value="1"/>
                    <d:var name="NmBusType" type="ENUMERATION" value="CAN"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = NmXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_nm_channels(element, nm)

        channels = nm.getNmChannelList()
        assert len(channels) == 1
        assert channels[0].getNmChannelId() == 1
        assert channels[0].getNmBusType() == "CAN"
