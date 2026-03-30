"""
Ethernet bus family model classes.

Implements: SWR_ETH_00001 (Ethernet stack model organization)
"""

from eb_model.models.eth_stack.ethif_xdm import (
    EthIfGeneral,
    EthIfController,
    EthIfFrameOwnerConfig,
    EthIfPhysController,
    EthIfSwitch,
    EthIfSwitchPortGroup,
    EthIfTransceiver,
    EthIfRxIndicationConfig,
    EthIfTxConfirmationConfig,
    EthIfEthControllerType,
    EthIfEthTrcvType,
    EthIfEthSwtType,
    EthIf,
)
from eb_model.models.eth_stack.ethsm_xdm import EthSMGeneral, EthSMDemEventParameterRefs, EthSMNetwork, EthSM
from eb_model.models.eth_stack.tcpip_xdm import (
    TcpIpGeneral, TcpIpOffloadChecksum, TcpIpIpV4Ctrl, TcpIpIpV6Ctrl,
    TcpIpCtrl, TcpIpLocalAddr, TcpIp
)
from eb_model.models.eth_stack.soad_xdm import (
    SoAdGeneral, SoAdSocketRemoteAddress, SoAdSocketUdp, SoAdSocketTcp,
    SoAdSocketConnection, SoAdSocketConnectionGroup, SoAdPduRouteDest,
    SoAdPduRoute, SoAdSocketRouteDest, SoAdSocketRoute, SoAdRoutingGroup,
    SoAd
)
from eb_model.models.eth_stack.udpnm_xdm import (
    UdpNmGeneral, UdpNmChannelIdentifiers, UdpNmRxPdu, UdpNmTxPdu,
    UdpNmUserDataTxPdu, UdpNmUserDataRxPdu, UdpNmChannel, UdpNm
)
from eb_model.models.eth_stack.doip_xdm import (
    DoIPGeneral, DoIPPduRRxPdu, DoIPPduRTxPdu, DoIPChannel,
    DoIPSoAdRxPdu, DoIPSoAdTxPdu, DoIPTcpConnection, DoIPUdpConnection,
    DoIPUdpVehicleAnnouncement, DoIPConnections, DoIP
)
from eb_model.models.eth_stack.someiptp_xdm import (
    SomeIpTpGeneral, SomeIpTpRxNPdu, SomeIpTpRxNSdu, SomeIpTpTxNPdu,
    SomeIpTpTxNSdu, SomeIpTpChannel, SomeIpTp
)
