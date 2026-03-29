"""
IpduM XDM Parser Module - Extracts AUTOSAR IpduM configuration from EB Tresos XDM files.

Implements:
    - SWR_IPDUM_00001: IpduM module parsing
    - SWR_IPDUM_00002: IpduM dynamic PDU parsing
"""
import xml.etree.ElementTree as ET
from ...models.core.eb_doc import EBModel
from ...models.com_stack.ipdum_xdm import IpduM, IpduMDynPdu
from ..core.eb_parser import AbstractEbModelParser


class IpduMXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR IpduM (IPDU Multiplexer) module configuration.

    Extracts IpduM multiplexer configuration including dynamic PDUs.

    Implements: SWR_IPDUM_00001 (IpduM Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the IpduM XDM parser."""
        super().__init__()
        self.ipdum = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse IpduM module configuration from XDM element.

        Implements: SWR_IPDUM_00001
        """
        if self.get_component_name(element) != "IpduM":
            raise ValueError("Invalid <%s> xdm file" % "IpduM")

        ipdum = doc.getIpduM()

        self.read_version(element, ipdum)

        self.logger.info("Parse IpduM ARVersion:<%s> SwVersion:<%s>" % (ipdum.getArVersion().getVersion(), ipdum.getSwVersion().getVersion()))

        self.ipdum = ipdum

        self.read_ipdum_dynamic_pdus(element, ipdum)

    def read_ipdum_dynamic_pdus(self, element: ET.Element, ipdum: IpduM):
        """
        Parse IpduM dynamic PDU configuration.

        Implements: SWR_IPDUM_00002 (IpduM dynamic PDU parsing)
        """
        for ctr_tag in self.find_ctr_tag_list(element, "IpduMDynamicPdu"):
            dyn_pdu = IpduMDynPdu(ipdum, ctr_tag.attrib["name"])
            dyn_pdu.setIpduMDynPduId(self.read_value(ctr_tag, "IpduMDynPduId"))
            dyn_pdu.setIpduMDynPduLength(self.read_value(ctr_tag, "IpduMDynPduLength"))
            ipdum.addIpduMDynPdu(dyn_pdu)
            self.logger.debug("Read IpduMDynamicPdu <%s>" % dyn_pdu.getName())
