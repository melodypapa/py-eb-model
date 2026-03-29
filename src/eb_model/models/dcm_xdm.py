"""
Dcm Model Module - Represents AUTOSAR Dcm configuration.

Implements:
    - SWR_DCM_00001: Dcm module model
    - SWR_DCM_00002: General configuration
"""
from typing import List, Optional
import logging
from .abstract import EcucParamConfContainerDef, EcucRefType, Module


class DcmGeneral(EcucParamConfContainerDef):
    """
    General configuration for Dcm module.

    Implements: SWR_DCM_00002 (General configuration)
    """

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.dcmDevErrorDetect: bool = None
        self.dcmEnabled: bool = None

    def getDcmDevErrorDetect(self) -> bool:
        return self.dcmDevErrorDetect

    def setDcmDevErrorDetect(self, value: bool):
        if value is not None:
            self.dcmDevErrorDetect = value
        return self

    def getDcmEnabled(self) -> bool:
        return self.dcmEnabled

    def setDcmEnabled(self, value: bool):
        if value is not None:
            self.dcmEnabled = value
        return self


class Dcm(Module):
    """
    AUTOSAR Dcm module.

    Provides diagnostic communication manager for unified diagnostic services
    and protocol handling.

    Implements: SWR_DCM_00001 (Dcm Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "Dcm")
        self.dcmGeneral: DcmGeneral = None

    def getDcmGeneral(self) -> DcmGeneral:
        return self.dcmGeneral

    def setDcmGeneral(self, value: DcmGeneral):
        if value is not None:
            self.dcmGeneral = value
        return self