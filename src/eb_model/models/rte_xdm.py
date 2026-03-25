from typing import Any, Dict, List, Optional, cast
from ..models.abstract import EcucObject, EcucParamConfContainerDef, EcucRefType, Module


class RteEventToIsrMapping(EcucParamConfContainerDef):
    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        super().__init__(parent, name)

        self.RtePositionInIsr: Optional[Any] = None
        self.RteIsrEventRef: Optional[Any] = None
        self.RteMappedToIsrRef: Optional[Any] = None
        self.RteRipsFillRoutineRef: Optional[Any] = None
        self.RteRipsFlushRoutineRef: Optional[Any] = None


class AbstractEventToTaskMapping(EcucParamConfContainerDef):
    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        super().__init__(parent, name)

        self.rtePositionInTask: Optional[int] = None

    def getRtePositionInTask(self) -> Optional[int]:
        return self.rtePositionInTask

    def getRtePositionInTaskNumber(self) -> int:
        if self.rtePositionInTask is None:
            return 0
        return self.rtePositionInTask

    def setRtePositionInTask(self, value: int) -> 'AbstractEventToTaskMapping':
        self.rtePositionInTask = value
        return self


class RteEventToTaskMapping(AbstractEventToTaskMapping):
    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        super().__init__(parent, name)

        self.rteActivationOffset: Optional[Any] = None
        self.rteImmediateRestart: Optional[Any] = None
        self.rteOsSchedulePoint: Optional[Any] = None

        self.rteServerNumberOfRequestProcessing: Optional[Any] = None
        self.rteServerQueueLength: Optional[Any] = None
        self.rteEventPredecessorSyncPointRef: Optional[Any] = None

        self.rteEventSuccessorSyncPointRef: Optional[Any] = None
        self.rteMappedToTaskRef: Optional[EcucRefType] = None
        self.rtePeriod: Optional[Any] = None
        self.rteRipsFillRoutineRef: Optional[Any] = None
        self.rteRipsFlushRoutineRef: Optional[Any] = None
        self.rteRipsInvocationHandlerRef: Optional[Any] = None
        self.rteUsedInitFnc: Optional[Any] = None
        self.rteUsedOsAlarmRef: Optional[Any] = None
        self.rteUsedOsEventRef: Optional[Any] = None
        self.rteUsedOsSchTblExpiryPointRef: Optional[Any] = None
        self.rteVirtuallyMappedToTaskRef: Optional[Any] = None

    def getRteSwComponentInstance(self) -> 'RteSwComponentInstance':  # type: ignore[override]
        return self.getParent()  # type: ignore[return-value]

    def getRteActivationOffset(self) -> Optional[Any]:
        return self.rteActivationOffset

    def setRteActivationOffset(self, value: Any) -> 'RteEventToTaskMapping':
        self.rteActivationOffset = value
        return self

    def getRteImmediateRestart(self) -> Optional[Any]:
        return self.rteImmediateRestart

    def setRteImmediateRestart(self, value: Any) -> 'RteEventToTaskMapping':
        self.rteImmediateRestart = value
        return self

    def getRteOsSchedulePoint(self) -> Optional[Any]:
        return self.rteOsSchedulePoint

    def setRteOsSchedulePoint(self, value: Any) -> 'RteEventToTaskMapping':
        self.rteOsSchedulePoint = value
        return self

    def getRtePositionInTask(self) -> Optional[int]:
        return AbstractEventToTaskMapping.getRtePositionInTask(self)

    def setRtePositionInTask(self, value: int) -> 'RteEventToTaskMapping':
        AbstractEventToTaskMapping.setRtePositionInTask(self, value)
        return self

    def getRteServerNumberOfRequestProcessing(self) -> Optional[Any]:
        return self.rteServerNumberOfRequestProcessing

    def setRteServerNumberOfRequestProcessing(self, value: Any) -> 'RteEventToTaskMapping':
        self.rteServerNumberOfRequestProcessing = value
        return self

    def getRteServerQueueLength(self) -> Optional[Any]:
        return self.rteServerQueueLength

    def setRteServerQueueLength(self, value: Any) -> 'RteEventToTaskMapping':
        self.rteServerQueueLength = value
        return self

    def getRteEventPredecessorSyncPointRef(self) -> Optional[Any]:
        return self.rteEventPredecessorSyncPointRef

    def setRteEventPredecessorSyncPointRef(self, value: Any) -> 'RteEventToTaskMapping':
        self.rteEventPredecessorSyncPointRef = value
        return self

    def getRteEventSuccessorSyncPointRef(self) -> Optional[Any]:
        return self.rteEventSuccessorSyncPointRef

    def setRteEventSuccessorSyncPointRef(self, value: Any) -> 'RteEventToTaskMapping':
        self.rteEventSuccessorSyncPointRef = value
        return self

    def getRteMappedToTaskRef(self) -> Optional[EcucRefType]:
        return self.rteMappedToTaskRef

    def setRteMappedToTaskRef(self, value: EcucRefType) -> 'RteEventToTaskMapping':
        self.rteMappedToTaskRef = value
        return self

    def getRtePeriod(self) -> Optional[Any]:
        return self.rtePeriod

    def setRtePeriod(self, value: Any) -> 'RteEventToTaskMapping':
        self.rtePeriod = value
        return self

    def getRteRipsFillRoutineRef(self) -> Optional[Any]:
        return self.rteRipsFillRoutineRef

    def setRteRipsFillRoutineRef(self, value: Any) -> 'RteEventToTaskMapping':
        self.rteRipsFillRoutineRef = value
        return self

    def getRteRipsFlushRoutineRef(self) -> Optional[Any]:
        return self.rteRipsFlushRoutineRef

    def setRteRipsFlushRoutineRef(self, value: Any) -> 'RteEventToTaskMapping':
        self.rteRipsFlushRoutineRef = value
        return self

    def getRteRipsInvocationHandlerRef(self) -> Optional[Any]:
        return self.rteRipsInvocationHandlerRef

    def setRteRipsInvocationHandlerRef(self, value: Any) -> 'RteEventToTaskMapping':
        self.rteRipsInvocationHandlerRef = value
        return self

    def getRteUsedInitFnc(self) -> Optional[Any]:
        return self.rteUsedInitFnc

    def setRteUsedInitFnc(self, value: Any) -> 'RteEventToTaskMapping':
        self.rteUsedInitFnc = value
        return self

    def getRteUsedOsAlarmRef(self) -> Optional[Any]:
        return self.rteUsedOsAlarmRef

    def setRteUsedOsAlarmRef(self, value: Any) -> 'RteEventToTaskMapping':
        self.rteUsedOsAlarmRef = value
        return self

    def getRteUsedOsEventRef(self) -> Optional[Any]:
        return self.rteUsedOsEventRef

    def setRteUsedOsEventRef(self, value: Any) -> 'RteEventToTaskMapping':
        self.rteUsedOsEventRef = value
        return self

    def getRteUsedOsSchTblExpiryPointRef(self) -> Optional[Any]:
        return self.rteUsedOsSchTblExpiryPointRef

    def setRteUsedOsSchTblExpiryPointRef(self, value: Any) -> 'RteEventToTaskMapping':
        self.rteUsedOsSchTblExpiryPointRef = value
        return self

    def getRteVirtuallyMappedToTaskRef(self) -> Optional[Any]:
        return self.rteVirtuallyMappedToTaskRef

    def setRteVirtuallyMappedToTaskRef(self, value: Any) -> 'RteEventToTaskMapping':
        self.rteVirtuallyMappedToTaskRef = value
        return self


class RteEventToTaskMappingV3(RteEventToTaskMapping):
    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        super().__init__(parent, name)

        self.rteEventRef: Optional[EcucRefType] = None

    def getRteEventRef(self) -> Optional[EcucRefType]:
        return self.rteEventRef

    def setRteEventRef(self, value: EcucRefType) -> 'RteEventToTaskMappingV3':
        self.rteEventRef = value
        return self


class RteEventToTaskMappingV4(RteEventToTaskMapping):
    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        super().__init__(parent, name)

        self.rteEventRefs: List[EcucRefType] = []

    def getRteEventRefs(self) -> List[EcucRefType]:
        return self.rteEventRefs

    def addRteEventRef(self, value: EcucRefType) -> 'RteEventToTaskMappingV4':
        if value is not None:
            self.rteEventRefs.append(value)
        return self

    def getRteEventRef(self) -> EcucRefType:
        if len(self.rteEventRefs) != 1:
            raise ValueError("Unsupported RteEventRef of RteEventToTaskMapping <%s> " % self.name)
        return self.rteEventRefs[0]


class RteBswEventToTaskMapping(AbstractEventToTaskMapping):
    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        super().__init__(parent, name)

        self.rteBswActivationOffset: Optional[Any] = None
        self.rteBswEventPeriod: Optional[Any] = None
        self.rteBswImmediateRestart: Optional[Any] = None

        self.rteBswServerNumberOfRequestProcessing: Optional[Any] = None
        self.rteBswServerQueueLength: Optional[Any] = None
        self.rteOsSchedulePoint: Optional[Any] = None
        self.rteBswEventPredecessorSyncPointRef: Optional[Any] = None

        self.rteBswMappedToTaskRef: Optional[EcucRefType] = None
        self.rteBswUsedOsAlarmRef: Optional[Any] = None
        self.rteBswUsedOsEventRef: Optional[Any] = None
        self.rteBswUsedOsSchTblExpiryPointRef: Optional[Any] = None
        self.rteRipsFillRoutineRef: Optional[Any] = None
        self.rteRipsFlushRoutineRef: Optional[Any] = None

    def getRteBswModuleInstance(self) -> 'RteBswModuleInstance':  # type: ignore[override]
        return self.getParent()  # type: ignore[return-value]

    def getRteBswActivationOffset(self) -> Optional[Any]:
        return self.rteBswActivationOffset

    def setRteBswActivationOffset(self, value: Any) -> 'RteBswEventToTaskMapping':
        self.rteBswActivationOffset = value
        return self

    def getRteBswEventPeriod(self) -> Optional[Any]:
        return self.rteBswEventPeriod

    def setRteBswEventPeriod(self, value: Any) -> 'RteBswEventToTaskMapping':
        self.rteBswEventPeriod = value
        return self

    def getRteBswImmediateRestart(self) -> Optional[Any]:
        return self.rteBswImmediateRestart

    def setRteBswImmediateRestart(self, value: Any) -> 'RteBswEventToTaskMapping':
        self.rteBswImmediateRestart = value
        return self

    def getRteBswPositionInTask(self) -> int:
        return AbstractEventToTaskMapping.getRtePositionInTask(self) or 0

    def setRteBswPositionInTask(self, value: int) -> 'RteBswEventToTaskMapping':
        AbstractEventToTaskMapping.setRtePositionInTask(self, value)
        return self

    def getRteBswServerNumberOfRequestProcessing(self) -> Optional[Any]:
        return self.rteBswServerNumberOfRequestProcessing

    def setRteBswServerNumberOfRequestProcessing(self, value: Any) -> 'RteBswEventToTaskMapping':
        self.rteBswServerNumberOfRequestProcessing = value
        return self

    def getRteBswServerQueueLength(self) -> Optional[Any]:
        return self.rteBswServerQueueLength

    def setRteBswServerQueueLength(self, value: Any) -> 'RteBswEventToTaskMapping':
        self.rteBswServerQueueLength = value
        return self

    def getRteOsSchedulePoint(self) -> Optional[Any]:
        return self.rteOsSchedulePoint

    def setRteOsSchedulePoint(self, value: Any) -> 'RteBswEventToTaskMapping':
        self.rteOsSchedulePoint = value
        return self

    def getRteBswEventPredecessorSyncPointRef(self) -> Optional[Any]:
        return self.rteBswEventPredecessorSyncPointRef

    def setRteBswEventPredecessorSyncPointRef(self, value: Any) -> 'RteBswEventToTaskMapping':
        self.rteBswEventPredecessorSyncPointRef = value
        return self

    def getRteBswMappedToTaskRef(self) -> Optional[EcucRefType]:
        return self.rteBswMappedToTaskRef

    def setRteBswMappedToTaskRef(self, value: EcucRefType) -> 'RteBswEventToTaskMapping':
        self.rteBswMappedToTaskRef = value
        return self

    def getRteBswUsedOsAlarmRef(self) -> Optional[Any]:
        return self.rteBswUsedOsAlarmRef

    def setRteBswUsedOsAlarmRef(self, value: Any) -> 'RteBswEventToTaskMapping':
        self.rteBswUsedOsAlarmRef = value
        return self

    def getRteBswUsedOsEventRef(self) -> Optional[Any]:
        return self.rteBswUsedOsEventRef

    def setRteBswUsedOsEventRef(self, value: Any) -> 'RteBswEventToTaskMapping':
        self.rteBswUsedOsEventRef = value
        return self

    def getRteBswUsedOsSchTblExpiryPointRef(self) -> Optional[Any]:
        return self.rteBswUsedOsSchTblExpiryPointRef

    def setRteBswUsedOsSchTblExpiryPointRef(self, value: Any) -> 'RteBswEventToTaskMapping':
        self.rteBswUsedOsSchTblExpiryPointRef = value
        return self

    def getRteRipsFillRoutineRef(self) -> Optional[Any]:
        return self.rteRipsFillRoutineRef

    def setRteRipsFillRoutineRef(self, value: Any) -> 'RteBswEventToTaskMapping':
        self.rteRipsFillRoutineRef = value
        return self

    def getRteRipsFlushRoutineRef(self) -> Optional[Any]:
        return self.rteRipsFlushRoutineRef

    def setRteRipsFlushRoutineRef(self, value: Any) -> 'RteBswEventToTaskMapping':
        self.rteRipsFlushRoutineRef = value
        return self


class RteBswEventToTaskMappingV3(RteBswEventToTaskMapping):
    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        super().__init__(parent, name)

        self.rteBswEventRef: Optional[EcucRefType] = None

    def getRteBswEventRef(self) -> Optional[EcucRefType]:
        return self.rteBswEventRef

    def setRteBswEventRef(self, value: EcucRefType) -> 'RteBswEventToTaskMappingV3':
        if value is not None:
            self.rteBswEventRef = value
        return self


class RteBswEventToTaskMappingV4(RteBswEventToTaskMapping):
    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        super().__init__(parent, name)

        self.rteBswEventRefs: List[EcucRefType] = []

    def getRteBswEventRefs(self) -> List[EcucRefType]:
        return self.rteBswEventRefs

    def addRteBswEventRef(self, value: EcucRefType) -> 'RteBswEventToTaskMappingV4':
        self.rteBswEventRefs.append(value)
        return self

    def getRteBswEventRef(self) -> EcucRefType:
        if len(self.rteBswEventRefs) != 1:
            raise ValueError("Unsupported RteEventRef of RteEventToTaskMapping <%s> " % self.name)
        return self.rteBswEventRefs[0]


class AbstractRteInstance(EcucParamConfContainerDef):
    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        super().__init__(parent, name)


class RteSwComponentInstance(AbstractRteInstance):
    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        super().__init__(parent, name)

        self.mappedToOsApplicationRef: Optional[EcucRefType] = None
        self.rteSoftwareComponentInstanceRef: Optional[EcucRefType] = None

        self.rteEventToIsrMappings: List[RteEventToIsrMapping] = []
        self.rteEventToTaskMappings: List[RteEventToTaskMapping] = []
        self.rteExclusiveAreaImplementations: List[Any] = []
        self.rteExternalTriggerConfigs: List[Any] = []
        self.rteInternalTriggerConfigs: List[Any] = []
        self.rteModeMachineInstanceConfigs: List[Any] = []
        self.rteNvRamAllocations: List[Any] = []

    def getMappedToOsApplicationRef(self) -> Optional[EcucRefType]:
        return self.mappedToOsApplicationRef

    def setMappedToOsApplicationRef(self, value: EcucRefType) -> 'RteSwComponentInstance':
        self.mappedToOsApplicationRef = value
        return self

    def getRteSoftwareComponentInstanceRef(self) -> Optional[EcucRefType]:
        return self.rteSoftwareComponentInstanceRef

    def setRteSoftwareComponentInstanceRef(self, value: EcucRefType) -> 'RteSwComponentInstance':
        self.rteSoftwareComponentInstanceRef = value
        return self

    def getRteEventToIsrMappingList(self) -> List[RteEventToIsrMapping]:
        return self.rteEventToIsrMappings

    def addRteEventToIsrMappings(self, value: RteEventToIsrMapping) -> 'RteSwComponentInstance':
        self.rteEventToIsrMappings.append(value)
        return self

    def getRteEventToTaskMappingList(self) -> List[RteEventToTaskMapping]:
        return self.rteEventToTaskMappings

    def addRteEventToTaskMapping(self, value: RteEventToTaskMapping) -> 'RteSwComponentInstance':
        self.rteEventToTaskMappings.append(value)
        return self

    def getRteExclusiveAreaImplementationList(self) -> List[Any]:
        return self.rteExclusiveAreaImplementations

    def addRteExclusiveAreaImplementations(self, value: Any) -> 'RteSwComponentInstance':
        self.rteExclusiveAreaImplementations.append(value)
        return self

    def getRteExternalTriggerConfigList(self) -> List[Any]:
        return self.rteExternalTriggerConfigs

    def addRteExternalTriggerConfig(self, value: Any) -> 'RteSwComponentInstance':
        self.rteExternalTriggerConfigs.append(value)
        return self

    def getRteInternalTriggerConfigList(self) -> List[Any]:
        return self.rteInternalTriggerConfigs

    def addRteInternalTriggerConfig(self, value: Any) -> 'RteSwComponentInstance':
        self.rteInternalTriggerConfigs.append(value)
        return self

    def getRteModeMachineInstanceConfigList(self) -> List[Any]:
        return self.rteModeMachineInstanceConfigs

    def addRteModeMachineInstanceConfig(self, value: Any) -> 'RteSwComponentInstance':
        self.rteModeMachineInstanceConfigs.append(value)
        return self

    def getRteNvRamAllocationList(self) -> List[Any]:
        return self.rteNvRamAllocations

    def addRteNvRamAllocation(self, value: Any) -> 'RteSwComponentInstance':
        self.rteNvRamAllocations.append(value)
        return self


class RteBswModuleInstance(AbstractRteInstance):
    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        super().__init__(parent, name)

        self.rteBswImplementationRef: Optional[EcucRefType] = None
        self.rteBswModuleConfigurationRefs: List[Any] = []
        self.rteBswEventToIsrMappings: List[Any] = []
        self.rteBswEventToTaskMappings: List[RteBswEventToTaskMapping] = []
        self.rteBswExclusiveAreaImpls: List[Any] = []
        self.rteBswExternalTriggerConfigs: List[Any] = []
        self.rteBswInternalTriggerConfigs: List[Any] = []
        self.rteMappedToOsApplicationRef: Optional[EcucRefType] = None
        self.rteBswModeMachineInstanceConfigs: List[Any] = []
        self.rteBswRequiredClientServerConnections: List[Any] = []
        self.rteBswRequiredModeGroupConnections: List[Any] = []
        self.rteBswRequiredSenderReceiverConnections: List[Any] = []
        self.rteBswRequiredTriggerConnections: List[Any] = []

    def getRteBswImplementationRef(self) -> Optional[EcucRefType]:
        return self.rteBswImplementationRef

    def setRteBswImplementationRef(self, value: EcucRefType) -> 'RteBswModuleInstance':
        self.rteBswImplementationRef = value
        return self

    def getRteBswModuleConfigurationRefList(self) -> List[Any]:
        return self.rteBswModuleConfigurationRefs

    def addRteBswModuleConfigurationRef(self, value: Any) -> 'RteBswModuleInstance':
        self.rteBswModuleConfigurationRefs.append(value)
        return self

    def getRteBswEventToIsrMappingList(self) -> List[Any]:
        return self.rteBswEventToIsrMappings

    def addRteBswEventToIsrMapping(self, value: Any) -> 'RteBswModuleInstance':
        self.rteBswEventToIsrMappings.append(value)
        return self

    def getRteBswEventToTaskMappingList(self) -> List[RteBswEventToTaskMapping]:
        return self.rteBswEventToTaskMappings

    def addRteBswEventToTaskMapping(self, value: RteBswEventToTaskMapping) -> 'RteBswModuleInstance':
        self.rteBswEventToTaskMappings.append(value)
        return self

    def getRteBswExclusiveAreaImplList(self) -> List[Any]:
        return self.rteBswExclusiveAreaImpls

    def addRteBswExclusiveAreaImpl(self, value: Any) -> 'RteBswModuleInstance':
        self.rteBswExclusiveAreaImpls.append(value)
        return self

    def getRteBswExternalTriggerConfigList(self) -> List[Any]:
        return self.rteBswExternalTriggerConfigs

    def addRteBswExternalTriggerConfig(self, value: Any) -> 'RteBswModuleInstance':
        self.rteBswExternalTriggerConfigs.append(value)
        return self

    def getRteBswInternalTriggerConfigList(self) -> List[Any]:
        return self.rteBswInternalTriggerConfigs

    def addRteBswInternalTriggerConfig(self, value: Any) -> 'RteBswModuleInstance':
        self.rteBswInternalTriggerConfigs.append(value)
        return self

    def getRteBswModeMachineInstanceConfigList(self) -> List[Any]:
        return self.rteBswModeMachineInstanceConfigs

    def addRteBswModeMachineInstanceConfig(self, value: Any) -> 'RteBswModuleInstance':
        self.rteBswModeMachineInstanceConfigs.append(value)
        return self

    def getRteBswRequiredClientServerConnectionList(self) -> List[Any]:
        return self.rteBswRequiredClientServerConnections

    def addRteBswRequiredClientServerConnection(self, value: Any) -> 'RteBswModuleInstance':
        self.rteBswRequiredClientServerConnections.append(value)
        return self

    def getRteBswRequiredModeGroupConnectionList(self) -> List[Any]:
        return self.rteBswRequiredModeGroupConnections

    def addRteBswRequiredModeGroupConnection(self, value: Any) -> 'RteBswModuleInstance':
        self.rteBswRequiredModeGroupConnections.append(value)
        return self

    def getRteBswRequiredSenderReceiverConnectionList(self) -> List[Any]:
        return self.rteBswRequiredSenderReceiverConnections

    def addRteBswRequiredSenderReceiverConnection(self, value: Any) -> 'RteBswModuleInstance':
        self.rteBswRequiredSenderReceiverConnections.append(value)
        return self

    def getRteBswRequiredTriggerConnectionList(self) -> List[Any]:
        return self.rteBswRequiredTriggerConnections

    def addRteBswRequiredTriggerConnection(self, value: Any) -> 'RteBswModuleInstance':
        self.rteBswRequiredTriggerConnections.append(value)
        return self

    def getRteMappedToOsApplicationRef(self) -> Optional[EcucRefType]:
        return self.rteMappedToOsApplicationRef

    def setRteMappedToOsApplicationRef(self, value: EcucRefType) -> 'RteBswModuleInstance':
        self.rteMappedToOsApplicationRef = value
        return self


class Rte(Module):
    def __init__(self, parent: Optional['EcucObject']) -> None:
        super().__init__(parent, "Rte")

        self.rteBswModuleInstances: List[RteBswModuleInstance] = []
        self.rteSwComponentInstances: List[RteSwComponentInstance] = []

    def getRteBswModuleInstance(self, name: str) -> Optional[RteBswModuleInstance]:
        result = list(filter(lambda a: a.name == name, self.rteBswModuleInstances))
        if len(result) > 0:
            return result[0]
        return None

    def getRteBswModuleInstanceList(self) -> List[RteBswModuleInstance]:
        return list(sorted(self.rteBswModuleInstances, key=lambda o: o.name))

    def addRteBswModuleInstance(self, value: RteBswModuleInstance) -> None:
        self.elements[value.getName()] = value
        self.rteBswModuleInstances.append(value)

    def getRteSwComponentInstance(self, name: str) -> Optional[RteSwComponentInstance]:
        result = list(filter(lambda a: a.name == name, self.rteSwComponentInstances))
        if len(result) > 0:
            return result[0]
        return None

    def getRteSwComponentInstanceList(self) -> List[RteSwComponentInstance]:
        return list(sorted(self.rteSwComponentInstances, key=lambda o: o.name))

    def addRteSwComponentInstance(self, value: RteSwComponentInstance) -> None:
        self.elements[value.getName()] = value
        self.rteSwComponentInstances.append(value)

    def getRteModuleInstanceList(self) -> List[AbstractRteInstance]:
        filtered = [cast(AbstractRteInstance, a) for a in self.elements.values() if isinstance(a, AbstractRteInstance)]
        return list(sorted(filtered, key=lambda o: o.name))  # type: ignore[arg-type]

    def _addToRteEventToOsTasks(self, mapping: AbstractEventToTaskMapping, os_tasks: Dict[str, List[AbstractEventToTaskMapping]]) -> None:
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
        os_tasks: Dict[str, List[AbstractEventToTaskMapping]] = {}
        for instance in self.getRteModuleInstanceList():
            if isinstance(instance, RteBswModuleInstance):
                for mapping in instance.getRteBswEventToTaskMappingList():
                    self._addToRteEventToOsTasks(mapping, os_tasks)  # type: ignore[arg-type]
            elif isinstance(instance, RteSwComponentInstance):
                for mapping in instance.getRteEventToTaskMappingList():
                    self._addToRteEventToOsTasks(mapping, os_tasks)
            else:
                raise NotImplementedError("Invalid Rte Module Instance <%s>" % type(instance))

        return os_tasks
