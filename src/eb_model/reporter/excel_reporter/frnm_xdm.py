from ...models.core.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class FrNmXdmXlsWriter(ExcelReporter):
    """Excel reporter for FrNm module configuration."""
    def __init__(self) -> None:
        super().__init__()

    def write_frnm_general(self, doc: EBModel):
        """Write FrNm general configuration sheet."""
        sheet = self.wb.create_sheet("FrNmGeneral", 0)

        title_row = [
            "Name", "DevErrorDetect", "VersionInfoApi", "MainFunctionPeriod"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getFrNm().getFrNmGeneral() is not None:
            general = doc.getFrNm().getFrNmGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getFrNmDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getFrNmVersionInfoApi())
            self.write_cell(sheet, row, 4, general.getFrNmMainFunctionPeriod())
            row += 1

        self.auto_width(sheet)

    def write_frnm_channels(self, doc: EBModel):
        """Write FrNm channel configurations sheet."""
        sheet = self.wb.create_sheet("FrNmChannel", 1)

        title_row = [
            "Name", "ChannelId", "RxPduId", "RxPduRef", "TxPduId", "TxPduRef"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getFrNm().getFrNmChannelList():
            self.write_cell(sheet, row, 1, cfg.getName())
            if cfg.getFrNmChannelIdentifiers() is not None:
                self.write_cell_center(sheet, row, 2, cfg.getFrNmChannelIdentifiers().getFrNmChannelId())
            if cfg.getFrNmRxPdu() is not None:
                self.write_cell_center(sheet, row, 3, cfg.getFrNmRxPdu().getFrNmRxPduId())
                if cfg.getFrNmRxPdu().getFrNmRxPduRef() is not None:
                    self.write_cell(sheet, row, 4, cfg.getFrNmRxPdu().getFrNmRxPduRef().getShortName())
            if cfg.getFrNmTxPdu() is not None:
                self.write_cell_center(sheet, row, 5, cfg.getFrNmTxPdu().getFrNmTxPduId())
                if cfg.getFrNmTxPdu().getFrNmTxPduRef() is not None:
                    self.write_cell(sheet, row, 6, cfg.getFrNmTxPdu().getFrNmTxPduRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """Write FrNm configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_frnm_general(doc)
        self.write_frnm_channels(doc)

        self.save(filename)
