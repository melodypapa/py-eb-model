from typing import List, Optional
import logging
from eb_model.models.core.abstract import EcucParamConfContainerDef, EcucRefType, Module


class EthSMGeneral(EcucParamConfContainerDef):
    """EthSM general configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ethSMDevErrorDetect: bool = None
        self.ethSMDummyMode: bool = None
        self.ethSMMainFunctionPeriod: float = None
        self.ethSMVersionInfoApi: bool = None
        self.ethSMSingleNetworkOptEnable: bool = None
        self.ethSMMaxNetworks: int = None
        self.ethSMMultiCoreSupport: bool = None
        self.ethSMDevAuthSupport: bool = None
        self.ethSMRelocatablePbcfgEnable: bool = None

        # Defensive programming
        self.ethSMDefProgEnabled: bool = None
        self.ethSMPrecondAssertEnabled: bool = None
        self.ethSMPostcondAssertEnabled: bool = None
        self.ethSMStaticAssertEnabled: bool = None
        self.ethSMUnreachAssertEnabled: bool = None
        self.ethSMInvariantAssertEnabled: bool = None

    def getEthSMDevErrorDetect(self) -> bool:
        return self.ethSMDevErrorDetect

    def setEthSMDevErrorDetect(self, value: bool):
        if value is not None:
            self.ethSMDevErrorDetect = value
        return self

    def getEthSMDummyMode(self) -> bool:
        return self.ethSMDummyMode

    def setEthSMDummyMode(self, value: bool):
        if value is not None:
            self.ethSMDummyMode = value
        return self

    def getEthSMMainFunctionPeriod(self) -> float:
        return self.ethSMMainFunctionPeriod

    def setEthSMMainFunctionPeriod(self, value: float):
        if value is not None:
            self.ethSMMainFunctionPeriod = value
        return self

    def getEthSMVersionInfoApi(self) -> bool:
        return self.ethSMVersionInfoApi

    def setEthSMVersionInfoApi(self, value: bool):
        if value is not None:
            self.ethSMVersionInfoApi = value
        return self

    def getEthSMSingleNetworkOptEnable(self) -> bool:
        return self.ethSMSingleNetworkOptEnable

    def setEthSMSingleNetworkOptEnable(self, value: bool):
        if value is not None:
            self.ethSMSingleNetworkOptEnable = value
        return self

    def getEthSMMaxNetworks(self) -> int:
        return self.ethSMMaxNetworks

    def setEthSMMaxNetworks(self, value: int):
        if value is not None:
            self.ethSMMaxNetworks = value
        return self

    def getEthSMMultiCoreSupport(self) -> bool:
        return self.ethSMMultiCoreSupport

    def setEthSMMultiCoreSupport(self, value: bool):
        if value is not None:
            self.ethSMMultiCoreSupport = value
        return self

    def getEthSMDevAuthSupport(self) -> bool:
        return self.ethSMDevAuthSupport

    def setEthSMDevAuthSupport(self, value: bool):
        if value is not None:
            self.ethSMDevAuthSupport = value
        return self

    def getEthSMRelocatablePbcfgEnable(self) -> bool:
        return self.ethSMRelocatablePbcfgEnable

    def setEthSMRelocatablePbcfgEnable(self, value: bool):
        if value is not None:
            self.ethSMRelocatablePbcfgEnable = value
        return self

    # Defensive programming getters/setters
    def getEthSMDefProgEnabled(self) -> bool:
        return self.ethSMDefProgEnabled

    def setEthSMDefProgEnabled(self, value: bool):
        if value is not None:
            self.ethSMDefProgEnabled = value
        return self

    def getEthSMPrecondAssertEnabled(self) -> bool:
        return self.ethSMPrecondAssertEnabled

    def setEthSMPrecondAssertEnabled(self, value: bool):
        if value is not None:
            self.ethSMPrecondAssertEnabled = value
        return self

    def getEthSMPostcondAssertEnabled(self) -> bool:
        return self.ethSMPostcondAssertEnabled

    def setEthSMPostcondAssertEnabled(self, value: bool):
        if value is not None:
            self.ethSMPostcondAssertEnabled = value
        return self

    def getEthSMStaticAssertEnabled(self) -> bool:
        return self.ethSMStaticAssertEnabled

    def setEthSMStaticAssertEnabled(self, value: bool):
        if value is not None:
            self.ethSMStaticAssertEnabled = value
        return self

    def getEthSMUnreachAssertEnabled(self) -> bool:
        return self.ethSMUnreachAssertEnabled

    def setEthSMUnreachAssertEnabled(self, value: bool):
        if value is not None:
            self.ethSMUnreachAssertEnabled = value
        return self

    def getEthSMInvariantAssertEnabled(self) -> bool:
        return self.ethSMInvariantAssertEnabled

    def setEthSMInvariantAssertEnabled(self, value: bool):
        if value is not None:
            self.ethSMInvariantAssertEnabled = value
        return self


class EthSMDemEventParameterRefs(EcucParamConfContainerDef):
    """EthSM DemEventParameterRefs configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ethSMDemEventParameterRef: EcucRefType = None

    def getEthSMDemEventParameterRef(self) -> EcucRefType:
        return self.ethSMDemEventParameterRef

    def setEthSMDemEventParameterRef(self, value: EcucRefType):
        if value is not None:
            self.ethSMDemEventParameterRef = value
        return self


class EthSMNetwork(EcucParamConfContainerDef):
    """EthSM network configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ethSMEthIfControllerRef: EcucRefType = None
        self.ethSMComMNetworkHandleRef: EcucRefType = None
        self.ethSMDevAuthNoComNotificationEnable: bool = None
        self.ethSMDemEventParameterRefs: EthSMDemEventParameterRefs = None

    def getEthSMEthIfControllerRef(self) -> EcucRefType:
        return self.ethSMEthIfControllerRef

    def setEthSMEthIfControllerRef(self, value: EcucRefType):
        if value is not None:
            self.ethSMEthIfControllerRef = value
        return self

    def getEthSMComMNetworkHandleRef(self) -> EcucRefType:
        return self.ethSMComMNetworkHandleRef

    def setEthSMComMNetworkHandleRef(self, value: EcucRefType):
        if value is not None:
            self.ethSMComMNetworkHandleRef = value
        return self

    def getEthSMDevAuthNoComNotificationEnable(self) -> bool:
        return self.ethSMDevAuthNoComNotificationEnable

    def setEthSMDevAuthNoComNotificationEnable(self, value: bool):
        if value is not None:
            self.ethSMDevAuthNoComNotificationEnable = value
        return self

    def getEthSMDemEventParameterRefs(self) -> EthSMDemEventParameterRefs:
        return self.ethSMDemEventParameterRefs

    def setEthSMDemEventParameterRefs(self, value: EthSMDemEventParameterRefs):
        if value is not None:
            self.ethSMDemEventParameterRefs = value
        return self


class EthSM(Module):
    """EthSM module model."""
    def __init__(self, parent) -> None:
        super().__init__(parent, "EthSM")

        self.ethSMGeneral: EthSMGeneral = None
        self.ethSMNetworks: List[EthSMNetwork] = []

        self.logger = logging.getLogger()

    def getEthSMGeneral(self) -> EthSMGeneral:
        return self.ethSMGeneral

    def setEthSMGeneral(self, value: EthSMGeneral):
        if value is not None:
            self.ethSMGeneral = value
        return self

    def getEthSMNetworkList(self) -> List[EthSMNetwork]:
        return list(sorted(filter(lambda a: isinstance(a, EthSMNetwork), self.elements.values()), key=lambda o: o.getName()))

    def addEthSMNetwork(self, value: EthSMNetwork):
        self.addElement(value)
        self.ethSMNetworks.append(value)
        return self
