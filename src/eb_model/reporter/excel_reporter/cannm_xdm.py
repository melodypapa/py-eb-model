from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class CanNmXdmXlsWriter(ExcelReporter):
    def __init__(self) -> None:
        super().__init__()

    def write_cannm_general(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanNmGeneral", 0)

        title_row = ["Name", "MultiCoreSupport", "PnSupported", "MaxPn", "DetRuntimeChecks"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getCanNm().getCanNmGeneral() is not None:
            general = doc.getCanNm().getCanNmGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getCanNmMultiCoreSupport())
            self.write_bool_cell(sheet, row, 3, general.getCanNmPnSupported())
            self.write_cell_center(sheet, row, 4, general.getCanNmMaxPn())
            self.write_bool_cell(sheet, row, 5, general.getCanNmDetRuntimeChecks())
            row += 1

        self.auto_width(sheet)

    def write_cannm_global_config(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanNmGlobalConfig", 1)

        title_row = [
            "Name", "DevErrorDetect", "PassiveMode", "BusLoadReduction",
            "RemoteSleepInd", "StateChangeInd", "MainFunctionPeriod",
            "NumberOfChannels"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getCanNm().getCanNmGlobalConfig() is not None:
            global_config = doc.getCanNm().getCanNmGlobalConfig()
            self.write_cell(sheet, row, 1, global_config.getName())
            self.write_bool_cell(sheet, row, 2, global_config.getCanNmDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, global_config.getCanNmPassiveModeEnabled())
            self.write_bool_cell(sheet, row, 4, global_config.getCanNmBusLoadReductionEnabled())
            self.write_bool_cell(sheet, row, 5, global_config.getCanNmRemoteSleepIndEnabled())
            self.write_bool_cell(sheet, row, 6, global_config.getCanNmStateChangeIndEnabled())
            self.write_cell(sheet, row, 7, global_config.getCanNmMainFunctionPeriod())
            self.write_cell_center(sheet, row, 8, global_config.getCanNmNumberOfChannels())
            row += 1

        self.auto_width(sheet)

    def write_cannm_channels(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanNmChannel", 2)

        title_row = ["Name", "NodeIdEnabled", "PnEnabled", "MsgCycleTime", "TimeoutTime", "NetworkHandle", "ComMNetworkHandleRef", "CanNmChannelRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for channel in doc.getCanNm().getCanNmChannelList():
            self.write_cell(sheet, row, 1, channel.getName())
            self.write_bool_cell(sheet, row, 2, channel.getCanNmNodeIdEnabled())
            self.write_bool_cell(sheet, row, 3, channel.getCanNmPnEnabled())
            self.write_cell(sheet, row, 4, channel.getCanNmMsgCycleTime())
            self.write_cell(sheet, row, 5, channel.getCanNmTimeoutTime())
            self.write_cell_center(sheet, row, 6, channel.getCanNmNetworkHandle())
            if channel.getCanNmComMNetworkHandleRef() is not None:
                self.write_cell(sheet, row, 7, channel.getCanNmComMNetworkHandleRef().getShortName())
            if channel.getCanNmCanNmChannelRef() is not None:
                self.write_cell(sheet, row, 8, channel.getCanNmCanNmChannelRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write_cannm_rx_pdus(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanNmRxPdu", 3)

        title_row = ["Name", "RxPduId", "RxPduRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for rx_pdu in doc.getCanNm().getCanNmRxPduList():
            self.write_cell(sheet, row, 1, rx_pdu.getName())
            self.write_cell_center(sheet, row, 2, rx_pdu.getCanNmRxPduId())
            if rx_pdu.getCanNmRxPduRef() is not None:
                self.write_cell(sheet, row, 3, rx_pdu.getCanNmRxPduRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write_cannm_tx_pdus(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanNmTxPdu", 4)

        title_row = ["Name", "TxConfirmationPduId", "TxPduRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for tx_pdu in doc.getCanNm().getCanNmTxPduList():
            self.write_cell(sheet, row, 1, tx_pdu.getName())
            self.write_cell_center(sheet, row, 2, tx_pdu.getCanNmTxConfirmationPduId())
            if tx_pdu.getCanNmTxPduRef() is not None:
                self.write_cell(sheet, row, 3, tx_pdu.getCanNmTxPduRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write_cannm_pn_info(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanNmPnInfo", 5)

        title_row = ["Name", "PnInfoLength", "PnInfoOffset"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getCanNm().getCanNmPnInfo() is not None:
            pn_info = doc.getCanNm().getCanNmPnInfo()
            self.write_cell(sheet, row, 1, pn_info.getName())
            self.write_cell_center(sheet, row, 2, pn_info.getCanNmPnInfoLength())
            self.write_cell_center(sheet, row, 3, pn_info.getCanNmPnInfoOffset())
            row += 1

        self.auto_width(sheet)

    def write_cannm_pn_filter_mask_bytes(self, doc: EBModel):
        sheet = self.wb.create_sheet("CanNmPnFilterMaskByte", 6)

        title_row = ["Name", "Index", "Value"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getCanNm().getCanNmPnInfo() is not None:
            for mask_byte in doc.getCanNm().getCanNmPnInfo().getCanNmPnFilterMaskByteList():
                self.write_cell(sheet, row, 1, mask_byte.getName())
                self.write_cell_center(sheet, row, 2, mask_byte.getCanNmPnFilterMaskByteIndex())
                self.write_cell_center(sheet, row, 3, mask_byte.getCanNmPnFilterMaskByteValue())
                row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        self.logger.info("Writing <%s>" % filename)

        self.write_cannm_general(doc)
        self.write_cannm_global_config(doc)
        self.write_cannm_channels(doc)
        self.write_cannm_rx_pdus(doc)
        self.write_cannm_tx_pdus(doc)
        self.write_cannm_pn_info(doc)
        self.write_cannm_pn_filter_mask_bytes(doc)

        self.save(filename)