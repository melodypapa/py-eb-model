from ...models.core.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class EthIfXdmXlsWriter(ExcelReporter):
    """Excel reporter for EthIf module configuration."""
    def __init__(self) -> None:
        super().__init__()

    def write_ethif_general(self, doc: EBModel):
        """Write EthIf general configuration sheet."""
        sheet = self.wb.create_sheet("EthIfGeneral", 0)

        title_row = [
            "Name", "DevErrorDetect", "EnableRxInterrupt", "MainFunctionPeriod",
            "MaxTrcvsTotal", "SupportEthAPI", "PublicHandleTypeEnum",
            "MaxCtrl", "MaxPhyCtrl", "MaxEthSwitches", "MaxSwtPorts",
            "RelocatablePbcfgEnable", "VLANSupportEnable"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getEthIf().getEthIfGeneral() is not None:
            general = doc.getEthIf().getEthIfGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getEthIfDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getEthIfEnableRxInterrupt())
            self.write_cell(sheet, row, 4, general.getEthIfMainFunctionPeriod())
            self.write_cell_center(sheet, row, 5, general.getEthIfMaxTrcvsTotal())
            self.write_cell(sheet, row, 6, general.getEthIfSupportEthAPI())
            self.write_cell(sheet, row, 7, general.getEthIfPublicHandleTypeEnum())
            self.write_cell_center(sheet, row, 8, general.getEthIfMaxCtrl())
            self.write_cell_center(sheet, row, 9, general.getEthIfMaxPhyCtrl())
            self.write_cell_center(sheet, row, 10, general.getEthIfMaxEthSwitches())
            self.write_cell_center(sheet, row, 11, general.getEthIfMaxSwtPorts())
            self.write_bool_cell(sheet, row, 12, general.getEthIfRelocatablePbcfgEnable())
            self.write_bool_cell(sheet, row, 13, general.getEthIfVLANSupportEnable())
            row += 1

        self.auto_width(sheet)

    def write_ethif_controllers(self, doc: EBModel):
        """Write EthIf controller configurations sheet."""
        sheet = self.wb.create_sheet("EthIfController", 1)

        title_row = [
            "Name", "CtrlIdx", "CtrlMtu", "MaxTxBufsTotal", "VlanId",
            "EthTrcvRef", "PhysControllerRef", "SwitchRefOrPortGroupRef"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getEthIf().getEthIfControllerList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_cell_center(sheet, row, 2, cfg.getEthIfCtrlIdx())
            self.write_cell_center(sheet, row, 3, cfg.getEthIfCtrlMtu())
            self.write_cell_center(sheet, row, 4, cfg.getEthIfMaxTxBufsTotal())
            self.write_cell_center(sheet, row, 5, cfg.getEthIfVlanId())
            if cfg.getEthIfEthTrcvRef() is not None:
                self.write_cell(sheet, row, 6, cfg.getEthIfEthTrcvRef().getShortName())
            if cfg.getEthIfPhysControllerRef() is not None:
                self.write_cell(sheet, row, 7, cfg.getEthIfPhysControllerRef().getShortName())
            if cfg.getEthIfSwitchRefOrPortGroupRef() is not None:
                self.write_cell(sheet, row, 8, cfg.getEthIfSwitchRefOrPortGroupRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write_ethif_frame_owner_configs(self, doc: EBModel):
        """Write EthIf frame owner configurations sheet."""
        sheet = self.wb.create_sheet("EthIfFrameOwnerConfig", 2)

        title_row = ["Name", "FrameType", "Owner"]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getEthIf().getEthIfFrameOwnerConfigList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_cell_center(sheet, row, 2, cfg.getEthIfFrameType())
            self.write_cell_center(sheet, row, 3, cfg.getEthIfOwner())
            row += 1

        self.auto_width(sheet)

    def write_ethif_phys_controllers(self, doc: EBModel):
        """Write EthIf physical controller configurations sheet."""
        sheet = self.wb.create_sheet("EthIfPhysController", 3)

        title_row = ["Name", "PhysControllerIdx", "EthCtrlRef", "WEthCtrlRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getEthIf().getEthIfPhysControllerList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_cell_center(sheet, row, 2, cfg.getEthIfPhysControllerIdx())
            if cfg.getEthIfEthCtrlRef() is not None:
                self.write_cell(sheet, row, 3, cfg.getEthIfEthCtrlRef().getShortName())
            if cfg.getEthIfWEthCtrlRef() is not None:
                self.write_cell(sheet, row, 4, cfg.getEthIfWEthCtrlRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write_ethif_switches(self, doc: EBModel):
        """Write EthIf switch configurations sheet."""
        sheet = self.wb.create_sheet("EthIfSwitch", 4)

        title_row = ["Name", "SwitchIdx", "SwitchRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getEthIf().getEthIfSwitchList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_cell_center(sheet, row, 2, cfg.getEthIfSwitchIdx())
            if cfg.getEthIfSwitchRef() is not None:
                self.write_cell(sheet, row, 3, cfg.getEthIfSwitchRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write_ethif_switch_port_groups(self, doc: EBModel):
        """Write EthIf switch port group configurations sheet."""
        sheet = self.wb.create_sheet("EthIfSwitchPortGroup", 5)

        title_row = ["Name", "SwitchPortGroupIdx", "PortRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getEthIf().getEthIfSwitchPortGroupList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_cell_center(sheet, row, 2, cfg.getEthIfSwitchPortGroupIdx())
            if cfg.getEthIfPortRef() is not None:
                self.write_cell(sheet, row, 3, cfg.getEthIfPortRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write_ethif_transceivers(self, doc: EBModel):
        """Write EthIf transceiver configurations sheet."""
        sheet = self.wb.create_sheet("EthIfTransceiver", 6)

        title_row = ["Name", "TransceiverIdx", "EthTrcvRef", "WEthTrcvRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getEthIf().getEthIfTransceiverList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_cell_center(sheet, row, 2, cfg.getEthIfTransceiverIdx())
            if cfg.getEthIfEthTrcvRef() is not None:
                self.write_cell(sheet, row, 3, cfg.getEthIfEthTrcvRef().getShortName())
            if cfg.getEthIfWEthTrcvRef() is not None:
                self.write_cell(sheet, row, 4, cfg.getEthIfWEthTrcvRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """Write EthIf configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_ethif_general(doc)
        self.write_ethif_controllers(doc)
        self.write_ethif_frame_owner_configs(doc)
        self.write_ethif_phys_controllers(doc)
        self.write_ethif_switches(doc)
        self.write_ethif_switch_port_groups(doc)
        self.write_ethif_transceivers(doc)

        self.save(filename)
