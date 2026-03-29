"""
EcuC XDM Parser Module - Extracts AUTOSAR EcuC configuration from EB Tresos XDM files.

Implements:
    - SWR_ECUC_00001: EcuC module parsing
    - SWR_ECUC_00002: Partition configuration parsing
    - SWR_ECUC_00003: Partition collection parsing
"""
import xml.etree.ElementTree as ET

from ..models.ecuc_xdm import EcuC, EcucPartition, EcucPartitionCollection, EcucPartitionSoftwareComponentInstanceRef, CommonPublishedInformation, PublishedInformation, EcucGeneral, EcucHardware, EcucCoreDefinition, EcucPduCollection, MetaDataType, MetaDataItem, Pdu, EcucPduDedicatedPartition, EcucPostBuildVariants, EcucVariationResolver
from ..models.eb_doc import EBModel
from ..parser.eb_parser import AbstractEbModelParser


class EcucXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR EcuC (ECU Configuration) module.

    Extracts EcuC configuration including partitions and partition collections.

    Implements: SWR_ECUC_00001 (EcuC Module Parser)
    """

    def __init__(self):
        """Initialize the EcuC XDM parser."""
        super().__init__()

        self.ecuc = None

    def read_common_published_information(self, element: ET.Element, ecuc: EcuC):
        """
        Parse CommonPublishedInformation container from XDM.
        """
        ctr_tag = self.find_ctr_tag(element, "CommonPublishedInformation")
        if ctr_tag is not None:
            pub_info = CommonPublishedInformation(ecuc, ctr_tag.attrib["name"])
            pub_info.setArMajorVersion(self.read_value(ctr_tag, "ArMajorVersion"))
            pub_info.setArMinorVersion(self.read_value(ctr_tag, "ArMinorVersion"))
            pub_info.setArPatchVersion(self.read_value(ctr_tag, "ArPatchVersion"))
            pub_info.setSwMajorVersion(self.read_value(ctr_tag, "SwMajorVersion"))
            pub_info.setSwMinorVersion(self.read_value(ctr_tag, "SwMinorVersion"))
            pub_info.setSwPatchVersion(self.read_value(ctr_tag, "SwPatchVersion"))
            ecuc.setCommonPublishedInformation(pub_info)
            self.logger.debug("Read CommonPublishedInformation")

    def read_published_information(self, element: ET.Element, ecuc: EcuC):
        """
        Parse PublishedInformation container from XDM.
        """
        ctr_tag = self.find_ctr_tag(element, "PublishedInformation")
        if ctr_tag is not None:
            pub_info = PublishedInformation(ecuc, ctr_tag.attrib["name"])
            pub_info.setVendorId(self.read_value(ctr_tag, "VendorId"))
            pub_info.setArReleaseMajorVersion(self.read_value(ctr_tag, "ArReleaseMajorVersion"))
            pub_info.setArReleaseMinorVersion(self.read_value(ctr_tag, "ArReleaseMinorVersion"))
            pub_info.setArReleasePatchVersion(self.read_value(ctr_tag, "ArReleasePatchVersion"))
            pub_info.setSwMajorVersion(self.read_value(ctr_tag, "SwMajorVersion"))
            pub_info.setSwMinorVersion(self.read_value(ctr_tag, "SwMinorVersion"))
            pub_info.setSwPatchVersion(self.read_value(ctr_tag, "SwPatchVersion"))
            ecuc.setPublishedInformation(pub_info)
            self.logger.debug("Read PublishedInformation")

    def read_ecuc_general(self, element: ET.Element, ecuc: EcuC):
        """
        Parse EcucGeneral container from XDM.
        """
        ctr_tag = self.find_ctr_tag(element, "EcucGeneral")
        if ctr_tag is not None:
            general = EcucGeneral(ecuc, ctr_tag.attrib["name"])
            general.setDevErrorDetect(self.read_optional_value(ctr_tag, "DevErrorDetect"))
            general.setLoadTolerant(self.read_optional_value(ctr_tag, "LoadTolerant"))
            ecuc.setEcucGeneral(general)
            self.logger.debug("Read EcucGeneral")

    def read_ecuc_hardware(self, element: ET.Element, ecuc: EcuC):
        """Parse EcucHardware container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "EcucHardware")
        if ctr_tag is not None:
            hardware = EcucHardware(ecuc, ctr_tag.attrib["name"])
            ecuc.setEcucHardware(hardware)
            self.logger.debug("Read EcucHardware")

    def read_ecuc_core_definition(self, element: ET.Element, ecuc: EcuC):
        """Parse EcucCoreDefinition container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "EcucCoreDefinition")
        if ctr_tag is not None:
            core_def = EcucCoreDefinition(ecuc, ctr_tag.attrib["name"])
            ecuc.setEcucCoreDefinition(core_def)
            self.logger.debug("Read EcucCoreDefinition")

    def read_ecuc_pdu_collection(self, element: ET.Element, ecuc: EcuC):
        """Parse EcucPduCollection container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "EcucPduCollection")
        if ctr_tag is not None:
            pdu_collection = EcucPduCollection(ecuc, ctr_tag.attrib["name"])
            ecuc.setEcucPduCollection(pdu_collection)
            self.logger.debug("Read EcucPduCollection")

    def read_meta_data_type(self, element: ET.Element, ecuc: EcuC):
        """Parse MetaDataType container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "MetaDataType")
        if ctr_tag is not None:
            meta_type = MetaDataType(ecuc, ctr_tag.attrib["name"])
            ecuc.setMetaDataType(meta_type)
            self.logger.debug("Read MetaDataType")

    def read_meta_data_item(self, element: ET.Element, ecuc: EcuC):
        """Parse MetaDataItem container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "MetaDataItem")
        if ctr_tag is not None:
            meta_item = MetaDataItem(ecuc, ctr_tag.attrib["name"])
            ecuc.setMetaDataItem(meta_item)
            self.logger.debug("Read MetaDataItem")

    def read_pdu(self, element: ET.Element, ecuc: EcuC):
        """Parse Pdu container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "Pdu")
        if ctr_tag is not None:
            pdu = Pdu(ecuc, ctr_tag.attrib["name"])
            ecuc.setPdu(pdu)
            self.logger.debug("Read Pdu")

    def read_ecuc_pdu_dedicated_partition(self, element: ET.Element, ecuc: EcuC):
        """Parse EcucPduDedicatedPartition container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "EcucPduDedicatedPartition")
        if ctr_tag is not None:
            pdu_partition = EcucPduDedicatedPartition(ecuc, ctr_tag.attrib["name"])
            ecuc.setEcucPduDedicatedPartition(pdu_partition)
            self.logger.debug("Read EcucPduDedicatedPartition")

    def read_ecuc_post_build_variants(self, element: ET.Element, ecuc: EcuC):
        """Parse EcucPostBuildVariants container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "EcucPostBuildVariants")
        if ctr_tag is not None:
            post_build = EcucPostBuildVariants(ecuc, ctr_tag.attrib["name"])
            ecuc.setEcucPostBuildVariants(post_build)
            self.logger.debug("Read EcucPostBuildVariants")

    def read_ecuc_variation_resolver(self, element: ET.Element, ecuc: EcuC):
        """Parse EcucVariationResolver container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "EcucVariationResolver")
        if ctr_tag is not None:
            variation_resolver = EcucVariationResolver(ecuc, ctr_tag.attrib["name"])
            ecuc.setEcucVariationResolver(variation_resolver)
            self.logger.debug("Read EcucVariationResolver")

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse EcuC module configuration from XDM element.

        Implements: SWR_ECUC_00001
        """
        if self.get_component_name(element) != "EcuC":
            raise ValueError("Invalid <%s> xdm file" % "EcuC")

        ecuc = doc.getEcuC()

        self.read_version(element, ecuc)

        self.logger.info("Parse Ecuc ARVersion:<%s> SwVersion:<%s>" % (ecuc.getArVersion().getVersion(), ecuc.getSwVersion().getVersion()))

        self.ecuc = ecuc

        self.read_common_published_information(element, ecuc)
        self.read_published_information(element, ecuc)
        self.read_ecuc_general(element, ecuc)
        self.read_ecuc_hardware(element, ecuc)
        self.read_ecuc_core_definition(element, ecuc)
        self.read_ecuc_pdu_collection(element, ecuc)
        self.read_meta_data_type(element, ecuc)
        self.read_meta_data_item(element, ecuc)
        self.read_pdu(element, ecuc)
        self.read_ecuc_pdu_dedicated_partition(element, ecuc)
        self.read_ecuc_post_build_variants(element, ecuc)
        self.read_ecuc_variation_resolver(element, ecuc)

        self.read_ecuc_partition_collection(element, ecuc)

    def read_ecuc_partition_collection(self, element: ET.Element, ecuc: EcuC):
        ctr_tag = self.find_ctr_tag(element, "EcucPartitionCollection")
        if ctr_tag is not None:
            collection = EcucPartitionCollection(ecuc, "EcucPartitionCollection")
            self.read_ecuc_partition(ctr_tag, collection)
            ecuc.setEcucPartitionCollection(collection)

    def read_ecuc_partition_software_component_instances(self, element: ET.Element, ecuc_partition: EcucPartition):
        for ctr_tag in self.find_ctr_tag_list(element, "EcucPartitionSoftwareComponentInstanceRef"):
            instance = EcucPartitionSoftwareComponentInstanceRef(ecuc_partition, ctr_tag.attrib['type'])
            instance.setEcucPartitionSoftwareComponentInstanceTargetRef(self.read_ref_value(ctr_tag, "TARGET"))
            if instance.getEcucPartitionSoftwareComponentInstanceTargetRef() is not None:
                self.logger.debug("Instance: %s" % instance.getEcucPartitionSoftwareComponentInstanceTargetRef().getShortName())
                ecuc_partition.addEcucPartitionSoftwareComponentInstanceRef(instance)
    
    def read_ecuc_partition(self, element: ET.Element, collection: EcucPartitionCollection):
        for ctr_tag in self.find_ctr_tag_list(element, "EcucPartition"):
            ecuc_partition = EcucPartition(collection, ctr_tag.attrib["name"])
            self.logger.info("Parse EcucPartition <%s>" % ecuc_partition.getName())

            ecuc_partition.setEcucDefaultBswPartition(self.read_optional_value(ctr_tag, "EcucDefaultBswPartition"))
            ecuc_partition.setEcucPartitionCanBeRestarted(self.read_optional_value(ctr_tag, "PartitionCanBeRestarted"))
            ecuc_partition.setEcucPartitionBswModuleExecution(self.read_optional_value(ctr_tag, "EcucPartitionBswModuleExecution"))
            ecuc_partition.setEcucPartitionQmBswModuleExecution(self.read_optional_value(ctr_tag, "EcucPartitionQmBswModuleExecution"))

            self.read_ecuc_partition_software_component_instances(ctr_tag, ecuc_partition)
            collection.addEcucPartition(ecuc_partition)

            
