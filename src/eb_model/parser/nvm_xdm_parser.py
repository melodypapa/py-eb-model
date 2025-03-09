import xml.etree.ElementTree as ET

from ..models.nvm_xdm import NvM, NvMBlockDescriptor
from ..models.eb_doc import EBModel
from ..parser.eb_parser import AbstractEbModelParser


class NvMXdmParser(AbstractEbModelParser):
    def __init__(self, ) -> None:
        super().__init__()

        self.nvm = None

    def parse(self, element: ET.Element, doc: EBModel):
        if self.get_component_name(element) != "NvM":
            raise ValueError("Invalid <%s> xdm file" % "NvM")

        nvm = doc.getNvM()

        self.read_version(element, nvm)

        self.logger.info("Parse NvM ARVersion:<%s> SwVersion:<%s>" % (nvm.getArVersion().getVersion(), nvm.getSwVersion().getVersion()))

        self.nvm = nvm

        self.read_nvm_block_descriptors(element, nvm)

    def read_nvm_block_descriptors(self, element: ET.Element, nvm: NvM):
        for ctr_tag in self.find_ctr_tag_list(element, "NvMBlockDescriptor"):
            nvm_block = NvMBlockDescriptor(nvm, ctr_tag.attrib["name"])
            nvm_block.setNvMBlockCrcType(self.read_optional_value(ctr_tag, "NvMBlockCrcType")) \
                     .setNvMBlockEcucPartitionRef(self.read_ref_value(ctr_tag, "NvMBlockEcucPartitionRef")) \
                     .setNvMNvramBlockIdentifier(self.read_value(ctr_tag, "NvMNvramBlockIdentifier")) \
                     .setNvMRamBlockDataAddress(self.read_optional_value(ctr_tag, "NvMRamBlockDataAddress")) \
                     .setNvMRomBlockDataAddress(self.read_optional_value(ctr_tag, "NvMRomBlockDataAddress")) \
                     .setNvMRomBlockNum(self.read_value(ctr_tag, "NvMRomBlockNum")) \
                     .setNvMBlockManagementType(self.read_value(ctr_tag, "NvMBlockManagementType")) \
                     .setNvMNvBlockLength(self.read_value(ctr_tag, "NvMNvBlockLength")) \
                     .setNvMNvBlockNum(self.read_value(ctr_tag, "NvMNvBlockNum")) \
                     .setNvMSelectBlockForReadAll(self.read_value(ctr_tag, "NvMSelectBlockForReadAll")) \
                     .setNvMSelectBlockForWriteAll(self.read_value(ctr_tag, "NvMSelectBlockForWriteAll")) 

            nvm.addNvMBlockDescriptor(nvm_block)
                     
