"""
SecOC XDM Excel Reporter - Generates Excel reports for SecOC module configuration.

Implements:
    - SWR_SECOC_00003: Excel output generation
"""
from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class SecOCXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR SecOC module configuration.

    Implements: SWR_SECOC_00003 (SecOC Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the SecOC Excel reporter."""
        super().__init__()

    def write_secoc_general(self, doc: EBModel):
        """
        Write SecOC general configuration to Excel sheet.

        Implements: SWR_SECOC_00002 (General Configuration Export)
        """
        sheet = self.wb.create_sheet("SecOCGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "Enabled"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getSecOC().getSecocGeneral() is not None:
            general = doc.getSecOC().getSecocGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getSecocDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getSecocEnabled())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """
        Write SecOC configuration to Excel file.

        Implements: SWR_SECOC_00003 (Excel Output Generation)
        """
        self.logger.info("Writing <%s>" % filename)

        self.write_secoc_general(doc)

        self.save(filename)