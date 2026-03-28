"""
LdCom XDM Excel Reporter - Generates Excel reports for LdCom module configuration.

Implements:
    - SWR_REPORTER_00002: Excel output generation
    - SWR_LDCOM_00002: LdCom configuration reporting
"""
from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class LdComXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR LdCom module configuration.

    Generates Excel workbook for LdCom module.

    Implements: SWR_LDCOM_00002 (LdCom Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the LdCom Excel reporter."""
        super().__init__()

    def write(self, filename, doc: EBModel, options=None):
        """Write LdCom configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_ldcom_general(doc)
        self.save(filename)

    def write_ldcom_general(self, doc: EBModel):
        """Write LdCom general configuration to Excel sheet."""
        sheet = self.wb.create_sheet("LdComGeneral", 0)

        title_row = ["Name"]
        self.write_title_row(sheet, title_row)

        row = 2
        ldcom = doc.getLdCom()
        self.write_cell(sheet, row, 1, ldcom.getName())
        row += 1
        self.logger.debug("Write LdCom <%s>" % ldcom.getName())

        self.auto_width(sheet)
