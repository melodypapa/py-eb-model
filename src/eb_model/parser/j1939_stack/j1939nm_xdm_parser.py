"""
J1939Nm XDM Parser Module - Extracts AUTOSAR J1939Nm configuration from EB Tresos XDM files.

Implements:
    - SWR_J1939NM_00001: J1939Nm module parsing
    - SWR_J1939NM_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET
from ...models.core.eb_doc import EBModel
from ...models.j1939_stack.j1939nm_xdm import J1939Nm, J1939NmGeneral
from ..core.eb_parser import AbstractEbModelParser


class J1939NmXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR J1939Nm module configuration from EB Tresos XDM files.

    Implements: SWR_J1939NM_00001 (J1939Nm Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the J1939Nm XDM parser."""
        super().__init__()

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse J1939Nm module configuration from XDM element.

        Implements: SWR_J1939NM_00001
        """
        if self.get_component_name(element) != "J1939Nm":
            raise ValueError("Invalid <%s> xdm file" % "J1939Nm")

        j1939nm = doc.getJ1939Nm()
        self.read_version(element, j1939nm)

        self.logger.info("Parse J1939Nm ARVersion:<%s> SwVersion:<%s>" %
                        (j1939nm.getArVersion().getVersion(), j1939nm.getSwVersion().getVersion()))

        self.read_j1939nm_general(element, j1939nm)

    def read_j1939nm_general(self, element: ET.Element, j1939nm: J1939Nm):
        """
        Parse J1939NmGeneral container from XDM.

        Implements: SWR_J1939NM_00002 (General configuration parsing)
        """
        ctr_tag = self.find_ctr_tag(element, "J1939NmGeneral")
        if ctr_tag is not None:
            general = J1939NmGeneral(j1939nm, ctr_tag.attrib["name"])
            general.setJ1939NmDevErrorDetect(self.read_value(ctr_tag, "J1939NmDevErrorDetect"))
            general.setJ1939NmEnabled(self.read_value(ctr_tag, "J1939NmEnabled"))
            j1939nm.setJ1939NmGeneral(general)
            self.logger.debug("Read J1939NmGeneral")