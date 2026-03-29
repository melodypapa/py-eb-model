"""
FiM XDM Parser Module - Extracts AUTOSAR FiM configuration from EB Tresos XDM files.

Implements:
    - SWR_FIM_00001: FiM module parsing
    - SWR_FIM_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.core.eb_doc import EBModel
from ..models.diag_stack.fim_xdm import FiM, FiMGeneral
from ..parser.eb_parser import AbstractEbModelParser


class FiMXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR FiM module configuration from EB Tresos XDM files.

    Implements: SWR_FIM_00001 (FiM Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the FiM XDM parser."""
        super().__init__()

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse FiM module configuration from XDM element.

        Implements: SWR_FIM_00001
        """
        if self.get_component_name(element) != "FiM":
            raise ValueError("Invalid <%s> xdm file" % "FiM")

        fim = doc.getFiM()
        self.read_version(element, fim)

        self.logger.info("Parse FiM ARVersion:<%s> SwVersion:<%s>" %
                        (fim.getArVersion().getVersion(), fim.getSwVersion().getVersion()))

        self.read_fim_general(element, fim)

    def read_fim_general(self, element: ET.Element, fim: FiM):
        """
        Parse FiMGeneral container from XDM.

        Implements: SWR_FIM_00002 (General configuration parsing)
        """
        ctr_tag = self.find_ctr_tag(element, "FiMGeneral")
        if ctr_tag is not None:
            general = FiMGeneral(fim, ctr_tag.attrib["name"])
            general.setFimDevErrorDetect(self.read_value(ctr_tag, "FimDevErrorDetect"))
            general.setFimEnabled(self.read_value(ctr_tag, "FimEnabled"))
            fim.setFimGeneral(general)
            self.logger.debug("Read FiMGeneral")