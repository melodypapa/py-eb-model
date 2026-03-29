"""
Nm XDM Parser Module - Extracts AUTOSAR Nm configuration from EB Tresos XDM files.

Implements:
    - SWR_NM_00001: Nm module parsing
    - SWR_NM_00002: Nm channel configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.core.eb_doc import EBModel
from ..models.com_stack.nm_xdm import Nm, NmChannel
from ..parser.eb_parser import AbstractEbModelParser


class NmXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR Nm (Network Management) module configuration.

    Extracts Nm configuration including channel definitions.

    Implements: SWR_NM_00001 (Nm Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the Nm XDM parser."""
        super().__init__()
        self.nm = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse Nm module configuration from XDM element.

        Implements: SWR_NM_00001
        """
        if self.get_component_name(element) != "Nm":
            raise ValueError("Invalid <%s> xdm file" % "Nm")

        nm = doc.getNm()

        self.read_version(element, nm)

        self.logger.info("Parse Nm ARVersion:<%s> SwVersion:<%s>" % (nm.getArVersion().getVersion(), nm.getSwVersion().getVersion()))

        self.nm = nm

        self.read_nm_channels(element, nm)

    def read_nm_channels(self, element: ET.Element, nm: Nm):
        """
        Parse Nm channel configuration.

        Implements: SWR_NM_00002 (Nm channel configuration parsing)
        """
        for ctr_tag in self.find_ctr_tag_list(element, "NmChannel"):
            channel = NmChannel(nm, ctr_tag.attrib["name"])
            channel.setNmChannelId(self.read_value(ctr_tag, "NmChannelId"))
            channel.setNmBusType(self.read_value(ctr_tag, "NmBusType"))
            channel.setNmMsgCycleTime(self.read_optional_value(ctr_tag, "NmMsgCycleTime"))
            channel.setNmTimeoutTime(self.read_optional_value(ctr_tag, "NmTimeoutTime"))
            channel.setNmNetworkHandle(self.read_optional_value(ctr_tag, "NmNetworkHandle"))
            channel.setNmComMNetworkHandleRef(self.read_optional_ref_value(ctr_tag, "NmComMNetworkHandleRef"))
            channel.setNmNodeEnabled(self.read_optional_value(ctr_tag, "NmNodeEnabled"))
            nm.addNmChannel(channel)
            self.logger.debug("Read NmChannel <%s>" % channel.getName())
