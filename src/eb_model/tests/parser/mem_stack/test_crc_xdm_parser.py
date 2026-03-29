"""
Unit tests for Crc XDM Parser.

Implements:
    - SWR_CRC_00001: Crc module parser tests
    - SWR_CRC_00002: Crc configuration parsing tests
"""
import xml.etree.ElementTree as ET
from ....parser.crc_xdm_parser import CrcXdmParser
from ....models.mem_stack.crc_xdm import Crc, CrcConfig
from ....models.core.eb_doc import EBModel


class TestCrcXdmParser:
    def test_read_crc_config(self):
        """
        Test reading Crc configuration from XDM.

        Implements: SWR_CRC_00002 (Crc configuration parsing test)
        """
        model = EBModel.getInstance()
        crc = model.getCrc()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="CrcConfig" type="MAP">
                <d:ctr name="CrcConfig_0" type="IDENTIFIABLE">
                    <d:var name="CrcId" type="INTEGER" value="1"/>
                    <d:var name="CrcCRCType" type="ENUMERATION" value="CRC_8"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = CrcXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_crc_configs(element, crc)

        configs = crc.getCrcConfigList()
        assert len(configs) == 1
        assert configs[0].getCrcId() == 1
        assert configs[0].getCrcCRCType() == "CRC_8"
