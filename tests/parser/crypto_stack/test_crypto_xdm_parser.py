from eb_model.parser.crypto_stack.crypto_xdm_parser import CryptoXdmParser
from eb_model.models.crypto_stack.crypto_xdm import CryptoGeneral
from eb_model.models.core.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestCryptoXdmParser:
    def test_read_crypto_general(self):
        model = EBModel.getInstance()
        crypto = model.getCrypto()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CryptoGeneral" type="IDENTIFIABLE">
                <d:var name="CryptoDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="CryptoEnabled" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = CryptoXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_crypto_general(element, crypto)

        general = crypto.getCryptoGeneral()
        assert general is not None
        assert general.getCryptoDevErrorDetect() is True
