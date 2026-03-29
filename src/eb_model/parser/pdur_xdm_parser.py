"""
PduR XDM Parser Module - Extracts AUTOSAR PduR configuration from EB Tresos XDM files.

Implements:
    - SWR_PDUR_00001: PduR module parsing
    - SWR_PDUR_00002: PduR routing configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.core.eb_doc import EBModel
from ..models.com_stack.pdur_xdm import PduR, PduRRoutingTableEntry
from ..parser.eb_parser import AbstractEbModelParser


class PduRXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR PduR (PDU Router) module configuration.

    Extracts PduR routing configuration including routing table entries.

    Implements: SWR_PDUR_00001 (PduR Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the PduR XDM parser."""
        super().__init__()
        self.pdur = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse PduR module configuration from XDM element.

        Implements: SWR_PDUR_00001
        """
        if self.get_component_name(element) != "PduR":
            raise ValueError("Invalid <%s> xdm file" % "PduR")

        pdur = doc.getPduR()

        self.read_version(element, pdur)

        self.logger.info("Parse PduR ARVersion:<%s> SwVersion:<%s>" % (pdur.getArVersion().getVersion(), pdur.getSwVersion().getVersion()))

        self.pdur = pdur

        self.read_pdur_routing_cfgs(element, pdur)

    def read_pdur_routing_cfgs(self, element: ET.Element, pdur: PduR):
        """
        Parse PduR routing table configuration.

        Implements: SWR_PDUR_00002 (PduR routing configuration parsing)
        """
        for ctr_tag in self.find_ctr_tag_list(element, "PduRRoutingTable"):
            cfg = PduRRoutingTableEntry(pdur, ctr_tag.attrib["name"])
            cfg.setPduRRoutingTableEntryID(self.read_value(ctr_tag, "PduRRoutingTableEntryID"))
            cfg.setPduRRoutingPduSID(self.read_value(ctr_tag, "PduRRoutingPduSID"))
            cfg.setPduRDestPduRef(self.read_ref_value(ctr_tag, "PduRDestPduRef"))
            cfg.setPduRSrcPduRef(self.read_optional_ref_value(ctr_tag, "PduRSrcPduRef"))
            pdur.addPduRRoutingTableEntry(cfg)
            self.logger.debug("Read PduRRoutingTableEntry <%s>" % cfg.getName())
