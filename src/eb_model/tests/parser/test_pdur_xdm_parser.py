import xml.etree.ElementTree as ET
from ...parser.pdur_xdm_parser import PduRXdmParser
from ...models.pdur_xdm import PduR, PduRRoutingTableEntry
from ...models.eb_doc import EBModel


class TestPduRXdmParser:
    def test_read_pdur_routing_cfgs(self):
        model = EBModel.getInstance()
        pdur = model.getPduR()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="PduRRoutingTable" type="MAP">
                <d:ctr name="PduRRoutingTable_0" type="IDENTIFIABLE">
                    <d:var name="PduRRoutingTableEntryID" type="INTEGER" value="1"/>
                    <d:var name="PduRRoutingPduSID" type="INTEGER" value="100"/>
                    <d:ref name="PduRDestPduRef" type="REFERENCE" value="ASPath:/Com/Com/ComIPdu/ComTxIPdu_0"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = PduRXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_pdur_routing_cfgs(element, pdur)

        routing_cfgs = pdur.getPduRRoutingTableEntryList()
        assert len(routing_cfgs) == 1
        assert routing_cfgs[0].getPduRRoutingTableEntryID() == 1
        assert routing_cfgs[0].getPduRRoutingPduSID() == 100
