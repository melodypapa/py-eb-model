from ....models.core.eb_doc import EBModel
from ..core.abstract import ExcelReporter


class LinTpXdmXlsWriter(ExcelReporter):
    def __init__(self) -> None:
        super().__init__()

    def write_lintp_general(self, doc: EBModel):
        sheet = self.wb.create_sheet("LinTpGeneral", 0)
        title_row = ["Name", "MaxNumberOfRespPendingFrames", "NumberOfRxNSdu", "NumberOfTxNSdu"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getLinTp().getLinTpGeneral() is not None:
            general = doc.getLinTp().getLinTpGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_cell_center(sheet, row, 2, general.getLinTpMaxNumberOfRespPendingFrames())
            self.write_cell_center(sheet, row, 3, general.getLinTpNumberOfRxNSdu())
            self.write_cell_center(sheet, row, 4, general.getLinTpNumberOfTxNSdu())
            row += 1

        self.auto_width(sheet)

    def write_lintp_rx_nsdus(self, doc: EBModel):
        sheet = self.wb.create_sheet("LinTpRxNSdu", 1)
        title_row = ["Name", "RxNSduId", "RxNSduRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for rx_nsdu in doc.getLinTp().getLinTpRxNSduList():
            self.write_cell(sheet, row, 1, rx_nsdu.getName())
            self.write_cell_center(sheet, row, 2, rx_nsdu.getLinTpRxNSduId())
            if rx_nsdu.getLinTpRxNSduRef() is not None:
                self.write_cell(sheet, row, 3, rx_nsdu.getLinTpRxNSduRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write_lintp_tx_nsdus(self, doc: EBModel):
        sheet = self.wb.create_sheet("LinTpTxNSdu", 2)
        title_row = ["Name", "TxNSduId", "TxNSduRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for tx_nsdu in doc.getLinTp().getLinTpTxNSduList():
            self.write_cell(sheet, row, 1, tx_nsdu.getName())
            self.write_cell_center(sheet, row, 2, tx_nsdu.getLinTpTxNSduId())
            if tx_nsdu.getLinTpTxNSduRef() is not None:
                self.write_cell(sheet, row, 3, tx_nsdu.getLinTpTxNSduRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        self.logger.info("Writing <%s>" % filename)

        self.write_lintp_general(doc)
        self.write_lintp_rx_nsdus(doc)
        self.write_lintp_tx_nsdus(doc)

        self.save(filename)
