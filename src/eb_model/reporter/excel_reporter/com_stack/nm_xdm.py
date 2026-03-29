"""
Nm XDM Excel Reporter - Generates Excel reports for Nm module configuration.

Implements:
    - SWR_REPORTER_00002: Excel output generation
    - SWR_NM_00003: Nm configuration reporting
"""
from ....models.core.eb_doc import EBModel
from ..core.abstract import ExcelReporter


class NmXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR Nm module configuration.

    Generates Excel workbook with sheet for channel configurations.

    Implements: SWR_NM_00003 (Nm Configuration Reporting)
    """

    def __init__(self) -> None:
        """Initialize the Nm Excel reporter."""
        super().__init__()

    def write(self, filename, doc: EBModel, options=None):
        """Write Nm configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_nm_channels(doc)
        self.save(filename)

    def write_nm_channels(self, doc: EBModel):
        """Write Nm channel configuration to Excel sheet."""
        sheet = self.wb.create_sheet("NmChannel", 0)

        title_row = ["Name", "ChannelId", "BusType", "MsgCycleTime", "TimeoutTime", "NetworkHandle", "ComMNetworkHandleRef", "NodeEnabled"]
        self.write_title_row(sheet, title_row)

        row = 2
        for channel in doc.getNm().getNmChannelList():
            self.write_cell(sheet, row, 1, channel.getName())
            self.write_cell_center(sheet, row, 2, channel.getNmChannelId())
            self.write_cell(sheet, row, 3, channel.getNmBusType())
            self.write_cell_center(sheet, row, 4, channel.getNmMsgCycleTime())
            self.write_cell_center(sheet, row, 5, channel.getNmTimeoutTime())
            self.write_cell_center(sheet, row, 6, channel.getNmNetworkHandle())

            if channel.getNmComMNetworkHandleRef() is not None:
                self.write_cell(sheet, row, 7, channel.getNmComMNetworkHandleRef().getValue())

            self.write_bool_cell(sheet, row, 8, channel.getNmNodeEnabled())

            row += 1
            self.logger.debug("Write NmChannel <%s>" % channel.getName())

        self.auto_width(sheet)
