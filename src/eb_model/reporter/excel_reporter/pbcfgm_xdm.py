from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class PbcfgMXdmXlsWriter(ExcelReporter):
    def __init__(self) -> None:
        super().__init__()

    def write_pbcfgm_general(self, doc: EBModel):
        sheet = self.wb.create_sheet("PbcfgMGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "InitConfiguration"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getPbcfgM().getPbcfgMGeneral() is not None:
            general = doc.getPbcfgM().getPbcfgMGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getPbcfgMDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getPbcfgMInitConfiguration())
            row += 1

        self.auto_width(sheet)

    def write_pbcfgm_protection_sets(self, doc: EBModel):
        sheet = self.wb.create_sheet("PbcfgMProtectionSet", 1)

        title_row = ["Name", "ProtectionSetName"]
        self.write_title_row(sheet, title_row)

        row = 2
        for protection_set in doc.getPbcfgM().getPbcfgMProtectionSetList():
            self.write_cell(sheet, row, 1, protection_set.getName())
            self.write_cell(sheet, row, 2, protection_set.getPbcfgMProtectionSetName())
            row += 1

        self.auto_width(sheet)

    def write_pbcfgm_core_protection_sets(self, doc: EBModel):
        sheet = self.wb.create_sheet("PbcfgMCoreProtectionSet", 2)

        title_row = ["Name", "CoreProtectionSetRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for core_protection_set in doc.getPbcfgM().getPbcfgMCoreProtectionSetList():
            self.write_cell(sheet, row, 1, core_protection_set.getName())
            if core_protection_set.getPbcfgMCoreProtectionSetRef() is not None:
                self.write_cell(sheet, row, 2, core_protection_set.getPbcfgMCoreProtectionSetRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        self.logger.info("Writing <%s>" % filename)

        self.write_pbcfgm_general(doc)
        self.write_pbcfgm_protection_sets(doc)
        self.write_pbcfgm_core_protection_sets(doc)

        self.save(filename)
