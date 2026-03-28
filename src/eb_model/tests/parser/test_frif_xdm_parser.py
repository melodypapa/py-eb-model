import xml.etree.ElementTree as ET
from ...parser.frif_xdm_parser import FrIfXdmParser
from ...models.frif_xdm import FrIf, FrIfGeneral, FrIfController
from ...models.eb_doc import EBModel


class TestFrIfXdmParser:
    def test_read_frif_general(self):
        model = EBModel.getInstance()
        frif = model.getFrIf()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="FrIfGeneral" type="IDENTIFIABLE">
                <d:var name="FrIfDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="FrIfMainFunctionPeriod" type="FLOAT" value="0.005"/>
                <d:var name="FrIfMaxNumOfClusters" type="INTEGER" value="1"/>
                <d:var name="FrIfSupportFrApi" type="ENUMERATION" value="FRIF_API_STANDARD"/>
                <d:var name="FrIfPolarizationSelection" type="BOOLEAN" value="false"/>
                <d:var name="FrIfTransceiverAssignment" type="BOOLEAN" value="true"/>
                <d:var name="FrIfWakeupPatternSupport" type="BOOLEAN" value="false"/>
                <d:var name="FrIfVTPSupport" type="BOOLEAN" value="false"/>
                <d:var name="FrIfPublicHandleTypeEnum" type="ENUMERATION" value="FRIF_HANDLE_TYPE_EXTENDED"/>
                <d:var name="FrIfRelocatablePbcfgEnable" type="BOOLEAN" value="false"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = FrIfXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_frif_general(element, frif)

        general = frif.getFrIfGeneral()
        assert general is not None
        assert general.getFrIfDevErrorDetect() is True
        assert general.getFrIfMainFunctionPeriod() == 0.005
        assert general.getFrIfMaxNumOfClusters() == 1
        assert general.getFrIfSupportFrApi() == "FRIF_API_STANDARD"
        assert general.getFrIfPolarizationSelection() is False
        assert general.getFrIfTransceiverAssignment() is True
        assert general.getFrIfWakeupPatternSupport() is False
        assert general.getFrIfVTPSupport() is False
        assert general.getFrIfRelocatablePbcfgEnable() is False

    def test_read_frif_controllers(self):
        model = EBModel.getInstance()
        frif = model.getFrIf()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="FrIfConfig" type="MAP">
                <d:lst name="FrIfController" type="MAP">
                    <d:ctr name="FrIfController_0" type="IDENTIFIABLE">
                        <d:var name="FrIfCtrlIdx" type="INTEGER" value="0"/>
                        <d:var name="FrIfCtrlMtu" type="INTEGER" value="127"/>
                    </d:ctr>
                    <d:ctr name="FrIfController_1" type="IDENTIFIABLE">
                        <d:var name="FrIfCtrlIdx" type="INTEGER" value="1"/>
                        <d:var name="FrIfCtrlMtu" type="INTEGER" value="254"/>
                    </d:ctr>
                </d:lst>
            </d:lst>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = FrIfXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_frif_controllers(element, frif)

        controllers = frif.getFrIfControllerList()
        assert len(controllers) == 2

        assert controllers[0].getFrIfCtrlIdx() == 0
        assert controllers[0].getFrIfCtrlMtu() == 127

        assert controllers[1].getFrIfCtrlIdx() == 1
        assert controllers[1].getFrIfCtrlMtu() == 254
