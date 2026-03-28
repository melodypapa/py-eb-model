"""
Crc Model Classes - AUTOSAR Crc (Cyclic Redundancy Check) configuration objects.

Implements:
    - SWR_CRC_00001: Crc module model
    - SWR_CRC_00002: Crc configuration model
"""
from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, Module


class CrcConfig(EcucParamConfContainerDef):
    """
    Crc configuration container.

    Represents a single CRC configuration in the Crc module.

    Implements: SWR_CRC_00002 (Crc configuration model)
    """

    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        """Initialize Crc configuration."""
        super().__init__(parent, name)

        self.crcId: int = None
        self.crcCRCType: str = None

    def getCrcId(self) -> int:
        return self.crcId

    def setCrcId(self, value: int):
        if value is not None:
            self.crcId = value
        return self

    def getCrcCRCType(self) -> str:
        return self.crcCRCType

    def setCrcCRCType(self, value: str):
        if value is not None:
            self.crcCRCType = value
        return self


class Crc(Module):
    """
    AUTOSAR Crc (Cyclic Redundancy Check) module configuration.

    Manages CRC calculation and verification for data integrity.

    Implements: SWR_CRC_00001 (Crc module model)
    """

    def __init__(self, parent: Optional['EcucObject']) -> None:
        """Initialize Crc module."""
        super().__init__(parent, "Crc")

        self.crcConfigList: List[CrcConfig] = []

        self.logger = logging.getLogger()

    def getCrcConfigList(self) -> List[CrcConfig]:
        return list(sorted(filter(lambda a: isinstance(a, CrcConfig), self.elements.values()), key=lambda o: o.getName()))

    def addCrcConfig(self, value: CrcConfig):
        self.addElement(value)
        self.crcConfigList.append(value)
        return self