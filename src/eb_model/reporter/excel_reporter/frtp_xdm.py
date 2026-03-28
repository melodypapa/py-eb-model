from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class FrTpXdmXlsWriter(ExcelReporter):
    """Excel reporter for FrTp module configuration."""
    def __init__(self) -> None:
        super().__init__()

    def write_frtp_general(self, doc: EBModel):
        """Write FrTp general configuration sheet."""
        sheet = self.wb.create_sheet("FrTpGeneral", 0)

        title_row = [
            "Name", "DevErrorDetect", "ChanNum", "MainFuncCycle",
            "VersionInfoApi", "TxPduNum", "RelocatablePbcfgEnable"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getFrTp().getFrTpGeneral() is not None:
            general = doc.getFrTp().getFrTpGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getFrTpDevErrorDetect())
            self.write_cell_center(sheet, row, 3, general.getFrTpChanNum())
            self.write_cell(sheet, row, 4, general.getFrTpMainFuncCycle())
            self.write_bool_cell(sheet, row, 5, general.getFrTpVersionInfoApi())
            self.write_cell_center(sheet, row, 6, general.getFrTpTxPduNum())
            self.write_bool_cell(sheet, row, 7, general.getFrTpRelocatablePbcfgEnable())
            row += 1

        self.auto_width(sheet)

    def write_frtp_connection_limit_config(self, doc: EBModel):
        """Write FrTp connection limit configuration sheet."""
        sheet = self.wb.create_sheet("FrTpConnectionLimitConfig", 1)

        title_row = ["Name", "Ra", "ConnectionLimit", "ConnectionBufferSize"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getFrTp().getFrTpConnectionLimitConfig() is not None:
            limit_config = doc.getFrTp().getFrTpConnectionLimitConfig()
            self.write_cell(sheet, row, 1, limit_config.getName())
            self.write_cell_center(sheet, row, 2, limit_config.getFrTpRa())
            self.write_cell_center(sheet, row, 3, limit_config.getFrTpConnectionLimit())
            self.write_cell_center(sheet, row, 4, limit_config.getFrTpConnectionBufferSize())
            row += 1

        self.auto_width(sheet)

    def write_frtp_connections(self, doc: EBModel):
        """Write FrTp connection configurations sheet."""
        sheet = self.wb.create_sheet("FrTpConnection", 2)

        title_row = [
            "Name", "BandwidthLimitation", "La", "Ra", "MultipleReceiverCon",
            "ConCtrlRef", "RxPduPoolRef", "TxPduPoolRef",
            "RxSduId", "RxSduRef", "TxSduId", "TxSduRef"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getFrTp().getFrTpConnectionList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_bool_cell(sheet, row, 2, cfg.getFrTpBandwidthLimitation())
            self.write_cell_center(sheet, row, 3, cfg.getFrTpLa())
            self.write_cell_center(sheet, row, 4, cfg.getFrTpRa())
            self.write_bool_cell(sheet, row, 5, cfg.getFrTpMultipleReceiverCon())
            if cfg.getFrTpConCtrlRef() is not None:
                self.write_cell(sheet, row, 6, cfg.getFrTpConCtrlRef().getShortName())
            if cfg.getFrTpRxPduPoolRef() is not None:
                self.write_cell(sheet, row, 7, cfg.getFrTpRxPduPoolRef().getShortName())
            if cfg.getFrTpTxPduPoolRef() is not None:
                self.write_cell(sheet, row, 8, cfg.getFrTpTxPduPoolRef().getShortName())
            if cfg.getFrTpRxSdu() is not None:
                self.write_cell_center(sheet, row, 9, cfg.getFrTpRxSdu().getFrTpRxSduId())
                if cfg.getFrTpRxSdu().getFrTpRxSduRef() is not None:
                    self.write_cell(sheet, row, 10, cfg.getFrTpRxSdu().getFrTpRxSduRef().getShortName())
            if cfg.getFrTpTxSdu() is not None:
                self.write_cell_center(sheet, row, 11, cfg.getFrTpTxSdu().getFrTpTxSduId())
                if cfg.getFrTpTxSdu().getFrTpTxSduRef() is not None:
                    self.write_cell(sheet, row, 12, cfg.getFrTpTxSdu().getFrTpTxSduRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """Write FrTp configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_frtp_general(doc)
        self.write_frtp_connection_limit_config(doc)
        self.write_frtp_connections(doc)

        self.save(filename)
