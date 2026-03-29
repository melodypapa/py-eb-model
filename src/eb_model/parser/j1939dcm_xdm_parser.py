"""
J1939Dcm XDM Parser Module - Extracts AUTOSAR J1939Dcm configuration from EB Tresos XDM files.

Implements:
    - SWR_J1939DCM_00001: J1939Dcm module parsing
    - SWR_J1939DCM_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.j1939dcm_xdm import J1939Dcm, J1939DcmGeneral
from ..parser.eb_parser import AbstractEbModelParser


class J1939DcmXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR J1939Dcm module configuration from EB Tresos XDM files.

    Implements: SWR_J1939DCM_00001 (J1939Dcm Module Parser)
    """

    def __init__(self, ) -> None:
        """Initialize the J1939Dcm XDM parser."""
        super().__init__()

        self.j1939dcm = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse J1939Dcm module configuration from XDM element.

        Implements: SWR_J1939DCM_00001
        """
        if self.get_component_name(element) != "J1939Dcm":
            raise ValueError("Invalid <%s> xdm file" % "J1939Dcm")

        j1939dcm = doc.getJ1939Dcm()
        self.read_version(element, j1939dcm)

        self.logger.info("Parse J1939Dcm ARVersion:<%s> SwVersion:<%s>" %
                        (j1939dcm.getArVersion().getVersion(), j1939dcm.getSwVersion().getVersion()))

        self.j1939dcm = j1939dcm
        self.read_j1939dcm_general(element, j1939dcm)

        return j1939dcm

    def read_j1939dcm_general(self, element: ET.Element, j1939dcm: J1939Dcm):
        """
        Parse J1939DcmGeneral container from XDM.

        Implements: SWR_J1939DCM_00002 (General configuration parsing)
        """
        ctr_tag = self.find_ctr_tag(element, "J1939DcmGeneral")
        if ctr_tag is not None:
            general = J1939DcmGeneral(j1939dcm, ctr_tag.attrib["name"])
            general.setJ1939DcmDevErrorDetect(self.read_value(ctr_tag, "J1939DcmDevErrorDetect"))
            general.setJ1939DcmEnabled(self.read_value(ctr_tag, "J1939DcmEnabled"))
            j1939dcm.setJ1939DcmGeneral(general)
            self.logger.debug("Read J1939DcmGeneral")