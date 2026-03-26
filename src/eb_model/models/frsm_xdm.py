from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class FrSMGeneral(EcucParamConfContainerDef):
    """FrSM general configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frSMDevErrorDetect: bool = None
        self.frSMSyncLossErrorIndicationName: str = None
        self.frSMVersionInfoApi: bool = None
        self.frSMFrTrcvControlEnable: bool = None
        self.frSMComMIndicationEnable: bool = None
        self.frSMSingleClstOptEnable: bool = None
        self.frSMReportToBswMEnable: bool = None
        self.frSMSetEcuPassiveEnable: bool = None
        self.frSMFrNmStartupErrorEnable: bool = None
        self.frSMKeySlotOnlyModeEnable: bool = None
        self.frSMSyncLossErrorIndicationHeaderName: str = None
        self.frSMMultiCoreSupportEnable: bool = None

        # Defensive programming
        self.frSMDefProgEnabled: bool = None
        self.frSMPrecondAssertEnabled: bool = None
        self.frSMPostcondAssertEnabled: bool = None
        self.frSMStaticAssertEnabled: bool = None
        self.frSMUnreachAssertEnabled: bool = None
        self.frSMInvariantAssertEnabled: bool = None

    def getFrSMDevErrorDetect(self) -> bool:
        return self.frSMDevErrorDetect

    def setFrSMDevErrorDetect(self, value: bool):
        if value is not None:
            self.frSMDevErrorDetect = value
        return self

    def getFrSMSyncLossErrorIndicationName(self) -> str:
        return self.frSMSyncLossErrorIndicationName

    def setFrSMSyncLossErrorIndicationName(self, value: str):
        if value is not None:
            self.frSMSyncLossErrorIndicationName = value
        return self

    def getFrSMVersionInfoApi(self) -> bool:
        return self.frSMVersionInfoApi

    def setFrSMVersionInfoApi(self, value: bool):
        if value is not None:
            self.frSMVersionInfoApi = value
        return self

    def getFrSMFrTrcvControlEnable(self) -> bool:
        return self.frSMFrTrcvControlEnable

    def setFrSMFrTrcvControlEnable(self, value: bool):
        if value is not None:
            self.frSMFrTrcvControlEnable = value
        return self

    def getFrSMComMIndicationEnable(self) -> bool:
        return self.frSMComMIndicationEnable

    def setFrSMComMIndicationEnable(self, value: bool):
        if value is not None:
            self.frSMComMIndicationEnable = value
        return self

    def getFrSMSingleClstOptEnable(self) -> bool:
        return self.frSMSingleClstOptEnable

    def setFrSMSingleClstOptEnable(self, value: bool):
        if value is not None:
            self.frSMSingleClstOptEnable = value
        return self

    def getFrSMReportToBswMEnable(self) -> bool:
        return self.frSMReportToBswMEnable

    def setFrSMReportToBswMEnable(self, value: bool):
        if value is not None:
            self.frSMReportToBswMEnable = value
        return self

    def getFrSMSetEcuPassiveEnable(self) -> bool:
        return self.frSMSetEcuPassiveEnable

    def setFrSMSetEcuPassiveEnable(self, value: bool):
        if value is not None:
            self.frSMSetEcuPassiveEnable = value
        return self

    def getFrSMFrNmStartupErrorEnable(self) -> bool:
        return self.frSMFrNmStartupErrorEnable

    def setFrSMFrNmStartupErrorEnable(self, value: bool):
        if value is not None:
            self.frSMFrNmStartupErrorEnable = value
        return self

    def getFrSMKeySlotOnlyModeEnable(self) -> bool:
        return self.frSMKeySlotOnlyModeEnable

    def setFrSMKeySlotOnlyModeEnable(self, value: bool):
        if value is not None:
            self.frSMKeySlotOnlyModeEnable = value
        return self

    def getFrSMSyncLossErrorIndicationHeaderName(self) -> str:
        return self.frSMSyncLossErrorIndicationHeaderName

    def setFrSMSyncLossErrorIndicationHeaderName(self, value: str):
        if value is not None:
            self.frSMSyncLossErrorIndicationHeaderName = value
        return self

    def getFrSMMultiCoreSupportEnable(self) -> bool:
        return self.frSMMultiCoreSupportEnable

    def setFrSMMultiCoreSupportEnable(self, value: bool):
        if value is not None:
            self.frSMMultiCoreSupportEnable = value
        return self

    # Defensive programming getters/setters
    def getFrSMDefProgEnabled(self) -> bool:
        return self.frSMDefProgEnabled

    def setFrSMDefProgEnabled(self, value: bool):
        if value is not None:
            self.frSMDefProgEnabled = value
        return self

    def getFrSMPrecondAssertEnabled(self) -> bool:
        return self.frSMPrecondAssertEnabled

    def setFrSMPrecondAssertEnabled(self, value: bool):
        if value is not None:
            self.frSMPrecondAssertEnabled = value
        return self

    def getFrSMPostcondAssertEnabled(self) -> bool:
        return self.frSMPostcondAssertEnabled

    def setFrSMPostcondAssertEnabled(self, value: bool):
        if value is not None:
            self.frSMPostcondAssertEnabled = value
        return self

    def getFrSMStaticAssertEnabled(self) -> bool:
        return self.frSMStaticAssertEnabled

    def setFrSMStaticAssertEnabled(self, value: bool):
        if value is not None:
            self.frSMStaticAssertEnabled = value
        return self

    def getFrSMUnreachAssertEnabled(self) -> bool:
        return self.frSMUnreachAssertEnabled

    def setFrSMUnreachAssertEnabled(self, value: bool):
        if value is not None:
            self.frSMUnreachAssertEnabled = value
        return self

    def getFrSMInvariantAssertEnabled(self) -> bool:
        return self.frSMInvariantAssertEnabled

    def setFrSMInvariantAssertEnabled(self, value: bool):
        if value is not None:
            self.frSMInvariantAssertEnabled = value
        return self


class FrSMClusterDemEventParameterRefs(EcucParamConfContainerDef):
    """FrSM cluster DemEventParameterRefs configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frSMClusterStartupRef: EcucRefType = None
        self.frSMClusterSyncLossRef: EcucRefType = None

    def getFrSMClusterStartupRef(self) -> EcucRefType:
        return self.frSMClusterStartupRef

    def setFrSMClusterStartupRef(self, value: EcucRefType):
        if value is not None:
            self.frSMClusterStartupRef = value
        return self

    def getFrSMClusterSyncLossRef(self) -> EcucRefType:
        return self.frSMClusterSyncLossRef

    def setFrSMClusterSyncLossRef(self, value: EcucRefType):
        if value is not None:
            self.frSMClusterSyncLossRef = value
        return self


class FrSMCluster(EcucParamConfContainerDef):
    """FrSM cluster configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frSMCheckWakeupReason: bool = None
        self.frSMDelayStartupWithoutWakeup: bool = None
        self.frSMDurationT1: float = None
        self.frSMDurationT2: float = None
        self.frSMDurationT3: float = None
        self.frSMIsColdstartEcu: bool = None
        self.frSMIsWakeupEcu: bool = None
        self.frSMMainFunctionCycleTime: float = None
        self.frSMMinNumberOfColdstarter: int = None
        self.frSMNumWakeupPatterns: int = None
        self.frSMStartupRepetitions: int = None
        self.frSMStartupRepetitionsWithWakeup: int = None
        self.frSMComMNetworkHandleRef: EcucRefType = None
        self.frSMFrIfClusterRef: EcucRefType = None
        self.frSMClusterDemEventParameterRefs: FrSMClusterDemEventParameterRefs = None

    def getFrSMCheckWakeupReason(self) -> bool:
        return self.frSMCheckWakeupReason

    def setFrSMCheckWakeupReason(self, value: bool):
        if value is not None:
            self.frSMCheckWakeupReason = value
        return self

    def getFrSMDelayStartupWithoutWakeup(self) -> bool:
        return self.frSMDelayStartupWithoutWakeup

    def setFrSMDelayStartupWithoutWakeup(self, value: bool):
        if value is not None:
            self.frSMDelayStartupWithoutWakeup = value
        return self

    def getFrSMDurationT1(self) -> float:
        return self.frSMDurationT1

    def setFrSMDurationT1(self, value: float):
        if value is not None:
            self.frSMDurationT1 = value
        return self

    def getFrSMDurationT2(self) -> float:
        return self.frSMDurationT2

    def setFrSMDurationT2(self, value: float):
        if value is not None:
            self.frSMDurationT2 = value
        return self

    def getFrSMDurationT3(self) -> float:
        return self.frSMDurationT3

    def setFrSMDurationT3(self, value: float):
        if value is not None:
            self.frSMDurationT3 = value
        return self

    def getFrSMIsColdstartEcu(self) -> bool:
        return self.frSMIsColdstartEcu

    def setFrSMIsColdstartEcu(self, value: bool):
        if value is not None:
            self.frSMIsColdstartEcu = value
        return self

    def getFrSMIsWakeupEcu(self) -> bool:
        return self.frSMIsWakeupEcu

    def setFrSMIsWakeupEcu(self, value: bool):
        if value is not None:
            self.frSMIsWakeupEcu = value
        return self

    def getFrSMMainFunctionCycleTime(self) -> float:
        return self.frSMMainFunctionCycleTime

    def setFrSMMainFunctionCycleTime(self, value: float):
        if value is not None:
            self.frSMMainFunctionCycleTime = value
        return self

    def getFrSMMinNumberOfColdstarter(self) -> int:
        return self.frSMMinNumberOfColdstarter

    def setFrSMMinNumberOfColdstarter(self, value: int):
        if value is not None:
            self.frSMMinNumberOfColdstarter = value
        return self

    def getFrSMNumWakeupPatterns(self) -> int:
        return self.frSMNumWakeupPatterns

    def setFrSMNumWakeupPatterns(self, value: int):
        if value is not None:
            self.frSMNumWakeupPatterns = value
        return self

    def getFrSMStartupRepetitions(self) -> int:
        return self.frSMStartupRepetitions

    def setFrSMStartupRepetitions(self, value: int):
        if value is not None:
            self.frSMStartupRepetitions = value
        return self

    def getFrSMStartupRepetitionsWithWakeup(self) -> int:
        return self.frSMStartupRepetitionsWithWakeup

    def setFrSMStartupRepetitionsWithWakeup(self, value: int):
        if value is not None:
            self.frSMStartupRepetitionsWithWakeup = value
        return self

    def getFrSMComMNetworkHandleRef(self) -> EcucRefType:
        return self.frSMComMNetworkHandleRef

    def setFrSMComMNetworkHandleRef(self, value: EcucRefType):
        if value is not None:
            self.frSMComMNetworkHandleRef = value
        return self

    def getFrSMFrIfClusterRef(self) -> EcucRefType:
        return self.frSMFrIfClusterRef

    def setFrSMFrIfClusterRef(self, value: EcucRefType):
        if value is not None:
            self.frSMFrIfClusterRef = value
        return self

    def getFrSMClusterDemEventParameterRefs(self) -> FrSMClusterDemEventParameterRefs:
        return self.frSMClusterDemEventParameterRefs

    def setFrSMClusterDemEventParameterRefs(self, value: FrSMClusterDemEventParameterRefs):
        if value is not None:
            self.frSMClusterDemEventParameterRefs = value
        return self


class FrSM(Module):
    """FrSM module model."""
    def __init__(self, parent) -> None:
        super().__init__(parent, "FrSM")

        self.frSMGeneral: FrSMGeneral = None
        self.frSMClusters: List[FrSMCluster] = []

        self.logger = logging.getLogger()

    def getFrSMGeneral(self) -> FrSMGeneral:
        return self.frSMGeneral

    def setFrSMGeneral(self, value: FrSMGeneral):
        if value is not None:
            self.frSMGeneral = value
        return self

    def getFrSMClusterList(self) -> List[FrSMCluster]:
        return list(sorted(filter(lambda a: isinstance(a, FrSMCluster), self.elements.values()), key=lambda o: o.getName()))

    def addFrSMCluster(self, value: FrSMCluster):
        self.addElement(value)
        self.frSMClusters.append(value)
        return self