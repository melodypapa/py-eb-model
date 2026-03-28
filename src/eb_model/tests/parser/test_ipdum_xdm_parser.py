import xml.etree.ElementTree as ET
from ...parser.ipdum_xdm_parser import IpduMXdmParser
from ...models.ipdum_xdm import IpduM, IpduMDynPdu
from ...models.eb_doc import EBModel


class TestIpduMXdmParser:
    def test_read_ipdum_dynamic_pdus(self):
        model = EBModel.getInstance()
        ipdum = model.getIpduM()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="IpduMDynamicPdu" type="MAP">
                <d:ctr name="IpduMDynamicPdu_0" type="IDENTIFIABLE">
                    <d:var name="IpduMDynPduId" type="INTEGER" value="1"/>
                    <d:var name="IpduMDynPduLength" type="INTEGER" value="8"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = IpduMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_ipdum_dynamic_pdus(element, ipdum)

        dyn_pdus = ipdum.getIpduMDynPduList()
        assert len(dyn_pdus) == 1
        assert dyn_pdus[0].getIpduMDynPduId() == 1
        assert dyn_pdus[0].getIpduMDynPduLength() == 8