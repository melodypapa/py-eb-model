import xml.etree.cElementTree as ET

from ..models.eb_doc import EBModel
from ..parser.eb_parser import AbstractEbModelParser


class EcucXdmParser(AbstractEbModelParser):
    def __init__(self):
        super().__init__()

        self.ecuc = None

    def parse(self, element: ET.Element, doc: EBModel):
        if self.get_component_name(element) != "NvM":
            raise ValueError("Invalid <%s> xdm file" % "EcuC")

        ecuc = doc.getEcuC()

        self.read_version(element, ecuc)

        self.logger.info("Parse Ecuc ARVersion:<%s> SwVersion:<%s>" % (ecuc.getArVersion().getVersion(), ecuc.getSwVersion().getVersion()))

        self.ecuc = ecuc

        self.read_ecuc_partition_collection(element, ecuc)

    def read_nvm_common(self, element: ET.Element, nvm: NvM):
        ctr_tag = self.find_ctr_tag(element, "NvMCommon")
        if ctr_tag is not None:
            nvm_common = NvMCommon(nvm, "NvMCommon")