from typing import List, Optional
import logging
from eb_model.models.core.abstract import EcucParamConfContainerDef, EcucRefType, Module


class SoAdGeneral(EcucParamConfContainerDef):
    """SoAd general configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.soAdDevErrorDetect: bool = None
        self.soAdGetAndResetMeasurementDataApi: bool = None
        self.soAdIPv6AddressEnabled: bool = None
        self.soAdMainFunctionPeriod: float = None
        self.soAdSoConMax: int = None
        self.soAdRoutingGroupMax: int = None
        self.soAdVersionInfoApi: bool = None
        self.soAdTlsEnabled: bool = None
        self.soAdEnableSecurityEventReporting: bool = None

    def getSoAdDevErrorDetect(self) -> bool:
        return self.soAdDevErrorDetect

    def setSoAdDevErrorDetect(self, value: bool):
        if value is not None:
            self.soAdDevErrorDetect = value
        return self

    def getSoAdGetAndResetMeasurementDataApi(self) -> bool:
        return self.soAdGetAndResetMeasurementDataApi

    def setSoAdGetAndResetMeasurementDataApi(self, value: bool):
        if value is not None:
            self.soAdGetAndResetMeasurementDataApi = value
        return self

    def getSoAdIPv6AddressEnabled(self) -> bool:
        return self.soAdIPv6AddressEnabled

    def setSoAdIPv6AddressEnabled(self, value: bool):
        if value is not None:
            self.soAdIPv6AddressEnabled = value
        return self

    def getSoAdMainFunctionPeriod(self) -> float:
        return self.soAdMainFunctionPeriod

    def setSoAdMainFunctionPeriod(self, value: float):
        if value is not None:
            self.soAdMainFunctionPeriod = value
        return self

    def getSoAdSoConMax(self) -> int:
        return self.soAdSoConMax

    def setSoAdSoConMax(self, value: int):
        if value is not None:
            self.soAdSoConMax = value
        return self

    def getSoAdRoutingGroupMax(self) -> int:
        return self.soAdRoutingGroupMax

    def setSoAdRoutingGroupMax(self, value: int):
        if value is not None:
            self.soAdRoutingGroupMax = value
        return self

    def getSoAdVersionInfoApi(self) -> bool:
        return self.soAdVersionInfoApi

    def setSoAdVersionInfoApi(self, value: bool):
        if value is not None:
            self.soAdVersionInfoApi = value
        return self

    def getSoAdTlsEnabled(self) -> bool:
        return self.soAdTlsEnabled

    def setSoAdTlsEnabled(self, value: bool):
        if value is not None:
            self.soAdTlsEnabled = value
        return self

    def getSoAdEnableSecurityEventReporting(self) -> bool:
        return self.soAdEnableSecurityEventReporting

    def setSoAdEnableSecurityEventReporting(self, value: bool):
        if value is not None:
            self.soAdEnableSecurityEventReporting = value
        return self


class SoAdSocketRemoteAddress(EcucParamConfContainerDef):
    """SoAd socket remote address configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.soAdSocketRemotePort: int = None

    def getSoAdSocketRemotePort(self) -> int:
        return self.soAdSocketRemotePort

    def setSoAdSocketRemotePort(self, value: int):
        if value is not None:
            self.soAdSocketRemotePort = value
        return self


class SoAdSocketUdp(EcucParamConfContainerDef):
    """SoAd socket UDP configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.soAdTxBufferPoolSize: int = None

    def getSoAdTxBufferPoolSize(self) -> int:
        return self.soAdTxBufferPoolSize

    def setSoAdTxBufferPoolSize(self, value: int):
        if value is not None:
            self.soAdTxBufferPoolSize = value
        return self


class SoAdSocketTcp(EcucParamConfContainerDef):
    """SoAd socket TCP configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.soAdSocketTcpInitiate: bool = None
        self.soAdSocketTcpKeepAlive: bool = None
        self.soAdSocketTcpKeepAliveTime: float = None
        self.soAdSocketTcpNoDelay: bool = None
        self.soAdSocketTcpTxQuota: int = None
        self.soAdTlsConnectionRef: EcucRefType = None
        self.soAdDatagramTlsConnectionRef: EcucRefType = None

    def getSoAdSocketTcpInitiate(self) -> bool:
        return self.soAdSocketTcpInitiate

    def setSoAdSocketTcpInitiate(self, value: bool):
        if value is not None:
            self.soAdSocketTcpInitiate = value
        return self

    def getSoAdSocketTcpKeepAlive(self) -> bool:
        return self.soAdSocketTcpKeepAlive

    def setSoAdSocketTcpKeepAlive(self, value: bool):
        if value is not None:
            self.soAdSocketTcpKeepAlive = value
        return self

    def getSoAdSocketTcpKeepAliveTime(self) -> float:
        return self.soAdSocketTcpKeepAliveTime

    def setSoAdSocketTcpKeepAliveTime(self, value: float):
        if value is not None:
            self.soAdSocketTcpKeepAliveTime = value
        return self

    def getSoAdSocketTcpNoDelay(self) -> bool:
        return self.soAdSocketTcpNoDelay

    def setSoAdSocketTcpNoDelay(self, value: bool):
        if value is not None:
            self.soAdSocketTcpNoDelay = value
        return self

    def getSoAdSocketTcpTxQuota(self) -> int:
        return self.soAdSocketTcpTxQuota

    def setSoAdSocketTcpTxQuota(self, value: int):
        if value is not None:
            self.soAdSocketTcpTxQuota = value
        return self

    def getSoAdTlsConnectionRef(self) -> EcucRefType:
        return self.soAdTlsConnectionRef

    def setSoAdTlsConnectionRef(self, value: EcucRefType):
        if value is not None:
            self.soAdTlsConnectionRef = value
        return self

    def getSoAdDatagramTlsConnectionRef(self) -> EcucRefType:
        return self.soAdDatagramTlsConnectionRef

    def setSoAdDatagramTlsConnectionRef(self, value: EcucRefType):
        if value is not None:
            self.soAdDatagramTlsConnectionRef = value
        return self


class SoAdSocketConnection(EcucParamConfContainerDef):
    """SoAd socket connection configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.soAdSocketId: int = None
        self.soAdSocketRemoteAddress: SoAdSocketRemoteAddress = None
        self.soAdSocketUdpListenOnly: bool = None
        self.soAdSocketUdp: SoAdSocketUdp = None
        self.soAdSocketTcp: SoAdSocketTcp = None

    def getSoAdSocketId(self) -> int:
        return self.soAdSocketId

    def setSoAdSocketId(self, value: int):
        if value is not None:
            self.soAdSocketId = value
        return self

    def getSoAdSocketRemoteAddress(self) -> SoAdSocketRemoteAddress:
        return self.soAdSocketRemoteAddress

    def setSoAdSocketRemoteAddress(self, value: SoAdSocketRemoteAddress):
        if value is not None:
            self.soAdSocketRemoteAddress = value
        return self

    def getSoAdSocketUdpListenOnly(self) -> bool:
        return self.soAdSocketUdpListenOnly

    def setSoAdSocketUdpListenOnly(self, value: bool):
        if value is not None:
            self.soAdSocketUdpListenOnly = value
        return self

    def getSoAdSocketUdp(self) -> SoAdSocketUdp:
        return self.soAdSocketUdp

    def setSoAdSocketUdp(self, value: SoAdSocketUdp):
        if value is not None:
            self.soAdSocketUdp = value
        return self

    def getSoAdSocketTcp(self) -> SoAdSocketTcp:
        return self.soAdSocketTcp

    def setSoAdSocketTcp(self, value: SoAdSocketTcp):
        if value is not None:
            self.soAdSocketTcp = value
        return self


class SoAdSocketConnectionGroup(EcucParamConfContainerDef):
    """SoAd socket connection group configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.soAdSocketLocalPort: int = None
        self.soAdSocketTpRxBufferMin: int = None
        self.soAdSocketFramePriority: int = None
        self.soAdSocketConnections: List[SoAdSocketConnection] = []

    def getSoAdSocketLocalPort(self) -> int:
        return self.soAdSocketLocalPort

    def setSoAdSocketLocalPort(self, value: int):
        if value is not None:
            self.soAdSocketLocalPort = value
        return self

    def getSoAdSocketTpRxBufferMin(self) -> int:
        return self.soAdSocketTpRxBufferMin

    def setSoAdSocketTpRxBufferMin(self, value: int):
        if value is not None:
            self.soAdSocketTpRxBufferMin = value
        return self

    def getSoAdSocketFramePriority(self) -> int:
        return self.soAdSocketFramePriority

    def setSoAdSocketFramePriority(self, value: int):
        if value is not None:
            self.soAdSocketFramePriority = value
        return self

    def getSoAdSocketConnectionList(self) -> List[SoAdSocketConnection]:
        return list(sorted(filter(lambda a: isinstance(a, SoAdSocketConnection), self.elements.values()), key=lambda o: o.getName()))

    def addSoAdSocketConnection(self, value: SoAdSocketConnection):
        self.addElement(value)
        self.soAdSocketConnections.append(value)
        return self


class SoAdPduRouteDest(EcucParamConfContainerDef):
    """SoAd PDU route destination configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.soAdTxPduHeaderId: int = None
        self.soAdTxUdpTriggerMode: str = None
        self.soAdTxUdpTriggerTimeout: float = None
        self.soAdTxSocketConnOrSocketConnBundleRef: EcucRefType = None

    def getSoAdTxPduHeaderId(self) -> int:
        return self.soAdTxPduHeaderId

    def setSoAdTxPduHeaderId(self, value: int):
        if value is not None:
            self.soAdTxPduHeaderId = value
        return self

    def getSoAdTxUdpTriggerMode(self) -> str:
        return self.soAdTxUdpTriggerMode

    def setSoAdTxUdpTriggerMode(self, value: str):
        if value is not None:
            self.soAdTxUdpTriggerMode = value
        return self

    def getSoAdTxUdpTriggerTimeout(self) -> float:
        return self.soAdTxUdpTriggerTimeout

    def setSoAdTxUdpTriggerTimeout(self, value: float):
        if value is not None:
            self.soAdTxUdpTriggerTimeout = value
        return self

    def getSoAdTxSocketConnOrSocketConnBundleRef(self) -> EcucRefType:
        return self.soAdTxSocketConnOrSocketConnBundleRef

    def setSoAdTxSocketConnOrSocketConnBundleRef(self, value: EcucRefType):
        if value is not None:
            self.soAdTxSocketConnOrSocketConnBundleRef = value
        return self


class SoAdPduRoute(EcucParamConfContainerDef):
    """SoAd PDU route configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.soAdTxPduId: int = None
        self.soAdTxUpperLayerType: str = None
        self.soAdSkipIfTxConfirmation: bool = None
        self.soAdPduHeaderEnable: bool = None
        self.soAdResourceManagementEnable: bool = None
        self.soAdPduRouteDest: SoAdPduRouteDest = None

    def getSoAdTxPduId(self) -> int:
        return self.soAdTxPduId

    def setSoAdTxPduId(self, value: int):
        if value is not None:
            self.soAdTxPduId = value
        return self

    def getSoAdTxUpperLayerType(self) -> str:
        return self.soAdTxUpperLayerType

    def setSoAdTxUpperLayerType(self, value: str):
        if value is not None:
            self.soAdTxUpperLayerType = value
        return self

    def getSoAdSkipIfTxConfirmation(self) -> bool:
        return self.soAdSkipIfTxConfirmation

    def setSoAdSkipIfTxConfirmation(self, value: bool):
        if value is not None:
            self.soAdSkipIfTxConfirmation = value
        return self

    def getSoAdPduHeaderEnable(self) -> bool:
        return self.soAdPduHeaderEnable

    def setSoAdPduHeaderEnable(self, value: bool):
        if value is not None:
            self.soAdPduHeaderEnable = value
        return self

    def getSoAdResourceManagementEnable(self) -> bool:
        return self.soAdResourceManagementEnable

    def setSoAdResourceManagementEnable(self, value: bool):
        if value is not None:
            self.soAdResourceManagementEnable = value
        return self

    def getSoAdPduRouteDest(self) -> SoAdPduRouteDest:
        return self.soAdPduRouteDest

    def setSoAdPduRouteDest(self, value: SoAdPduRouteDest):
        if value is not None:
            self.soAdPduRouteDest = value
        return self


class SoAdSocketRouteDest(EcucParamConfContainerDef):
    """SoAd socket route destination configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.soAdRxPduHeaderId: int = None
        self.soAdRxPduId: int = None
        self.soAdRxUpperLayerType: str = None
        self.soAdRxSocketConnOrSocketConnBundleRef: EcucRefType = None
        self.soAdRxPduRef: EcucRefType = None

    def getSoAdRxPduHeaderId(self) -> int:
        return self.soAdRxPduHeaderId

    def setSoAdRxPduHeaderId(self, value: int):
        if value is not None:
            self.soAdRxPduHeaderId = value
        return self

    def getSoAdRxPduId(self) -> int:
        return self.soAdRxPduId

    def setSoAdRxPduId(self, value: int):
        if value is not None:
            self.soAdRxPduId = value
        return self

    def getSoAdRxUpperLayerType(self) -> str:
        return self.soAdRxUpperLayerType

    def setSoAdRxUpperLayerType(self, value: str):
        if value is not None:
            self.soAdRxUpperLayerType = value
        return self

    def getSoAdRxSocketConnOrSocketConnBundleRef(self) -> EcucRefType:
        return self.soAdRxSocketConnOrSocketConnBundleRef

    def setSoAdRxSocketConnOrSocketConnBundleRef(self, value: EcucRefType):
        if value is not None:
            self.soAdRxSocketConnOrSocketConnBundleRef = value
        return self

    def getSoAdRxPduRef(self) -> EcucRefType:
        return self.soAdRxPduRef

    def setSoAdRxPduRef(self, value: EcucRefType):
        if value is not None:
            self.soAdRxPduRef = value
        return self


class SoAdSocketRoute(EcucParamConfContainerDef):
    """SoAd socket route configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.soAdSocketRouteDest: SoAdSocketRouteDest = None

    def getSoAdSocketRouteDest(self) -> SoAdSocketRouteDest:
        return self.soAdSocketRouteDest

    def setSoAdSocketRouteDest(self, value: SoAdSocketRouteDest):
        if value is not None:
            self.soAdSocketRouteDest = value
        return self


class SoAdRoutingGroup(EcucParamConfContainerDef):
    """SoAd routing group configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.soAdRoutingGroupId: int = None

    def getSoAdRoutingGroupId(self) -> int:
        return self.soAdRoutingGroupId

    def setSoAdRoutingGroupId(self, value: int):
        if value is not None:
            self.soAdRoutingGroupId = value
        return self


class SoAd(Module):
    """SoAd module model."""
    def __init__(self, parent) -> None:
        super().__init__(parent, "SoAd")

        self.soAdGeneral: SoAdGeneral = None
        self.soAdSocketConnectionGroups: List[SoAdSocketConnectionGroup] = []
        self.soAdPduRoutes: List[SoAdPduRoute] = []
        self.soAdSocketRoutes: List[SoAdSocketRoute] = []
        self.soAdRoutingGroups: List[SoAdRoutingGroup] = []

        self.logger = logging.getLogger()

    def getSoAdGeneral(self) -> SoAdGeneral:
        return self.soAdGeneral

    def setSoAdGeneral(self, value: SoAdGeneral):
        if value is not None:
            self.soAdGeneral = value
        return self

    def getSoAdSocketConnectionGroupList(self) -> List[SoAdSocketConnectionGroup]:
        return list(sorted(filter(lambda a: isinstance(a, SoAdSocketConnectionGroup), self.elements.values()), key=lambda o: o.getName()))

    def addSoAdSocketConnectionGroup(self, value: SoAdSocketConnectionGroup):
        self.addElement(value)
        self.soAdSocketConnectionGroups.append(value)
        return self

    def getSoAdPduRouteList(self) -> List[SoAdPduRoute]:
        return list(sorted(filter(lambda a: isinstance(a, SoAdPduRoute), self.elements.values()), key=lambda o: o.getName()))

    def addSoAdPduRoute(self, value: SoAdPduRoute):
        self.addElement(value)
        self.soAdPduRoutes.append(value)
        return self

    def getSoAdSocketRouteList(self) -> List[SoAdSocketRoute]:
        return list(sorted(filter(lambda a: isinstance(a, SoAdSocketRoute), self.elements.values()), key=lambda o: o.getName()))

    def addSoAdSocketRoute(self, value: SoAdSocketRoute):
        self.addElement(value)
        self.soAdSocketRoutes.append(value)
        return self

    def getSoAdRoutingGroupList(self) -> List[SoAdRoutingGroup]:
        return list(sorted(filter(lambda a: isinstance(a, SoAdRoutingGroup), self.elements.values()), key=lambda o: o.getName()))

    def addSoAdRoutingGroup(self, value: SoAdRoutingGroup):
        self.addElement(value)
        self.soAdRoutingGroups.append(value)
        return self
