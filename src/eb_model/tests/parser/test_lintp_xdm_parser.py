import xml.etree.ElementTree as ET
from ...parser.lintp_xdm_parser import LinTpXdmParser
from ...models.lintp_xdm import LinTp, LinTpGeneral, LinTpRxNSdu, LinTpTxNSdu
from ...models.eb_doc import EBModel


class TestLinTpXdmParser:
    def test_read_lintp_general(self):
        model = EBModel.getInstance()
        lintp = model.getLinTp()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="LinTpGlobalConfig" type="IDENTIFIABLE">
                <d:var name="LinTpMaxNumberOfRespPendingFrames" type="INTEGER" value="2"/>
                <d:var name="LinTpNumberOfRxNSdu" type="INTEGER" value="4"/>
                <d:var name="LinTpNumberOfTxNSdu" type="INTEGER" value="4"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = LinTpXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_lintp_general(element, lintp)

        general = lintp.getLinTpGeneral()
        assert general is not None
        assert general.getLinTpMaxNumberOfRespPendingFrames() == 2
        assert general.getLinTpNumberOfRxNSdu() == 4
        assert general.getLinTpNumberOfTxNSdu() == 4

    def test_read_lintp_rx_nsdus(self):
        model = EBModel.getInstance()
        lintp = model.getLinTp()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="LinTpGlobalConfig" type="IDENTIFIABLE">
                <d:lst name="LinTpRxNSdu" type="MAP">
                    <d:ctr name="LinTpRxNSdu_0" type="IDENTIFIABLE">
                        <d:var name="LinTpRxNSduId" type="INTEGER" value="0"/>
                        <d:ref name="LinTpRxNSduRef" type="REFERENCE" value="ASPath:/LinIf/LinIfConfig/LinIfRxPdu_0"/>
                    </d:ctr>
                </d:lst>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = LinTpXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_lintp_rx_nsdus(element, lintp)

        rx_nsdus = lintp.getLinTpRxNSduList()
        assert len(rx_nsdus) == 1

        assert rx_nsdus[0].getLinTpRxNSduId() == 0
        assert rx_nsdus[0].getLinTpRxNSduRef().getValue() == "/LinIf/LinIfConfig/LinIfRxPdu_0"

    def test_read_lintp_tx_nsdus(self):
        model = EBModel.getInstance()
        lintp = model.getLinTp()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="LinTpGlobalConfig" type="IDENTIFIABLE">
                <d:lst name="LinTpTxNSdu" type="MAP">
                    <d:ctr name="LinTpTxNSdu_0" type="IDENTIFIABLE">
                        <d:var name="LinTpTxNSduId" type="INTEGER" value="0"/>
                        <d:ref name="LinTpTxNSduRef" type="REFERENCE" value="ASPath:/LinIf/LinIfConfig/LinIfTxPdu_0"/>
                    </d:ctr>
                </d:lst>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = LinTpXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_lintp_tx_nsdus(element, lintp)

        tx_nsdus = lintp.getLinTpTxNSduList()
        assert len(tx_nsdus) == 1

        assert tx_nsdus[0].getLinTpTxNSduId() == 0
        assert tx_nsdus[0].getLinTpTxNSduRef().getValue() == "/LinIf/LinIfConfig/LinIfTxPdu_0"
