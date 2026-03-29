"""
Dcm XDM Excel Reporter - Generates Excel reports for Dcm module configuration.

Implements:
    - SWR_DCM_00003: Excel output generation
"""
from eb_model.models.core.eb_doc import EBModel
from eb_model.reporter.excel_reporter.core.abstract import ExcelReporter


class DcmXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR Dcm module configuration.

    Implements: SWR_DCM_00003 (Dcm Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the Dcm Excel reporter."""
        super().__init__()

    def write_dcm_general(self, doc: EBModel):
        """
        Write Dcm general configuration to Excel sheet.

        Implements: SWR_DCM_00002 (General Configuration Export)
        """
        sheet = self.wb.create_sheet("DcmGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "Enabled"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getDcm().getDcmGeneral() is not None:
            general = doc.getDcm().getDcmGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getDcmDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getDcmEnabled())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """
        Write Dcm configuration to Excel file.

        Implements: SWR_DCM_00003 (Excel Output Generation)
        """
        self.logger.info("Writing <%s>" % filename)

        self.write_dcm_general(doc)

        self.save(filename)
