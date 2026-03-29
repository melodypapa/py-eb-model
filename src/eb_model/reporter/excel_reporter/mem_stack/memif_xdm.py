"""
MemIf XDM Excel Reporter - Generates Excel reports for MemIf module configuration.

Implements:
    - SWR_REPORTER_00002: Excel output generation
    - SWR_MEMIF_00010: MemIf configuration reporting
"""
from eb_model.models.core.eb_doc import EBModel
from eb_model.reporter.excel_reporter.core.abstract import ExcelReporter


class MemIfXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR MemIf module configuration.

    Generates Excel workbook with sheets for initialization
    configuration and device abstraction parameters.

    Implements: SWR_MEMIF_00010 (MemIf Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the MemIf Excel reporter."""
        super().__init__()

    def write_memif_init(self, doc: EBModel):
        """Write MemIfInit configuration to Excel sheet."""
        sheet = self.wb.create_sheet("MemIfInit", 0)

        title_row = ["Name", "DevErrorDetect", "Index", "JobPriority", "MaxNumberJobs"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getMemIf().getMemIfInit() is not None:
            init = doc.getMemIf().getMemIfInit()
            self.write_cell(sheet, row, 1, init.getName())
            self.write_bool_cell(sheet, row, 2, init.getMemIfDevErrorDetect())
            self.write_cell(sheet, row, 3, init.getMemIfIndex())
            self.write_cell(sheet, row, 4, init.getMemIfJobPriority())
            self.write_cell(sheet, row, 5, init.getMemIfMaxNumberJobs())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """Write MemIf configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_memif_init(doc)

        self.save(filename)
