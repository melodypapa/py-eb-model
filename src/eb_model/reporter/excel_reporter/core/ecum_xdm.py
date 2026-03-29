from ....models.core.eb_doc import EBModel
from .abstract import ExcelReporter


class EcuMXdmXlsWriter(ExcelReporter):
    def __init__(self) -> None:
        super().__init__()

    def write_ecum_general(self, doc: EBModel):
        sheet = self.wb.create_sheet("EcuMGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "ConfigurationVariant"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getEcuM().getEcumGeneral() is not None:
            general = doc.getEcuM().getEcumGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getEcumDevErrorDetect())
            self.write_cell(sheet, row, 3, general.getEcumConfigurationVariant())
            row += 1

        self.auto_width(sheet)

    def write_ecum_startup(self, doc: EBModel):
        sheet = self.wb.create_sheet("EcuMStartup", 1)

        title_row = ["Name", "EnableUserMcuStartup", "UserMcuStartupRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getEcuM().getEcumStartup() is not None:
            startup = doc.getEcuM().getEcumStartup()
            self.write_cell(sheet, row, 1, startup.getName())
            self.write_bool_cell(sheet, row, 2, startup.getEcumEnableUserMcuStartup())
            if startup.getEcumUserMcuStartupRef() is not None:
                self.write_cell(sheet, row, 3, startup.getEcumUserMcuStartupRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write_ecum_shutdown(self, doc: EBModel):
        sheet = self.wb.create_sheet("EcuMShutdown", 2)

        title_row = ["Name", "EnableUserMcuShutdown", "UserMcuShutdownRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getEcuM().getEcumShutdown() is not None:
            shutdown = doc.getEcuM().getEcumShutdown()
            self.write_cell(sheet, row, 1, shutdown.getName())
            self.write_bool_cell(sheet, row, 2, shutdown.getEcumEnableUserMcuShutdown())
            if shutdown.getEcumUserMcuShutdownRef() is not None:
                self.write_cell(sheet, row, 3, shutdown.getEcumUserMcuShutdownRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write_ecum_alarms(self, doc: EBModel):
        sheet = self.wb.create_sheet("EcuMAlarm", 3)

        title_row = ["Name", "CounterRef", "ActionRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for alarm in doc.getEcuM().getEcumAlarmList():
            self.write_cell(sheet, row, 1, alarm.getName())
            if alarm.getEcumAlarmCounterRef() is not None:
                self.write_cell(sheet, row, 2, alarm.getEcumAlarmCounterRef().getShortName())
            if alarm.getEcumAlarmActionRef() is not None:
                self.write_cell(sheet, row, 3, alarm.getEcumAlarmActionRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        self.logger.info("Writing <%s>" % filename)

        self.write_ecum_general(doc)
        self.write_ecum_startup(doc)
        self.write_ecum_shutdown(doc)
        self.write_ecum_alarms(doc)

        self.save(filename)
