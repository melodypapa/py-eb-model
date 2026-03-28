from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class FrArTpXdmXlsWriter(ExcelReporter):
    """Excel reporter for FrArTp module configuration."""
    def __init__(self) -> None:
        super().__init__()

    def write_frartp_general(self, doc: EBModel):
        """Write FrArTp general configuration sheet."""
        sheet = self.wb.create_sheet("FrArTpGeneral", 0)

        title_row = [
            "Name", "DevErrorDetect", "HaveAckRt", "HaveGrpSeg",
            "HaveLm", "HaveTc", "MainFuncCycle", "VersionInfoApi",
            "RelocatablePbcfgEnable", "MaxConnections", "MaxActiveConnections",
            "MaxTxPdus", "SupportLowLevelRouting", "LowLevelRoutingPraefix"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getFrArTp().getFrArTpGeneral() is not None:
            general = doc.getFrArTp().getFrArTpGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getFrArTpDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getFrArTpHaveAckRt())
            self.write_bool_cell(sheet, row, 4, general.getFrArTpHaveGrpSeg())
            self.write_bool_cell(sheet, row, 5, general.getFrArTpHaveLm())
            self.write_bool_cell(sheet, row, 6, general.getFrArTpHaveTc())
            self.write_cell(sheet, row, 7, general.getFrArTpMainFuncCycle())
            self.write_bool_cell(sheet, row, 8, general.getFrArTpVersionInfoApi())
            self.write_bool_cell(sheet, row, 9, general.getFrArTpRelocatablePbcfgEnable())
            self.write_cell_center(sheet, row, 10, general.getFrArTpMaxConnections())
            self.write_cell_center(sheet, row, 11, general.getFrArTpMaxActiveConnections())
            self.write_cell_center(sheet, row, 12, general.getFrArTpMaxTxPdus())
            self.write_bool_cell(sheet, row, 13, general.getSupportLowLevelRouting())
            self.write_cell(sheet, row, 14, general.getLowLevelRoutingPraefix())
            row += 1

        self.auto_width(sheet)

    def write_frartp_channels(self, doc: EBModel):
        """Write FrArTp channel configurations sheet."""
        sheet = self.wb.create_sheet("FrArTpChannel", 1)

        title_row = [
            "Name", "AckType", "AdrType", "ConcurrentConnections",
            "GrpSeg", "Lm", "MaxAr", "MaxAs", "MaxBs", "MaxRn",
            "MaxWft", "StMin", "StMinGrpSeg", "Tc", "TimeBr",
            "TimeCs", "TimeoutAr", "TimeoutAs", "TimeoutBs", "TimeoutCr"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getFrArTp().getFrArTpChannelList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_cell(sheet, row, 2, cfg.getFrArTpAckType())
            self.write_cell(sheet, row, 3, cfg.getFrArTpAdrType())
            self.write_cell_center(sheet, row, 4, cfg.getFrArTpConcurrentConnections())
            self.write_bool_cell(sheet, row, 5, cfg.getFrArTpGrpSeg())
            self.write_cell(sheet, row, 6, cfg.getFrArTpLm())
            self.write_cell_center(sheet, row, 7, cfg.getFrArTpMaxAr())
            self.write_cell_center(sheet, row, 8, cfg.getFrArTpMaxAs())
            self.write_cell_center(sheet, row, 9, cfg.getFrArTpMaxBs())
            self.write_cell_center(sheet, row, 10, cfg.getFrArTpMaxRn())
            self.write_cell_center(sheet, row, 11, cfg.getFrArTpMaxWft())
            self.write_cell(sheet, row, 12, cfg.getFrArTpStMin())
            self.write_cell(sheet, row, 13, cfg.getFrArTpStMinGrpSeg())
            self.write_bool_cell(sheet, row, 14, cfg.getFrArTpTc())
            self.write_cell(sheet, row, 15, cfg.getFrArTpTimeBr())
            self.write_cell(sheet, row, 16, cfg.getFrArTpTimeCs())
            self.write_cell(sheet, row, 17, cfg.getFrArTpTimeoutAr())
            self.write_cell(sheet, row, 18, cfg.getFrArTpTimeoutAs())
            self.write_cell(sheet, row, 19, cfg.getFrArTpTimeoutBs())
            self.write_cell(sheet, row, 20, cfg.getFrArTpTimeoutCr())
            row += 1

        self.auto_width(sheet)

    def write_frartp_pdus(self, doc: EBModel):
        """Write FrArTp PDU configurations sheet."""
        sheet = self.wb.create_sheet("FrArTpPdu", 2)

        title_row = ["Name", "PduDirection", "PduId", "PduRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for channel in doc.getFrArTp().getFrArTpChannelList():
            for pdu in channel.getFrArTpPduList():
                self.write_cell(sheet, row, 1, pdu.getName())
                self.write_cell(sheet, row, 2, pdu.getFrArTpPduDirection())
                self.write_cell_center(sheet, row, 3, pdu.getFrArTpPduId())
                if pdu.getFrArTpPduRef() is not None:
                    self.write_cell(sheet, row, 4, pdu.getFrArTpPduRef().getShortName())
                row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """Write FrArTp configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_frartp_general(doc)
        self.write_frartp_channels(doc)
        self.write_frartp_pdus(doc)

        self.save(filename)
