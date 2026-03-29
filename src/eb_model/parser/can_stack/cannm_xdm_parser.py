"""
CanNm XDM Parser Module - Extracts AUTOSAR CanNm configuration from EB Tresos XDM files.

Implements:
    - SWR_CANNM_00001: CanNm module parsing
    - SWR_CANNM_00002: Channel configuration parsing
    - SWR_CANNM_00003: PDU configuration parsing
"""
import xml.etree.ElementTree as ET
from ...models.core.eb_doc import EBModel
from ...models.can_stack.cannm_xdm import (
    CanNm, CanNmGeneral, CanNmGlobalConfig, CanNmChannel,
    CanNmRxPdu, CanNmTxPdu, CanNmPnFilterMaskByte, CanNmPnInfo
)
from ..core.eb_parser import AbstractEbModelParser


class CanNmXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR CanNm (CAN Network Management) module configuration.

    Extracts CanNm configuration including channels and PDUs.

    Implements: SWR_CANNM_00001 (CanNm Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the CanNm XDM parser."""
        super().__init__()
        self.cannm = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse CanNm module configuration from XDM element.

        Implements: SWR_CANNM_00001
        """
        if self.get_component_name(element) != "CanNm":
            raise ValueError("Invalid <%s> xdm file" % "CanNm")

        cannm = doc.getCanNm()

        self.read_version(element, cannm)

        self.logger.info("Parse CanNm ARVersion:<%s> SwVersion:<%s>" % (cannm.getArVersion().getVersion(), cannm.getSwVersion().getVersion()))

        self.cannm = cannm

        self.read_cannm_general(element, cannm)
        self.read_cannm_global_config(element, cannm)
        self.read_cannm_pn_info(element, cannm)

    def read_cannm_general(self, element: ET.Element, cannm: CanNm):
        ctr_tag = self.find_ctr_tag(element, "CanNmGeneral")
        if ctr_tag is not None:
            general = CanNmGeneral(cannm, ctr_tag.attrib["name"])
            general.setCanNmMultiCoreSupport(self.read_value(ctr_tag, "CanNmMultiCoreSupport"))
            general.setCanNmPnSupported(self.read_value(ctr_tag, "CanNmPnSupported"))
            general.setCanNmMaxPn(self.read_optional_value(ctr_tag, "CanNmMaxPn"))
            general.setCanNmDetRuntimeChecks(self.read_optional_value(ctr_tag, "CanNmDetRuntimeChecks"))
            cannm.setCanNmGeneral(general)
            self.logger.debug("Read CanNmGeneral")

    def read_cannm_global_config(self, element: ET.Element, cannm: CanNm):
        ctr_tag = self.find_ctr_tag(element, "CanNmGlobalConfig")
        if ctr_tag is not None:
            global_config = CanNmGlobalConfig(cannm, ctr_tag.attrib["name"])
            global_config.setCanNmDevErrorDetect(self.read_value(ctr_tag, "CanNmDevErrorDetect"))
            global_config.setCanNmPassiveModeEnabled(self.read_optional_value(ctr_tag, "CanNmPassiveModeEnabled"))
            global_config.setCanNmBusLoadReductionEnabled(self.read_optional_value(ctr_tag, "CanNmBusLoadReductionEnabled"))
            global_config.setCanNmRemoteSleepIndEnabled(self.read_optional_value(ctr_tag, "CanNmRemoteSleepIndEnabled"))
            global_config.setCanNmStateChangeIndEnabled(self.read_optional_value(ctr_tag, "CanNmStateChangeIndEnabled"))
            global_config.setCanNmComUserDataSupport(self.read_optional_value(ctr_tag, "CanNmComUserDataSupport"))
            global_config.setCanNmMainFunctionPeriod(self.read_optional_value(ctr_tag, "CanNmMainFunctionPeriod"))
            global_config.setCanNmNumberOfChannels(self.read_value(ctr_tag, "CanNmNumberOfChannels"))
            global_config.setCanNmNodeIdCallback(self.read_optional_value(ctr_tag, "CanNmNodeIdCallback"))
            cannm.setCanNmGlobalConfig(global_config)
            self.logger.debug("Read CanNmGlobalConfig")

            # Read channels
            self.read_cannm_channels(ctr_tag, cannm)

            # Read Rx PDUs
            self.read_cannm_rx_pdus(ctr_tag, cannm)

            # Read Tx PDUs
            self.read_cannm_tx_pdus(ctr_tag, cannm)

    def read_cannm_channels(self, element: ET.Element, cannm: CanNm):
        for ctr_tag in self.find_ctr_tag_list(element, "CanNmChannel"):
            channel = CanNmChannel(cannm, ctr_tag.attrib["name"])
            channel.setCanNmNodeIdEnabled(self.read_optional_value(ctr_tag, "CanNmNodeIdEnabled"))
            channel.setCanNmPnEnabled(self.read_optional_value(ctr_tag, "CanNmPnEnabled"))
            channel.setCanNmMsgCycleTime(self.read_optional_value(ctr_tag, "CanNmMsgCycleTime"))
            channel.setCanNmTimeoutTime(self.read_optional_value(ctr_tag, "CanNmTimeoutTime"))
            channel.setCanNmNetworkHandle(self.read_optional_value(ctr_tag, "CanNmNetworkHandle"))
            channel.setCanNmComMNetworkHandleRef(self.read_optional_ref_value(ctr_tag, "CanNmComMNetworkHandleRef"))
            channel.setCanNmCanNmChannelRef(self.read_ref_value(ctr_tag, "CanNmCanNmChannelRef"))
            cannm.addCanNmChannel(channel)
            self.logger.debug("Read CanNmChannel <%s>" % channel.getName())

    def read_cannm_rx_pdus(self, element: ET.Element, cannm: CanNm):
        for ctr_tag in self.find_ctr_tag_list(element, "CanNmRxPdu"):
            rx_pdu = CanNmRxPdu(cannm, ctr_tag.attrib["name"])
            rx_pdu.setCanNmRxPduId(self.read_value(ctr_tag, "CanNmRxPduId"))
            rx_pdu.setCanNmRxPduRef(self.read_ref_value(ctr_tag, "CanNmRxPduRef"))
            cannm.addCanNmRxPdu(rx_pdu)
            self.logger.debug("Read CanNmRxPdu <%s>" % rx_pdu.getName())

    def read_cannm_tx_pdus(self, element: ET.Element, cannm: CanNm):
        for ctr_tag in self.find_ctr_tag_list(element, "CanNmTxPdu"):
            tx_pdu = CanNmTxPdu(cannm, ctr_tag.attrib["name"])
            tx_pdu.setCanNmTxConfirmationPduId(self.read_optional_value(ctr_tag, "CanNmTxConfirmationPduId"))
            tx_pdu.setCanNmTxPduRef(self.read_ref_value(ctr_tag, "CanNmTxPduRef"))
            cannm.addCanNmTxPdu(tx_pdu)
            self.logger.debug("Read CanNmTxPdu <%s>" % tx_pdu.getName())

    def read_cannm_pn_info(self, element: ET.Element, cannm: CanNm):
        ctr_tag = self.find_ctr_tag(element, "CanNmPnInfo")
        if ctr_tag is not None:
            pn_info = CanNmPnInfo(cannm, ctr_tag.attrib["name"])
            pn_info.setCanNmPnInfoLength(self.read_optional_value(ctr_tag, "CanNmPnInfoLength"))
            pn_info.setCanNmPnInfoOffset(self.read_optional_value(ctr_tag, "CanNmPnInfoOffset"))
            cannm.setCanNmPnInfo(pn_info)

            # Read filter mask bytes
            self.read_cannm_pn_filter_mask_bytes(ctr_tag, pn_info)

            self.logger.debug("Read CanNmPnInfo")

    def read_cannm_pn_filter_mask_bytes(self, element: ET.Element, pn_info: CanNmPnInfo):
        for ctr_tag in self.find_ctr_tag_list(element, "CanNmPnFilterMaskByte"):
            mask_byte = CanNmPnFilterMaskByte(pn_info, ctr_tag.attrib["name"])
            mask_byte.setCanNmPnFilterMaskByteIndex(self.read_value(ctr_tag, "CanNmPnFilterMaskByteIndex"))
            mask_byte.setCanNmPnFilterMaskByteValue(self.read_value(ctr_tag, "CanNmPnFilterMaskByteValue"))
            pn_info.addCanNmPnFilterMaskByte(mask_byte)
            self.logger.debug("Read CanNmPnFilterMaskByte <%s>" % mask_byte.getName())
