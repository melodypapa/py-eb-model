from typing import List
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module  # noqa F401


class ComGeneral(EcucParamConfContainerDef):
    """
    General COM configuration parameters.

    Implements: SWR_COM_00002 (ComGeneral configuration)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.comEnableUserSupport: bool = None
        self.comUserInitSignal: bool = None

    def getComEnableUserSupport(self) -> bool:
        return self.comEnableUserSupport

    def setComEnableUserSupport(self, value: bool):
        if value is not None:
            self.comEnableUserSupport = value
        return self

    def getComUserInitSignal(self) -> bool:
        return self.comUserInitSignal

    def setComUserInitSignal(self, value: bool):
        if value is not None:
            self.comUserInitSignal = value
        return self


class Com(Module):
    """
    AUTOSAR COM (Communication) module configuration.

    Implements: SWR_COM_00001 (Com Module Parser)
    """
    def __init__(self, parent) -> None:
        super().__init__(parent, "Com")

        self.comGeneral: ComGeneral = None

        self.logger = logging.getLogger()

    def getComGeneral(self) -> ComGeneral:
        return self.comGeneral

    def setComGeneral(self, value: ComGeneral):
        if value is not None:
            self.comGeneral = value
        return self
