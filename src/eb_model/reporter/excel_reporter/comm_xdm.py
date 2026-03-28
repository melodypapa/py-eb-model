"""
ComM XDM Excel Reporter - Generates Excel reports for ComM module configuration.

Implements:
    - SWR_REPORTER_00002: Excel output generation
    - SWR_COMM_00003: ComM configuration reporting
"""
from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class ComMXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR ComM module configuration.

    Generates Excel workbook with sheet for channel configurations.

    Implements: SWR_COMM_00003 (ComM Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the ComM Excel reporter."""
        super().__init__()

    def write(self, filename, doc: EBModel, options=None):
        """Write ComM configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_comm_channels(doc)
        self.save(filename)

    def write_comm_channels(self, doc: EBModel):
        """Write ComM channel configuration to Excel sheet."""
        sheet = self.wb.create_sheet("ComMChannel", 0)

        title_row = ["Name", "ChannelName", "ChannelId"]
        self.write_title_row(sheet, title_row)

        row = 2
        for channel in doc.getComM().getComMChannelList():
            self.write_cell(sheet, row, 1, channel.getName())
            self.write_cell(sheet, row, 2, channel.getComMChannelName())
            self.write_cell_center(sheet, row, 3, channel.getComMChannelId())
            row += 1
            self.logger.debug("Write ComMChannel <%s>" % channel.getName())

        self.auto_width(sheet)