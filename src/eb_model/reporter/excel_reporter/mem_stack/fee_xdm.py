"""
Fee XDM Excel Reporter - Generates Excel reports for Fee module configuration.

Implements:
    - SWR_REPORTER_00002: Excel output generation
    - SWR_FEE_00010: Fee configuration reporting
"""
from ....models.core.eb_doc import EBModel
from ..core.abstract import ExcelReporter


class FeeXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR Fee module configuration.

    Generates Excel workbook with sheets for general configuration
    and wear-leveling parameters.

    Implements: SWR_FEE_00010 (Fee Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the Fee Excel reporter."""
        super().__init__()

    def write_fee_general(self, doc: EBModel):
        """Write FeeGeneral configuration to Excel sheet."""
        sheet = self.wb.create_sheet("FeeGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "PageSize", "VirtualPageSize", "NumberOfSectors"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getFee().getFeeGeneral() is not None:
            general = doc.getFee().getFeeGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getFeeDevErrorDetect())
            self.write_cell(sheet, row, 3, general.getFeePageSize())
            self.write_cell(sheet, row, 4, general.getFeeVirtualPageSize())
            self.write_cell(sheet, row, 5, general.getFeeNumberOfSectors())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """Write Fee configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_fee_general(doc)

        self.save(filename)