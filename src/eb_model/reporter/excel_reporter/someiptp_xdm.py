from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class SomeIpTpXdmXlsWriter(ExcelReporter):
    """Excel reporter for SomeIpTp module configuration."""
    def __init__(self) -> None:
        super().__init__()

    def write_someiptp_general(self, doc: EBModel):
        """Write SomeIpTp general configuration sheet."""
        sheet = self.wb.create_sheet("SomeIpTpGeneral", 0)

        title_row = [
            "Name", "DevErrorDetect", "RxMainFunctionPeriod",
            "TxMainFunctionPeriod", "VersionInfoApi"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getSomeIpTp().getSomeIpTpGeneral() is not None:
            general = doc.getSomeIpTp().getSomeIpTpGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getSomeIpTpDevErrorDetect())
            self.write_cell(sheet, row, 3, general.getSomeIpTpRxMainFunctionPeriod())
            self.write_cell(sheet, row, 4, general.getSomeIpTpTxMainFunctionPeriod())
            self.write_bool_cell(sheet, row, 5, general.getSomeIpTpVersionInfoApi())
            row += 1

        self.auto_width(sheet)

    def write_someiptp_channels(self, doc: EBModel):
        """Write SomeIpTp channel configurations sheet."""
        sheet = self.wb.create_sheet("SomeIpTpChannel", 1)

        title_row = [
            "Name", "NPduSeparationTime", "RxTimeoutTime", "TxConfirmationTimeout",
            "RxSduRef", "RxNPduHandleId", "RxNPduRef",
            "TxNSduHandleId", "TxSduRef", "TxNPduHandleId", "TxNPduRef"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getSomeIpTp().getSomeIpTpChannelList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_cell(sheet, row, 2, cfg.getSomeIpTpNPduSeparationTime())
            self.write_cell(sheet, row, 3, cfg.getSomeIpTpRxTimeoutTime())
            self.write_cell(sheet, row, 4, cfg.getSomeIpTpTxConfirmationTimeout())

            if cfg.getSomeIpTpRxNSdu() is not None:
                rx_nsdu = cfg.getSomeIpTpRxNSdu()
                if rx_nsdu.getSomeIpTpRxSduRef() is not None:
                    self.write_cell(sheet, row, 5, rx_nsdu.getSomeIpTpRxSduRef().getShortName())
                if rx_nsdu.getSomeIpTpRxNPdu() is not None:
                    rx_npdus = rx_nsdu.getSomeIpTpRxNPdu()
                    self.write_cell_center(sheet, row, 6, rx_npdus.getSomeIpTpRxNPduHandleId())
                    if rx_npdus.getSomeIpTpRxNPduRef() is not None:
                        self.write_cell(sheet, row, 7, rx_npdus.getSomeIpTpRxNPduRef().getShortName())

            if cfg.getSomeIpTpTxNSdu() is not None:
                tx_nsdu = cfg.getSomeIpTpTxNSdu()
                self.write_cell_center(sheet, row, 8, tx_nsdu.getSomeIpTpTxNSduHandleId())
                if tx_nsdu.getSomeIpTpTxNSduRef() is not None:
                    self.write_cell(sheet, row, 9, tx_nsdu.getSomeIpTpTxNSduRef().getShortName())
                if tx_nsdu.getSomeIpTpTxNPdu() is not None:
                    tx_npdus = tx_nsdu.getSomeIpTpTxNPdu()
                    self.write_cell_center(sheet, row, 10, tx_npdus.getSomeIpTpTxNPduHandleId())
                    if tx_npdus.getSomeIpTpTxNPduRef() is not None:
                        self.write_cell(sheet, row, 11, tx_npdus.getSomeIpTpTxNPduRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """Write SomeIpTp configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_someiptp_general(doc)
        self.write_someiptp_channels(doc)

        self.save(filename)
