"""
LdCom XDM Parser Module - Extracts AUTOSAR LdCom configuration from EB Tresos XDM files.

Implements:
    - SWR_LDCOM_00001: LdCom module parsing
"""
import xml.etree.ElementTree as ET
from ...models.core.eb_doc import EBModel
from ...models.com_stack.ldcom_xdm import LdCom
from ..core.eb_parser import AbstractEbModelParser


class LdComXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR LdCom (Local Data Communication) module configuration.

    Extracts LdCom configuration from EB Tresos XDM files.

    Implements: SWR_LDCOM_00001 (LdCom Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the LdCom XDM parser."""
        super().__init__()

        self.ldcom = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse LdCom module configuration from XDM element.

        Implements: SWR_LDCOM_00001
        """
        if self.get_component_name(element) != "LdCom":
            raise ValueError("Invalid <%s> xdm file" % "LdCom")

        ldcom = doc.getLdCom()

        self.read_version(element, ldcom)

        self.logger.info("Parse LdCom ARVersion:<%s> SwVersion:<%s>" % (ldcom.getArVersion().getVersion(), ldcom.getSwVersion().getVersion()))

        self.ldcom = ldcom
