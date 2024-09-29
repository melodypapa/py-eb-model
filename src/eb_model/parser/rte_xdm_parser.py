import xml.etree.ElementTree as ET

from ..models.rte_xdm import Rte, RteBswEventToTaskMapping, RteBswModuleInstance, RteEventToTaskMapping, RteSwComponentInstance
from ..models.eb_doc import EBModel
from .eb_parser import AbstractEbModelParser


class RteXdmParser(AbstractEbModelParser):
    def __init__(self, ) -> None:
        super().__init__()

    def parse(self, element: ET.Element, doc: EBModel):
        if self.get_component_name(element) != "Rte":
            raise ValueError("Invalid <%s> xdm file" % "Rte")
        
        self.read_rte_bsw_module_instances(element, doc.getRte())
        self.read_rte_sw_component_instances(element, doc.getRte())

    def read_rte_bsw_module_instance_event_to_task_mappings(self, element: ET.Element, instance: RteBswModuleInstance):
        for ctr_tag in self.find_ctr_tag_list(element, "RteBswEventToTaskMapping"):
            mapping = RteBswEventToTaskMapping(instance, ctr_tag.attrib['name'])
            mapping.setRteBswActivationOffset(self.read_optional_value(ctr_tag, "RteBswActivationOffset")) \
                .setRteBswEventPeriod(self.read_optional_value(ctr_tag, "RteBswPeriod")) \
                .setRteBswPositionInTask(self.read_optional_value(ctr_tag, "RteBswPositionInTask")) \
                .setRteBswServerQueueLength(self.read_optional_value(ctr_tag, "RteBswServerQueueLength")) \
                .setRteBswEventRef(self.read_ref_value(ctr_tag, "RteBswEventRef")) \
                .setRteBswMappedToTaskRef(self.read_optional_ref_value(ctr_tag, "RteBswMappedToTaskRef"))
            instance.addRteBswEventToTaskMapping(mapping)
        
    def read_rte_bsw_module_instances(self, element: ET.Element, rte: Rte):
        for ctr_tag in self.find_ctr_tag_list(element, 'RteBswModuleInstance'):
            instance = RteBswModuleInstance(rte, ctr_tag.attrib['name'])
            instance.setRteBswImplementationRef(self.read_ref_value(ctr_tag, "RteBswImplementationRef")) \
                .setRteMappedToOsApplicationRef(self.read_optional_ref_value(ctr_tag, "RteMappedToOsApplicationRef"))

            self.read_rte_bsw_module_instance_event_to_task_mappings(ctr_tag, instance)
            
            self.logger.debug("Add the RteBswModuleInstance <%s>" % instance.getName())

            rte.addRteBswModuleInstance(instance)

    def read_rte_sw_component_instance_event_to_task_mappings(self, element: ET.Element, instance: RteSwComponentInstance):
        for ctr_tag in self.find_ctr_tag_list(element, "RteEventToTaskMapping"):
            mapping = RteEventToTaskMapping(instance, ctr_tag.attrib['name'])
            mapping.setRteActivationOffset(self.read_optional_value(ctr_tag, "RteActivationOffset")) \
                .setRtePeriod(self.read_optional_value(ctr_tag, "RtePeriod")) \
                .setRtePositionInTask(self.read_optional_value(ctr_tag, "RtePositionInTask")) \
                .setRteServerQueueLength(self.read_optional_value(ctr_tag, "RteServerQueueLength")) \
                .setRteEventRef(self.read_ref_value(ctr_tag, "RteEventRef")) \
                .setRteMappedToTaskRef(self.read_optional_ref_value(ctr_tag, "RteMappedToTaskRef"))
            
            instance.addRteEventToTaskMapping(mapping)

    def read_rte_sw_component_instances(self, element: ET.Element, rte: Rte):
        for ctr_tag in self.find_ctr_tag_list(element, 'RteSwComponentInstance'):
            instance = RteSwComponentInstance(rte, ctr_tag.attrib['name'])
            instance.setMappedToOsApplicationRef(self.read_optional_ref_value(ctr_tag, "MappedToOsApplicationRef")) \
                .setRteSoftwareComponentInstanceRef(self.read_optional_ref_value(ctr_tag, "RteSoftwareComponentInstanceRef"))
            
            self.read_rte_sw_component_instance_event_to_task_mappings(ctr_tag, instance)
            
            self.logger.debug("Add the RteSwComponentInstance <%s>" % instance.getName())

            rte.addRteSwComponentInstance(instance)