
from typing import List
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class EcucPartitionSoftwareComponentInstanceRef(EcucParamConfContainerDef):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.TargetRef: EcucRefType = None

    def getTarget(self) -> EcucRefType:
        return self.TargetRef
    
    def setTargetRef(self, target: EcucRefType):
        self.TargetRef = target
        return self


class EcucPartition(EcucParamConfContainerDef):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.EcucPartitionId: int = None
        self.EcucDefaultBswPartition: bool = None
        self.PartitionCanBeRestarted: bool = None
        self.EcucPartitionRef: EcucRefType = None

        self.EcucPartitionBswModuleDistinguishedPartitions: List[EcucRefType] = []
        self.EcucPartitionCoreRef: EcucRefType = None
        self.EcucPartitionSoftwareComponentInstanceRefs: List[EcucPartitionSoftwareComponentInstanceRef] = []

    def getEcucPartitionId(self) -> int:
        return self.EcucPartitionId

    def setEcuPartitionId(self, partitionId: int):
        self.EcucPartitionId = partitionId
        return self
    
    def getEcucDefaultBswPartition(self) -> bool:
        return self.EcucDefaultBswPartition
    
    def setEcucDefaultBswPartition(self, is_default: bool):
        self.EcucDefaultBswPartition = is_default
        return self
    
    def getPartitionCanBeRestarted(self) -> bool:
        return self.PartitionCanBeRestarted
    
    def setPartitionCanBeRestarted(self, can_be_restarted: bool):
        self.PartitionCanBeRestarted = can_be_restarted
        return self
    
    def getEcucPartitionRef(self) -> EcucRefType:
        return self.EcucPartitionRef

    def setEcucPartitionRef(self, ref: EcucRefType):
        self.EcucPartitionRef = ref
        return self

    def getEcucPartitionBswModuleDistinguishedPartition(self) -> List[EcucRefType]:
        return self.EcucPartitionBswModuleDistinguishedPartitions

    def addEcucPartitionBswModuleDistinguishedPartition(self, partition: EcucRefType):
        self.EcucPartitionBswModuleDistinguishedPartitions.append(partition)
        return self

    def getEcucPartitionCoreRef(self) -> EcucRefType:
        return self.EcucPartitionCoreRef

    def setEcucPartitionCoreRef(self, core_ref: EcucRefType):
        self.EcucPartitionCoreRef = core_ref
        return self

    def getEcucPartitionSoftwareComponentInstanceRefs(self) -> List[EcucPartitionSoftwareComponentInstanceRef]:
        return self.EcucPartitionSoftwareComponentInstanceRefs

    def addEcucPartitionSoftwareComponentInstanceRef(self, ref: EcucPartitionSoftwareComponentInstanceRef):
        self.EcucPartitionSoftwareComponentInstanceRefs.append(ref)
        return self


class EcucPartitionCollection(EcucParamConfContainerDef):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.EcucPartitions: List[EcucPartition] = []

    def getEcucPartitions(self) -> List[EcucPartition]:
        return self.EcucPartitions

    def addEcucPartition(self, partition: EcucPartition):
        self.EcucPartitions.append(partition)
        return self
    

class EcuC(Module):
    def __init__(self, parent):
        super().__init__(parent, "EcuC")

        self.EcucPartitionCollection = None

    def getEcucPartitionCollection(self) -> EcucPartitionCollection:
        return self.EcucPartitionCollection

    def setEcucPartitionCollection(self, collection: EcucPartitionCollection):
        self.EcucPartitionCollection = collection
        return self
