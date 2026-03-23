from typing import List
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module  # noqa F401


class DetErrorHook(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.detErrorHookCallbackName: str = None

    def getDetErrorHookCallbackName(self) -> str:
        return self.detErrorHookCallbackName

    def setDetErrorHookCallbackName(self, value: str):
        if value is not None:
            self.detErrorHookCallbackName = value
        return self


class DetInitError(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.detInitErrorRef: EcucRefType = None

    def getDetInitErrorRef(self) -> EcucRefType:
        return self.detInitErrorRef

    def setDetInitErrorRef(self, value: EcucRefType):
        if value is not None:
            self.detInitErrorRef = value
        return self


class DetGeneral(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.detDevErrorDetect: bool = None
        self.detEnabled: bool = None

    def getDetDevErrorDetect(self) -> bool:
        return self.detDevErrorDetect

    def setDetDevErrorDetect(self, value: bool):
        if value is not None:
            self.detDevErrorDetect = value
        return self

    def getDetEnabled(self) -> bool:
        return self.detEnabled

    def setDetEnabled(self, value: bool):
        if value is not None:
            self.detEnabled = value
        return self


class Det(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "Det")

        self.detGeneral: DetGeneral = None
        self.detErrorHook: DetErrorHook = None
        self.detInitError: DetInitError = None

        self.logger = logging.getLogger()

    def getDetGeneral(self) -> DetGeneral:
        return self.detGeneral

    def setDetGeneral(self, value: DetGeneral):
        if value is not None:
            self.detGeneral = value
        return self

    def getDetErrorHook(self) -> DetErrorHook:
        return self.detErrorHook

    def setDetErrorHook(self, value: DetErrorHook):
        if value is not None:
            self.detErrorHook = value
        return self

    def getDetInitError(self) -> DetInitError:
        return self.detInitError

    def setDetInitError(self, value: DetInitError):
        if value is not None:
            self.detInitError = value
        return self
