"""
FiM XDM Excel Reporter - Generates Excel reports for FiM module configuration.

Implements:
    - SWR_FIM_00003: Excel output generation
"""
from eb_model.models.core.eb_doc import EBModel
from eb_model.reporter.excel_reporter.core.abstract import ExcelReporter


class FiMXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR FiM module configuration.

    Implements: SWR_FIM_00003 (FiM Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the FiM Excel reporter."""
        super().__init__()

    def write_fim_general(self, doc: EBModel):
        """
        Write FiM general configuration to Excel sheet.

        Implements: SWR_FIM_00002 (General Configuration Export)
        """
        sheet = self.wb.create_sheet("FiMGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "Enabled"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getFiM().getFimGeneral() is not None:
            general = doc.getFiM().getFimGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getFimDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getFimEnabled())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """
        Write FiM configuration to Excel file.

        Implements: SWR_FIM_00003 (Excel Output Generation)
        """
        self.logger.info("Writing <%s>" % filename)

        self.write_fim_general(doc)

        self.save(filename)
