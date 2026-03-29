"""
ComM XDM Parser Module - Extracts AUTOSAR ComM configuration from EB Tresos XDM files.

Implements:
    - SWR_COMM_00001: ComM module parsing
    - SWR_COMM_00002: ComM channel configuration parsing
"""
import xml.etree.ElementTree as ET
from ...models.core.eb_doc import EBModel
from ...models.com_stack.comm_xdm import ComM, ComMChannel
from ..core.eb_parser import AbstractEbModelParser


class ComMXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR ComM (Communication Manager) module configuration.

    Extracts ComM communication channel configuration.

    Implements: SWR_COMM_00001 (ComM Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the ComM XDM parser."""
        super().__init__()
        self.comm = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse ComM module configuration from XDM element.

        Implements: SWR_COMM_00001
        """
        if self.get_component_name(element) != "ComM":
            raise ValueError("Invalid <%s> xdm file" % "ComM")

        comm = doc.getComM()

        self.read_version(element, comm)

        self.logger.info("Parse ComM ARVersion:<%s> SwVersion:<%s>" % (comm.getArVersion().getVersion(), comm.getSwVersion().getVersion()))

        self.comm = comm

        self.read_comm_channels(element, comm)

    def read_comm_channels(self, element: ET.Element, comm: ComM):
        """
        Parse ComM channel configuration.

        Implements: SWR_COMM_00002 (ComM channel configuration parsing)
        """
        for ctr_tag in self.find_ctr_tag_list(element, "ComMChannel"):
            cfg = ComMChannel(comm, ctr_tag.attrib["name"])
            cfg.setComMChannelName(self.read_value(ctr_tag, "ComMChannelName"))
            cfg.setComMChannelId(self.read_value(ctr_tag, "ComMChannelId"))
            comm.addComMChannel(cfg)
            self.logger.debug("Read ComMChannel <%s>" % cfg.getName())
