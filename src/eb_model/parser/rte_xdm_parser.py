import xml.etree.ElementTree as ET

from ..models.rte_xdm import Rte, RteBswEventToTaskMapping, RteBswEventToTaskMappingV3, RteBswEventToTaskMappingV4, RteBswModuleInstance
from ..models.rte_xdm import RteEventToTaskMapping, RteEventToTaskMappingV3, RteEventToTaskMappingV4, RteSwComponentInstance
from ..models.eb_doc import EBModel
from ..parser.eb_parser import AbstractEbModelParser


class RteXdmParser(AbstractEbModelParser):
    def __init__(self, ) -> None:
        super().__init__()
        self.rte = None

    def parse(self, element: ET.Element, doc: EBModel):
        if self.get_component_name(element) != "Rte":
            raise ValueError("Invalid <%s> xdm file" % "Rte")
        
        rte = doc.getRte()
        self.read_version(element, rte)

        self.logger.info("Parse Rte ARVersion:<%s> SwVersion:<%s>" % (rte.getArVersion().getVersion(), rte.getSwVersion().getVersion()))
        self.rte = rte

        self.read_rte_bsw_module_instances(element, rte)
        self.read_rte_sw_component_instances(element, rte)

    def read_rte_bsw_module_instance_event_to_task_mappings(self, element: ET.Element, instance: RteBswModuleInstance):
        for ctr_tag in self.find_ctr_tag_list(element, "RteBswEventToTaskMapping"):
            self.logger.debug("Read RteBswEventToTaskMapping <%s>" % ctr_tag.attrib['name'])

            if self.rte.getArVersion().getMajorVersion() >= 4:
                mapping = RteBswEventToTaskMappingV4(instance, ctr_tag.attrib['name'])
            else:
                mapping = RteBswEventToTaskMappingV3(instance, ctr_tag.attrib['name'])

            mapping.setRteBswActivationOffset(self.read_optional_value(ctr_tag, "RteBswActivationOffset")) \
                .setRteBswEventPeriod(self.read_optional_value(ctr_tag, "RteBswPeriod")) \
                .setRteBswPositionInTask(self.read_optional_value(ctr_tag, "RteBswPositionInTask")) \
                .setRteBswServerQueueLength(self.read_optional_value(ctr_tag, "RteBswServerQueueLength"))
            
            if isinstance(mapping, RteBswEventToTaskMappingV4):
                for resource_ref in self.read_ref_value_list(ctr_tag, "RteBswEventRef"):
                    mapping.addRteBswEventRef(resource_ref)
            elif isinstance(mapping, RteBswEventToTaskMappingV3):
                mapping.setRteBswEventRef(self.read_ref_value(ctr_tag, "RteBswEventRef"))

            mapping.setRteBswMappedToTaskRef(self.read_optional_ref_value(ctr_tag, "RteBswMappedToTaskRef"))
            instance.addRteBswEventToTaskMapping(mapping)
        
    def read_rte_bsw_module_instances(self, element: ET.Element, rte: Rte):
        for ctr_tag in self.find_ctr_tag_list(element, 'RteBswModuleInstance'):
            self.logger.debug("Read RteBswModuleInstance <%s>" % ctr_tag.attrib['name'])

            instance = RteBswModuleInstance(rte, ctr_tag.attrib['name'])
            instance.setRteBswImplementationRef(self.read_ref_value(ctr_tag, "RteBswImplementationRef")) \
                .setRteMappedToOsApplicationRef(self.read_optional_ref_value(ctr_tag, "RteMappedToOsApplicationRef"))
            
            self.read_rte_bsw_module_instance_event_to_task_mappings(ctr_tag, instance)
            rte.addRteBswModuleInstance(instance)

    def read_rte_sw_component_instance_event_to_task_mappings(self, element: ET.Element, instance: RteSwComponentInstance):
        for ctr_tag in self.find_ctr_tag_list(element, "RteEventToTaskMapping"):
            
            if self.rte.getArVersion().getMajorVersion() >= 4:
                mapping = RteEventToTaskMappingV4(instance, ctr_tag.attrib['name'])
            else:
                mapping = RteEventToTaskMappingV3(instance, ctr_tag.attrib['name'])

            mapping.setRteActivationOffset(self.read_optional_value(ctr_tag, "RteActivationOffset")) \
                .setRtePeriod(self.read_optional_value(ctr_tag, "RtePeriod")) \
                .setRtePositionInTask(self.read_optional_value(ctr_tag, "RtePositionInTask")) \
                .setRteServerQueueLength(self.read_optional_value(ctr_tag, "RteServerQueueLength"))
            
            if isinstance(mapping, RteEventToTaskMappingV4):
                for resource_ref in self.read_ref_value_list(ctr_tag, "RteEventRef"):
                    mapping.addRteEventRef(resource_ref)
            elif isinstance(mapping, RteEventToTaskMappingV3):
                mapping.setRteEventRef(self.read_ref_value(ctr_tag, "RteEventRef"))

            mapping.setRteMappedToTaskRef(self.read_optional_ref_value(ctr_tag, "RteMappedToTaskRef"))

            self.logger.debug("Rte Event %s" % mapping.getRteEventRef().getShortName())
            
            instance.addRteEventToTaskMapping(mapping)

    def read_rte_sw_component_instances(self, element: ET.Element, rte: Rte):
        for ctr_tag in self.find_ctr_tag_list(element, 'RteSwComponentInstance'):
            self.logger.debug("Read RteSwComponentInstance <%s>" % ctr_tag.attrib['name'])

            instance = RteSwComponentInstance(rte, ctr_tag.attrib['name'])
            instance.setMappedToOsApplicationRef(self.read_optional_ref_value(ctr_tag, "MappedToOsApplicationRef")) \
                    .setRteSoftwareComponentInstanceRef(self.read_optional_ref_value(ctr_tag, "RteSoftwareComponentInstanceRef"))
            
            self.read_rte_sw_component_instance_event_to_task_mappings(ctr_tag, instance)
            rte.addRteSwComponentInstance(instance)
