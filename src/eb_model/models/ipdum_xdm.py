"""
IpduM Model Classes - AUTOSAR IpduM (IPDU Multiplexer) configuration objects.

Implements:
    - SWR_IPDUM_00001: IpduM module model
    - SWR_IPDUM_00002: IpduM dynamic PDU model
"""
from typing import List, Optional
import logging
from ..models.abstract import EcucObject, EcucParamConfContainerDef, Module


class IpduMDynPdu(EcucParamConfContainerDef):
    """
    IpduM dynamic PDU configuration.

    Represents a single dynamic PDU in the IpduM multiplexer.

    Implements: SWR_IPDUM_00002 (IpduM dynamic PDU model)
    """

    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        """Initialize IpduM dynamic PDU."""
        super().__init__(parent, name)

        self.ipduMDynPduId: int = None
        self.ipduMDynPduLength: int = None

    def getIpduMDynPduId(self) -> int:
        return self.ipduMDynPduId

    def setIpduMDynPduId(self, value: int):
        if value is not None:
            self.ipduMDynPduId = value
        return self

    def getIpduMDynPduLength(self) -> int:
        return self.ipduMDynPduLength

    def setIpduMDynPduLength(self, value: int):
        if value is not None:
            self.ipduMDynPduLength = value
        return self


class IpduM(Module):
    """
    AUTOSAR IpduM (IPDU Multiplexer) module configuration.

    Manages multiplexing of PDUs for communication layers.

    Implements: SWR_IPDUM_00001 (IpduM module model)
    """

    def __init__(self, parent: Optional['EcucObject']) -> None:
        """Initialize IpduM module."""
        super().__init__(parent, "IpduM")

        self.ipduMDynPduList: List[IpduMDynPdu] = []

        self.logger = logging.getLogger()

    def getIpduMDynPduList(self) -> List[IpduMDynPdu]:
        return list(sorted(filter(lambda a: isinstance(a, IpduMDynPdu), self.elements.values()), key=lambda o: o.getName()))

    def addIpduMDynPdu(self, value: IpduMDynPdu):
        self.addElement(value)
        self.ipduMDynPduList.append(value)
        return self
