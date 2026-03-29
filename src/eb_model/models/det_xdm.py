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


class DetServiceAPI(EcucParamConfContainerDef):
    """
    Service API configuration for Det module.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.detVersionInfoApi: bool = None
        self.detReportRuntimeErrorCallout: bool = None

    def getDetVersionInfoApi(self) -> bool:
        return self.detVersionInfoApi

    def setDetVersionInfoApi(self, value: bool):
        if value is not None:
            self.detVersionInfoApi = value
        return self

    def getDetReportRuntimeErrorCallout(self) -> bool:
        return self.detReportRuntimeErrorCallout

    def setDetReportRuntimeErrorCallout(self, value: bool):
        if value is not None:
            self.detReportRuntimeErrorCallout = value
        return self


class DetNotification(EcucParamConfContainerDef):
    """
    Notification configuration for Det module.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.detErrorNotification: bool = None
        self.detRuntimeErrorNotification: bool = None
        self.detTransitionErrorNotification: bool = None

    def getDetErrorNotification(self) -> bool:
        return self.detErrorNotification

    def setDetErrorNotification(self, value: bool):
        if value is not None:
            self.detErrorNotification = value
        return self

    def getDetRuntimeErrorNotification(self) -> bool:
        return self.detRuntimeErrorNotification

    def setDetRuntimeErrorNotification(self, value: bool):
        if value is not None:
            self.detRuntimeErrorNotification = value
        return self

    def getDetTransitionErrorNotification(self) -> bool:
        return self.detTransitionErrorNotification

    def setDetTransitionErrorNotification(self, value: bool):
        if value is not None:
            self.detTransitionErrorNotification = value
        return self


class DetDefensiveProgramming(EcucParamConfContainerDef):
    """
    Defensive programming configuration for Det module.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.detNullPointerCheck: bool = None
        self.detParameterCheck: bool = None

    def getDetNullPointerCheck(self) -> bool:
        return self.detNullPointerCheck

    def setDetNullPointerCheck(self, value: bool):
        if value is not None:
            self.detNullPointerCheck = value
        return self

    def getDetParameterCheck(self) -> bool:
        return self.detParameterCheck

    def setDetParameterCheck(self, value: bool):
        if value is not None:
            self.detParameterCheck = value
        return self


class SoftwareComponentList(EcucParamConfContainerDef):
    """
    List of software components for Det module.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class InstanceIdList(EcucParamConfContainerDef):
    """
    List of instance IDs for Det module.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class DetErrorHook(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.detErrorHookCallbackName: str = None

    def getDetErrorHookCallbackName(self) -> str:
        return self.detErrorHookCallbackName

    def setDetErrorHookCallbackName(self, value: str):
        if value is not None:
            self.detErrorHookCallbackName = value
        return self


class DetInitError(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.detInitErrorRef: EcucRefType = None

    def getDetInitErrorRef(self) -> EcucRefType:
        return self.detInitErrorRef

    def setDetInitErrorRef(self, value: EcucRefType):
        if value is not None:
            self.detInitErrorRef = value
        return self


class DetGeneral(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.detDevErrorDetect: bool = None
        self.detEnabled: bool = None
        self.detForwardToDlt: bool = None
        self.detVersionInfoApi: bool = None
        self.loggingMode: str = None
        self.bufferSize: int = None

    def getDetDevErrorDetect(self) -> bool:
        return self.detDevErrorDetect

    def setDetDevErrorDetect(self, value: bool):
        if value is not None:
            self.detDevErrorDetect = value
        return self

    def getDetEnabled(self) -> bool:
        return self.detEnabled

    def setDetEnabled(self, value: bool):
        if value is not None:
            self.detEnabled = value
        return self

    def getDetForwardToDlt(self) -> bool:
        return self.detForwardToDlt

    def setDetForwardToDlt(self, value: bool):
        if value is not None:
            self.detForwardToDlt = value
        return self

    def getDetVersionInfoApi(self) -> bool:
        return self.detVersionInfoApi

    def setDetVersionInfoApi(self, value: bool):
        if value is not None:
            self.detVersionInfoApi = value
        return self

    def getLoggingMode(self) -> str:
        return self.loggingMode

    def setLoggingMode(self, value: str):
        if value is not None:
            self.loggingMode = value
        return self

    def getBufferSize(self) -> int:
        return self.bufferSize

    def setBufferSize(self, value: int):
        if value is not None:
            self.bufferSize = value
        return self


class Det(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "Det")

        self.detGeneral: DetGeneral = None
        self.detErrorHook: DetErrorHook = None
        self.detInitError: DetInitError = None
        self.commonPublishedInformation: CommonPublishedInformation = None
        self.publishedInformation: PublishedInformation = None
        self.detServiceAPI: DetServiceAPI = None
        self.detNotification: DetNotification = None
        self.detDefensiveProgramming: DetDefensiveProgramming = None
        self.softwareComponentList: SoftwareComponentList = None
        self.instanceIdList: InstanceIdList = None

        self.logger = logging.getLogger()

    def getDetGeneral(self) -> DetGeneral:
        return self.detGeneral

    def setDetGeneral(self, value: DetGeneral):
        if value is not None:
            self.detGeneral = value
        return self

    def getDetErrorHook(self) -> DetErrorHook:
        return self.detErrorHook

    def setDetErrorHook(self, value: DetErrorHook):
        if value is not None:
            self.detErrorHook = value
        return self

    def getDetInitError(self) -> DetInitError:
        return self.detInitError

    def setDetInitError(self, value: DetInitError):
        if value is not None:
            self.detInitError = value
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

    def getDetServiceAPI(self) -> DetServiceAPI:
        return self.detServiceAPI

    def setDetServiceAPI(self, value: DetServiceAPI):
        if value is not None:
            self.detServiceAPI = value
        return self

    def getDetNotification(self) -> DetNotification:
        return self.detNotification

    def setDetNotification(self, value: DetNotification):
        if value is not None:
            self.detNotification = value
        return self

    def getDetDefensiveProgramming(self) -> DetDefensiveProgramming:
        return self.detDefensiveProgramming

    def setDetDefensiveProgramming(self, value: DetDefensiveProgramming):
        if value is not None:
            self.detDefensiveProgramming = value
        return self

    def getSoftwareComponentList(self) -> SoftwareComponentList:
        return self.softwareComponentList

    def setSoftwareComponentList(self, value: SoftwareComponentList):
        if value is not None:
            self.softwareComponentList = value
        return self

    def getInstanceIdList(self) -> InstanceIdList:
        return self.instanceIdList

    def setInstanceIdList(self, value: InstanceIdList):
        if value is not None:
            self.instanceIdList = value
        return self
