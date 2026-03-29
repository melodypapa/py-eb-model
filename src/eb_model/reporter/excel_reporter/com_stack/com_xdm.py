"""
Com XDM Excel Reporter - Generates Excel reports for Com module configuration.

Implements:
    - SWR_REPORTER_00002: Excel output generation
    - SWR_COM_00003: Com configuration reporting
"""
from ....models.core.eb_doc import EBModel
from ..core.abstract import ExcelReporter


class ComXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR Com module configuration.

    Generates Excel workbook with sheet for general COM configuration.

    Implements: SWR_COM_00003 (Com Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the Com Excel reporter."""
        super().__init__()

    def write(self, filename, doc: EBModel, options=None):
        """Write Com configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_com_general(doc)
        self.save(filename)

    def write_com_general(self, doc: EBModel):
        """Write ComGeneral configuration to Excel sheet."""
        sheet = self.wb.create_sheet("ComGeneral", 0)

        title_row = ["Name", "EnableUserSupport", "UserInitSignal", "UserStatusSupport", "UserTxConfirmation", "UserRxIndication"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getCom().getComGeneral() is not None:
            general = doc.getCom().getComGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getComEnableUserSupport())
            self.write_bool_cell(sheet, row, 3, general.getComUserInitSignal())
            self.write_bool_cell(sheet, row, 4, general.getComUserStatusSupport())
            self.write_bool_cell(sheet, row, 5, general.getComUserTxConfirmation())
            self.write_bool_cell(sheet, row, 6, general.getComUserRxIndication())
            row += 1
            self.logger.debug("Write ComGeneral <%s>" % general.getName())

        self.auto_width(sheet)
