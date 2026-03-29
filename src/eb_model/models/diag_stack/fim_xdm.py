"""
FiM Model Module - Represents AUTOSAR FiM configuration.

Implements:
    - SWR_FIM_00001: FiM module model
    - SWR_FIM_00002: General configuration
"""
from typing import List, Optional
import logging
from eb_model.models.core.abstract import EcucParamConfContainerDef, EcucRefType, Module


class FiMGeneral(EcucParamConfContainerDef):
    """
    General configuration for FiM module.

    Implements: SWR_FIM_00002 (General configuration)
    """

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.fimDevErrorDetect: bool = None
        self.fimEnabled: bool = None

    def getFimDevErrorDetect(self) -> bool:
        return self.fimDevErrorDetect

    def setFimDevErrorDetect(self, value: bool):
        if value is not None:
            self.fimDevErrorDetect = value
        return self

    def getFimEnabled(self) -> bool:
        return self.fimEnabled

    def setFimEnabled(self, value: bool):
        if value is not None:
            self.fimEnabled = value
        return self


class FiM(Module):
    """
    AUTOSAR FiM module.

    Provides function inhibition mechanism for selective function
    inhibition during fault conditions.

    Implements: SWR_FIM_00001 (FiM Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "FiM")
        self.fimGeneral: FiMGeneral = None

    def getFimGeneral(self) -> FiMGeneral:
        return self.fimGeneral

    def setFimGeneral(self, value: FiMGeneral):
        if value is not None:
            self.fimGeneral = value
        return self
