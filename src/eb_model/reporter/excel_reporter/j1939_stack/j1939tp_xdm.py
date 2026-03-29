"""
J1939Tp XDM Excel Reporter - Generates Excel reports for J1939Tp module configuration.

Implements:
    - SWR_J1939TP_00003: Excel output generation
    - SWR_J1939TP_00002: General configuration export
"""
from ....models.core.eb_doc import EBModel
from ..core.abstract import ExcelReporter


class J1939TpXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR J1939Tp module configuration.

    Implements: SWR_J1939TP_00003 (J1939Tp Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the J1939Tp Excel reporter."""
        super().__init__()

    def write_j1939tp_general(self, doc: EBModel):
        """
        Write J1939Tp general configuration to Excel sheet.

        Implements: SWR_J1939TP_00002 (General Configuration Export)
        """
        sheet = self.wb.create_sheet("J1939TpGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "Enabled"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getJ1939Tp().getJ1939TpGeneral() is not None:
            general = doc.getJ1939Tp().getJ1939TpGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getJ1939TpDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getJ1939TpEnabled())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """
        Write J1939Tp configuration to Excel file.

        Implements: SWR_J1939TP_00003 (Excel Output Generation)
        """
        self.logger.info("Writing <%s>" % filename)

        self.write_j1939tp_general(doc)

        self.save(filename)