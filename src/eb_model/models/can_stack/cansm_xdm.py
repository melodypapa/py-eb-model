from typing import List, Optional
import logging
from eb_model.models.core.abstract import EcucParamConfContainerDef, EcucRefType, Module


class CanSMGeneral(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canSMDevErrorDetect: bool = None
        self.canSMMainFunctionTimePeriod: float = None
        self.canSMPNSupport: bool = None
        self.canSMEnhancedBusOffReporting: bool = None

    def getCanSMDevErrorDetect(self) -> bool:
        return self.canSMDevErrorDetect

    def setCanSMDevErrorDetect(self, value: bool):
        if value is not None:
            self.canSMDevErrorDetect = value
        return self

    def getCanSMMainFunctionTimePeriod(self) -> float:
        return self.canSMMainFunctionTimePeriod

    def setCanSMMainFunctionTimePeriod(self, value: float):
        if value is not None:
            self.canSMMainFunctionTimePeriod = value
        return self

    def getCanSMPNSupport(self) -> bool:
        return self.canSMPNSupport

    def setCanSMPNSupport(self, value: bool):
        if value is not None:
            self.canSMPNSupport = value
        return self

    def getCanSMEnhancedBusOffReporting(self) -> bool:
        return self.canSMEnhancedBusOffReporting

    def setCanSMEnhancedBusOffReporting(self, value: bool):
        if value is not None:
            self.canSMEnhancedBusOffReporting = value
        return self


class CanSMManagerNetwork(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canSMBorCounterL1ToL2: int = None
        self.canSMBorTimeL1: float = None
        self.canSMBorTimeL2: float = None
        self.canSMBorTimeTxEnsured: float = None
        self.canSMBorTxConfirmationPolling: bool = None
        self.canSMActivatePN: bool = None
        self.canSMComMNetworkHandleRef: EcucRefType = None
        self.canSMTransceiverId: EcucRefType = None

    def getCanSMBorCounterL1ToL2(self) -> int:
        return self.canSMBorCounterL1ToL2

    def setCanSMBorCounterL1ToL2(self, value: int):
        if value is not None:
            self.canSMBorCounterL1ToL2 = value
        return self

    def getCanSMBorTimeL1(self) -> float:
        return self.canSMBorTimeL1

    def setCanSMBorTimeL1(self, value: float):
        if value is not None:
            self.canSMBorTimeL1 = value
        return self

    def getCanSMBorTimeL2(self) -> float:
        return self.canSMBorTimeL2

    def setCanSMBorTimeL2(self, value: float):
        if value is not None:
            self.canSMBorTimeL2 = value
        return self

    def getCanSMBorTimeTxEnsured(self) -> float:
        return self.canSMBorTimeTxEnsured

    def setCanSMBorTimeTxEnsured(self, value: float):
        if value is not None:
            self.canSMBorTimeTxEnsured = value
        return self

    def getCanSMBorTxConfirmationPolling(self) -> bool:
        return self.canSMBorTxConfirmationPolling

    def setCanSMBorTxConfirmationPolling(self, value: bool):
        if value is not None:
            self.canSMBorTxConfirmationPolling = value
        return self

    def getCanSMActivatePN(self) -> bool:
        return self.canSMActivatePN

    def setCanSMActivatePN(self, value: bool):
        if value is not None:
            self.canSMActivatePN = value
        return self

    def getCanSMComMNetworkHandleRef(self) -> EcucRefType:
        return self.canSMComMNetworkHandleRef

    def setCanSMComMNetworkHandleRef(self, value: EcucRefType):
        if value is not None:
            self.canSMComMNetworkHandleRef = value
        return self

    def getCanSMTransceiverId(self) -> EcucRefType:
        return self.canSMTransceiverId

    def setCanSMTransceiverId(self, value: EcucRefType):
        if value is not None:
            self.canSMTransceiverId = value
        return self


class CanSMController(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canSMControllerId: EcucRefType = None

    def getCanSMControllerId(self) -> EcucRefType:
        return self.canSMControllerId

    def setCanSMControllerId(self, value: EcucRefType):
        if value is not None:
            self.canSMControllerId = value
        return self


class CanSMDemEventParameterRefs(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canSMBusOffDemEventRef: EcucRefType = None

    def getCanSMBusOffDemEventRef(self) -> EcucRefType:
        return self.canSMBusOffDemEventRef

    def setCanSMBusOffDemEventRef(self, value: EcucRefType):
        if value is not None:
            self.canSMBusOffDemEventRef = value
        return self


class CanSM(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "CanSM")

        self.canSMGeneral: CanSMGeneral = None
        self.canSMManagerNetworks: List[CanSMManagerNetwork] = []
        self.canSMDemEventParameterRefs: CanSMDemEventParameterRefs = None

        self.logger = logging.getLogger()

    def getCanSMGeneral(self) -> CanSMGeneral:
        return self.canSMGeneral

    def setCanSMGeneral(self, value: CanSMGeneral):
        if value is not None:
            self.canSMGeneral = value
        return self

    def getCanSMManagerNetworkList(self) -> List[CanSMManagerNetwork]:
        return list(sorted(filter(lambda a: isinstance(a, CanSMManagerNetwork), self.elements.values()), key=lambda o: o.getName()))

    def addCanSMManagerNetwork(self, value: CanSMManagerNetwork):
        self.addElement(value)
        self.canSMManagerNetworks.append(value)
        return self

    def getCanSMDemEventParameterRefs(self) -> CanSMDemEventParameterRefs:
        return self.canSMDemEventParameterRefs

    def setCanSMDemEventParameterRefs(self, value: CanSMDemEventParameterRefs):
        if value is not None:
            self.canSMDemEventParameterRefs = value
        return self
