"""
CryIf Model Module - Represents AUTOSAR CryIf configuration.

Implements:
    - SWR_CRYIF_00001: CryIf module model
    - SWR_CRYIF_00002: General configuration
"""
import logging
from ..core.abstract import EcucParamConfContainerDef, EcucRefType, Module


class CryIfGeneral(EcucParamConfContainerDef):
    """
    General configuration for CryIf module.

    Implements: SWR_CRYIF_00002 (General configuration)
    """

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.cryIfDevErrorDetect: bool = None
        self.cryIfEnabled: bool = None

    def getCryIfDevErrorDetect(self) -> bool:
        return self.cryIfDevErrorDetect

    def setCryIfDevErrorDetect(self, value: bool):
        if value is not None:
            self.cryIfDevErrorDetect = value
        return self

    def getCryIfEnabled(self) -> bool:
        return self.cryIfEnabled

    def setCryIfEnabled(self, value: bool):
        if value is not None:
            self.cryIfEnabled = value
        return self


class CryIf(Module):
    """
    AUTOSAR CryIf module.

    Provides cryptographic interface for secure communication
    and cryptographic operations.

    Implements: SWR_CRYIF_00001 (CryIf Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "CryIf")
        self.cryIfGeneral: CryIfGeneral = None

    def getCryIfGeneral(self) -> CryIfGeneral:
        return self.cryIfGeneral

    def setCryIfGeneral(self, value: CryIfGeneral):
        if value is not None:
            self.cryIfGeneral = value
        return self