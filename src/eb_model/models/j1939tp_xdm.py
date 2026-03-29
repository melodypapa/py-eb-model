"""
J1939Tp Model Module - Represents AUTOSAR J1939Tp configuration.

Implements:
    - SWR_J1939TP_00001: J1939Tp module model
    - SWR_J1939TP_00002: General configuration
"""
from typing import List, Optional
import logging
from .abstract import EcucParamConfContainerDef, EcucRefType, Module


class J1939TpGeneral(EcucParamConfContainerDef):
    """
    General configuration for J1939Tp module.

    Implements: SWR_J1939TP_00002 (General configuration)
    """

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.j1939TpDevErrorDetect: bool = None
        self.j1939TpEnabled: bool = None

    def getJ1939TpDevErrorDetect(self) -> bool:
        return self.j1939TpDevErrorDetect

    def setJ1939TpDevErrorDetect(self, value: bool):
        if value is not None:
            self.j1939TpDevErrorDetect = value
        return self

    def getJ1939TpEnabled(self) -> bool:
        return self.j1939TpEnabled

    def setJ1939TpEnabled(self, value: bool):
        if value is not None:
            self.j1939TpEnabled = value
        return self


class J1939Tp(Module):
    """
    AUTOSAR J1939Tp module.

    Provides J1939 transport protocol for SAE J1939 protocol.

    Implements: SWR_J1939TP_00001 (J1939Tp Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "J1939Tp")
        self.j1939TpGeneral: J1939TpGeneral = None

    def getJ1939TpGeneral(self) -> J1939TpGeneral:
        return self.j1939TpGeneral

    def setJ1939TpGeneral(self, value: J1939TpGeneral):
        if value is not None:
            self.j1939TpGeneral = value
        return self