from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class CanIfXdmXlsWriter(ExcelReporter):
    def __init__(self) -> None:
        super().__init__()

    def write_canif_general(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanIfGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "NumberOfCanHwUnits", "MaxCtrl", "MaxTxPdus", "MaxRxPdus", "SupportTTCAN"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getCanIf().getCanIfGeneral() is not None:
            general = doc.getCanIf().getCanIfGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getCanIfDevErrorDetect())
            self.write_cell_center(sheet, row, 3, general.getCanIfPublicNumberOfCanHwUnits())
            self.write_cell_center(sheet, row, 4, general.getCanIfPublicMaxCtrl())
            self.write_cell_center(sheet, row, 5, general.getCanIfPublicMaxTxPdus())
            self.write_cell_center(sheet, row, 6, general.getCanIfPublicMaxRxPdus())
            self.write_bool_cell(sheet, row, 7, general.getCanIfSupportTTCAN())
            row += 1

        self.auto_width(sheet)

    def write_canif_ctrl_cfgs(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanIfCtrlCfg", 1)

        title_row = ["Name", "CtrlId", "WakeupSupport", "CanCtrlRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getCanIf().getCanIfCtrlCfgList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_cell_center(sheet, row, 2, cfg.getCanIfCtrlId())
            self.write_bool_cell(sheet, row, 3, cfg.getCanIfCtrlWakeupSupport())
            if cfg.getCanIfCtrlCanCtrlRef() is not None:
                self.write_cell(sheet, row, 4, cfg.getCanIfCtrlCanCtrlRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write_canif_trcv_cfgs(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanIfTrcvCfg", 2)

        title_row = ["Name", "TrcvId", "WakeupSupport", "CanTrcvRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getCanIf().getCanIfTrcvCfgList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_cell_center(sheet, row, 2, cfg.getCanIfTrcvId())
            self.write_bool_cell(sheet, row, 3, cfg.getCanIfTrcvWakeupSupport())
            if cfg.getCanIfTrcvCanTrcvRef() is not None:
                self.write_cell(sheet, row, 4, cfg.getCanIfTrcvCanTrcvRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write_canif_dispatch_cfg(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanIfDispatchCfg", 3)

        title_row = ["Name", "CtrlBusOffName", "CtrlModeIndicationName"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getCanIf().getCanIfDispatchCfg() is not None:
            cfg = doc.getCanIf().getCanIfDispatchCfg()
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_cell(sheet, row, 2, cfg.getCanIfDispatchUserCtrlBusOffName())
            self.write_cell(sheet, row, 3, cfg.getCanIfDispatchUserCtrlModeIndicationName())
            row += 1

        self.auto_width(sheet)

    def write_canif_buffer_cfgs(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanIfBufferCfg", 4)

        title_row = ["Name", "BufferSize", "HthRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getCanIf().getCanIfBufferCfgList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_cell_center(sheet, row, 2, cfg.getCanIfBufferSize())
            if cfg.getCanIfBufferHthRef() is not None:
                self.write_cell(sheet, row, 3, cfg.getCanIfBufferHthRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write_canif_hrh_cfgs(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanIfHrhCfg", 5)

        title_row = ["Name", "SoftwareFilter", "CanCtrlIdRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getCanIf().getCanIfHrhCfgList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_bool_cell(sheet, row, 2, cfg.getCanIfHrhSoftwareFilter())
            if cfg.getCanIfHrhCanCtrlIdRef() is not None:
                self.write_cell(sheet, row, 3, cfg.getCanIfHrhCanCtrlIdRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write_canif_hth_cfgs(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanIfHthCfg", 6)

        title_row = ["Name", "CanCtrlIdRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getCanIf().getCanIfHthCfgList():
            self.write_cell(sheet, row, 1, cfg.getName())
            if cfg.getCanIfHthCanCtrlIdRef() is not None:
                self.write_cell(sheet, row, 2, cfg.getCanIfHthCanCtrlIdRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write_canif_rx_pdu_cfgs(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanIfRxPduCfg", 7)

        title_row = ["Name", "CanId", "CanIdType", "Dlc", "PduId", "HrhIdRef", "UpperLayerRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getCanIf().getCanIfRxPduCfgList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_cell(sheet, row, 2, hex(cfg.getCanIfRxPduCanId()))
            self.write_cell(sheet, row, 3, cfg.getCanIfRxPduCanIdType())
            self.write_cell_center(sheet, row, 4, cfg.getCanIfRxPduDlc())
            self.write_cell_center(sheet, row, 5, cfg.getCanIfRxPduId())
            if cfg.getCanIfRxPduHrhIdRef() is not None:
                self.write_cell(sheet, row, 6, cfg.getCanIfRxPduHrhIdRef().getShortName())
            if cfg.getCanIfRxPduUpperLayerRef() is not None:
                self.write_cell(sheet, row, 7, cfg.getCanIfRxPduUpperLayerRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write_canif_tx_pdu_cfgs(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanIfTxPduCfg", 8)

        title_row = ["Name", "CanId", "CanIdType", "Dlc", "PduId", "Type", "BufferRef", "HthIdRef", "UpperLayerRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getCanIf().getCanIfTxPduCfgList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_cell(sheet, row, 2, hex(cfg.getCanIfTxPduCanId()))
            self.write_cell(sheet, row, 3, cfg.getCanIfTxPduCanIdType())
            self.write_cell_center(sheet, row, 4, cfg.getCanIfTxPduDlc())
            self.write_cell_center(sheet, row, 5, cfg.getCanIfTxPduId())
            self.write_cell(sheet, row, 6, cfg.getCanIfTxPduType())
            if cfg.getCanIfTxPduBufferRef() is not None:
                self.write_cell(sheet, row, 7, cfg.getCanIfTxPduBufferRef().getShortName())
            if cfg.getCanIfTxPduHthIdRef() is not None:
                self.write_cell(sheet, row, 8, cfg.getCanIfTxPduHthIdRef().getShortName())
            if cfg.getCanIfTxPduUpperLayerRef() is not None:
                self.write_cell(sheet, row, 9, cfg.getCanIfTxPduUpperLayerRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        self.logger.info("Writing <%s>" % filename)

        self.write_canif_general(doc)
        self.write_canif_ctrl_cfgs(doc)
        self.write_canif_trcv_cfgs(doc)
        self.write_canif_dispatch_cfg(doc)
        self.write_canif_buffer_cfgs(doc)
        self.write_canif_hrh_cfgs(doc)
        self.write_canif_hth_cfgs(doc)
        self.write_canif_rx_pdu_cfgs(doc)
        self.write_canif_tx_pdu_cfgs(doc)

        self.save(filename)