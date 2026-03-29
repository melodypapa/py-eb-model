"""
PduR Model Classes - AUTOSAR PduR (PDU Router) configuration objects.

Implements:
    - SWR_PDUR_00001: PduR module model
    - SWR_PDUR_00002: PduR routing table entry model
"""
from typing import List, Optional
import logging
from eb_model.models.core.abstract import EcucObject, EcucParamConfContainerDef, EcucRefType, Module


class PduRRoutingTableEntry(EcucParamConfContainerDef):
    """
    PduR routing table entry configuration.

    Represents a single routing entry in the PduR routing table.

    Implements: SWR_PDUR_00002 (PduR routing table entry model)
    """

    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        """Initialize PduR routing table entry."""
        super().__init__(parent, name)

        self.pduRRoutingTableEntryID: int = None
        self.pduRRoutingPduSID: int = None
        self.pduRDestPduRef: EcucRefType = None
        self.pduRSrcPduRef: EcucRefType = None

    def getPduRRoutingTableEntryID(self) -> int:
        return self.pduRRoutingTableEntryID

    def setPduRRoutingTableEntryID(self, value: int):
        if value is not None:
            self.pduRRoutingTableEntryID = value
        return self

    def getPduRRoutingPduSID(self) -> int:
        return self.pduRRoutingPduSID

    def setPduRRoutingPduSID(self, value: int):
        if value is not None:
            self.pduRRoutingPduSID = value
        return self

    def getPduRDestPduRef(self) -> EcucRefType:
        return self.pduRDestPduRef

    def setPduRDestPduRef(self, value: EcucRefType):
        if value is not None:
            self.pduRDestPduRef = value
        return self

    def getPduRSrcPduRef(self) -> EcucRefType:
        return self.pduRSrcPduRef

    def setPduRSrcPduRef(self, value: EcucRefType):
        if value is not None:
            self.pduRSrcPduRef = value
        return self


class PduR(Module):
    """
    AUTOSAR PduR (PDU Router) module configuration.

    Manages routing of PDUs between different communication layers.

    Implements: SWR_PDUR_00001 (PduR module model)
    """

    def __init__(self, parent: Optional['EcucObject']) -> None:
        """Initialize PduR module."""
        super().__init__(parent, "PduR")

        self.pduRRoutingTableEntryList: List[PduRRoutingTableEntry] = []

        self.logger = logging.getLogger()

    def getPduRRoutingTableEntryList(self) -> List[PduRRoutingTableEntry]:
        return list(sorted(filter(lambda a: isinstance(a, PduRRoutingTableEntry), self.elements.values()), key=lambda o: o.getName()))

    def addPduRRoutingTableEntry(self, value: PduRRoutingTableEntry):
        self.addElement(value)
        self.pduRRoutingTableEntryList.append(value)
        return self
