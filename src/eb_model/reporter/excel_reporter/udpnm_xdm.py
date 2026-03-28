from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class UdpNmXdmXlsWriter(ExcelReporter):
    """Excel reporter for UdpNm module configuration."""
    def __init__(self) -> None:
        super().__init__()

    def write_udpnm_general(self, doc: EBModel):
        """Write UdpNm general configuration sheet."""
        sheet = self.wb.create_sheet("UdpNmGeneral", 0)

        title_row = [
            "Name", "DevErrorDetect", "VersionInfoApi", "MainFunctionPeriod"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getUdpNm().getUdpNmGeneral() is not None:
            general = doc.getUdpNm().getUdpNmGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getUdpNmDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getUdpNmVersionInfoApi())
            self.write_cell(sheet, row, 4, general.getUdpNmMainFunctionPeriod())
            row += 1

        self.auto_width(sheet)

    def write_udpnm_channels(self, doc: EBModel):
        """Write UdpNm channel configurations sheet."""
        sheet = self.wb.create_sheet("UdpNmChannel", 1)

        title_row = [
            "Name", "ChannelId", "RxPduId", "RxPduRef", "TxPduId", "TxPduRef"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getUdpNm().getUdpNmChannelList():
            self.write_cell(sheet, row, 1, cfg.getName())
            if cfg.getUdpNmChannelIdentifiers() is not None:
                self.write_cell_center(sheet, row, 2, cfg.getUdpNmChannelIdentifiers().getUdpNmChannelId())
            if cfg.getUdpNmRxPdu() is not None:
                self.write_cell_center(sheet, row, 3, cfg.getUdpNmRxPdu().getUdpNmRxPduId())
                if cfg.getUdpNmRxPdu().getUdpNmRxPduRef() is not None:
                    self.write_cell(sheet, row, 4, cfg.getUdpNmRxPdu().getUdpNmRxPduRef().getShortName())
            if cfg.getUdpNmTxPdu() is not None:
                self.write_cell_center(sheet, row, 5, cfg.getUdpNmTxPdu().getUdpNmTxPduId())
                if cfg.getUdpNmTxPdu().getUdpNmTxPduRef() is not None:
                    self.write_cell(sheet, row, 6, cfg.getUdpNmTxPdu().getUdpNmTxPduRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """Write UdpNm configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_udpnm_general(doc)
        self.write_udpnm_channels(doc)

        self.save(filename)
