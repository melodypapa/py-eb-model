"""
CryIf XDM Parser Module - Extracts AUTOSAR CryIf configuration from EB Tresos XDM files.

Implements:
    - SWR_CRYIF_00001: CryIf module parsing
    - SWR_CRYIF_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.core.eb_doc import EBModel
from ..models.crypto_stack.cryif_xdm import CryIf, CryIfGeneral
from ..parser.eb_parser import AbstractEbModelParser


class CryIfXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR CryIf module configuration from EB Tresos XDM files.

    Implements: SWR_CRYIF_00001 (CryIf Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the CryIf XDM parser."""
        super().__init__()

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse CryIf module configuration from XDM element.

        Implements: SWR_CRYIF_00001
        """
        if self.get_component_name(element) != "CryIf":
            raise ValueError("Invalid <%s> xdm file" % "CryIf")

        cryif = doc.getCryIf()
        self.read_version(element, cryif)

        self.logger.info("Parse CryIf ARVersion:<%s> SwVersion:<%s>" %
                        (cryif.getArVersion().getVersion(), cryif.getSwVersion().getVersion()))

        self.read_cryif_general(element, cryif)

    def read_cryif_general(self, element: ET.Element, cryif: CryIf):
        """
        Parse CryIfGeneral container from XDM.

        Implements: SWR_CRYIF_00002 (General configuration parsing)
        """
        ctr_tag = self.find_ctr_tag(element, "CryIfGeneral")
        if ctr_tag is not None:
            general = CryIfGeneral(cryif, ctr_tag.attrib["name"])
            general.setCryIfDevErrorDetect(self.read_value(ctr_tag, "CryIfDevErrorDetect"))
            general.setCryIfEnabled(self.read_value(ctr_tag, "CryIfEnabled"))
            cryif.setCryIfGeneral(general)
            self.logger.debug("Read CryIfGeneral")