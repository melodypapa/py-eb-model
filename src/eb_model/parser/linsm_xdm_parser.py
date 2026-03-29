"""
LinSM XDM Parser Module - Extracts AUTOSAR LinSM configuration from EB Tresos XDM files.

Implements:
    - SWR_LINSM_00001: LinSM module parsing
    - SWR_LINSM_00002: Channel configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.core.eb_doc import EBModel
from ..models.lin_stack.linsm_xdm import LinSM, LinSMGeneral, LinSMChannel
from ..parser.eb_parser import AbstractEbModelParser


class LinSMXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR LinSM (LIN State Manager) module configuration.

    Extracts LinSM configuration including channels.

    Implements: SWR_LINSM_00001 (LinSM Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the LinSM XDM parser."""
        super().__init__()
        self.linsm = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse LinSM module configuration from XDM element.

        Implements: SWR_LINSM_00001
        """
        if self.get_component_name(element) != "LinSM":
            raise ValueError("Invalid <%s> xdm file" % "LinSM")

        linsm = doc.getLinSM()

        self.read_version(element, linsm)

        self.logger.info("Parse LinSM ARVersion:<%s> SwVersion:<%s>" % (linsm.getArVersion().getVersion(), linsm.getSwVersion().getVersion()))

        self.linsm = linsm

        self.read_linsm_general(element, linsm)
        self.read_linsm_config_set(element, linsm)

    def read_linsm_general(self, element: ET.Element, linsm: LinSM):
        ctr_tag = self.find_ctr_tag(element, "LinSMGeneral")
        if ctr_tag is not None:
            general = LinSMGeneral(linsm, ctr_tag.attrib["name"])
            general.setLinSMDevErrorDetect(self.read_value(ctr_tag, "LinSMDevErrorDetect"))
            general.setLinSMMainProcessingPeriod(self.read_optional_value(ctr_tag, "LinSMMainProcessingPeriod"))
            linsm.setLinSMGeneral(general)
            self.logger.debug("Read LinSMGeneral")

    def read_linsm_config_set(self, element: ET.Element, linsm: LinSM):
        config_tag = self.find_ctr_tag(element, "LinSMConfigSet")
        if config_tag is not None:
            self.read_linsm_channels(config_tag, linsm)

    def read_linsm_channels(self, element: ET.Element, linsm: LinSM):
        for ctr_tag in self.find_ctr_tag_list(element, "LinSMChannel"):
            channel = LinSMChannel(linsm, ctr_tag.attrib["name"])
            channel.setLinSMConfirmationTimeout(self.read_optional_value(ctr_tag, "LinSMConfirmationTimeout"))
            channel.setLinSMSleepSupport(self.read_optional_value(ctr_tag, "LinSMSleepSupport"))
            channel.setLinSMComMNetworkHandleRef(self.read_ref_value(ctr_tag, "LinSMComMNetworkHandleRef"))
            channel.setLinSMNodeType(self.read_optional_value(ctr_tag, "LinSMNodeType"))
            linsm.addLinSMChannel(channel)
            self.logger.debug("Read LinSMChannel <%s>" % channel.getName())
