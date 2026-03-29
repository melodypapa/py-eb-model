"""
Crc XDM Excel Reporter - Generates Excel reports for Crc module configuration.

Implements:
    - SWR_REPORTER_00002: Excel output generation
    - SWR_CRC_00003: Crc configuration reporting
"""
from ....models.core.eb_doc import EBModel
from ..core.abstract import ExcelReporter


class CrcXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR Crc module configuration.

    Generates Excel workbook with sheet for CRC configurations.

    Implements: SWR_CRC_00003 (Crc Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the Crc Excel reporter."""
        super().__init__()

    def write(self, filename, doc: EBModel, options=None):
        """Write Crc configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_crc_config(doc)
        self.save(filename)

    def write_crc_config(self, doc: EBModel):
        """Write Crc configuration to Excel sheet."""
        sheet = self.wb.create_sheet("CrcConfig", 0)

        title_row = ["Name", "CrcId", "CRCType"]
        self.write_title_row(sheet, title_row)

        row = 2
        for config in doc.getCrc().getCrcConfigList():
            self.write_cell(sheet, row, 1, config.getName())
            self.write_cell_center(sheet, row, 2, config.getCrcId())
            self.write_cell(sheet, row, 3, config.getCrcCRCType())
            row += 1
            self.logger.debug("Write CrcConfig <%s>" % config.getName())

        self.auto_width(sheet)
