"""
UdpNm XDM Parser Module - Extracts AUTOSAR UdpNm configuration from EB Tresos XDM files.

Implements:
    - SWR_UDPNM_00001: UdpNm module parsing
    - SWR_UDPNM_00002: General configuration parsing
    - SWR_UDPNM_00003: Channel configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.core.eb_doc import EBModel
from ..models.eth_stack.udpnm_xdm import (
    UdpNm, UdpNmGeneral, UdpNmChannel, UdpNmChannelIdentifiers,
    UdpNmRxPdu, UdpNmTxPdu, UdpNmUserDataTxPdu, UdpNmUserDataRxPdu
)
from ..parser.eb_parser import AbstractEbModelParser


class UdpNmXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR UdpNm (UDP Network Management) module configuration.

    Extracts UdpNm configuration including general parameters and channel configurations.

    Implements: SWR_UDPNM_00001 (UdpNm Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the UdpNm XDM parser."""
        super().__init__()
        self.udpnm = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse UdpNm module configuration from XDM element.

        Implements: SWR_UDPNM_00001
        """
        if self.get_component_name(element) != "UdpNm":
            raise ValueError("Invalid <%s> xdm file" % "UdpNm")

        udpnm = doc.getUdpNm()

        self.read_version(element, udpnm)

        self.logger.info("Parse UdpNm ARVersion:<%s> SwVersion:<%s>" % (udpnm.getArVersion().getVersion(), udpnm.getSwVersion().getVersion()))

        self.udpnm = udpnm

        self.read_udpnm_general(element, udpnm)
        self.read_udpnm_channels(element, udpnm)

    def read_udpnm_general(self, element: ET.Element, udpnm: UdpNm):
        """
        Parse UdpNm general configuration.

        Implements: SWR_UDPNM_00002
        """
        ctr_tag = self.find_ctr_tag(element, "UdpNmGeneral")
        if ctr_tag is not None:
            general = UdpNmGeneral(udpnm, ctr_tag.attrib["name"])
            general.setUdpNmDevErrorDetect(self.read_value(ctr_tag, "UdpNmDevErrorDetect"))
            general.setUdpNmVersionInfoApi(self.read_value(ctr_tag, "UdpNmVersionInfoApi"))
            general.setUdpNmMainFunctionPeriod(self.read_value(ctr_tag, "UdpNmMainFunctionPeriod"))
            udpnm.setUdpNmGeneral(general)
            self.logger.debug("Read UdpNmGeneral")

    def read_udpnm_channels(self, element: ET.Element, udpnm: UdpNm):
        """
        Parse UdpNm channel configurations.

        Implements: SWR_UDPNM_00003
        """
        config_lst = self.find_ctr_tag_list(element, "UdpNmChannelConfig")
        if config_lst:
            for lst_tag in config_lst:
                for ctr_tag in self.find_ctr_tag_list(lst_tag, "UdpNmChannel"):
                    channel = UdpNmChannel(udpnm, ctr_tag.attrib["name"])

                    # Read identifiers
                    id_ctr = self.find_ctr_tag(ctr_tag, "UdpNmChannelIdentifiers")
                    if id_ctr is not None:
                        ids = UdpNmChannelIdentifiers(channel, id_ctr.attrib["name"])
                        ids.setUdpNmChannelId(self.read_value(id_ctr, "UdpNmChannelId"))
                        channel.setUdpNmChannelIdentifiers(ids)

                    # Read RxPdu
                    rx_pdu_ctr = self.find_ctr_tag(ctr_tag, "UdpNmRxPdu")
                    if rx_pdu_ctr is not None:
                        rx_pdu = UdpNmRxPdu(channel, rx_pdu_ctr.attrib["name"])
                        rx_pdu.setUdpNmRxPduId(self.read_value(rx_pdu_ctr, "UdpNmRxPduId"))
                        rx_pdu.setUdpNmRxPduRef(self.read_ref_value(rx_pdu_ctr, "UdpNmRxPduRef"))
                        channel.setUdpNmRxPdu(rx_pdu)

                    # Read TxPdu
                    tx_pdu_ctr = self.find_ctr_tag(ctr_tag, "UdpNmTxPdu")
                    if tx_pdu_ctr is not None:
                        tx_pdu = UdpNmTxPdu(channel, tx_pdu_ctr.attrib["name"])
                        tx_pdu.setUdpNmTxPduId(self.read_value(tx_pdu_ctr, "UdpNmTxPduId"))
                        tx_pdu.setUdpNmTxPduRef(self.read_ref_value(tx_pdu_ctr, "UdpNmTxPduRef"))
                        channel.setUdpNmTxPdu(tx_pdu)

                    udpnm.addUdpNmChannel(channel)
                    self.logger.debug("Read UdpNmChannel <%s>" % channel.getName())
