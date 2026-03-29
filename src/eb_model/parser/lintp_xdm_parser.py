"""
LinTp XDM Parser Module - Extracts AUTOSAR LinTp configuration from EB Tresos XDM files.

Implements:
    - SWR_LINTP_00001: LinTp module parsing
    - SWR_LINTP_00002: NSDU configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.core.eb_doc import EBModel
from ..models.lin_stack.lintp_xdm import LinTp, LinTpGeneral, LinTpRxNSdu, LinTpTxNSdu
from ..parser.eb_parser import AbstractEbModelParser


class LinTpXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR LinTp (LIN Transport Protocol) module configuration.

    Extracts LinTp configuration including NSDUs.

    Implements: SWR_LINTP_00001 (LinTp Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the LinTp XDM parser."""
        super().__init__()
        self.lintp = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse LinTp module configuration from XDM element.

        LinTp may be embedded in LinIf or standalone.

        Implements: SWR_LINTP_00001
        """
        # LinTp may be embedded in LinIf or standalone
        if self.get_component_name(element) != "LinTp":
            raise ValueError("Invalid <%s> xdm file" % "LinTp")

        lintp = doc.getLinTp()

        self.read_version(element, lintp)

        self.logger.info("Parse LinTp ARVersion:<%s> SwVersion:<%s>" % (lintp.getArVersion().getVersion(), lintp.getSwVersion().getVersion()))

        self.lintp = lintp

        self.read_lintp_general(element, lintp)
        self.read_lintp_global_config(element, lintp)

    def read_lintp_general(self, element: ET.Element, lintp: LinTp):
        # LinTp general is within LinTpGlobalConfig
        config_tag = self.find_ctr_tag(element, "LinTpGlobalConfig")
        if config_tag is not None:
            general = LinTpGeneral(lintp, config_tag.attrib["name"])
            general.setLinTpMaxNumberOfRespPendingFrames(self.read_optional_value(config_tag, "LinTpMaxNumberOfRespPendingFrames"))
            general.setLinTpNumberOfRxNSdu(self.read_optional_value(config_tag, "LinTpNumberOfRxNSdu"))
            general.setLinTpNumberOfTxNSdu(self.read_optional_value(config_tag, "LinTpNumberOfTxNSdu"))
            lintp.setLinTpGeneral(general)
            self.logger.debug("Read LinTpGeneral")

    def read_lintp_global_config(self, element: ET.Element, lintp: LinTp):
        config_tag = self.find_ctr_tag(element, "LinTpGlobalConfig")
        if config_tag is not None:
            self.read_lintp_rx_nsdus(config_tag, lintp)
            self.read_lintp_tx_nsdus(config_tag, lintp)

    def read_lintp_rx_nsdus(self, element: ET.Element, lintp: LinTp):
        for ctr_tag in self.find_ctr_tag_list(element, "LinTpRxNSdu"):
            rx_nsdu = LinTpRxNSdu(lintp, ctr_tag.attrib["name"])
            rx_nsdu.setLinTpRxNSduId(self.read_value(ctr_tag, "LinTpRxNSduId"))
            rx_nsdu.setLinTpRxNSduRef(self.read_ref_value(ctr_tag, "LinTpRxNSduRef"))
            lintp.addLinTpRxNSdu(rx_nsdu)
            self.logger.debug("Read LinTpRxNSdu <%s>" % rx_nsdu.getName())

    def read_lintp_tx_nsdus(self, element: ET.Element, lintp: LinTp):
        for ctr_tag in self.find_ctr_tag_list(element, "LinTpTxNSdu"):
            tx_nsdu = LinTpTxNSdu(lintp, ctr_tag.attrib["name"])
            tx_nsdu.setLinTpTxNSduId(self.read_value(ctr_tag, "LinTpTxNSduId"))
            tx_nsdu.setLinTpTxNSduRef(self.read_ref_value(ctr_tag, "LinTpTxNSduRef"))
            lintp.addLinTpTxNSdu(tx_nsdu)
            self.logger.debug("Read LinTpTxNSdu <%s>" % tx_nsdu.getName())
