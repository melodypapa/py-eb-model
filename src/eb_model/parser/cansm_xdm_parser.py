"""
CanSM XDM Parser Module - Extracts AUTOSAR CanSM configuration from EB Tresos XDM files.

Implements:
    - SWR_CANSM_00001: CanSM module parsing
    - SWR_CANSM_00002: Network manager configuration parsing
    - SWR_CANSM_00003: Controller configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.core.eb_doc import EBModel
from ..models.can_stack.cansm_xdm import (
    CanSM, CanSMGeneral, CanSMManagerNetwork,
    CanSMController, CanSMDemEventParameterRefs
)
from ..parser.eb_parser import AbstractEbModelParser


class CanSMXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR CanSM (CAN State Manager) module configuration.

    Extracts CanSM configuration including network managers and controllers.

    Implements: SWR_CANSM_00001 (CanSM Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the CanSM XDM parser."""
        super().__init__()
        self.cansm = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse CanSM module configuration from XDM element.

        Implements: SWR_CANSM_00001
        """
        if self.get_component_name(element) != "CanSM":
            raise ValueError("Invalid <%s> xdm file" % "CanSM")

        cansm = doc.getCanSM()

        self.read_version(element, cansm)

        self.logger.info("Parse CanSM ARVersion:<%s> SwVersion:<%s>" % (cansm.getArVersion().getVersion(), cansm.getSwVersion().getVersion()))

        self.cansm = cansm

        self.read_cansm_general(element, cansm)
        self.read_cansm_manager_networks(element, cansm)
        self.read_cansm_dem_event_refs(element, cansm)

    def read_cansm_general(self, element: ET.Element, cansm: CanSM):
        ctr_tag = self.find_ctr_tag(element, "CanSMGeneral")
        if ctr_tag is not None:
            general = CanSMGeneral(cansm, ctr_tag.attrib["name"])
            general.setCanSMDevErrorDetect(self.read_value(ctr_tag, "CanSMDevErrorDetect"))
            general.setCanSMMainFunctionTimePeriod(self.read_value(ctr_tag, "CanSMMainFunctionTimePeriod"))
            general.setCanSMPNSupport(self.read_optional_value(ctr_tag, "CanSMPNSupport"))
            general.setCanSMEnhancedBusOffReporting(self.read_optional_value(ctr_tag, "CanSMEnhancedBusOffReporting"))
            cansm.setCanSMGeneral(general)
            self.logger.debug("Read CanSMGeneral")

    def read_cansm_manager_networks(self, element: ET.Element, cansm: CanSM):
        # CanSMManagerNetwork is within CanSMConfiguration
        config_tag = self.find_ctr_tag(element, "CanSMConfiguration")
        if config_tag is not None:
            for ctr_tag in self.find_ctr_tag_list(config_tag, "CanSMManagerNetwork"):
                network = CanSMManagerNetwork(cansm, ctr_tag.attrib["name"])
                network.setCanSMBorCounterL1ToL2(self.read_optional_value(ctr_tag, "CanSMBorCounterL1ToL2"))
                network.setCanSMBorTimeL1(self.read_optional_value(ctr_tag, "CanSMBorTimeL1"))
                network.setCanSMBorTimeL2(self.read_optional_value(ctr_tag, "CanSMBorTimeL2"))
                network.setCanSMBorTimeTxEnsured(self.read_optional_value(ctr_tag, "CanSMBorTimeTxEnsured"))
                network.setCanSMBorTxConfirmationPolling(self.read_optional_value(ctr_tag, "CanSMBorTxConfirmationPolling"))
                network.setCanSMActivatePN(self.read_optional_value(ctr_tag, "CanSMActivatePN"))
                network.setCanSMComMNetworkHandleRef(self.read_ref_value(ctr_tag, "CanSMComMNetworkHandleRef"))
                network.setCanSMTransceiverId(self.read_ref_value(ctr_tag, "CanSMTransceiverId"))
                cansm.addCanSMManagerNetwork(network)
                self.logger.debug("Read CanSMManagerNetwork <%s>" % network.getName())

    def read_cansm_dem_event_refs(self, element: ET.Element, cansm: CanSM):
        config_tag = self.find_ctr_tag(element, "CanSMConfiguration")
        if config_tag is not None:
            ctr_tag = self.find_ctr_tag(config_tag, "CanSMDemEventParameterRefs")
            if ctr_tag is not None:
                dem_refs = CanSMDemEventParameterRefs(cansm, ctr_tag.attrib["name"])
                dem_refs.setCanSMBusOffDemEventRef(self.read_ref_value(ctr_tag, "CANSM_E_BUS_OFF"))
                cansm.setCanSMDemEventParameterRefs(dem_refs)
                self.logger.debug("Read CanSMDemEventParameterRefs")
