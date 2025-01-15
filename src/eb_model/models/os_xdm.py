from typing import Dict, List
import logging
from ..models.abstract import EcucContainer, EcucObject, EcucRefType, Module


class OsAlarmAction(EcucContainer):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class OsAlarmAutostart(EcucContainer):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osAlarmAlarmTime = None
        self.osAlarmAutostartType = None
        self.osAlarmCycleTime = None
        self.osAlarmAppModeRefs = []

    def getOsAlarmAlarmTime(self):
        return self.osAlarmAlarmTime

    def setOsAlarmAlarmTime(self, value):
        self.osAlarmAlarmTime = value

    def getOsAlarmAutostartType(self):
        return self.osAlarmAutostartType

    def setOsAlarmAutostartType(self, value):
        self.osAlarmAutostartType = value

    def getOsAlarmCycleTime(self):
        return self.osAlarmCycleTime

    def setOsAlarmCycleTime(self, value):
        self.osAlarmCycleTime = value

    def getOsAlarmAppModeRefs(self) -> List[EcucRefType]:
        return self.osAlarmAppModeRefs

    def addOsAlarmAppModeRef(self, ref: EcucRefType):
        self.osAlarmAppModeRefs.append(ref)


class OsAlarmActivateTask(OsAlarmAction):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osAlarmActivateTaskRef = None

    def getOsAlarmActivateTaskRef(self) -> EcucRefType:
        return self.osAlarmActivateTaskRef

    def setOsAlarmActivateTaskRef(self, value: EcucRefType):
        self.osAlarmActivateTaskRef = value


class OsAlarmCallback(OsAlarmAction):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osAlarmCallbackName = None
        self.osMemoryMappingCodeLocationRef = None

    def getOsAlarmCallbackName(self):
        return self.osAlarmCallbackName

    def setOsAlarmCallbackName(self, value):
        self.osAlarmCallbackName = value

    def getOsMemoryMappingCodeLocationRef(self):
        return self.osMemoryMappingCodeLocationRef

    def setOsMemoryMappingCodeLocationRef(self, value):
        self.osMemoryMappingCodeLocationRef = value


class OsAlarmIncrementCounter(OsAlarmAction):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osAlarmIncrementCounterRef = None

    def getOsAlarmIncrementCounterRef(self):
        return self.osAlarmIncrementCounterRef

    def setOsAlarmIncrementCounterRef(self, value):
        self.osAlarmIncrementCounterRef = value


class OsAlarmSetEvent(OsAlarmAction):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osAlarmSetEventRef = None
        self.osAlarmSetEventTaskRef = None

    def getOsAlarmSetEventRef(self) -> EcucRefType:
        return self.osAlarmSetEventRef

    def setOsAlarmSetEventRef(self, value: EcucRefType):
        self.osAlarmSetEventRef = value
        return self

    def getOsAlarmSetEventTaskRef(self) -> EcucRefType:
        return self.osAlarmSetEventTaskRef

    def setOsAlarmSetEventTaskRef(self, value: EcucRefType):
        self.osAlarmSetEventTaskRef = value
        return self


class OsAlarm(EcucContainer):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osAlarmAccessingApplicationRefs = []   # type: List[EcucRefType]
        self.osAlarmCounterRef = None
        self.osAlarmAction = None                   # type: OsAlarmAction
        self.osAlarmAutostart = None

    def getOsAlarmAccessingApplicationRefList(self) -> List[EcucRefType]:
        return self.osAlarmAccessingApplicationRefs

    def addOsAlarmAccessingApplicationRef(self, ref: EcucRefType):
        self.osAlarmAccessingApplicationRefs.append(ref)
        return self

    def getOsAlarmCounterRef(self) -> EcucRefType:
        return self.osAlarmCounterRef

    def setOsAlarmCounterRef(self, value: EcucRefType):
        self.osAlarmCounterRef = value
        return self

    def getOsAlarmAction(self) -> OsAlarmAction:
        return self.osAlarmAction

    def setOsAlarmAction(self, value: OsAlarmAction):
        self.osAlarmAction = value
        return self

    def getOsAlarmAutostart(self) -> OsAlarmAutostart:
        return self.osAlarmAutostart

    def setOsAlarmAutostart(self, value: OsAlarmAutostart):
        self.osAlarmAutostart = value
        return self

    def __str__(self) -> str:
        result = []
        result.append("Name                        : %s" % self.getName())
        result.append("Full Name                   : %s" % self.getFullName())
        result.append("OsAlarmCounterRef           : %s" %
                      self.getOsAlarmCounterRef())
        result.append("OsAlarmAccessingApplication :")
        for ref in self.getOsAlarmAccessingApplicationRefList():
            result.append("    - %s" % ref)

        return "\n".join(result)


class OsApplicationHooks(EcucContainer):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.OsAppErrorHook = False                                     # type: bool
        self.OsAppShutdownHook = False                                  # type: bool
        self.OsAppStartupHook = False                                   # type: bool
        self.OsMemoryMappingCodeLocationRef = None                      # type: EcucRefType

    def getOsAppErrorHook(self):
        return self.OsAppErrorHook

    def setOsAppErrorHook(self, value):
        self.OsAppErrorHook = value
        return self

    def getOsAppShutdownHook(self):
        return self.OsAppShutdownHook

    def setOsAppShutdownHook(self, value):
        self.OsAppShutdownHook = value
        return self

    def getOsAppStartupHook(self):
        return self.OsAppStartupHook

    def setOsAppStartupHook(self, value):
        self.OsAppStartupHook = value
        return self

    def getOsMemoryMappingCodeLocationRef(self):
        return self.OsMemoryMappingCodeLocationRef

    def setOsMemoryMappingCodeLocationRef(self, value):
        self.OsMemoryMappingCodeLocationRef = value
        return self


class OsApplicationTrustedFunction(EcucContainer):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.OsTrustedFunctionName = None                               # type: str
        self.OsMemoryMappingCodeLocationRef = None                      # type: EcucRefType

    def getOsTrustedFunctionName(self):
        return self.OsTrustedFunctionName

    def setOsTrustedFunctionName(self, value):
        self.OsTrustedFunctionName = value
        return self

    def getOsMemoryMappingCodeLocationRef(self):
        return self.OsMemoryMappingCodeLocationRef

    def setOsMemoryMappingCodeLocationRef(self, value):
        self.OsMemoryMappingCodeLocationRef = value
        return self


class OsAppMode(EcucContainer):
    def __init__(self, parent, name):
        super().__init__(parent, name)


class OsApplication(EcucContainer):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.OsTrusted = False                                          # type: bool
        self.OsTrustedApplicationDelayTimingViolationCall = False       # type: bool
        self.OsTrustedApplicationWithProtection = False                 # type: bool
        self.OsAppAlarmRefs = []                                        # type: List[EcucRefType]
        self.OsAppCounterRefs = []                                      # type: List[EcucRefType]
        self.OsAppEcucPartitionRefs = []                                # type: List[EcucRefType]
        self.OsAppIsrRefs = []                                          # type: List[EcucRefType]
        self.OsApplicationCoreRefs = []                                 # type: List[EcucRefType]
        self.OsAppScheduleTableRefs = []                                # type: List[EcucRefType]
        self.OsAppTaskRefs = []                                         # type: List[EcucRefType]
        self.OsMemoryMappingCodeLocationRef = None                      # type: EcucRefType
        self.OsRestartTask = None                                       # type: EcucRefType

        '''
        EB Tresos
        '''
        self.OsAppResourceRefs = []                                     # type: List[EcucRefType]

    def getOsTrusted(self):
        return self.OsTrusted

    def setOsTrusted(self, value):
        self.OsTrusted = value
        return self

    def getOsTrustedApplicationDelayTimingViolationCall(self):
        return self.OsTrustedApplicationDelayTimingViolationCall

    def setOsTrustedApplicationDelayTimingViolationCall(self, value):
        self.OsTrustedApplicationDelayTimingViolationCall = value
        return self

    def getOsTrustedApplicationWithProtection(self):
        return self.OsTrustedApplicationWithProtection

    def setOsTrustedApplicationWithProtection(self, value):
        self.OsTrustedApplicationWithProtection = value
        return self

    def getOsAppAlarmRefs(self):
        return self.OsAppAlarmRefs

    def addOsAppAlarmRef(self, value):
        self.OsAppAlarmRefs.append(value)
        return self

    def getOsAppCounterRefs(self):
        return self.OsAppCounterRefs

    def addOsAppCounterRefs(self, value):
        self.OsAppCounterRefs.append(value)
        return self

    def getOsAppEcucPartitionRefs(self):
        return self.OsAppEcucPartitionRefs

    def addOsAppEcucPartitionRef(self, value):
        if value is not None:
            self.OsAppEcucPartitionRefs.append(value)
        return self

    def getOsAppIsrRefs(self):
        return self.OsAppIsrRefs

    def addOsAppIsrRef(self, value):
        if value is not None:
            self.OsAppIsrRefs.append(value)
        return self

    def getOsApplicationCoreRefs(self):
        return self.OsApplicationCoreRefs

    def addOsApplicationCoreRefs(self, value):
        self.OsApplicationCoreRefs.append(value)
        return self

    def getOsAppScheduleTableRefs(self):
        return self.OsAppScheduleTableRefs

    def addOsAppScheduleTableRef(self, value):
        if value is not None:
            self.OsAppScheduleTableRefs.append(value)
        return self

    def getOsAppTaskRefs(self):
        return self.OsAppTaskRefs

    def addOsAppTaskRef(self, value):
        if value is not None:
            self.OsAppTaskRefs.append(value)
        return self

    def getOsMemoryMappingCodeLocationRef(self):
        return self.OsMemoryMappingCodeLocationRef

    def setOsMemoryMappingCodeLocationRef(self, value):
        self.OsMemoryMappingCodeLocationRef = value
        return self

    def getOsRestartTask(self):
        return self.OsRestartTask

    def setOsRestartTask(self, value):
        self.OsRestartTask = value
        return self
    
    def getOsAppResourceRefs(self):
        return self.OsAppResourceRefs

    def addOsAppResourceRef(self, value):
        if value is not None:
            self.OsAppResourceRefs.append(value)
        return self


class OsDriver(EcucContainer):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osGptChannelRef = None

    def getOsGptChannelRef(self) -> EcucRefType:
        '''
        Multiplicity: 0..1
        '''
        return self.osGptChannelRef

    def setOsGptChannelRef(self, value: EcucRefType):
        '''
        Multiplicity: 0..1
        '''
        self.osGptChannelRef = value
        return self


class OsTimeConstant(EcucContainer):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osTimeValue = None

    def getOsTimeValue(self):
        '''
        Multiplicity: 1
        '''
        return self.osTimeValue

    def setOsTimeValue(self, value):
        '''
        Multiplicity: 1
        '''
        self.osTimeValue = value
        return self


class OsCounter(EcucContainer):

    OS_COUNTER_TYPE_HARDWARE = "HARDWARE"
    OS_COUNTER_TYPE_SOFTWARE = "SOFTWARE"

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osCounterMaxAllowedValue = None                    # type: int
        self.osCounterMinCycle = None                           # type: int
        self.osCounterTicksPerBase = None                       # type: int
        self.osCounterType = None                               # type: str
        self.osSecondsPerTick = None                            # type: float
        self.osCounterAccessingApplications = []                # type: List[EcucRefType]
        self.osDriver = None                                    # Multiplicity: 0..1
        self.osTimeConstants = []                               # Multiplicity: 0..*

    def getOsCounterMaxAllowedValue(self):
        return self.osCounterMaxAllowedValue

    def setOsCounterMaxAllowedValue(self, value):
        '''
        Multiplicity: 1
        '''
        self.osCounterMaxAllowedValue = value
        return self

    def getOsCounterMinCycle(self):
        '''
        Multiplicity: 1
        '''
        return self.osCounterMinCycle

    def setOsCounterMinCycle(self, value):
        '''
        Multiplicity: 1
        '''
        self.osCounterMinCycle = value
        return self

    def getOsCounterTicksPerBase(self):
        '''
        Multiplicity: 1
        '''
        return self.osCounterTicksPerBase

    def setOsCounterTicksPerBase(self, value):
        '''
        Multiplicity: 1
        '''
        self.osCounterTicksPerBase = value
        return self

    def getOsCounterType(self):
        return self.osCounterType

    def setOsCounterType(self, value):
        '''
        Multiplicity: 1
        '''
        self.osCounterType = value
        return self

    def getOsSecondsPerTick(self):
        return self.osSecondsPerTick

    def setOsSecondsPerTick(self, value):
        '''
        Multiplicity: 0..1
        '''
        self.osSecondsPerTick = value
        return self

    def getOsCounterAccessingApplicationList(self):
        '''
        Multiplicity: 0..*
        '''
        return self.osCounterAccessingApplications

    def setOsCounterAccessingApplications(self, value):
        self.osCounterAccessingApplications.append(value)
        return self

    def getOsDriver(self):
        return self.osDriver

    def setOsDriver(self, value):
        self.osDriver = value
        return self

    def getOsTimeConstants(self):
        return self.osTimeConstants

    def setOsTimeConstants(self, value):
        self.osTimeConstants = value
        return self


class OsResource(EcucContainer):
    def __init__(self) -> None:
        pass


class OsIsrResourceLock(EcucContainer):
    def __init__(self) -> None:
        self.osIsrResourceLockBudget = None
        self.osIsrResourceLockResourceRef = None


class OsIsrTimingProtection(EcucObject):
    def __init__(self) -> None:
        self.osIsrAllInterruptLockBudget = None
        self.osIsrExecutionBudget = None
        self.osIsrOsInterruptLockBudget = None
        self.osIsrTimeFrame = None
        self.osIsrResourceLock = OsIsrResourceLock()


class OsIsr(EcucObject):
    '''
    The OsIsr container represents an ISO 17356 interrupt service routine.
    '''

    OS_ISR_CATEGORY_1 = "CATEGORY_1"       # Interrupt is of category 1
    OS_ISR_CATEGORY_2 = "CATEGORY_2"       # Interrupt is of category 2

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osIsrCategory = None
        self.osIsrPeriod = None
        self.osIsrResourceRef = None
        self.osMemoryMappingCodeLocationRef = None
        self.osIsrTimingProtection = OsIsrTimingProtection()

        self.osIsrPriority = None
        self.osStacksize = None
        self.osIsrVector = None

    def getOsIsrCategory(self):
        return self.osIsrCategory

    def setOsIsrCategory(self, value):
        if value is not None:
            self.osIsrCategory = value
        return self

    def getOsIsrPeriod(self):
        return self.osIsrPeriod

    def setOsIsrPeriod(self, value):
        if value is not None:
            self.osIsrPeriod = value
        return self

    def getOsIsrResourceRef(self):
        return self.osIsrResourceRef

    def setOsIsrResourceRef(self, value):
        if value is not None:
            self.osIsrResourceRef = value
        return self

    def getOsMemoryMappingCodeLocationRef(self):
        return self.osMemoryMappingCodeLocationRef

    def setOsMemoryMappingCodeLocationRef(self, value):
        if value is not None:
            self.osMemoryMappingCodeLocationRef = value
        return self

    def getOsIsrTimingProtection(self):
        return self.osIsrTimingProtection

    def setOsIsrTimingProtection(self, value):
        if value is not None:
            self.osIsrTimingProtection = value
        return self

    def getOsIsrPriority(self):
        return self.osIsrPriority

    def setOsIsrPriority(self, value):
        if value is not None:
            self.osIsrPriority = value
        return self

    def getOsStacksize(self):
        return self.osStacksize

    def setOsStacksize(self, value):
        if value is not None:
            self.osStacksize = value
        return self
    
    def getOsIsrVector(self):
        return self.osIsrVector

    def setOsIsrVector(self, value):
        if value is not None:
            self.osIsrVector = value
        return self


class OsTaskAutostart(EcucObject):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osTaskAppModeRefs = []                                     # type: List[EcucRefType]

    def getOsTaskAppModeRefList(self):
        return self.osTaskAppModeRefs

    def addOsTaskAppModeRef(self, value):
        self.osTaskAppModeRefs.append(value)
        return self


class OsTaskResourceLock(EcucObject):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osTaskResourceLockBudget = None


class OsTaskTimingProtection(EcucObject):
    def __init__(self) -> None:
        self.osTaskAllInterruptLockBudget = None
        self.osTaskExecutionBudget = None
        self.osTaskOsInterruptLockBudget = None
        self.osTaskTimeFrame = None


class OsTask(EcucObject):

    FULL = "FULL"   # Task is preemptable.
    NON = "NON"    # Task is not preemptable.

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osTaskActivation = None                    # type: int
        self.osTaskPeriod = 0.0                         # type: float
        self.osTaskPriority = None                      # type: int
        self.osTaskSchedule = ""
        self.OsTaskType = None                          # type: str
        self.osStacksize = 0                            # type: int
        self.osMemoryMappingCodeLocationRef = None      # type: EcucRefType
        self.osTaskAccessingApplication = None
        self.osTaskEventRef = None                      # type: EcucRefType
        self.osTaskResourceRefs = []                    # type: List[EcucRefType]
        self.osTaskAutostart = None                     # type: bool

    def getOsTaskActivation(self):
        return self.osTaskActivation

    def setOsTaskActivation(self, value):
        self.osTaskActivation = value
        return self

    def getOsTaskPeriod(self):
        return self.osTaskPeriod

    def setOsTaskPeriod(self, value):
        self.osTaskPeriod = value
        return self

    def getOsTaskPriority(self):
        return self.osTaskPriority

    def setOsTaskPriority(self, value):
        self.osTaskPriority = value
        return self

    def getOsTaskSchedule(self):
        return self.osTaskSchedule

    def setOsTaskSchedule(self, value):
        self.osTaskSchedule = value
        return self
    
    def getOsTaskType(self):
        return self.OsTaskType

    def setOsTaskType(self, value):
        self.OsTaskType = value
        return self

    def getOsStacksize(self) -> int:
        return self.osStacksize

    def setOsStacksize(self, value: int):
        self.osStacksize = value
        return self

    def getOsMemoryMappingCodeLocationRef(self):
        return self.osMemoryMappingCodeLocationRef

    def setOsMemoryMappingCodeLocationRef(self, value):
        self.osMemoryMappingCodeLocationRef = value
        return self

    def getOsTaskAccessingApplication(self):
        return self.osTaskAccessingApplication

    def setOsTaskAccessingApplication(self, value):
        self.osTaskAccessingApplication = value
        return self

    def getOsTaskEventRef(self):
        return self.osTaskEventRef

    def setOsTaskEventRef(self, value):
        self.osTaskEventRef = value
        return self

    def getOsTaskResourceRefList(self) -> List[EcucRefType]:
        return self.osTaskResourceRefs

    def addOsTaskResourceRef(self, value: EcucRefType):
        self.osTaskResourceRefs.append(value)
        return self

    def IsPreemptable(self) -> bool:
        if self.osTaskSchedule == OsTask.FULL:
            return True
        return False
    
    def getOsTaskAutostart(self):
        return self.osTaskAutostart

    def setOsTaskAutostart(self, value):
        self.osTaskAutostart = value
        return self


class OsScheduleTableAutostart(EcucContainer):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osScheduleTableAutostartType = None        # Multiplicity: 1
        self.osScheduleTableStartValue = None           # Multiplicity: 0..1
        self.osScheduleTableAppModeRef = None           # Multiplicity: 1..*

    def getOsScheduleTableAutostartType(self):
        return self.osScheduleTableAutostartType

    def setOsScheduleTableAutostartType(self, value):
        self.osScheduleTableAutostartType = value
        return self

    def getOsScheduleTableStartValue(self):
        return self.osScheduleTableStartValue

    def setOsScheduleTableStartValue(self, value):
        self.osScheduleTableStartValue = value
        return self

    def getOsScheduleTableAppModeRef(self):
        return self.osScheduleTableAppModeRef

    def setOsScheduleTableAppModeRef(self, value):
        self.osScheduleTableAppModeRef = value
        return self


class OsScheduleTblAdjustableExpPoint(EcucContainer):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osScheduleTableMaxLengthen = None          # Multiplicity: 1
        self.osScheduleTableMaxShorten = None           # Multiplicity: 1

    def getOsScheduleTableMaxLengthen(self) -> int:
        return self.osScheduleTableMaxLengthen

    def setOsScheduleTableMaxLengthen(self, value: int):
        self.osScheduleTableMaxLengthen = value
        return self

    def getOsScheduleTableMaxShorten(self) -> int:
        return self.osScheduleTableMaxShorten

    def setOsScheduleTableMaxShorten(self, value: int):
        self.osScheduleTableMaxShorten = value
        return self


class OsScheduleTableTaskActivation(EcucContainer):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osScheduleTableActivateTaskRef = None      # Multiplicity: 1

    def getOsScheduleTableActivateTaskRef(self) -> EcucRefType:
        return self.osScheduleTableActivateTaskRef

    def setOsScheduleTableActivateTaskRef(self, value: EcucRefType):
        self.osScheduleTableActivateTaskRef = value
        return self


class OsScheduleTableEventSetting(EcucContainer):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        # Multiplicity: 1       Reference to OsEvent
        self.osScheduleTableSetEventRef = None
        # Multiplicity: 1       Reference to OsTask
        self.osScheduleTableSetEventTaskRef = None

    def getOsScheduleTableSetEventRef(self):
        return self.osScheduleTableSetEventRef

    def setOsScheduleTableSetEventRef(self, value):
        self.osScheduleTableSetEventRef = value
        return self

    def getOsScheduleTableSetEventTaskRef(self):
        return self.osScheduleTableSetEventTaskRef

    def setOsScheduleTableSetEventTaskRef(self, value):
        self.osScheduleTableSetEventTaskRef = value
        return self


class OsScheduleTableExpiryPoint(EcucContainer):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osScheduleTblExpPointOffset = None         # Multiplicity: 1
        self.osScheduleTableEventSettings = []          # Multiplicity: 0..*
        self.osScheduleTableTaskActivations = []        # Multiplicity: 0..*
        self.osScheduleTblAdjustableExpPoint = None     # Multiplicity: 0..1

    def getOsScheduleTblExpPointOffset(self):
        return self.osScheduleTblExpPointOffset

    def setOsScheduleTblExpPointOffset(self, value):
        self.osScheduleTblExpPointOffset = value
        return self

    def getOsScheduleTableEventSettingList(self) -> List[OsScheduleTableEventSetting]:
        return self.osScheduleTableEventSettings

    def addOsScheduleTableEventSetting(self, value: OsScheduleTableEventSetting):
        self.addElement(value)
        self.osScheduleTableEventSettings.append(value)
        return self

    def getOsScheduleTableTaskActivationList(self) -> List[OsScheduleTableTaskActivation]:
        return self.osScheduleTableTaskActivations

    def addOsScheduleTableTaskActivation(self, value: OsScheduleTableTaskActivation):
        self.addElement(value)
        self.osScheduleTableTaskActivations.append(value)
        return self

    def getOsScheduleTblAdjustableExpPoint(self) -> OsScheduleTblAdjustableExpPoint:
        return self.osScheduleTblAdjustableExpPoint

    def setOsScheduleTblAdjustableExpPoint(self, value: OsScheduleTblAdjustableExpPoint):
        self.osScheduleTblAdjustableExpPoint = value
        return self


class OsScheduleTable(EcucContainer):

    OS_TIME_UNIT_NANOSECONDS = "NANOSECONDS"
    OS_TIME_UNIT_TICKS = "TICKS"

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osScheduleTableDuration = None             # Multiplicity: 1
        self.osScheduleTableRepeating = None            # Multiplicity: 1
        self.osScheduleTableCounterRef = None           # Multiplicity: 1
        self.osSchTblAccessingApplications = []         # Multiplicity: 0..*
        self.osTimeUnit = None                          # Multiplicity: 0..1

        self.osScheduleTableAutostart = None            # Multiplicity: 0..1
        self.osScheduleTableExpiryPoints = []           # Multiplicity: 1..*
        self.osScheduleTableSync = None                 # Multiplicity: 0..1

    def getOsScheduleTableDuration(self):
        return self.osScheduleTableDuration

    def setOsScheduleTableDuration(self, value):
        self.osScheduleTableDuration = value
        return self

    def getOsScheduleTableRepeating(self):
        return self.osScheduleTableRepeating

    def setOsScheduleTableRepeating(self, value):
        self.osScheduleTableRepeating = value
        return self

    def getOsScheduleTableCounterRef(self) -> EcucRefType:
        return self.osScheduleTableCounterRef

    def setOsScheduleTableCounterRef(self, value: EcucRefType):
        self.osScheduleTableCounterRef = value
        return self

    def getOsSchTblAccessingApplicationList(self):
        return self.osSchTblAccessingApplications

    def addOsSchTblAccessingApplication(self, value):
        self.osSchTblAccessingApplications.append(value)
        return self

    def getOsTimeUnit(self) -> str:
        return self.osTimeUnit

    def setOsTimeUnit(self, value: str):
        if value is not None:
            if value not in [OsScheduleTable.OS_TIME_UNIT_NANOSECONDS, OsScheduleTable.OS_TIME_UNIT_TICKS]:
                raise ValueError("Invalid OsTimeUnit <%s>" % value)
        self.osTimeUnit = value     # set to None if the value is None
        return self

    def getOsScheduleTableAutostart(self):
        return self.osScheduleTableAutostart

    def setOsScheduleTableAutostart(self, value):
        self.osScheduleTableAutostart = value
        return self

    def getOsScheduleTableExpiryPointList(self) -> List[OsScheduleTableExpiryPoint]:
        return self.osScheduleTableExpiryPoints

    def addOsScheduleTableExpiryPoint(self, value: OsScheduleTableExpiryPoint):
        self.addElement(value
                        )
        self.osScheduleTableExpiryPoints.append(value)
        return self

    def getOsScheduleTableSync(self):
        return self.osScheduleTableSync

    def setOsScheduleTableSync(self, value):
        self.osScheduleTableSync = value
        return self


class Os(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "Os")

        self.osTasks = []                               # type: List[OsTask]
        self.osIsrs = []                                # type: List[OsIsr]
        self.osAlarms = []                              # type: List[OsAlarm]
        self.osScheduleTables = []                      # type: List[OsScheduleTable]
        self.osCounters = []                            # type: List[OsCounter]
        self.osApplications = []                        # type: List[OsApplication]

        # extended attributes to speed up performance
        self.osIsrToOsAppMappings = {}                  # type: Dict[str, OsApplication]
        self.osTaskToOsAppMappings = {}                 # typeL Dict[str, OsApplication]

        self.logger = logging.getLogger()

    def getOsTaskList(self) -> List[OsTask]:
        return list(sorted(filter(lambda a: isinstance(a, OsTask), self.elements.values()), key=lambda o: o.name))

    def addOsTask(self, os_task: OsTask):
        self.addElement(os_task)
        self.osTasks.append(os_task)
        return self

    def getOsIsrList(self) -> List[OsIsr]:
        return list(sorted(filter(lambda a: isinstance(a, OsIsr), self.elements.values()), key=lambda o: o.name))

    def addOsIsr(self, os_isr: OsIsr):
        self.addElement(os_isr)
        self.osIsrs.append(os_isr)
        return self

    def getOsAlarmList(self) -> List[OsAlarm]:
        return list(sorted(filter(lambda a: isinstance(a, OsAlarm), self.elements.values()), key=lambda o: o.name))

    def addOsAlarm(self, os_alarm: OsAlarm):
        self.addElement(os_alarm)
        self.osAlarms.append(os_alarm)
        return self

    def getOsScheduleTableList(self) -> List[OsScheduleTable]:
        return list(sorted(filter(lambda a: isinstance(a, OsScheduleTable), self.elements.values()), key=lambda o: o.name))

    def addOsScheduleTable(self, os_schedule_table: OsScheduleTable):
        self.addElement(os_schedule_table)
        self.osScheduleTables.append(os_schedule_table)
        return self

    def getOsCounterList(self) -> List[OsCounter]:
        return list(sorted(filter(lambda a: isinstance(a, OsCounter), self.elements.values()), key=lambda o: o.name))

    def addOsCounter(self, os_counter: OsCounter):
        self.addElement(os_counter)
        self.osCounters.append(os_counter)
        return self
    
    def getOsApplicationList(self) -> List[OsApplication]:
        return list(sorted(filter(lambda a: isinstance(a, OsApplication), self.elements.values()), key=lambda o: o.name))

    def addOsApplication(self, value: OsApplication):
        self.addElement(value)
        self.osApplications.append(value)
        
        for isr_ref in value.getOsAppIsrRefs():
            self.logger.debug("Create OsISR <%s> -> OsApp <%s> Mapping." % (isr_ref.getShortName(), value.getName))
            self.osIsrToOsAppMappings[isr_ref.getShortName()] = value

        for task_ref in value.getOsAppTaskRefs():
            self.logger.debug("Create OsTask <%s> -> OsApp <%s> Mapping." % (task_ref.getShortName(), value.getName))
            self.osTaskToOsAppMappings[task_ref.getShortName()] = value

        return self
    
    def getOsIsrOsApplication(self, isr_name: str) -> OsApplication:
        if isr_name in self.osIsrToOsAppMappings:
            return self.osIsrToOsAppMappings[isr_name]
        return None
    
    def getOsTaskOsApplication(self, isr_name: str) -> OsApplication:
        if isr_name in self.osTaskToOsAppMappings:
            return self.osTaskToOsAppMappings[isr_name]
        return None
