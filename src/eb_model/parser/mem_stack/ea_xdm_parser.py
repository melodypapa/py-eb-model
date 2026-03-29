"""
Ea XDM Parser Module - Extracts AUTOSAR Ea configuration from EB Tresos XDM files.

Implements:
    - SWR_EA_00001: Ea module parsing
    - SWR_EA_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET

from ...models.core.eb_doc import EBModel
from ...models.mem_stack.ea_xdm import Ea, EaGeneral
from ..core.eb_parser import AbstractEbModelParser


class EaXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR Ea (EEPROM Abstraction) module configuration.

    Extracts Ea configuration including page size, address alignment,
    and device-specific parameters.

    Implements: SWR_EA_00001 (Ea Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the Ea XDM parser."""
        super().__init__()
        self.ea = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse Ea module configuration from XDM element.

        Implements: SWR_EA_00001
        """
        if self.get_component_name(element) != "Ea":
            raise ValueError("Invalid <%s> xdm file" % "Ea")

        ea = doc.getEa()
        self.read_version(element, ea)

        self.logger.info("Parse Ea ARVersion:<%s> SwVersion:<%s>" %
                        (ea.getArVersion().getVersion(), ea.getSwVersion().getVersion()))

        self.ea = ea
        self.read_ea_general(element, ea)

    def read_ea_general(self, element: ET.Element, ea: Ea):
        """
        Parse EaGeneral configuration from XDM.

        Implements: SWR_EA_00002
        """
        ctr_tag = self.find_ctr_tag(element, "EaGeneral")
        if ctr_tag is not None:
            general = EaGeneral(ea, ctr_tag.attrib["name"])
            general.setEaDevErrorDetect(self.read_value(ctr_tag, "EaDevErrorDetect"))
            general.setEaPageSize(self.read_value(ctr_tag, "EaPageSize"))
            general.setEaAddressAlignment(self.read_value(ctr_tag, "EaAddressAlignment"))
            general.setEaReadMode(self.read_optional_value(ctr_tag, "EaReadMode"))
            ea.setEaGeneral(general)
            self.logger.debug("Read EaGeneral")