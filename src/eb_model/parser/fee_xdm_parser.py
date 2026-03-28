"""
Fee XDM Parser Module - Extracts AUTOSAR Fee configuration from EB Tresos XDM files.

Implements:
    - SWR_FEE_00001: Fee module parsing
    - SWR_FEE_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET

from ..models.eb_doc import EBModel
from ..models.fee_xdm import Fee, FeeGeneral
from ..parser.eb_parser import AbstractEbModelParser


class FeeXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR Fee (Flash EEPROM Emulation) module configuration.

    Extracts Fee configuration including page size, sector definitions,
    and wear-leveling parameters.

    Implements: SWR_FEE_00001 (Fee Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the Fee XDM parser."""
        super().__init__()
        self.fee = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse Fee module configuration from XDM element.

        Implements: SWR_FEE_00001
        """
        if self.get_component_name(element) != "Fee":
            raise ValueError("Invalid <%s> xdm file" % "Fee")

        fee = doc.getFee()
        self.read_version(element, fee)

        self.logger.info("Parse Fee ARVersion:<%s> SwVersion:<%s>" %
                        (fee.getArVersion().getVersion(), fee.getSwVersion().getVersion()))

        self.fee = fee
        self.read_fee_general(element, fee)

    def read_fee_general(self, element: ET.Element, fee: Fee):
        """
        Parse FeeGeneral configuration from XDM.

        Implements: SWR_FEE_00002
        """
        ctr_tag = self.find_ctr_tag(element, "FeeGeneral")
        if ctr_tag is not None:
            general = FeeGeneral(fee, ctr_tag.attrib["name"])
            general.setFeeDevErrorDetect(self.read_value(ctr_tag, "FeeDevErrorDetect"))
            general.setFeePageSize(self.read_value(ctr_tag, "FeePageSize"))
            general.setFeeVirtualPageSize(self.read_value(ctr_tag, "FeeVirtualPageSize"))
            general.setFeeNumberOfSectors(self.read_optional_value(ctr_tag, "FeeNumberOfSectors"))
            fee.setFeeGeneral(general)
            self.logger.debug("Read FeeGeneral")