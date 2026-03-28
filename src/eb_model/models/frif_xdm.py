from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class FrIfGeneral(EcucParamConfContainerDef):
    """FrIf general configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frIfDevErrorDetect: bool = None
        self.frIfMainFunctionPeriod: float = None
        self.frIfMaxNumOfClusters: int = None
        self.frIfSupportFrApi: str = None
        self.frIfPolarizationSelection: bool = None
        self.frIfTransceiverAssignment: bool = None
        self.frIfWakeupPatternSupport: bool = None
        self.frIfVTPSupport: bool = None
        self.frIfPublicHandleTypeEnum: str = None
        self.frIfRelocatablePbcfgEnable: bool = None

    def getFrIfDevErrorDetect(self) -> bool:
        return self.frIfDevErrorDetect

    def setFrIfDevErrorDetect(self, value: bool):
        if value is not None:
            self.frIfDevErrorDetect = value
        return self

    def getFrIfMainFunctionPeriod(self) -> float:
        return self.frIfMainFunctionPeriod

    def setFrIfMainFunctionPeriod(self, value: float):
        if value is not None:
            self.frIfMainFunctionPeriod = value
        return self

    def getFrIfMaxNumOfClusters(self) -> int:
        return self.frIfMaxNumOfClusters

    def setFrIfMaxNumOfClusters(self, value: int):
        if value is not None:
            self.frIfMaxNumOfClusters = value
        return self

    def getFrIfSupportFrApi(self) -> str:
        return self.frIfSupportFrApi

    def setFrIfSupportFrApi(self, value: str):
        if value is not None:
            self.frIfSupportFrApi = value
        return self

    def getFrIfPolarizationSelection(self) -> bool:
        return self.frIfPolarizationSelection

    def setFrIfPolarizationSelection(self, value: bool):
        if value is not None:
            self.frIfPolarizationSelection = value
        return self

    def getFrIfTransceiverAssignment(self) -> bool:
        return self.frIfTransceiverAssignment

    def setFrIfTransceiverAssignment(self, value: bool):
        if value is not None:
            self.frIfTransceiverAssignment = value
        return self

    def getFrIfWakeupPatternSupport(self) -> bool:
        return self.frIfWakeupPatternSupport

    def setFrIfWakeupPatternSupport(self, value: bool):
        if value is not None:
            self.frIfWakeupPatternSupport = value
        return self

    def getFrIfVTPSupport(self) -> bool:
        return self.frIfVTPSupport

    def setFrIfVTPSupport(self, value: bool):
        if value is not None:
            self.frIfVTPSupport = value
        return self

    def getFrIfPublicHandleTypeEnum(self) -> str:
        return self.frIfPublicHandleTypeEnum

    def setFrIfPublicHandleTypeEnum(self, value: str):
        if value is not None:
            self.frIfPublicHandleTypeEnum = value
        return self

    def getFrIfRelocatablePbcfgEnable(self) -> bool:
        return self.frIfRelocatablePbcfgEnable

    def setFrIfRelocatablePbcfgEnable(self, value: bool):
        if value is not None:
            self.frIfRelocatablePbcfgEnable = value
        return self


class FrIfCluster(EcucParamConfContainerDef):
    """FrIf cluster configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class FrIfController(EcucParamConfContainerDef):
    """FrIf controller configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frIfCtrlIdx: int = None
        self.frIfCtrlMtu: int = None

    def getFrIfCtrlIdx(self) -> int:
        return self.frIfCtrlIdx

    def setFrIfCtrlIdx(self, value: int):
        if value is not None:
            self.frIfCtrlIdx = value
        return self

    def getFrIfCtrlMtu(self) -> int:
        return self.frIfCtrlMtu

    def setFrIfCtrlMtu(self, value: int):
        if value is not None:
            self.frIfCtrlMtu = value
        return self


class FrIf(Module):
    """FrIf module model."""
    def __init__(self, parent) -> None:
        super().__init__(parent, "FrIf")

        self.frIfGeneral: FrIfGeneral = None
        self.frIfClusters: List[FrIfCluster] = []
        self.frIfControllers: List[FrIfController] = []

        self.logger = logging.getLogger()

    def getFrIfGeneral(self) -> FrIfGeneral:
        return self.frIfGeneral

    def setFrIfGeneral(self, value: FrIfGeneral):
        if value is not None:
            self.frIfGeneral = value
        return self

    def getFrIfClusterList(self) -> List[FrIfCluster]:
        return list(sorted(filter(lambda a: isinstance(a, FrIfCluster), self.elements.values()), key=lambda o: o.getName()))

    def addFrIfCluster(self, value: FrIfCluster):
        self.addElement(value)
        self.frIfClusters.append(value)
        return self

    def getFrIfControllerList(self) -> List[FrIfController]:
        return list(sorted(filter(lambda a: isinstance(a, FrIfController), self.elements.values()), key=lambda o: o.getName()))

    def addFrIfController(self, value: FrIfController):
        self.addElement(value)
        self.frIfControllers.append(value)
        return self
