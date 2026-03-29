"""
Dlt XDM Excel Reporter - Generates Excel reports for Dlt module configuration.

Implements:
    - SWR_DLT_00003: Excel output generation
"""
from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class DltXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR Dlt module configuration.

    Implements: SWR_DLT_00003 (Dlt Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the Dlt Excel reporter."""
        super().__init__()

    def write_dlt_general(self, doc: EBModel):
        """
        Write Dlt general configuration to Excel sheet.

        Implements: SWR_DLT_00002 (General Configuration Export)
        """
        sheet = self.wb.create_sheet("DltGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "Enabled"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getDlt().getDltGeneral() is not None:
            general = doc.getDlt().getDltGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getDltDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getDltEnabled())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """
        Write Dlt configuration to Excel file.

        Implements: SWR_DLT_00003 (Excel Output Generation)
        """
        self.logger.info("Writing <%s>" % filename)

        self.write_dlt_general(doc)

        self.save(filename)