"""
J1939Dcm XDM Excel Reporter - Generates Excel reports for J1939Dcm module configuration.

Implements:
    - SWR_J1939DCM_00003: Excel output generation
    - SWR_J1939DCM_00002: General configuration export
"""
from ....models.core.eb_doc import EBModel
from ..core.abstract import ExcelReporter


class J1939DcmXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR J1939Dcm module configuration.

    Implements: SWR_J1939DCM_00003 (J1939Dcm Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the J1939Dcm Excel reporter."""
        super().__init__()

    def write_j1939dcm_general(self, doc: EBModel):
        """
        Write J1939Dcm general configuration to Excel sheet.

        Implements: SWR_J1939DCM_00002 (General Configuration Export)
        """
        sheet = self.wb.create_sheet("J1939DcmGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "Enabled"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getJ1939Dcm().getJ1939DcmGeneral() is not None:
            general = doc.getJ1939Dcm().getJ1939DcmGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getJ1939DcmDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getJ1939DcmEnabled())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """
        Write J1939Dcm configuration to Excel file.

        Implements: SWR_J1939DCM_00003 (Excel Output Generation)
        """
        self.logger.info("Writing <%s>" % filename)

        self.write_j1939dcm_general(doc)

        self.save(filename)