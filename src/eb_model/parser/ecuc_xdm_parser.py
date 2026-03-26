"""
EcuC XDM Parser Module - Extracts AUTOSAR EcuC configuration from EB Tresos XDM files.

Implements:
    - SWR_ECUC_00001: EcuC module parsing
    - SWR_ECUC_00002: Partition configuration parsing
    - SWR_ECUC_00003: Partition collection parsing
"""
import xml.etree.ElementTree as ET

from ..models.ecuc_xdm import EcuC, EcucPartition, EcucPartitionCollection, EcucPartitionSoftwareComponentInstanceRef
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
            ecuc_partition.setPartitionCanBeRestarted(self.read_value(ctr_tag, "PartitionCanBeRestarted"))

            self.read_ecuc_partition_software_component_instances(ctr_tag, ecuc_partition)
            collection.addEcucPartition(ecuc_partition)

            
