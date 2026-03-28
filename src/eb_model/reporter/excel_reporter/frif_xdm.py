from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class FrIfXdmXlsWriter(ExcelReporter):
    """Excel reporter for FrIf module configuration."""
    def __init__(self) -> None:
        super().__init__()

    def write_frif_general(self, doc: EBModel):
        """Write FrIf general configuration sheet."""
        sheet = self.wb.create_sheet("FrIfGeneral", 0)

        title_row = [
            "Name", "DevErrorDetect", "MainFunctionPeriod", "MaxNumOfClusters",
            "SupportFrApi", "PolarizationSelection", "TransceiverAssignment",
            "WakeupPatternSupport", "VTPSupport", "PublicHandleTypeEnum",
            "RelocatablePbcfgEnable"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getFrIf().getFrIfGeneral() is not None:
            general = doc.getFrIf().getFrIfGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getFrIfDevErrorDetect())
            self.write_cell(sheet, row, 3, general.getFrIfMainFunctionPeriod())
            self.write_cell_center(sheet, row, 4, general.getFrIfMaxNumOfClusters())
            self.write_cell(sheet, row, 5, general.getFrIfSupportFrApi())
            self.write_bool_cell(sheet, row, 6, general.getFrIfPolarizationSelection())
            self.write_bool_cell(sheet, row, 7, general.getFrIfTransceiverAssignment())
            self.write_bool_cell(sheet, row, 8, general.getFrIfWakeupPatternSupport())
            self.write_bool_cell(sheet, row, 9, general.getFrIfVTPSupport())
            self.write_cell(sheet, row, 10, general.getFrIfPublicHandleTypeEnum())
            self.write_bool_cell(sheet, row, 11, general.getFrIfRelocatablePbcfgEnable())
            row += 1

        self.auto_width(sheet)

    def write_frif_controllers(self, doc: EBModel):
        """Write FrIf controller configurations sheet."""
        sheet = self.wb.create_sheet("FrIfController", 1)

        title_row = ["Name", "CtrlIdx", "CtrlMtu"]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getFrIf().getFrIfControllerList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_cell_center(sheet, row, 2, cfg.getFrIfCtrlIdx())
            self.write_cell_center(sheet, row, 3, cfg.getFrIfCtrlMtu())
            row += 1

        self.auto_width(sheet)

    def write_frif_clusters(self, doc: EBModel):
        """Write FrIf cluster configurations sheet."""
        sheet = self.wb.create_sheet("FrIfCluster", 2)

        title_row = ["Name"]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getFrIf().getFrIfClusterList():
            self.write_cell(sheet, row, 1, cfg.getName())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """Write FrIf configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_frif_general(doc)
        self.write_frif_controllers(doc)
        self.write_frif_clusters(doc)

        self.save(filename)
