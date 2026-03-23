import logging
import xml.etree.ElementTree as ET

from .rte_xdm_parser import RteXdmParser
from .ecuc_xdm_parser import EcucXdmParser
from .os_xdm_parser import OsXdmParser
from .nvm_xdm_parser import NvMXdmParser
from .tm_xdm_parser import TmXdmParser
from .pbcfgm_xdm_parser import PbcfgMXdmParser
from .ecum_xdm_parser import EcuMXdmParser
from .det_xdm_parser import DetXdmParser
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

        parsers = {
            "Os": OsXdmParser,
            "Rte": RteXdmParser,
            "NvM": NvMXdmParser,
            "EcuC": EcucXdmParser,
            "Tm": TmXdmParser,
            "PbcfgM": PbcfgMXdmParser,
            "EcuM": EcuMXdmParser,
            "Det": DetXdmParser,
        }

        if name in parsers:
            return parsers[name]()
        else:
            raise NotImplementedError("Unsupported EB xdm file <%s>" % name)
