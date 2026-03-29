"""
J1939Nm XDM Excel Reporter - Generates Excel reports for J1939Nm module configuration.

Implements:
    - SWR_J1939NM_00003: Excel output generation
    - SWR_J1939NM_00002: General configuration export
"""
from ...models.core.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class J1939NmXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR J1939Nm module configuration.

    Implements: SWR_J1939NM_00003 (J1939Nm Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the J1939Nm Excel reporter."""
        super().__init__()

    def write_j1939nm_general(self, doc: EBModel):
        """
        Write J1939Nm general configuration to Excel sheet.

        Implements: SWR_J1939NM_00002 (General Configuration Export)
        """
        sheet = self.wb.create_sheet("J1939NmGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "Enabled"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getJ1939Nm().getJ1939NmGeneral() is not None:
            general = doc.getJ1939Nm().getJ1939NmGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getJ1939NmDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getJ1939NmEnabled())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """
        Write J1939Nm configuration to Excel file.

        Implements: SWR_J1939NM_00003 (Excel Output Generation)
        """
        self.logger.info("Writing <%s>" % filename)

        self.write_j1939nm_general(doc)

        self.save(filename)