"""
Dcm XDM Parser Module - Extracts AUTOSAR Dcm configuration from EB Tresos XDM files.

Implements:
    - SWR_DCM_00001: Dcm module parsing
    - SWR_DCM_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.dcm_xdm import Dcm, DcmGeneral
from ..parser.eb_parser import AbstractEbModelParser


class DcmXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR Dcm module configuration from EB Tresos XDM files.

    Implements: SWR_DCM_00001 (Dcm Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the Dcm XDM parser."""
        super().__init__()

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse Dcm module configuration from XDM element.

        Implements: SWR_DCM_00001
        """
        if self.get_component_name(element) != "Dcm":
            raise ValueError("Invalid <%s> xdm file" % "Dcm")

        dcm = doc.getDcm()
        self.read_version(element, dcm)

        self.logger.info("Parse Dcm ARVersion:<%s> SwVersion:<%s>" %
                        (dcm.getArVersion().getVersion(), dcm.getSwVersion().getVersion()))

        self.read_dcm_general(element, dcm)

    def read_dcm_general(self, element: ET.Element, dcm: Dcm):
        """
        Parse DcmGeneral container from XDM.

        Implements: SWR_DCM_00002 (General configuration parsing)
        """
        ctr_tag = self.find_ctr_tag(element, "DcmGeneral")
        if ctr_tag is not None:
            general = DcmGeneral(dcm, ctr_tag.attrib["name"])
            general.setDcmDevErrorDetect(self.read_value(ctr_tag, "DcmDevErrorDetect"))
            general.setDcmEnabled(self.read_value(ctr_tag, "DcmEnabled"))
            dcm.setDcmGeneral(general)
            self.logger.debug("Read DcmGeneral")