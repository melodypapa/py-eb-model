from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class EthSMXdmXlsWriter(ExcelReporter):
    """Excel reporter for EthSM module configuration."""
    def __init__(self) -> None:
        super().__init__()

    def write_ethsm_general(self, doc: EBModel):
        """Write EthSM general configuration sheet."""
        sheet = self.wb.create_sheet("EthSMGeneral", 0)

        title_row = [
            "Name", "DevErrorDetect", "DummyMode", "MainFunctionPeriod",
            "VersionInfoApi", "SingleNetworkOptEnable", "MaxNetworks",
            "MultiCoreSupport", "DevAuthSupport", "RelocatablePbcfgEnable"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getEthSM().getEthSMGeneral() is not None:
            general = doc.getEthSM().getEthSMGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getEthSMDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getEthSMDummyMode())
            self.write_cell(sheet, row, 4, general.getEthSMMainFunctionPeriod())
            self.write_bool_cell(sheet, row, 5, general.getEthSMVersionInfoApi())
            self.write_bool_cell(sheet, row, 6, general.getEthSMSingleNetworkOptEnable())
            self.write_cell_center(sheet, row, 7, general.getEthSMMaxNetworks())
            self.write_bool_cell(sheet, row, 8, general.getEthSMMultiCoreSupport())
            self.write_bool_cell(sheet, row, 9, general.getEthSMDevAuthSupport())
            self.write_bool_cell(sheet, row, 10, general.getEthSMRelocatablePbcfgEnable())
            row += 1

        self.auto_width(sheet)

    def write_ethsm_networks(self, doc: EBModel):
        """Write EthSM network configurations sheet."""
        sheet = self.wb.create_sheet("EthSMNetwork", 1)

        title_row = [
            "Name", "EthIfControllerRef", "ComMNetworkHandleRef",
            "DevAuthNoComNotificationEnable", "DemEventParameterRef"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getEthSM().getEthSMNetworkList():
            self.write_cell(sheet, row, 1, cfg.getName())
            if cfg.getEthSMEthIfControllerRef() is not None:
                self.write_cell(sheet, row, 2, cfg.getEthSMEthIfControllerRef().getShortName())
            if cfg.getEthSMComMNetworkHandleRef() is not None:
                self.write_cell(sheet, row, 3, cfg.getEthSMComMNetworkHandleRef().getShortName())
            self.write_bool_cell(sheet, row, 4, cfg.getEthSMDevAuthNoComNotificationEnable())
            if cfg.getEthSMDemEventParameterRefs() is not None:
                dem_ref = cfg.getEthSMDemEventParameterRefs().getEthSMDemEventParameterRef()
                if dem_ref is not None:
                    self.write_cell(sheet, row, 5, dem_ref.getShortName())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """Write EthSM configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_ethsm_general(doc)
        self.write_ethsm_networks(doc)

        self.save(filename)