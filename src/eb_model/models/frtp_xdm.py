from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class FrTpGeneral(EcucParamConfContainerDef):
    """FrTp general configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frTpDevErrorDetect: bool = None
        self.frTpChanNum: int = None
        self.frTpMainFuncCycle: float = None
        self.frTpVersionInfoApi: bool = None
        self.frTpTxPduNum: int = None
        self.frTpRelocatablePbcfgEnable: bool = None

    def getFrTpDevErrorDetect(self) -> bool:
        return self.frTpDevErrorDetect

    def setFrTpDevErrorDetect(self, value: bool):
        if value is not None:
            self.frTpDevErrorDetect = value
        return self

    def getFrTpChanNum(self) -> int:
        return self.frTpChanNum

    def setFrTpChanNum(self, value: int):
        if value is not None:
            self.frTpChanNum = value
        return self

    def getFrTpMainFuncCycle(self) -> float:
        return self.frTpMainFuncCycle

    def setFrTpMainFuncCycle(self, value: float):
        if value is not None:
            self.frTpMainFuncCycle = value
        return self

    def getFrTpVersionInfoApi(self) -> bool:
        return self.frTpVersionInfoApi

    def setFrTpVersionInfoApi(self, value: bool):
        if value is not None:
            self.frTpVersionInfoApi = value
        return self

    def getFrTpTxPduNum(self) -> int:
        return self.frTpTxPduNum

    def setFrTpTxPduNum(self, value: int):
        if value is not None:
            self.frTpTxPduNum = value
        return self

    def getFrTpRelocatablePbcfgEnable(self) -> bool:
        return self.frTpRelocatablePbcfgEnable

    def setFrTpRelocatablePbcfgEnable(self, value: bool):
        if value is not None:
            self.frTpRelocatablePbcfgEnable = value
        return self


class FrTpConnectionLimitConfig(EcucParamConfContainerDef):
    """FrTp connection limit configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frTpRa: int = None
        self.frTpConnectionLimit: int = None
        self.frTpConnectionBufferSize: int = None

    def getFrTpRa(self) -> int:
        return self.frTpRa

    def setFrTpRa(self, value: int):
        if value is not None:
            self.frTpRa = value
        return self

    def getFrTpConnectionLimit(self) -> int:
        return self.frTpConnectionLimit

    def setFrTpConnectionLimit(self, value: int):
        if value is not None:
            self.frTpConnectionLimit = value
        return self

    def getFrTpConnectionBufferSize(self) -> int:
        return self.frTpConnectionBufferSize

    def setFrTpConnectionBufferSize(self, value: int):
        if value is not None:
            self.frTpConnectionBufferSize = value
        return self


class FrTpConnectionControl(EcucParamConfContainerDef):
    """FrTp connection control configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frTpAckType: str = None
        self.frTpMaxAr: int = None
        self.frTpMaxAs: int = None
        self.frTpMaxBufferSize: int = None
        self.frTpMaxFCWait: int = None
        self.frTpMaxFrIf: int = None
        self.frTpMaxNbrOfNPduPerCycle: int = None
        self.frTpMaxRn: int = None
        self.frTpSCexp: int = None
        self.frTpTimeBr: float = None
        self.frTpTimeBuffer: float = None
        self.frTpTimeFrIf: float = None
        self.frTpTimeoutAr: float = None
        self.frTpTimeoutAs: float = None
        self.frTpTimeoutBs: float = None
        self.frTpTimeoutCr: float = None
        self.frTpMaxBufReq: int = None

    def getFrTpAckType(self) -> str:
        return self.frTpAckType

    def setFrTpAckType(self, value: str):
        if value is not None:
            self.frTpAckType = value
        return self

    def getFrTpMaxAr(self) -> int:
        return self.frTpMaxAr

    def setFrTpMaxAr(self, value: int):
        if value is not None:
            self.frTpMaxAr = value
        return self

    def getFrTpMaxAs(self) -> int:
        return self.frTpMaxAs

    def setFrTpMaxAs(self, value: int):
        if value is not None:
            self.frTpMaxAs = value
        return self

    def getFrTpMaxBufferSize(self) -> int:
        return self.frTpMaxBufferSize

    def setFrTpMaxBufferSize(self, value: int):
        if value is not None:
            self.frTpMaxBufferSize = value
        return self

    def getFrTpMaxFCWait(self) -> int:
        return self.frTpMaxFCWait

    def setFrTpMaxFCWait(self, value: int):
        if value is not None:
            self.frTpMaxFCWait = value
        return self

    def getFrTpMaxFrIf(self) -> int:
        return self.frTpMaxFrIf

    def setFrTpMaxFrIf(self, value: int):
        if value is not None:
            self.frTpMaxFrIf = value
        return self

    def getFrTpMaxNbrOfNPduPerCycle(self) -> int:
        return self.frTpMaxNbrOfNPduPerCycle

    def setFrTpMaxNbrOfNPduPerCycle(self, value: int):
        if value is not None:
            self.frTpMaxNbrOfNPduPerCycle = value
        return self

    def getFrTpMaxRn(self) -> int:
        return self.frTpMaxRn

    def setFrTpMaxRn(self, value: int):
        if value is not None:
            self.frTpMaxRn = value
        return self

    def getFrTpSCexp(self) -> int:
        return self.frTpSCexp

    def setFrTpSCexp(self, value: int):
        if value is not None:
            self.frTpSCexp = value
        return self

    def getFrTpTimeBr(self) -> float:
        return self.frTpTimeBr

    def setFrTpTimeBr(self, value: float):
        if value is not None:
            self.frTpTimeBr = value
        return self

    def getFrTpTimeBuffer(self) -> float:
        return self.frTpTimeBuffer

    def setFrTpTimeBuffer(self, value: float):
        if value is not None:
            self.frTpTimeBuffer = value
        return self

    def getFrTpTimeFrIf(self) -> float:
        return self.frTpTimeFrIf

    def setFrTpTimeFrIf(self, value: float):
        if value is not None:
            self.frTpTimeFrIf = value
        return self

    def getFrTpTimeoutAr(self) -> float:
        return self.frTpTimeoutAr

    def setFrTpTimeoutAr(self, value: float):
        if value is not None:
            self.frTpTimeoutAr = value
        return self

    def getFrTpTimeoutAs(self) -> float:
        return self.frTpTimeoutAs

    def setFrTpTimeoutAs(self, value: float):
        if value is not None:
            self.frTpTimeoutAs = value
        return self

    def getFrTpTimeoutBs(self) -> float:
        return self.frTpTimeoutBs

    def setFrTpTimeoutBs(self, value: float):
        if value is not None:
            self.frTpTimeoutBs = value
        return self

    def getFrTpTimeoutCr(self) -> float:
        return self.frTpTimeoutCr

    def setFrTpTimeoutCr(self, value: float):
        if value is not None:
            self.frTpTimeoutCr = value
        return self

    def getFrTpMaxBufReq(self) -> int:
        return self.frTpMaxBufReq

    def setFrTpMaxBufReq(self, value: int):
        if value is not None:
            self.frTpMaxBufReq = value
        return self


class FrTpRxSdu(EcucParamConfContainerDef):
    """FrTp RxSdu configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frTpRxSduId: int = None
        self.frTpRxSduRef: EcucRefType = None

    def getFrTpRxSduId(self) -> int:
        return self.frTpRxSduId

    def setFrTpRxSduId(self, value: int):
        if value is not None:
            self.frTpRxSduId = value
        return self

    def getFrTpRxSduRef(self) -> EcucRefType:
        return self.frTpRxSduRef

    def setFrTpRxSduRef(self, value: EcucRefType):
        if value is not None:
            self.frTpRxSduRef = value
        return self


class FrTpTxSdu(EcucParamConfContainerDef):
    """FrTp TxSdu configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frTpTxSduId: int = None
        self.frTpTxSduRef: EcucRefType = None

    def getFrTpTxSduId(self) -> int:
        return self.frTpTxSduId

    def setFrTpTxSduId(self, value: int):
        if value is not None:
            self.frTpTxSduId = value
        return self

    def getFrTpTxSduRef(self) -> EcucRefType:
        return self.frTpTxSduRef

    def setFrTpTxSduRef(self, value: EcucRefType):
        if value is not None:
            self.frTpTxSduRef = value
        return self


class FrTpConnection(EcucParamConfContainerDef):
    """FrTp connection configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frTpBandwidthLimitation: bool = None
        self.frTpLa: int = None
        self.frTpRa: int = None
        self.frTpMultipleReceiverCon: bool = None
        self.frTpConCtrlRef: EcucRefType = None
        self.frTpRxPduPoolRef: EcucRefType = None
        self.frTpTxPduPoolRef: EcucRefType = None
        self.frTpRxSdu: FrTpRxSdu = None
        self.frTpTxSdu: FrTpTxSdu = None
        self.frTpConnectionControl: FrTpConnectionControl = None

    def getFrTpBandwidthLimitation(self) -> bool:
        return self.frTpBandwidthLimitation

    def setFrTpBandwidthLimitation(self, value: bool):
        if value is not None:
            self.frTpBandwidthLimitation = value
        return self

    def getFrTpLa(self) -> int:
        return self.frTpLa

    def setFrTpLa(self, value: int):
        if value is not None:
            self.frTpLa = value
        return self

    def getFrTpRa(self) -> int:
        return self.frTpRa

    def setFrTpRa(self, value: int):
        if value is not None:
            self.frTpRa = value
        return self

    def getFrTpMultipleReceiverCon(self) -> bool:
        return self.frTpMultipleReceiverCon

    def setFrTpMultipleReceiverCon(self, value: bool):
        if value is not None:
            self.frTpMultipleReceiverCon = value
        return self

    def getFrTpConCtrlRef(self) -> EcucRefType:
        return self.frTpConCtrlRef

    def setFrTpConCtrlRef(self, value: EcucRefType):
        if value is not None:
            self.frTpConCtrlRef = value
        return self

    def getFrTpRxPduPoolRef(self) -> EcucRefType:
        return self.frTpRxPduPoolRef

    def setFrTpRxPduPoolRef(self, value: EcucRefType):
        if value is not None:
            self.frTpRxPduPoolRef = value
        return self

    def getFrTpTxPduPoolRef(self) -> EcucRefType:
        return self.frTpTxPduPoolRef

    def setFrTpTxPduPoolRef(self, value: EcucRefType):
        if value is not None:
            self.frTpTxPduPoolRef = value
        return self

    def getFrTpRxSdu(self) -> FrTpRxSdu:
        return self.frTpRxSdu

    def setFrTpRxSdu(self, value: FrTpRxSdu):
        if value is not None:
            self.frTpRxSdu = value
        return self

    def getFrTpTxSdu(self) -> FrTpTxSdu:
        return self.frTpTxSdu

    def setFrTpTxSdu(self, value: FrTpTxSdu):
        if value is not None:
            self.frTpTxSdu = value
        return self

    def getFrTpConnectionControl(self) -> FrTpConnectionControl:
        return self.frTpConnectionControl

    def setFrTpConnectionControl(self, value: FrTpConnectionControl):
        if value is not None:
            self.frTpConnectionControl = value
        return self


class FrTp(Module):
    """FrTp module model."""
    def __init__(self, parent) -> None:
        super().__init__(parent, "FrTp")

        self.frTpGeneral: FrTpGeneral = None
        self.frTpConnectionLimitConfig: FrTpConnectionLimitConfig = None
        self.frTpConnections: List[FrTpConnection] = []

        self.logger = logging.getLogger()

    def getFrTpGeneral(self) -> FrTpGeneral:
        return self.frTpGeneral

    def setFrTpGeneral(self, value: FrTpGeneral):
        if value is not None:
            self.frTpGeneral = value
        return self

    def getFrTpConnectionLimitConfig(self) -> FrTpConnectionLimitConfig:
        return self.frTpConnectionLimitConfig

    def setFrTpConnectionLimitConfig(self, value: FrTpConnectionLimitConfig):
        if value is not None:
            self.frTpConnectionLimitConfig = value
        return self

    def getFrTpConnectionList(self) -> List[FrTpConnection]:
        return list(sorted(filter(lambda a: isinstance(a, FrTpConnection), self.elements.values()), key=lambda o: o.getName()))

    def addFrTpConnection(self, value: FrTpConnection):
        self.addElement(value)
        self.frTpConnections.append(value)
        return self