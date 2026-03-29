"""
IpduM XDM Excel Reporter - Generates Excel reports for IpduM module configuration.

Implements:
    - SWR_REPORTER_00002: Excel output generation
    - SWR_IPDUM_00003: IpduM configuration reporting
"""
from ...models.core.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class IpduMXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR IpduM module configuration.

    Generates Excel workbook with sheet for dynamic PDUs.

    Implements: SWR_IPDUM_00003 (IpduM Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the IpduM Excel reporter."""
        super().__init__()

    def write(self, filename, doc: EBModel, options=None):
        """Write IpduM configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_ipdum_dyn_pdu(doc)
        self.save(filename)

    def write_ipdum_dyn_pdu(self, doc: EBModel):
        """Write IpduM dynamic PDU configuration to Excel sheet."""
        sheet = self.wb.create_sheet("IpduMDynPdu", 0)

        title_row = ["Name", "DynPduId", "DynPduLength"]
        self.write_title_row(sheet, title_row)

        row = 2
        for pdu in doc.getIpduM().getIpduMDynPduList():
            self.write_cell(sheet, row, 1, pdu.getName())
            self.write_cell_center(sheet, row, 2, pdu.getIpduMDynPduId())
            self.write_cell_center(sheet, row, 3, pdu.getIpduMDynPduLength())
            row += 1
            self.logger.debug("Write IpduMDynPdu <%s>" % pdu.getName())

        self.auto_width(sheet)
