"""
Com XDM Parser Module - Extracts AUTOSAR COM configuration from EB Tresos XDM files.

Implements:
    - SWR_COM_00001: Com module parsing
    - SWR_COM_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET
from eb_model.models.core.eb_doc import EBModel
from eb_model.models.com_stack.com_xdm import Com, ComGeneral
from eb_model.parser.core.eb_parser import AbstractEbModelParser


class ComXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR COM (Communication) module configuration.

    Extracts COM configuration including general parameters and signal
    configurations for inter-module communication.

    Implements: SWR_COM_00001 (Com Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the Com XDM parser."""
        super().__init__()

        self.com = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse Com module configuration from XDM element.

        Implements: SWR_COM_00001
        """
        if self.get_component_name(element) != "Com":
            raise ValueError("Invalid <%s> xdm file" % "Com")

        com = doc.getCom()

        self.read_version(element, com)

        self.logger.info("Parse Com ARVersion:<%s> SwVersion:<%s>" % (com.getArVersion().getVersion(), com.getSwVersion().getVersion()))

        self.com = com

        self.read_com_general(element, com)

    def read_com_general(self, element: ET.Element, com: Com):
        """
        Parse ComGeneral container from XDM.

        Implements: SWR_COM_00002
        """
        ctr_tag = self.find_ctr_tag(element, "ComConfig")
        if ctr_tag is not None:
            general = ComGeneral(com, ctr_tag.attrib["name"])
            general.setComEnableUserSupport(self.read_value(ctr_tag, "ComEnableUserSupport"))
            general.setComUserInitSignal(self.read_value(ctr_tag, "ComUserInitSignal"))
            general.setComUserStatusSupport(self.read_optional_value(ctr_tag, "ComUserStatusSupport"))
            general.setComUserTxConfirmation(self.read_optional_value(ctr_tag, "ComUserTxConfirmation"))
            general.setComUserRxIndication(self.read_optional_value(ctr_tag, "ComUserRxIndication"))
            com.setComGeneral(general)
            self.logger.debug("Read ComGeneral")
