"""
PduR XDM Excel Reporter - Generates Excel reports for PduR module configuration.

Implements:
    - SWR_REPORTER_00002: Excel output generation
    - SWR_PDUR_00003: PduR configuration reporting
"""
from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class PduRXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR PduR module configuration.

    Generates Excel workbook with sheet for routing table entries.

    Implements: SWR_PDUR_00003 (PduR Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the PduR Excel reporter."""
        super().__init__()

    def write(self, filename, doc: EBModel, options=None):
        """Write PduR configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_pdur_routing_table(doc)
        self.save(filename)

    def write_pdur_routing_table(self, doc: EBModel):
        """Write PduR routing table to Excel sheet."""
        sheet = self.wb.create_sheet("PduRRoutingTable", 0)

        title_row = ["Name", "EntryID", "PduSID", "SrcPduRef", "DestPduRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for entry in doc.getPduR().getPduRRoutingTableEntryList():
            self.write_cell(sheet, row, 1, entry.getName())
            self.write_cell_center(sheet, row, 2, entry.getPduRRoutingTableEntryID())
            self.write_cell_center(sheet, row, 3, entry.getPduRRoutingPduSID())

            if entry.getPduRSrcPduRef() is not None:
                self.write_cell(sheet, row, 4, entry.getPduRSrcPduRef().getValue())
            if entry.getPduRDestPduRef() is not None:
                self.write_cell(sheet, row, 5, entry.getPduRDestPduRef().getValue())

            row += 1
            self.logger.debug("Write PduRRoutingTableEntry <%s>" % entry.getName())

        self.auto_width(sheet)
