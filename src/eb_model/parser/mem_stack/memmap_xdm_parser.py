"""
MemMap XDM Parser Module - Extracts AUTOSAR MemMap configuration from EB Tresos XDM files.

Implements:
    - SWR_MEMMAP_00001: MemMap module parsing
    - SWR_MEMMAP_00002: Common configuration parsing
"""
import xml.etree.ElementTree as ET

from eb_model.models.core.eb_doc import EBModel
from eb_model.models.mem_stack.memmap_xdm import MemMap, MemMapCommon
from eb_model.parser.core.eb_parser import AbstractEbModelParser


class MemMapXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR MemMap (Memory Mapping) module configuration.

    Extracts MemMap configuration including memory section definitions
    and segment mappings.

    Implements: SWR_MEMMAP_00001 (MemMap Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the MemMap XDM parser."""
        super().__init__()
        self.memmap = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse MemMap module configuration from XDM element.

        Implements: SWR_MEMMAP_00001
        """
        if self.get_component_name(element) != "MemMap":
            raise ValueError("Invalid <%s> xdm file" % "MemMap")

        memmap = doc.getMemMap()
        self.read_version(element, memmap)

        self.logger.info("Parse MemMap ARVersion:<%s> SwVersion:<%s>" %
                        (memmap.getArVersion().getVersion(), memmap.getSwVersion().getVersion()))

        self.memmap = memmap
        self.read_memmap_common(element, memmap)

    def read_memmap_common(self, element: ET.Element, memmap: MemMap):
        """
        Parse MemMapCommon configuration from XDM.

        Implements: SWR_MEMMAP_00002
        """
        ctr_tag = self.find_ctr_tag(element, "MemMapCommon")
        if ctr_tag is not None:
            common = MemMapCommon(memmap, ctr_tag.attrib["name"])
            common.setMemMapDevErrorDetect(self.read_value(ctr_tag, "MemMapDevErrorDetect"))
            common.setMemMapApi(self.read_value(ctr_tag, "MemMapApi"))
            common.setMemMapInitStatus(self.read_optional_value(ctr_tag, "MemMapInitStatus"))
            memmap.setMemMapCommon(common)
            self.logger.debug("Read MemMapCommon")
