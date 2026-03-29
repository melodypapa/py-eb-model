from typing import List, Optional
import logging
from ..core.abstract import EcucParamConfContainerDef, EcucRefType, Module


class LinTpGeneral(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.linTpMaxNumberOfRespPendingFrames: int = None
        self.linTpNumberOfRxNSdu: int = None
        self.linTpNumberOfTxNSdu: int = None

    def getLinTpMaxNumberOfRespPendingFrames(self) -> int:
        return self.linTpMaxNumberOfRespPendingFrames

    def setLinTpMaxNumberOfRespPendingFrames(self, value: int):
        if value is not None:
            self.linTpMaxNumberOfRespPendingFrames = value
        return self

    def getLinTpNumberOfRxNSdu(self) -> int:
        return self.linTpNumberOfRxNSdu

    def setLinTpNumberOfRxNSdu(self, value: int):
        if value is not None:
            self.linTpNumberOfRxNSdu = value
        return self

    def getLinTpNumberOfTxNSdu(self) -> int:
        return self.linTpNumberOfTxNSdu

    def setLinTpNumberOfTxNSdu(self, value: int):
        if value is not None:
            self.linTpNumberOfTxNSdu = value
        return self


class LinTpRxNSdu(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.linTpRxNSduId: int = None
        self.linTpRxNSduRef: EcucRefType = None

    def getLinTpRxNSduId(self) -> int:
        return self.linTpRxNSduId

    def setLinTpRxNSduId(self, value: int):
        if value is not None:
            self.linTpRxNSduId = value
        return self

    def getLinTpRxNSduRef(self) -> EcucRefType:
        return self.linTpRxNSduRef

    def setLinTpRxNSduRef(self, value: EcucRefType):
        if value is not None:
            self.linTpRxNSduRef = value
        return self


class LinTpTxNSdu(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.linTpTxNSduId: int = None
        self.linTpTxNSduRef: EcucRefType = None

    def getLinTpTxNSduId(self) -> int:
        return self.linTpTxNSduId

    def setLinTpTxNSduId(self, value: int):
        if value is not None:
            self.linTpTxNSduId = value
        return self

    def getLinTpTxNSduRef(self) -> EcucRefType:
        return self.linTpTxNSduRef

    def setLinTpTxNSduRef(self, value: EcucRefType):
        if value is not None:
            self.linTpTxNSduRef = value
        return self


class LinTp(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "LinTp")
        self.linTpGeneral: LinTpGeneral = None
        self.linTpRxNSdus: List[LinTpRxNSdu] = []
        self.linTpTxNSdus: List[LinTpTxNSdu] = []
        self.logger = logging.getLogger()

    def getLinTpGeneral(self) -> LinTpGeneral:
        return self.linTpGeneral

    def setLinTpGeneral(self, value: LinTpGeneral):
        if value is not None:
            self.linTpGeneral = value
        return self

    def getLinTpRxNSduList(self) -> List[LinTpRxNSdu]:
        return list(sorted(filter(lambda a: isinstance(a, LinTpRxNSdu), self.elements.values()), key=lambda o: o.getName()))

    def addLinTpRxNSdu(self, value: LinTpRxNSdu):
        self.addElement(value)
        self.linTpRxNSdus.append(value)
        return self

    def getLinTpTxNSduList(self) -> List[LinTpTxNSdu]:
        return list(sorted(filter(lambda a: isinstance(a, LinTpTxNSdu), self.elements.values()), key=lambda o: o.getName()))

    def addLinTpTxNSdu(self, value: LinTpTxNSdu):
        self.addElement(value)
        self.linTpTxNSdus.append(value)
        return self
