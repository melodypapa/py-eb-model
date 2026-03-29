"""
J1939Rm XDM Parser Module - Extracts AUTOSAR J1939Rm configuration from EB Tresos XDM files.

Implements:
    - SWR_J1939RM_00001: J1939Rm module parsing
    - SWR_J1939RM_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET
from eb_model.models.core.eb_doc import EBModel
from eb_model.models.j1939_stack.j1939rm_xdm import J1939Rm, J1939RmGeneral
from eb_model.parser.core.eb_parser import AbstractEbModelParser


class J1939RmXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR J1939Rm module configuration from EB Tresos XDM files.

    Implements: SWR_J1939RM_00001 (J1939Rm Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the J1939Rm XDM parser."""
        super().__init__()

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse J1939Rm module configuration from XDM element.

        Implements: SWR_J1939RM_00001
        """
        if self.get_component_name(element) != "J1939Rm":
            raise ValueError("Invalid <%s> xdm file" % "J1939Rm")

        j1939rm = doc.getJ1939Rm()
        self.read_version(element, j1939rm)

        self.logger.info("Parse J1939Rm ARVersion:<%s> SwVersion:<%s>" %
                        (j1939rm.getArVersion().getVersion(), j1939rm.getSwVersion().getVersion()))

        self.read_j1939rm_general(element, j1939rm)

    def read_j1939rm_general(self, element: ET.Element, j1939rm: J1939Rm):
        """
        Parse J1939RmGeneral container from XDM.

        Implements: SWR_J1939RM_00002 (General configuration parsing)
        """
        ctr_tag = self.find_ctr_tag(element, "J1939RmGeneral")
        if ctr_tag is not None:
            general = J1939RmGeneral(j1939rm, ctr_tag.attrib["name"])
            general.setJ1939RmDevErrorDetect(self.read_value(ctr_tag, "J1939RmDevErrorDetect"))
            general.setJ1939RmEnabled(self.read_value(ctr_tag, "J1939RmEnabled"))
            j1939rm.setJ1939RmGeneral(general)
            self.logger.debug("Read J1939RmGeneral")
