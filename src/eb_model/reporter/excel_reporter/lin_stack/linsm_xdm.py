from ....models.core.eb_doc import EBModel
from ..core.abstract import ExcelReporter


class LinSMXdmXlsWriter(ExcelReporter):
    def __init__(self) -> None:
        super().__init__()

    def write_linsm_general(self, doc: EBModel):
        sheet = self.wb.create_sheet("LinSMGeneral", 0)
        title_row = ["Name", "DevErrorDetect", "MainProcessingPeriod"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getLinSM().getLinSMGeneral() is not None:
            general = doc.getLinSM().getLinSMGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getLinSMDevErrorDetect())
            self.write_cell(sheet, row, 3, general.getLinSMMainProcessingPeriod())
            row += 1

        self.auto_width(sheet)

    def write_linsm_channels(self, doc: EBModel):
        sheet = self.wb.create_sheet("LinSMChannel", 1)
        title_row = ["Name", "ConfirmationTimeout", "SleepSupport", "ComMNetworkHandleRef", "NodeType"]
        self.write_title_row(sheet, title_row)

        row = 2
        for channel in doc.getLinSM().getLinSMChannelList():
            self.write_cell(sheet, row, 1, channel.getName())
            self.write_cell(sheet, row, 2, channel.getLinSMConfirmationTimeout())
            self.write_bool_cell(sheet, row, 3, channel.getLinSMSleepSupport())
            if channel.getLinSMComMNetworkHandleRef() is not None:
                self.write_cell(sheet, row, 4, channel.getLinSMComMNetworkHandleRef().getShortName())
            self.write_cell(sheet, row, 5, channel.getLinSMNodeType())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        self.logger.info("Writing <%s>" % filename)

        self.write_linsm_general(doc)
        self.write_linsm_channels(doc)

        self.save(filename)
