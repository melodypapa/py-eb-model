from typing import List
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class EcucPartitionSoftwareComponentInstanceRef(EcucParamConfContainerDef):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.ecucPartitionSoftwareComponentInstanceTargetRef: EcucRefType = None

    def getEcucPartitionSoftwareComponentInstanceTargetRef(self) -> EcucRefType:
        return self.ecucPartitionSoftwareComponentInstanceTargetRef

    def setEcucPartitionSoftwareComponentInstanceTargetRef(self, target: EcucRefType):
        self.ecucPartitionSoftwareComponentInstanceTargetRef = target
        return self


class EcucPartition(EcucParamConfContainerDef):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.ecucPartitionId: int = None
        self.ecucDefaultBswPartition: bool = None
        self.ecucPartitionCanBeRestarted: bool = None
        self.ecucPartitionRef: EcucRefType = None

        self.ecucPartitionBswModuleDistinguishedPartitions: List[EcucRefType] = []
        self.ecucPartitionCoreRef: EcucRefType = None
        self.ecucPartitionSoftwareComponentInstanceRefs: List[EcucPartitionSoftwareComponentInstanceRef] = []

    def getEcucPartitionId(self) -> int:
        return self.ecucPartitionId

    def setEcucPartitionId(self, partitionId: int):
        if partitionId is not None:
            self.ecucPartitionId = partitionId
        return self

    def getEcucDefaultBswPartition(self) -> bool:
        return self.ecucDefaultBswPartition

    def setEcucDefaultBswPartition(self, is_default: bool):
        if is_default is not None:
            self.ecucDefaultBswPartition = is_default
        return self

    def getEcucPartitionCanBeRestarted(self) -> bool:
        return self.ecucPartitionCanBeRestarted

    def setEcucPartitionCanBeRestarted(self, can_be_restarted: bool):
        if can_be_restarted is not None:
            self.ecucPartitionCanBeRestarted = can_be_restarted
        return self

    def getEcucPartitionRef(self) -> EcucRefType:
        return self.ecucPartitionRef

    def setEcucPartitionRef(self, ref: EcucRefType):
        if ref is not None:
            self.ecucPartitionRef = ref
        return self

    def getEcucPartitionBswModuleDistinguishedPartitions(self) -> List[EcucRefType]:
        return self.ecucPartitionBswModuleDistinguishedPartitions

    def addEcucPartitionBswModuleDistinguishedPartition(self, partition: EcucRefType):
        if partition is not None:
            self.ecucPartitionBswModuleDistinguishedPartitions.append(partition)
        return self

    def getEcucPartitionCoreRef(self) -> EcucRefType:
        return self.ecucPartitionCoreRef

    def setEcucPartitionCoreRef(self, core_ref: EcucRefType):
        if core_ref is not None:
            self.ecucPartitionCoreRef = core_ref
        return self

    def getEcucPartitionSoftwareComponentInstanceRefs(self) -> List[EcucPartitionSoftwareComponentInstanceRef]:
        return self.ecucPartitionSoftwareComponentInstanceRefs

    def addEcucPartitionSoftwareComponentInstanceRef(self, ref: EcucPartitionSoftwareComponentInstanceRef):
        if ref is not None:
            self.ecucPartitionSoftwareComponentInstanceRefs.append(ref)
        return self


class EcucPartitionCollection(EcucParamConfContainerDef):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.ecucPartitions: List[EcucPartition] = []

    def getEcucPartitions(self) -> List[EcucPartition]:
        return self.ecucPartitions

    def addEcucPartition(self, partition: EcucPartition):
        if partition is not None:
            self.addElement(partition)
            self.ecucPartitions.append(partition)
        return self


class EcuC(Module):
    def __init__(self, parent):
        super().__init__(parent, "EcuC")

        self.ecucPartitionCollection = None

    def getEcucPartitionCollection(self) -> EcucPartitionCollection:
        return self.ecucPartitionCollection

    def setEcucPartitionCollection(self, collection: EcucPartitionCollection):
        if collection is not None:
            self.ecucPartitionCollection = collection
        return self
