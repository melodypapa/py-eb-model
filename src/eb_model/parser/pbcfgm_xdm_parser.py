import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.pbcfgm_xdm import PbcfgM, PbcfgMGeneral, PbcfgMProtectionSet, PbcfgMCoreProtectionSet
from ..parser.eb_parser import AbstractEbModelParser


class PbcfgMXdmParser(AbstractEbModelParser):
    def __init__(self) -> None:
        super().__init__()

        self.pbcfgm = None

    def parse(self, element: ET.Element, doc: EBModel):
        if self.get_component_name(element) != "PbcfgM":
            raise ValueError("Invalid <%s> xdm file" % "PbcfgM")

        pbcfgm = doc.getPbcfgM()

        self.read_version(element, pbcfgm)

        self.logger.info("Parse PbcfgM ARVersion:<%s> SwVersion:<%s>" % (pbcfgm.getArVersion().getVersion(), pbcfgm.getSwVersion().getVersion()))

        self.pbcfgm = pbcfgm

        self.read_pbcfgm_general(element, pbcfgm)
        self.read_pbcfgm_protection_sets(element, pbcfgm)
        self.read_pbcfgm_core_protection_sets(element, pbcfgm)

    def read_pbcfgm_general(self, element: ET.Element, pbcfgm: PbcfgM):
        ctr_tag = self.find_ctr_tag(element, "PbcfgMGeneral")
        if ctr_tag is not None:
            general = PbcfgMGeneral(pbcfgm, ctr_tag.attrib["name"])
            general.setPbcfgMDevErrorDetect(self.read_value(ctr_tag, "PbcfgMDevErrorDetect"))
            general.setPbcfgMInitConfiguration(self.read_optional_value(ctr_tag, "PbcfgMInitConfiguration"))
            pbcfgm.setPbcfgMGeneral(general)
            self.logger.debug("Read PbcfgMGeneral")

    def read_pbcfgm_protection_sets(self, element: ET.Element, pbcfgm: PbcfgM):
        for ctr_tag in self.find_ctr_tag_list(element, "PbcfgMProtectionSet"):
            protection_set = PbcfgMProtectionSet(pbcfgm, ctr_tag.attrib["name"])
            protection_set.setPbcfgMProtectionSetName(self.read_value(ctr_tag, "PbcfgMProtectionSetName"))
            pbcfgm.addPbcfgMProtectionSet(protection_set)
            self.logger.debug("Read PbcfgMProtectionSet <%s>" % protection_set.getName())

    def read_pbcfgm_core_protection_sets(self, element: ET.Element, pbcfgm: PbcfgM):
        for ctr_tag in self.find_ctr_tag_list(element, "PbcfgMCoreProtectionSet"):
            core_protection_set = PbcfgMCoreProtectionSet(pbcfgm, ctr_tag.attrib["name"])
            core_protection_set.setPbcfgMCoreProtectionSetRef(self.read_ref_value(ctr_tag, "PbcfgMCoreProtectionSetRef"))
            pbcfgm.addPbcfgMCoreProtectionSet(core_protection_set)
            self.logger.debug("Read PbcfgMCoreProtectionSet <%s>" % core_protection_set.getName())
