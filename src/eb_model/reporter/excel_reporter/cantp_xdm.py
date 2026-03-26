from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class CanTpXdmXlsWriter(ExcelReporter):
    def __init__(self) -> None:
        super().__init__()

    def write_cantp_general(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanTpGeneral", 0)
        title_row = ["Name", "DevErrorDetect", "MainFunctionPeriod", "MaxTxChannels", "MaxRxChannels"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getCanTp().getCanTpGeneral() is not None:
            general = doc.getCanTp().getCanTpGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getCanTpDevErrorDetect())
            self.write_cell(sheet, row, 3, general.getCanTpMainFunctionPeriod())
            self.write_cell_center(sheet, row, 4, general.getCanTpMaxTxChannels())
            self.write_cell_center(sheet, row, 5, general.getCanTpMaxRxChannels())
            row += 1

        self.auto_width(sheet)

    def write_cantp_channels(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanTpChannel", 1)
        title_row = ["Name", "ChannelMode", "STmin"]
        self.write_title_row(sheet, title_row)

        row = 2
        for channel in doc.getCanTp().getCanTpChannelList():
            self.write_cell(sheet, row, 1, channel.getName())
            self.write_cell(sheet, row, 2, channel.getCanTpChannelMode())
            self.write_cell(sheet, row, 3, channel.getCanTpSTmin())
            row += 1

        self.auto_width(sheet)

    def write_cantp_rx_nsdus(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanTpRxNSdu", 2)
        title_row = ["Name", "RxNSduId", "RxNSduRef", "Bs", "STmin"]
        self.write_title_row(sheet, title_row)

        row = 2
        for rx_nsdu in doc.getCanTp().getCanTpRxNSduList():
            self.write_cell(sheet, row, 1, rx_nsdu.getName())
            self.write_cell_center(sheet, row, 2, rx_nsdu.getCanTpRxNSduId())
            if rx_nsdu.getCanTpRxNSduRef() is not None:
                self.write_cell(sheet, row, 3, rx_nsdu.getCanTpRxNSduRef().getShortName())
            self.write_cell_center(sheet, row, 4, rx_nsdu.getCanTpBs())
            self.write_cell(sheet, row, 5, rx_nsdu.getCanTpSTmin())
            row += 1

        self.auto_width(sheet)

    def write_cantp_tx_nsdus(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanTpTxNSdu", 3)
        title_row = ["Name", "TxNSduId", "TxNSduRef", "Tc", "STmin"]
        self.write_title_row(sheet, title_row)

        row = 2
        for tx_nsdu in doc.getCanTp().getCanTpTxNSduList():
            self.write_cell(sheet, row, 1, tx_nsdu.getName())
            self.write_cell_center(sheet, row, 2, tx_nsdu.getCanTpTxNSduId())
            if tx_nsdu.getCanTpTxNSduRef() is not None:
                self.write_cell(sheet, row, 3, tx_nsdu.getCanTpTxNSduRef().getShortName())
            self.write_bool_cell(sheet, row, 4, tx_nsdu.getCanTpTc())
            self.write_cell(sheet, row, 5, tx_nsdu.getCanTpSTmin())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        self.logger.info("Writing <%s>" % filename)

        self.write_cantp_general(doc)
        self.write_cantp_channels(doc)
        self.write_cantp_rx_nsdus(doc)
        self.write_cantp_tx_nsdus(doc)

        self.save(filename)
