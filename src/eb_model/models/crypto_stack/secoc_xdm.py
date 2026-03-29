"""
SecOC XDM Model Module - Represents AUTOSAR SecOC configuration.

Implements:
    - SWR_SECOC_00001: SecOC module model
    - SWR_SECOC_00002: General configuration
"""
from typing import List, Optional
import logging
from ..core.abstract import EcucParamConfContainerDef, EcucRefType, Module


class SecOCGeneral(EcucParamConfContainerDef):
    """
    General configuration for SecOC module.

    Implements: SWR_SECOC_00002 (General configuration)
    """

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.secocDevErrorDetect: bool = None
        self.secocEnabled: bool = None

    def getSecocDevErrorDetect(self) -> bool:
        return self.secocDevErrorDetect

    def setSecocDevErrorDetect(self, value: bool):
        if value is not None:
            self.secocDevErrorDetect = value
        return self

    def getSecocEnabled(self) -> bool:
        return self.secocEnabled

    def setSecocEnabled(self, value: bool):
        if value is not None:
            self.secocEnabled = value
        return self


class SecOC(Module):
    """
    AUTOSAR SecOC module.

    Provides secure on-board communication with message authentication
    and freshness verification.

    Implements: SWR_SECOC_00001 (SecOC Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "SecOC")
        self.secocGeneral: SecOCGeneral = None

    def getSecocGeneral(self) -> SecOCGeneral:
        return self.secocGeneral

    def setSecocGeneral(self, value: SecOCGeneral):
        if value is not None:
            self.secocGeneral = value
        return self