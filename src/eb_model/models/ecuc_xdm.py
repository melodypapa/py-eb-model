
from typing import List
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class EcucPartition(EcucParamConfContainerDef):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.EcucPartitionId: int = None
        self.EcucPartitionRef: EcucRefType = None
        self.EcucPartitionBswModuleDistinguishedPartitions: List[EcucRefType] = []
        self.EcucPartitionCoreRef: EcucRefType = None
        self.EcucPartitionSoftwareComponentInstanceRefs: List[EcucRefType] = []

    def getEcucPartitionId(self) -> int:
        return self.EcucPartitionId

    def setEcuPartitionId(self, partitionId: int):
        self.EcucPartitionId = partitionId
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

    def getEcucPartitionSoftwareComponentInstanceRefs(self) -> List[EcucRefType]:
        return self.EcucPartitionSoftwareComponentInstanceRefs

    def addEcucPartitionSoftwareComponentInstanceRef(self, ref: EcucRefType):
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
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.EcucPartitionCollection = None

    def getEcucPartitionCollection(self):
        return self.EcucPartitionCollection

    def setEcucPartitionCollection(self, partition_collection: EcucPartitionCollection):
        self.EcucPartitionCollection = partition_collection
        return self