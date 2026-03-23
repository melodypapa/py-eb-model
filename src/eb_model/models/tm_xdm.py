from typing import List
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module  # noqa F401


class TmGeneral(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.tmDevErrorDetect: bool = None
        self.tmMainWindowProtect: bool = None

    def getTmDevErrorDetect(self) -> bool:
        return self.tmDevErrorDetect

    def setTmDevErrorDetect(self, value: bool):
        if value is not None:
            self.tmDevErrorDetect = value
        return self

    def getTmMainWindowProtect(self) -> bool:
        return self.tmMainWindowProtect

    def setTmMainWindowProtect(self, value: bool):
        if value is not None:
            self.tmMainWindowProtect = value
        return self


class TmInterruptSynchronization(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.tmSyncMode: str = None

    def getTmSyncMode(self) -> str:
        return self.tmSyncMode

    def setTmSyncMode(self, value: str):
        if value is not None:
            self.tmSyncMode = value
        return self


class TmTickTime(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.tmTickTimeBase: int = None
        self.tmTickPriority: int = None

    def getTmTickTimeBase(self) -> int:
        return self.tmTickTimeBase

    def setTmTickTimeBase(self, value: int):
        if value is not None:
            self.tmTickTimeBase = value
        return self

    def getTmTickPriority(self) -> int:
        return self.tmTickPriority

    def setTmTickPriority(self, value: int):
        if value is not None:
            self.tmTickPriority = value
        return self


class TmTrigger(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.tmTriggerChannelRef: EcucRefType = None

    def getTmTriggerChannelRef(self) -> EcucRefType:
        return self.tmTriggerChannelRef

    def setTmTriggerChannelRef(self, value: EcucRefType):
        if value is not None:
            self.tmTriggerChannelRef = value
        return self


class Tm(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "Tm")

        self.tmGeneral: TmGeneral = None
        self.tmInterruptSynchronization: TmInterruptSynchronization = None
        self.tmTickTime: TmTickTime = None
        self.tmTriggers: List[TmTrigger] = []

        self.logger = logging.getLogger()

    def getTmGeneral(self) -> TmGeneral:
        return self.tmGeneral

    def setTmGeneral(self, value: TmGeneral):
        if value is not None:
            self.tmGeneral = value
        return self

    def getTmInterruptSynchronization(self) -> TmInterruptSynchronization:
        return self.tmInterruptSynchronization

    def setTmInterruptSynchronization(self, value: TmInterruptSynchronization):
        if value is not None:
            self.tmInterruptSynchronization = value
        return self

    def getTmTickTime(self) -> TmTickTime:
        return self.tmTickTime

    def setTmTickTime(self, value: TmTickTime):
        if value is not None:
            self.tmTickTime = value
        return self

    def getTmTriggerList(self) -> List[TmTrigger]:
        return list(sorted(filter(lambda a: isinstance(a, TmTrigger), self.elements.values()), key=lambda o: o.getName()))

    def addTmTrigger(self, value: TmTrigger):
        self.addElement(value)
        self.tmTriggers.append(value)
        return self
