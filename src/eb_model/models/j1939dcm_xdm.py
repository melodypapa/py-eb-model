"""
J1939Dcm Model Module - Represents AUTOSAR J1939Dcm configuration.

Implements:
    - SWR_J1939DCM_00001: J1939Dcm module model
    - SWR_J1939DCM_00002: General configuration
"""
from typing import List, Optional
import logging
from .abstract import EcucParamConfContainerDef, EcucRefType, Module


class J1939DcmGeneral(EcucParamConfContainerDef):
    """
    General configuration for J1939Dcm module.

    Implements: SWR_J1939DCM_00002 (General configuration)
    """

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.j1939DcmDevErrorDetect: bool = None
        self.j1939DcmEnabled: bool = None

    def getJ1939DcmDevErrorDetect(self) -> bool:
        return self.j1939DcmDevErrorDetect

    def setJ1939DcmDevErrorDetect(self, value: bool):
        if value is not None:
            self.j1939DcmDevErrorDetect = value
        return self

    def getJ1939DcmEnabled(self) -> bool:
        return self.j1939DcmEnabled

    def setJ1939DcmEnabled(self, value: bool):
        if value is not None:
            self.j1939DcmEnabled = value
        return self


class J1939Dcm(Module):
    """
    AUTOSAR J1939Dcm module.

    Provides J1939 diagnostic communication manager for SAE J1939 protocol.

    Implements: SWR_J1939DCM_00001 (J1939Dcm Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "J1939Dcm")
        self.j1939DcmGeneral: J1939DcmGeneral = None

    def getJ1939DcmGeneral(self) -> J1939DcmGeneral:
        return self.j1939DcmGeneral

    def setJ1939DcmGeneral(self, value: J1939DcmGeneral):
        if value is not None:
            self.j1939DcmGeneral = value
        return self