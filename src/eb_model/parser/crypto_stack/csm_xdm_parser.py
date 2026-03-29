"""
Csm XDM Parser Module - Extracts AUTOSAR Csm configuration from EB Tresos XDM files.

Implements:
    - SWR_CSM_00001: Csm module parsing
    - SWR_CSM_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET
from ...models.core.eb_doc import EBModel
from ...models.crypto_stack.csm_xdm import Csm, CsmGeneral
from ..core.eb_parser import AbstractEbModelParser


class CsmXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR Csm module configuration from EB Tresos XDM files.

    Implements: SWR_CSM_00001 (Csm Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the Csm XDM parser."""
        super().__init__()

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse Csm module configuration from XDM element.

        Implements: SWR_CSM_00001
        """
        if self.get_component_name(element) != "Csm":
            raise ValueError("Invalid <%s> xdm file" % "Csm")

        csm = doc.getCsm()
        self.read_version(element, csm)

        self.logger.info("Parse Csm ARVersion:<%s> SwVersion:<%s>" %
                        (csm.getArVersion().getVersion(), csm.getSwVersion().getVersion()))

        self.read_csm_general(element, csm)

    def read_csm_general(self, element: ET.Element, csm: Csm):
        """
        Parse CsmGeneral container from XDM.

        Implements: SWR_CSM_00002 (General configuration parsing)
        """
        ctr_tag = self.find_ctr_tag(element, "CsmGeneral")
        if ctr_tag is not None:
            general = CsmGeneral(csm, ctr_tag.attrib["name"])
            general.setCsmDevErrorDetect(self.read_value(ctr_tag, "CsmDevErrorDetect"))
            general.setCsmEnabled(self.read_value(ctr_tag, "CsmEnabled"))
            csm.setCsmGeneral(general)
            self.logger.debug("Read CsmGeneral")