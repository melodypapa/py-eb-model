import xml.etree.cElementTree as ET

from ..models.ecuc_xdm import EcuC, EcucPartition, EcucPartitionCollection, EcucPartitionSoftwareComponentInstanceRef
from ..models.eb_doc import EBModel
from ..parser.eb_parser import AbstractEbModelParser


class EcucXdmParser(AbstractEbModelParser):
    def __init__(self):
        super().__init__()

        self.ecuc = None

    def parse(self, element: ET.Element, doc: EBModel):
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
            instance.setTargetRef(self.read_ref_value(ctr_tag, "TARGET"))
            if instance.getTargetRef() is not None:
                self.logger.info("Instance: %s" % instance.getTargetRef().getShortName())
                ecuc_partition.addEcucPartitionSoftwareComponentInstanceRef(instance)
    
    def read_ecuc_partition(self, element: ET.Element, collection: EcucPartitionCollection):
        for ctr_tag in self.find_ctr_tag_list(element, "EcucPartition"):
            ecuc_partition = EcucPartition(collection, ctr_tag.attrib["name"])
            self.logger.info("Parse EcucPartition <%s>" % ecuc_partition.getName())

            ecuc_partition.setEcucDefaultBswPartition(self.read_optional_value(ctr_tag, "EcucDefaultBswPartition"))
            ecuc_partition.setPartitionCanBeRestarted(self.read_value(ctr_tag, "PartitionCanBeRestarted"))
            # ecuc_partition.setEcucPartitionRef(self.read_optional_ref_value(ctr_tag, "EcucEcuPartitionRef"))

            self.read_ecuc_partition_software_component_instances(ctr_tag, ecuc_partition)
            collection.addEcucPartition(ecuc_partition)

            
