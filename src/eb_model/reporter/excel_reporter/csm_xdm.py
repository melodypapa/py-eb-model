"""
Csm XDM Excel Reporter - Generates Excel reports for Csm module configuration.

Implements:
    - SWR_CSM_00003: Excel output generation
"""
from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class CsmXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR Csm module configuration.

    Implements: SWR_CSM_00003 (Csm Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the Csm Excel reporter."""
        super().__init__()

    def write_csm_general(self, doc: EBModel):
        """
        Write Csm general configuration to Excel sheet.

        Implements: SWR_CSM_00002 (General Configuration Export)
        """
        sheet = self.wb.create_sheet("CsmGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "Enabled"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getCsm().getCsmGeneral() is not None:
            general = doc.getCsm().getCsmGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getCsmDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getCsmEnabled())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """
        Write Csm configuration to Excel file.

        Implements: SWR_CSM_00003 (Excel Output Generation)
        """
        self.logger.info("Writing <%s>" % filename)

        self.write_csm_general(doc)

        self.save(filename)