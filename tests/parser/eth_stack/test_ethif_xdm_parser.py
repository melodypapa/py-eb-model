import xml.etree.ElementTree as ET
from eb_model.parser.eth_stack.ethif_xdm_parser import EthIfXdmParser
from eb_model.models.eth_stack.ethif_xdm import EthIf, EthIfGeneral, EthIfController
from eb_model.models.core.eb_doc import EBModel


class TestEthIfXdmParser:
    def test_read_ethif_general(self):
        model = EBModel.getInstance()
        ethif = model.getEthIf()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="EthIfGeneral" type="IDENTIFIABLE">
                <d:var name="EthIfDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="EthIfEnableRxInterrupt" type="BOOLEAN" value="false"/>
                <d:var name="EthIfMainFunctionPeriod" type="FLOAT" value="0.01"/>
                <d:var name="EthIfMaxTrcvsTotal" type="INTEGER" value="2"/>
                <d:var name="EthIfSupportEthAPI" type="ENUMERATION" value="ETHIF_API_STANDARD"/>
                <d:var name="EthIfPublicHandleTypeEnum" type="ENUMERATION" value="ETHIF_HANDLE_TYPE_EXTENDED"/>
                <d:var name="EthIfMaxCtrl" type="INTEGER" value="1"/>
                <d:var name="EthIfMaxPhyCtrl" type="INTEGER" value="2"/>
                <d:var name="EthIfMaxEthSwitches" type="INTEGER" value="0"/>
                <d:var name="EthIfMaxSwtPorts" type="INTEGER" value="0"/>
                <d:var name="EthIfRelocatablePbcfgEnable" type="BOOLEAN" value="false"/>
                <d:var name="EthIfVLANSupportEnable" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = EthIfXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_ethif_general(element, ethif)

        general = ethif.getEthIfGeneral()
        assert general is not None
        assert general.getEthIfDevErrorDetect() is True
        assert general.getEthIfEnableRxInterrupt() is False
        assert general.getEthIfMainFunctionPeriod() == 0.01
        assert general.getEthIfMaxTrcvsTotal() == 2
        assert general.getEthIfSupportEthAPI() == "ETHIF_API_STANDARD"
        assert general.getEthIfPublicHandleTypeEnum() == "ETHIF_HANDLE_TYPE_EXTENDED"
        assert general.getEthIfMaxCtrl() == 1
        assert general.getEthIfMaxPhyCtrl() == 2
        assert general.getEthIfMaxEthSwitches() == 0
        assert general.getEthIfMaxSwtPorts() == 0
        assert general.getEthIfRelocatablePbcfgEnable() is False
        assert general.getEthIfVLANSupportEnable() is True

    def test_read_ethif_controllers(self):
        model = EBModel.getInstance()
        ethif = model.getEthIf()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="EthIfController" type="MAP">
                <d:ctr name="EthIfController_0" type="IDENTIFIABLE">
                    <d:var name="EthIfCtrlIdx" type="INTEGER" value="0"/>
                    <d:var name="EthIfCtrlMtu" type="INTEGER" value="1518"/>
                    <d:var name="EthIfMaxTxBufsTotal" type="INTEGER" value="64"/>
                    <d:var name="EthIfVlanId" type="INTEGER" value="0"/>
                    <d:ref name="EthIfEthTrcvRef" type="REFERENCE" value="ASPath:/Eth/Trcv/TrcvConfig_0"/>
                    <d:ref name="EthIfPhysControllerRef" type="REFERENCE" value="ASPath:/EthIf/EthIfPhysController/PhysCtrl_0"/>
                </d:ctr>
                <d:ctr name="EthIfController_1" type="IDENTIFIABLE">
                    <d:var name="EthIfCtrlIdx" type="INTEGER" value="1"/>
                    <d:var name="EthIfCtrlMtu" type="INTEGER" value="1518"/>
                    <d:var name="EthIfMaxTxBufsTotal" type="INTEGER" value="32"/>
                    <d:ref name="EthIfEthTrcvRef" type="REFERENCE" value="ASPath:/Eth/Trcv/TrcvConfig_1"/>
                    <d:ref name="EthIfPhysControllerRef" type="REFERENCE" value="ASPath:/EthIf/EthIfPhysController/PhysCtrl_1"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = EthIfXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_ethif_controllers(element, ethif)

        controllers = ethif.getEthIfControllerList()
        assert len(controllers) == 2

        assert controllers[0].getEthIfCtrlIdx() == 0
        assert controllers[0].getEthIfCtrlMtu() == 1518
        assert controllers[0].getEthIfMaxTxBufsTotal() == 64
        assert controllers[0].getEthIfVlanId() == 0

        assert controllers[1].getEthIfCtrlIdx() == 1
        assert controllers[1].getEthIfCtrlMtu() == 1518
        assert controllers[1].getEthIfMaxTxBufsTotal() == 32
