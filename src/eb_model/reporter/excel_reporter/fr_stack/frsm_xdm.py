from ....models.core.eb_doc import EBModel
from ..core.abstract import ExcelReporter


class FrSMXdmXlsWriter(ExcelReporter):
    """Excel reporter for FrSM module configuration."""
    def __init__(self) -> None:
        super().__init__()

    def write_frsm_general(self, doc: EBModel):
        """Write FrSM general configuration sheet."""
        sheet = self.wb.create_sheet("FrSMGeneral", 0)

        title_row = [
            "Name", "DevErrorDetect", "SyncLossErrorIndicationName",
            "VersionInfoApi", "FrTrcvControlEnable", "ComMIndicationEnable",
            "SingleClstOptEnable", "ReportToBswMEnable", "SetEcuPassiveEnable",
            "FrNmStartupErrorEnable", "KeySlotOnlyModeEnable",
            "SyncLossErrorIndicationHeaderName", "MultiCoreSupportEnable"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getFrSM().getFrSMGeneral() is not None:
            general = doc.getFrSM().getFrSMGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getFrSMDevErrorDetect())
            self.write_cell(sheet, row, 3, general.getFrSMSyncLossErrorIndicationName())
            self.write_bool_cell(sheet, row, 4, general.getFrSMVersionInfoApi())
            self.write_bool_cell(sheet, row, 5, general.getFrSMFrTrcvControlEnable())
            self.write_bool_cell(sheet, row, 6, general.getFrSMComMIndicationEnable())
            self.write_bool_cell(sheet, row, 7, general.getFrSMSingleClstOptEnable())
            self.write_bool_cell(sheet, row, 8, general.getFrSMReportToBswMEnable())
            self.write_bool_cell(sheet, row, 9, general.getFrSMSetEcuPassiveEnable())
            self.write_bool_cell(sheet, row, 10, general.getFrSMFrNmStartupErrorEnable())
            self.write_bool_cell(sheet, row, 11, general.getFrSMKeySlotOnlyModeEnable())
            self.write_cell(sheet, row, 12, general.getFrSMSyncLossErrorIndicationHeaderName())
            self.write_bool_cell(sheet, row, 13, general.getFrSMMultiCoreSupportEnable())
            row += 1

        self.auto_width(sheet)

    def write_frsm_clusters(self, doc: EBModel):
        """Write FrSM cluster configurations sheet."""
        sheet = self.wb.create_sheet("FrSMCluster", 1)

        title_row = [
            "Name", "CheckWakeupReason", "DelayStartupWithoutWakeup",
            "DurationT1", "DurationT2", "DurationT3", "IsColdstartEcu",
            "IsWakeupEcu", "MainFunctionCycleTime", "MinNumberOfColdstarter",
            "NumWakeupPatterns", "StartupRepetitions", "StartupRepetitionsWithWakeup",
            "ComMNetworkHandleRef", "FrIfClusterRef", "ClusterStartupRef", "ClusterSyncLossRef"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getFrSM().getFrSMClusterList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_bool_cell(sheet, row, 2, cfg.getFrSMCheckWakeupReason())
            self.write_bool_cell(sheet, row, 3, cfg.getFrSMDelayStartupWithoutWakeup())
            self.write_cell(sheet, row, 4, cfg.getFrSMDurationT1())
            self.write_cell(sheet, row, 5, cfg.getFrSMDurationT2())
            self.write_cell(sheet, row, 6, cfg.getFrSMDurationT3())
            self.write_bool_cell(sheet, row, 7, cfg.getFrSMIsColdstartEcu())
            self.write_bool_cell(sheet, row, 8, cfg.getFrSMIsWakeupEcu())
            self.write_cell(sheet, row, 9, cfg.getFrSMMainFunctionCycleTime())
            self.write_cell_center(sheet, row, 10, cfg.getFrSMMinNumberOfColdstarter())
            self.write_cell_center(sheet, row, 11, cfg.getFrSMNumWakeupPatterns())
            self.write_cell_center(sheet, row, 12, cfg.getFrSMStartupRepetitions())
            self.write_cell_center(sheet, row, 13, cfg.getFrSMStartupRepetitionsWithWakeup())
            if cfg.getFrSMComMNetworkHandleRef() is not None:
                self.write_cell(sheet, row, 14, cfg.getFrSMComMNetworkHandleRef().getShortName())
            if cfg.getFrSMFrIfClusterRef() is not None:
                self.write_cell(sheet, row, 15, cfg.getFrSMFrIfClusterRef().getShortName())
            if cfg.getFrSMClusterDemEventParameterRefs() is not None:
                dem_refs = cfg.getFrSMClusterDemEventParameterRefs()
                if dem_refs.getFrSMClusterStartupRef() is not None:
                    self.write_cell(sheet, row, 16, dem_refs.getFrSMClusterStartupRef().getShortName())
                if dem_refs.getFrSMClusterSyncLossRef() is not None:
                    self.write_cell(sheet, row, 17, dem_refs.getFrSMClusterSyncLossRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """Write FrSM configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_frsm_general(doc)
        self.write_frsm_clusters(doc)

        self.save(filename)
