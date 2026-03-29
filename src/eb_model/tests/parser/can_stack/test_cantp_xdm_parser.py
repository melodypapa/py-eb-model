import xml.etree.ElementTree as ET
from ....parser.cantp_xdm_parser import CanTpXdmParser
from ....models.can_stack.cantp_xdm import CanTp, CanTpGeneral, CanTpChannel, CanTpRxNSdu, CanTpTxNSdu
from ....models.core.eb_doc import EBModel


class TestCanTpXdmParser:
    def test_read_cantp_general(self):
        model = EBModel.getInstance()
        cantp = model.getCanTp()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CanTpGeneral" type="IDENTIFIABLE">
                <d:var name="CanTpDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="CanTpMainFunctionPeriod" type="FLOAT" value="0.005"/>
                <d:var name="CanTpMaxTxChannels" type="INTEGER" value="2"/>
                <d:var name="CanTpMaxRxChannels" type="INTEGER" value="2"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = CanTpXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_cantp_general(element, cantp)

        general = cantp.getCanTpGeneral()
        assert general is not None
        assert general.getCanTpDevErrorDetect() is True
        assert general.getCanTpMainFunctionPeriod() == 0.005
        assert general.getCanTpMaxTxChannels() == 2
        assert general.getCanTpMaxRxChannels() == 2

    def test_read_cantp_channels(self):
        model = EBModel.getInstance()
        cantp = model.getCanTp()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CanTpConfig" type="IDENTIFIABLE">
                <d:lst name="CanTpChannel" type="MAP">
                    <d:ctr name="CanTpChannel_0" type="IDENTIFIABLE">
                        <d:var name="CanTpChannelMode" type="ENUMERATION" value="CANTP_CHANNEL_MODE_FULL_DUPLEX"/>
                        <d:var name="CanTpSTmin" type="FLOAT" value="0.0"/>
                    </d:ctr>
                    <d:ctr name="CanTpChannel_1" type="IDENTIFIABLE">
                        <d:var name="CanTpChannelMode" type="ENUMERATION" value="CANTP_CHANNEL_MODE_TX_ONLY"/>
                        <d:var name="CanTpSTmin" type="FLOAT" value="0.001"/>
                    </d:ctr>
                </d:lst>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = CanTpXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_cantp_channels(element, cantp)

        channels = cantp.getCanTpChannelList()
        assert len(channels) == 2

        assert channels[0].getCanTpChannelMode() == "CANTP_CHANNEL_MODE_FULL_DUPLEX"
        assert channels[0].getCanTpSTmin() == 0.0

        assert channels[1].getCanTpChannelMode() == "CANTP_CHANNEL_MODE_TX_ONLY"
        assert channels[1].getCanTpSTmin() == 0.001

    def test_read_cantp_rx_nsdus(self):
        model = EBModel.getInstance()
        cantp = model.getCanTp()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CanTpConfig" type="IDENTIFIABLE">
                <d:lst name="CanTpRxNSdu" type="MAP">
                    <d:ctr name="CanTpRxNSdu_0" type="IDENTIFIABLE">
                        <d:var name="CanTpRxNSduId" type="INTEGER" value="0"/>
                        <d:ref name="CanTpRxNSduRef" type="REFERENCE" value="ASPath:/CanIf/CanIfInitCfg/CanIfRxPduCfg/CanTp_Rx"/>
                        <d:var name="CanTpBs" type="INTEGER" value="16"/>
                        <d:var name="CanTpSTmin" type="FLOAT" value="0.0"/>
                    </d:ctr>
                </d:lst>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = CanTpXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_cantp_rx_nsdus(element, cantp)

        rx_nsdus = cantp.getCanTpRxNSduList()
        assert len(rx_nsdus) == 1

        assert rx_nsdus[0].getCanTpRxNSduId() == 0
        assert rx_nsdus[0].getCanTpRxNSduRef().getValue() == "/CanIf/CanIfInitCfg/CanIfRxPduCfg/CanTp_Rx"
        assert rx_nsdus[0].getCanTpBs() == 16
        assert rx_nsdus[0].getCanTpSTmin() == 0.0

    def test_read_cantp_tx_nsdus(self):
        model = EBModel.getInstance()
        cantp = model.getCanTp()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CanTpConfig" type="IDENTIFIABLE">
                <d:lst name="CanTpTxNSdu" type="MAP">
                    <d:ctr name="CanTpTxNSdu_0" type="IDENTIFIABLE">
                        <d:var name="CanTpTxNSduId" type="INTEGER" value="0"/>
                        <d:ref name="CanTpTxNSduRef" type="REFERENCE" value="ASPath:/CanIf/CanIfInitCfg/CanIfTxPduCfg/CanTp_Tx"/>
                        <d:var name="CanTpTc" type="BOOLEAN" value="true"/>
                        <d:var name="CanTpSTmin" type="FLOAT" value="0.002"/>
                    </d:ctr>
                </d:lst>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = CanTpXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_cantp_tx_nsdus(element, cantp)

        tx_nsdus = cantp.getCanTpTxNSduList()
        assert len(tx_nsdus) == 1

        assert tx_nsdus[0].getCanTpTxNSduId() == 0
        assert tx_nsdus[0].getCanTpTxNSduRef().getValue() == "/CanIf/CanIfInitCfg/CanIfTxPduCfg/CanTp_Tx"
        assert tx_nsdus[0].getCanTpTc() is True
        assert tx_nsdus[0].getCanTpSTmin() == 0.002
