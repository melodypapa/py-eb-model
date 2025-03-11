from typing import Dict, List
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class RteEventToIsrMapping(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        
        self.RtePositionInIsr = None
        self.RteIsrEventRef = None
        self.RteMappedToIsrRef = None
        self.RteRipsFillRoutineRef = None
        self.RteRipsFlushRoutineRef = None


class AbstractEventToTaskMapping(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rtePositionInTask = None

    def getRtePositionInTask(self):
        return self.rtePositionInTask
    
    def getRtePositionInTaskNumber(self) -> int:
        if self.rtePositionInTask is None:
            return 0
        return self.rtePositionInTask

    def setRtePositionInTask(self, value):
        self.rtePositionInTask = value
        return self


class RteEventToTaskMapping(AbstractEventToTaskMapping):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        
        self.rteActivationOffset = None
        self.rteImmediateRestart = None
        self.rteOsSchedulePoint = None
        
        self.rteServerNumberOfRequestProcessing = None
        self.rteServerQueueLength = None
        self.rteEventPredecessorSyncPointRef = None
        
        self.rteEventSuccessorSyncPointRef = None
        self.rteMappedToTaskRef = None
        self.rtePeriod = None
        self.rteRipsFillRoutineRef = None
        self.rteRipsFlushRoutineRef = None
        self.rteRipsInvocationHandlerRef = None
        self.rteUsedInitFnc = None
        self.rteUsedOsAlarmRef = None
        self.rteUsedOsEventRef = None
        self.rteUsedOsSchTblExpiryPointRef = None
        self.rteVirtuallyMappedToTaskRef = None

    def getRteSwComponentInstance(self):        # type: () -> RteSwComponentInstance
        return self.getParent()

    def getRteActivationOffset(self):
        return self.rteActivationOffset

    def setRteActivationOffset(self, value):
        self.rteActivationOffset = value
        return self

    def getRteImmediateRestart(self):
        return self.rteImmediateRestart

    def setRteImmediateRestart(self, value):
        self.rteImmediateRestart = value
        return self

    def getRteOsSchedulePoint(self):
        return self.rteOsSchedulePoint

    def setRteOsSchedulePoint(self, value):
        self.rteOsSchedulePoint = value
        return self

    def getRtePositionInTask(self):
        return AbstractEventToTaskMapping.getRtePositionInTask(self)

    def setRtePositionInTask(self, value):
        AbstractEventToTaskMapping.setRtePositionInTask(self, value)
        return self

    def getRteServerNumberOfRequestProcessing(self):
        return self.rteServerNumberOfRequestProcessing

    def setRteServerNumberOfRequestProcessing(self, value):
        self.rteServerNumberOfRequestProcessing = value
        return self

    def getRteServerQueueLength(self):
        return self.rteServerQueueLength

    def setRteServerQueueLength(self, value):
        self.rteServerQueueLength = value
        return self

    def getRteEventPredecessorSyncPointRef(self):
        return self.rteEventPredecessorSyncPointRef

    def setRteEventPredecessorSyncPointRef(self, value):
        self.rteEventPredecessorSyncPointRef = value
        return self

    def getRteEventSuccessorSyncPointRef(self):
        return self.rteEventSuccessorSyncPointRef

    def setRteEventSuccessorSyncPointRef(self, value):
        self.rteEventSuccessorSyncPointRef = value
        return self

    def getRteMappedToTaskRef(self) -> EcucRefType:
        return self.rteMappedToTaskRef

    def setRteMappedToTaskRef(self, value: EcucRefType):
        self.rteMappedToTaskRef = value
        return self
    
    def getRtePeriod(self):
        return self.rtePeriod

    def setRtePeriod(self, value):
        self.rtePeriod = value
        return self

    def getRteRipsFillRoutineRef(self):
        return self.rteRipsFillRoutineRef

    def setRteRipsFillRoutineRef(self, value):
        self.rteRipsFillRoutineRef = value
        return self

    def getRteRipsFlushRoutineRef(self):
        return self.rteRipsFlushRoutineRef

    def setRteRipsFlushRoutineRef(self, value):
        self.rteRipsFlushRoutineRef = value
        return self

    def getRteRipsInvocationHandlerRef(self):
        return self.rteRipsInvocationHandlerRef

    def setRteRipsInvocationHandlerRef(self, value):
        self.rteRipsInvocationHandlerRef = value
        return self

    def getRteUsedInitFnc(self):
        return self.rteUsedInitFnc

    def setRteUsedInitFnc(self, value):
        self.rteUsedInitFnc = value
        return self

    def getRteUsedOsAlarmRef(self):
        return self.rteUsedOsAlarmRef

    def setRteUsedOsAlarmRef(self, value):
        self.rteUsedOsAlarmRef = value
        return self

    def getRteUsedOsEventRef(self):
        return self.rteUsedOsEventRef

    def setRteUsedOsEventRef(self, value):
        self.rteUsedOsEventRef = value
        return self

    def getRteUsedOsSchTblExpiryPointRef(self):
        return self.rteUsedOsSchTblExpiryPointRef

    def setRteUsedOsSchTblExpiryPointRef(self, value):
        self.rteUsedOsSchTblExpiryPointRef = value
        return self

    def getRteVirtuallyMappedToTaskRef(self):
        return self.rteVirtuallyMappedToTaskRef

    def setRteVirtuallyMappedToTaskRef(self, value):
        self.rteVirtuallyMappedToTaskRef = value
        return self


class RteEventToTaskMappingV3(RteEventToTaskMapping):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.rteEventRef: EcucParamConfContainerDef = None

    def getRteEventRef(self) -> EcucRefType:
        return self.rteEventRef

    def setRteEventRef(self, value: EcucRefType):
        self.rteEventRef = value
        return self


class RteEventToTaskMappingV4(RteEventToTaskMapping):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.rteEventRefs: List[EcucRefType] = []

    def getRteEventRefs(self) -> List[EcucRefType]:
        return self.rteEventRefs

    def addRteEventRef(self, value: EcucRefType):
        if value is not None:
            self.rteEventRefs.append(value)
        return self
    
    def getRteEventRef(self) -> EcucRefType:
        if len(self.rteEventRefs) != 1:
            raise ValueError("Unsupported RteEventRef of RteEventToTaskMapping <%s> " % self.name)
        return self.rteEventRefs[0]


class RteBswEventToTaskMapping(AbstractEventToTaskMapping):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteBswActivationOffset = None
        self.rteBswEventPeriod = None
        self.rteBswImmediateRestart = None

        self.rteBswServerNumberOfRequestProcessing = None
        self.rteBswServerQueueLength = None
        self.rteOsSchedulePoint = None
        self.rteBswEventPredecessorSyncPointRef = None
       
        self.rteBswMappedToTaskRef = None
        self.rteBswUsedOsAlarmRef = None
        self.rteBswUsedOsEventRef = None
        self.rteBswUsedOsSchTblExpiryPointRef = None
        self.rteRipsFillRoutineRef = None
        self.rteRipsFlushRoutineRef = None

    def getRteBswModuleInstance(self):        # type: () -> RteBswModuleInstance
        return self.getParent()

    def getRteBswActivationOffset(self):
        return self.rteBswActivationOffset

    def setRteBswActivationOffset(self, value):
        self.rteBswActivationOffset = value
        return self

    def getRteBswEventPeriod(self):
        return self.rteBswEventPeriod

    def setRteBswEventPeriod(self, value):
        self.rteBswEventPeriod = value
        return self

    def getRteBswImmediateRestart(self):
        return self.rteBswImmediateRestart

    def setRteBswImmediateRestart(self, value):
        self.rteBswImmediateRestart = value
        return self

    def getRteBswPositionInTask(self) -> int:
        return AbstractEventToTaskMapping.getRtePositionInTask(self)

    def setRteBswPositionInTask(self, value: int):
        AbstractEventToTaskMapping.setRtePositionInTask(self, value)
        return self

    def getRteBswServerNumberOfRequestProcessing(self):
        return self.rteBswServerNumberOfRequestProcessing

    def setRteBswServerNumberOfRequestProcessing(self, value):
        self.rteBswServerNumberOfRequestProcessing = value
        return self

    def getRteBswServerQueueLength(self):
        return self.rteBswServerQueueLength

    def setRteBswServerQueueLength(self, value):
        self.rteBswServerQueueLength = value
        return self

    def getRteOsSchedulePoint(self):
        return self.rteOsSchedulePoint

    def setRteOsSchedulePoint(self, value):
        self.rteOsSchedulePoint = value
        return self

    def getRteBswEventPredecessorSyncPointRef(self):
        return self.rteBswEventPredecessorSyncPointRef

    def setRteBswEventPredecessorSyncPointRef(self, value):
        self.rteBswEventPredecessorSyncPointRef = value
        return self

    def getRteBswMappedToTaskRef(self) -> EcucRefType:
        return self.rteBswMappedToTaskRef

    def setRteBswMappedToTaskRef(self, value: EcucRefType):
        self.rteBswMappedToTaskRef = value
        return self

    def getRteBswUsedOsAlarmRef(self):
        return self.rteBswUsedOsAlarmRef

    def setRteBswUsedOsAlarmRef(self, value):
        self.rteBswUsedOsAlarmRef = value
        return self

    def getRteBswUsedOsEventRef(self):
        return self.rteBswUsedOsEventRef

    def setRteBswUsedOsEventRef(self, value):
        self.rteBswUsedOsEventRef = value
        return self

    def getRteBswUsedOsSchTblExpiryPointRef(self):
        return self.rteBswUsedOsSchTblExpiryPointRef

    def setRteBswUsedOsSchTblExpiryPointRef(self, value):
        self.rteBswUsedOsSchTblExpiryPointRef = value
        return self

    def getRteRipsFillRoutineRef(self):
        return self.rteRipsFillRoutineRef

    def setRteRipsFillRoutineRef(self, value):
        self.rteRipsFillRoutineRef = value
        return self

    def getRteRipsFlushRoutineRef(self):
        return self.rteRipsFlushRoutineRef

    def setRteRipsFlushRoutineRef(self, value):
        self.rteRipsFlushRoutineRef = value
        return self


class RteBswEventToTaskMappingV3(RteBswEventToTaskMapping):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.rteBswEventRef: EcucRefType = None

    def getRteBswEventRef(self) -> EcucRefType:
        return self.rteBswEventRef

    def setRteBswEventRef(self, value: EcucRefType):
        if value is not None:
            self.rteBswEventRef = value
        return self


class RteBswEventToTaskMappingV4(RteBswEventToTaskMapping):
    def __init__(self, parent, name):
        super().__init__(parent, name)
        
        self.rteBswEventRefs: List[EcucRefType] = []

    def getRteBswEventRefs(self) -> List[EcucRefType]:
        return self.rteBswEventRefs

    def addRteBswEventRef(self, value: EcucRefType):
        self.rteBswEventRefs.append(value)
        return self
    
    def getRteBswEventRef(self) -> EcucRefType:
        if len(self.rteBswEventRefs) != 1:
            raise ValueError("Unsupported RteEventRef of RteEventToTaskMapping <%s> " % self.name)
        return self.rteBswEventRefs[0]


class AbstractRteInstance(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class RteSwComponentInstance(AbstractRteInstance):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.mappedToOsApplicationRef = None                # type: EcucRefType
        self.rteSoftwareComponentInstanceRef = None

        self.rteEventToIsrMappings = []
        self.rteEventToTaskMappings = []
        self.rteExclusiveAreaImplementations = []
        self.rteExternalTriggerConfigs = []
        self.rteInternalTriggerConfigs = []
        self.rteModeMachineInstanceConfigs = []
        self.rteNvRamAllocations = []
    
    def getMappedToOsApplicationRef(self):
        return self.mappedToOsApplicationRef

    def setMappedToOsApplicationRef(self, value):
        self.mappedToOsApplicationRef = value
        return self

    def getRteSoftwareComponentInstanceRef(self) -> EcucRefType:
        return self.rteSoftwareComponentInstanceRef

    def setRteSoftwareComponentInstanceRef(self, value: EcucRefType):
        self.rteSoftwareComponentInstanceRef = value
        return self

    def getRteEventToIsrMappingList(self) -> List[RteEventToIsrMapping]:
        return self.rteEventToIsrMappings

    def addRteEventToIsrMappings(self, value: RteEventToIsrMapping):
        self.rteEventToIsrMappings.append(value)
        return self

    def getRteEventToTaskMappingList(self) -> List[RteEventToTaskMapping]:
        return self.rteEventToTaskMappings

    def addRteEventToTaskMapping(self, value: RteEventToTaskMapping):
        self.rteEventToTaskMappings.append(value)
        return self

    def getRteExclusiveAreaImplementationList(self):
        return self.rteExclusiveAreaImplementations

    def addRteExclusiveAreaImplementations(self, value):
        self.rteExclusiveAreaImplementations.append(value)
        return self

    def getRteExternalTriggerConfigList(self):
        return self.rteExternalTriggerConfigs

    def addRteExternalTriggerConfig(self, value):
        self.rteExternalTriggerConfigs.append(value)
        return self

    def getRteInternalTriggerConfigList(self):
        return self.rteInternalTriggerConfigs

    def addRteInternalTriggerConfig(self, value):
        self.rteInternalTriggerConfigs.append(value)
        return self

    def getRteModeMachineInstanceConfigList(self):
        return self.rteModeMachineInstanceConfigs

    def addRteModeMachineInstanceConfig(self, value):
        self.rteModeMachineInstanceConfigs.append(value)
        return self

    def getRteNvRamAllocationList(self):
        return self.rteNvRamAllocations

    def addRteNvRamAllocation(self, value):
        self.rteNvRamAllocations.append(value)
        return self


class RteBswModuleInstance(AbstractRteInstance):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteBswImplementationRef = None
        self.rteBswModuleConfigurationRefs = []
        self.rteBswEventToIsrMappings = []
        self.rteBswEventToTaskMappings = []                     # type: List[RteBswEventToTaskMapping]
        self.rteBswExclusiveAreaImpls = []
        self.rteBswExternalTriggerConfigs = []
        self.rteBswInternalTriggerConfigs = []
        self.rteMappedToOsApplicationRef = None                 # type: EcucRefType
        self.rteBswModeMachineInstanceConfigs = []
        self.rteBswRequiredClientServerConnections = []
        self.rteBswRequiredModeGroupConnections = []
        self.rteBswRequiredSenderReceiverConnections = []
        self.rteBswRequiredTriggerConnections = []

    def getRteBswImplementationRef(self) -> EcucRefType:
        return self.rteBswImplementationRef

    def setRteBswImplementationRef(self, value: EcucRefType):
        self.rteBswImplementationRef = value
        return self

    def getRteBswModuleConfigurationRefList(self):
        return self.rteBswModuleConfigurationRefs

    def addRteBswModuleConfigurationRef(self, value):
        self.rteBswModuleConfigurationRefs.append(value)
        return self

    def getRteBswEventToIsrMappingList(self):
        return self.rteBswEventToIsrMappings

    def addRteBswEventToIsrMapping(self, value):
        self.rteBswEventToIsrMappings.append(value)
        return self

    def getRteBswEventToTaskMappingList(self) -> List[RteBswEventToTaskMapping]:
        return self.rteBswEventToTaskMappings

    def addRteBswEventToTaskMapping(self, value: RteBswEventToTaskMapping):
        self.rteBswEventToTaskMappings.append(value)
        return self

    def getRteBswExclusiveAreaImplList(self):
        return self.rteBswExclusiveAreaImpls

    def addRteBswExclusiveAreaImpl(self, value):
        self.rteBswExclusiveAreaImpls.append(value)
        return self

    def getRteBswExternalTriggerConfigList(self):
        return self.rteBswExternalTriggerConfigs

    def addRteBswExternalTriggerConfig(self, value):
        self.rteBswExternalTriggerConfigs.append(value)
        return self

    def getRteBswInternalTriggerConfigList(self):
        return self.rteBswInternalTriggerConfigs

    def addRteBswInternalTriggerConfig(self, value):
        self.rteBswInternalTriggerConfigs.append(value)
        return self

    def getRteBswModeMachineInstanceConfigList(self):
        return self.rteBswModeMachineInstanceConfigs

    def addRteBswModeMachineInstanceConfig(self, value):
        self.rteBswModeMachineInstanceConfigs.append(value)
        return self

    def getRteBswRequiredClientServerConnectionList(self):
        return self.rteBswRequiredClientServerConnections

    def addRteBswRequiredClientServerConnection(self, value):
        self.rteBswRequiredClientServerConnections.append(value)
        return self

    def getRteBswRequiredModeGroupConnectionList(self):
        return self.rteBswRequiredModeGroupConnections

    def addRteBswRequiredModeGroupConnection(self, value):
        self.rteBswRequiredModeGroupConnections.append(value)
        return self

    def getRteBswRequiredSenderReceiverConnectionList(self):
        return self.rteBswRequiredSenderReceiverConnections

    def addRteBswRequiredSenderReceiverConnection(self, value):
        self.rteBswRequiredSenderReceiverConnections.append(value)
        return self

    def getRteBswRequiredTriggerConnectionList(self):
        return self.rteBswRequiredTriggerConnections

    def addRteBswRequiredTriggerConnection(self, value):
        self.rteBswRequiredTriggerConnections.append(value)
        return self
    
    def getRteMappedToOsApplicationRef(self):
        return self.rteMappedToOsApplicationRef

    def setRteMappedToOsApplicationRef(self, value):
        self.rteMappedToOsApplicationRef = value
        return self


class Rte(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "Rte")

        self.rteBswModuleInstances = []                                         # type: List[RteBswModuleInstance]
        self.rteSwComponentInstances = []                                       # type: List[RteSwComponentInstance]

    def getRteBswModuleInstance(self, name: str) -> RteBswModuleInstance:
        result = list(filter(lambda a: a.name == name, self.rteBswModuleInstances))
        if len(result) > 0:
            return result[0]
        return None

    def getRteBswModuleInstanceList(self) -> List[RteBswModuleInstance]:
        return list(sorted(self.rteBswModuleInstances, key=lambda o: o.name))

    def addRteBswModuleInstance(self, value: RteBswModuleInstance):
        self.elements[value.getName()] = value
        self.rteBswModuleInstances.append(value)

    def getRteSwComponentInstance(self, name: str) -> RteSwComponentInstance:
        result = list(filter(lambda a: a.name == name, self.rteSwComponentInstances))
        if len(result) > 0:
            return result[0]
        return None

    def getRteSwComponentInstanceList(self) -> List[RteSwComponentInstance]:
        return list(sorted(self.rteSwComponentInstances, key=lambda o: o.name))

    def addRteSwComponentInstance(self, value: RteSwComponentInstance):
        self.elements[value.getName()] = value
        self.rteSwComponentInstances.append(value)

    def getRteModuleInstanceList(self) -> List[AbstractRteInstance]:
        return list(sorted(filter(lambda a: isinstance(a, AbstractRteInstance), self.elements.values()), key=lambda o: o.name))
    
    def _addToRteEventToOsTasks(self, mapping: AbstractEventToTaskMapping, os_tasks: Dict[str, List[AbstractEventToTaskMapping]]):
        if isinstance(mapping, RteBswEventToTaskMapping):
            task_ref = mapping.getRteBswMappedToTaskRef()
        elif isinstance(mapping, RteEventToTaskMapping):
            task_ref = mapping.getRteMappedToTaskRef()
        else:
            raise NotImplementedError("Unsupported AbstractEventToTaskMapping <%s>" % type(mapping))
        
        # Skip event do not map to task
        if task_ref is None:
            return
        
        task_name = task_ref.getShortName()
        
        if task_name not in os_tasks:
            os_tasks[task_name] = []
        os_tasks[task_name].append(mapping)
    
    def getMappedEvents(self) -> Dict[str, List[AbstractEventToTaskMapping]]:
        os_tasks = {}
        for instance in self.getRteModuleInstanceList():
            if isinstance(instance, RteBswModuleInstance):
                for mapping in instance.getRteBswEventToTaskMappingList():
                    self._addToRteEventToOsTasks(mapping, os_tasks)
            elif isinstance(instance, RteSwComponentInstance):
                for mapping in instance.getRteEventToTaskMappingList():
                    self._addToRteEventToOsTasks(mapping, os_tasks)
            else:
                raise NotImplementedError("Invalid Rte Module Instance <%s>" % type(instance))

        return os_tasks
