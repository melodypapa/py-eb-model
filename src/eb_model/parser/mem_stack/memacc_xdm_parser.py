"""
MemAcc XDM Parser Module - Extracts AUTOSAR MemAcc configuration from EB Tresos XDM files.

Implements:
    - SWR_MEMACC_00001: MemAcc module parsing
    - SWR_MEMACC_00002: Common configuration parsing
"""
import xml.etree.ElementTree as ET

from ...models.core.eb_doc import EBModel
from ...models.mem_stack.memacc_xdm import MemAcc, MemAccCommon
from ..core.eb_parser import AbstractEbModelParser


class MemAccXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR MemAcc (Memory Access) module configuration.

    Extracts MemAcc configuration including protection zones,
    access permissions, and address validation.

    Implements: SWR_MEMACC_00001 (MemAcc Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the MemAcc XDM parser."""
        super().__init__()
        self.memacc = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse MemAcc module configuration from XDM element.

        Implements: SWR_MEMACC_00001
        """
        if self.get_component_name(element) != "MemAcc":
            raise ValueError("Invalid <%s> xdm file" % "MemAcc")

        memacc = doc.getMemAcc()
        self.read_version(element, memacc)

        self.logger.info("Parse MemAcc ARVersion:<%s> SwVersion:<%s>" %
                        (memacc.getArVersion().getVersion(), memacc.getSwVersion().getVersion()))

        self.memacc = memacc
        self.read_memacc_common(element, memacc)

    def read_memacc_common(self, element: ET.Element, memacc: MemAcc):
        """
        Parse MemAccCommon configuration from XDM.

        Implements: SWR_MEMACC_00002
        """
        ctr_tag = self.find_ctr_tag(element, "MemAccCommon")
        if ctr_tag is not None:
            common = MemAccCommon(memacc, ctr_tag.attrib["name"])
            common.setMemAccDevErrorDetect(self.read_value(ctr_tag, "MemAccDevErrorDetect"))
            common.setMemAccProtectionApi(self.read_value(ctr_tag, "MemAccProtectionApi"))
            common.setMemAccVirtualProtection(self.read_optional_value(ctr_tag, "MemAccVirtualProtection"))
            memacc.setMemAccCommon(common)
            self.logger.debug("Read MemAccCommon")