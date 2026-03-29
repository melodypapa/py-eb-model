"""
EthIf XDM Parser Module - Extracts AUTOSAR EthIf configuration from EB Tresos XDM files.

Implements:
    - SWR_ETHIF_00001: EthIf module parsing
    - SWR_ETHIF_00002: General configuration parsing
    - SWR_ETHIF_00003: Controller configuration parsing
    - SWR_ETHIF_00004: Physical controller configuration parsing
    - SWR_ETHIF_00005: Switch configuration parsing
    - SWR_ETHIF_00006: Transceiver configuration parsing
    - SWR_ETHIF_00007: RX/TX indication configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.core.eb_doc import EBModel
from ..models.eth_stack.ethif_xdm import (
    EthIf, EthIfGeneral, EthIfController, EthIfFrameOwnerConfig,
    EthIfPhysController, EthIfSwitch, EthIfSwitchPortGroup,
    EthIfTransceiver, EthIfRxIndicationConfig, EthIfTxConfirmationConfig,
    EthIfEthControllerType, EthIfEthTrcvType, EthIfEthSwtType
)
from ..parser.eb_parser import AbstractEbModelParser


class EthIfXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR EthIf (Ethernet Interface) module configuration.

    Extracts EthIf configuration including controllers, switches, transceivers,
    and RX/TX indication configurations.

    Implements: SWR_ETHIF_00001 (EthIf Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the EthIf XDM parser."""
        super().__init__()
        self.ethif = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse EthIf module configuration from XDM element.

        Implements: SWR_ETHIF_00001
        """
        if self.get_component_name(element) != "EthIf":
            raise ValueError("Invalid <%s> xdm file" % "EthIf")

        ethif = doc.getEthIf()

        self.read_version(element, ethif)

        self.logger.info("Parse EthIf ARVersion:<%s> SwVersion:<%s>" % (ethif.getArVersion().getVersion(), ethif.getSwVersion().getVersion()))

        self.ethif = ethif

        self.read_ethif_general(element, ethif)
        self.read_ethif_defensive_programming(element, ethif)
        self.read_ethif_controllers(element, ethif)
        self.read_ethif_frame_owner_configs(element, ethif)
        self.read_ethif_phys_controllers(element, ethif)
        self.read_ethif_switches(element, ethif)
        self.read_ethif_switch_port_groups(element, ethif)
        self.read_ethif_transceivers(element, ethif)
        self.read_ethif_rx_indication_configs(element, ethif)
        self.read_ethif_tx_confirmation_configs(element, ethif)
        self.read_ethif_eth_controller_types(element, ethif)
        self.read_ethif_eth_trcv_types(element, ethif)
        self.read_ethif_eth_swt_types(element, ethif)

    def read_ethif_general(self, element: ET.Element, ethif: EthIf):
        """
        Parse EthIf general configuration.

        Implements: SWR_ETHIF_00002
        """
        ctr_tag = self.find_ctr_tag(element, "EthIfGeneral")
        if ctr_tag is not None:
            general = EthIfGeneral(ethif, ctr_tag.attrib["name"])
            general.setEthIfDevErrorDetect(self.read_value(ctr_tag, "EthIfDevErrorDetect"))
            general.setEthIfEnableRxInterrupt(self.read_value(ctr_tag, "EthIfEnableRxInterrupt"))
            general.setEthIfMainFunctionPeriod(self.read_value(ctr_tag, "EthIfMainFunctionPeriod"))
            general.setEthIfMaxTrcvsTotal(self.read_value(ctr_tag, "EthIfMaxTrcvsTotal"))
            general.setEthIfSupportEthAPI(self.read_value(ctr_tag, "EthIfSupportEthAPI"))
            general.setEthIfPublicHandleTypeEnum(self.read_value(ctr_tag, "EthIfPublicHandleTypeEnum"))
            general.setEthIfMaxCtrl(self.read_value(ctr_tag, "EthIfMaxCtrl"))
            general.setEthIfMaxPhyCtrl(self.read_value(ctr_tag, "EthIfMaxPhyCtrl"))
            general.setEthIfMaxEthSwitches(self.read_value(ctr_tag, "EthIfMaxEthSwitches"))
            general.setEthIfMaxSwtPorts(self.read_value(ctr_tag, "EthIfMaxSwtPorts"))
            general.setEthIfRelocatablePbcfgEnable(self.read_optional_value(ctr_tag, "EthIfRelocatablePbcfgEnable"))
            general.setEthIfVLANSupportEnable(self.read_value(ctr_tag, "EthIfVLANSupportEnable"))
            ethif.setEthIfGeneral(general)
            self.logger.debug("Read EthIfGeneral")

    def read_ethif_defensive_programming(self, element: ET.Element, ethif: EthIf):
        """Parse EthIf defensive programming configuration."""
        ctr_tag = self.find_ctr_tag(element, "EthIfDefensiveProgramming")
        if ctr_tag is not None:
            general = ethif.getEthIfGeneral()
            if general is not None:
                general.setEthIfDefProgEnabled(self.read_value(ctr_tag, "EthIfDefProgEnabled"))
                general.setEthIfPrecondAssertEnabled(self.read_value(ctr_tag, "EthIfPrecondAssertEnabled"))
                general.setEthIfPostcondAssertEnabled(self.read_value(ctr_tag, "EthIfPostcondAssertEnabled"))
                general.setEthIfStaticAssertEnabled(self.read_value(ctr_tag, "EthIfStaticAssertEnabled"))
                general.setEthIfUnreachAssertEnabled(self.read_value(ctr_tag, "EthIfUnreachAssertEnabled"))
                general.setEthIfInvariantAssertEnabled(self.read_value(ctr_tag, "EthIfInvariantAssertEnabled"))
            self.logger.debug("Read EthIfDefensiveProgramming")

    def read_ethif_controllers(self, element: ET.Element, ethif: EthIf):
        """
        Parse EthIf controller configurations.

        Implements: SWR_ETHIF_00003
        """
        for ctr_tag in self.find_ctr_tag_list(element, "EthIfController"):
            cfg = EthIfController(ethif, ctr_tag.attrib["name"])
            cfg.setEthIfCtrlIdx(self.read_value(ctr_tag, "EthIfCtrlIdx"))
            cfg.setEthIfCtrlMtu(self.read_value(ctr_tag, "EthIfCtrlMtu"))
            cfg.setEthIfMaxTxBufsTotal(self.read_value(ctr_tag, "EthIfMaxTxBufsTotal"))
            cfg.setEthIfVlanId(self.read_optional_value(ctr_tag, "EthIfVlanId"))
            cfg.setEthIfEthTrcvRef(self.read_ref_value(ctr_tag, "EthIfEthTrcvRef"))
            cfg.setEthIfPhysControllerRef(self.read_ref_value(ctr_tag, "EthIfPhysControllerRef"))
            cfg.setEthIfSwitchRefOrPortGroupRef(self.read_optional_ref_value(ctr_tag, "EthIfSwitchRefOrPortGroupRef"))
            ethif.addEthIfController(cfg)
            self.logger.debug("Read EthIfController <%s>" % cfg.getName())

    def read_ethif_frame_owner_configs(self, element: ET.Element, ethif: EthIf):
        """Parse EthIf frame owner configurations."""
        for ctr_tag in self.find_ctr_tag_list(element, "EthIfFrameOwnerConfig"):
            cfg = EthIfFrameOwnerConfig(ethif, ctr_tag.attrib["name"])
            cfg.setEthIfFrameType(self.read_value(ctr_tag, "EthIfFrameType"))
            cfg.setEthIfOwner(self.read_value(ctr_tag, "EthIfOwner"))
            ethif.addEthIfFrameOwnerConfig(cfg)
            self.logger.debug("Read EthIfFrameOwnerConfig <%s>" % cfg.getName())

    def read_ethif_phys_controllers(self, element: ET.Element, ethif: EthIf):
        """
        Parse EthIf physical controller configurations.

        Implements: SWR_ETHIF_00004
        """
        for ctr_tag in self.find_ctr_tag_list(element, "EthIfPhysController"):
            cfg = EthIfPhysController(ethif, ctr_tag.attrib["name"])
            cfg.setEthIfPhysControllerIdx(self.read_value(ctr_tag, "EthIfPhysControllerIdx"))
            cfg.setEthIfEthCtrlRef(self.read_ref_value(ctr_tag, "EthIfEthCtrlRef"))
            cfg.setEthIfWEthCtrlRef(self.read_optional_ref_value(ctr_tag, "EthIfWEthCtrlRef"))
            ethif.addEthIfPhysController(cfg)
            self.logger.debug("Read EthIfPhysController <%s>" % cfg.getName())

    def read_ethif_switches(self, element: ET.Element, ethif: EthIf):
        """
        Parse EthIf switch configurations.

        Implements: SWR_ETHIF_00005
        """
        for ctr_tag in self.find_ctr_tag_list(element, "EthIfSwitch"):
            cfg = EthIfSwitch(ethif, ctr_tag.attrib["name"])
            cfg.setEthIfSwitchIdx(self.read_value(ctr_tag, "EthIfSwitchIdx"))
            cfg.setEthIfSwitchRef(self.read_ref_value(ctr_tag, "EthIfSwitchRef"))
            ethif.addEthIfSwitch(cfg)
            self.logger.debug("Read EthIfSwitch <%s>" % cfg.getName())

    def read_ethif_switch_port_groups(self, element: ET.Element, ethif: EthIf):
        """Parse EthIf switch port group configurations."""
        for ctr_tag in self.find_ctr_tag_list(element, "EthIfSwitchPortGroup"):
            cfg = EthIfSwitchPortGroup(ethif, ctr_tag.attrib["name"])
            cfg.setEthIfSwitchPortGroupIdx(self.read_value(ctr_tag, "EthIfSwitchPortGroupIdx"))
            cfg.setEthIfPortRef(self.read_ref_value(ctr_tag, "EthIfPortRef"))
            ethif.addEthIfSwitchPortGroup(cfg)
            self.logger.debug("Read EthIfSwitchPortGroup <%s>" % cfg.getName())

    def read_ethif_transceivers(self, element: ET.Element, ethif: EthIf):
        """
        Parse EthIf transceiver configurations.

        Implements: SWR_ETHIF_00006
        """
        for ctr_tag in self.find_ctr_tag_list(element, "EthIfTransceiver"):
            cfg = EthIfTransceiver(ethif, ctr_tag.attrib["name"])
            cfg.setEthIfTransceiverIdx(self.read_value(ctr_tag, "EthIfTransceiverIdx"))
            cfg.setEthIfEthTrcvRef(self.read_ref_value(ctr_tag, "EthIfEthTrcvRef"))
            cfg.setEthIfWEthTrcvRef(self.read_optional_ref_value(ctr_tag, "EthIfWEthTrcvRef"))
            ethif.addEthIfTransceiver(cfg)
            self.logger.debug("Read EthIfTransceiver <%s>" % cfg.getName())

    def read_ethif_rx_indication_configs(self, element: ET.Element, ethif: EthIf):
        """
        Parse EthIf RX indication configurations.

        Implements: SWR_ETHIF_00007
        """
        for ctr_tag in self.find_ctr_tag_list(element, "EthIfRxIndicationConfig"):
            cfg = EthIfRxIndicationConfig(ethif, ctr_tag.attrib["name"])
            ethif.addEthIfRxIndicationConfig(cfg)
            self.logger.debug("Read EthIfRxIndicationConfig <%s>" % cfg.getName())

    def read_ethif_tx_confirmation_configs(self, element: ET.Element, ethif: EthIf):
        """Parse EthIf TX confirmation configurations."""
        for ctr_tag in self.find_ctr_tag_list(element, "EthIfTxConfirmationConfig"):
            cfg = EthIfTxConfirmationConfig(ethif, ctr_tag.attrib["name"])
            ethif.addEthIfTxConfirmationConfig(cfg)
            self.logger.debug("Read EthIfTxConfirmationConfig <%s>" % cfg.getName())

    def read_ethif_eth_controller_types(self, element: ET.Element, ethif: EthIf):
        """Parse EthIf EthControllerType configurations."""
        for ctr_tag in self.find_ctr_tag_list(element, "EthIfEthControllerType"):
            cfg = EthIfEthControllerType(ethif, ctr_tag.attrib["name"])
            ethif.addEthIfEthControllerType(cfg)
            self.logger.debug("Read EthIfEthControllerType <%s>" % cfg.getName())

    def read_ethif_eth_trcv_types(self, element: ET.Element, ethif: EthIf):
        """Parse EthIf EthTrcvType configurations."""
        for ctr_tag in self.find_ctr_tag_list(element, "EthIfEthTrcvType"):
            cfg = EthIfEthTrcvType(ethif, ctr_tag.attrib["name"])
            ethif.addEthIfEthTrcvType(cfg)
            self.logger.debug("Read EthIfEthTrcvType <%s>" % cfg.getName())

    def read_ethif_eth_swt_types(self, element: ET.Element, ethif: EthIf):
        """Parse EthIf EthSwtType configurations."""
        for ctr_tag in self.find_ctr_tag_list(element, "EthIfEthSwtType"):
            cfg = EthIfEthSwtType(ethif, ctr_tag.attrib["name"])
            ethif.addEthIfEthSwtType(cfg)
            self.logger.debug("Read EthIfEthSwtType <%s>" % cfg.getName())
