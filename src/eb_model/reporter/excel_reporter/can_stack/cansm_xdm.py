from eb_model.models.core.eb_doc import EBModel
from eb_model.reporter.excel_reporter.core.abstract import ExcelReporter


class CanSMXdmXlsWriter(ExcelReporter):
    def __init__(self) -> None:
        super().__init__()

    def write_cansm_general(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanSMGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "MainFunctionTimePeriod", "PNSupport", "EnhancedBusOffReporting"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getCanSM().getCanSMGeneral() is not None:
            general = doc.getCanSM().getCanSMGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getCanSMDevErrorDetect())
            self.write_cell(sheet, row, 3, general.getCanSMMainFunctionTimePeriod())
            self.write_bool_cell(sheet, row, 4, general.getCanSMPNSupport())
            self.write_bool_cell(sheet, row, 5, general.getCanSMEnhancedBusOffReporting())
            row += 1

        self.auto_width(sheet)

    def write_cansm_manager_networks(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanSMManagerNetwork", 1)

        title_row = ["Name", "BorCounterL1ToL2", "BorTimeL1", "BorTimeL2", "BorTimeTxEnsured",
                     "TxConfirmationPolling", "ActivatePN", "ComMNetworkHandleRef", "TransceiverId"]
        self.write_title_row(sheet, title_row)

        row = 2
        for network in doc.getCanSM().getCanSMManagerNetworkList():
            self.write_cell(sheet, row, 1, network.getName())
            self.write_cell_center(sheet, row, 2, network.getCanSMBorCounterL1ToL2())
            self.write_cell(sheet, row, 3, network.getCanSMBorTimeL1())
            self.write_cell(sheet, row, 4, network.getCanSMBorTimeL2())
            self.write_cell(sheet, row, 5, network.getCanSMBorTimeTxEnsured())
            self.write_bool_cell(sheet, row, 6, network.getCanSMBorTxConfirmationPolling())
            self.write_bool_cell(sheet, row, 7, network.getCanSMActivatePN())
            if network.getCanSMComMNetworkHandleRef() is not None:
                self.write_cell(sheet, row, 8, network.getCanSMComMNetworkHandleRef().getShortName())
            if network.getCanSMTransceiverId() is not None:
                self.write_cell(sheet, row, 9, network.getCanSMTransceiverId().getShortName())
            row += 1

        self.auto_width(sheet)

    def write_cansm_dem_event_refs(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanSMDemEventParameterRefs", 2)

        title_row = ["Name", "BusOffDemEventRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getCanSM().getCanSMDemEventParameterRefs() is not None:
            dem_refs = doc.getCanSM().getCanSMDemEventParameterRefs()
            self.write_cell(sheet, row, 1, dem_refs.getName())
            if dem_refs.getCanSMBusOffDemEventRef() is not None:
                self.write_cell(sheet, row, 2, dem_refs.getCanSMBusOffDemEventRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        self.logger.info("Writing <%s>" % filename)

        self.write_cansm_general(doc)
        self.write_cansm_manager_networks(doc)
        self.write_cansm_dem_event_refs(doc)

        self.save(filename)
