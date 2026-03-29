"""
FrTp XDM Parser Module - Extracts AUTOSAR FrTp configuration from EB Tresos XDM files.

Implements:
    - SWR_FRTP_00001: FrTp module parsing
    - SWR_FRTP_00002: General configuration parsing
    - SWR_FRTP_00003: Connection configuration parsing
    - SWR_FRTP_00004: RxSdu/TxSdu configuration parsing
"""
import xml.etree.ElementTree as ET
from eb_model.models.core.eb_doc import EBModel
from eb_model.models.fr_stack.frtp_xdm import (
    FrTp, FrTpGeneral, FrTpConnection, FrTpConnectionControl,
    FrTpRxSdu, FrTpTxSdu, FrTpConnectionLimitConfig
)
from eb_model.parser.core.eb_parser import AbstractEbModelParser


class FrTpXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR FrTp (FlexRay Transport Protocol) module configuration.

    Extracts FrTp configuration including general parameters and connections.

    Implements: SWR_FRTP_00001 (FrTp Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the FrTp XDM parser."""
        super().__init__()
        self.frtp = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse FrTp module configuration from XDM element.

        Implements: SWR_FRTP_00001
        """
        if self.get_component_name(element) != "FrTp":
            raise ValueError("Invalid <%s> xdm file" % "FrTp")

        frtp = doc.getFrTp()

        self.read_version(element, frtp)

        self.logger.info("Parse FrTp ARVersion:<%s> SwVersion:<%s>" % (frtp.getArVersion().getVersion(), frtp.getSwVersion().getVersion()))

        self.frtp = frtp

        self.read_frtp_general(element, frtp)
        self.read_frtp_connection_limit_config(element, frtp)
        self.read_frtp_connections(element, frtp)

    def read_frtp_general(self, element: ET.Element, frtp: FrTp):
        """
        Parse FrTp general configuration.

        Implements: SWR_FRTP_00002
        """
        ctr_tag = self.find_ctr_tag(element, "FrTpGeneral")
        if ctr_tag is not None:
            general = FrTpGeneral(frtp, ctr_tag.attrib["name"])
            general.setFrTpDevErrorDetect(self.read_value(ctr_tag, "FrTpDevErrorDetect"))
            general.setFrTpChanNum(self.read_value(ctr_tag, "FrTpChanNum"))
            general.setFrTpMainFuncCycle(self.read_value(ctr_tag, "FrTpMainFuncCycle"))
            general.setFrTpVersionInfoApi(self.read_value(ctr_tag, "FrTpVersionInfoApi"))
            general.setFrTpTxPduNum(self.read_value(ctr_tag, "FrTpTxPduNum"))
            general.setFrTpRelocatablePbcfgEnable(self.read_optional_value(ctr_tag, "FrTpRelocatablePbcfgEnable"))
            frtp.setFrTpGeneral(general)
            self.logger.debug("Read FrTpGeneral")

    def read_frtp_connection_limit_config(self, element: ET.Element, frtp: FrTp):
        """Parse FrTp connection limit configuration."""
        ctr_tag = self.find_ctr_tag(element, "FrTpConnectionLimitConfig")
        if ctr_tag is not None:
            limit_config = FrTpConnectionLimitConfig(frtp, ctr_tag.attrib["name"])
            limit_config.setFrTpRa(self.read_value(ctr_tag, "FrTpRa"))
            limit_config.setFrTpConnectionLimit(self.read_value(ctr_tag, "FrTpConnectionLimit"))
            limit_config.setFrTpConnectionBufferSize(self.read_value(ctr_tag, "FrTpConnectionBufferSize"))
            frtp.setFrTpConnectionLimitConfig(limit_config)
            self.logger.debug("Read FrTpConnectionLimitConfig")

    def read_frtp_connections(self, element: ET.Element, frtp: FrTp):
        """
        Parse FrTp connection configurations.

        Implements: SWR_FRTP_00003
        """
        multi_lst = self.find_ctr_tag_list(element, "FrTpMultipleConfig")
        if multi_lst:
            for lst_tag in multi_lst:
                for ctr_tag in self.find_ctr_tag_list(lst_tag, "FrTpConnection"):
                    connection = FrTpConnection(frtp, ctr_tag.attrib["name"])

                    # Read connection-level parameters
                    connection.setFrTpBandwidthLimitation(self.read_optional_value(ctr_tag, "FrTpBandwidthLimitation"))
                    connection.setFrTpLa(self.read_value(ctr_tag, "FrTpLa"))
                    connection.setFrTpRa(self.read_value(ctr_tag, "FrTpRa"))
                    connection.setFrTpMultipleReceiverCon(self.read_optional_value(ctr_tag, "FrTpMultipleReceiverCon"))

                    # Read references
                    connection.setFrTpConCtrlRef(self.read_ref_value(ctr_tag, "FrTpConCtrlRef"))
                    connection.setFrTpRxPduPoolRef(self.read_ref_value(ctr_tag, "FrTpRxPduPoolRef"))
                    connection.setFrTpTxPduPoolRef(self.read_ref_value(ctr_tag, "FrTpTxPduPoolRef"))

                    # Read RxSdu
                    self.read_frtp_rx_sdu(ctr_tag, connection)

                    # Read TxSdu
                    self.read_frtp_tx_sdu(ctr_tag, connection)

                    # Read connection control
                    self.read_frtp_connection_control(ctr_tag, connection)

                    frtp.addFrTpConnection(connection)
                    self.logger.debug("Read FrTpConnection <%s>" % connection.getName())

    def read_frtp_rx_sdu(self, conn_ctr: ET.Element, connection: FrTpConnection):
        """
        Parse FrTp RxSdu configuration.

        Implements: SWR_FRTP_00004
        """
        rx_ctr = self.find_ctr_tag(conn_ctr, "FrTpRxSdu")
        if rx_ctr is not None:
            rx_sdu = FrTpRxSdu(connection, rx_ctr.attrib["name"])
            rx_sdu.setFrTpRxSduId(self.read_value(rx_ctr, "FrTpRxSduId"))
            rx_sdu.setFrTpRxSduRef(self.read_ref_value(rx_ctr, "FrTpRxSduRef"))
            connection.setFrTpRxSdu(rx_sdu)

    def read_frtp_tx_sdu(self, conn_ctr: ET.Element, connection: FrTpConnection):
        """Parse FrTp TxSdu configuration."""
        tx_ctr = self.find_ctr_tag(conn_ctr, "FrTpTxSdu")
        if tx_ctr is not None:
            tx_sdu = FrTpTxSdu(connection, tx_ctr.attrib["name"])
            tx_sdu.setFrTpTxSduId(self.read_value(tx_ctr, "FrTpTxSduId"))
            tx_sdu.setFrTpTxSduRef(self.read_ref_value(tx_ctr, "FrTpTxSduRef"))
            connection.setFrTpTxSdu(tx_sdu)

    def read_frtp_connection_control(self, conn_ctr: ET.Element, connection: FrTpConnection):
        """Parse FrTp connection control configuration."""
        control_ctr = self.find_ctr_tag(conn_ctr, "FrTpConnectionControl")
        if control_ctr is not None:
            control = FrTpConnectionControl(connection, control_ctr.attrib["name"])
            control.setFrTpAckType(self.read_value(control_ctr, "FrTpAckType"))
            control.setFrTpMaxAr(self.read_value(control_ctr, "FrTpMaxAr"))
            control.setFrTpMaxAs(self.read_value(control_ctr, "FrTpMaxAs"))
            control.setFrTpMaxBufferSize(self.read_value(control_ctr, "FrTpMaxBufferSize"))
            control.setFrTpMaxFCWait(self.read_value(control_ctr, "FrTpMaxFCWait"))
            control.setFrTpMaxFrIf(self.read_value(control_ctr, "FrTpMaxFrIf"))
            control.setFrTpMaxNbrOfNPduPerCycle(self.read_value(control_ctr, "FrTpMaxNbrOfNPduPerCycle"))
            control.setFrTpMaxRn(self.read_value(control_ctr, "FrTpMaxRn"))
            control.setFrTpSCexp(self.read_value(control_ctr, "FrTpSCexp"))
            control.setFrTpTimeBr(self.read_value(control_ctr, "FrTpTimeBr"))
            control.setFrTpTimeBuffer(self.read_value(control_ctr, "FrTpTimeBuffer"))
            control.setFrTpTimeFrIf(self.read_value(control_ctr, "FrTpTimeFrIf"))
            control.setFrTpTimeoutAr(self.read_value(control_ctr, "FrTpTimeoutAr"))
            control.setFrTpTimeoutAs(self.read_value(control_ctr, "FrTpTimeoutAs"))
            control.setFrTpTimeoutBs(self.read_value(control_ctr, "FrTpTimeoutBs"))
            control.setFrTpTimeoutCr(self.read_value(control_ctr, "FrTpTimeoutCr"))
            control.setFrTpMaxBufReq(self.read_value(control_ctr, "FrTpMaxBufReq"))
            connection.setFrTpConnectionControl(control)
