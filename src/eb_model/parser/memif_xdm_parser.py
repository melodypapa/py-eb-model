"""
MemIf XDM Parser Module - Extracts AUTOSAR MemIf configuration from EB Tresos XDM files.

Implements:
    - SWR_MEMIF_00001: MemIf module parsing
    - SWR_MEMIF_00002: Init configuration parsing
"""
import xml.etree.ElementTree as ET

from ..models.core.eb_doc import EBModel
from ..models.mem_stack.memif_xdm import MemIf, MemIfInit
from ..parser.eb_parser import AbstractEbModelParser


class MemIfXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR MemIf (Memory Abstraction Interface) module configuration.

    Extracts MemIf configuration including initialization settings and
    device abstraction parameters.

    Implements: SWR_MEMIF_00001 (MemIf Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the MemIf XDM parser."""
        super().__init__()
        self.memif = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse MemIf module configuration from XDM element.

        Implements: SWR_MEMIF_00001
        """
        if self.get_component_name(element) != "MemIf":
            raise ValueError("Invalid <%s> xdm file" % "MemIf")

        memif = doc.getMemIf()
        self.read_version(element, memif)

        self.logger.info("Parse MemIf ARVersion:<%s> SwVersion:<%s>" %
                        (memif.getArVersion().getVersion(), memif.getSwVersion().getVersion()))

        self.memif = memif
        self.read_memif_init(element, memif)

    def read_memif_init(self, element: ET.Element, memif: MemIf):
        """
        Parse MemIfInit configuration from XDM.

        Implements: SWR_MEMIF_00002
        """
        ctr_tag = self.find_ctr_tag(element, "MemIfInit")
        if ctr_tag is not None:
            init = MemIfInit(memif, ctr_tag.attrib["name"])
            init.setMemIfDevErrorDetect(self.read_value(ctr_tag, "MemIfDevErrorDetect"))
            init.setMemIfIndex(self.read_value(ctr_tag, "MemIfIndex"))
            init.setMemIfJobPriority(self.read_value(ctr_tag, "MemIfJobPriority"))
            init.setMemIfMaxNumberJobs(self.read_optional_value(ctr_tag, "MemIfMaxNumberJobs"))
            memif.setMemIfInit(init)
            self.logger.debug("Read MemIfInit")