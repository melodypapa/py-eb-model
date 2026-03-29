"""
Crc XDM Parser Module - Extracts AUTOSAR Crc configuration from EB Tresos XDM files.

Implements:
    - SWR_CRC_00001: Crc module parsing
    - SWR_CRC_00002: Crc configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.core.eb_doc import EBModel
from ..models.mem_stack.crc_xdm import Crc, CrcConfig
from ..parser.eb_parser import AbstractEbModelParser


class CrcXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR Crc (Cyclic Redundancy Check) module configuration.

    Extracts Crc configuration including CRC parameters and settings.

    Implements: SWR_CRC_00001 (Crc Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the Crc XDM parser."""
        super().__init__()
        self.crc = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse Crc module configuration from XDM element.

        Implements: SWR_CRC_00001
        """
        if self.get_component_name(element) != "Crc":
            raise ValueError("Invalid <%s> xdm file" % "Crc")

        crc = doc.getCrc()

        self.read_version(element, crc)

        self.logger.info("Parse Crc ARVersion:<%s> SwVersion:<%s>" % (crc.getArVersion().getVersion(), crc.getSwVersion().getVersion()))

        self.crc = crc

        self.read_crc_configs(element, crc)

    def read_crc_configs(self, element: ET.Element, crc: Crc):
        """
        Parse Crc configuration.

        Implements: SWR_CRC_00002 (Crc configuration parsing)
        """
        for ctr_tag in self.find_ctr_tag_list(element, "CrcConfig"):
            cfg = CrcConfig(crc, ctr_tag.attrib["name"])
            cfg.setCrcId(self.read_value(ctr_tag, "CrcId"))
            cfg.setCrcCRCType(self.read_value(ctr_tag, "CrcCRCType"))
            crc.addCrcConfig(cfg)
            self.logger.debug("Read CrcConfig <%s>" % cfg.getName())
