from typing import List

from ..models.abstract import EcucObject

class OsApplication:
    def __init__(self) -> None:
        pass

class OsCounter:
    def __init__(self) -> None:
        pass

class OsResource:
    def __init__(self) -> None:
        pass

class OsIsrResourceLock:
    def __init__(self) -> None:
        self.OsIsrResourceLockBudget = None
        self.OsIsrResourceLockResourceRef = None


class OsIsrTimingProtection:
    def __init__(self) -> None:
        self.OsIsrAllInterruptLockBudget = None
        self.OsIsrExecutionBudget = None
        self.OsIsrOsInterruptLockBudget = None
        self.OsIsrTimeFrame = None                 
        self.OsIsrResourceLock = OsIsrResourceLock()

class OsIsr(EcucObject):
    '''
    The OsIsr container represents an ISO 17356 interrupt service routine.
    '''
    
    OS_ISR_CATEGORY_1 = "CATEGORY_1"       # Interrupt is of category 1
    OS_ISR_CATEGORY_2 = "CATEGORY_2"       # Interrupt is of category 2

    def __init__(self) -> None:
        self.OsIsrCategory = None
        self.OsIsrPeriod = None
        self.OsIsrResourceRef = None
        self.OsMemoryMappingCodeLocationRef = None
        self.OsIsrTimingProtection = OsIsrTimingProtection()    # type: OsIsrTimingProtection

        self.OsIsrPriority = None
        self.OsStacksize = None

    def getOsIsrCategory(self):
        return self.OsIsrCategory

    def setOsIsrCategory(self, value):
        self.OsIsrCategory = value
        return self

    def getOsIsrPeriod(self):
        return self.OsIsrPeriod

    def setOsIsrPeriod(self, value):
        self.OsIsrPeriod = value
        return self

    def getOsIsrResourceRef(self):
        return self.OsIsrResourceRef

    def setOsIsrResourceRef(self, value):
        self.OsIsrResourceRef = value
        return self

    def getOsMemoryMappingCodeLocationRef(self):
        return self.OsMemoryMappingCodeLocationRef

    def setOsMemoryMappingCodeLocationRef(self, value):
        self.OsMemoryMappingCodeLocationRef = value
        return self

    def getOsIsrTimingProtection(self):
        return self.OsIsrTimingProtection

    def setOsIsrTimingProtection(self, value):
        self.OsIsrTimingProtection = value
        return self
    
    def getOsIsrPriority(self):
        return self.OsIsrPriority

    def setOsIsrPriority(self, value):
        self.OsIsrPriority = value
        return self

    def getOsStacksize(self):
        return self.OsStacksize

    def setOsStacksize(self, value):
        self.OsStacksize = value
        return self

class OsTaskAutostart:
    def __init__(self) -> None:
        self.OsTaskAppModeRef = None

class OsTaskResourceLock:
    def __init__(self) -> None:
        self.OsTaskResourceLockBudget = None

class OsTaskTimingProtection:
    def __init__(self) -> None:
        self.OsTaskAllInterruptLockBudget = None
        self.OsTaskExecutionBudget = None
        self.OsTaskOsInterruptLockBudget = None
        self.OsTaskTimeFrame = None

class OsTimeConstant:
    def __init__(self) -> None:
        self.OsTimeValue

class OsTask(EcucObject):

    FULL = "FULL"   # Task is preemptable.
    NON  = "NON"    # Task is not preemptable.

    def __init__(self) -> None:
        self.OsTaskActivation = None                    # type: int 
        self.OsTaskPeriod = 0.0                         # type: float
        self.OsTaskPriority = None                      # type: int
        self.OsTaskSchedule = ""
        self.OsStacksize = 0                            # type: int
        self.OsMemoryMappingCodeLocationRef = None
        self.OsTaskAccessingApplication = None
        self.OsTaskEventRef = None
        self.OsTaskResourceRef = None

    def getOsTaskActivation(self):
        return self.OsTaskActivation

    def setOsTaskActivation(self, value):
        self.OsTaskActivation = value
        return self

    def getOsTaskPeriod(self):
        return self.OsTaskPeriod

    def setOsTaskPeriod(self, value):
        self.OsTaskPeriod = value
        return self

    def getOsTaskPriority(self):
        return self.OsTaskPriority

    def setOsTaskPriority(self, value):
        self.OsTaskPriority = value
        return self

    def getOsTaskSchedule(self):
        return self.OsTaskSchedule

    def setOsTaskSchedule(self, value):
        self.OsTaskSchedule = value
        return self
    
    def getOsStacksize(self):
        return self.OsStacksize

    def setOsStacksize(self, value):
        self.OsStacksize = value
        return self

    def getOsMemoryMappingCodeLocationRef(self):
        return self.OsMemoryMappingCodeLocationRef

    def setOsMemoryMappingCodeLocationRef(self, value):
        self.OsMemoryMappingCodeLocationRef = value
        return self

    def getOsTaskAccessingApplication(self):
        return self.OsTaskAccessingApplication

    def setOsTaskAccessingApplication(self, value):
        self.OsTaskAccessingApplication = value
        return self

    def getOsTaskEventRef(self):
        return self.OsTaskEventRef

    def setOsTaskEventRef(self, value):
        self.OsTaskEventRef = value
        return self

    def getOsTaskResourceRef(self):
        return self.OsTaskResourceRef

    def setOsTaskResourceRef(self, value):
        self.OsTaskResourceRef = value
        return self
    
    def IsPreemptable(self) -> bool:
        if self.OsTaskSchedule == OsTask.FULL:
            return True
        return False

class Os(EcucObject):
    def __init__(self, parent) -> None:
        super().__init__(parent, "Os")

        self.osTasks = []                               # type: List[OsTask]
        self.osIsrs = []                                # type: List[OsIsr]

    def getOsTaskList(self) -> List[OsTask]:
        return self.osTasks
    
    def addOsTask(self, os_task: OsTask):
        self.osTasks.append(os_task)
        return self

    def getOsIsrList(self) -> List[OsIsr]:
        return self.osIsrs
    
    def addOsIsr(self, os_isr: OsIsr):
        self.osIsrs.append(os_isr)
        return self