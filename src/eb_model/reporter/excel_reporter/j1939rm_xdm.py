"""
J1939Rm XDM Excel Reporter - Generates Excel reports for J1939Rm module configuration.

Implements:
    - SWR_J1939RM_00003: Excel output generation
    - SWR_J1939RM_00002: General configuration export
"""
from ...models.core.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class J1939RmXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR J1939Rm module configuration.

    Implements: SWR_J1939RM_00003 (J1939Rm Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the J1939Rm Excel reporter."""
        super().__init__()

    def write_j1939rm_general(self, doc: EBModel):
        """
        Write J1939Rm general configuration to Excel sheet.

        Implements: SWR_J1939RM_00002 (General Configuration Export)
        """
        sheet = self.wb.create_sheet("J1939RmGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "Enabled"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getJ1939Rm().getJ1939RmGeneral() is not None:
            general = doc.getJ1939Rm().getJ1939RmGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getJ1939RmDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getJ1939RmEnabled())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """
        Write J1939Rm configuration to Excel file.

        Implements: SWR_J1939RM_00003 (Excel Output Generation)
        """
        self.logger.info("Writing <%s>" % filename)

        self.write_j1939rm_general(doc)

        self.save(filename)