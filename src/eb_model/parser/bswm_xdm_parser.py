from ..parser.eb_parser import AbstractEbModelParser
import xml.etree.cElementTree as ET
from ..models.eb_doc import EBModel


class BswMXdmParser(AbstractEbModelParser):
    def __init__(self):
        super().__init__()

        self.bswm = None

    def parse(self, element: ET.Element, doc: EBModel):
        if self.get_component_name(element) != "BswM":
            raise ValueError("Invalid <%s> xdm file" % "BswM")
