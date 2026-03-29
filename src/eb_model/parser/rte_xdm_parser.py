"""
RTE XDM Parser Module - Extracts AUTOSAR RTE configuration from EB Tresos XDM files.

Implements:
    - SWR_RTE_00001: RTE module parsing
    - SWR_RTE_00002: BSW module instance parsing
    - SWR_RTE_00003: SW component instance parsing
    - SWR_RTE_00004: Event-to-task mapping parsing
"""
import xml.etree.ElementTree as ET

from ..models.rte_xdm import Rte, RteBswEventToTaskMapping, RteBswEventToTaskMappingV3, RteBswEventToTaskMappingV4, RteBswModuleInstance
from ..models.rte_xdm import RteEventToTaskMapping, RteEventToTaskMappingV3, RteEventToTaskMappingV4, RteSwComponentInstance
from ..models.rte_xdm import CommonPublishedInformation, PublishedInformation, RteBswGeneral
from ..models.rte_xdm import RteBswEventToIsrMapping, RteBswExclusiveAreaImpl, RteBswExternalTriggerConfig
from ..models.rte_xdm import RteBswInternalTriggerConfig, RteBswRequiredModeGroupConnection
from ..models.rte_xdm import RteBswRequiredSenderReceiverConnection, RteBswRequiredClientServerConnection
from ..models.rte_xdm import RteBswRequiredTriggerConnection, RteGeneration, ComTaskConfiguration
from ..models.rte_xdm import BswConfiguration, OsCounterAssignments, CooperativeTasks, TaskChain
from ..models.rte_xdm import RteImplicitCommunication, RteInitializationBehavior, RteInitializationRunnableBatch
from ..models.rte_xdm import RteOsInteraction, RteModeToScheduleTableMapping, RteRips, DataMappings
from ..models.rte_xdm import RteExclusiveAreaImplementation, RteExternalTriggerConfig, RteInternalTriggerConfig
from ..models.rte_xdm import RteNvRamAllocation, RteSwComponentType
from ..models.eb_doc import EBModel
from ..parser.eb_parser import AbstractEbModelParser


class RteXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR RTE module configuration from EB Tresos XDM files.

    Extracts RTE configuration including BSW module instances, SW component instances,
    and event-to-task mappings.

    Implements: SWR_RTE_00001 (RTE Module Parser)
    """

    def __init__(self, ) -> None:
        """Initialize the RTE XDM parser."""
        super().__init__()
        self.rte = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse RTE module configuration from XDM element.

        Implements: SWR_RTE_00001
        """
        if self.get_component_name(element) != "Rte":
            raise ValueError("Invalid <%s> xdm file" % "Rte")

        rte = doc.getRte()
        self.read_version(element, rte)

        self.logger.info("Parse Rte ARVersion:<%s> SwVersion:<%s>" % (rte.getArVersion().getVersion(), rte.getSwVersion().getVersion()))
        self.rte = rte

        self.read_common_published_information(element, rte)
        self.read_published_information(element, rte)
        self.read_rte_bsw_general(element, rte)
        self.read_rte_generation(element, rte)
        self.read_com_task_configurations(element, rte)
        self.read_bsw_configurations(element, rte)
        self.read_os_counter_assignments(element, rte)
        self.read_cooperative_tasks(element, rte)
        self.read_task_chains(element, rte)
        self.read_rte_implicit_communication(element, rte)
        self.read_rte_initialization_behavior(element, rte)
        self.read_rte_initialization_runnable_batches(element, rte)
        self.read_rte_os_interaction(element, rte)
        self.read_rte_mode_to_schedule_table_mappings(element, rte)
        self.read_rte_rips(element, rte)
        self.read_data_mappings(element, rte)
        self.read_rte_exclusive_area_implementations(element, rte)
        self.read_rte_external_trigger_configs(element, rte)
        self.read_rte_internal_trigger_configs(element, rte)
        self.read_rte_nv_ram_allocations(element, rte)
        self.read_rte_sw_component_types(element, rte)
        self.read_rte_bsw_module_instances(element, rte)
        self.read_rte_sw_component_instances(element, rte)

    def read_common_published_information(self, element: ET.Element, rte: Rte):
        ctr_tag = self.find_ctr_tag(element, "CommonPublishedInformation")
        if ctr_tag is not None:
            common_info = CommonPublishedInformation(rte, ctr_tag.attrib["name"])
            common_info.setArMajorVersion(self.read_optional_value(ctr_tag, "ArMajorVersion"))
            common_info.setArMinorVersion(self.read_optional_value(ctr_tag, "ArMinorVersion"))
            common_info.setArPatchVersion(self.read_optional_value(ctr_tag, "ArPatchVersion"))
            common_info.setSwMajorVersion(self.read_optional_value(ctr_tag, "SwMajorVersion"))
            common_info.setSwMinorVersion(self.read_optional_value(ctr_tag, "SwMinorVersion"))
            common_info.setSwPatchVersion(self.read_optional_value(ctr_tag, "SwPatchVersion"))
            rte.setCommonPublishedInformation(common_info)
            self.logger.debug("Read CommonPublishedInformation")

    def read_published_information(self, element: ET.Element, rte: Rte):
        ctr_tag = self.find_ctr_tag(element, "PublishedInformation")
        if ctr_tag is not None:
            pub_info = PublishedInformation(rte, ctr_tag.attrib["name"])
            pub_info.setVendorId(self.read_optional_value(ctr_tag, "VendorId"))
            pub_info.setArReleaseMajorVersion(self.read_optional_value(ctr_tag, "ArReleaseMajorVersion"))
            pub_info.setArReleaseMinorVersion(self.read_optional_value(ctr_tag, "ArReleaseMinorVersion"))
            pub_info.setArReleasePatchVersion(self.read_optional_value(ctr_tag, "ArReleasePatchVersion"))
            pub_info.setSwMajorVersion(self.read_optional_value(ctr_tag, "SwMajorVersion"))
            pub_info.setSwMinorVersion(self.read_optional_value(ctr_tag, "SwMinorVersion"))
            pub_info.setSwPatchVersion(self.read_optional_value(ctr_tag, "SwPatchVersion"))
            rte.setPublishedInformation(pub_info)
            self.logger.debug("Read PublishedInformation")

    def read_rte_bsw_general(self, element: ET.Element, rte: Rte):
        ctr_tag = self.find_ctr_tag(element, "RteBswGeneral")
        if ctr_tag is not None:
            bsw_general = RteBswGeneral(rte, ctr_tag.attrib["name"])
            schedule_table_ref = self.read_optional_ref_value(ctr_tag, "RteGenerationScheduleTableRef")
            if schedule_table_ref is not None:
                bsw_general.setRteGenerationScheduleTableRef(schedule_table_ref)
            bsw_general.setRteDevelopmentErrorDetect(self.read_optional_value(ctr_tag, "RteDevelopmentErrorDetect"))
            bsw_general.setRteUseApplConfig(self.read_optional_value(ctr_tag, "RteUseApplConfig"))
            rte.setRteBswGeneral(bsw_general)
            self.logger.debug("Read RteBswGeneral")

    def read_rte_generation(self, element: ET.Element, rte: Rte):
        ctr_tag = self.find_ctr_tag(element, "RteGeneration")
        if ctr_tag is not None:
            generation = RteGeneration(rte, ctr_tag.attrib["name"])
            generation.setRteGenerationConfiguration(self.read_optional_value(ctr_tag, "RteGenerationConfiguration"))
            tool_ref = self.read_optional_ref_value(ctr_tag, "RteGenerationToolRef")
            if tool_ref is not None:
                generation.setRteGenerationToolRef(tool_ref)
            rte.setRteGeneration(generation)
            self.logger.debug("Read RteGeneration")

    def read_com_task_configurations(self, element: ET.Element, rte: Rte):
        for ctr_tag in self.find_ctr_tag_list(element, "ComTaskConfiguration"):
            com_task = ComTaskConfiguration(rte, ctr_tag.attrib["name"])
            task_ref = self.read_optional_ref_value(ctr_tag, "RteComTaskRef")
            if task_ref is not None:
                com_task.setRteComTaskRef(task_ref)
            rte.addComTaskConfiguration(com_task)
            self.logger.debug("Read ComTaskConfiguration <%s>" % com_task.getName())

    def read_bsw_configurations(self, element: ET.Element, rte: Rte):
        for ctr_tag in self.find_ctr_tag_list(element, "BswConfiguration"):
            bsw_config = BswConfiguration(rte, ctr_tag.attrib["name"])
            config_ref = self.read_optional_ref_value(ctr_tag, "RteBswModuleConfigRef")
            if config_ref is not None:
                bsw_config.setRteBswModuleConfigRef(config_ref)
            rte.addBswConfiguration(bsw_config)
            self.logger.debug("Read BswConfiguration <%s>" % bsw_config.getName())

    def read_os_counter_assignments(self, element: ET.Element, rte: Rte):
        for ctr_tag in self.find_ctr_tag_list(element, "OsCounterAssignments"):
            os_counter = OsCounterAssignments(rte, ctr_tag.attrib["name"])
            counter_ref = self.read_optional_ref_value(ctr_tag, "RteOsCounterRef")
            if counter_ref is not None:
                os_counter.setRteOsCounterRef(counter_ref)
            rte.addOsCounterAssignment(os_counter)
            self.logger.debug("Read OsCounterAssignments <%s>" % os_counter.getName())

    def read_cooperative_tasks(self, element: ET.Element, rte: Rte):
        for ctr_tag in self.find_ctr_tag_list(element, "CooperativeTasks"):
            coop_task = CooperativeTasks(rte, ctr_tag.attrib["name"])
            task_ref = self.read_optional_ref_value(ctr_tag, "RteCooperativeTaskRef")
            if task_ref is not None:
                coop_task.setRteCooperativeTaskRef(task_ref)
            rte.addCooperativeTask(coop_task)
            self.logger.debug("Read CooperativeTasks <%s>" % coop_task.getName())

    def read_task_chains(self, element: ET.Element, rte: Rte):
        for ctr_tag in self.find_ctr_tag_list(element, "TaskChain"):
            task_chain = TaskChain(rte, ctr_tag.attrib["name"])
            chain_ref = self.read_optional_ref_value(ctr_tag, "RteTaskChainRef")
            if chain_ref is not None:
                task_chain.setRteTaskChainRef(chain_ref)
            rte.addTaskChain(task_chain)
            self.logger.debug("Read TaskChain <%s>" % task_chain.getName())

    def read_rte_implicit_communication(self, element: ET.Element, rte: Rte):
        ctr_tag = self.find_ctr_tag(element, "RteImplicitCommunication")
        if ctr_tag is not None:
            implicit_comm = RteImplicitCommunication(rte, ctr_tag.attrib["name"])
            implicit_comm.setRteImplicitCommunicationType(self.read_optional_value(ctr_tag, "RteImplicitCommunicationType"))
            rte.setRteImplicitCommunication(implicit_comm)
            self.logger.debug("Read RteImplicitCommunication")

    def read_rte_initialization_behavior(self, element: ET.Element, rte: Rte):
        ctr_tag = self.find_ctr_tag(element, "RteInitializationBehavior")
        if ctr_tag is not None:
            init_behavior = RteInitializationBehavior(rte, ctr_tag.attrib["name"])
            init_behavior.setRteInitializationBehavior(self.read_optional_value(ctr_tag, "RteInitializationBehavior"))
            rte.setRteInitializationBehavior(init_behavior)
            self.logger.debug("Read RteInitializationBehavior")

    def read_rte_initialization_runnable_batches(self, element: ET.Element, rte: Rte):
        for ctr_tag in self.find_ctr_tag_list(element, "RteInitializationRunnableBatch"):
            init_batch = RteInitializationRunnableBatch(rte, ctr_tag.attrib["name"])
            runnable_ref = self.read_optional_ref_value(ctr_tag, "RteInitializationRunnableRef")
            if runnable_ref is not None:
                init_batch.setRteInitializationRunnableRef(runnable_ref)
            rte.addRteInitializationRunnableBatch(init_batch)
            self.logger.debug("Read RteInitializationRunnableBatch <%s>" % init_batch.getName())

    def read_rte_os_interaction(self, element: ET.Element, rte: Rte):
        ctr_tag = self.find_ctr_tag(element, "RteOsInteraction")
        if ctr_tag is not None:
            os_interaction = RteOsInteraction(rte, ctr_tag.attrib["name"])
            os_interaction.setRteOsInteractionType(self.read_optional_value(ctr_tag, "RteOsInteractionType"))
            rte.setRteOsInteraction(os_interaction)
            self.logger.debug("Read RteOsInteraction")

    def read_rte_mode_to_schedule_table_mappings(self, element: ET.Element, rte: Rte):
        for ctr_tag in self.find_ctr_tag_list(element, "RteModeToScheduleTableMapping"):
            mode_mapping = RteModeToScheduleTableMapping(rte, ctr_tag.attrib["name"])
            mode_ref = self.read_optional_ref_value(ctr_tag, "RteModeRef")
            if mode_ref is not None:
                mode_mapping.setRteModeRef(mode_ref)
            schedule_ref = self.read_optional_ref_value(ctr_tag, "RteScheduleTableRef")
            if schedule_ref is not None:
                mode_mapping.setRteScheduleTableRef(schedule_ref)
            rte.addRteModeToScheduleTableMapping(mode_mapping)
            self.logger.debug("Read RteModeToScheduleTableMapping <%s>" % mode_mapping.getName())

    def read_rte_rips(self, element: ET.Element, rte: Rte):
        ctr_tag = self.find_ctr_tag(element, "RteRips")
        if ctr_tag is not None:
            rips = RteRips(rte, ctr_tag.attrib["name"])
            rips.setRteRipsConfiguration(self.read_optional_value(ctr_tag, "RteRipsConfiguration"))
            rte.setRteRips(rips)
            self.logger.debug("Read RteRips")

    def read_data_mappings(self, element: ET.Element, rte: Rte):
        for ctr_tag in self.find_ctr_tag_list(element, "DataMappings"):
            data_mapping = DataMappings(rte, ctr_tag.attrib["name"])
            mapping_ref = self.read_optional_ref_value(ctr_tag, "RteDataMappingRef")
            if mapping_ref is not None:
                data_mapping.setRteDataMappingRef(mapping_ref)
            rte.addDataMapping(data_mapping)
            self.logger.debug("Read DataMappings <%s>" % data_mapping.getName())

    def read_rte_exclusive_area_implementations(self, element: ET.Element, rte: Rte):
        for ctr_tag in self.find_ctr_tag_list(element, "RteExclusiveAreaImplementation"):
            excl_area = RteExclusiveAreaImplementation(rte, ctr_tag.attrib["name"])
            area_ref = self.read_optional_ref_value(ctr_tag, "RteExclusiveAreaRef")
            if area_ref is not None:
                excl_area.setRteExclusiveAreaRef(area_ref)
            excl_area.setRteExclusiveAreaImplementationType(self.read_optional_value(ctr_tag, "RteExclusiveAreaImplementationType"))
            rte.addRteExclusiveAreaImplementation(excl_area)
            self.logger.debug("Read RteExclusiveAreaImplementation <%s>" % excl_area.getName())

    def read_rte_external_trigger_configs(self, element: ET.Element, rte: Rte):
        for ctr_tag in self.find_ctr_tag_list(element, "RteExternalTriggerConfig"):
            ext_trigger = RteExternalTriggerConfig(rte, ctr_tag.attrib["name"])
            trigger_ref = self.read_optional_ref_value(ctr_tag, "RteExternalTriggerRef")
            if trigger_ref is not None:
                ext_trigger.setRteExternalTriggerRef(trigger_ref)
            rte.addRteExternalTriggerConfig(ext_trigger)
            self.logger.debug("Read RteExternalTriggerConfig <%s>" % ext_trigger.getName())

    def read_rte_internal_trigger_configs(self, element: ET.Element, rte: Rte):
        for ctr_tag in self.find_ctr_tag_list(element, "RteInternalTriggerConfig"):
            int_trigger = RteInternalTriggerConfig(rte, ctr_tag.attrib["name"])
            trigger_ref = self.read_optional_ref_value(ctr_tag, "RteInternalTriggerRef")
            if trigger_ref is not None:
                int_trigger.setRteInternalTriggerRef(trigger_ref)
            rte.addRteInternalTriggerConfig(int_trigger)
            self.logger.debug("Read RteInternalTriggerConfig <%s>" % int_trigger.getName())

    def read_rte_nv_ram_allocations(self, element: ET.Element, rte: Rte):
        for ctr_tag in self.find_ctr_tag_list(element, "RteNvRamAllocation"):
            nv_alloc = RteNvRamAllocation(rte, ctr_tag.attrib["name"])
            block_ref = self.read_optional_ref_value(ctr_tag, "RteNvRamBlockRef")
            if block_ref is not None:
                nv_alloc.setRteNvRamBlockRef(block_ref)
            rte.addRteNvRamAllocation(nv_alloc)
            self.logger.debug("Read RteNvRamAllocation <%s>" % nv_alloc.getName())

    def read_rte_sw_component_types(self, element: ET.Element, rte: Rte):
        for ctr_tag in self.find_ctr_tag_list(element, "RteSwComponentType"):
            sw_type = RteSwComponentType(rte, ctr_tag.attrib["name"])
            type_ref = self.read_optional_ref_value(ctr_tag, "RteSwComponentTypeRef")
            if type_ref is not None:
                sw_type.setRteSwComponentTypeRef(type_ref)
            rte.addRteSwComponentType(sw_type)
            self.logger.debug("Read RteSwComponentType <%s>" % sw_type.getName())

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

            # Read new missing attributes
            instance.setRteBswModuleInitRef(self.read_optional_ref_value(ctr_tag, "RteBswModuleInitRef"))
            instance.setRteBswModuleDeinitRef(self.read_optional_ref_value(ctr_tag, "RteBswModuleDeinitRef"))
            instance.setRteBswComponentTypeRef(self.read_optional_ref_value(ctr_tag, "RteBswComponentTypeRef"))
            instance.setRteBswProvideModeSwitchFunctions(self.read_optional_value(ctr_tag, "RteBswProvideModeSwitchFunctions"))
            instance.setRteBswInitFunction(self.read_optional_ref_value(ctr_tag, "RteBswInitFunction"))
            instance.setRteBswDeinitFunction(self.read_optional_ref_value(ctr_tag, "RteBswDeinitFunction"))
            instance.setRteBswModuleVariableLocking(self.read_optional_value(ctr_tag, "RteBswModuleVariableLocking"))
            instance.setRteBswModuleInterfaceLocking(self.read_optional_value(ctr_tag, "RteBswModuleInterfaceLocking"))
            instance.setRteBswModuleLocalDataLocking(self.read_optional_value(ctr_tag, "RteBswModuleLocalDataLocking"))
            instance.setRteBswModuleInterModuleDataLocking(self.read_optional_value(ctr_tag, "RteBswModuleInterModuleDataLocking"))
            instance.setRteBswModuleNvmDataLocking(self.read_optional_value(ctr_tag, "RteBswModuleNvmDataLocking"))
            instance.setRteBswModuleEnableModeSwitch(self.read_optional_value(ctr_tag, "RteBswModuleEnableModeSwitch"))
            instance.setRteBswModuleEnableRouting(self.read_optional_value(ctr_tag, "RteBswModuleEnableRouting"))
            instance.setRteBswModuleEnableSequencing(self.read_optional_value(ctr_tag, "RteBswModuleEnableSequencing"))
            instance.setRteBswModuleTimeoutMonitoring(self.read_optional_value(ctr_tag, "RteBswModuleTimeoutMonitoring"))
            instance.setRteBswModuleErrorHandling(self.read_optional_value(ctr_tag, "RteBswModuleErrorHandling"))
            instance.setRteBswModuleDefaultMonitoring(self.read_optional_value(ctr_tag, "RteBswModuleDefaultMonitoring"))
            instance.setRteBswModuleProvideComponentMonitoring(self.read_optional_value(ctr_tag, "RteBswModuleProvideComponentMonitoring"))
            instance.setRteBswModuleTimingProtection(self.read_optional_value(ctr_tag, "RteBswModuleTimingProtection"))
            instance.setRteBswModuleResourceManagement(self.read_optional_value(ctr_tag, "RteBswModuleResourceManagement"))
            instance.setRteBswModuleScheduling(self.read_optional_value(ctr_tag, "RteBswModuleScheduling"))

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

            # Read new missing attributes
            instance.setRteActivationOffset(self.read_optional_value(ctr_tag, "RteActivationOffset"))
            instance.setRtePeriod(self.read_optional_value(ctr_tag, "RtePeriod"))
            instance.setRteImmediateRestart(self.read_optional_value(ctr_tag, "RteImmediateRestart"))
            instance.setRteNvmRamBlockLocationSymbol(self.read_optional_value(ctr_tag, "RteNvRamBlockLocationSymbol"))
            instance.setRteInitRunnableRef(self.read_optional_ref_value(ctr_tag, "RteInitRunnableRef"))
            instance.setRteCommunicationErrorHandling(self.read_optional_value(ctr_tag, "RteCommunicationErrorHandling"))
            instance.setRteDataConsistency(self.read_optional_value(ctr_tag, "RteDataConsistency"))
            instance.setRteDataUpdate(self.read_optional_value(ctr_tag, "RteDataUpdate"))
            instance.setRteMessageSending(self.read_optional_value(ctr_tag, "RteMessageSending"))
            instance.setRteMessageReception(self.read_optional_value(ctr_tag, "RteMessageReception"))
            instance.setRteComponentInstanceVariableLocking(
                self.read_optional_value(ctr_tag, "RteComponentInstanceVariableLocking"))
            instance.setRteComponentInstanceLocalDataLocking(
                self.read_optional_value(ctr_tag, "RteComponentInstanceLocalDataLocking"))
            instance.setRteComponentInstanceInterInstanceDataLocking(
                self.read_optional_value(ctr_tag, "RteComponentInstanceInterInstanceDataLocking"))

            self.read_rte_sw_component_instance_event_to_task_mappings(ctr_tag, instance)
            rte.addRteSwComponentInstance(instance)
