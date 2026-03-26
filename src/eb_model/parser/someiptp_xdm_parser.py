"""
SomeIpTp XDM Parser Module - Extracts AUTOSAR SomeIpTp configuration from EB Tresos XDM files.

Implements:
    - SWR_SOMEIPTP_00001: SomeIpTp module parsing
    - SWR_SOMEIPTP_00002: General configuration parsing
    - SWR_SOMEIPTP_00003: Channel configuration parsing
    - SWR_SOMEIPTP_00004: RxNSdu configuration parsing
    - SWR_SOMEIPTP_00005: TxNSdu configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.someiptp_xdm import (
    SomeIpTp, SomeIpTpGeneral, SomeIpTpChannel,
    SomeIpTpRxNSdu, SomeIpTpTxNSdu, SomeIpTpRxNPdu, SomeIpTpTxNPdu
)
from ..parser.eb_parser import AbstractEbModelParser


class SomeIpTpXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR SomeIpTp (SOME/IP Transport Protocol) module configuration.

    Extracts SomeIpTp configuration including general parameters and channel configurations.

    Implements: SWR_SOMEIPTP_00001 (SomeIpTp Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the SomeIpTp XDM parser."""
        super().__init__()
        self.someiptp = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse SomeIpTp module configuration from XDM element.

        Implements: SWR_SOMEIPTP_00001
        """
        if self.get_component_name(element) != "SomeIpTp":
            raise ValueError("Invalid <%s> xdm file" % "SomeIpTp")

        someiptp = doc.getSomeIpTp()

        self.read_version(element, someiptp)

        self.logger.info("Parse SomeIpTp ARVersion:<%s> SwVersion:<%s>" % (someiptp.getArVersion().getVersion(),
                                               someiptp.getSwVersion().getVersion()))

        self.someiptp = someiptp

        self.read_someiptp_general(element, someiptp)
        self.read_someiptp_channels(element, someiptp)

    def read_someiptp_general(self, element: ET.Element, someiptp: SomeIpTp):
        """
        Parse SomeIpTp general configuration.

        Implements: SWR_SOMEIPTP_00002
        """
        ctr_tag = self.find_ctr_tag(element, "SomeIpTpGeneral")
        if ctr_tag is not None:
            general = SomeIpTpGeneral(someiptp, ctr_tag.attrib["name"])
            general.setSomeIpTpDevErrorDetect(self.read_value(ctr_tag, "SomeIpTpDevErrorDetect"))
            general.setSomeIpTpRxMainFunctionPeriod(self.read_value(ctr_tag, "SomeIpTpRxMainFunctionPeriod"))
            general.setSomeIpTpTxMainFunctionPeriod(self.read_value(ctr_tag, "SomeIpTpTxMainFunctionPeriod"))
            general.setSomeIpTpVersionInfoApi(self.read_value(ctr_tag, "SomeIpTpVersionInfoApi"))
            someiptp.setSomeIpTpGeneral(general)
            self.logger.debug("Read SomeIpTpGeneral")

    def read_someiptp_channels(self, element: ET.Element, someiptp: SomeIpTp):
        """
        Parse SomeIpTp channel configurations.

        Implements: SWR_SOMEIPTP_00003
        """
        for ctr_tag in self.find_ctr_tag_list(element, "SomeIpTpChannel"):
            channel = SomeIpTpChannel(someiptp, ctr_tag.attrib["name"])

            # Read channel-level parameters
            channel.setSomeIpTpNPduSeparationTime(self.read_optional_value(ctr_tag, "SomeIpTpNPduSeparationTime"))
            channel.setSomeIpTpRxTimeoutTime(self.read_value(ctr_tag, "SomeIpTpRxTimeoutTime"))
            channel.setSomeIpTpTxConfirmationTimeout(self.read_value(ctr_tag, "SomeIpTpTxConfirmationTimeout"))

            # Read RxNSdu configurations
            self.read_someiptp_rx_nsdus(ctr_tag, channel)

            # Read TxNSdu configurations
            self.read_someiptp_tx_nsdus(ctr_tag, channel)

            someiptp.addSomeIpTpChannel(channel)
            self.logger.debug("Read SomeIpTpChannel <%s>" % channel.getName())

    def read_someiptp_rx_nsdus(self, channel_ctr: ET.Element, channel: SomeIpTpChannel):
        """
        Parse SomeIpTp RxNSdu configurations.

        Implements: SWR_SOMEIPTP_00004
        """
        rx_ctr = self.find_ctr_tag(channel_ctr, "SomeIpTpRxNSdu")
        if rx_ctr is not None:
            rx_nsdu = SomeIpTpRxNSdu(channel, rx_ctr.attrib["name"])

            # Read RxSduRef
            rx_nsdu.setSomeIpTpRxSduRef(self.read_ref_value(rx_ctr, "SomeIpTpRxSduRef"))

            # Read RxNPdu
            rx_npdus_ctr = self.find_ctr_tag(rx_ctr, "SomeIpTpRxNPdu")
            if rx_npdus_ctr is not None:
                rx_npdus = SomeIpTpRxNPdu(rx_nsdu, rx_npdus_ctr.attrib["name"])
                rx_npdus.setSomeIpTpRxNPduHandleId(self.read_value(rx_npdus_ctr, "SomeIpTpRxNPduHandleId"))
                rx_npdus.setSomeIpTpRxNPduRef(self.read_ref_value(rx_npdus_ctr, "SomeIpTpRxNPduRef"))
                rx_nsdu.setSomeIpTpRxNPdu(rx_npdus)

            channel.setSomeIpTpRxNSdu(rx_nsdu)

    def read_someiptp_tx_nsdus(self, channel_ctr: ET.Element, channel: SomeIpTpChannel):
        """
        Parse SomeIpTp TxNSdu configurations.

        Implements: SWR_SOMEIPTP_00005
        """
        tx_ctr = self.find_ctr_tag(channel_ctr, "SomeIpTpTxNSdu")
        if tx_ctr is not None:
            tx_nsdu = SomeIpTpTxNSdu(channel, tx_ctr.attrib["name"])

            # Read TxNSduHandleId
            tx_nsdu.setSomeIpTpTxNSduHandleId(self.read_value(tx_ctr, "SomeIpTpTxNSduHandleId"))

            # Read TxSduRef
            tx_nsdu.setSomeIpTpTxNSduRef(self.read_ref_value(tx_ctr, "SomeIpTpTxNSduRef"))

            # Read TxNPdu
            tx_npdus_ctr = self.find_ctr_tag(tx_ctr, "SomeIpTpTxNPdu")
            if tx_npdus_ctr is not None:
                tx_npdus = SomeIpTpTxNPdu(tx_nsdu, tx_npdus_ctr.attrib["name"])
                tx_npdus.setSomeIpTpTxNPduHandleId(self.read_value(tx_npdus_ctr, "SomeIpTpTxNPduHandleId"))
                tx_npdus.setSomeIpTpTxNPduRef(self.read_ref_value(tx_npdus_ctr, "SomeIpTpTxNPduRef"))
                tx_nsdu.setSomeIpTpTxNPdu(tx_npdus)

            channel.setSomeIpTpTxNSdu(tx_nsdu)