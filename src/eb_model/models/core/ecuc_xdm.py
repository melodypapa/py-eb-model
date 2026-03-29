from typing import List
from .abstract import EcucParamConfContainerDef, EcucRefType, Module


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
        self.ecucPartitionBswModuleExecution: bool = None
        self.ecucPartitionQmBswModuleExecution: bool = None

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

    def getEcucPartitionBswModuleExecution(self) -> bool:
        return self.ecucPartitionBswModuleExecution

    def setEcucPartitionBswModuleExecution(self, value: bool):
        if value is not None:
            self.ecucPartitionBswModuleExecution = value
        return self

    def getEcucPartitionQmBswModuleExecution(self) -> bool:
        return self.ecucPartitionQmBswModuleExecution

    def setEcucPartitionQmBswModuleExecution(self, value: bool):
        if value is not None:
            self.ecucPartitionQmBswModuleExecution = value
        return self


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


class EcucGeneral(EcucParamConfContainerDef):
    """
    General EcuC configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.devErrorDetect: bool = None
        self.loadTolerant: bool = None

    def getDevErrorDetect(self) -> bool:
        return self.devErrorDetect

    def setDevErrorDetect(self, value: bool):
        if value is not None:
            self.devErrorDetect = value
        return self

    def getLoadTolerant(self) -> bool:
        return self.loadTolerant

    def setLoadTolerant(self, value: bool):
        if value is not None:
            self.loadTolerant = value
        return self


class EcucHardware(EcucParamConfContainerDef):
    """
    Hardware configuration for EcuC.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class EcucCoreDefinition(EcucParamConfContainerDef):
    """
    Core definition for multi-core EcuC.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class EcucPduCollection(EcucParamConfContainerDef):
    """
    PDU collection for EcuC.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class MetaDataType(EcucParamConfContainerDef):
    """
    Metadata type definition.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class MetaDataItem(EcucParamConfContainerDef):
    """
    Metadata item definition.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class Pdu(EcucParamConfContainerDef):
    """
    PDU definition for EcuC.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class EcucPduDedicatedPartition(EcucParamConfContainerDef):
    """
    Dedicated partition for PDU.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class EcucPostBuildVariants(EcucParamConfContainerDef):
    """
    Post-build variants configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class EcucVariationResolver(EcucParamConfContainerDef):
    """
    Variation resolver configuration.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


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
        self.commonPublishedInformation: CommonPublishedInformation = None
        self.publishedInformation: PublishedInformation = None
        self.ecucGeneral: EcucGeneral = None
        self.ecucHardware: EcucHardware = None
        self.ecucCoreDefinition: EcucCoreDefinition = None
        self.ecucPduCollection: EcucPduCollection = None
        self.metaDataType: MetaDataType = None
        self.metaDataItem: MetaDataItem = None
        self.pdu: Pdu = None
        self.ecucPduDedicatedPartition: EcucPduDedicatedPartition = None
        self.ecucPostBuildVariants: EcucPostBuildVariants = None
        self.ecucVariationResolver: EcucVariationResolver = None

    def getEcucPartitionCollection(self) -> EcucPartitionCollection:
        return self.ecucPartitionCollection

    def setEcucPartitionCollection(self, collection: EcucPartitionCollection):
        if collection is not None:
            self.ecucPartitionCollection = collection
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

    def getEcucGeneral(self) -> EcucGeneral:
        return self.ecucGeneral

    def setEcucGeneral(self, value: EcucGeneral):
        if value is not None:
            self.ecucGeneral = value
        return self

    def getEcucHardware(self) -> EcucHardware:
        return self.ecucHardware

    def setEcucHardware(self, value: EcucHardware):
        if value is not None:
            self.ecucHardware = value
        return self

    def getEcucCoreDefinition(self) -> EcucCoreDefinition:
        return self.ecucCoreDefinition

    def setEcucCoreDefinition(self, value: EcucCoreDefinition):
        if value is not None:
            self.ecucCoreDefinition = value
        return self

    def getEcucPduCollection(self) -> EcucPduCollection:
        return self.ecucPduCollection

    def setEcucPduCollection(self, value: EcucPduCollection):
        if value is not None:
            self.ecucPduCollection = value
        return self

    def getMetaDataType(self) -> MetaDataType:
        return self.metaDataType

    def setMetaDataType(self, value: MetaDataType):
        if value is not None:
            self.metaDataType = value
        return self

    def getMetaDataItem(self) -> MetaDataItem:
        return self.metaDataItem

    def setMetaDataItem(self, value: MetaDataItem):
        if value is not None:
            self.metaDataItem = value
        return self

    def getPdu(self) -> Pdu:
        return self.pdu

    def setPdu(self, value: Pdu):
        if value is not None:
            self.pdu = value
        return self

    def getEcucPduDedicatedPartition(self) -> EcucPduDedicatedPartition:
        return self.ecucPduDedicatedPartition

    def setEcucPduDedicatedPartition(self, value: EcucPduDedicatedPartition):
        if value is not None:
            self.ecucPduDedicatedPartition = value
        return self

    def getEcucPostBuildVariants(self) -> EcucPostBuildVariants:
        return self.ecucPostBuildVariants

    def setEcucPostBuildVariants(self, value: EcucPostBuildVariants):
        if value is not None:
            self.ecucPostBuildVariants = value
        return self

    def getEcucVariationResolver(self) -> EcucVariationResolver:
        return self.ecucVariationResolver

    def setEcucVariationResolver(self, value: EcucVariationResolver):
        if value is not None:
            self.ecucVariationResolver = value
        return self
