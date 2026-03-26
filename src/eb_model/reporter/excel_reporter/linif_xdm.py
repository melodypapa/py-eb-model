from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class LinIfXdmXlsWriter(ExcelReporter):
    def __init__(self) -> None:
        super().__init__()

    def write_linif_general(self, doc: EBModel):
        sheet = self.wb.create_sheet("LinIfGeneral", 0)
        title_row = ["Name", "DevErrorDetect", "MaxChannels", "TpSupported"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getLinIf().getLinIfGeneral() is not None:
            general = doc.getLinIf().getLinIfGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getLinIfDevErrorDetect())
            self.write_cell_center(sheet, row, 3, general.getLinIfMaxChannels())
            self.write_bool_cell(sheet, row, 4, general.getLinIfTpSupported())
            row += 1

        self.auto_width(sheet)

    def write_linif_channels(self, doc: EBModel):
        sheet = self.wb.create_sheet("LinIfChannel", 1)
        title_row = ["Name", "ChannelId", "ChannelRef", "ComMNetworkHandleRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for channel in doc.getLinIf().getLinIfChannelList():
            self.write_cell(sheet, row, 1, channel.getName())
            self.write_cell_center(sheet, row, 2, channel.getLinIfChannelId())
            if channel.getLinIfChannelRef() is not None:
                self.write_cell(sheet, row, 3, channel.getLinIfChannelRef().getShortName())
            if channel.getLinIfComMNetworkHandleRef() is not None:
                self.write_cell(sheet, row, 4, channel.getLinIfComMNetworkHandleRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write_linif_frames(self, doc: EBModel):
        sheet = self.wb.create_sheet("LinIfFrame", 2)
        title_row = ["Name", "FrameId", "FrameType", "ChecksumType", "Length"]
        self.write_title_row(sheet, title_row)

        row = 2
        for frame in doc.getLinIf().getLinIfFrameList():
            self.write_cell(sheet, row, 1, frame.getName())
            self.write_cell_center(sheet, row, 2, frame.getLinIfFrameId())
            self.write_cell(sheet, row, 3, frame.getLinIfFrameType())
            self.write_cell(sheet, row, 4, frame.getLinIfChecksumType())
            self.write_cell_center(sheet, row, 5, frame.getLinIfLength())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        self.logger.info("Writing <%s>" % filename)

        self.write_linif_general(doc)
        self.write_linif_channels(doc)
        self.write_linif_frames(doc)

        self.save(filename)
