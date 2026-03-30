import xml.etree.ElementTree as ET
from eb_model.parser.can_stack.cannm_xdm_parser import CanNmXdmParser
from eb_model.models.can_stack.cannm_xdm import CanNm, CanNmGeneral, CanNmGlobalConfig, CanNmChannel, CanNmRxPdu, CanNmTxPdu
from eb_model.models.core.eb_doc import EBModel


class TestCanNmXdmParser:
    def test_read_cannm_general(self):
        model = EBModel.getInstance()
        cannm = model.getCanNm()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CanNmGeneral" type="IDENTIFIABLE">
                <d:var name="CanNmMultiCoreSupport" type="BOOLEAN" value="true"/>
                <d:var name="CanNmPnSupported" type="BOOLEAN" value="false"/>
                <d:var name="CanNmMaxPn" type="INTEGER" value="4"/>
                <d:var name="CanNmDetRuntimeChecks" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = CanNmXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_cannm_general(element, cannm)

        general = cannm.getCanNmGeneral()
        assert general is not None
        assert general.getCanNmMultiCoreSupport() is True
        assert general.getCanNmPnSupported() is False
        assert general.getCanNmMaxPn() == 4
        assert general.getCanNmDetRuntimeChecks() is True

    def test_read_cannm_global_config(self):
        model = EBModel.getInstance()
        cannm = model.getCanNm()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CanNmGlobalConfig" type="IDENTIFIABLE">
                <d:var name="CanNmDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="CanNmPassiveModeEnabled" type="BOOLEAN" value="false"/>
                <d:var name="CanNmBusLoadReductionEnabled" type="BOOLEAN" value="true"/>
                <d:var name="CanNmRemoteSleepIndEnabled" type="BOOLEAN" value="false"/>
                <d:var name="CanNmStateChangeIndEnabled" type="BOOLEAN" value="true"/>
                <d:var name="CanNmComUserDataSupport" type="BOOLEAN" value="false"/>
                <d:var name="CanNmMainFunctionPeriod" type="FLOAT" value="0.01"/>
                <d:var name="CanNmNumberOfChannels" type="INTEGER" value="2"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = CanNmXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_cannm_global_config(element, cannm)

        global_config = cannm.getCanNmGlobalConfig()
        assert global_config is not None
        assert global_config.getCanNmDevErrorDetect() is True
        assert global_config.getCanNmPassiveModeEnabled() is False
        assert global_config.getCanNmBusLoadReductionEnabled() is True
        assert global_config.getCanNmRemoteSleepIndEnabled() is False
        assert global_config.getCanNmStateChangeIndEnabled() is True
        assert global_config.getCanNmComUserDataSupport() is False
        assert global_config.getCanNmMainFunctionPeriod() == 0.01
        assert global_config.getCanNmNumberOfChannels() == 2

    def test_read_cannm_channels(self):
        model = EBModel.getInstance()
        cannm = model.getCanNm()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CanNmGlobalConfig" type="IDENTIFIABLE">
                <d:lst name="CanNmChannel" type="MAP">
                    <d:ctr name="CanNmChannel_0" type="IDENTIFIABLE">
                        <d:var name="CanNmNodeIdEnabled" type="BOOLEAN" value="true"/>
                        <d:var name="CanNmPnEnabled" type="BOOLEAN" value="false"/>
                        <d:var name="CanNmMsgCycleTime" type="FLOAT" value="0.5"/>
                        <d:var name="CanNmTimeoutTime" type="FLOAT" value="1.5"/>
                        <d:var name="CanNmNetworkHandle" type="INTEGER" value="0"/>
                        <d:ref name="CanNmCanNmChannelRef" type="REFERENCE" value="ASPath:/CanNm/CanNmConfig/CanNmChannel_0"/>
                    </d:ctr>
                </d:lst>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = CanNmXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_cannm_channels(element, cannm)

        channels = cannm.getCanNmChannelList()
        assert len(channels) == 1

        assert channels[0].getCanNmNodeIdEnabled() is True
        assert channels[0].getCanNmPnEnabled() is False
        assert channels[0].getCanNmMsgCycleTime() == 0.5
        assert channels[0].getCanNmTimeoutTime() == 1.5
        assert channels[0].getCanNmNetworkHandle() == 0

    def test_read_cannm_rx_pdus(self):
        model = EBModel.getInstance()
        cannm = model.getCanNm()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CanNmGlobalConfig" type="IDENTIFIABLE">
                <d:lst name="CanNmRxPdu" type="MAP">
                    <d:ctr name="CanNmRxPdu_0" type="IDENTIFIABLE">
                        <d:var name="CanNmRxPduId" type="INTEGER" value="0"/>
                        <d:ref name="CanNmRxPduRef" type="REFERENCE" value="ASPath:/CanIf/CanIfInitCfg/CanIfRxPduCfg/CanNm_Rx"/>
                    </d:ctr>
                </d:lst>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = CanNmXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_cannm_rx_pdus(element, cannm)

        rx_pdus = cannm.getCanNmRxPduList()
        assert len(rx_pdus) == 1

        assert rx_pdus[0].getCanNmRxPduId() == 0
        assert rx_pdus[0].getCanNmRxPduRef().getValue() == "/CanIf/CanIfInitCfg/CanIfRxPduCfg/CanNm_Rx"

    def test_read_cannm_tx_pdus(self):
        model = EBModel.getInstance()
        cannm = model.getCanNm()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CanNmGlobalConfig" type="IDENTIFIABLE">
                <d:lst name="CanNmTxPdu" type="MAP">
                    <d:ctr name="CanNmTxPdu_0" type="IDENTIFIABLE">
                        <d:var name="CanNmTxConfirmationPduId" type="INTEGER" value="0"/>
                        <d:ref name="CanNmTxPduRef" type="REFERENCE" value="ASPath:/CanIf/CanIfInitCfg/CanIfTxPduCfg/CanNm_Tx"/>
                    </d:ctr>
                </d:lst>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = CanNmXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_cannm_tx_pdus(element, cannm)

        tx_pdus = cannm.getCanNmTxPduList()
        assert len(tx_pdus) == 1

        assert tx_pdus[0].getCanNmTxConfirmationPduId() == 0
        assert tx_pdus[0].getCanNmTxPduRef().getValue() == "/CanIf/CanIfInitCfg/CanIfTxPduCfg/CanNm_Tx"
