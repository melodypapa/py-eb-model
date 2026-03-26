"""
FrArTp XDM Parser Module - Extracts AUTOSAR FrArTp configuration from EB Tresos XDM files.

Implements:
    - SWR_FRARTP_00001: FrArTp module parsing
    - SWR_FRARTP_00002: General configuration parsing
    - SWR_FRARTP_00003: Channel configuration parsing
    - SWR_FRARTP_00004: Connection configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.frartp_xdm import (
    FrArTp, FrArTpGeneral, FrArTpChannel, FrArTpConnection,
    FrArTpRxSdu, FrArTpTxSdu, FrArTpPdu
)
from ..parser.eb_parser import AbstractEbModelParser


class FrArTpXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR FrArTp (FlexRay AR Transport Protocol) module configuration.

    Extracts FrArTp configuration including general parameters and channel configurations.

    Implements: SWR_FRARTP_00001 (FrArTp Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the FrArTp XDM parser."""
        super().__init__()
        self.frartp = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse FrArTp module configuration from XDM element.

        Implements: SWR_FRARTP_00001
        """
        if self.get_component_name(element) != "FrArTp":
            raise ValueError("Invalid <%s> xdm file" % "FrArTp")

        frartp = doc.getFrArTp()

        self.read_version(element, frartp)

        self.logger.info("Parse FrArTp ARVersion:<%s> SwVersion:<%s>" % (frartp.getArVersion().getVersion(), frartp.getSwVersion().getVersion()))

        self.frartp = frartp

        self.read_frartp_general(element, frartp)
        self.read_frartp_defensive_programming(element, frartp)
        self.read_frartp_channels(element, frartp)

    def read_frartp_general(self, element: ET.Element, frartp: FrArTp):
        """
        Parse FrArTp general configuration.

        Implements: SWR_FRARTP_00002
        """
        ctr_tag = self.find_ctr_tag(element, "FrArTpGeneral")
        if ctr_tag is not None:
            general = FrArTpGeneral(frartp, ctr_tag.attrib["name"])
            general.setFrArTpDevErrorDetect(self.read_value(ctr_tag, "FrArTpDevErrorDetect"))
            general.setFrArTpHaveAckRt(self.read_optional_value(ctr_tag, "FrArTpHaveAckRt"))
            general.setFrArTpHaveGrpSeg(self.read_optional_value(ctr_tag, "FrArTpHaveGrpSeg"))
            general.setFrArTpHaveLm(self.read_value(ctr_tag, "FrArTpHaveLm"))
            general.setFrArTpHaveTc(self.read_value(ctr_tag, "FrArTpHaveTc"))
            general.setFrArTpMainFuncCycle(self.read_value(ctr_tag, "FrArTpMainFuncCycle"))
            general.setFrArTpVersionInfoApi(self.read_value(ctr_tag, "FrArTpVersionInfoApi"))
            general.setFrArTpRelocatablePbcfgEnable(self.read_value(ctr_tag, "FrArTpRelocatablePbcfgEnable"))
            general.setFrArTpMaxConnections(self.read_value(ctr_tag, "FrArTpMaxConnections"))
            general.setFrArTpMaxActiveConnections(self.read_optional_value(ctr_tag, "FrArTpMaxActiveConnections"))
            general.setFrArTpMaxTxPdus(self.read_optional_value(ctr_tag, "FrArTpMaxTxPdus"))
            general.setSupportLowLevelRouting(self.read_optional_value(ctr_tag, "SupportLowLevelRouting"))
            general.setLowLevelRoutingPraefix(self.read_optional_value(ctr_tag, "LowLevelRoutingPraefix"))
            frartp.setFrArTpGeneral(general)
            self.logger.debug("Read FrArTpGeneral")

    def read_frartp_defensive_programming(self, element: ET.Element, frartp: FrArTp):
        """Parse FrArTp defensive programming configuration."""
        ctr_tag = self.find_ctr_tag(element, "FrArTpDefensiveProgramming")
        if ctr_tag is not None:
            general = frartp.getFrArTpGeneral()
            if general is not None:
                general.setFrArTpDefProgEnabled(self.read_value(ctr_tag, "FrArTpDefProgEnabled"))
                general.setFrArTpPrecondAssertEnabled(self.read_value(ctr_tag, "FrArTpPrecondAssertEnabled"))
                general.setFrArTpPostcondAssertEnabled(self.read_value(ctr_tag, "FrArTpPostcondAssertEnabled"))
                general.setFrArTpStaticAssertEnabled(self.read_value(ctr_tag, "FrArTpStaticAssertEnabled"))
                general.setFrArTpUnreachAssertEnabled(self.read_value(ctr_tag, "FrArTpUnreachAssertEnabled"))
                general.setFrArTpInvariantAssertEnabled(self.read_value(ctr_tag, "FrArTpInvariantAssertEnabled"))
            self.logger.debug("Read FrArTpDefensiveProgramming")

    def read_frartp_channels(self, element: ET.Element, frartp: FrArTp):
        """
        Parse FrArTp channel configurations.

        Implements: SWR_FRARTP_00003
        """
        for ctr_tag in self.find_ctr_tag_list(element, "FrArTpChannel"):
            channel = FrArTpChannel(frartp, ctr_tag.attrib["name"])

            # Read channel-level parameters
            channel.setFrArTpAckType(self.read_optional_value(ctr_tag, "FrArTpAckType"))
            channel.setFrArTpAdrType(self.read_value(ctr_tag, "FrArTpAdrType"))
            channel.setFrArTpConcurrentConnections(self.read_optional_value(ctr_tag, "FrArTpConcurrentConnections"))
            channel.setFrArTpGrpSeg(self.read_optional_value(ctr_tag, "FrArTpGrpSeg"))
            channel.setFrArTpLm(self.read_value(ctr_tag, "FrArTpLm"))
            channel.setFrArTpMaxAr(self.read_optional_value(ctr_tag, "FrArTpMaxAr"))
            channel.setFrArTpMaxAs(self.read_optional_value(ctr_tag, "FrArTpMaxAs"))
            channel.setFrArTpMaxBs(self.read_value(ctr_tag, "FrArTpMaxBs"))
            channel.setFrArTpMaxRn(self.read_optional_value(ctr_tag, "FrArTpMaxRn"))
            channel.setFrArTpMaxWft(self.read_value(ctr_tag, "FrArTpMaxWft"))
            channel.setFrArTpStMin(self.read_value(ctr_tag, "FrArTpStMin"))
            channel.setFrArTpStMinGrpSeg(self.read_optional_value(ctr_tag, "FrArTpStMinGrpSeg"))
            channel.setFrArTpTc(self.read_value(ctr_tag, "FrArTpTc"))
            channel.setFrArTpTimeBr(self.read_value(ctr_tag, "FrArTpTimeBr"))
            channel.setFrArTpTimeCs(self.read_value(ctr_tag, "FrArTpTimeCs"))
            channel.setFrArTpTimeoutAr(self.read_value(ctr_tag, "FrArTpTimeoutAr"))
            channel.setFrArTpTimeoutAs(self.read_value(ctr_tag, "FrArTpTimeoutAs"))
            channel.setFrArTpTimeoutBs(self.read_value(ctr_tag, "FrArTpTimeoutBs"))
            channel.setFrArTpTimeoutCr(self.read_value(ctr_tag, "FrArTpTimeoutCr"))

            # Read connections
            self.read_frartp_connections(ctr_tag, channel)

            # Read Pdus
            self.read_frartp_pdus(ctr_tag, channel)

            frartp.addFrArTpChannel(channel)
            self.logger.debug("Read FrArTpChannel <%s>" % channel.getName())

    def read_frartp_connections(self, channel_ctr: ET.Element, channel: FrArTpChannel):
        """
        Parse FrArTp connection configurations.

        Implements: SWR_FRARTP_00004
        """
        for ctr_tag in self.find_ctr_tag_list(channel_ctr, "FrArTpConnection"):
            connection = FrArTpConnection(channel, ctr_tag.attrib["name"])

            # Read connection-level parameters
            connection.setFrArTpConPrioPdus(self.read_optional_value(ctr_tag, "FrArTpConPrioPdus"))
            connection.setFrArTpLa(self.read_value(ctr_tag, "FrArTpLa"))
            connection.setFrArTpRa(self.read_value(ctr_tag, "FrArTpRa"))
            connection.setFrArTpMultRec(self.read_value(ctr_tag, "FrArTpMultRec"))

            # Read RxSdu
            rx_ctr = self.find_ctr_tag(ctr_tag, "FrArTpRxSdu")
            if rx_ctr is not None:
                rx_sdu = FrArTpRxSdu(connection, rx_ctr.attrib["name"])
                rx_sdu.setFrArTpSduRxId(self.read_value(rx_ctr, "FrArTpSduRxId"))
                rx_sdu.setFrArTpRxSduRef(self.read_ref_value(rx_ctr, "FrArTpRxSduRef"))
                connection.setFrArTpRxSdu(rx_sdu)

            # Read TxSdu
            tx_ctr = self.find_ctr_tag(ctr_tag, "FrArTpTxSdu")
            if tx_ctr is not None:
                tx_sdu = FrArTpTxSdu(connection, tx_ctr.attrib["name"])
                tx_sdu.setFrArTpSduTxId(self.read_value(tx_ctr, "FrArTpSduTxId"))
                tx_sdu.setFrArTpTxSduRef(self.read_ref_value(tx_ctr, "FrArTpTxSduRef"))
                connection.setFrArTpTxSdu(tx_sdu)

            channel.addFrArTpConnection(connection)

    def read_frartp_pdus(self, channel_ctr: ET.Element, channel: FrArTpChannel):
        """Parse FrArTp PDU configurations."""
        for ctr_tag in self.find_ctr_tag_list(channel_ctr, "FrArTpPdu"):
            pdu = FrArTpPdu(channel, ctr_tag.attrib["name"])
            pdu.setFrArTpPduDirection(self.read_value(ctr_tag, "FrArTpPduDirection"))
            pdu.setFrArTpPduId(self.read_value(ctr_tag, "FrArTpPduId"))
            pdu.setFrArTpPduRef(self.read_ref_value(ctr_tag, "FrArTpPduRef"))
            channel.addFrArTpPdu(pdu)