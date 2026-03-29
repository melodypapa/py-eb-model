import xml.etree.ElementTree as ET
from ....parser.comm_xdm_parser import ComMXdmParser
from ....models.com_stack.comm_xdm import ComM, ComMChannel
from ....models.core.eb_doc import EBModel


class TestComMXdmParser:
    def test_read_comm_channels(self):
        model = EBModel.getInstance()
        comm = model.getComM()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="ComMChannel" type="MAP">
                <d:ctr name="ComMChannel_Can" type="IDENTIFIABLE">
                    <d:var name="ComMChannelName" type="STRING" value="CanIf"/>
                    <d:var name="ComMChannelId" type="INTEGER" value="1"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = ComMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_comm_channels(element, comm)

        channels = comm.getComMChannelList()
        assert len(channels) == 1
        assert channels[0].getComMChannelName() == "CanIf"
        assert channels[0].getComMChannelId() == 1
