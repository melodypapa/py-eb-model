"""
Crypto XDM Excel Reporter - Generates Excel reports for Crypto module configuration.

Implements:
    - SWR_CRYPTO_00003: Excel output generation
"""
from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class CryptoXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR Crypto module configuration.

    Implements: SWR_CRYPTO_00003 (Crypto Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the Crypto Excel reporter."""
        super().__init__()

    def write_crypto_general(self, doc: EBModel):
        """
        Write Crypto general configuration to Excel sheet.

        Implements: SWR_CRYPTO_00002 (General Configuration Export)
        """
        sheet = self.wb.create_sheet("CryptoGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "Enabled"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getCrypto().getCryptoGeneral() is not None:
            general = doc.getCrypto().getCryptoGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getCryptoDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getCryptoEnabled())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """
        Write Crypto configuration to Excel file.

        Implements: SWR_CRYPTO_00003 (Excel Output Generation)
        """
        self.logger.info("Writing <%s>" % filename)

        self.write_crypto_general(doc)

        self.save(filename)