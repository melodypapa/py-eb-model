"""
Dem XDM Excel Reporter - Generates Excel reports for Dem module configuration.

Implements:
    - SWR_DEM_00003: Excel output generation
"""
from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class DemXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR Dem module configuration.

    Implements: SWR_DEM_00003 (Dem Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the Dem Excel reporter."""
        super().__init__()

    def write_dem_general(self, doc: EBModel):
        """
        Write Dem general configuration to Excel sheet.

        Implements: SWR_DEM_00002 (General Configuration Export)
        """
        sheet = self.wb.create_sheet("DemGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "Enabled"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getDem().getDemGeneral() is not None:
            general = doc.getDem().getDemGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getDemDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getDemEnabled())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """
        Write Dem configuration to Excel file.

        Implements: SWR_DEM_00003 (Excel Output Generation)
        """
        self.logger.info("Writing <%s>" % filename)

        self.write_dem_general(doc)

        self.save(filename)