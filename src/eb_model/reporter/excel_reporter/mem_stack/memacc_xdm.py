"""
MemAcc XDM Excel Reporter - Generates Excel reports for MemAcc module configuration.

Implements:
    - SWR_REPORTER_00002: Excel output generation
    - SWR_MEMACC_00010: MemAcc configuration reporting
"""
from ....models.core.eb_doc import EBModel
from ..core.abstract import ExcelReporter


class MemAccXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR MemAcc module configuration.

    Generates Excel workbook with sheets for common configuration
    and protection zone definitions.

    Implements: SWR_MEMACC_00010 (MemAcc Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the MemAcc Excel reporter."""
        super().__init__()

    def write_memacc_common(self, doc: EBModel):
        """Write MemAccCommon configuration to Excel sheet."""
        sheet = self.wb.create_sheet("MemAccCommon", 0)

        title_row = ["Name", "DevErrorDetect", "ProtectionApi", "VirtualProtection"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getMemAcc().getMemAccCommon() is not None:
            common = doc.getMemAcc().getMemAccCommon()
            self.write_cell(sheet, row, 1, common.getName())
            self.write_bool_cell(sheet, row, 2, common.getMemAccDevErrorDetect())
            self.write_cell(sheet, row, 3, common.getMemAccProtectionApi())
            self.write_bool_cell(sheet, row, 4, common.getMemAccVirtualProtection())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """Write MemAcc configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_memacc_common(doc)

        self.save(filename)