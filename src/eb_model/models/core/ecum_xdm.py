from typing import List
import logging
from .abstract import EcucParamConfContainerDef, EcucRefType, Module  # noqa F401


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


class EcuMCommonConfiguration(EcucParamConfContainerDef):
    """
    Common configuration for EcuM module.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumDevErrorDetect: bool = None
        self.ecumIncludeDem: bool = None
        self.ecumIncludeDet: bool = None
        self.ecumMainFunctionPeriod: float = None

    def getEcumDevErrorDetect(self) -> bool:
        return self.ecumDevErrorDetect

    def setEcumDevErrorDetect(self, value: bool):
        if value is not None:
            self.ecumDevErrorDetect = value
        return self

    def getEcumIncludeDem(self) -> bool:
        return self.ecumIncludeDem

    def setEcumIncludeDem(self, value: bool):
        if value is not None:
            self.ecumIncludeDem = value
        return self

    def getEcumIncludeDet(self) -> bool:
        return self.ecumIncludeDet

    def setEcumIncludeDet(self, value: bool):
        if value is not None:
            self.ecumIncludeDet = value
        return self

    def getEcumMainFunctionPeriod(self) -> float:
        return self.ecumMainFunctionPeriod

    def setEcumMainFunctionPeriod(self, value: float):
        if value is not None:
            self.ecumMainFunctionPeriod = value
        return self


class EcuMDefaultShutdownTarget(EcucParamConfContainerDef):
    """
    Default shutdown target configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumDefaultShutdownTargetRef: EcucRefType = None

    def getEcumDefaultShutdownTargetRef(self) -> EcucRefType:
        return self.ecumDefaultShutdownTargetRef

    def setEcumDefaultShutdownTargetRef(self, value: EcucRefType):
        if value is not None:
            self.ecumDefaultShutdownTargetRef = value
        return self


class EcuMDriverInitItem(EcucParamConfContainerDef):
    """
    Driver initialization item.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumDriverInitRef: EcucRefType = None

    def getEcumDriverInitRef(self) -> EcucRefType:
        return self.ecumDriverInitRef

    def setEcumDriverInitRef(self, value: EcucRefType):
        if value is not None:
            self.ecumDriverInitRef = value
        return self


class EcuMDriverInitListOne(EcucParamConfContainerDef):
    """
    Driver initialization list one.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumDriverInitItems: List[EcuMDriverInitItem] = []

    def getEcumDriverInitItemList(self) -> List[EcuMDriverInitItem]:
        return self.ecumDriverInitItems

    def addEcumDriverInitItem(self, value: EcuMDriverInitItem):
        self.ecumDriverInitItems.append(value)
        return self


class EcuMDriverInitListZero(EcucParamConfContainerDef):
    """
    Driver initialization list zero.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumDriverInitItems: List[EcuMDriverInitItem] = []

    def getEcumDriverInitItemList(self) -> List[EcuMDriverInitItem]:
        return self.ecumDriverInitItems

    def addEcumDriverInitItem(self, value: EcuMDriverInitItem):
        self.ecumDriverInitItems.append(value)
        return self


class EcuMDriverRestartList(EcucParamConfContainerDef):
    """
    Driver restart list.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumDriverInitItems: List[EcuMDriverInitItem] = []

    def getEcumDriverInitItemList(self) -> List[EcuMDriverInitItem]:
        return self.ecumDriverInitItems

    def addEcumDriverInitItem(self, value: EcuMDriverInitItem):
        self.ecumDriverInitItems.append(value)
        return self


class EcuMSleepMode(EcucParamConfContainerDef):
    """
    Sleep mode configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumSleepModeRef: EcucRefType = None
        self.ecumCancelShutdown: bool = None

    def getEcumSleepModeRef(self) -> EcucRefType:
        return self.ecumSleepModeRef

    def setEcumSleepModeRef(self, value: EcucRefType):
        if value is not None:
            self.ecumSleepModeRef = value
        return self

    def getEcumCancelShutdown(self) -> bool:
        return self.ecumCancelShutdown

    def setEcumCancelShutdown(self, value: bool):
        if value is not None:
            self.ecumCancelShutdown = value
        return self


class EcuMWakeupSource(EcucParamConfContainerDef):
    """
    Wakeup source configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumWakeupSourceRef: EcucRefType = None
        self.ecumEnableWakeupValidation: bool = None

    def getEcumWakeupSourceRef(self) -> EcucRefType:
        return self.ecumWakeupSourceRef

    def setEcumWakeupSourceRef(self, value: EcucRefType):
        if value is not None:
            self.ecumWakeupSourceRef = value
        return self

    def getEcumEnableWakeupValidation(self) -> bool:
        return self.ecumEnableWakeupValidation

    def setEcumEnableWakeupValidation(self, value: bool):
        if value is not None:
            self.ecumEnableWakeupValidation = value
        return self


class EcuMDemEventParameterRefs(EcucParamConfContainerDef):
    """
    DEM event parameter references.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumDemEventParameterRef: EcucRefType = None

    def getEcumDemEventParameterRef(self) -> EcucRefType:
        return self.ecumDemEventParameterRef

    def setEcumDemEventParameterRef(self, value: EcucRefType):
        if value is not None:
            self.ecumDemEventParameterRef = value
        return self


class EcuMFixedConfiguration(EcucParamConfContainerDef):
    """
    Fixed configuration for EcuM module.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumMaxSleepModeCounter: int = None
        self.ecumInitCheck: bool = None

    def getEcumMaxSleepModeCounter(self) -> int:
        return self.ecumMaxSleepModeCounter

    def setEcumMaxSleepModeCounter(self, value: int):
        if value is not None:
            self.ecumMaxSleepModeCounter = value
        return self

    def getEcumInitCheck(self) -> bool:
        return self.ecumInitCheck

    def setEcumInitCheck(self, value: bool):
        if value is not None:
            self.ecumInitCheck = value
        return self


class EcuMDriverInitListThree(EcucParamConfContainerDef):
    """
    Driver initialization list three.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumDriverInitItems: List[EcuMDriverInitItem] = []

    def getEcumDriverInitItemList(self) -> List[EcuMDriverInitItem]:
        return self.ecumDriverInitItems

    def addEcumDriverInitItem(self, value: EcuMDriverInitItem):
        self.ecumDriverInitItems.append(value)
        return self


class EcuMDriverInitListTwo(EcucParamConfContainerDef):
    """
    Driver initialization list two.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumDriverInitItems: List[EcuMDriverInitItem] = []

    def getEcumDriverInitItemList(self) -> List[EcuMDriverInitItem]:
        return self.ecumDriverInitItems

    def addEcumDriverInitItem(self, value: EcuMDriverInitItem):
        self.ecumDriverInitItems.append(value)
        return self


class EcuMFixedUserConfig(EcucParamConfContainerDef):
    """
    Fixed user configuration for EcuM module.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumEnableUserPostBuild: bool = None

    def getEcumEnableUserPostBuild(self) -> bool:
        return self.ecumEnableUserPostBuild

    def setEcumEnableUserPostBuild(self, value: bool):
        if value is not None:
            self.ecumEnableUserPostBuild = value
        return self


class EcuMTTII(EcucParamConfContainerDef):
    """
    Two Timer Interrupt Indicator configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumTtiiPrepSleepDuration: int = None
        self.ecumTtiiWakeupDuration: int = None

    def getEcumTtiiPrepSleepDuration(self) -> int:
        return self.ecumTtiiPrepSleepDuration

    def setEcumTtiiPrepSleepDuration(self, value: int):
        if value is not None:
            self.ecumTtiiPrepSleepDuration = value
        return self

    def getEcumTtiiWakeupDuration(self) -> int:
        return self.ecumTtiiWakeupDuration

    def setEcumTtiiWakeupDuration(self, value: int):
        if value is not None:
            self.ecumTtiiWakeupDuration = value
        return self


class EcuMWdgM(EcucParamConfContainerDef):
    """
    Watchdog Manager configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumWdgMTriggerWithOs: bool = None
        self.ecumWdgMSupervisionRef: EcucRefType = None

    def getEcumWdgMTriggerWithOs(self) -> bool:
        return self.ecumWdgMTriggerWithOs

    def setEcumWdgMTriggerWithOs(self, value: bool):
        if value is not None:
            self.ecumWdgMTriggerWithOs = value
        return self

    def getEcumWdgMSupervisionRef(self) -> EcucRefType:
        return self.ecumWdgMSupervisionRef

    def setEcumWdgMSupervisionRef(self, value: EcucRefType):
        if value is not None:
            self.ecumWdgMSupervisionRef = value
        return self


class EcuMFlexConfiguration(EcucParamConfContainerDef):
    """
    Flexible configuration for EcuM module.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumRunPostBuild: bool = None

    def getEcumRunPostBuild(self) -> bool:
        return self.ecumRunPostBuild

    def setEcumRunPostBuild(self, value: bool):
        if value is not None:
            self.ecumRunPostBuild = value
        return self


class EcuMAlarmClock(EcucParamConfContainerDef):
    """
    Alarm clock configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumAlarmClockRef: EcucRefType = None

    def getEcumAlarmClockRef(self) -> EcucRefType:
        return self.ecumAlarmClockRef

    def setEcumAlarmClockRef(self, value: EcucRefType):
        if value is not None:
            self.ecumAlarmClockRef = value
        return self


class EcuMFlexUserConfig(EcucParamConfContainerDef):
    """
    Flexible user configuration for EcuM module.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumEnableUserPostBuild: bool = None

    def getEcumEnableUserPostBuild(self) -> bool:
        return self.ecumEnableUserPostBuild

    def setEcumEnableUserPostBuild(self, value: bool):
        if value is not None:
            self.ecumEnableUserPostBuild = value
        return self


class EcuMGoDownAllowedUsers(EcucParamConfContainerDef):
    """
    Go down allowed users configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumGoDownAllowedUserRef: EcucRefType = None

    def getEcumGoDownAllowedUserRef(self) -> EcucRefType:
        return self.ecumGoDownAllowedUserRef

    def setEcumGoDownAllowedUserRef(self, value: EcucRefType):
        if value is not None:
            self.ecumGoDownAllowedUserRef = value
        return self


class EcuMResetMode(EcucParamConfContainerDef):
    """
    Reset mode configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumResetModeRef: EcucRefType = None

    def getEcumResetModeRef(self) -> EcucRefType:
        return self.ecumResetModeRef

    def setEcumResetModeRef(self, value: EcucRefType):
        if value is not None:
            self.ecumResetModeRef = value
        return self


class EcuMSetClockAllowedUsers(EcucParamConfContainerDef):
    """
    Set clock allowed users configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumSetClockAllowedUserRef: EcucRefType = None

    def getEcumSetClockAllowedUserRef(self) -> EcucRefType:
        return self.ecumSetClockAllowedUserRef

    def setEcumSetClockAllowedUserRef(self, value: EcucRefType):
        if value is not None:
            self.ecumSetClockAllowedUserRef = value
        return self


class EcuMShutdownCause(EcucParamConfContainerDef):
    """
    Shutdown cause configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumShutdownCauseRef: EcucRefType = None
        self.ecumShutdownTargetRef: EcucRefType = None

    def getEcumShutdownCauseRef(self) -> EcucRefType:
        return self.ecumShutdownCauseRef

    def setEcumShutdownCauseRef(self, value: EcucRefType):
        if value is not None:
            self.ecumShutdownCauseRef = value
        return self

    def getEcumShutdownTargetRef(self) -> EcucRefType:
        return self.ecumShutdownTargetRef

    def setEcumShutdownTargetRef(self, value: EcucRefType):
        if value is not None:
            self.ecumShutdownTargetRef = value
        return self


class EcuMShutdownTarget(EcucParamConfContainerDef):
    """
    Shutdown target configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumShutdownTargetType: str = None
        self.ecumResetModeRef: EcucRefType = None

    def getEcumShutdownTargetType(self) -> str:
        return self.ecumShutdownTargetType

    def setEcumShutdownTargetType(self, value: str):
        if value is not None:
            self.ecumShutdownTargetType = value
        return self

    def getEcumResetModeRef(self) -> EcucRefType:
        return self.ecumResetModeRef

    def setEcumResetModeRef(self, value: EcucRefType):
        if value is not None:
            self.ecumResetModeRef = value
        return self


class EcuMDefensiveProgramming(EcucParamConfContainerDef):
    """
    Defensive programming configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumDevErrorDetect: bool = None
        self.ecumNullPointerCheck: bool = None

    def getEcumDevErrorDetect(self) -> bool:
        return self.ecumDevErrorDetect

    def setEcumDevErrorDetect(self, value: bool):
        if value is not None:
            self.ecumDevErrorDetect = value
        return self

    def getEcumNullPointerCheck(self) -> bool:
        return self.ecumNullPointerCheck

    def setEcumNullPointerCheck(self, value: bool):
        if value is not None:
            self.ecumNullPointerCheck = value
        return self


class EcuMFixedGeneral(EcucParamConfContainerDef):
    """
    Fixed general configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumDevErrorDetect: bool = None
        self.ecumMainFunctionPeriod: float = None

    def getEcumDevErrorDetect(self) -> bool:
        return self.ecumDevErrorDetect

    def setEcumDevErrorDetect(self, value: bool):
        if value is not None:
            self.ecumDevErrorDetect = value
        return self

    def getEcumMainFunctionPeriod(self) -> float:
        return self.ecumMainFunctionPeriod

    def setEcumMainFunctionPeriod(self, value: float):
        if value is not None:
            self.ecumMainFunctionPeriod = value
        return self


class EcuMFlexGeneral(EcucParamConfContainerDef):
    """
    Flexible general configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumDevErrorDetect: bool = None
        self.ecumMainFunctionPeriod: float = None

    def getEcumDevErrorDetect(self) -> bool:
        return self.ecumDevErrorDetect

    def setEcumDevErrorDetect(self, value: bool):
        if value is not None:
            self.ecumDevErrorDetect = value
        return self

    def getEcumMainFunctionPeriod(self) -> float:
        return self.ecumMainFunctionPeriod

    def setEcumMainFunctionPeriod(self, value: float):
        if value is not None:
            self.ecumMainFunctionPeriod = value
        return self


class EcuMServiceAPI(EcucParamConfContainerDef):
    """
    Service API configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumReportErrorNotification: bool = None
        self.ecumVersionInfoApi: bool = None

    def getEcumReportErrorNotification(self) -> bool:
        return self.ecumReportErrorNotification

    def setEcumReportErrorNotification(self, value: bool):
        if value is not None:
            self.ecumReportErrorNotification = value
        return self

    def getEcumVersionInfoApi(self) -> bool:
        return self.ecumVersionInfoApi

    def setEcumVersionInfoApi(self, value: bool):
        if value is not None:
            self.ecumVersionInfoApi = value
        return self


class ReportToDem(EcucParamConfContainerDef):
    """
    Report to DEM configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumDemEventIdRef: EcucRefType = None

    def getEcumDemEventIdRef(self) -> EcucRefType:
        return self.ecumDemEventIdRef

    def setEcumDemEventIdRef(self, value: EcucRefType):
        if value is not None:
            self.ecumDemEventIdRef = value
        return self


class EcuMStartup(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumEnableUserMcuStartup: bool = None
        self.ecumUserMcuStartupRef: EcucRefType = None

    def getEcumEnableUserMcuStartup(self) -> bool:
        return self.ecumEnableUserMcuStartup

    def setEcumEnableUserMcuStartup(self, value: bool):
        if value is not None:
            self.ecumEnableUserMcuStartup = value
        return self

    def getEcumUserMcuStartupRef(self) -> EcucRefType:
        return self.ecumUserMcuStartupRef

    def setEcumUserMcuStartupRef(self, value: EcucRefType):
        if value is not None:
            self.ecumUserMcuStartupRef = value
        return self


class EcuMShutdown(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumEnableUserMcuShutdown: bool = None
        self.ecumUserMcuShutdownRef: EcucRefType = None

    def getEcumEnableUserMcuShutdown(self) -> bool:
        return self.ecumEnableUserMcuShutdown

    def setEcumEnableUserMcuShutdown(self, value: bool):
        if value is not None:
            self.ecumEnableUserMcuShutdown = value
        return self

    def getEcumUserMcuShutdownRef(self) -> EcucRefType:
        return self.ecumUserMcuShutdownRef

    def setEcumUserMcuShutdownRef(self, value: EcucRefType):
        if value is not None:
            self.ecumUserMcuShutdownRef = value
        return self


class EcuMAlarm(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumAlarmCounterRef: EcucRefType = None
        self.ecumAlarmActionRef: EcucRefType = None

    def getEcumAlarmCounterRef(self) -> EcucRefType:
        return self.ecumAlarmCounterRef

    def setEcumAlarmCounterRef(self, value: EcucRefType):
        if value is not None:
            self.ecumAlarmCounterRef = value
        return self

    def getEcumAlarmActionRef(self) -> EcucRefType:
        return self.ecumAlarmActionRef

    def setEcumAlarmActionRef(self, value: EcucRefType):
        if value is not None:
            self.ecumAlarmActionRef = value
        return self


class EcuMGeneral(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ecumDevErrorDetect: bool = None
        self.ecumConfigurationVariant: str = None
        self.ecumIncludeDem: bool = None
        self.ecumIncludeDet: bool = None
        self.ecumMainFunctionPeriod: float = None

    def getEcumDevErrorDetect(self) -> bool:
        return self.ecumDevErrorDetect

    def setEcumDevErrorDetect(self, value: bool):
        if value is not None:
            self.ecumDevErrorDetect = value
        return self

    def getEcumConfigurationVariant(self) -> str:
        return self.ecumConfigurationVariant

    def setEcumConfigurationVariant(self, value: str):
        if value is not None:
            self.ecumConfigurationVariant = value
        return self

    def getEcumIncludeDem(self) -> bool:
        return self.ecumIncludeDem

    def setEcumIncludeDem(self, value: bool):
        if value is not None:
            self.ecumIncludeDem = value
        return self

    def getEcumIncludeDet(self) -> bool:
        return self.ecumIncludeDet

    def setEcumIncludeDet(self, value: bool):
        if value is not None:
            self.ecumIncludeDet = value
        return self

    def getEcumMainFunctionPeriod(self) -> float:
        return self.ecumMainFunctionPeriod

    def setEcumMainFunctionPeriod(self, value: float):
        if value is not None:
            self.ecumMainFunctionPeriod = value
        return self


class EcuM(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "EcuM")

        self.ecumGeneral: EcuMGeneral = None
        self.ecumStartup: EcuMStartup = None
        self.ecumShutdown: EcuMShutdown = None
        self.ecumAlarms: List[EcuMAlarm] = []
        self.commonPublishedInformation: CommonPublishedInformation = None
        self.publishedInformation: PublishedInformation = None
        self.ecumCommonConfiguration: EcuMCommonConfiguration = None
        self.ecumDefaultShutdownTarget: EcuMDefaultShutdownTarget = None
        self.ecumDriverInitListOne: EcuMDriverInitListOne = None
        self.ecumDriverInitListZero: EcuMDriverInitListZero = None
        self.ecumDriverRestartList: EcuMDriverRestartList = None
        self.ecumSleepModes: List[EcuMSleepMode] = []
        self.ecumWakeupSources: List[EcuMWakeupSource] = []
        self.ecumDemEventParameterRefs: List[EcuMDemEventParameterRefs] = []
        self.ecumFixedConfiguration: EcuMFixedConfiguration = None
        self.ecumDriverInitListThree: EcuMDriverInitListThree = None
        self.ecumDriverInitListTwo: EcuMDriverInitListTwo = None
        self.ecumFixedUserConfig: EcuMFixedUserConfig = None
        self.ecumTtii: EcuMTTII = None
        self.ecumWdgM: EcuMWdgM = None
        self.ecumFlexConfiguration: EcuMFlexConfiguration = None
        self.ecumAlarmClock: EcuMAlarmClock = None
        self.ecumFlexUserConfig: EcuMFlexUserConfig = None
        self.ecumGoDownAllowedUsers: List[EcuMGoDownAllowedUsers] = []
        self.ecumResetModes: List[EcuMResetMode] = []
        self.ecumSetClockAllowedUsers: List[EcuMSetClockAllowedUsers] = []
        self.ecumShutdownCauses: List[EcuMShutdownCause] = []
        self.ecumShutdownTargets: List[EcuMShutdownTarget] = []
        self.ecumDefensiveProgramming: EcuMDefensiveProgramming = None
        self.ecumFixedGeneral: EcuMFixedGeneral = None
        self.ecumFlexGeneral: EcuMFlexGeneral = None
        self.ecumServiceAPI: EcuMServiceAPI = None
        self.reportToDem: ReportToDem = None

        self.logger = logging.getLogger()

    def getEcumGeneral(self) -> EcuMGeneral:
        return self.ecumGeneral

    def setEcumGeneral(self, value: EcuMGeneral):
        if value is not None:
            self.ecumGeneral = value
        return self

    def getEcumStartup(self) -> EcuMStartup:
        return self.ecumStartup

    def setEcumStartup(self, value: EcuMStartup):
        if value is not None:
            self.ecumStartup = value
        return self

    def getEcumShutdown(self) -> EcuMShutdown:
        return self.ecumShutdown

    def setEcumShutdown(self, value: EcuMShutdown):
        if value is not None:
            self.ecumShutdown = value
        return self

    def getEcumAlarmList(self) -> List[EcuMAlarm]:
        return list(sorted(filter(lambda a: isinstance(a, EcuMAlarm), self.elements.values()), key=lambda o: o.getName()))

    def addEcumAlarm(self, value: EcuMAlarm):
        self.addElement(value)
        self.ecumAlarms.append(value)
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

    def getEcumCommonConfiguration(self) -> EcuMCommonConfiguration:
        return self.ecumCommonConfiguration

    def setEcumCommonConfiguration(self, value: EcuMCommonConfiguration):
        if value is not None:
            self.ecumCommonConfiguration = value
        return self

    def getEcumDefaultShutdownTarget(self) -> EcuMDefaultShutdownTarget:
        return self.ecumDefaultShutdownTarget

    def setEcumDefaultShutdownTarget(self, value: EcuMDefaultShutdownTarget):
        if value is not None:
            self.ecumDefaultShutdownTarget = value
        return self

    def getEcumDriverInitListOne(self) -> EcuMDriverInitListOne:
        return self.ecumDriverInitListOne

    def setEcumDriverInitListOne(self, value: EcuMDriverInitListOne):
        if value is not None:
            self.ecumDriverInitListOne = value
        return self

    def getEcumDriverInitListZero(self) -> EcuMDriverInitListZero:
        return self.ecumDriverInitListZero

    def setEcumDriverInitListZero(self, value: EcuMDriverInitListZero):
        if value is not None:
            self.ecumDriverInitListZero = value
        return self

    def getEcumDriverRestartList(self) -> EcuMDriverRestartList:
        return self.ecumDriverRestartList

    def setEcumDriverRestartList(self, value: EcuMDriverRestartList):
        if value is not None:
            self.ecumDriverRestartList = value
        return self

    def getEcumSleepModeList(self) -> List[EcuMSleepMode]:
        return list(sorted(filter(lambda a: isinstance(a, EcuMSleepMode), self.elements.values()), key=lambda o: o.getName()))

    def addEcumSleepMode(self, value: EcuMSleepMode):
        self.addElement(value)
        self.ecumSleepModes.append(value)
        return self

    def getEcumWakeupSourceList(self) -> List[EcuMWakeupSource]:
        return list(sorted(filter(lambda a: isinstance(a, EcuMWakeupSource), self.elements.values()), key=lambda o: o.getName()))

    def addEcumWakeupSource(self, value: EcuMWakeupSource):
        self.addElement(value)
        self.ecumWakeupSources.append(value)
        return self

    def getEcumDemEventParameterRefList(self) -> List[EcuMDemEventParameterRefs]:
        return list(sorted(filter(lambda a: isinstance(a, EcuMDemEventParameterRefs), self.elements.values()), key=lambda o: o.getName()))

    def addEcumDemEventParameterRef(self, value: EcuMDemEventParameterRefs):
        self.addElement(value)
        self.ecumDemEventParameterRefs.append(value)
        return self

    def getEcumFixedConfiguration(self) -> EcuMFixedConfiguration:
        return self.ecumFixedConfiguration

    def setEcumFixedConfiguration(self, value: EcuMFixedConfiguration):
        if value is not None:
            self.ecumFixedConfiguration = value
        return self

    def getEcumDriverInitListThree(self) -> EcuMDriverInitListThree:
        return self.ecumDriverInitListThree

    def setEcumDriverInitListThree(self, value: EcuMDriverInitListThree):
        if value is not None:
            self.ecumDriverInitListThree = value
        return self

    def getEcumDriverInitListTwo(self) -> EcuMDriverInitListTwo:
        return self.ecumDriverInitListTwo

    def setEcumDriverInitListTwo(self, value: EcuMDriverInitListTwo):
        if value is not None:
            self.ecumDriverInitListTwo = value
        return self

    def getEcumFixedUserConfig(self) -> EcuMFixedUserConfig:
        return self.ecumFixedUserConfig

    def setEcumFixedUserConfig(self, value: EcuMFixedUserConfig):
        if value is not None:
            self.ecumFixedUserConfig = value
        return self

    def getEcumTtii(self) -> EcuMTTII:
        return self.ecumTtii

    def setEcumTtii(self, value: EcuMTTII):
        if value is not None:
            self.ecumTtii = value
        return self

    def getEcumWdgM(self) -> EcuMWdgM:
        return self.ecumWdgM

    def setEcumWdgM(self, value: EcuMWdgM):
        if value is not None:
            self.ecumWdgM = value
        return self

    def getEcumFlexConfiguration(self) -> EcuMFlexConfiguration:
        return self.ecumFlexConfiguration

    def setEcumFlexConfiguration(self, value: EcuMFlexConfiguration):
        if value is not None:
            self.ecumFlexConfiguration = value
        return self

    def getEcumAlarmClock(self) -> EcuMAlarmClock:
        return self.ecumAlarmClock

    def setEcumAlarmClock(self, value: EcuMAlarmClock):
        if value is not None:
            self.ecumAlarmClock = value
        return self

    def getEcumFlexUserConfig(self) -> EcuMFlexUserConfig:
        return self.ecumFlexUserConfig

    def setEcumFlexUserConfig(self, value: EcuMFlexUserConfig):
        if value is not None:
            self.ecumFlexUserConfig = value
        return self

    def getEcumGoDownAllowedUserList(self) -> List[EcuMGoDownAllowedUsers]:
        return list(sorted(filter(lambda a: isinstance(a, EcuMGoDownAllowedUsers), self.elements.values()), key=lambda o: o.getName()))

    def addEcumGoDownAllowedUser(self, value: EcuMGoDownAllowedUsers):
        self.addElement(value)
        self.ecumGoDownAllowedUsers.append(value)
        return self

    def getEcumResetModeList(self) -> List[EcuMResetMode]:
        return list(sorted(filter(lambda a: isinstance(a, EcuMResetMode), self.elements.values()), key=lambda o: o.getName()))

    def addEcumResetMode(self, value: EcuMResetMode):
        self.addElement(value)
        self.ecumResetModes.append(value)
        return self

    def getEcumSetClockAllowedUserList(self) -> List[EcuMSetClockAllowedUsers]:
        return list(sorted(filter(lambda a: isinstance(a, EcuMSetClockAllowedUsers), self.elements.values()), key=lambda o: o.getName()))

    def addEcumSetClockAllowedUser(self, value: EcuMSetClockAllowedUsers):
        self.addElement(value)
        self.ecumSetClockAllowedUsers.append(value)
        return self

    def getEcumShutdownCauseList(self) -> List[EcuMShutdownCause]:
        return list(sorted(filter(lambda a: isinstance(a, EcuMShutdownCause), self.elements.values()), key=lambda o: o.getName()))

    def addEcumShutdownCause(self, value: EcuMShutdownCause):
        self.addElement(value)
        self.ecumShutdownCauses.append(value)
        return self

    def getEcumShutdownTargetList(self) -> List[EcuMShutdownTarget]:
        return list(sorted(filter(lambda a: isinstance(a, EcuMShutdownTarget), self.elements.values()), key=lambda o: o.getName()))

    def addEcumShutdownTarget(self, value: EcuMShutdownTarget):
        self.addElement(value)
        self.ecumShutdownTargets.append(value)
        return self

    def getEcumDefensiveProgramming(self) -> EcuMDefensiveProgramming:
        return self.ecumDefensiveProgramming

    def setEcumDefensiveProgramming(self, value: EcuMDefensiveProgramming):
        if value is not None:
            self.ecumDefensiveProgramming = value
        return self

    def getEcumFixedGeneral(self) -> EcuMFixedGeneral:
        return self.ecumFixedGeneral

    def setEcumFixedGeneral(self, value: EcuMFixedGeneral):
        if value is not None:
            self.ecumFixedGeneral = value
        return self

    def getEcumFlexGeneral(self) -> EcuMFlexGeneral:
        return self.ecumFlexGeneral

    def setEcumFlexGeneral(self, value: EcuMFlexGeneral):
        if value is not None:
            self.ecumFlexGeneral = value
        return self

    def getEcumServiceAPI(self) -> EcuMServiceAPI:
        return self.ecumServiceAPI

    def setEcumServiceAPI(self, value: EcuMServiceAPI):
        if value is not None:
            self.ecumServiceAPI = value
        return self

    def getReportToDem(self) -> ReportToDem:
        return self.reportToDem

    def setReportToDem(self, value: ReportToDem):
        if value is not None:
            self.reportToDem = value
        return self
