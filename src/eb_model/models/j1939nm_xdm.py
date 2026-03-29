"""
J1939Nm Model Module - Represents AUTOSAR J1939Nm configuration.

Implements:
    - SWR_J1939NM_00001: J1939Nm module model
    - SWR_J1939NM_00002: General configuration
"""
from typing import List, Optional
import logging
from .abstract import EcucParamConfContainerDef, EcucRefType, Module


class J1939NmGeneral(EcucParamConfContainerDef):
    """
    General configuration for J1939Nm module.

    Implements: SWR_J1939NM_00002 (General configuration)
    """

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.j1939NmDevErrorDetect: bool = None
        self.j1939NmEnabled: bool = None

    def getJ1939NmDevErrorDetect(self) -> bool:
        return self.j1939NmDevErrorDetect

    def setJ1939NmDevErrorDetect(self, value: bool):
        if value is not None:
            self.j1939NmDevErrorDetect = value
        return self

    def getJ1939NmEnabled(self) -> bool:
        return self.j1939NmEnabled

    def setJ1939NmEnabled(self, value: bool):
        if value is not None:
            self.j1939NmEnabled = value
        return self


class J1939Nm(Module):
    """
    AUTOSAR J1939Nm module.

    Provides J1939 network management for SAE J1939 protocol.

    Implements: SWR_J1939NM_00001 (J1939Nm Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "J1939Nm")
        self.j1939NmGeneral: J1939NmGeneral = None
        self.logger = logging.getLogger()

    def getJ1939NmGeneral(self) -> J1939NmGeneral:
        return self.j1939NmGeneral

    def setJ1939NmGeneral(self, value: J1939NmGeneral):
        if value is not None:
            self.j1939NmGeneral = value
        return self