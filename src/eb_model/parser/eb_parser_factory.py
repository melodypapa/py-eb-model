import logging
import xml.etree.cElementTree as ET

from .rte_xdm_parser import RteXdmParser
from .ecuc_xdm_parser import EcucXdmParser
from .os_xdm_parser import OsXdmParser
from .nvm_xdm_parser import NvMXdmParser
from .eb_parser import AbstractEbModelParser


class EbParserFactory:
    
    @classmethod
    def get_component_name(cls, filename: str) -> str:
        tree = ET.parse(filename)
        ns = dict([node for _, node in ET.iterparse(filename, events=['start-ns'])])
        tag = tree.getroot().find(".//d:chc[@type='AR-ELEMENT'][@value='MODULE-CONFIGURATION']", ns)
        return tag.attrib['name']
    
    @classmethod
    def create(self, xdm: str) -> AbstractEbModelParser:
        logging.getLogger().info("Analyzing file <%s>" % xdm)

        name = EbParserFactory.get_component_name(xdm)

        if name == "Os":
            return OsXdmParser()
        elif name == "Rte":
            return RteXdmParser()
        if name == "NvM":
            return NvMXdmParser()
        elif name == "EcuC":
            return EcucXdmParser()
        else:
            raise NotImplementedError("Unsupported EB xdm file <%s>" % name)
