from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class FrArTpGeneral(EcucParamConfContainerDef):
    """FrArTp general configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frArTpDevErrorDetect: bool = None
        self.frArTpHaveAckRt: bool = None
        self.frArTpHaveGrpSeg: bool = None
        self.frArTpHaveLm: bool = None
        self.frArTpHaveTc: bool = None
        self.frArTpMainFuncCycle: float = None
        self.frArTpVersionInfoApi: bool = None
        self.frArTpRelocatablePbcfgEnable: bool = None
        self.frArTpMaxConnections: int = None
        self.frArTpMaxActiveConnections: int = None
        self.frArTpMaxTxPdus: int = None
        self.supportLowLevelRouting: bool = None
        self.lowLevelRoutingPraefix: str = None

        # Defensive programming
        self.frArTpDefProgEnabled: bool = None
        self.frArTpPrecondAssertEnabled: bool = None
        self.frArTpPostcondAssertEnabled: bool = None
        self.frArTpStaticAssertEnabled: bool = None
        self.frArTpUnreachAssertEnabled: bool = None
        self.frArTpInvariantAssertEnabled: bool = None

    def getFrArTpDevErrorDetect(self) -> bool:
        return self.frArTpDevErrorDetect

    def setFrArTpDevErrorDetect(self, value: bool):
        if value is not None:
            self.frArTpDevErrorDetect = value
        return self

    def getFrArTpHaveAckRt(self) -> bool:
        return self.frArTpHaveAckRt

    def setFrArTpHaveAckRt(self, value: bool):
        if value is not None:
            self.frArTpHaveAckRt = value
        return self

    def getFrArTpHaveGrpSeg(self) -> bool:
        return self.frArTpHaveGrpSeg

    def setFrArTpHaveGrpSeg(self, value: bool):
        if value is not None:
            self.frArTpHaveGrpSeg = value
        return self

    def getFrArTpHaveLm(self) -> bool:
        return self.frArTpHaveLm

    def setFrArTpHaveLm(self, value: bool):
        if value is not None:
            self.frArTpHaveLm = value
        return self

    def getFrArTpHaveTc(self) -> bool:
        return self.frArTpHaveTc

    def setFrArTpHaveTc(self, value: bool):
        if value is not None:
            self.frArTpHaveTc = value
        return self

    def getFrArTpMainFuncCycle(self) -> float:
        return self.frArTpMainFuncCycle

    def setFrArTpMainFuncCycle(self, value: float):
        if value is not None:
            self.frArTpMainFuncCycle = value
        return self

    def getFrArTpVersionInfoApi(self) -> bool:
        return self.frArTpVersionInfoApi

    def setFrArTpVersionInfoApi(self, value: bool):
        if value is not None:
            self.frArTpVersionInfoApi = value
        return self

    def getFrArTpRelocatablePbcfgEnable(self) -> bool:
        return self.frArTpRelocatablePbcfgEnable

    def setFrArTpRelocatablePbcfgEnable(self, value: bool):
        if value is not None:
            self.frArTpRelocatablePbcfgEnable = value
        return self

    def getFrArTpMaxConnections(self) -> int:
        return self.frArTpMaxConnections

    def setFrArTpMaxConnections(self, value: int):
        if value is not None:
            self.frArTpMaxConnections = value
        return self

    def getFrArTpMaxActiveConnections(self) -> int:
        return self.frArTpMaxActiveConnections

    def setFrArTpMaxActiveConnections(self, value: int):
        if value is not None:
            self.frArTpMaxActiveConnections = value
        return self

    def getFrArTpMaxTxPdus(self) -> int:
        return self.frArTpMaxTxPdus

    def setFrArTpMaxTxPdus(self, value: int):
        if value is not None:
            self.frArTpMaxTxPdus = value
        return self

    def getSupportLowLevelRouting(self) -> bool:
        return self.supportLowLevelRouting

    def setSupportLowLevelRouting(self, value: bool):
        if value is not None:
            self.supportLowLevelRouting = value
        return self

    def getLowLevelRoutingPraefix(self) -> str:
        return self.lowLevelRoutingPraefix

    def setLowLevelRoutingPraefix(self, value: str):
        if value is not None:
            self.lowLevelRoutingPraefix = value
        return self

    # Defensive programming getters/setters
    def getFrArTpDefProgEnabled(self) -> bool:
        return self.frArTpDefProgEnabled

    def setFrArTpDefProgEnabled(self, value: bool):
        if value is not None:
            self.frArTpDefProgEnabled = value
        return self

    def getFrArTpPrecondAssertEnabled(self) -> bool:
        return self.frArTpPrecondAssertEnabled

    def setFrArTpPrecondAssertEnabled(self, value: bool):
        if value is not None:
            self.frArTpPrecondAssertEnabled = value
        return self

    def getFrArTpPostcondAssertEnabled(self) -> bool:
        return self.frArTpPostcondAssertEnabled

    def setFrArTpPostcondAssertEnabled(self, value: bool):
        if value is not None:
            self.frArTpPostcondAssertEnabled = value
        return self

    def getFrArTpStaticAssertEnabled(self) -> bool:
        return self.frArTpStaticAssertEnabled

    def setFrArTpStaticAssertEnabled(self, value: bool):
        if value is not None:
            self.frArTpStaticAssertEnabled = value
        return self

    def getFrArTpUnreachAssertEnabled(self) -> bool:
        return self.frArTpUnreachAssertEnabled

    def setFrArTpUnreachAssertEnabled(self, value: bool):
        if value is not None:
            self.frArTpUnreachAssertEnabled = value
        return self

    def getFrArTpInvariantAssertEnabled(self) -> bool:
        return self.frArTpInvariantAssertEnabled

    def setFrArTpInvariantAssertEnabled(self, value: bool):
        if value is not None:
            self.frArTpInvariantAssertEnabled = value
        return self


class FrArTpRxSdu(EcucParamConfContainerDef):
    """FrArTp RxSdu configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frArTpSduRxId: int = None
        self.frArTpRxSduRef: EcucRefType = None

    def getFrArTpSduRxId(self) -> int:
        return self.frArTpSduRxId

    def setFrArTpSduRxId(self, value: int):
        if value is not None:
            self.frArTpSduRxId = value
        return self

    def getFrArTpRxSduRef(self) -> EcucRefType:
        return self.frArTpRxSduRef

    def setFrArTpRxSduRef(self, value: EcucRefType):
        if value is not None:
            self.frArTpRxSduRef = value
        return self


class FrArTpTxSdu(EcucParamConfContainerDef):
    """FrArTp TxSdu configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frArTpSduTxId: int = None
        self.frArTpTxSduRef: EcucRefType = None

    def getFrArTpSduTxId(self) -> int:
        return self.frArTpSduTxId

    def setFrArTpSduTxId(self, value: int):
        if value is not None:
            self.frArTpSduTxId = value
        return self

    def getFrArTpTxSduRef(self) -> EcucRefType:
        return self.frArTpTxSduRef

    def setFrArTpTxSduRef(self, value: EcucRefType):
        if value is not None:
            self.frArTpTxSduRef = value
        return self


class FrArTpPdu(EcucParamConfContainerDef):
    """FrArTp Pdu configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frArTpPduDirection: str = None
        self.frArTpPduId: int = None
        self.frArTpPduRef: EcucRefType = None

    def getFrArTpPduDirection(self) -> str:
        return self.frArTpPduDirection

    def setFrArTpPduDirection(self, value: str):
        if value is not None:
            self.frArTpPduDirection = value
        return self

    def getFrArTpPduId(self) -> int:
        return self.frArTpPduId

    def setFrArTpPduId(self, value: int):
        if value is not None:
            self.frArTpPduId = value
        return self

    def getFrArTpPduRef(self) -> EcucRefType:
        return self.frArTpPduRef

    def setFrArTpPduRef(self, value: EcucRefType):
        if value is not None:
            self.frArTpPduRef = value
        return self


class FrArTpConnection(EcucParamConfContainerDef):
    """FrArTp connection configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frArTpConPrioPdus: int = None
        self.frArTpLa: int = None
        self.frArTpRa: int = None
        self.frArTpMultRec: bool = None
        self.frArTpRxSdu: FrArTpRxSdu = None
        self.frArTpTxSdu: FrArTpTxSdu = None

    def getFrArTpConPrioPdus(self) -> int:
        return self.frArTpConPrioPdus

    def setFrArTpConPrioPdus(self, value: int):
        if value is not None:
            self.frArTpConPrioPdus = value
        return self

    def getFrArTpLa(self) -> int:
        return self.frArTpLa

    def setFrArTpLa(self, value: int):
        if value is not None:
            self.frArTpLa = value
        return self

    def getFrArTpRa(self) -> int:
        return self.frArTpRa

    def setFrArTpRa(self, value: int):
        if value is not None:
            self.frArTpRa = value
        return self

    def getFrArTpMultRec(self) -> bool:
        return self.frArTpMultRec

    def setFrArTpMultRec(self, value: bool):
        if value is not None:
            self.frArTpMultRec = value
        return self

    def getFrArTpRxSdu(self) -> FrArTpRxSdu:
        return self.frArTpRxSdu

    def setFrArTpRxSdu(self, value: FrArTpRxSdu):
        if value is not None:
            self.frArTpRxSdu = value
        return self

    def getFrArTpTxSdu(self) -> FrArTpTxSdu:
        return self.frArTpTxSdu

    def setFrArTpTxSdu(self, value: FrArTpTxSdu):
        if value is not None:
            self.frArTpTxSdu = value
        return self


class FrArTpChannel(EcucParamConfContainerDef):
    """FrArTp channel configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frArTpAckType: str = None
        self.frArTpAdrType: str = None
        self.frArTpConcurrentConnections: int = None
        self.frArTpGrpSeg: bool = None
        self.frArTpLm: str = None
        self.frArTpMaxAr: int = None
        self.frArTpMaxAs: int = None
        self.frArTpMaxBs: int = None
        self.frArTpMaxRn: int = None
        self.frArTpMaxWft: int = None
        self.frArTpStMin: float = None
        self.frArTpStMinGrpSeg: float = None
        self.frArTpTc: bool = None
        self.frArTpTimeBr: float = None
        self.frArTpTimeCs: float = None
        self.frArTpTimeoutAr: float = None
        self.frArTpTimeoutAs: float = None
        self.frArTpTimeoutBs: float = None
        self.frArTpTimeoutCr: float = None
        self.frArTpConnections: List[FrArTpConnection] = []
        self.frArTpPdus: List[FrArTpPdu] = []

    def getFrArTpAckType(self) -> str:
        return self.frArTpAckType

    def setFrArTpAckType(self, value: str):
        if value is not None:
            self.frArTpAckType = value
        return self

    def getFrArTpAdrType(self) -> str:
        return self.frArTpAdrType

    def setFrArTpAdrType(self, value: str):
        if value is not None:
            self.frArTpAdrType = value
        return self

    def getFrArTpConcurrentConnections(self) -> int:
        return self.frArTpConcurrentConnections

    def setFrArTpConcurrentConnections(self, value: int):
        if value is not None:
            self.frArTpConcurrentConnections = value
        return self

    def getFrArTpGrpSeg(self) -> bool:
        return self.frArTpGrpSeg

    def setFrArTpGrpSeg(self, value: bool):
        if value is not None:
            self.frArTpGrpSeg = value
        return self

    def getFrArTpLm(self) -> str:
        return self.frArTpLm

    def setFrArTpLm(self, value: str):
        if value is not None:
            self.frArTpLm = value
        return self

    def getFrArTpMaxAr(self) -> int:
        return self.frArTpMaxAr

    def setFrArTpMaxAr(self, value: int):
        if value is not None:
            self.frArTpMaxAr = value
        return self

    def getFrArTpMaxAs(self) -> int:
        return self.frArTpMaxAs

    def setFrArTpMaxAs(self, value: int):
        if value is not None:
            self.frArTpMaxAs = value
        return self

    def getFrArTpMaxBs(self) -> int:
        return self.frArTpMaxBs

    def setFrArTpMaxBs(self, value: int):
        if value is not None:
            self.frArTpMaxBs = value
        return self

    def getFrArTpMaxRn(self) -> int:
        return self.frArTpMaxRn

    def setFrArTpMaxRn(self, value: int):
        if value is not None:
            self.frArTpMaxRn = value
        return self

    def getFrArTpMaxWft(self) -> int:
        return self.frArTpMaxWft

    def setFrArTpMaxWft(self, value: int):
        if value is not None:
            self.frArTpMaxWft = value
        return self

    def getFrArTpStMin(self) -> float:
        return self.frArTpStMin

    def setFrArTpStMin(self, value: float):
        if value is not None:
            self.frArTpStMin = value
        return self

    def getFrArTpStMinGrpSeg(self) -> float:
        return self.frArTpStMinGrpSeg

    def setFrArTpStMinGrpSeg(self, value: float):
        if value is not None:
            self.frArTpStMinGrpSeg = value
        return self

    def getFrArTpTc(self) -> bool:
        return self.frArTpTc

    def setFrArTpTc(self, value: bool):
        if value is not None:
            self.frArTpTc = value
        return self

    def getFrArTpTimeBr(self) -> float:
        return self.frArTpTimeBr

    def setFrArTpTimeBr(self, value: float):
        if value is not None:
            self.frArTpTimeBr = value
        return self

    def getFrArTpTimeCs(self) -> float:
        return self.frArTpTimeCs

    def setFrArTpTimeCs(self, value: float):
        if value is not None:
            self.frArTpTimeCs = value
        return self

    def getFrArTpTimeoutAr(self) -> float:
        return self.frArTpTimeoutAr

    def setFrArTpTimeoutAr(self, value: float):
        if value is not None:
            self.frArTpTimeoutAr = value
        return self

    def getFrArTpTimeoutAs(self) -> float:
        return self.frArTpTimeoutAs

    def setFrArTpTimeoutAs(self, value: float):
        if value is not None:
            self.frArTpTimeoutAs = value
        return self

    def getFrArTpTimeoutBs(self) -> float:
        return self.frArTpTimeoutBs

    def setFrArTpTimeoutBs(self, value: float):
        if value is not None:
            self.frArTpTimeoutBs = value
        return self

    def getFrArTpTimeoutCr(self) -> float:
        return self.frArTpTimeoutCr

    def setFrArTpTimeoutCr(self, value: float):
        if value is not None:
            self.frArTpTimeoutCr = value
        return self

    def getFrArTpConnectionList(self) -> List[FrArTpConnection]:
        return list(sorted(filter(lambda a: isinstance(a, FrArTpConnection), self.elements.values()), key=lambda o: o.getName()))

    def addFrArTpConnection(self, value: FrArTpConnection):
        self.addElement(value)
        self.frArTpConnections.append(value)
        return self

    def getFrArTpPduList(self) -> List[FrArTpPdu]:
        return list(sorted(filter(lambda a: isinstance(a, FrArTpPdu), self.elements.values()), key=lambda o: o.getName()))

    def addFrArTpPdu(self, value: FrArTpPdu):
        self.addElement(value)
        self.frArTpPdus.append(value)
        return self


class FrArTp(Module):
    """FrArTp module model."""
    def __init__(self, parent) -> None:
        super().__init__(parent, "FrArTp")

        self.frArTpGeneral: FrArTpGeneral = None
        self.frArTpChannels: List[FrArTpChannel] = []

        self.logger = logging.getLogger()

    def getFrArTpGeneral(self) -> FrArTpGeneral:
        return self.frArTpGeneral

    def setFrArTpGeneral(self, value: FrArTpGeneral):
        if value is not None:
            self.frArTpGeneral = value
        return self

    def getFrArTpChannelList(self) -> List[FrArTpChannel]:
        return list(sorted(filter(lambda a: isinstance(a, FrArTpChannel), self.elements.values()), key=lambda o: o.getName()))

    def addFrArTpChannel(self, value: FrArTpChannel):
        self.addElement(value)
        self.frArTpChannels.append(value)
        return self