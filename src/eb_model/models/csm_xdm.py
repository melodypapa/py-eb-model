"""
Csm Model Module - Represents AUTOSAR Csm configuration.

Implements:
    - SWR_CSM_00001: Csm module model
    - SWR_CSM_00002: General configuration
"""
from typing import List, Optional
import logging
from .abstract import EcucParamConfContainerDef, EcucRefType, Module


class CsmGeneral(EcucParamConfContainerDef):
    """
    General configuration for Csm module.

    Implements: SWR_CSM_00002 (General configuration)
    """

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.csmDevErrorDetect: bool = None
        self.csmEnabled: bool = None

    def getCsmDevErrorDetect(self) -> bool:
        return self.csmDevErrorDetect

    def setCsmDevErrorDetect(self, value: bool):
        if value is not None:
            self.csmDevErrorDetect = value
        return self

    def getCsmEnabled(self) -> bool:
        return self.csmEnabled

    def setCsmEnabled(self, value: bool):
        if value is not None:
            self.csmEnabled = value
        return self


class Csm(Module):
    """
    AUTOSAR Csm module.

    Provides cryptographic services management for secure communication
    and cryptographic operations.

    Implements: SWR_CSM_00001 (Csm Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "Csm")
        self.csmGeneral: CsmGeneral = None
        self.logger = logging.getLogger()

    def getCsmGeneral(self) -> CsmGeneral:
        return self.csmGeneral

    def setCsmGeneral(self, value: CsmGeneral):
        if value is not None:
            self.csmGeneral = value
        return self