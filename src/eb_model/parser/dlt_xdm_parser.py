"""
Dlt XDM Parser Module - Extracts AUTOSAR Dlt configuration from EB Tresos XDM files.

Implements:
    - SWR_DLT_00001: Dlt module parsing
    - SWR_DLT_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.dlt_xdm import Dlt, DltGeneral
from ..parser.eb_parser import AbstractEbModelParser


class DltXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR Dlt module configuration from EB Tresos XDM files.

    Implements: SWR_DLT_00001 (Dlt Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the Dlt XDM parser."""
        super().__init__()

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse Dlt module configuration from XDM element.

        Implements: SWR_DLT_00001
        """
        if self.get_component_name(element) != "Dlt":
            raise ValueError("Invalid <%s> xdm file" % "Dlt")

        dlt = doc.getDlt()
        self.read_version(element, dlt)

        self.logger.info("Parse Dlt ARVersion:<%s> SwVersion:<%s>" %
                        (dlt.getArVersion().getVersion(), dlt.getSwVersion().getVersion()))

        self.read_dlt_general(element, dlt)

    def read_dlt_general(self, element: ET.Element, dlt: Dlt):
        """
        Parse DltGeneral container from XDM.

        Implements: SWR_DLT_00002 (General configuration parsing)
        """
        ctr_tag = self.find_ctr_tag(element, "DltGeneral")
        if ctr_tag is not None:
            general = DltGeneral(dlt, ctr_tag.attrib["name"])
            general.setDltDevErrorDetect(self.read_value(ctr_tag, "DltDevErrorDetect"))
            general.setDltEnabled(self.read_value(ctr_tag, "DltEnabled"))
            dlt.setDltGeneral(general)
            self.logger.debug("Read DltGeneral")