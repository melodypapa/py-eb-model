"""
CanTp XDM Parser Module - Extracts AUTOSAR CanTp configuration from EB Tresos XDM files.

Implements:
    - SWR_CANTP_00001: CanTp module parsing
    - SWR_CANTP_00002: Channel configuration parsing
    - SWR_CANTP_00003: NSDU configuration parsing
"""
import xml.etree.ElementTree as ET
from eb_model.models.core.eb_doc import EBModel
from eb_model.models.can_stack.cantp_xdm import (
    CanTp, CanTpGeneral, CanTpChannel, CanTpRxNSdu, CanTpTxNSdu
)
from eb_model.parser.core.eb_parser import AbstractEbModelParser


class CanTpXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR CanTp (CAN Transport Protocol) module configuration.

    Extracts CanTp configuration including channels and NSDUs.

    Implements: SWR_CANTP_00001 (CanTp Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the CanTp XDM parser."""
        super().__init__()
        self.cantp = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse CanTp module configuration from XDM element.

        Implements: SWR_CANTP_00001
        """
        if self.get_component_name(element) != "CanTp":
            raise ValueError("Invalid <%s> xdm file" % "CanTp")

        cantp = doc.getCanTp()

        self.read_version(element, cantp)

        self.logger.info("Parse CanTp ARVersion:<%s> SwVersion:<%s>" % (cantp.getArVersion().getVersion(), cantp.getSwVersion().getVersion()))

        self.cantp = cantp

        self.read_cantp_general(element, cantp)
        self.read_cantp_config(element, cantp)

    def read_cantp_general(self, element: ET.Element, cantp: CanTp):
        ctr_tag = self.find_ctr_tag(element, "CanTpGeneral")
        if ctr_tag is not None:
            general = CanTpGeneral(cantp, ctr_tag.attrib["name"])
            general.setCanTpDevErrorDetect(self.read_value(ctr_tag, "CanTpDevErrorDetect"))
            general.setCanTpMainFunctionPeriod(self.read_optional_value(ctr_tag, "CanTpMainFunctionPeriod"))
            general.setCanTpMaxTxChannels(self.read_optional_value(ctr_tag, "CanTpMaxTxChannels"))
            general.setCanTpMaxRxChannels(self.read_optional_value(ctr_tag, "CanTpMaxRxChannels"))
            cantp.setCanTpGeneral(general)
            self.logger.debug("Read CanTpGeneral")

    def read_cantp_config(self, element: ET.Element, cantp: CanTp):
        config_tag = self.find_ctr_tag(element, "CanTpConfig")
        if config_tag is not None:
            self.read_cantp_channels(config_tag, cantp)
            self.read_cantp_rx_nsdus(config_tag, cantp)
            self.read_cantp_tx_nsdus(config_tag, cantp)

    def read_cantp_channels(self, element: ET.Element, cantp: CanTp):
        for ctr_tag in self.find_ctr_tag_list(element, "CanTpChannel"):
            channel = CanTpChannel(cantp, ctr_tag.attrib["name"])
            channel.setCanTpChannelMode(self.read_optional_value(ctr_tag, "CanTpChannelMode"))
            channel.setCanTpSTmin(self.read_optional_value(ctr_tag, "CanTpSTmin"))
            cantp.addCanTpChannel(channel)
            self.logger.debug("Read CanTpChannel <%s>" % channel.getName())

    def read_cantp_rx_nsdus(self, element: ET.Element, cantp: CanTp):
        for ctr_tag in self.find_ctr_tag_list(element, "CanTpRxNSdu"):
            rx_nsdu = CanTpRxNSdu(cantp, ctr_tag.attrib["name"])
            rx_nsdu.setCanTpRxNSduId(self.read_value(ctr_tag, "CanTpRxNSduId"))
            rx_nsdu.setCanTpRxNSduRef(self.read_ref_value(ctr_tag, "CanTpRxNSduRef"))
            rx_nsdu.setCanTpBs(self.read_optional_value(ctr_tag, "CanTpBs"))
            rx_nsdu.setCanTpSTmin(self.read_optional_value(ctr_tag, "CanTpSTmin"))
            cantp.addCanTpRxNSdu(rx_nsdu)
            self.logger.debug("Read CanTpRxNSdu <%s>" % rx_nsdu.getName())

    def read_cantp_tx_nsdus(self, element: ET.Element, cantp: CanTp):
        for ctr_tag in self.find_ctr_tag_list(element, "CanTpTxNSdu"):
            tx_nsdu = CanTpTxNSdu(cantp, ctr_tag.attrib["name"])
            tx_nsdu.setCanTpTxNSduId(self.read_value(ctr_tag, "CanTpTxNSduId"))
            tx_nsdu.setCanTpTxNSduRef(self.read_ref_value(ctr_tag, "CanTpTxNSduRef"))
            tx_nsdu.setCanTpTc(self.read_optional_value(ctr_tag, "CanTpTc"))
            tx_nsdu.setCanTpSTmin(self.read_optional_value(ctr_tag, "CanTpSTmin"))
            cantp.addCanTpTxNSdu(tx_nsdu)
            self.logger.debug("Read CanTpTxNSdu <%s>" % tx_nsdu.getName())
