"""
BswM XDM Parser Module - Extracts AUTOSAR BswM configuration from EB Tresos XDM files.

Implements:
    - SWR_BSWM_00001: BswM module parsing
    - SWR_BSWM_00002: Mode declaration parsing
    - SWR_BSWM_00003: Mode condition parsing
"""
import xml.etree.ElementTree as ET
from ..models.core.eb_doc import EBModel
from ..models.core.bswm_xdm import BswM, BswMGeneral, BswMModeDeclaration, BswMModeCondition
from ..parser.eb_parser import AbstractEbModelParser


class BswMXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR BswM (Basic Software Mode Manager) module configuration.

    Extracts BswM configuration including mode declarations and conditions.

    Implements: SWR_BSWM_00001 (BswM Module Parser)
    """

    def __init__(self):
        """Initialize the BswM XDM parser."""
        super().__init__()

        self.bswm = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse BswM module configuration from XDM element.

        Implements: SWR_BSWM_00001
        """
        if self.get_component_name(element) != "BswM":
            raise ValueError("Invalid <%s> xdm file" % "BswM")

        bswm = doc.getBswM()

        self.read_version(element, bswm)

        self.logger.info("Parse BswM ARVersion:<%s> SwVersion:<%s>" % (bswm.getArVersion().getVersion(), bswm.getSwVersion().getVersion()))

        self.bswm = bswm

        self.read_bswm_general(element, bswm)
        self.read_bswm_mode_declarations(element, bswm)

    def read_bswm_general(self, element: ET.Element, bswm: BswM):
        ctr_tag = self.find_ctr_tag(element, "BswMGeneral")
        if ctr_tag is not None:
            general = BswMGeneral(bswm, ctr_tag.attrib["name"])
            general.setBswMDevErrorDetect(self.read_value(ctr_tag, "BswMDevErrorDetect"))
            bswm.setBswMGeneral(general)
            self.logger.debug("Read BswMGeneral")

    def read_bswm_mode_declarations(self, element: ET.Element, bswm: BswM):
        for ctr_tag in self.find_ctr_tag_list(element, "BswMModeDeclaration"):
            mode_declaration = BswMModeDeclaration(bswm, ctr_tag.attrib["name"])
            mode_declaration.setBswMAvailableForScheduler(self.read_value(ctr_tag, "BswMAvailableForScheduler"))
            mode_declaration.setBswMModeParentRef(self.read_optional_ref_value(ctr_tag, "BswMModeParentRef"))
            mode_declaration.setBswMModeType(self.read_value(ctr_tag, "BswMModeType"))
            self.read_bswm_mode_conditions(ctr_tag, mode_declaration)
            bswm.addBswMModeDeclaration(mode_declaration)
            self.logger.debug("Read BswMModeDeclaration <%s>" % mode_declaration.getName())

    def read_bswm_mode_conditions(self, element: ET.Element, mode_declaration: BswMModeDeclaration):
        for ctr_tag in self.find_ctr_tag_list(element, "BswMModeCondition"):
            mode_condition = BswMModeCondition(mode_declaration, ctr_tag.attrib["name"])
            mode_condition.setBswMModeConditionSourceRef(self.read_ref_value(ctr_tag, "BswMModeConditionSourceRef"))
            mode_declaration.addBswMModeCondition(mode_condition)
