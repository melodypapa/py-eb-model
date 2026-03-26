import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.canif_xdm import (
    CanIf, CanIfGeneral, CanIfCtrlCfg, CanIfTrcvCfg,
    CanIfDispatchCfg, CanIfBufferCfg, CanIfHrhCfg, CanIfHthCfg,
    CanIfRxPduCfg, CanIfTxPduCfg
)
from ..parser.eb_parser import AbstractEbModelParser


class CanIfXdmParser(AbstractEbModelParser):
    def __init__(self) -> None:
        super().__init__()
        self.canif = None

    def parse(self, element: ET.Element, doc: EBModel):
        if self.get_component_name(element) != "CanIf":
            raise ValueError("Invalid <%s> xdm file" % "CanIf")

        canif = doc.getCanIf()

        self.read_version(element, canif)

        self.logger.info("Parse CanIf ARVersion:<%s> SwVersion:<%s>" % (canif.getArVersion().getVersion(), canif.getSwVersion().getVersion()))

        self.canif = canif

        self.read_canif_general(element, canif)
        self.read_canif_ctrl_cfgs(element, canif)
        self.read_canif_trcv_cfgs(element, canif)
        self.read_canif_dispatch_cfg(element, canif)
        self.read_canif_buffer_cfgs(element, canif)
        self.read_canif_hrh_cfgs(element, canif)
        self.read_canif_hth_cfgs(element, canif)
        self.read_canif_rx_pdu_cfgs(element, canif)
        self.read_canif_tx_pdu_cfgs(element, canif)

    def read_canif_general(self, element: ET.Element, canif: CanIf):
        ctr_tag = self.find_ctr_tag(element, "CanIfPublicCfg")
        if ctr_tag is not None:
            general = CanIfGeneral(canif, ctr_tag.attrib["name"])
            general.setCanIfDevErrorDetect(self.read_value(ctr_tag, "CanIfPublicDevErrorDetect"))
            general.setCanIfPublicNumberOfCanHwUnits(self.read_value(ctr_tag, "CanIfPublicNumberOfCanHwUnits"))
            general.setCanIfPublicMaxCtrl(self.read_value(ctr_tag, "CanIfPublicMaxCtrl"))
            general.setCanIfPublicMaxTxPdus(self.read_value(ctr_tag, "CanIfPublicMaxTxPdus"))
            general.setCanIfPublicMaxRxPdus(self.read_value(ctr_tag, "CanIfPublicMaxRxPdus"))
            canif.setCanIfGeneral(general)
            self.logger.debug("Read CanIfGeneral")

            # Read TTCAN support from private config
            private_tag = self.find_ctr_tag(element, "CanIfPrivateCfg")
            if private_tag is not None:
                general.setCanIfSupportTTCAN(self.read_optional_value(private_tag, "CanIfSupportTTCAN"))

    def read_canif_ctrl_cfgs(self, element: ET.Element, canif: CanIf):
        for ctr_tag in self.find_ctr_tag_list(element, "CanIfCtrlCfg"):
            cfg = CanIfCtrlCfg(canif, ctr_tag.attrib["name"])
            cfg.setCanIfCtrlId(self.read_value(ctr_tag, "CanIfCtrlId"))
            cfg.setCanIfCtrlWakeupSupport(self.read_optional_value(ctr_tag, "CanIfCtrlWakeupSupport"))
            cfg.setCanIfCtrlCanCtrlRef(self.read_ref_value(ctr_tag, "CanIfCtrlCanCtrlRef"))
            canif.addCanIfCtrlCfg(cfg)
            self.logger.debug("Read CanIfCtrlCfg <%s>" % cfg.getName())

    def read_canif_trcv_cfgs(self, element: ET.Element, canif: CanIf):
        for ctr_tag in self.find_ctr_tag_list(element, "CanIfTrcvCfg"):
            cfg = CanIfTrcvCfg(canif, ctr_tag.attrib["name"])
            cfg.setCanIfTrcvId(self.read_value(ctr_tag, "CanIfTrcvId"))
            cfg.setCanIfTrcvWakeupSupport(self.read_optional_value(ctr_tag, "CanIfTrcvWakeupSupport"))
            cfg.setCanIfTrcvCanTrcvRef(self.read_ref_value(ctr_tag, "CanIfTrcvCanTrcvRef"))
            canif.addCanIfTrcvCfg(cfg)
            self.logger.debug("Read CanIfTrcvCfg <%s>" % cfg.getName())

    def read_canif_dispatch_cfg(self, element: ET.Element, canif: CanIf):
        ctr_tag = self.find_ctr_tag(element, "CanIfDispatchCfg")
        if ctr_tag is not None:
            cfg = CanIfDispatchCfg(canif, ctr_tag.attrib["name"])
            cfg.setCanIfDispatchUserCtrlBusOffName(self.read_optional_value(ctr_tag, "CanIfDispatchUserCtrlBusOffName"))
            cfg.setCanIfDispatchUserCtrlModeIndicationName(self.read_optional_value(ctr_tag, "CanIfDispatchUserCtrlModeIndicationName"))
            canif.setCanIfDispatchCfg(cfg)
            self.logger.debug("Read CanIfDispatchCfg")

    def read_canif_buffer_cfgs(self, element: ET.Element, canif: CanIf):
        for ctr_tag in self.find_ctr_tag_list(element, "CanIfBufferCfg"):
            cfg = CanIfBufferCfg(canif, ctr_tag.attrib["name"])
            cfg.setCanIfBufferSize(self.read_value(ctr_tag, "CanIfBufferSize"))
            cfg.setCanIfBufferHthRef(self.read_optional_ref_value(ctr_tag, "CanIfBufferHthRef"))
            canif.addCanIfBufferCfg(cfg)
            self.logger.debug("Read CanIfBufferCfg <%s>" % cfg.getName())

    def read_canif_hrh_cfgs(self, element: ET.Element, canif: CanIf):
        for ctr_tag in self.find_ctr_tag_list(element, "CanIfHrhCfg"):
            cfg = CanIfHrhCfg(canif, ctr_tag.attrib["name"])
            cfg.setCanIfHrhSoftwareFilter(self.read_optional_value(ctr_tag, "CanIfHrhSoftwareFilter"))
            cfg.setCanIfHrhCanCtrlIdRef(self.read_ref_value(ctr_tag, "CanIfHrhCanCtrlIdRef"))
            canif.addCanIfHrhCfg(cfg)
            self.logger.debug("Read CanIfHrhCfg <%s>" % cfg.getName())

    def read_canif_hth_cfgs(self, element: ET.Element, canif: CanIf):
        for ctr_tag in self.find_ctr_tag_list(element, "CanIfHthCfg"):
            cfg = CanIfHthCfg(canif, ctr_tag.attrib["name"])
            cfg.setCanIfHthCanCtrlIdRef(self.read_ref_value(ctr_tag, "CanIfHthCanCtrlIdRef"))
            canif.addCanIfHthCfg(cfg)
            self.logger.debug("Read CanIfHthCfg <%s>" % cfg.getName())

    def read_canif_rx_pdu_cfgs(self, element: ET.Element, canif: CanIf):
        for ctr_tag in self.find_ctr_tag_list(element, "CanIfRxPduCfg"):
            cfg = CanIfRxPduCfg(canif, ctr_tag.attrib["name"])
            cfg.setCanIfRxPduCanId(self.read_value(ctr_tag, "CanIfRxPduCanId"))
            cfg.setCanIfRxPduCanIdType(self.read_value(ctr_tag, "CanIfRxPduCanIdType"))
            cfg.setCanIfRxPduDlc(self.read_value(ctr_tag, "CanIfRxPduDlc"))
            cfg.setCanIfRxPduId(self.read_value(ctr_tag, "CanIfRxPduId"))
            cfg.setCanIfRxPduHrhIdRef(self.read_ref_value(ctr_tag, "CanIfRxPduHrhIdRef"))
            cfg.setCanIfRxPduUpperLayerRef(self.read_optional_ref_value(ctr_tag, "CanIfRxPduUpperLayerRef"))
            canif.addCanIfRxPduCfg(cfg)
            self.logger.debug("Read CanIfRxPduCfg <%s>" % cfg.getName())

    def read_canif_tx_pdu_cfgs(self, element: ET.Element, canif: CanIf):
        for ctr_tag in self.find_ctr_tag_list(element, "CanIfTxPduCfg"):
            cfg = CanIfTxPduCfg(canif, ctr_tag.attrib["name"])
            cfg.setCanIfTxPduCanId(self.read_value(ctr_tag, "CanIfTxPduCanId"))
            cfg.setCanIfTxPduCanIdType(self.read_value(ctr_tag, "CanIfTxPduCanIdType"))
            cfg.setCanIfTxPduDlc(self.read_value(ctr_tag, "CanIfTxPduDlc"))
            cfg.setCanIfTxPduId(self.read_value(ctr_tag, "CanIfTxPduId"))
            cfg.setCanIfTxPduType(self.read_value(ctr_tag, "CanIfTxPduType"))
            cfg.setCanIfTxPduBufferRef(self.read_optional_ref_value(ctr_tag, "CanIfTxPduBufferRef"))
            cfg.setCanIfTxPduHthIdRef(self.read_ref_value(ctr_tag, "CanIfTxPduHthIdRef"))
            cfg.setCanIfTxPduUpperLayerRef(self.read_optional_ref_value(ctr_tag, "CanIfTxPduUpperLayerRef"))
            canif.addCanIfTxPduCfg(cfg)
            self.logger.debug("Read CanIfTxPduCfg <%s>" % cfg.getName())
