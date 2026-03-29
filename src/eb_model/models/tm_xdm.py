from typing import List
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module  # noqa F401


class CommonPublishedInformation(EcucParamConfContainerDef):
    """
    Common published information containing AUTOSAR version information.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.arMajorVersion: int = None
        self.arMinorVersion: int = None
        self.arPatchVersion: int = None
        self.swMajorVersion: int = None
        self.swMinorVersion: int = None
        self.swPatchVersion: int = None

    def getArMajorVersion(self) -> int:
        return self.arMajorVersion

    def setArMajorVersion(self, value: int):
        if value is not None:
            self.arMajorVersion = value
        return self

    def getArMinorVersion(self) -> int:
        return self.arMinorVersion

    def setArMinorVersion(self, value: int):
        if value is not None:
            self.arMinorVersion = value
        return self

    def getArPatchVersion(self) -> int:
        return self.arPatchVersion

    def setArPatchVersion(self, value: int):
        if value is not None:
            self.arPatchVersion = value
        return self

    def getSwMajorVersion(self) -> int:
        return self.swMajorVersion

    def setSwMajorVersion(self, value: int):
        if value is not None:
            self.swMajorVersion = value
        return self

    def getSwMinorVersion(self) -> int:
        return self.swMinorVersion

    def setSwMinorVersion(self, value: int):
        if value is not None:
            self.swMinorVersion = value
        return self

    def getSwPatchVersion(self) -> int:
        return self.swPatchVersion

    def setSwPatchVersion(self, value: int):
        if value is not None:
            self.swPatchVersion = value
        return self


class PublishedInformation(EcucParamConfContainerDef):
    """
    Module-specific published information.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.vendorId: str = None
        self.arReleaseMajorVersion: str = None
        self.arReleaseMinorVersion: str = None
        self.arReleasePatchVersion: str = None
        self.swMajorVersion: str = None
        self.swMinorVersion: str = None
        self.swPatchVersion: str = None

    def getVendorId(self) -> str:
        return self.vendorId

    def setVendorId(self, value: str):
        if value is not None:
            self.vendorId = value
        return self

    def getArReleaseMajorVersion(self) -> str:
        return self.arReleaseMajorVersion

    def setArReleaseMajorVersion(self, value: str):
        if value is not None:
            self.arReleaseMajorVersion = value
        return self

    def getArReleaseMinorVersion(self) -> str:
        return self.arReleaseMinorVersion

    def setArReleaseMinorVersion(self, value: str):
        if value is not None:
            self.arReleaseMinorVersion = value
        return self

    def getArReleasePatchVersion(self) -> str:
        return self.arReleasePatchVersion

    def setArReleasePatchVersion(self, value: str):
        if value is not None:
            self.arReleasePatchVersion = value
        return self

    def getSwMajorVersion(self) -> str:
        return self.swMajorVersion

    def setSwMajorVersion(self, value: str):
        if value is not None:
            self.swMajorVersion = value
        return self

    def getSwMinorVersion(self) -> str:
        return self.swMinorVersion

    def setSwMinorVersion(self, value: str):
        if value is not None:
            self.swMinorVersion = value
        return self

    def getSwPatchVersion(self) -> str:
        return self.swPatchVersion

    def setSwPatchVersion(self, value: str):
        if value is not None:
            self.swPatchVersion = value
        return self


class TmGeneral(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.tmDevErrorDetect: bool = None
        self.tmMainWindowProtect: bool = None
        self.tmVersionInfoApi: bool = None
        self.tmEnablePredefTimer1us16bit: bool = None
        self.tmEnablePredefTimer1us24bit: bool = None
        self.tmEnablePredefTimer1us32bit: bool = None
        self.tmEnablePredefTimer100us32bit: bool = None

    def getTmDevErrorDetect(self) -> bool:
        return self.tmDevErrorDetect

    def setTmDevErrorDetect(self, value: bool):
        if value is not None:
            self.tmDevErrorDetect = value
        return self

    def getTmMainWindowProtect(self) -> bool:
        return self.tmMainWindowProtect

    def setTmMainWindowProtect(self, value: bool):
        if value is not None:
            self.tmMainWindowProtect = value
        return self

    def getTmVersionInfoApi(self) -> bool:
        return self.tmVersionInfoApi

    def setTmVersionInfoApi(self, value: bool):
        if value is not None:
            self.tmVersionInfoApi = value
        return self

    def getTmEnablePredefTimer1us16bit(self) -> bool:
        return self.tmEnablePredefTimer1us16bit

    def setTmEnablePredefTimer1us16bit(self, value: bool):
        if value is not None:
            self.tmEnablePredefTimer1us16bit = value
        return self

    def getTmEnablePredefTimer1us24bit(self) -> bool:
        return self.tmEnablePredefTimer1us24bit

    def setTmEnablePredefTimer1us24bit(self, value: bool):
        if value is not None:
            self.tmEnablePredefTimer1us24bit = value
        return self

    def getTmEnablePredefTimer1us32bit(self) -> bool:
        return self.tmEnablePredefTimer1us32bit

    def setTmEnablePredefTimer1us32bit(self, value: bool):
        if value is not None:
            self.tmEnablePredefTimer1us32bit = value
        return self

    def getTmEnablePredefTimer100us32bit(self) -> bool:
        return self.tmEnablePredefTimer100us32bit

    def setTmEnablePredefTimer100us32bit(self, value: bool):
        if value is not None:
            self.tmEnablePredefTimer100us32bit = value
        return self


class TmInterruptSynchronization(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.tmSyncMode: str = None

    def getTmSyncMode(self) -> str:
        return self.tmSyncMode

    def setTmSyncMode(self, value: str):
        if value is not None:
            self.tmSyncMode = value
        return self


class TmTickTime(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.tmTickTimeBase: int = None
        self.tmTickPriority: int = None

    def getTmTickTimeBase(self) -> int:
        return self.tmTickTimeBase

    def setTmTickTimeBase(self, value: int):
        if value is not None:
            self.tmTickTimeBase = value
        return self

    def getTmTickPriority(self) -> int:
        return self.tmTickPriority

    def setTmTickPriority(self, value: int):
        if value is not None:
            self.tmTickPriority = value
        return self


class TmTrigger(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.tmTriggerChannelRef: EcucRefType = None

    def getTmTriggerChannelRef(self) -> EcucRefType:
        return self.tmTriggerChannelRef

    def setTmTriggerChannelRef(self, value: EcucRefType):
        if value is not None:
            self.tmTriggerChannelRef = value
        return self


class Tm(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "Tm")

        self.tmGeneral: TmGeneral = None
        self.tmInterruptSynchronization: TmInterruptSynchronization = None
        self.tmTickTime: TmTickTime = None
        self.tmTriggers: List[TmTrigger] = []
        self.commonPublishedInformation: CommonPublishedInformation = None
        self.publishedInformation: PublishedInformation = None

        self.logger = logging.getLogger()

    def getTmGeneral(self) -> TmGeneral:
        return self.tmGeneral

    def setTmGeneral(self, value: TmGeneral):
        if value is not None:
            self.tmGeneral = value
        return self

    def getTmInterruptSynchronization(self) -> TmInterruptSynchronization:
        return self.tmInterruptSynchronization

    def setTmInterruptSynchronization(self, value: TmInterruptSynchronization):
        if value is not None:
            self.tmInterruptSynchronization = value
        return self

    def getTmTickTime(self) -> TmTickTime:
        return self.tmTickTime

    def setTmTickTime(self, value: TmTickTime):
        if value is not None:
            self.tmTickTime = value
        return self

    def getTmTriggerList(self) -> List[TmTrigger]:
        return list(sorted(filter(lambda a: isinstance(a, TmTrigger), self.elements.values()), key=lambda o: o.getName()))

    def addTmTrigger(self, value: TmTrigger):
        self.addElement(value)
        self.tmTriggers.append(value)
        return self

    def getCommonPublishedInformation(self) -> CommonPublishedInformation:
        return self.commonPublishedInformation

    def setCommonPublishedInformation(self, value: CommonPublishedInformation):
        if value is not None:
            self.commonPublishedInformation = value
        return self

    def getPublishedInformation(self) -> PublishedInformation:
        return self.publishedInformation

    def setPublishedInformation(self, value: PublishedInformation):
        if value is not None:
            self.publishedInformation = value
        return self
