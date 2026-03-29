"""
TcpIp XDM Parser Module - Extracts AUTOSAR TcpIp configuration from EB Tresos XDM files.

Implements:
    - SWR_TCPIP_00001: TcpIp module parsing
    - SWR_TCPIP_00002: General configuration parsing
    - SWR_TCPIP_00003: Controller configuration parsing
    - SWR_TCPIP_00004: TCP/UDP configuration parsing
    - SWR_TCPIP_00005: Local address configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.core.eb_doc import EBModel
from ..models.eth_stack.tcpip_xdm import (
    TcpIp, TcpIpGeneral, TcpIpCtrl, TcpIpOffloadChecksum,
    TcpIpIpV4Ctrl, TcpIpIpV6Ctrl, TcpIpLocalAddr
)
from ..parser.eb_parser import AbstractEbModelParser


class TcpIpXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR TcpIp (TCP/IP Stack) module configuration.

    Extracts TcpIp configuration including controllers, TCP/UDP settings,
    and local address configurations.

    Implements: SWR_TCPIP_00001 (TcpIp Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the TcpIp XDM parser."""
        super().__init__()
        self.tcpip = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse TcpIp module configuration from XDM element.

        Implements: SWR_TCPIP_00001
        """
        if self.get_component_name(element) != "TcpIp":
            raise ValueError("Invalid <%s> xdm file" % "TcpIp")

        tcpip = doc.getTcpIp()

        self.read_version(element, tcpip)

        self.logger.info("Parse TcpIp ARVersion:<%s> SwVersion:<%s>" % (tcpip.getArVersion().getVersion(), tcpip.getSwVersion().getVersion()))

        self.tcpip = tcpip

        self.read_tcpip_general(element, tcpip)
        self.read_tcpip_ctrls(element, tcpip)
        self.read_tcpip_local_addrs(element, tcpip)

    def read_tcpip_general(self, element: ET.Element, tcpip: TcpIp):
        """
        Parse TcpIp general configuration.

        Implements: SWR_TCPIP_00002
        """
        ctr_tag = self.find_ctr_tag(element, "TcpIpGeneral")
        if ctr_tag is not None:
            general = TcpIpGeneral(tcpip, ctr_tag.attrib["name"])
            general.setTcpIpDevErrorDetect(self.read_value(ctr_tag, "TcpIpDevErrorDetect"))
            general.setTcpIpMainFunctionPeriod(self.read_value(ctr_tag, "TcpIpMainFunctionPeriod"))
            general.setTcpIpBufferSizeMax(self.read_value(ctr_tag, "TcpIpBufferSizeMax"))
            general.setTcpIpMaxNumOfSockets(self.read_value(ctr_tag, "TcpIpMaxNumOfSockets"))
            tcpip.setTcpIpGeneral(general)
            self.logger.debug("Read TcpIpGeneral")

    def read_tcpip_ctrls(self, element: ET.Element, tcpip: TcpIp):
        """
        Parse TcpIp controller configurations.

        Implements: SWR_TCPIP_00003
        """
        for ctr_tag in self.find_ctr_tag_list(element, "TcpIpCtrl"):
            ctrl = TcpIpCtrl(tcpip, ctr_tag.attrib["name"])

            # Read references
            ctrl.setTcpIpEthIfCtrlRef(self.read_optional_ref_value(ctr_tag, "TcpIpEthIfCtrlRef"))
            ctrl.setTcpIpDhcpServerConfigRef(self.read_optional_ref_value(ctr_tag, "TcpIpDhcpServerConfigRef"))

            # Read OffloadChecksum if present
            offload_ctr = self.find_ctr_tag(ctr_tag, "TcpIpOffloadChecksum")
            if offload_ctr is not None:
                offload = TcpIpOffloadChecksum(ctrl, offload_ctr.attrib["name"])
                ctrl.setTcpIpOffloadChecksum(offload)

            # Read IPv4 controller config if present
            ipv4_ctr = self.find_ctr_tag(ctr_tag, "TcpIpIpV4Ctrl")
            if ipv4_ctr is not None:
                ipv4_ctrl = TcpIpIpV4Ctrl(ctrl, ipv4_ctr.attrib["name"])
                ipv4_ctrl.setTcpIpIpV4PathMtuEnabled(self.read_value(ipv4_ctr, "TcpIpIpV4PathMtuEnabled"))
                ipv4_ctrl.setTcpIpIpV4PathMtuTimeout(self.read_value(ipv4_ctr, "TcpIpIpV4PathMtuTimeout"))
                ctrl.setTcpIpIpV4Ctrl(ipv4_ctrl)

            # Read IPv6 controller config if present
            ipv6_ctr = self.find_ctr_tag(ctr_tag, "TcpIpIpV6Ctrl")
            if ipv6_ctr is not None:
                ipv6_ctrl = TcpIpIpV6Ctrl(ctrl, ipv6_ctr.attrib["name"])
                ipv6_ctrl.setTcpIpIpV6PathMtuEnabled(self.read_value(ipv6_ctr, "TcpIpIpV6PathMtuEnabled"))
                ipv6_ctrl.setTcpIpIpV6PathMtuTimeout(self.read_value(ipv6_ctr, "TcpIpIpV6PathMtuTimeout"))
                ctrl.setTcpIpIpV6Ctrl(ipv6_ctrl)

            tcpip.addTcpIpCtrl(ctrl)
            self.logger.debug("Read TcpIpCtrl <%s>" % ctrl.getName())

    def read_tcpip_local_addrs(self, element: ET.Element, tcpip: TcpIp):
        """
        Parse TcpIp local address configurations.

        Implements: SWR_TCPIP_00005
        """
        for ctr_tag in self.find_ctr_tag_list(element, "TcpIpLocalAddr"):
            local_addr = TcpIpLocalAddr(tcpip, ctr_tag.attrib["name"])
            local_addr.setTcpIpAddrId(self.read_value(ctr_tag, "TcpIpAddrId"))
            local_addr.setTcpIpAddressType(self.read_value(ctr_tag, "TcpIpAddressType"))
            local_addr.setTcpIpDomainType(self.read_value(ctr_tag, "TcpIpDomainType"))
            tcpip.addTcpIpLocalAddr(local_addr)
            self.logger.debug("Read TcpIpLocalAddr <%s>" % local_addr.getName())
