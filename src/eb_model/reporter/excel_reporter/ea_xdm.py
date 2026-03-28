"""
Ea XDM Excel Reporter - Generates Excel reports for Ea module configuration.

Implements:
    - SWR_REPORTER_00002: Excel output generation
    - SWR_EA_00010: Ea configuration reporting
"""
from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class EaXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR Ea module configuration.

    Generates Excel workbook with sheets for general configuration
    and device-specific parameters.

    Implements: SWR_EA_00010 (Ea Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the Ea Excel reporter."""
        super().__init__()

    def write_ea_general(self, doc: EBModel):
        """Write EaGeneral configuration to Excel sheet."""
        sheet = self.wb.create_sheet("EaGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "PageSize", "AddressAlignment", "ReadMode"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getEa().getEaGeneral() is not None:
            general = doc.getEa().getEaGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getEaDevErrorDetect())
            self.write_cell(sheet, row, 3, general.getEaPageSize())
            self.write_cell(sheet, row, 4, general.getEaAddressAlignment())
            self.write_cell(sheet, row, 5, general.getEaReadMode())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """Write Ea configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_ea_general(doc)

        self.save(filename)