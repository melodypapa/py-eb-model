from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class SomeIpTpGeneral(EcucParamConfContainerDef):
    """SomeIpTp general configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.someIpTpDevErrorDetect: bool = None
        self.someIpTpRxMainFunctionPeriod: float = None
        self.someIpTpTxMainFunctionPeriod: float = None
        self.someIpTpVersionInfoApi: bool = None

    def getSomeIpTpDevErrorDetect(self) -> bool:
        return self.someIpTpDevErrorDetect

    def setSomeIpTpDevErrorDetect(self, value: bool):
        if value is not None:
            self.someIpTpDevErrorDetect = value
        return self

    def getSomeIpTpRxMainFunctionPeriod(self) -> float:
        return self.someIpTpRxMainFunctionPeriod

    def setSomeIpTpRxMainFunctionPeriod(self, value: float):
        if value is not None:
            self.someIpTpRxMainFunctionPeriod = value
        return self

    def getSomeIpTpTxMainFunctionPeriod(self) -> float:
        return self.someIpTpTxMainFunctionPeriod

    def setSomeIpTpTxMainFunctionPeriod(self, value: float):
        if value is not None:
            self.someIpTpTxMainFunctionPeriod = value
        return self

    def getSomeIpTpVersionInfoApi(self) -> bool:
        return self.someIpTpVersionInfoApi

    def setSomeIpTpVersionInfoApi(self, value: bool):
        if value is not None:
            self.someIpTpVersionInfoApi = value
        return self


class SomeIpTpRxNPdu(EcucParamConfContainerDef):
    """SomeIpTp RxNPdu configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.someIpTpRxNPduHandleId: int = None
        self.someIpTpRxNPduRef: EcucRefType = None

    def getSomeIpTpRxNPduHandleId(self) -> int:
        return self.someIpTpRxNPduHandleId

    def setSomeIpTpRxNPduHandleId(self, value: int):
        if value is not None:
            self.someIpTpRxNPduHandleId = value
        return self

    def getSomeIpTpRxNPduRef(self) -> EcucRefType:
        return self.someIpTpRxNPduRef

    def setSomeIpTpRxNPduRef(self, value: EcucRefType):
        if value is not None:
            self.someIpTpRxNPduRef = value
        return self


class SomeIpTpRxNSdu(EcucParamConfContainerDef):
    """SomeIpTp RxNSdu configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.someIpTpRxSduRef: EcucRefType = None
        self.someIpTpRxNPdu: SomeIpTpRxNPdu = None

    def getSomeIpTpRxSduRef(self) -> EcucRefType:
        return self.someIpTpRxSduRef

    def setSomeIpTpRxSduRef(self, value: EcucRefType):
        if value is not None:
            self.someIpTpRxSduRef = value
        return self

    def getSomeIpTpRxNPdu(self) -> SomeIpTpRxNPdu:
        return self.someIpTpRxNPdu

    def setSomeIpTpRxNPdu(self, value: SomeIpTpRxNPdu):
        if value is not None:
            self.someIpTpRxNPdu = value
        return self


class SomeIpTpTxNPdu(EcucParamConfContainerDef):
    """SomeIpTp TxNPdu configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.someIpTpTxNPduHandleId: int = None
        self.someIpTpTxNPduRef: EcucRefType = None

    def getSomeIpTpTxNPduHandleId(self) -> int:
        return self.someIpTpTxNPduHandleId

    def setSomeIpTpTxNPduHandleId(self, value: int):
        if value is not None:
            self.someIpTpTxNPduHandleId = value
        return self

    def getSomeIpTpTxNPduRef(self) -> EcucRefType:
        return self.someIpTpTxNPduRef

    def setSomeIpTpTxNPduRef(self, value: EcucRefType):
        if value is not None:
            self.someIpTpTxNPduRef = value
        return self


class SomeIpTpTxNSdu(EcucParamConfContainerDef):
    """SomeIpTp TxNSdu configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.someIpTpTxNSduHandleId: int = None
        self.someIpTpTxNSduRef: EcucRefType = None
        self.someIpTpTxNPdu: SomeIpTpTxNPdu = None

    def getSomeIpTpTxNSduHandleId(self) -> int:
        return self.someIpTpTxNSduHandleId

    def setSomeIpTpTxNSduHandleId(self, value: int):
        if value is not None:
            self.someIpTpTxNSduHandleId = value
        return self

    def getSomeIpTpTxNSduRef(self) -> EcucRefType:
        return self.someIpTpTxNSduRef

    def setSomeIpTpTxNSduRef(self, value: EcucRefType):
        if value is not None:
            self.someIpTpTxNSduRef = value
        return self

    def getSomeIpTpTxNPdu(self) -> SomeIpTpTxNPdu:
        return self.someIpTpTxNPdu

    def setSomeIpTpTxNPdu(self, value: SomeIpTpTxNPdu):
        if value is not None:
            self.someIpTpTxNPdu = value
        return self


class SomeIpTpChannel(EcucParamConfContainerDef):
    """SomeIpTp channel configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.someIpTpNPduSeparationTime: float = None
        self.someIpTpRxTimeoutTime: float = None
        self.someIpTpTxConfirmationTimeout: float = None
        self.someIpTpRxNSdu: SomeIpTpRxNSdu = None
        self.someIpTpTxNSdu: SomeIpTpTxNSdu = None

    def getSomeIpTpNPduSeparationTime(self) -> float:
        return self.someIpTpNPduSeparationTime

    def setSomeIpTpNPduSeparationTime(self, value: float):
        if value is not None:
            self.someIpTpNPduSeparationTime = value
        return self

    def getSomeIpTpRxTimeoutTime(self) -> float:
        return self.someIpTpRxTimeoutTime

    def setSomeIpTpRxTimeoutTime(self, value: float):
        if value is not None:
            self.someIpTpRxTimeoutTime = value
        return self

    def getSomeIpTpTxConfirmationTimeout(self) -> float:
        return self.someIpTpTxConfirmationTimeout

    def setSomeIpTpTxConfirmationTimeout(self, value: float):
        if value is not None:
            self.someIpTpTxConfirmationTimeout = value
        return self

    def getSomeIpTpRxNSdu(self) -> SomeIpTpRxNSdu:
        return self.someIpTpRxNSdu

    def setSomeIpTpRxNSdu(self, value: SomeIpTpRxNSdu):
        if value is not None:
            self.someIpTpRxNSdu = value
        return self

    def getSomeIpTpTxNSdu(self) -> SomeIpTpTxNSdu:
        return self.someIpTpTxNSdu

    def setSomeIpTpTxNSdu(self, value: SomeIpTpTxNSdu):
        if value is not None:
            self.someIpTpTxNSdu = value
        return self


class SomeIpTp(Module):
    """SomeIpTp module model."""
    def __init__(self, parent) -> None:
        super().__init__(parent, "SomeIpTp")

        self.someIpTpGeneral: SomeIpTpGeneral = None
        self.someIpTpChannels: List[SomeIpTpChannel] = []

        self.logger = logging.getLogger()

    def getSomeIpTpGeneral(self) -> SomeIpTpGeneral:
        return self.someIpTpGeneral

    def setSomeIpTpGeneral(self, value: SomeIpTpGeneral):
        if value is not None:
            self.someIpTpGeneral = value
        return self

    def getSomeIpTpChannelList(self) -> List[SomeIpTpChannel]:
        return list(sorted(filter(lambda a: isinstance(a, SomeIpTpChannel), self.elements.values()), key=lambda o: o.getName()))

    def addSomeIpTpChannel(self, value: SomeIpTpChannel):
        self.addElement(value)
        self.someIpTpChannels.append(value)
        return self