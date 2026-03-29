"""
CryIf XDM Excel Reporter - Generates Excel reports for CryIf module configuration.

Implements:
    - SWR_CRYIF_00003: Excel output generation
"""
from ....models.core.eb_doc import EBModel
from ..core.abstract import ExcelReporter


class CryIfXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR CryIf module configuration.

    Implements: SWR_CRYIF_00003 (CryIf Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the CryIf Excel reporter."""
        super().__init__()

    def write_cryif_general(self, doc: EBModel):
        """
        Write CryIf general configuration to Excel sheet.

        Implements: SWR_CRYIF_00002 (General Configuration Export)
        """
        sheet = self.wb.create_sheet("CryIfGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "Enabled"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getCryIf().getCryIfGeneral() is not None:
            general = doc.getCryIf().getCryIfGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getCryIfDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getCryIfEnabled())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """
        Write CryIf configuration to Excel file.

        Implements: SWR_CRYIF_00003 (Excel Output Generation)
        """
        self.logger.info("Writing <%s>" % filename)

        self.write_cryif_general(doc)

        self.save(filename)