"""
SoAd XDM Parser Module - Extracts AUTOSAR SoAd configuration from EB Tresos XDM files.

Implements:
    - SWR_SOAD_00001: SoAd module parsing
    - SWR_SOAD_00002: General configuration parsing
    - SWR_SOAD_00003: Socket connection configuration parsing
    - SWR_SOAD_00004: PDU route configuration parsing
    - SWR_SOAD_00005: Routing group configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.soad_xdm import (
    SoAd, SoAdGeneral, SoAdSocketConnectionGroup, SoAdSocketConnection,
    SoAdSocketRemoteAddress, SoAdSocketUdp, SoAdSocketTcp,
    SoAdPduRoute, SoAdPduRouteDest, SoAdSocketRoute, SoAdSocketRouteDest, SoAdRoutingGroup
)
from ..parser.eb_parser import AbstractEbModelParser


class SoAdXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR SoAd (Socket Adapter) module configuration.

    Extracts SoAd configuration including socket connections, PDU routes,
    and routing groups.

    Implements: SWR_SOAD_00001 (SoAd Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the SoAd XDM parser."""
        super().__init__()
        self.soad = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse SoAd module configuration from XDM element.

        Implements: SWR_SOAD_00001
        """
        if self.get_component_name(element) != "SoAd":
            raise ValueError("Invalid <%s> xdm file" % "SoAd")

        soad = doc.getSoAd()

        self.read_version(element, soad)

        self.logger.info("Parse SoAd ARVersion:<%s> SwVersion:<%s>" % (soad.getArVersion().getVersion(), soad.getSwVersion().getVersion()))

        self.soad = soad

        self.read_soad_general(element, soad)
        self.read_soad_socket_connection_groups(element, soad)
        self.read_soad_pdu_routes(element, soad)
        self.read_soad_socket_routes(element, soad)
        self.read_soad_routing_groups(element, soad)

    def read_soad_general(self, element: ET.Element, soad: SoAd):
        """
        Parse SoAd general configuration.

        Implements: SWR_SOAD_00002
        """
        ctr_tag = self.find_ctr_tag(element, "SoAdGeneral")
        if ctr_tag is not None:
            general = SoAdGeneral(soad, ctr_tag.attrib["name"])
            general.setSoAdDevErrorDetect(self.read_value(ctr_tag, "SoAdDevErrorDetect"))
            general.setSoAdGetAndResetMeasurementDataApi(self.read_value(ctr_tag, "SoAdGetAndResetMeasurementDataApi"))
            general.setSoAdIPv6AddressEnabled(self.read_value(ctr_tag, "SoAdIPv6AddressEnabled"))
            general.setSoAdMainFunctionPeriod(self.read_value(ctr_tag, "SoAdMainFunctionPeriod"))
            general.setSoAdSoConMax(self.read_value(ctr_tag, "SoAdSoConMax"))
            general.setSoAdRoutingGroupMax(self.read_value(ctr_tag, "SoAdRoutingGroupMax"))
            general.setSoAdVersionInfoApi(self.read_value(ctr_tag, "SoAdVersionInfoApi"))
            general.setSoAdTlsEnabled(self.read_optional_value(ctr_tag, "SoAdTlsEnabled"))
            general.setSoAdEnableSecurityEventReporting(self.read_optional_value(ctr_tag, "SoAdEnableSecurityEventReporting"))
            soad.setSoAdGeneral(general)
            self.logger.debug("Read SoAdGeneral")

    def read_soad_socket_connection_groups(self, element: ET.Element, soad: SoAd):
        """
        Parse SoAd socket connection group configurations.

        Implements: SWR_SOAD_00003
        """
        for ctr_tag in self.find_ctr_tag_list(element, "SoAdSocketConnectionGroup"):
            group = SoAdSocketConnectionGroup(soad, ctr_tag.attrib["name"])
            group.setSoAdSocketLocalPort(self.read_value(ctr_tag, "SoAdSocketLocalPort"))
            group.setSoAdSocketTpRxBufferMin(self.read_value(ctr_tag, "SoAdSocketTpRxBufferMin"))
            group.setSoAdSocketFramePriority(self.read_value(ctr_tag, "SoAdSocketFramePriority"))

            # Read nested socket connections
            for conn_tag in self.find_ctr_tag_list(ctr_tag, "SoAdSocketConnection"):
                conn = SoAdSocketConnection(group, conn_tag.attrib["name"])
                conn.setSoAdSocketId(self.read_value(conn_tag, "SoAdSocketId"))

                # Read remote address
                remote_ctr = self.find_ctr_tag(conn_tag, "SoAdSocketRemoteAddress")
                if remote_ctr is not None:
                    remote_addr = SoAdSocketRemoteAddress(conn, remote_ctr.attrib["name"])
                    remote_addr.setSoAdSocketRemotePort(self.read_value(remote_ctr, "SoAdSocketRemotePort"))
                    conn.setSoAdSocketRemoteAddress(remote_addr)

                conn.setSoAdSocketUdpListenOnly(self.read_optional_value(conn_tag, "SoAdSocketUdpListenOnly"))

                # Read UDP config if present
                udp_ctr = self.find_ctr_tag(conn_tag, "SoAdSocketUdp")
                if udp_ctr is not None:
                    udp = SoAdSocketUdp(conn, udp_ctr.attrib["name"])
                    udp.setSoAdTxBufferPoolSize(self.read_value(udp_ctr, "SoAdTxBufferPoolSize"))
                    conn.setSoAdSocketUdp(udp)

                # Read TCP config if present
                tcp_ctr = self.find_ctr_tag(conn_tag, "SoAdSocketTcp")
                if tcp_ctr is not None:
                    tcp = SoAdSocketTcp(conn, tcp_ctr.attrib["name"])
                    tcp.setSoAdSocketTcpInitiate(self.read_value(tcp_ctr, "SoAdSocketTcpInitiate"))
                    tcp.setSoAdSocketTcpKeepAlive(self.read_optional_value(tcp_ctr, "SoAdSocketTcpKeepAlive"))
                    tcp.setSoAdSocketTcpKeepAliveTime(self.read_optional_value(tcp_ctr, "SoAdSocketTcpKeepAliveTime"))
                    tcp.setSoAdSocketTcpNoDelay(self.read_optional_value(tcp_ctr, "SoAdSocketTcpNoDelay"))
                    tcp.setSoAdSocketTcpTxQuota(self.read_optional_value(tcp_ctr, "SoAdSocketTcpTxQuota"))
                    tcp.setSoAdTlsConnectionRef(self.read_optional_ref_value(tcp_ctr, "SoAdTlsConnectionRef"))
                    tcp.setSoAdDatagramTlsConnectionRef(self.read_optional_ref_value(tcp_ctr, "SoAdDatagramTlsConnectionRef"))
                    conn.setSoAdSocketTcp(tcp)

                group.addSoAdSocketConnection(conn)

            soad.addSoAdSocketConnectionGroup(group)
            self.logger.debug("Read SoAdSocketConnectionGroup <%s>" % group.getName())

    def read_soad_pdu_routes(self, element: ET.Element, soad: SoAd):
        """
        Parse SoAd PDU route configurations.

        Implements: SWR_SOAD_00004
        """
        for ctr_tag in self.find_ctr_tag_list(element, "SoAdPduRoute"):
            route = SoAdPduRoute(soad, ctr_tag.attrib["name"])
            route.setSoAdTxPduId(self.read_value(ctr_tag, "SoAdTxPduId"))
            route.setSoAdTxUpperLayerType(self.read_value(ctr_tag, "SoAdTxUpperLayerType"))
            route.setSoAdSkipIfTxConfirmation(self.read_optional_value(ctr_tag, "SoAdSkipIfTxConfirmation"))
            route.setSoAdPduHeaderEnable(self.read_optional_value(ctr_tag, "SoAdPduHeaderEnable"))
            route.setSoAdResourceManagementEnable(self.read_optional_value(ctr_tag, "SoAdResourceManagementEnable"))

            # Read destination
            dest_ctr = self.find_ctr_tag(ctr_tag, "SoAdPduRouteDest")
            if dest_ctr is not None:
                dest = SoAdPduRouteDest(route, dest_ctr.attrib["name"])
                dest.setSoAdTxPduHeaderId(self.read_value(dest_ctr, "SoAdTxPduHeaderId"))
                dest.setSoAdTxUdpTriggerMode(self.read_value(dest_ctr, "SoAdTxUdpTriggerMode"))
                dest.setSoAdTxUdpTriggerTimeout(self.read_value(dest_ctr, "SoAdTxUdpTriggerTimeout"))
                dest.setSoAdTxSocketConnOrSocketConnBundleRef(self.read_ref_value(dest_ctr, "SoAdTxSocketConnOrSocketConnBundleRef"))
                route.setSoAdPduRouteDest(dest)

            soad.addSoAdPduRoute(route)
            self.logger.debug("Read SoAdPduRoute <%s>" % route.getName())

    def read_soad_socket_routes(self, element: ET.Element, soad: SoAd):
        """Parse SoAd socket route configurations."""
        for ctr_tag in self.find_ctr_tag_list(element, "SoAdSocketRoute"):
            route = SoAdSocketRoute(soad, ctr_tag.attrib["name"])

            # Read destination
            dest_ctr = self.find_ctr_tag(ctr_tag, "SoAdSocketRouteDest")
            if dest_ctr is not None:
                dest = SoAdSocketRouteDest(route, dest_ctr.attrib["name"])
                dest.setSoAdRxPduHeaderId(self.read_value(dest_ctr, "SoAdRxPduHeaderId"))
                dest.setSoAdRxPduId(self.read_value(dest_ctr, "SoAdRxPduId"))
                dest.setSoAdRxUpperLayerType(self.read_value(dest_ctr, "SoAdRxUpperLayerType"))
                dest.setSoAdRxSocketConnOrSocketConnBundleRef(self.read_ref_value(dest_ctr, "SoAdRxSocketConnOrSocketConnBundleRef"))
                dest.setSoAdRxPduRef(self.read_optional_ref_value(dest_ctr, "SoAdRxPduRef"))
                route.setSoAdSocketRouteDest(dest)

            soad.addSoAdSocketRoute(route)
            self.logger.debug("Read SoAdSocketRoute <%s>" % route.getName())

    def read_soad_routing_groups(self, element: ET.Element, soad: SoAd):
        """
        Parse SoAd routing group configurations.

        Implements: SWR_SOAD_00005
        """
        for ctr_tag in self.find_ctr_tag_list(element, "SoAdRoutingGroup"):
            group = SoAdRoutingGroup(soad, ctr_tag.attrib["name"])
            group.setSoAdRoutingGroupId(self.read_value(ctr_tag, "SoAdRoutingGroupId"))
            soad.addSoAdRoutingGroup(group)
            self.logger.debug("Read SoAdRoutingGroup <%s>" % group.getName())
