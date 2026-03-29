"""
DoIP XDM Parser Module - Extracts AUTOSAR DoIP configuration from EB Tresos XDM files.

Implements:
    - SWR_DOIP_00001: DoIP module parsing
    - SWR_DOIP_00002: General configuration parsing
    - SWR_DOIP_00003: Channel configuration parsing
    - SWR_DOIP_00004: Connection configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.core.eb_doc import EBModel
from ..models.eth_stack.doip_xdm import (
    DoIP, DoIPGeneral, DoIPChannel, DoIPConnections,
    DoIPTcpConnection, DoIPUdpConnection, DoIPUdpVehicleAnnouncement,
    DoIPPduRRxPdu, DoIPPduRTxPdu, DoIPSoAdRxPdu, DoIPSoAdTxPdu
)
from ..parser.eb_parser import AbstractEbModelParser


class DoIPXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR DoIP (Diagnostics over IP) module configuration.

    Extracts DoIP configuration including general parameters, channels,
    and connections.

    Implements: SWR_DOIP_00001 (DoIP Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the DoIP XDM parser."""
        super().__init__()
        self.doip = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse DoIP module configuration from XDM element.

        Implements: SWR_DOIP_00001
        """
        if self.get_component_name(element) != "DoIP":
            raise ValueError("Invalid <%s> xdm file" % "DoIP")

        doip = doc.getDoIP()

        self.read_version(element, doip)

        self.logger.info("Parse DoIP ARVersion:<%s> SwVersion:<%s>" % (doip.getArVersion().getVersion(), doip.getSwVersion().getVersion()))

        self.doip = doip

        self.read_doip_general(element, doip)
        self.read_doip_channels(element, doip)
        self.read_doip_custom_channels(element, doip)
        self.read_doip_connections(element, doip)

    def read_doip_general(self, element: ET.Element, doip: DoIP):
        """
        Parse DoIP general configuration.

        Implements: SWR_DOIP_00002
        """
        ctr_tag = self.find_ctr_tag(element, "DoIPGeneral")
        if ctr_tag is not None:
            general = DoIPGeneral(doip, ctr_tag.attrib["name"])
            general.setDoIPDevErrorDetect(self.read_value(ctr_tag, "DoIPDevErrorDetect"))
            general.setDoIPVersionInfoApi(self.read_optional_value(ctr_tag, "DoIPVersionInfoApi"))
            general.setDoIPMainFunctionPeriod(self.read_value(ctr_tag, "DoIPMainFunctionPeriod"))
            doip.setDoIPGeneral(general)
            self.logger.debug("Read DoIPGeneral")

    def read_doip_channels(self, element: ET.Element, doip: DoIP):
        """
        Parse DoIP channel configurations.

        Implements: SWR_DOIP_00003
        """
        config_set_lst = self.find_ctr_tag_list(element, "DoIPConfigSet")
        if config_set_lst:
            for lst_tag in config_set_lst:
                for ctr_tag in self.find_ctr_tag_list(lst_tag, "DoIPChannel"):
                    channel = DoIPChannel(doip, ctr_tag.attrib["name"])

                    # Read RxPdu
                    rx_pdu_ctr = self.find_ctr_tag(ctr_tag, "DoIPPduRRxPdu")
                    if rx_pdu_ctr is not None:
                        rx_pdu = DoIPPduRRxPdu(channel, rx_pdu_ctr.attrib["name"])
                        channel.setDoIPPduRRxPdu(rx_pdu)

                    # Read TxPdu
                    tx_pdu_ctr = self.find_ctr_tag(ctr_tag, "DoIPPduRTxPdu")
                    if tx_pdu_ctr is not None:
                        tx_pdu = DoIPPduRTxPdu(channel, tx_pdu_ctr.attrib["name"])
                        channel.setDoIPPduRTxPdu(tx_pdu)

                    doip.addDoIPChannel(channel)
                    self.logger.debug("Read DoIPChannel <%s>" % channel.getName())

    def read_doip_custom_channels(self, element: ET.Element, doip: DoIP):
        """Parse DoIP custom channel configurations."""
        config_set_lst = self.find_ctr_tag_list(element, "DoIPConfigSet")
        if config_set_lst:
            for lst_tag in config_set_lst:
                for ctr_tag in self.find_ctr_tag_list(lst_tag, "DoIPCustomChannel"):
                    channel = DoIPChannel(doip, ctr_tag.attrib["name"])

                    # Read RxPdu
                    rx_pdu_ctr = self.find_ctr_tag(ctr_tag, "DoIPPduRRxPdu")
                    if rx_pdu_ctr is not None:
                        rx_pdu = DoIPPduRRxPdu(channel, rx_pdu_ctr.attrib["name"])
                        channel.setDoIPPduRRxPdu(rx_pdu)

                    # Read TxPdu
                    tx_pdu_ctr = self.find_ctr_tag(ctr_tag, "DoIPPduRTxPdu")
                    if tx_pdu_ctr is not None:
                        tx_pdu = DoIPPduRTxPdu(channel, tx_pdu_ctr.attrib["name"])
                        channel.setDoIPPduRTxPdu(tx_pdu)

                    doip.addDoIPCustomChannel(channel)
                    self.logger.debug("Read DoIPCustomChannel <%s>" % channel.getName())

    def read_doip_connections(self, element: ET.Element, doip: DoIP):
        """
        Parse DoIP connection configurations.

        Implements: SWR_DOIP_00004
        """
        config_set_lst = self.find_ctr_tag_list(element, "DoIPConfigSet")
        if config_set_lst:
            for lst_tag in config_set_lst:
                conn_ctr = self.find_ctr_tag(lst_tag, "DoIPConnections")
                if conn_ctr is not None:
                    connections = DoIPConnections(doip, conn_ctr.attrib["name"])

                    # Read TCP connections
                    for tcp_ctr in self.find_ctr_tag_list(conn_ctr, "DoIPTcpConnection"):
                        tcp_conn = DoIPTcpConnection(connections, tcp_ctr.attrib["name"])

                        # Read SoAdRxPdu
                        rx_pdu_ctr = self.find_ctr_tag(tcp_ctr, "DoIPSoAdRxPdu")
                        if rx_pdu_ctr is not None:
                            rx_pdu = DoIPSoAdRxPdu(tcp_conn, rx_pdu_ctr.attrib["name"])
                            tcp_conn.setDoIPSoAdRxPdu(rx_pdu)

                        # Read SoAdTxPdu
                        tx_pdu_ctr = self.find_ctr_tag(tcp_ctr, "DoIPSoAdTxPdu")
                        if tx_pdu_ctr is not None:
                            tx_pdu = DoIPSoAdTxPdu(tcp_conn, tx_pdu_ctr.attrib["name"])
                            tcp_conn.setDoIPSoAdTxPdu(tx_pdu)

                        connections.addDoIPTcpConnection(tcp_conn)

                    # Read UDP connections
                    for udp_ctr in self.find_ctr_tag_list(conn_ctr, "DoIPUdpConnection"):
                        udp_conn = DoIPUdpConnection(connections, udp_ctr.attrib["name"])

                        # Read SoAdRxPdu
                        rx_pdu_ctr = self.find_ctr_tag(udp_ctr, "DoIPSoAdRxPdu")
                        if rx_pdu_ctr is not None:
                            rx_pdu = DoIPSoAdRxPdu(udp_conn, rx_pdu_ctr.attrib["name"])
                            udp_conn.setDoIPSoAdRxPdu(rx_pdu)

                        # Read SoAdTxPdu
                        tx_pdu_ctr = self.find_ctr_tag(udp_ctr, "DoIPSoAdTxPdu")
                        if tx_pdu_ctr is not None:
                            tx_pdu = DoIPSoAdTxPdu(udp_conn, tx_pdu_ctr.attrib["name"])
                            udp_conn.setDoIPSoAdTxPdu(tx_pdu)

                        connections.addDoIPUdpConnection(udp_conn)

                    # Read UDP vehicle announcement
                    va_ctr = self.find_ctr_tag(conn_ctr, "DoIPUdpVehicleAnnouncement")
                    if va_ctr is not None:
                        va = DoIPUdpVehicleAnnouncement(connections, va_ctr.attrib["name"])

                        # Read SoAdTxPdu
                        tx_pdu_ctr = self.find_ctr_tag(va_ctr, "DoIPSoAdTxPdu")
                        if tx_pdu_ctr is not None:
                            tx_pdu = DoIPSoAdTxPdu(va, tx_pdu_ctr.attrib["name"])
                            va.setDoIPSoAdTxPdu(tx_pdu)

                        connections.setDoIPUdpVehicleAnnouncement(va)

                    doip.setDoIPConnections(connections)
                    self.logger.debug("Read DoIPConnections")
