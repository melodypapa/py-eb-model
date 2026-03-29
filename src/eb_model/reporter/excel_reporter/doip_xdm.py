from ...models.core.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class DoIPXdmXlsWriter(ExcelReporter):
    """Excel reporter for DoIP module configuration."""
    def __init__(self) -> None:
        super().__init__()

    def write_doip_general(self, doc: EBModel):
        """Write DoIP general configuration sheet."""
        sheet = self.wb.create_sheet("DoIPGeneral", 0)

        title_row = [
            "Name", "DevErrorDetect", "VersionInfoApi", "MainFunctionPeriod"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getDoIP().getDoIPGeneral() is not None:
            general = doc.getDoIP().getDoIPGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getDoIPDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getDoIPVersionInfoApi())
            self.write_cell(sheet, row, 4, general.getDoIPMainFunctionPeriod())
            row += 1

        self.auto_width(sheet)

    def write_doip_channels(self, doc: EBModel):
        """Write DoIP channel configurations sheet."""
        sheet = self.wb.create_sheet("DoIPChannel", 1)

        title_row = ["Name"]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getDoIP().getDoIPChannelList():
            self.write_cell(sheet, row, 1, cfg.getName())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """Write DoIP configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_doip_general(doc)
        self.write_doip_channels(doc)

        self.save(filename)
