from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class TcpIpXdmXlsWriter(ExcelReporter):
    """Excel reporter for TcpIp module configuration."""
    def __init__(self) -> None:
        super().__init__()

    def write_tcpip_general(self, doc: EBModel):
        """Write TcpIp general configuration sheet."""
        sheet = self.wb.create_sheet("TcpIpGeneral", 0)

        title_row = [
            "Name", "DevErrorDetect", "MainFunctionPeriod",
            "BufferSizeMax", "MaxNumOfSockets"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getTcpIp().getTcpIpGeneral() is not None:
            general = doc.getTcpIp().getTcpIpGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getTcpIpDevErrorDetect())
            self.write_cell(sheet, row, 3, general.getTcpIpMainFunctionPeriod())
            self.write_cell_center(sheet, row, 4, general.getTcpIpBufferSizeMax())
            self.write_cell_center(sheet, row, 5, general.getTcpIpMaxNumOfSockets())
            row += 1

        self.auto_width(sheet)

    def write_tcpip_ctrls(self, doc: EBModel):
        """Write TcpIp controller configurations sheet."""
        sheet = self.wb.create_sheet("TcpIpCtrl", 1)

        title_row = [
            "Name", "EthIfCtrlRef", "DhcpServerConfigRef",
            "IpV4PathMtuEnabled", "IpV4PathMtuTimeout",
            "IpV6PathMtuEnabled", "IpV6PathMtuTimeout"
        ]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getTcpIp().getTcpIpCtrlList():
            self.write_cell(sheet, row, 1, cfg.getName())
            if cfg.getTcpIpEthIfCtrlRef() is not None:
                self.write_cell(sheet, row, 2, cfg.getTcpIpEthIfCtrlRef().getShortName())
            if cfg.getTcpIpDhcpServerConfigRef() is not None:
                self.write_cell(sheet, row, 3, cfg.getTcpIpDhcpServerConfigRef().getShortName())
            if cfg.getTcpIpIpV4Ctrl() is not None:
                self.write_bool_cell(sheet, row, 4, cfg.getTcpIpIpV4Ctrl().getTcpIpIpV4PathMtuEnabled())
                self.write_cell(sheet, row, 5, cfg.getTcpIpIpV4Ctrl().getTcpIpIpV4PathMtuTimeout())
            if cfg.getTcpIpIpV6Ctrl() is not None:
                self.write_bool_cell(sheet, row, 6, cfg.getTcpIpIpV6Ctrl().getTcpIpIpV6PathMtuEnabled())
                self.write_cell(sheet, row, 7, cfg.getTcpIpIpV6Ctrl().getTcpIpIpV6PathMtuTimeout())
            row += 1

        self.auto_width(sheet)

    def write_tcpip_local_addrs(self, doc: EBModel):
        """Write TcpIp local address configurations sheet."""
        sheet = self.wb.create_sheet("TcpIpLocalAddr", 2)

        title_row = ["Name", "AddrId", "AddressType", "DomainType"]
        self.write_title_row(sheet, title_row)

        row = 2
        for cfg in doc.getTcpIp().getTcpIpLocalAddrList():
            self.write_cell(sheet, row, 1, cfg.getName())
            self.write_cell_center(sheet, row, 2, cfg.getTcpIpAddrId())
            self.write_cell(sheet, row, 3, cfg.getTcpIpAddressType())
            self.write_cell(sheet, row, 4, cfg.getTcpIpDomainType())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        """Write TcpIp configuration to Excel file."""
        self.logger.info("Writing <%s>" % filename)

        self.write_tcpip_general(doc)
        self.write_tcpip_ctrls(doc)
        self.write_tcpip_local_addrs(doc)

        self.save(filename)
