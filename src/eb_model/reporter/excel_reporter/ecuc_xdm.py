from ...models.core.rte_xdm import RteBswEventToTaskMapping, RteBswEventToTaskMappingV3, RteBswEventToTaskMappingV4, RteBswModuleInstance
from ...models.core.rte_xdm import RteEventToTaskMapping, RteEventToTaskMappingV3, RteEventToTaskMappingV4, RteSwComponentInstance
from ...models.core.eb_doc import EBModel
from .abstract import ExcelReporter


class EcucXdmXlsWriter(ExcelReporter):
    def __init__(self) -> None:
        super().__init__()

    def write_ecuc_partition_collection(self, doc: EBModel):
        sheet = self.wb.create_sheet("EcucPartition", 0)

        title_row = ["EcucPartition", "PartitionCanBeRestarted", "EcucPartitionRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for partition in doc.getEcuC().getEcucPartitionCollection().getEcucPartitions():
            self.write_cell(sheet, row, 1, partition.getName())
            self.write_cell(sheet, row, 2, partition.getEcucPartitionCanBeRestarted())
            if partition.getEcucPartitionRef() is not None:
                self.write_cell(sheet, row, 3, partition.getEcucPartitionRef().getShortName())

            row += 1

        self.auto_width(sheet)

    def write_ecuc_partition_software_component_instances(self, doc: EBModel):
        sheet = self.wb.create_sheet("SoftwareComponent", 1)

        title_row = ["Instance", "EcucPartition"]
        self.write_title_row(sheet, title_row)

        row = 2
        for partition in doc.getEcuC().getEcucPartitionCollection().getEcucPartitions():
            for instance in partition.getEcucPartitionSoftwareComponentInstanceRefs():
                if instance.getEcucPartitionSoftwareComponentInstanceTargetRef() is not None:
                    self.write_cell(sheet, row, 1, instance.getEcucPartitionSoftwareComponentInstanceTargetRef().getValue())
                    self.write_cell(sheet, row, 2, partition.getName())

                    row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel):
        self.logger.info("Writing <%s>" % filename)

        self.write_ecuc_partition_collection(doc)
        self.write_ecuc_partition_software_component_instances(doc)

        self.save(filename)
