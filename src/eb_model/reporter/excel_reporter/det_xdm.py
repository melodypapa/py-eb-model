from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class DetXdmXlsWriter(ExcelReporter):
    def __init__(self) -> None:
        super().__init__()

    def write_det_general(self, doc: EBModel):
        sheet = self.wb.create_sheet("DetGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "Enabled"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getDet().getDetGeneral() is not None:
            general = doc.getDet().getDetGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getDetDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getDetEnabled())
            row += 1

        self.auto_width(sheet)

    def write_det_error_hook(self, doc: EBModel):
        sheet = self.wb.create_sheet("DetErrorHook", 1)

        title_row = ["Name", "ErrorHookCallbackName"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getDet().getDetErrorHook() is not None:
            error_hook = doc.getDet().getDetErrorHook()
            self.write_cell(sheet, row, 1, error_hook.getName())
            self.write_cell(sheet, row, 2, error_hook.getDetErrorHookCallbackName())
            row += 1

        self.auto_width(sheet)

    def write_det_init_error(self, doc: EBModel):
        sheet = self.wb.create_sheet("DetInitError", 2)

        title_row = ["Name", "InitErrorRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getDet().getDetInitError() is not None:
            init_error = doc.getDet().getDetInitError()
            self.write_cell(sheet, row, 1, init_error.getName())
            if init_error.getDetInitErrorRef() is not None:
                self.write_cell(sheet, row, 2, init_error.getDetInitErrorRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        self.logger.info("Writing <%s>" % filename)

        self.write_det_general(doc)
        self.write_det_error_hook(doc)
        self.write_det_init_error(doc)

        self.save(filename)
