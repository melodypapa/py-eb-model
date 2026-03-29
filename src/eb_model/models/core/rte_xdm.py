from typing import Any, Dict, List, Optional, cast
from .abstract import EcucObject, EcucParamConfContainerDef, EcucRefType, Module


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


class RteBswGeneral(EcucParamConfContainerDef):
    """
    BSW general configuration for Rte module.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteGenerationScheduleTableRef: Optional[EcucRefType] = None
        self.rteDevelopmentErrorDetect: bool = None
        self.rteUseApplConfig: bool = None

    def getRteGenerationScheduleTableRef(self) -> Optional[EcucRefType]:
        return self.rteGenerationScheduleTableRef

    def setRteGenerationScheduleTableRef(self, value: Optional[EcucRefType]) -> 'RteBswGeneral':
        self.rteGenerationScheduleTableRef = value
        return self

    def getRteDevelopmentErrorDetect(self) -> bool:
        return self.rteDevelopmentErrorDetect

    def setRteDevelopmentErrorDetect(self, value: bool) -> 'RteBswGeneral':
        if value is not None:
            self.rteDevelopmentErrorDetect = value
        return self

    def getRteUseApplConfig(self) -> bool:
        return self.rteUseApplConfig

    def setRteUseApplConfig(self, value: bool) -> 'RteBswGeneral':
        if value is not None:
            self.rteUseApplConfig = value
        return self


class RteBswEventToIsrMapping(EcucParamConfContainerDef):
    """
    BSW event to ISR mapping configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteBswEventRef: Optional[EcucRefType] = None
        self.rteBswMappedToIsrRef: Optional[EcucRefType] = None
        self.rteBswPositionInIsr: int = None

    def getRteBswEventRef(self) -> Optional[EcucRefType]:
        return self.rteBswEventRef

    def setRteBswEventRef(self, value: Optional[EcucRefType]) -> 'RteBswEventToIsrMapping':
        self.rteBswEventRef = value
        return self

    def getRteBswMappedToIsrRef(self) -> Optional[EcucRefType]:
        return self.rteBswMappedToIsrRef

    def setRteBswMappedToIsrRef(self, value: Optional[EcucRefType]) -> 'RteBswEventToIsrMapping':
        self.rteBswMappedToIsrRef = value
        return self

    def getRteBswPositionInIsr(self) -> int:
        return self.rteBswPositionInIsr

    def setRteBswPositionInIsr(self, value: int) -> 'RteBswEventToIsrMapping':
        self.rteBswPositionInIsr = value
        return self


class RteBswExclusiveAreaImpl(EcucParamConfContainerDef):
    """
    BSW exclusive area implementation configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteBswExclusiveAreaRef: Optional[EcucRefType] = None
        self.rteBswExclusiveAreaImplementationType: str = None

    def getRteBswExclusiveAreaRef(self) -> Optional[EcucRefType]:
        return self.rteBswExclusiveAreaRef

    def setRteBswExclusiveAreaRef(self, value: Optional[EcucRefType]) -> 'RteBswExclusiveAreaImpl':
        self.rteBswExclusiveAreaRef = value
        return self

    def getRteBswExclusiveAreaImplementationType(self) -> str:
        return self.rteBswExclusiveAreaImplementationType

    def setRteBswExclusiveAreaImplementationType(self, value: str) -> 'RteBswExclusiveAreaImpl':
        self.rteBswExclusiveAreaImplementationType = value
        return self


class RteBswExternalTriggerConfig(EcucParamConfContainerDef):
    """
    BSW external trigger configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteBswExternalTriggerRef: Optional[EcucRefType] = None

    def getRteBswExternalTriggerRef(self) -> Optional[EcucRefType]:
        return self.rteBswExternalTriggerRef

    def setRteBswExternalTriggerRef(self, value: Optional[EcucRefType]) -> 'RteBswExternalTriggerConfig':
        self.rteBswExternalTriggerRef = value
        return self


class RteBswInternalTriggerConfig(EcucParamConfContainerDef):
    """
    BSW internal trigger configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteBswInternalTriggerRef: Optional[EcucRefType] = None

    def getRteBswInternalTriggerRef(self) -> Optional[EcucRefType]:
        return self.rteBswInternalTriggerRef

    def setRteBswInternalTriggerRef(self, value: Optional[EcucRefType]) -> 'RteBswInternalTriggerConfig':
        self.rteBswInternalTriggerRef = value
        return self


class RteBswRequiredModeGroupConnection(EcucParamConfContainerDef):
    """
    BSW required mode group connection configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteBswModeGroupConnectionRef: Optional[EcucRefType] = None

    def getRteBswModeGroupConnectionRef(self) -> Optional[EcucRefType]:
        return self.rteBswModeGroupConnectionRef

    def setRteBswModeGroupConnectionRef(self, value: Optional[EcucRefType]) -> 'RteBswRequiredModeGroupConnection':
        self.rteBswModeGroupConnectionRef = value
        return self


class RteBswRequiredSenderReceiverConnection(EcucParamConfContainerDef):
    """
    BSW required sender receiver connection configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteBswSenderReceiverConnectionRef: Optional[EcucRefType] = None

    def getRteBswSenderReceiverConnectionRef(self) -> Optional[EcucRefType]:
        return self.rteBswSenderReceiverConnectionRef

    def setRteBswSenderReceiverConnectionRef(self, value: Optional[EcucRefType]) -> 'RteBswRequiredSenderReceiverConnection':
        self.rteBswSenderReceiverConnectionRef = value
        return self


class RteBswRequiredClientServerConnection(EcucParamConfContainerDef):
    """
    BSW required client server connection configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteBswClientServerConnectionRef: Optional[EcucRefType] = None

    def getRteBswClientServerConnectionRef(self) -> Optional[EcucRefType]:
        return self.rteBswClientServerConnectionRef

    def setRteBswClientServerConnectionRef(self, value: Optional[EcucRefType]) -> 'RteBswRequiredClientServerConnection':
        self.rteBswClientServerConnectionRef = value
        return self


class RteBswRequiredTriggerConnection(EcucParamConfContainerDef):
    """
    BSW required trigger connection configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteBswTriggerConnectionRef: Optional[EcucRefType] = None

    def getRteBswTriggerConnectionRef(self) -> Optional[EcucRefType]:
        return self.rteBswTriggerConnectionRef

    def setRteBswTriggerConnectionRef(self, value: Optional[EcucRefType]) -> 'RteBswRequiredTriggerConnection':
        self.rteBswTriggerConnectionRef = value
        return self


class RteGeneration(EcucParamConfContainerDef):
    """
    RTE generation configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteGenerationConfiguration: str = None
        self.rteGenerationToolRef: Optional[EcucRefType] = None

    def getRteGenerationConfiguration(self) -> str:
        return self.rteGenerationConfiguration

    def setRteGenerationConfiguration(self, value: str) -> 'RteGeneration':
        self.rteGenerationConfiguration = value
        return self

    def getRteGenerationToolRef(self) -> Optional[EcucRefType]:
        return self.rteGenerationToolRef

    def setRteGenerationToolRef(self, value: Optional[EcucRefType]) -> 'RteGeneration':
        self.rteGenerationToolRef = value
        return self


class ComTaskConfiguration(EcucParamConfContainerDef):
    """
    Communication task configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteComTaskRef: Optional[EcucRefType] = None

    def getRteComTaskRef(self) -> Optional[EcucRefType]:
        return self.rteComTaskRef

    def setRteComTaskRef(self, value: Optional[EcucRefType]) -> 'ComTaskConfiguration':
        self.rteComTaskRef = value
        return self


class BswConfiguration(EcucParamConfContainerDef):
    """
    BSW configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteBswModuleConfigRef: Optional[EcucRefType] = None

    def getRteBswModuleConfigRef(self) -> Optional[EcucRefType]:
        return self.rteBswModuleConfigRef

    def setRteBswModuleConfigRef(self, value: Optional[EcucRefType]) -> 'BswConfiguration':
        self.rteBswModuleConfigRef = value
        return self


class OsCounterAssignments(EcucParamConfContainerDef):
    """
    OS counter assignments configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteOsCounterRef: Optional[EcucRefType] = None

    def getRteOsCounterRef(self) -> Optional[EcucRefType]:
        return self.rteOsCounterRef

    def setRteOsCounterRef(self, value: Optional[EcucRefType]) -> 'OsCounterAssignments':
        self.rteOsCounterRef = value
        return self


class CooperativeTasks(EcucParamConfContainerDef):
    """
    Cooperative tasks configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteCooperativeTaskRef: Optional[EcucRefType] = None

    def getRteCooperativeTaskRef(self) -> Optional[EcucRefType]:
        return self.rteCooperativeTaskRef

    def setRteCooperativeTaskRef(self, value: Optional[EcucRefType]) -> 'CooperativeTasks':
        self.rteCooperativeTaskRef = value
        return self


class TaskChain(EcucParamConfContainerDef):
    """
    Task chain configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteTaskChainRef: Optional[EcucRefType] = None

    def getRteTaskChainRef(self) -> Optional[EcucRefType]:
        return self.rteTaskChainRef

    def setRteTaskChainRef(self, value: Optional[EcucRefType]) -> 'TaskChain':
        self.rteTaskChainRef = value
        return self


class RteImplicitCommunication(EcucParamConfContainerDef):
    """
    RTE implicit communication configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteImplicitCommunicationType: str = None

    def getRteImplicitCommunicationType(self) -> str:
        return self.rteImplicitCommunicationType

    def setRteImplicitCommunicationType(self, value: str) -> 'RteImplicitCommunication':
        self.rteImplicitCommunicationType = value
        return self


class RteInitializationBehavior(EcucParamConfContainerDef):
    """
    RTE initialization behavior configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteInitializationBehavior: str = None

    def getRteInitializationBehavior(self) -> str:
        return self.rteInitializationBehavior

    def setRteInitializationBehavior(self, value: str) -> 'RteInitializationBehavior':
        self.rteInitializationBehavior = value
        return self


class RteInitializationRunnableBatch(EcucParamConfContainerDef):
    """
    RTE initialization runnable batch configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteInitializationRunnableRef: Optional[EcucRefType] = None

    def getRteInitializationRunnableRef(self) -> Optional[EcucRefType]:
        return self.rteInitializationRunnableRef

    def setRteInitializationRunnableRef(self, value: Optional[EcucRefType]) -> 'RteInitializationRunnableBatch':
        self.rteInitializationRunnableRef = value
        return self


class RteOsInteraction(EcucParamConfContainerDef):
    """
    RTE OS interaction configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteOsInteractionType: str = None

    def getRteOsInteractionType(self) -> str:
        return self.rteOsInteractionType

    def setRteOsInteractionType(self, value: str) -> 'RteOsInteraction':
        self.rteOsInteractionType = value
        return self


class RteModeToScheduleTableMapping(EcucParamConfContainerDef):
    """
    RTE mode to schedule table mapping configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteModeRef: Optional[EcucRefType] = None
        self.rteScheduleTableRef: Optional[EcucRefType] = None

    def getRteModeRef(self) -> Optional[EcucRefType]:
        return self.rteModeRef

    def setRteModeRef(self, value: Optional[EcucRefType]) -> 'RteModeToScheduleTableMapping':
        self.rteModeRef = value
        return self

    def getRteScheduleTableRef(self) -> Optional[EcucRefType]:
        return self.rteScheduleTableRef

    def setRteScheduleTableRef(self, value: Optional[EcucRefType]) -> 'RteModeToScheduleTableMapping':
        self.rteScheduleTableRef = value
        return self


class RteRips(EcucParamConfContainerDef):
    """
    RTE RIPs configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteRipsConfiguration: str = None

    def getRteRipsConfiguration(self) -> str:
        return self.rteRipsConfiguration

    def setRteRipsConfiguration(self, value: str) -> 'RteRips':
        self.rteRipsConfiguration = value
        return self


class DataMappings(EcucParamConfContainerDef):
    """
    Data mappings configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteDataMappingRef: Optional[EcucRefType] = None

    def getRteDataMappingRef(self) -> Optional[EcucRefType]:
        return self.rteDataMappingRef

    def setRteDataMappingRef(self, value: Optional[EcucRefType]) -> 'DataMappings':
        self.rteDataMappingRef = value
        return self


class RteExclusiveAreaImplementation(EcucParamConfContainerDef):
    """
    RTE exclusive area implementation configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteExclusiveAreaRef: Optional[EcucRefType] = None
        self.rteExclusiveAreaImplementationType: str = None

    def getRteExclusiveAreaRef(self) -> Optional[EcucRefType]:
        return self.rteExclusiveAreaRef

    def setRteExclusiveAreaRef(self, value: Optional[EcucRefType]) -> 'RteExclusiveAreaImplementation':
        self.rteExclusiveAreaRef = value
        return self

    def getRteExclusiveAreaImplementationType(self) -> str:
        return self.rteExclusiveAreaImplementationType

    def setRteExclusiveAreaImplementationType(self, value: str) -> 'RteExclusiveAreaImplementation':
        self.rteExclusiveAreaImplementationType = value
        return self


class RteExternalTriggerConfig(EcucParamConfContainerDef):
    """
    RTE external trigger configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteExternalTriggerRef: Optional[EcucRefType] = None

    def getRteExternalTriggerRef(self) -> Optional[EcucRefType]:
        return self.rteExternalTriggerRef

    def setRteExternalTriggerRef(self, value: Optional[EcucRefType]) -> 'RteExternalTriggerConfig':
        self.rteExternalTriggerRef = value
        return self


class RteInternalTriggerConfig(EcucParamConfContainerDef):
    """
    RTE internal trigger configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteInternalTriggerRef: Optional[EcucRefType] = None

    def getRteInternalTriggerRef(self) -> Optional[EcucRefType]:
        return self.rteInternalTriggerRef

    def setRteInternalTriggerRef(self, value: Optional[EcucRefType]) -> 'RteInternalTriggerConfig':
        self.rteInternalTriggerRef = value
        return self


class RteNvRamAllocation(EcucParamConfContainerDef):
    """
    RTE NVRAM allocation configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteNvRamBlockRef: Optional[EcucRefType] = None

    def getRteNvRamBlockRef(self) -> Optional[EcucRefType]:
        return self.rteNvRamBlockRef

    def setRteNvRamBlockRef(self, value: Optional[EcucRefType]) -> 'RteNvRamAllocation':
        self.rteNvRamBlockRef = value
        return self


class RteSwComponentType(EcucParamConfContainerDef):
    """
    RTE SW component type configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.rteSwComponentTypeRef: Optional[EcucRefType] = None

    def getRteSwComponentTypeRef(self) -> Optional[EcucRefType]:
        return self.rteSwComponentTypeRef

    def setRteSwComponentTypeRef(self, value: Optional[EcucRefType]) -> 'RteSwComponentType':
        self.rteSwComponentTypeRef = value
        return self


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
        self.rteActivationOffset: float = None
        self.rtePeriod: float = None
        self.rteImmediateRestart: bool = None
        self.rteNvmRamBlockLocationSymbol: str = None
        self.rteInitRunnableRef: Optional[EcucRefType] = None
        self.rteCallbacks: List[Any] = []
        self.rteDataSendPoints: List[Any] = []
        self.rteDataReceivePoints: List[Any] = []
        self.rteDataConsumePoints: List[Any] = []
        self.rteServerCallPoints: List[Any] = []
        self.rteClientCallPoints: List[Any] = []
        self.rteModeSwitchPoints: List[Any] = []
        self.rteTriggerPoints: List[Any] = []
        self.rteCommunicationErrorHandling: bool = None
        self.rteDataConsistency: bool = None
        self.rteDataUpdate: bool = None
        self.rteMessageSending: bool = None
        self.rteMessageReception: bool = None
        self.rteComponentInstanceVariableLocking: bool = None
        self.rteComponentInstanceLocalDataLocking: bool = None
        self.rteComponentInstanceInterInstanceDataLocking: bool = None

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

    def getRteActivationOffset(self) -> float:
        return self.rteActivationOffset

    def setRteActivationOffset(self, value: float) -> 'RteSwComponentInstance':
        self.rteActivationOffset = value
        return self

    def getRtePeriod(self) -> float:
        return self.rtePeriod

    def setRtePeriod(self, value: float) -> 'RteSwComponentInstance':
        self.rtePeriod = value
        return self

    def getRteImmediateRestart(self) -> bool:
        return self.rteImmediateRestart

    def setRteImmediateRestart(self, value: bool) -> 'RteSwComponentInstance':
        self.rteImmediateRestart = value
        return self

    def getRteNvmRamBlockLocationSymbol(self) -> str:
        return self.rteNvmRamBlockLocationSymbol

    def setRteNvmRamBlockLocationSymbol(self, value: str) -> 'RteSwComponentInstance':
        self.rteNvmRamBlockLocationSymbol = value
        return self

    def getRteInitRunnableRef(self) -> Optional[EcucRefType]:
        return self.rteInitRunnableRef

    def setRteInitRunnableRef(self, value: Optional[EcucRefType]) -> 'RteSwComponentInstance':
        self.rteInitRunnableRef = value
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

    def getRteCallbacks(self) -> List[Any]:
        return self.rteCallbacks

    def addRteCallback(self, value: Any) -> 'RteSwComponentInstance':
        self.rteCallbacks.append(value)
        return self

    def getRteDataSendPoints(self) -> List[Any]:
        return self.rteDataSendPoints

    def addRteDataSendPoint(self, value: Any) -> 'RteSwComponentInstance':
        self.rteDataSendPoints.append(value)
        return self

    def getRteDataReceivePoints(self) -> List[Any]:
        return self.rteDataReceivePoints

    def addRteDataReceivePoint(self, value: Any) -> 'RteSwComponentInstance':
        self.rteDataReceivePoints.append(value)
        return self

    def getRteDataConsumePoints(self) -> List[Any]:
        return self.rteDataConsumePoints

    def addRteDataConsumePoint(self, value: Any) -> 'RteSwComponentInstance':
        self.rteDataConsumePoints.append(value)
        return self

    def getRteServerCallPoints(self) -> List[Any]:
        return self.rteServerCallPoints

    def addRteServerCallPoint(self, value: Any) -> 'RteSwComponentInstance':
        self.rteServerCallPoints.append(value)
        return self

    def getRteClientCallPoints(self) -> List[Any]:
        return self.rteClientCallPoints

    def addRteClientCallPoint(self, value: Any) -> 'RteSwComponentInstance':
        self.rteClientCallPoints.append(value)
        return self

    def getRteModeSwitchPoints(self) -> List[Any]:
        return self.rteModeSwitchPoints

    def addRteModeSwitchPoint(self, value: Any) -> 'RteSwComponentInstance':
        self.rteModeSwitchPoints.append(value)
        return self

    def getRteTriggerPoints(self) -> List[Any]:
        return self.rteTriggerPoints

    def addRteTriggerPoint(self, value: Any) -> 'RteSwComponentInstance':
        self.rteTriggerPoints.append(value)
        return self

    def getRteCommunicationErrorHandling(self) -> bool:
        return self.rteCommunicationErrorHandling

    def setRteCommunicationErrorHandling(self, value: bool) -> 'RteSwComponentInstance':
        self.rteCommunicationErrorHandling = value
        return self

    def getRteDataConsistency(self) -> bool:
        return self.rteDataConsistency

    def setRteDataConsistency(self, value: bool) -> 'RteSwComponentInstance':
        self.rteDataConsistency = value
        return self

    def getRteDataUpdate(self) -> bool:
        return self.rteDataUpdate

    def setRteDataUpdate(self, value: bool) -> 'RteSwComponentInstance':
        self.rteDataUpdate = value
        return self

    def getRteMessageSending(self) -> bool:
        return self.rteMessageSending

    def setRteMessageSending(self, value: bool) -> 'RteSwComponentInstance':
        self.rteMessageSending = value
        return self

    def getRteMessageReception(self) -> bool:
        return self.rteMessageReception

    def setRteMessageReception(self, value: bool) -> 'RteSwComponentInstance':
        self.rteMessageReception = value
        return self

    def getRteComponentInstanceVariableLocking(self) -> bool:
        return self.rteComponentInstanceVariableLocking

    def setRteComponentInstanceVariableLocking(self, value: bool) -> 'RteSwComponentInstance':
        self.rteComponentInstanceVariableLocking = value
        return self

    def getRteComponentInstanceLocalDataLocking(self) -> bool:
        return self.rteComponentInstanceLocalDataLocking

    def setRteComponentInstanceLocalDataLocking(self, value: bool) -> 'RteSwComponentInstance':
        self.rteComponentInstanceLocalDataLocking = value
        return self

    def getRteComponentInstanceInterInstanceDataLocking(self) -> bool:
        return self.rteComponentInstanceInterInstanceDataLocking

    def setRteComponentInstanceInterInstanceDataLocking(self, value: bool) -> 'RteSwComponentInstance':
        self.rteComponentInstanceInterInstanceDataLocking = value
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
        self.rteBswModuleInitRef: Optional[EcucRefType] = None
        self.rteBswModuleDeinitRef: Optional[EcucRefType] = None
        self.rteBswComponentTypeRef: Optional[EcucRefType] = None
        self.rteBswProvideModeSwitchFunctions: bool = None
        self.rteBswInitFunction: Optional[EcucRefType] = None
        self.rteBswDeinitFunction: Optional[EcucRefType] = None
        self.rteBswCallbacks: List[Any] = []
        self.rteBswModuleVariableLocking: bool = None
        self.rteBswModuleInterfaceLocking: bool = None
        self.rteBswModuleLocalDataLocking: bool = None
        self.rteBswModuleInterModuleDataLocking: bool = None
        self.rteBswModuleNvmDataLocking: bool = None
        self.rteBswModuleEnableModeSwitch: bool = None
        self.rteBswModuleEnableRouting: bool = None
        self.rteBswModuleEnableSequencing: bool = None
        self.rteBswModuleTimeoutMonitoring: bool = None
        self.rteBswModuleErrorHandling: bool = None
        self.rteBswModuleDefaultMonitoring: bool = None
        self.rteBswModuleProvideComponentMonitoring: bool = None
        self.rteBswModuleTimingProtection: bool = None
        self.rteBswModuleResourceManagement: bool = None
        self.rteBswModuleScheduling: bool = None

    def getRteBswImplementationRef(self) -> Optional[EcucRefType]:
        return self.rteBswImplementationRef

    def setRteBswImplementationRef(self, value: EcucRefType) -> 'RteBswModuleInstance':
        self.rteBswImplementationRef = value
        return self

    def getRteBswModuleInitRef(self) -> Optional[EcucRefType]:
        return self.rteBswModuleInitRef

    def setRteBswModuleInitRef(self, value: Optional[EcucRefType]) -> 'RteBswModuleInstance':
        self.rteBswModuleInitRef = value
        return self

    def getRteBswModuleDeinitRef(self) -> Optional[EcucRefType]:
        return self.rteBswModuleDeinitRef

    def setRteBswModuleDeinitRef(self, value: Optional[EcucRefType]) -> 'RteBswModuleInstance':
        self.rteBswModuleDeinitRef = value
        return self

    def getRteBswComponentTypeRef(self) -> Optional[EcucRefType]:
        return self.rteBswComponentTypeRef

    def setRteBswComponentTypeRef(self, value: Optional[EcucRefType]) -> 'RteBswModuleInstance':
        self.rteBswComponentTypeRef = value
        return self

    def getRteBswProvideModeSwitchFunctions(self) -> bool:
        return self.rteBswProvideModeSwitchFunctions

    def setRteBswProvideModeSwitchFunctions(self, value: bool) -> 'RteBswModuleInstance':
        self.rteBswProvideModeSwitchFunctions = value
        return self

    def getRteBswInitFunction(self) -> Optional[EcucRefType]:
        return self.rteBswInitFunction

    def setRteBswInitFunction(self, value: Optional[EcucRefType]) -> 'RteBswModuleInstance':
        self.rteBswInitFunction = value
        return self

    def getRteBswDeinitFunction(self) -> Optional[EcucRefType]:
        return self.rteBswDeinitFunction

    def setRteBswDeinitFunction(self, value: Optional[EcucRefType]) -> 'RteBswModuleInstance':
        self.rteBswDeinitFunction = value
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

    def getRteBswCallbacks(self) -> List[Any]:
        return self.rteBswCallbacks

    def addRteBswCallback(self, value: Any) -> 'RteBswModuleInstance':
        self.rteBswCallbacks.append(value)
        return self

    def getRteBswModuleVariableLocking(self) -> bool:
        return self.rteBswModuleVariableLocking

    def setRteBswModuleVariableLocking(self, value: bool) -> 'RteBswModuleInstance':
        self.rteBswModuleVariableLocking = value
        return self

    def getRteBswModuleInterfaceLocking(self) -> bool:
        return self.rteBswModuleInterfaceLocking

    def setRteBswModuleInterfaceLocking(self, value: bool) -> 'RteBswModuleInstance':
        self.rteBswModuleInterfaceLocking = value
        return self

    def getRteBswModuleLocalDataLocking(self) -> bool:
        return self.rteBswModuleLocalDataLocking

    def setRteBswModuleLocalDataLocking(self, value: bool) -> 'RteBswModuleInstance':
        self.rteBswModuleLocalDataLocking = value
        return self

    def getRteBswModuleInterModuleDataLocking(self) -> bool:
        return self.rteBswModuleInterModuleDataLocking

    def setRteBswModuleInterModuleDataLocking(self, value: bool) -> 'RteBswModuleInstance':
        self.rteBswModuleInterModuleDataLocking = value
        return self

    def getRteBswModuleNvmDataLocking(self) -> bool:
        return self.rteBswModuleNvmDataLocking

    def setRteBswModuleNvmDataLocking(self, value: bool) -> 'RteBswModuleInstance':
        self.rteBswModuleNvmDataLocking = value
        return self

    def getRteBswModuleEnableModeSwitch(self) -> bool:
        return self.rteBswModuleEnableModeSwitch

    def setRteBswModuleEnableModeSwitch(self, value: bool) -> 'RteBswModuleInstance':
        self.rteBswModuleEnableModeSwitch = value
        return self

    def getRteBswModuleEnableRouting(self) -> bool:
        return self.rteBswModuleEnableRouting

    def setRteBswModuleEnableRouting(self, value: bool) -> 'RteBswModuleInstance':
        self.rteBswModuleEnableRouting = value
        return self

    def getRteBswModuleEnableSequencing(self) -> bool:
        return self.rteBswModuleEnableSequencing

    def setRteBswModuleEnableSequencing(self, value: bool) -> 'RteBswModuleInstance':
        self.rteBswModuleEnableSequencing = value
        return self

    def getRteBswModuleTimeoutMonitoring(self) -> bool:
        return self.rteBswModuleTimeoutMonitoring

    def setRteBswModuleTimeoutMonitoring(self, value: bool) -> 'RteBswModuleInstance':
        self.rteBswModuleTimeoutMonitoring = value
        return self

    def getRteBswModuleErrorHandling(self) -> bool:
        return self.rteBswModuleErrorHandling

    def setRteBswModuleErrorHandling(self, value: bool) -> 'RteBswModuleInstance':
        self.rteBswModuleErrorHandling = value
        return self

    def getRteBswModuleDefaultMonitoring(self) -> bool:
        return self.rteBswModuleDefaultMonitoring

    def setRteBswModuleDefaultMonitoring(self, value: bool) -> 'RteBswModuleInstance':
        self.rteBswModuleDefaultMonitoring = value
        return self

    def getRteBswModuleProvideComponentMonitoring(self) -> bool:
        return self.rteBswModuleProvideComponentMonitoring

    def setRteBswModuleProvideComponentMonitoring(self, value: bool) -> 'RteBswModuleInstance':
        self.rteBswModuleProvideComponentMonitoring = value
        return self

    def getRteBswModuleTimingProtection(self) -> bool:
        return self.rteBswModuleTimingProtection

    def setRteBswModuleTimingProtection(self, value: bool) -> 'RteBswModuleInstance':
        self.rteBswModuleTimingProtection = value
        return self

    def getRteBswModuleResourceManagement(self) -> bool:
        return self.rteBswModuleResourceManagement

    def setRteBswModuleResourceManagement(self, value: bool) -> 'RteBswModuleInstance':
        self.rteBswModuleResourceManagement = value
        return self

    def getRteBswModuleScheduling(self) -> bool:
        return self.rteBswModuleScheduling

    def setRteBswModuleScheduling(self, value: bool) -> 'RteBswModuleInstance':
        self.rteBswModuleScheduling = value
        return self


class Rte(Module):
    def __init__(self, parent: Optional['EcucObject']) -> None:
        super().__init__(parent, "Rte")

        self.rteBswModuleInstances: List[RteBswModuleInstance] = []
        self.rteSwComponentInstances: List[RteSwComponentInstance] = []
        self.commonPublishedInformation: CommonPublishedInformation = None
        self.publishedInformation: PublishedInformation = None
        self.rteBswGeneral: RteBswGeneral = None
        self.rteGeneration: RteGeneration = None
        self.comTaskConfigurations: List[ComTaskConfiguration] = []
        self.bswConfigurations: List[BswConfiguration] = []
        self.osCounterAssignments: List[OsCounterAssignments] = []
        self.cooperativeTasks: List[CooperativeTasks] = []
        self.taskChains: List[TaskChain] = []
        self.rteImplicitCommunication: RteImplicitCommunication = None
        self.rteInitializationBehavior: RteInitializationBehavior = None
        self.rteInitializationRunnableBatches: List[RteInitializationRunnableBatch] = []
        self.rteOsInteraction: RteOsInteraction = None
        self.rteModeToScheduleTableMappings: List[RteModeToScheduleTableMapping] = []
        self.rteRips: RteRips = None
        self.dataMappings: List[DataMappings] = []
        self.rteExclusiveAreaImplementations: List[RteExclusiveAreaImplementation] = []
        self.rteExternalTriggerConfigs: List[RteExternalTriggerConfig] = []
        self.rteInternalTriggerConfigs: List[RteInternalTriggerConfig] = []
        self.rteNvRamAllocations: List[RteNvRamAllocation] = []
        self.rteSwComponentTypes: List[RteSwComponentType] = []

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

    def getRteBswGeneral(self) -> RteBswGeneral:
        return self.rteBswGeneral

    def setRteBswGeneral(self, value: RteBswGeneral):
        if value is not None:
            self.rteBswGeneral = value
        return self

    def getRteGeneration(self) -> RteGeneration:
        return self.rteGeneration

    def setRteGeneration(self, value: RteGeneration):
        if value is not None:
            self.rteGeneration = value
        return self

    def getComTaskConfigurationList(self) -> List[ComTaskConfiguration]:
        return list(sorted(filter(lambda a: isinstance(a, ComTaskConfiguration), self.elements.values()), key=lambda o: o.getName()))

    def addComTaskConfiguration(self, value: ComTaskConfiguration):
        self.addElement(value)
        self.comTaskConfigurations.append(value)
        return self

    def getBswConfigurationList(self) -> List[BswConfiguration]:
        return list(sorted(filter(lambda a: isinstance(a, BswConfiguration), self.elements.values()), key=lambda o: o.getName()))

    def addBswConfiguration(self, value: BswConfiguration):
        self.addElement(value)
        self.bswConfigurations.append(value)
        return self

    def getOsCounterAssignmentList(self) -> List[OsCounterAssignments]:
        return list(sorted(filter(lambda a: isinstance(a, OsCounterAssignments), self.elements.values()), key=lambda o: o.getName()))

    def addOsCounterAssignment(self, value: OsCounterAssignments):
        self.addElement(value)
        self.osCounterAssignments.append(value)
        return self

    def getCooperativeTaskList(self) -> List[CooperativeTasks]:
        return list(sorted(filter(lambda a: isinstance(a, CooperativeTasks), self.elements.values()), key=lambda o: o.getName()))

    def addCooperativeTask(self, value: CooperativeTasks):
        self.addElement(value)
        self.cooperativeTasks.append(value)
        return self

    def getTaskChainList(self) -> List[TaskChain]:
        return list(sorted(filter(lambda a: isinstance(a, TaskChain), self.elements.values()), key=lambda o: o.getName()))

    def addTaskChain(self, value: TaskChain):
        self.addElement(value)
        self.taskChains.append(value)
        return self

    def getRteImplicitCommunication(self) -> RteImplicitCommunication:
        return self.rteImplicitCommunication

    def setRteImplicitCommunication(self, value: RteImplicitCommunication):
        if value is not None:
            self.rteImplicitCommunication = value
        return self

    def getRteInitializationBehavior(self) -> RteInitializationBehavior:
        return self.rteInitializationBehavior

    def setRteInitializationBehavior(self, value: RteInitializationBehavior):
        if value is not None:
            self.rteInitializationBehavior = value
        return self

    def getRteInitializationRunnableBatchList(self) -> List[RteInitializationRunnableBatch]:
        return list(sorted(filter(lambda a: isinstance(a, RteInitializationRunnableBatch), self.elements.values()), key=lambda o: o.getName()))

    def addRteInitializationRunnableBatch(self, value: RteInitializationRunnableBatch):
        self.addElement(value)
        self.rteInitializationRunnableBatches.append(value)
        return self

    def getRteOsInteraction(self) -> RteOsInteraction:
        return self.rteOsInteraction

    def setRteOsInteraction(self, value: RteOsInteraction):
        if value is not None:
            self.rteOsInteraction = value
        return self

    def getRteModeToScheduleTableMappingList(self) -> List[RteModeToScheduleTableMapping]:
        return list(sorted(filter(lambda a: isinstance(a, RteModeToScheduleTableMapping), self.elements.values()), key=lambda o: o.getName()))

    def addRteModeToScheduleTableMapping(self, value: RteModeToScheduleTableMapping):
        self.addElement(value)
        self.rteModeToScheduleTableMappings.append(value)
        return self

    def getRteRips(self) -> RteRips:
        return self.rteRips

    def setRteRips(self, value: RteRips):
        if value is not None:
            self.rteRips = value
        return self

    def getDataMappingList(self) -> List[DataMappings]:
        return list(sorted(filter(lambda a: isinstance(a, DataMappings), self.elements.values()), key=lambda o: o.getName()))

    def addDataMapping(self, value: DataMappings):
        self.addElement(value)
        self.dataMappings.append(value)
        return self

    def getRteExclusiveAreaImplementationList(self) -> List[RteExclusiveAreaImplementation]:
        return list(sorted(filter(lambda a: isinstance(a, RteExclusiveAreaImplementation), self.elements.values()), key=lambda o: o.getName()))

    def addRteExclusiveAreaImplementation(self, value: RteExclusiveAreaImplementation):
        self.addElement(value)
        self.rteExclusiveAreaImplementations.append(value)
        return self

    def getRteExternalTriggerConfigList(self) -> List[RteExternalTriggerConfig]:
        return list(sorted(filter(lambda a: isinstance(a, RteExternalTriggerConfig), self.elements.values()), key=lambda o: o.getName()))

    def addRteExternalTriggerConfig(self, value: RteExternalTriggerConfig):
        self.addElement(value)
        self.rteExternalTriggerConfigs.append(value)
        return self

    def getRteInternalTriggerConfigList(self) -> List[RteInternalTriggerConfig]:
        return list(sorted(filter(lambda a: isinstance(a, RteInternalTriggerConfig), self.elements.values()), key=lambda o: o.getName()))

    def addRteInternalTriggerConfig(self, value: RteInternalTriggerConfig):
        self.addElement(value)
        self.rteInternalTriggerConfigs.append(value)
        return self

    def getRteNvRamAllocationList(self) -> List[RteNvRamAllocation]:
        return list(sorted(filter(lambda a: isinstance(a, RteNvRamAllocation), self.elements.values()), key=lambda o: o.getName()))

    def addRteNvRamAllocation(self, value: RteNvRamAllocation):
        self.addElement(value)
        self.rteNvRamAllocations.append(value)
        return self

    def getRteSwComponentTypeList(self) -> List[RteSwComponentType]:
        return list(sorted(filter(lambda a: isinstance(a, RteSwComponentType), self.elements.values()), key=lambda o: o.getName()))

    def addRteSwComponentType(self, value: RteSwComponentType):
        self.addElement(value)
        self.rteSwComponentTypes.append(value)
        return self

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
