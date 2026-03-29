"""
EthSM XDM Parser Module - Extracts AUTOSAR EthSM configuration from EB Tresos XDM files.

Implements:
    - SWR_ETHSM_00001: EthSM module parsing
    - SWR_ETHSM_00002: General configuration parsing
    - SWR_ETHSM_00003: Network configuration parsing
"""
import xml.etree.ElementTree as ET
from ...models.core.eb_doc import EBModel
from ...models.eth_stack.ethsm_xdm import (
    EthSM, EthSMGeneral, EthSMNetwork, EthSMDemEventParameterRefs
)
from ..core.eb_parser import AbstractEbModelParser


class EthSMXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR EthSM (Ethernet State Manager) module configuration.

    Extracts EthSM configuration including general parameters and network configurations.

    Implements: SWR_ETHSM_00001 (EthSM Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the EthSM XDM parser."""
        super().__init__()
        self.ethsm = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse EthSM module configuration from XDM element.

        Implements: SWR_ETHSM_00001
        """
        if self.get_component_name(element) != "EthSM":
            raise ValueError("Invalid <%s> xdm file" % "EthSM")

        ethsm = doc.getEthSM()

        self.read_version(element, ethsm)

        self.logger.info("Parse EthSM ARVersion:<%s> SwVersion:<%s>" % (ethsm.getArVersion().getVersion(), ethsm.getSwVersion().getVersion()))

        self.ethsm = ethsm

        self.read_ethsm_general(element, ethsm)
        self.read_ethsm_defensive_programming(element, ethsm)
        self.read_ethsm_networks(element, ethsm)

    def read_ethsm_general(self, element: ET.Element, ethsm: EthSM):
        """
        Parse EthSM general configuration.

        Implements: SWR_ETHSM_00002
        """
        ctr_tag = self.find_ctr_tag(element, "EthSMGeneral")
        if ctr_tag is not None:
            general = EthSMGeneral(ethsm, ctr_tag.attrib["name"])
            general.setEthSMDevErrorDetect(self.read_value(ctr_tag, "EthSMDevErrorDetect"))
            general.setEthSMDummyMode(self.read_value(ctr_tag, "EthSMDummyMode"))
            general.setEthSMMainFunctionPeriod(self.read_value(ctr_tag, "EthSMMainFunctionPeriod"))
            general.setEthSMVersionInfoApi(self.read_value(ctr_tag, "EthSMVersionInfoApi"))
            general.setEthSMSingleNetworkOptEnable(self.read_value(ctr_tag, "EthSMSingleNetworkOptEnable"))
            general.setEthSMMaxNetworks(self.read_value(ctr_tag, "EthSMMaxNetworks"))
            general.setEthSMMultiCoreSupport(self.read_optional_value(ctr_tag, "EthSMMultiCoreSupport"))
            general.setEthSMDevAuthSupport(self.read_optional_value(ctr_tag, "EthSMDevAuthSupport"))
            general.setEthSMRelocatablePbcfgEnable(self.read_optional_value(ctr_tag, "EthSMRelocatablePbcfgEnable"))
            ethsm.setEthSMGeneral(general)
            self.logger.debug("Read EthSMGeneral")

    def read_ethsm_defensive_programming(self, element: ET.Element, ethsm: EthSM):
        """Parse EthSM defensive programming configuration."""
        ctr_tag = self.find_ctr_tag(element, "EthSMDefensiveProgramming")
        if ctr_tag is not None:
            general = ethsm.getEthSMGeneral()
            if general is not None:
                general.setEthSMDefProgEnabled(self.read_value(ctr_tag, "EthSMDefProgEnabled"))
                general.setEthSMPrecondAssertEnabled(self.read_value(ctr_tag, "EthSMPrecondAssertEnabled"))
                general.setEthSMPostcondAssertEnabled(self.read_value(ctr_tag, "EthSMPostcondAssertEnabled"))
                general.setEthSMStaticAssertEnabled(self.read_value(ctr_tag, "EthSMStaticAssertEnabled"))
                general.setEthSMUnreachAssertEnabled(self.read_value(ctr_tag, "EthSMUnreachAssertEnabled"))
                general.setEthSMInvariantAssertEnabled(self.read_value(ctr_tag, "EthSMInvariantAssertEnabled"))
            self.logger.debug("Read EthSMDefensiveProgramming")

    def read_ethsm_networks(self, element: ET.Element, ethsm: EthSM):
        """
        Parse EthSM network configurations.

        Implements: SWR_ETHSM_00003
        """
        for ctr_tag in self.find_ctr_tag_list(element, "EthSMNetwork"):
            network = EthSMNetwork(ethsm, ctr_tag.attrib["name"])

            # Read references
            network.setEthSMEthIfControllerRef(self.read_ref_value(ctr_tag, "EthSMEthIfControllerRef"))
            network.setEthSMComMNetworkHandleRef(self.read_ref_value(ctr_tag, "EthSMComMNetworkHandleRef"))
            network.setEthSMDevAuthNoComNotificationEnable(self.read_optional_value(ctr_tag, "EthSMDevAuthNoComNotificationEnable"))

            # Read DemEventParameterRefs if present
            dem_ctr = self.find_ctr_tag(ctr_tag, "EthSMDemEventParameterRefs")
            if dem_ctr is not None:
                dem_refs = EthSMDemEventParameterRefs(network, dem_ctr.attrib["name"])
                dem_refs.setEthSMDemEventParameterRef(self.read_ref_value(dem_ctr, "ETHSM_E_LINK_DOWN"))
                network.setEthSMDemEventParameterRefs(dem_refs)

            ethsm.addEthSMNetwork(network)
            self.logger.debug("Read EthSMNetwork <%s>" % network.getName())
