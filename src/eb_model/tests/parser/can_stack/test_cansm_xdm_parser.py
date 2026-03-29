import xml.etree.ElementTree as ET
from ....parser.cansm_xdm_parser import CanSMXdmParser
from ....models.can_stack.cansm_xdm import CanSM, CanSMGeneral, CanSMManagerNetwork, CanSMDemEventParameterRefs
from ....models.core.eb_doc import EBModel


class TestCanSMXdmParser:
    def test_read_cansm_general(self):
        model = EBModel.getInstance()
        cansm = model.getCanSM()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CanSMGeneral" type="IDENTIFIABLE">
                <d:var name="CanSMDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="CanSMMainFunctionTimePeriod" type="FLOAT" value="0.01"/>
                <d:var name="CanSMPNSupport" type="BOOLEAN" value="false"/>
                <d:var name="CanSMEnhancedBusOffReporting" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = CanSMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_cansm_general(element, cansm)

        general = cansm.getCanSMGeneral()
        assert general is not None
        assert general.getCanSMDevErrorDetect() is True
        assert general.getCanSMMainFunctionTimePeriod() == 0.01
        assert general.getCanSMPNSupport() is False
        assert general.getCanSMEnhancedBusOffReporting() is True

    def test_read_cansm_manager_networks(self):
        model = EBModel.getInstance()
        cansm = model.getCanSM()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CanSMConfiguration" type="IDENTIFIABLE">
                <d:lst name="CanSMManagerNetwork" type="MAP">
                    <d:ctr name="CanSMManagerNetwork_0" type="IDENTIFIABLE">
                        <d:var name="CanSMBorCounterL1ToL2" type="INTEGER" value="8"/>
                        <d:var name="CanSMBorTimeL1" type="FLOAT" value="0.05"/>
                        <d:var name="CanSMBorTimeL2" type="FLOAT" value="0.1"/>
                        <d:var name="CanSMBorTimeTxEnsured" type="FLOAT" value="0.02"/>
                        <d:var name="CanSMBorTxConfirmationPolling" type="BOOLEAN" value="true"/>
                        <d:var name="CanSMActivatePN" type="BOOLEAN" value="false"/>
                        <d:ref name="CanSMComMNetworkHandleRef" type="REFERENCE" value="ASPath:/ComM/ComMConfig/ComMChannel_0"/>
                        <d:ref name="CanSMTransceiverId" type="REFERENCE" value="ASPath:/CanTrcv/CanTrcvConfig/CanTrcv_0"/>
                    </d:ctr>
                </d:lst>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = CanSMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_cansm_manager_networks(element, cansm)

        networks = cansm.getCanSMManagerNetworkList()
        assert len(networks) == 1

        assert networks[0].getCanSMBorCounterL1ToL2() == 8
        assert networks[0].getCanSMBorTimeL1() == 0.05
        assert networks[0].getCanSMBorTimeL2() == 0.1
        assert networks[0].getCanSMBorTimeTxEnsured() == 0.02
        assert networks[0].getCanSMBorTxConfirmationPolling() is True
        assert networks[0].getCanSMActivatePN() is False
        assert networks[0].getCanSMComMNetworkHandleRef().getValue() == "/ComM/ComMConfig/ComMChannel_0"
        assert networks[0].getCanSMTransceiverId().getValue() == "/CanTrcv/CanTrcvConfig/CanTrcv_0"

    def test_read_cansm_dem_event_refs(self):
        model = EBModel.getInstance()
        cansm = model.getCanSM()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CanSMConfiguration" type="IDENTIFIABLE">
                <d:ctr name="CanSMDemEventParameterRefs" type="IDENTIFIABLE">
                    <d:ref name="CANSM_E_BUS_OFF" type="REFERENCE" value="ASPath:/Dem/DemConfigSet/CANSM_E_BUS_OFF"/>
                </d:ctr>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)

        parser = CanSMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_cansm_dem_event_refs(element, cansm)

        dem_refs = cansm.getCanSMDemEventParameterRefs()
        assert dem_refs is not None
        assert dem_refs.getCanSMBusOffDemEventRef().getValue() == "/Dem/DemConfigSet/CANSM_E_BUS_OFF"
