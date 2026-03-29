from ....models.core.eb_doc import EBModel
from ..core.abstract import ExcelReporter


class SoAdXdmXlsWriter(ExcelReporter):
    """Excel reporter for SoAd module configuration."""
    def __init__(self) -> None:
        super().__init__()

    def write_soad_general(self, doc: EBModel):
        """Write SoAd general configuration sheet."""
        sheet = self.wb.create_sheet("SoAdGeneral", 0)

        title_row = [
            "Name", "DevErrorDetect", "GetAndResetMeasurementDataApi",
            "IPv6AddressEnabled", "MainFunctionPeriod", "SoConMax",
            "RoutingGroupMax", "VersionInfoApi", "TlsEnabled",
            "EnableSecurityEventReporting"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getSoAd().getSoAdGeneral() is not None:
            general = doc.getSoAd().getSoAdGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getSoAdDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getSoAdGetAndResetMeasurementDataApi())
            self.write_bool_cell(sheet, row, 4, general.getSoAdIPv6AddressEnabled())
            self.write_cell(sheet, row, 5, general.getSoAdMainFunctionPeriod())
            self.write_cell_center(sheet, row, 6, general.getSoAdSoConMax())
            self.write_cell_center(sheet, row, 7, general.getSoAdRoutingGroupMax())
            self.write_bool_cell(sheet, row, 8, general.getSoAdVersionInfoApi())
            self.write_bool_cell(sheet, row, 9, general.getSoAdTlsEnabled())
            self.write_bool_cell(sheet, row, 10, general.getSoAdEnableSecurityEventReporting())
            row += 1

        self.auto_width(sheet)

    def write_soad_routing_groups(self, doc: EBModel):
        """Write SoAd routing group configurations sheet."""
        sheet = self.wb.create_sheet("SoAdRoutingGroup", 1)

        title_row = ["Name", "RoutingGroupId"]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getSoAd().getSoAdRoutingGroupList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_cell_center(sheet, row, 2, cfg.getSoAdRoutingGroupId())
            row += 1

        self.auto_width(sheet)

    def write_soad_pdu_routes(self, doc: EBModel):
        """Write SoAd PDU route configurations sheet."""
        sheet = self.wb.create_sheet("SoAdPduRoute", 2)

        title_row = [
            "Name", "TxPduId", "TxUpperLayerType", "SkipIfTxConfirmation",
            "PduHeaderEnable", "ResourceManagementEnable",
            "TxPduHeaderId", "TxUdpTriggerMode", "TxUdpTriggerTimeout",
            "TxSocketConnOrSocketConnBundleRef"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        for route in doc.getSoAd().getSoAdPduRouteList():
            self.write_cell(sheet, row, 1, route.getName())
            self.write_cell_center(sheet, row, 2, route.getSoAdTxPduId())
            self.write_cell(sheet, row, 3, route.getSoAdTxUpperLayerType())
            self.write_bool_cell(sheet, row, 4, route.getSoAdSkipIfTxConfirmation())
            self.write_bool_cell(sheet, row, 5, route.getSoAdPduHeaderEnable())
            self.write_bool_cell(sheet, row, 6, route.getSoAdResourceManagementEnable())
            if route.getSoAdPduRouteDest() is not None:
                dest = route.getSoAdPduRouteDest()
                self.write_cell_center(sheet, row, 7, dest.getSoAdTxPduHeaderId())
                self.write_cell(sheet, row, 8, dest.getSoAdTxUdpTriggerMode())
                self.write_cell(sheet, row, 9, dest.getSoAdTxUdpTriggerTimeout())
                if dest.getSoAdTxSocketConnOrSocketConnBundleRef() is not None:
                    self.write_cell(sheet, row, 10, dest.getSoAdTxSocketConnOrSocketConnBundleRef().getShortName())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """Write SoAd configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_soad_general(doc)
        self.write_soad_routing_groups(doc)
        self.write_soad_pdu_routes(doc)

        self.save(filename)
