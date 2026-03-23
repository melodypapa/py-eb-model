from typing import List
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module  # noqa F401


class EcuMStartup(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumEnableUserMcuStartup: bool = None
        self.ecumUserMcuStartupRef: EcucRefType = None

    def getEcumEnableUserMcuStartup(self) -> bool:
        return self.ecumEnableUserMcuStartup

    def setEcumEnableUserMcuStartup(self, value: bool):
        if value is not None:
            self.ecumEnableUserMcuStartup = value
        return self

    def getEcumUserMcuStartupRef(self) -> EcucRefType:
        return self.ecumUserMcuStartupRef

    def setEcumUserMcuStartupRef(self, value: EcucRefType):
        if value is not None:
            self.ecumUserMcuStartupRef = value
        return self


class EcuMShutdown(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumEnableUserMcuShutdown: bool = None
        self.ecumUserMcuShutdownRef: EcucRefType = None

    def getEcumEnableUserMcuShutdown(self) -> bool:
        return self.ecumEnableUserMcuShutdown

    def setEcumEnableUserMcuShutdown(self, value: bool):
        if value is not None:
            self.ecumEnableUserMcuShutdown = value
        return self

    def getEcumUserMcuShutdownRef(self) -> EcucRefType:
        return self.ecumUserMcuShutdownRef

    def setEcumUserMcuShutdownRef(self, value: EcucRefType):
        if value is not None:
            self.ecumUserMcuShutdownRef = value
        return self


class EcuMAlarm(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumAlarmCounterRef: EcucRefType = None
        self.ecumAlarmActionRef: EcucRefType = None

    def getEcumAlarmCounterRef(self) -> EcucRefType:
        return self.ecumAlarmCounterRef

    def setEcumAlarmCounterRef(self, value: EcucRefType):
        if value is not None:
            self.ecumAlarmCounterRef = value
        return self

    def getEcumAlarmActionRef(self) -> EcucRefType:
        return self.ecumAlarmActionRef

    def setEcumAlarmActionRef(self, value: EcucRefType):
        if value is not None:
            self.ecumAlarmActionRef = value
        return self


class EcuMGeneral(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumDevErrorDetect: bool = None
        self.ecumConfigurationVariant: str = None

    def getEcumDevErrorDetect(self) -> bool:
        return self.ecumDevErrorDetect

    def setEcumDevErrorDetect(self, value: bool):
        if value is not None:
            self.ecumDevErrorDetect = value
        return self

    def getEcumConfigurationVariant(self) -> str:
        return self.ecumConfigurationVariant

    def setEcumConfigurationVariant(self, value: str):
        if value is not None:
            self.ecumConfigurationVariant = value
        return self


class EcuM(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "EcuM")

        self.ecumGeneral: EcuMGeneral = None
        self.ecumStartup: EcuMStartup = None
        self.ecumShutdown: EcuMShutdown = None
        self.ecumAlarms: List[EcuMAlarm] = []

        self.logger = logging.getLogger()

    def getEcumGeneral(self) -> EcuMGeneral:
        return self.ecumGeneral

    def setEcumGeneral(self, value: EcuMGeneral):
        if value is not None:
            self.ecumGeneral = value
        return self

    def getEcumStartup(self) -> EcuMStartup:
        return self.ecumStartup

    def setEcumStartup(self, value: EcuMStartup):
        if value is not None:
            self.ecumStartup = value
        return self

    def getEcumShutdown(self) -> EcuMShutdown:
        return self.ecumShutdown

    def setEcumShutdown(self, value: EcuMShutdown):
        if value is not None:
            self.ecumShutdown = value
        return self

    def getEcumAlarmList(self) -> List[EcuMAlarm]:
        return list(sorted(filter(lambda a: isinstance(a, EcuMAlarm), self.elements.values()), key=lambda o: o.getName()))

    def addEcumAlarm(self, value: EcuMAlarm):
        self.addElement(value)
        self.ecumAlarms.append(value)
        return self
