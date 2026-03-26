"""
LinIf XDM Parser Module - Extracts AUTOSAR LinIf configuration from EB Tresos XDM files.

Implements:
    - SWR_LINIF_00001: LinIf module parsing
    - SWR_LINIF_00002: Channel configuration parsing
    - SWR_LINIF_00003: Frame configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.linif_xdm import LinIf, LinIfGeneral, LinIfChannel, LinIfFrame
from ..parser.eb_parser import AbstractEbModelParser


class LinIfXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR LinIf (LIN Interface) module configuration.

    Extracts LinIf configuration including channels and frames.

    Implements: SWR_LINIF_00001 (LinIf Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the LinIf XDM parser."""
        super().__init__()
        self.linif = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse LinIf module configuration from XDM element.

        Implements: SWR_LINIF_00001
        """
        if self.get_component_name(element) != "LinIf":
            raise ValueError("Invalid <%s> xdm file" % "LinIf")

        linif = doc.getLinIf()

        self.read_version(element, linif)

        self.logger.info("Parse LinIf ARVersion:<%s> SwVersion:<%s>" % (linif.getArVersion().getVersion(), linif.getSwVersion().getVersion()))

        self.linif = linif

        self.read_linif_general(element, linif)
        self.read_linif_global_config(element, linif)

    def read_linif_general(self, element: ET.Element, linif: LinIf):
        ctr_tag = self.find_ctr_tag(element, "LinIfGeneral")
        if ctr_tag is not None:
            general = LinIfGeneral(linif, ctr_tag.attrib["name"])
            general.setLinIfDevErrorDetect(self.read_value(ctr_tag, "LinIfDevErrorDetect"))
            general.setLinIfMaxChannels(self.read_optional_value(ctr_tag, "LinIfMaxChannels"))
            general.setLinIfTpSupported(self.read_optional_value(ctr_tag, "LinIfTpSupported"))
            linif.setLinIfGeneral(general)
            self.logger.debug("Read LinIfGeneral")

    def read_linif_global_config(self, element: ET.Element, linif: LinIf):
        config_tag = self.find_ctr_tag(element, "LinIfGlobalConfig")
        if config_tag is not None:
            self.read_linif_channels(config_tag, linif)
            self.read_linif_frames(config_tag, linif)

    def read_linif_channels(self, element: ET.Element, linif: LinIf):
        for ctr_tag in self.find_ctr_tag_list(element, "LinIfChannel"):
            channel = LinIfChannel(linif, ctr_tag.attrib["name"])
            channel.setLinIfChannelId(self.read_value(ctr_tag, "LinIfChannelId"))
            channel.setLinIfChannelRef(self.read_ref_value(ctr_tag, "LinIfChannelRef"))
            channel.setLinIfComMNetworkHandleRef(self.read_optional_ref_value(ctr_tag, "LinIfComMNetworkHandleRef"))
            linif.addLinIfChannel(channel)
            self.logger.debug("Read LinIfChannel <%s>" % channel.getName())

    def read_linif_frames(self, element: ET.Element, linif: LinIf):
        for ctr_tag in self.find_ctr_tag_list(element, "LinIfFrame"):
            frame = LinIfFrame(linif, ctr_tag.attrib["name"])
            frame.setLinIfFrameId(self.read_value(ctr_tag, "LinIfFrameId"))
            frame.setLinIfFrameType(self.read_optional_value(ctr_tag, "LinIfFrameType"))
            frame.setLinIfChecksumType(self.read_optional_value(ctr_tag, "LinIfChecksumType"))
            frame.setLinIfLength(self.read_optional_value(ctr_tag, "LinIfLength"))
            linif.addLinIfFrame(frame)
            self.logger.debug("Read LinIfFrame <%s>" % frame.getName())
