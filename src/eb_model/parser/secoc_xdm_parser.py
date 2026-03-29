"""
SecOC XDM Parser Module - Extracts AUTOSAR SecOC configuration from EB Tresos XDM files.

Implements:
    - SWR_SECOC_00001: SecOC module parsing
    - SWR_SECOC_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.secoc_xdm import SecOC, SecOCGeneral
from ..parser.eb_parser import AbstractEbModelParser


class SecOCXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR SecOC module configuration from EB Tresos XDM files.

    Implements: SWR_SECOC_00001 (SecOC Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the SecOC XDM parser."""
        super().__init__()

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse SecOC module configuration from XDM element.

        Implements: SWR_SECOC_00001
        """
        if self.get_component_name(element) != "SecOC":
            raise ValueError("Invalid <%s> xdm file" % "SecOC")

        secoc = doc.getSecOC()
        self.read_version(element, secoc)

        self.logger.info("Parse SecOC ARVersion:<%s> SwVersion:<%s>" %
                        (secoc.getArVersion().getVersion(), secoc.getSwVersion().getVersion()))

        self.read_secoc_general(element, secoc)

    def read_secoc_general(self, element: ET.Element, secoc: SecOC):
        """
        Parse SecOCGeneral container from XDM.

        Implements: SWR_SECOC_00002 (General configuration parsing)
        """
        ctr_tag = self.find_ctr_tag(element, "SecOCGeneral")
        if ctr_tag is not None:
            general = SecOCGeneral(secoc, ctr_tag.attrib["name"])
            general.setSecocDevErrorDetect(self.read_value(ctr_tag, "SecOCDevErrorDetect"))
            general.setSecocEnabled(self.read_value(ctr_tag, "SecOCEnabled"))
            secoc.setSecocGeneral(general)
            self.logger.debug("Read SecOCGeneral")