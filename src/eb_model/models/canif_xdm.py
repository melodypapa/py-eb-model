from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class CanIfGeneral(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canIfDevErrorDetect: bool = None
        self.canIfPublicNumberOfCanHwUnits: int = None
        self.canIfPublicMaxCtrl: int = None
        self.canIfPublicMaxTxPdus: int = None
        self.canIfPublicMaxRxPdus: int = None
        self.canIfSupportTTCAN: bool = None

    def getCanIfDevErrorDetect(self) -> bool:
        return self.canIfDevErrorDetect

    def setCanIfDevErrorDetect(self, value: bool):
        if value is not None:
            self.canIfDevErrorDetect = value
        return self

    def getCanIfPublicNumberOfCanHwUnits(self) -> int:
        return self.canIfPublicNumberOfCanHwUnits

    def setCanIfPublicNumberOfCanHwUnits(self, value: int):
        if value is not None:
            self.canIfPublicNumberOfCanHwUnits = value
        return self

    def getCanIfPublicMaxCtrl(self) -> int:
        return self.canIfPublicMaxCtrl

    def setCanIfPublicMaxCtrl(self, value: int):
        if value is not None:
            self.canIfPublicMaxCtrl = value
        return self

    def getCanIfPublicMaxTxPdus(self) -> int:
        return self.canIfPublicMaxTxPdus

    def setCanIfPublicMaxTxPdus(self, value: int):
        if value is not None:
            self.canIfPublicMaxTxPdus = value
        return self

    def getCanIfPublicMaxRxPdus(self) -> int:
        return self.canIfPublicMaxRxPdus

    def setCanIfPublicMaxRxPdus(self, value: int):
        if value is not None:
            self.canIfPublicMaxRxPdus = value
        return self

    def getCanIfSupportTTCAN(self) -> bool:
        return self.canIfSupportTTCAN

    def setCanIfSupportTTCAN(self, value: bool):
        if value is not None:
            self.canIfSupportTTCAN = value
        return self


class CanIfCtrlCfg(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canIfCtrlId: int = None
        self.canIfCtrlWakeupSupport: bool = None
        self.canIfCtrlCanCtrlRef: EcucRefType = None

    def getCanIfCtrlId(self) -> int:
        return self.canIfCtrlId

    def setCanIfCtrlId(self, value: int):
        if value is not None:
            self.canIfCtrlId = value
        return self

    def getCanIfCtrlWakeupSupport(self) -> bool:
        return self.canIfCtrlWakeupSupport

    def setCanIfCtrlWakeupSupport(self, value: bool):
        if value is not None:
            self.canIfCtrlWakeupSupport = value
        return self

    def getCanIfCtrlCanCtrlRef(self) -> EcucRefType:
        return self.canIfCtrlCanCtrlRef

    def setCanIfCtrlCanCtrlRef(self, value: EcucRefType):
        if value is not None:
            self.canIfCtrlCanCtrlRef = value
        return self


class CanIfTrcvCfg(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canIfTrcvId: int = None
        self.canIfTrcvWakeupSupport: bool = None
        self.canIfTrcvCanTrcvRef: EcucRefType = None

    def getCanIfTrcvId(self) -> int:
        return self.canIfTrcvId

    def setCanIfTrcvId(self, value: int):
        if value is not None:
            self.canIfTrcvId = value
        return self

    def getCanIfTrcvWakeupSupport(self) -> bool:
        return self.canIfTrcvWakeupSupport

    def setCanIfTrcvWakeupSupport(self, value: bool):
        if value is not None:
            self.canIfTrcvWakeupSupport = value
        return self

    def getCanIfTrcvCanTrcvRef(self) -> EcucRefType:
        return self.canIfTrcvCanTrcvRef

    def setCanIfTrcvCanTrcvRef(self, value: EcucRefType):
        if value is not None:
            self.canIfTrcvCanTrcvRef = value
        return self


class CanIfDispatchCfg(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canIfDispatchUserCtrlBusOffName: str = None
        self.canIfDispatchUserCtrlModeIndicationName: str = None

    def getCanIfDispatchUserCtrlBusOffName(self) -> str:
        return self.canIfDispatchUserCtrlBusOffName

    def setCanIfDispatchUserCtrlBusOffName(self, value: str):
        if value is not None:
            self.canIfDispatchUserCtrlBusOffName = value
        return self

    def getCanIfDispatchUserCtrlModeIndicationName(self) -> str:
        return self.canIfDispatchUserCtrlModeIndicationName

    def setCanIfDispatchUserCtrlModeIndicationName(self, value: str):
        if value is not None:
            self.canIfDispatchUserCtrlModeIndicationName = value
        return self


class CanIfBufferCfg(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canIfBufferSize: int = None
        self.canIfBufferHthRef: EcucRefType = None

    def getCanIfBufferSize(self) -> int:
        return self.canIfBufferSize

    def setCanIfBufferSize(self, value: int):
        if value is not None:
            self.canIfBufferSize = value
        return self

    def getCanIfBufferHthRef(self) -> EcucRefType:
        return self.canIfBufferHthRef

    def setCanIfBufferHthRef(self, value: EcucRefType):
        if value is not None:
            self.canIfBufferHthRef = value
        return self


class CanIfHrhCfg(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canIfHrhSoftwareFilter: bool = None
        self.canIfHrhCanCtrlIdRef: EcucRefType = None

    def getCanIfHrhSoftwareFilter(self) -> bool:
        return self.canIfHrhSoftwareFilter

    def setCanIfHrhSoftwareFilter(self, value: bool):
        if value is not None:
            self.canIfHrhSoftwareFilter = value
        return self

    def getCanIfHrhCanCtrlIdRef(self) -> EcucRefType:
        return self.canIfHrhCanCtrlIdRef

    def setCanIfHrhCanCtrlIdRef(self, value: EcucRefType):
        if value is not None:
            self.canIfHrhCanCtrlIdRef = value
        return self


class CanIfHthCfg(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canIfHthCanCtrlIdRef: EcucRefType = None

    def getCanIfHthCanCtrlIdRef(self) -> EcucRefType:
        return self.canIfHthCanCtrlIdRef

    def setCanIfHthCanCtrlIdRef(self, value: EcucRefType):
        if value is not None:
            self.canIfHthCanCtrlIdRef = value
        return self


class CanIfRxPduCfg(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canIfRxPduCanId: int = None
        self.canIfRxPduCanIdType: str = None
        self.canIfRxPduDlc: int = None
        self.canIfRxPduId: int = None
        self.canIfRxPduHrhIdRef: EcucRefType = None
        self.canIfRxPduUpperLayerRef: EcucRefType = None

    def getCanIfRxPduCanId(self) -> int:
        return self.canIfRxPduCanId

    def setCanIfRxPduCanId(self, value: int):
        if value is not None:
            self.canIfRxPduCanId = value
        return self

    def getCanIfRxPduCanIdType(self) -> str:
        return self.canIfRxPduCanIdType

    def setCanIfRxPduCanIdType(self, value: str):
        if value is not None:
            self.canIfRxPduCanIdType = value
        return self

    def getCanIfRxPduDlc(self) -> int:
        return self.canIfRxPduDlc

    def setCanIfRxPduDlc(self, value: int):
        if value is not None:
            self.canIfRxPduDlc = value
        return self

    def getCanIfRxPduId(self) -> int:
        return self.canIfRxPduId

    def setCanIfRxPduId(self, value: int):
        if value is not None:
            self.canIfRxPduId = value
        return self

    def getCanIfRxPduHrhIdRef(self) -> EcucRefType:
        return self.canIfRxPduHrhIdRef

    def setCanIfRxPduHrhIdRef(self, value: EcucRefType):
        if value is not None:
            self.canIfRxPduHrhIdRef = value
        return self

    def getCanIfRxPduUpperLayerRef(self) -> EcucRefType:
        return self.canIfRxPduUpperLayerRef

    def setCanIfRxPduUpperLayerRef(self, value: EcucRefType):
        if value is not None:
            self.canIfRxPduUpperLayerRef = value
        return self


class CanIfTxPduCfg(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canIfTxPduCanId: int = None
        self.canIfTxPduCanIdType: str = None
        self.canIfTxPduDlc: int = None
        self.canIfTxPduId: int = None
        self.canIfTxPduType: str = None
        self.canIfTxPduBufferRef: EcucRefType = None
        self.canIfTxPduHthIdRef: EcucRefType = None
        self.canIfTxPduUpperLayerRef: EcucRefType = None

    def getCanIfTxPduCanId(self) -> int:
        return self.canIfTxPduCanId

    def setCanIfTxPduCanId(self, value: int):
        if value is not None:
            self.canIfTxPduCanId = value
        return self

    def getCanIfTxPduCanIdType(self) -> str:
        return self.canIfTxPduCanIdType

    def setCanIfTxPduCanIdType(self, value: str):
        if value is not None:
            self.canIfTxPduCanIdType = value
        return self

    def getCanIfTxPduDlc(self) -> int:
        return self.canIfTxPduDlc

    def setCanIfTxPduDlc(self, value: int):
        if value is not None:
            self.canIfTxPduDlc = value
        return self

    def getCanIfTxPduId(self) -> int:
        return self.canIfTxPduId

    def setCanIfTxPduId(self, value: int):
        if value is not None:
            self.canIfTxPduId = value
        return self

    def getCanIfTxPduType(self) -> str:
        return self.canIfTxPduType

    def setCanIfTxPduType(self, value: str):
        if value is not None:
            self.canIfTxPduType = value
        return self

    def getCanIfTxPduBufferRef(self) -> EcucRefType:
        return self.canIfTxPduBufferRef

    def setCanIfTxPduBufferRef(self, value: EcucRefType):
        if value is not None:
            self.canIfTxPduBufferRef = value
        return self

    def getCanIfTxPduHthIdRef(self) -> EcucRefType:
        return self.canIfTxPduHthIdRef

    def setCanIfTxPduHthIdRef(self, value: EcucRefType):
        if value is not None:
            self.canIfTxPduHthIdRef = value
        return self

    def getCanIfTxPduUpperLayerRef(self) -> EcucRefType:
        return self.canIfTxPduUpperLayerRef

    def setCanIfTxPduUpperLayerRef(self, value: EcucRefType):
        if value is not None:
            self.canIfTxPduUpperLayerRef = value
        return self


class CanIf(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "CanIf")

        self.canIfGeneral: CanIfGeneral = None
        self.canIfCtrlCfgs: List[CanIfCtrlCfg] = []
        self.canIfTrcvCfgs: List[CanIfTrcvCfg] = []
        self.canIfDispatchCfg: CanIfDispatchCfg = None
        self.canIfBufferCfgs: List[CanIfBufferCfg] = []
        self.canIfHrhCfgs: List[CanIfHrhCfg] = []
        self.canIfHthCfgs: List[CanIfHthCfg] = []
        self.canIfRxPduCfgs: List[CanIfRxPduCfg] = []
        self.canIfTxPduCfgs: List[CanIfTxPduCfg] = []

        self.logger = logging.getLogger()

    def getCanIfGeneral(self) -> CanIfGeneral:
        return self.canIfGeneral

    def setCanIfGeneral(self, value: CanIfGeneral):
        if value is not None:
            self.canIfGeneral = value
        return self

    def getCanIfCtrlCfgList(self) -> List[CanIfCtrlCfg]:
        return list(sorted(filter(lambda a: isinstance(a, CanIfCtrlCfg), self.elements.values()), key=lambda o: o.getName()))

    def addCanIfCtrlCfg(self, value: CanIfCtrlCfg):
        self.addElement(value)
        self.canIfCtrlCfgs.append(value)
        return self

    def getCanIfTrcvCfgList(self) -> List[CanIfTrcvCfg]:
        return list(sorted(filter(lambda a: isinstance(a, CanIfTrcvCfg), self.elements.values()), key=lambda o: o.getName()))

    def addCanIfTrcvCfg(self, value: CanIfTrcvCfg):
        self.addElement(value)
        self.canIfTrcvCfgs.append(value)
        return self

    def getCanIfDispatchCfg(self) -> CanIfDispatchCfg:
        return self.canIfDispatchCfg

    def setCanIfDispatchCfg(self, value: CanIfDispatchCfg):
        if value is not None:
            self.canIfDispatchCfg = value
        return self

    def getCanIfBufferCfgList(self) -> List[CanIfBufferCfg]:
        return list(sorted(filter(lambda a: isinstance(a, CanIfBufferCfg), self.elements.values()), key=lambda o: o.getName()))

    def addCanIfBufferCfg(self, value: CanIfBufferCfg):
        self.addElement(value)
        self.canIfBufferCfgs.append(value)
        return self

    def getCanIfHrhCfgList(self) -> List[CanIfHrhCfg]:
        return list(sorted(filter(lambda a: isinstance(a, CanIfHrhCfg), self.elements.values()), key=lambda o: o.getName()))

    def addCanIfHrhCfg(self, value: CanIfHrhCfg):
        self.addElement(value)
        self.canIfHrhCfgs.append(value)
        return self

    def getCanIfHthCfgList(self) -> List[CanIfHthCfg]:
        return list(sorted(filter(lambda a: isinstance(a, CanIfHthCfg), self.elements.values()), key=lambda o: o.getName()))

    def addCanIfHthCfg(self, value: CanIfHthCfg):
        self.addElement(value)
        self.canIfHthCfgs.append(value)
        return self

    def getCanIfRxPduCfgList(self) -> List[CanIfRxPduCfg]:
        return list(sorted(filter(lambda a: isinstance(a, CanIfRxPduCfg), self.elements.values()), key=lambda o: o.getName()))

    def addCanIfRxPduCfg(self, value: CanIfRxPduCfg):
        self.addElement(value)
        self.canIfRxPduCfgs.append(value)
        return self

    def getCanIfTxPduCfgList(self) -> List[CanIfTxPduCfg]:
        return list(sorted(filter(lambda a: isinstance(a, CanIfTxPduCfg), self.elements.values()), key=lambda o: o.getName()))

    def addCanIfTxPduCfg(self, value: CanIfTxPduCfg):
        self.addElement(value)
        self.canIfTxPduCfgs.append(value)
        return self
