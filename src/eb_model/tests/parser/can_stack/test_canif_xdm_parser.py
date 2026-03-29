import xml.etree.ElementTree as ET
from ....parser.canif_xdm_parser import CanIfXdmParser
from ....models.can_stack.canif_xdm import CanIf, CanIfGeneral, CanIfCtrlCfg, CanIfDispatchCfg
from ....models.core.eb_doc import EBModel


class TestCanIfXdmParser:
    def test_read_canif_general(self):
        model = EBModel.getInstance()
        canif = model.getCanIf()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CanIfPublicCfg" type="IDENTIFIABLE">
                <d:var name="CanIfPublicDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="CanIfPublicNumberOfCanHwUnits" type="INTEGER" value="2"/>
                <d:var name="CanIfPublicMaxCtrl" type="INTEGER" value="1"/>
                <d:var name="CanIfPublicMaxTxPdus" type="INTEGER" value="100"/>
                <d:var name="CanIfPublicMaxRxPdus" type="INTEGER" value="100"/>
            </d:ctr>
            <d:ctr name="CanIfPrivateCfg" type="IDENTIFIABLE">
                <d:var name="CanIfSupportTTCAN" type="BOOLEAN" value="false"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = CanIfXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_canif_general(element, canif)

        general = canif.getCanIfGeneral()
        assert general is not None
        assert general.getCanIfDevErrorDetect() is True
        assert general.getCanIfPublicNumberOfCanHwUnits() == 2
        assert general.getCanIfPublicMaxCtrl() == 1
        assert general.getCanIfPublicMaxTxPdus() == 100
        assert general.getCanIfPublicMaxRxPdus() == 100
        assert general.getCanIfSupportTTCAN() is False

    def test_read_canif_ctrl_cfgs(self):
        model = EBModel.getInstance()
        canif = model.getCanIf()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="CanIfCtrlCfg" type="MAP">
                <d:ctr name="CanIfCtrlCfg_0" type="IDENTIFIABLE">
                    <d:var name="CanIfCtrlId" type="INTEGER" value="0"/>
                    <d:var name="CanIfCtrlWakeupSupport" type="BOOLEAN" value="true"/>
                    <d:ref name="CanIfCtrlCanCtrlRef" type="REFERENCE" value="ASPath:/Can/Can/CanConfigSet/CanConfig_0"/>
                </d:ctr>
                <d:ctr name="CanIfCtrlCfg_1" type="IDENTIFIABLE">
                    <d:var name="CanIfCtrlId" type="INTEGER" value="1"/>
                    <d:var name="CanIfCtrlWakeupSupport" type="BOOLEAN" value="false"/>
                    <d:ref name="CanIfCtrlCanCtrlRef" type="REFERENCE" value="ASPath:/Can/Can/CanConfigSet/CanConfig_1"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = CanIfXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_canif_ctrl_cfgs(element, canif)

        ctrl_cfgs = canif.getCanIfCtrlCfgList()
        assert len(ctrl_cfgs) == 2

        assert ctrl_cfgs[0].getCanIfCtrlId() == 0
        assert ctrl_cfgs[0].getCanIfCtrlWakeupSupport() is True
        assert ctrl_cfgs[0].getCanIfCtrlCanCtrlRef().getValue() == "/Can/Can/CanConfigSet/CanConfig_0"

        assert ctrl_cfgs[1].getCanIfCtrlId() == 1
        assert ctrl_cfgs[1].getCanIfCtrlWakeupSupport() is False

    def test_read_canif_dispatch_cfg(self):
        model = EBModel.getInstance()
        canif = model.getCanIf()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CanIfDispatchCfg" type="IDENTIFIABLE">
                <d:var name="CanIfDispatchUserCtrlBusOffName" type="FUNCTION-NAME" value="CanIf_CallbackBusOff"/>
                <d:var name="CanIfDispatchUserCtrlModeIndicationName" type="FUNCTION-NAME" value="CanIf_CallbackCtrlMode"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = CanIfXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_canif_dispatch_cfg(element, canif)

        cfg = canif.getCanIfDispatchCfg()
        assert cfg is not None
        assert cfg.getCanIfDispatchUserCtrlBusOffName() == "CanIf_CallbackBusOff"
        assert cfg.getCanIfDispatchUserCtrlModeIndicationName() == "CanIf_CallbackCtrlMode"

    def test_read_canif_rx_pdu_cfgs(self):
        model = EBModel.getInstance()
        canif = model.getCanIf()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="CanIfRxPduCfg" type="MAP">
                <d:ctr name="CanIfRxPduCfg_Engine" type="IDENTIFIABLE">
                    <d:var name="CanIfRxPduCanId" type="INTEGER" value="291"/>
                    <d:var name="CanIfRxPduCanIdType" type="ENUMERATION" value="STANDARD_CAN"/>
                    <d:var name="CanIfRxPduDlc" type="INTEGER" value="8"/>
                    <d:var name="CanIfRxPduId" type="INTEGER" value="1"/>
                    <d:ref name="CanIfRxPduHrhIdRef" type="REFERENCE" value="ASPath:/CanIf/CanIfInitCfg/CanIfHrhCfg/CanIfHrhCfg_0"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = CanIfXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_canif_rx_pdu_cfgs(element, canif)

        rx_cfgs = canif.getCanIfRxPduCfgList()
        assert len(rx_cfgs) == 1

        assert rx_cfgs[0].getCanIfRxPduCanId() == 291
        assert rx_cfgs[0].getCanIfRxPduCanIdType() == "STANDARD_CAN"
        assert rx_cfgs[0].getCanIfRxPduDlc() == 8
        assert rx_cfgs[0].getCanIfRxPduId() == 1

    def test_read_canif_tx_pdu_cfgs(self):
        model = EBModel.getInstance()
        canif = model.getCanIf()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="CanIfTxPduCfg" type="MAP">
                <d:ctr name="CanIfTxPduCfg_Status" type="IDENTIFIABLE">
                    <d:var name="CanIfTxPduCanId" type="INTEGER" value="1110"/>
                    <d:var name="CanIfTxPduCanIdType" type="ENUMERATION" value="EXTENDED_CAN"/>
                    <d:var name="CanIfTxPduDlc" type="INTEGER" value="8"/>
                    <d:var name="CanIfTxPduId" type="INTEGER" value="2"/>
                    <d:var name="CanIfTxPduType" type="ENUMERATION" value="STATIC"/>
                    <d:ref name="CanIfTxPduHthIdRef" type="REFERENCE" value="ASPath:/CanIf/CanIfInitCfg/CanIfHthCfg/CanIfHthCfg_0"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = CanIfXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_canif_tx_pdu_cfgs(element, canif)

        tx_cfgs = canif.getCanIfTxPduCfgList()
        assert len(tx_cfgs) == 1

        assert tx_cfgs[0].getCanIfTxPduCanId() == 1110
        assert tx_cfgs[0].getCanIfTxPduCanIdType() == "EXTENDED_CAN"
        assert tx_cfgs[0].getCanIfTxPduDlc() == 8
        assert tx_cfgs[0].getCanIfTxPduId() == 2
        assert tx_cfgs[0].getCanIfTxPduType() == "STATIC"
