"""
J1939Tp XDM Parser Module - Extracts AUTOSAR J1939Tp configuration from EB Tresos XDM files.

Implements:
    - SWR_J1939TP_00001: J1939Tp module parsing
    - SWR_J1939TP_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.j1939tp_xdm import J1939Tp, J1939TpGeneral
from ..parser.eb_parser import AbstractEbModelParser


class J1939TpXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR J1939Tp module configuration from EB Tresos XDM files.

    Implements: SWR_J1939TP_00001 (J1939Tp Module Parser)
    """

    def __init__(self, ) -> None:
        """Initialize the J1939Tp XDM parser."""
        super().__init__()

        self.j1939tp = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse J1939Tp module configuration from XDM element.

        Implements: SWR_J1939TP_00001
        """
        if self.get_component_name(element) != "J1939Tp":
            raise ValueError("Invalid <%s> xdm file" % "J1939Tp")

        j1939tp = doc.getJ1939Tp()
        self.read_version(element, j1939tp)

        self.logger.info("Parse J1939Tp ARVersion:<%s> SwVersion:<%s>" %
                        (j1939tp.getArVersion().getVersion(), j1939tp.getSwVersion().getVersion()))

        self.j1939tp = j1939tp
        self.read_j1939tp_general(element, j1939tp)

        return j1939tp

    def read_j1939tp_general(self, element: ET.Element, j1939tp: J1939Tp):
        """
        Parse J1939TpGeneral container from XDM.

        Implements: SWR_J1939TP_00002 (General configuration parsing)
        """
        ctr_tag = self.find_ctr_tag(element, "J1939TpGeneral")
        if ctr_tag is not None:
            general = J1939TpGeneral(j1939tp, ctr_tag.attrib["name"])
            general.setJ1939TpDevErrorDetect(self.read_value(ctr_tag, "J1939TpDevErrorDetect"))
            general.setJ1939TpEnabled(self.read_value(ctr_tag, "J1939TpEnabled"))
            j1939tp.setJ1939TpGeneral(general)
            self.logger.debug("Read J1939TpGeneral")