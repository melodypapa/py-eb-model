"""
FrNm XDM Parser Module - Extracts AUTOSAR FrNm configuration from EB Tresos XDM files.

Implements:
    - SWR_FRNM_00001: FrNm module parsing
    - SWR_FRNM_00002: General configuration parsing
    - SWR_FRNM_00003: Channel configuration parsing
"""
import xml.etree.ElementTree as ET
from eb_model.models.core.eb_doc import EBModel
from eb_model.models.fr_stack.frnm_xdm import (
    FrNm, FrNmGeneral, FrNmChannel, FrNmChannelIdentifiers,
    FrNmRxPdu, FrNmTxPdu
)
from eb_model.parser.core.eb_parser import AbstractEbModelParser


class FrNmXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR FrNm (FlexRay Network Management) module configuration.

    Extracts FrNm configuration including general parameters and channel configurations.

    Implements: SWR_FRNM_00001 (FrNm Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the FrNm XDM parser."""
        super().__init__()
        self.frnm = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse FrNm module configuration from XDM element.

        Implements: SWR_FRNM_00001
        """
        if self.get_component_name(element) != "FrNm":
            raise ValueError("Invalid <%s> xdm file" % "FrNm")

        frnm = doc.getFrNm()

        self.read_version(element, frnm)

        self.logger.info("Parse FrNm ARVersion:<%s> SwVersion:<%s>" % (frnm.getArVersion().getVersion(), frnm.getSwVersion().getVersion()))

        self.frnm = frnm

        self.read_frnm_general(element, frnm)
        self.read_frnm_channels(element, frnm)

    def read_frnm_general(self, element: ET.Element, frnm: FrNm):
        """
        Parse FrNm general configuration.

        Implements: SWR_FRNM_00002
        """
        ctr_tag = self.find_ctr_tag(element, "FrNmGeneral")
        if ctr_tag is not None:
            general = FrNmGeneral(frnm, ctr_tag.attrib["name"])
            general.setFrNmDevErrorDetect(self.read_value(ctr_tag, "FrNmDevErrorDetect"))
            general.setFrNmVersionInfoApi(self.read_value(ctr_tag, "FrNmVersionInfoApi"))
            general.setFrNmMainFunctionPeriod(self.read_value(ctr_tag, "FrNmMainFunctionPeriod"))
            frnm.setFrNmGeneral(general)
            self.logger.debug("Read FrNmGeneral")

    def read_frnm_channels(self, element: ET.Element, frnm: FrNm):
        """
        Parse FrNm channel configurations.

        Implements: SWR_FRNM_00003
        """
        config_lst = self.find_ctr_tag_list(element, "FrNmChannelConfig")
        if config_lst:
            for lst_tag in config_lst:
                for ctr_tag in self.find_ctr_tag_list(lst_tag, "FrNmChannel"):
                    channel = FrNmChannel(frnm, ctr_tag.attrib["name"])

                    # Read identifiers
                    id_ctr = self.find_ctr_tag(ctr_tag, "FrNmChannelIdentifiers")
                    if id_ctr is not None:
                        ids = FrNmChannelIdentifiers(channel, id_ctr.attrib["name"])
                        ids.setFrNmChannelId(self.read_value(id_ctr, "FrNmChannelId"))
                        channel.setFrNmChannelIdentifiers(ids)

                    # Read RxPdu
                    rx_pdu_ctr = self.find_ctr_tag(ctr_tag, "FrNmRxPdu")
                    if rx_pdu_ctr is not None:
                        rx_pdu = FrNmRxPdu(channel, rx_pdu_ctr.attrib["name"])
                        rx_pdu.setFrNmRxPduId(self.read_value(rx_pdu_ctr, "FrNmRxPduId"))
                        rx_pdu.setFrNmRxPduRef(self.read_ref_value(rx_pdu_ctr, "FrNmRxPduRef"))
                        channel.setFrNmRxPdu(rx_pdu)

                    # Read TxPdu
                    tx_pdu_ctr = self.find_ctr_tag(ctr_tag, "FrNmTxPdu")
                    if tx_pdu_ctr is not None:
                        tx_pdu = FrNmTxPdu(channel, tx_pdu_ctr.attrib["name"])
                        tx_pdu.setFrNmTxPduId(self.read_value(tx_pdu_ctr, "FrNmTxPduId"))
                        tx_pdu.setFrNmTxPduRef(self.read_ref_value(tx_pdu_ctr, "FrNmTxPduRef"))
                        channel.setFrNmTxPdu(tx_pdu)

                    frnm.addFrNmChannel(channel)
                    self.logger.debug("Read FrNmChannel <%s>" % channel.getName())
