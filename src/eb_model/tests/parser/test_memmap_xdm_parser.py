from ...parser.memmap_xdm_parser import MemMapXdmParser
from ...models.memmap_xdm import MemMap, MemMapCommon
from ...models.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestMemMapXdmParser:
    def test_read_memmap_common(self):

        model = EBModel.getInstance()
        memmap = model.getMemMap()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="MemMapCommon" type="IDENTIFIABLE">
                <d:var name="MemMapDevErrorDetect" type="BOOLEAN" value="false"/>
                <d:var name="MemMapApi" type="ENUMERATION" value="MEMMAP_AR_MAJOR_VERSION_4_0_3"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = MemMapXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_memmap_common(element, memmap)

        common = memmap.getMemMapCommon()
        assert common is not None
        assert common.getMemMapDevErrorDetect() is False
        assert common.getMemMapApi() == "MEMMAP_AR_MAJOR_VERSION_4_0_3"