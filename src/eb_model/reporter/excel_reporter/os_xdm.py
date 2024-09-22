from ...models.eb_doc import EBModel
from .abstract import ExcelReporter

class OsXdmXlsWriter(ExcelReporter):
    def __init__(self) -> None:
        super().__init__()

    def write_os_tasks(self, doc: EBModel):
        sheet = self.wb.create_sheet("OsTask", 0)

        title_row = ["Name", "OsTaskActivation", "OsTaskPriority", "OsTaskSchedule", "OsStacksize"]
        self.write_title_row(sheet, title_row)

        row = 2
        for os_task in doc.getOs().getOsTaskList():
            self.write_cell(sheet, row, 1, os_task.getName())
            self.write_cell(sheet, row, 2, os_task.getOsTaskActivation())
            self.write_cell(sheet, row, 3, os_task.getOsTaskPriority())
            self.write_cell(sheet, row, 4, os_task.getOsTaskSchedule())
            self.write_cell(sheet, row, 5, os_task.getOsStacksize())
            row += 1

        self.auto_width(sheet)

    def write_os_isrs(self, doc: EBModel):
        sheet = self.wb.create_sheet("OsIsr", 0)

        title_row = ["Name", "OsIsrCategory", "OsStacksize"]
        self.write_title_row(sheet, title_row)

        row = 2
        for os_isr in doc.getOs().getOsIsrList():
            self.write_cell(sheet, row, 1, os_isr.getName())
            self.write_cell(sheet, row, 2, os_isr.getOsIsrCategory())
            self.write_cell(sheet, row, 3, os_isr.getOsStacksize())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel):
        self.write_os_tasks(doc)
        self.write_os_isrs(doc)

        self.save(filename)
