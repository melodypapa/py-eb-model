import xml.etree.ElementTree as ET
import logging
from ..models.eb_doc import PreferenceModel
from ..models.importer_xdm import SystemDescriptionImporter
from . import AbstractEbModelParser

class PerfXdmParser(AbstractEbModelParser):
    def __init__(self, ) -> None:
        super().__init__()

        self.logger = logging.getLogger()

    def parse_input_files(self, element: ET.Element, importer: SystemDescriptionImporter):
        for ctr_tag in self.find_ctr_tag_list(element, "InputFiles"):
            file_name = self.read_value(ctr_tag, "FileName")
            self.logger.debug("Add the file <%s>" % file_name)
            importer.addInputFile(file_name)

    def parse_preference(self, element: ET.Element, doc: PreferenceModel):
        importer = doc.getSystemDescriptionImporter()

        for ctr_tag in self.find_ctr_tag_list(element, "SystemDescriptionImporters"):
            self.logger.info("Parse SystemDescriptionImporters: <%s>" % ctr_tag.attrib["name"])
            self.parse_input_files(ctr_tag, importer)
            #importer.addInputFile()