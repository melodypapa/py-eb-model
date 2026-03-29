from ...models.core.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class BswMXdmXlsWriter(ExcelReporter):
    def __init__(self) -> None:
        super().__init__()

    def write_bswm_general(self, doc: EBModel):
        sheet = self.wb.create_sheet("BswMGeneral", 0)

        title_row = ["Name", "DevErrorDetect"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getBswM().getBswMGeneral() is not None:
            general = doc.getBswM().getBswmGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getBswMDevErrorDetect())
            row += 1

        self.auto_width(sheet)

    def write_bswm_mode_declarations(self, doc: EBModel):
        sheet = self.wb.create_sheet("BswMModeDeclaration", 1)

        title_row = ["Name", "AvailableForScheduler", "ModeType", "ModeParentRef", "ModeConditionCount"]
        self.write_title_row(sheet, title_row)

        row = 2
        for mode_declaration in doc.getBswM().getBswMModeDeclarationList():
            self.write_cell(sheet, row, 1, mode_declaration.getName())
            self.write_bool_cell(sheet, row, 2, mode_declaration.getBswMAvailableForScheduler())
            self.write_cell(sheet, row, 3, mode_declaration.getBswMModeType())
            if mode_declaration.getBswMModeParentRef() is not None:
                self.write_cell(sheet, row, 4, mode_declaration.getBswMModeParentRef().getShortName())
            self.write_cell_center(sheet, row, 5, len(mode_declaration.getBswMModeConditionList()))
            row += 1

        self.auto_width(sheet)

    def write_bswm_mode_conditions(self, doc: EBModel):
        sheet = self.wb.create_sheet("BswMModeCondition", 2)

        title_row = ["Name", "BswMModeDeclaration", "SourceRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for mode_declaration in doc.getBswM().getBswMModeDeclarationList():
            for mode_condition in mode_declaration.getBswMModeConditionList():
                self.write_cell(sheet, row, 1, mode_condition.getName())
                self.write_cell(sheet, row, 2, mode_declaration.getName())
                if mode_condition.getBswMModeConditionSourceRef() is not None:
                    self.write_cell(sheet, row, 3, mode_condition.getBswMModeConditionSourceRef().getShortName())
                row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        self.logger.info("Writing <%s>" % filename)

        self.write_bswm_general(doc)
        self.write_bswm_mode_declarations(doc)
        self.write_bswm_mode_conditions(doc)

        self.save(filename)
