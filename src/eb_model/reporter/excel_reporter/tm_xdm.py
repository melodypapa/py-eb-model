from ...models.core.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class TmXdmXlsWriter(ExcelReporter):
    def __init__(self) -> None:
        super().__init__()

    def write_tm_general(self, doc: EBModel):
        sheet = self.wb.create_sheet("TmGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "MainWindowProtect"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getTm().getTmGeneral() is not None:
            general = doc.getTm().getTmGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getTmDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getTmMainWindowProtect())
            row += 1

        self.auto_width(sheet)

    def write_tm_interrupt_synchronization(self, doc: EBModel):
        sheet = self.wb.create_sheet("TmInterruptSynchronization", 1)

        title_row = ["Name", "SyncMode"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getTm().getTmInterruptSynchronization() is not None:
            sync = doc.getTm().getTmInterruptSynchronization()
            self.write_cell(sheet, row, 1, sync.getName())
            self.write_cell(sheet, row, 2, sync.getTmSyncMode())
            row += 1

        self.auto_width(sheet)

    def write_tm_tick_time(self, doc: EBModel):
        sheet = self.wb.create_sheet("TmTickTime", 2)

        title_row = ["Name", "TickTimeBase", "TickPriority"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getTm().getTmTickTime() is not None:
            tick_time = doc.getTm().getTmTickTime()
            self.write_cell(sheet, row, 1, tick_time.getName())
            self.write_cell_center(sheet, row, 2, tick_time.getTmTickTimeBase())
            self.write_cell_center(sheet, row, 3, tick_time.getTmTickPriority())
            row += 1

        self.auto_width(sheet)

    def write_tm_triggers(self, doc: EBModel):
        sheet = self.wb.create_sheet("TmTrigger", 3)

        title_row = ["Name", "TriggerChannelRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for trigger in doc.getTm().getTmTriggerList():
            self.write_cell(sheet, row, 1, trigger.getName())
            if trigger.getTmTriggerChannelRef() is not None:
                self.write_cell(sheet, row, 2, trigger.getTmTriggerChannelRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        self.logger.info("Writing <%s>" % filename)

        self.write_tm_general(doc)
        self.write_tm_interrupt_synchronization(doc)
        self.write_tm_tick_time(doc)
        self.write_tm_triggers(doc)

        self.save(filename)
