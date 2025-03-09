from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class NvMXdmXlsWriter(ExcelReporter):
    def __init__(self) -> None:
        super().__init__()

    def write_nvm_block_descriptors(self, doc: EBModel):
        sheet = self.wb.create_sheet("NvMBlock", 0)

        title_row = [
            "BlockId", "Name", "NvMBlockEcucPartitionRef", "NvMRamBlockDataAddress", "NvMRomBlockDataAddress",
            "NvMBlockManagementType", "NvMNvBlockLength", "NvMNvBlockNum", "NvMSelectBlockForReadAll", "NvMSelectBlockForWriteAll"]
        self.write_title_row(sheet, title_row)

        row = 2
        for nvm_block in doc.getNvM().getNvMBlockDescriptorList():
            self.write_cell(sheet, row, 1, nvm_block.getNvMNvramBlockIdentifier())
            self.write_cell(sheet, row, 2, nvm_block.getName())
            self.write_cell(sheet, row, 3, nvm_block.getNvMBlockEcucPartitionRef())
            self.write_cell(sheet, row, 4, nvm_block.getNvMRamBlockDataAddress())
            self.write_cell(sheet, row, 5, nvm_block.getNvMRomBlockDataAddress())
            self.write_cell(sheet, row, 6, nvm_block.getNvMBlockManagementType())
            self.write_cell(sheet, row, 7, nvm_block.getNvMNvBlockLength())
            self.write_cell(sheet, row, 8, nvm_block.getNvMNvBlockNum())

            
            row += 1

            self.logger.debug("Write NvM Block <%s>" % nvm_block.getName())

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options):
        self.logger.info("Writing <%s>" % filename)

        self.write_nvm_block_descriptors(doc)

        self.save(filename)
