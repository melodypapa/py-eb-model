from typing import List, Optional
import logging
from eb_model.models.core.abstract import EcucParamConfContainerDef, EcucRefType, Module


class LinSMGeneral(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.linSMDevErrorDetect: bool = None
        self.linSMMainProcessingPeriod: float = None

    def getLinSMDevErrorDetect(self) -> bool:
        return self.linSMDevErrorDetect

    def setLinSMDevErrorDetect(self, value: bool):
        if value is not None:
            self.linSMDevErrorDetect = value
        return self

    def getLinSMMainProcessingPeriod(self) -> float:
        return self.linSMMainProcessingPeriod

    def setLinSMMainProcessingPeriod(self, value: float):
        if value is not None:
            self.linSMMainProcessingPeriod = value
        return self


class LinSMChannel(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.linSMConfirmationTimeout: float = None
        self.linSMSleepSupport: bool = None
        self.linSMComMNetworkHandleRef: EcucRefType = None
        self.linSMNodeType: str = None

    def getLinSMConfirmationTimeout(self) -> float:
        return self.linSMConfirmationTimeout

    def setLinSMConfirmationTimeout(self, value: float):
        if value is not None:
            self.linSMConfirmationTimeout = value
        return self

    def getLinSMSleepSupport(self) -> bool:
        return self.linSMSleepSupport

    def setLinSMSleepSupport(self, value: bool):
        if value is not None:
            self.linSMSleepSupport = value
        return self

    def getLinSMComMNetworkHandleRef(self) -> EcucRefType:
        return self.linSMComMNetworkHandleRef

    def setLinSMComMNetworkHandleRef(self, value: EcucRefType):
        if value is not None:
            self.linSMComMNetworkHandleRef = value
        return self

    def getLinSMNodeType(self) -> str:
        return self.linSMNodeType

    def setLinSMNodeType(self, value: str):
        if value is not None:
            self.linSMNodeType = value
        return self


class LinSM(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "LinSM")
        self.linSMGeneral: LinSMGeneral = None
        self.linSMChannels: List[LinSMChannel] = []
        self.logger = logging.getLogger()

    def getLinSMGeneral(self) -> LinSMGeneral:
        return self.linSMGeneral

    def setLinSMGeneral(self, value: LinSMGeneral):
        if value is not None:
            self.linSMGeneral = value
        return self

    def getLinSMChannelList(self) -> List[LinSMChannel]:
        return list(sorted(filter(lambda a: isinstance(a, LinSMChannel), self.elements.values()), key=lambda o: o.getName()))

    def addLinSMChannel(self, value: LinSMChannel):
        self.addElement(value)
        self.linSMChannels.append(value)
        return self
