from ...models.rte_xdm import RteBswEventToTaskMapping, RteBswModuleInstance, RteEventToTaskMapping, RteSwComponentInstance
from ...models.eb_doc import EBModel
from .abstract import ExcelReporter


class RteXdmXlsWriter(ExcelReporter):
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
        self.logger.info("Writing <%s>" % filename)
        self.write_os_tasks(doc)
        self.write_os_isrs(doc)

        self.save(filename)


class RteRunnableEntityXlsWriter(ExcelReporter):
    def __init__(self) -> None:
        super().__init__()

    def write_mapped_events(self, doc: EBModel):
        sheet = self.wb.create_sheet("Event Mapping", 0)

        title_row = ["OsTask", "Event", "Event Type", "Executable Entity", "Instance", "Position", "Offset"]
        self.write_title_row(sheet, title_row)

        row = 2
        for os_task, mappings in doc.getRte().getMappedEvents().items():
            for mapping in sorted(mappings, key=lambda a: a.getRtePositionInTask()):
                self.write_cell(sheet, row, 1, os_task)
                if isinstance(mapping, RteBswEventToTaskMapping):
                    self.logger.debug("Write Mapping %s" % mapping.getName())
                    instance = mapping.getRteBswModuleInstance()
                    self.write_cell(sheet, row, 2, mapping.getRteBswEventRefs().getShortName())
                    self.write_cell(sheet, row, 5, instance.getRteBswImplementationRef().getValue())
                    self.write_cell(sheet, row, 6, mapping.getRteBswPositionInTask())
                    self.write_cell(sheet, row, 7, mapping.getRteBswActivationOffset())
                elif isinstance(mapping, RteEventToTaskMapping):
                    self.logger.debug("Write Mapping %s" % mapping.getName())
                    instance = mapping.getRteSwComponentInstance()
                    self.write_cell(sheet, row, 2, mapping.getRteEventRef().getShortName())
                    self.write_cell(sheet, row, 5, instance.getRteSoftwareComponentInstanceRef().getValue())
                    self.write_cell(sheet, row, 6, mapping.getRtePositionInTask())
                    self.write_cell(sheet, row, 7, mapping.getRteActivationOffset())
                else:
                    raise NotImplementedError("Invalid Rte Event To Task Mapping <%s>" % type(mapping))
                
                row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel):
        self.logger.info("Writing <%s>" % filename)
        self.write_mapped_events(doc)

        self.save(filename)
