"""
MemMap XDM Excel Reporter - Generates Excel reports for MemMap module configuration.

Implements:
    - SWR_REPORTER_00002: Excel output generation
    - SWR_MEMMAP_00010: MemMap configuration reporting
"""
from ....models.core.eb_doc import EBModel
from ..core.abstract import ExcelReporter


class MemMapXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR MemMap module configuration.

    Generates Excel workbook with sheets for common configuration
    and memory section definitions.

    Implements: SWR_MEMMAP_00010 (MemMap Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the MemMap Excel reporter."""
        super().__init__()

    def write_memmap_common(self, doc: EBModel):
        """Write MemMapCommon configuration to Excel sheet."""
        sheet = self.wb.create_sheet("MemMapCommon", 0)

        title_row = ["Name", "DevErrorDetect", "Api", "InitStatus"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getMemMap().getMemMapCommon() is not None:
            common = doc.getMemMap().getMemMapCommon()
            self.write_cell(sheet, row, 1, common.getName())
            self.write_bool_cell(sheet, row, 2, common.getMemMapDevErrorDetect())
            self.write_cell(sheet, row, 3, common.getMemMapApi())
            self.write_cell(sheet, row, 4, common.getMemMapInitStatus())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """Write MemMap configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_memmap_common(doc)

        self.save(filename)