from typing import List, Dict
import xml.etree.ElementTree as ET
import re

from ..models.abstract import EcucContainer, EcucObject
from ..models.eb_doc import EBModel
from ..models.os_xdm import Os, OsApplication, OsCounter, OsResource, OsTask, OsIsr
from .eb_parser import EBModelParser

class OsXdmParser(EBModelParser):
    def __init__(self, ) -> None:
        super().__init__()

    def parse(self, filename: str, doc: EBModel):
        self._read_namespaces(filename)
        tree = ET.parse(filename)
        self.root_tag = tree.getroot()
        self.validate_root(self.root_tag)

        self.read_os_tasks(doc.getOs())
        self.read_os_isrs(doc.getOs())

    def read_os_tasks(self, os: Os):
        for ctr_tag in self.find_ctr_tag_list(self.root_tag, 'OsTask'):
            os_task = OsTask()
            os_task.setName(ctr_tag.attrib['name']) \
                .setOsTaskPriority(self.read_value(ctr_tag, "OsTaskPriority")) \
                .setOsTaskActivation(self.read_value(ctr_tag, "OsTaskActivation")) \
                .setOsTaskSchedule(self.read_value(ctr_tag, "OsTaskSchedule")) \
                .setOsStacksize(self.read_optional_value(ctr_tag, "OsStacksize", 0))
            os.addOsTask(os_task)
    
    def read_os_isrs(self, os: Os):
        for ctr_tag in self.find_ctr_tag_list(self.root_tag, 'OsIsr'):
            os_isr = OsIsr()
            os_isr.setName(ctr_tag.attrib['name']) \
                .setOsIsrCategory(self.read_value(ctr_tag, "OsIsrCategory")) \
                .setOsIsrPeriod(self.read_optional_value(ctr_tag, "OsIsrPeriod", 0.0)) \
                .setOsStacksize(self.read_value(ctr_tag, "OsStacksize")) \
                .setOsIsrPriority(self.read_optional_value(ctr_tag, "OsIsrPriority"))

            os.addOsIsr(os_isr)
    