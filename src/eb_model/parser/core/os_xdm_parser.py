"""
OS XDM Parser Module - Extracts AUTOSAR OS configuration from EB Tresos XDM files.

Implements:
    - SWR_OS_00001: OS module parsing
    - SWR_OS_00002: Task parsing (OsTask)
    - SWR_OS_00003: ISR parsing (OsIsr)
    - SWR_OS_00004: Alarm parsing (OsAlarm)
    - SWR_OS_00005: Schedule table parsing (OsScheduleTable)
    - SWR_OS_00006: Counter parsing (OsCounter)
    - SWR_OS_00007: Application parsing (OsApplication)
    - SWR_OS_00008: Resource parsing (OsResource)
    - SWR_OS_00009: Microkernel parsing (OsMicrokernel)
"""
import xml.etree.ElementTree as ET
from ...models.core.eb_doc import EBModel
from ...models.core.os_xdm import Os, OsAlarm, OsAlarmActivateTask, OsAlarmCallback
from ...models.core.os_xdm import OsAlarmIncrementCounter, OsAlarmSetEvent, OsCounter, OsResource
from ...models.core.os_xdm import CommonPublishedInformation, PublishedInformation, OsHwIncrementer
from ...models.core.os_xdm import OsEvent, OsSpinlock, OsPeripheralArea, OsOS, OsHooks
from ...models.core.os_xdm import OsCoreConfig, OsAutosarCustomization
from ...models.core.os_xdm import OsScheduleTable
from ...models.core.os_xdm import OsTask, OsIsr, OsApplication, OsScheduleTableEventSetting
from ...models.core.os_xdm import OsScheduleTableExpiryPoint, OsScheduleTableTaskActivation
from ...models.core.os_xdm import OsScheduleTblAdjustableExpPoint, OsTaskAutostart
from ...models.core.os_xdm import OsMicrokernel, MkMemoryProtection, MkMemoryRegion
from .eb_parser import AbstractEbModelParser


class OsXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR OS module configuration from EB Tresos XDM files.

    Extracts OS configuration including tasks, ISRs, alarms, schedule tables,
    counters, applications, resources, and microkernel settings.

    Implements: SWR_OS_00001 (OS Module Parser)
    """

    def __init__(self, ) -> None:
        """Initialize the OS XDM parser."""
        super().__init__()

        self.os = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse OS module configuration from XDM element.

        Implements: SWR_OS_00001
        """
        if self.get_component_name(element) != "Os":
            raise ValueError("Invalid <%s> xdm file" % "Os")

        os = doc.getOs()

        self.read_version(element, os)

        self.logger.info("Parse Os ARVersion:<%s> SwVersion:<%s>" % (os.getArVersion().getVersion(), os.getSwVersion().getVersion()))

        self.os = os

        self.read_os_tasks(element, os)
        self.read_os_isrs(element, os)
        self.read_os_alarms(element, os)
        self.read_os_schedule_tables(element, os)
        self.read_os_counters(element, os)
        self.read_os_applications(element, os)
        self.read_os_resources(element, os)
        self.read_os_microkernel(element, os)
        self.read_common_published_information(element, os)
        self.read_published_information(element, os)
        self.read_os_hw_incrementer(element, os)
        self.read_os_events(element, os)
        self.read_os_spinlocks(element, os)
        self.read_os_peripheral_areas(element, os)
        self.read_os_os(element, os)
        self.read_os_hooks(element, os)
        self.read_os_core_configs(element, os)
        self.read_os_autosar_customization(element, os)

    def read_os_task_autostart(self, element: ET.Element, os_task: OsTask):
        """Parse OsTaskAutostart configuration for a task."""
        ctr_tag = self.find_ctr_tag(element, "OsTaskAutostart")
        if ctr_tag is not None:
            autostart = OsTaskAutostart(os_task, ctr_tag.attrib["name"])
            for app_mode_ref in self.read_ref_value_list(ctr_tag, "OsTaskAppModeRef"):
                autostart.addOsTaskAppModeRef(app_mode_ref)
            os_task.setOsTaskAutostart(autostart)

    def read_os_tasks(self, element: ET.Element, os: Os):
        """
        Parse all OsTask containers from XDM.

        Implements: SWR_OS_00002 (Task parsing)
        """
        for ctr_tag in self.find_ctr_tag_list(element, "OsTask"):
            os_task = OsTask(os, ctr_tag.attrib["name"])
            os_task.setOsTaskPriority(int(self.read_value(ctr_tag, "OsTaskPriority")))
            os_task.setOsTaskActivation(self.read_value(ctr_tag, "OsTaskActivation"))
            os_task.setOsTaskSchedule(self.read_value(ctr_tag, "OsTaskSchedule"))
            os_task.setOsTaskType(self.read_optional_value(ctr_tag, "OsTaskType"))
            os_task.setOsStacksize(int(self.read_value(ctr_tag, "OsStacksize")))
            os_task.setOsMeasureMaxRuntime(self.read_optional_value(ctr_tag, "OsMeasure_Max_Runtime"))
            os_task.setOsTaskUseHwFp(self.read_optional_value(ctr_tag, "OsTaskUse_Hw_Fp"))
            os_task.setOsTaskCallScheduler(self.read_optional_value(ctr_tag, "OsTaskCallScheduler"))

            for resource_ref in self.read_ref_value_list(ctr_tag, "OsTaskResourceRef"):
                os_task.addOsTaskResourceRef(resource_ref)

            self.read_os_task_autostart(ctr_tag, os_task)

            self.logger.debug("Read OsTask <%s>" % os_task.getName())
            os.addOsTask(os_task)

    def read_os_isrs(self, element: ET.Element, os: Os):
        """
        Parse all OsIsr containers from XDM.

        Implements: SWR_OS_00003 (ISR parsing)
        """
        for ctr_tag in self.find_ctr_tag_list(element, "OsIsr"):
            os_isr = OsIsr(os, ctr_tag.attrib["name"])
            os_isr.setOsIsrCategory(self.read_value(ctr_tag, "OsIsrCategory"))
            os_isr.setOsIsrPeriod(self.read_optional_value(ctr_tag, "OsIsrPeriod", 0.0))
            os_isr.setOsStacksize(int(self.read_value(ctr_tag, "OsStacksize")))
            os_isr.setOsIsrPriority(self.read_eb_origin_value(ctr_tag, "OsIsrPriority"))
            
            # Infineon Aurix Tricore
            os_isr.setOsIsrPriority(self.read_eb_origin_value(ctr_tag, "OsTricoreIrqLevel"))
            os_isr.setOsIsrVector(self.read_eb_origin_value(ctr_tag, "OsTricoreVector"))
            os_isr.setOsTricoreIrqLevel(self.read_eb_origin_value(ctr_tag, "OsTricoreIrqLevel"))
            os_isr.setOsTricoreVector(self.read_eb_origin_value(ctr_tag, "OsTricoreVector"))
            
            # ARM Core
            os_isr.setOsIsrPriority(self.read_eb_origin_value(ctr_tag, "OsARMIrqLevel"))
            os_isr.setOsIsrVector(self.read_eb_origin_value(ctr_tag, "OsARMVector"))
            os_isr.setOsARMIrqLevel(self.read_eb_origin_value(ctr_tag, "OsARMIrqLevel"))
            os_isr.setOsARMVector(self.read_eb_origin_value(ctr_tag, "OsARMVector"))

            # EB Safety OS
            for ref in self.read_ref_value_list(ctr_tag, "OsIsrMkMemoryRegionRef"):
                os_isr.addOsIsrMkMemoryRegionRef(ref)

            self.logger.debug("Read OsIsr <%s>" % os_isr.getName())
            os.addOsIsr(os_isr)

    def read_os_alarm_action(self, element: ET.Element, os_alarm: OsAlarm):
        """Parse OsAlarmAction choice and create appropriate action object."""
        chc = self.read_choice_value(element, "OsAlarmAction")
        if chc is None:
            raise ValueError("OsAlarmAction is required.")
        if chc == "OsAlarmActivateTask":
            os_alarm_action = OsAlarmActivateTask(os_alarm, "OsAlarmActivateTask") \
                .setOsAlarmActivateTaskRef(self.read_ref_value(element, "OsAlarmActivateTaskRef"))
        elif chc == "OsAlarmIncrementCounter":
            os_alarm_action = OsAlarmIncrementCounter(os_alarm, "OsAlarmIncrementCounter") \
                .setOsAlarmIncrementCounterRef(self.read_ref_value(element, "OsAlarmIncrementCounterRef"))
        elif chc == "OsAlarmSetEvent":
            os_alarm_action = OsAlarmSetEvent(os_alarm, "OsAlarmSetEvent") \
                .setOsAlarmSetEventRef(self.read_ref_value(element, "OsAlarmSetEventRef")) \
                .setOsAlarmSetEventTaskRef(self.read_ref_value(element, "OsAlarmSetEventTaskRef"))
        elif chc == "OsAlarmCallback":
            os_alarm_action = OsAlarmCallback(os_alarm, "OsAlarmCallback") \
                .setOsAlarmCallbackName(self.read_value(element, "OsAlarmCallbackName"))
        else:
            raise ValueError("Unsupported OsAlarmAction <%s>" % chc)
        os_alarm.setOsAlarmAction(os_alarm_action)

        # Read callback name if available
        os_alarm.setOsAlarmCallbackName(self.read_optional_value(element, "OsAlarmCallbackName"))

    def read_os_alarms(self, element: ET.Element, os: Os):
        """
        Parse all OsAlarm containers from XDM.

        Implements: SWR_OS_00004 (Alarm parsing)
        """
        for ctr_tag in self.find_ctr_tag_list(element, "OsAlarm"):
            os_alarm = OsAlarm(os, ctr_tag.attrib["name"]) \
                .setOsAlarmCounterRef(self.read_ref_value(ctr_tag, "OsAlarmCounterRef"))

            for ref in self.read_ref_value_list(ctr_tag, "OsAlarmAccessingApplication"):
                os_alarm.addOsAlarmAccessingApplicationRef(ref)

            self.read_os_alarm_action(ctr_tag, os_alarm)

            self.logger.debug("Read OsAlarm <%s>" % os_alarm.getName())
            os.addOsAlarm(os_alarm)

    def read_os_schedule_table_event_settings(self, element: ET.Element, expiry_point: OsScheduleTableExpiryPoint):
        """Parse OsScheduleTableEventSetting containers for an expiry point."""
        for ctr_tag in self.find_ctr_tag_list(element, "OsScheduleTableEventSetting"):
            event_setting = OsScheduleTableEventSetting(expiry_point, ctr_tag.attrib["name"]) \
                .setOsScheduleTableSetEventRef(self.read_ref_value(ctr_tag, "OsScheduleTableSetEventRef")) \
                .setOsScheduleTableSetEventTaskRef(self.read_ref_value(ctr_tag, "OsScheduleTableSetEventTaskRef"))

            expiry_point.addOsScheduleTableEventSetting(event_setting)

    def read_os_schedule_table_task_activations(self, element: ET.Element, expiry_point: OsScheduleTableExpiryPoint):
        for ctr_tag in self.find_ctr_tag_list(element, "OsScheduleTableTaskActivation"):
            activation = OsScheduleTableTaskActivation(expiry_point, ctr_tag.attrib["name"]) \
                .setOsScheduleTableActivateTaskRef(self.read_ref_value(ctr_tag, "OsScheduleTableActivateTaskRef"))

            expiry_point.addOsScheduleTableTaskActivation(activation)

    def read_os_schedule_tbl_adjustable_exp_point(self, element: ET.Element, expiry_point: OsScheduleTableExpiryPoint):
        ctr_tag = self.find_ctr_tag(element, "OsScheduleTblAdjustableExpPoint")
        if ctr_tag is not None:
            exp_point = OsScheduleTblAdjustableExpPoint(expiry_point, ctr_tag.attrib["name"]) \
                .setOsScheduleTableMaxLengthen(self.read_ref_value(ctr_tag, "OsScheduleTableMaxLengthen")) \
                .setOsScheduleTableMaxShorten(self.read_ref_value(ctr_tag, "OsScheduleTableMaxShorten"))

            expiry_point.setOsScheduleTblAdjustableExpPoint(exp_point)

    def read_os_schedule_table_expiry_points(self, element: ET.Element, os_schedule_table: OsScheduleTable):
        for ctr_tag in self.find_ctr_tag_list(element, "OsScheduleTableExpiryPoint"):
            expiry_point = OsScheduleTableExpiryPoint(os_schedule_table, ctr_tag.attrib["name"]) \
                .setOsScheduleTblExpPointOffset(self.read_value(ctr_tag, "OsScheduleTblExpPointOffset")) \
            
            self.read_os_schedule_table_event_settings(ctr_tag, expiry_point)
            self.read_os_schedule_table_task_activations(ctr_tag, expiry_point)
            self.read_os_schedule_tbl_adjustable_exp_point(ctr_tag, expiry_point)

            os_schedule_table.addOsScheduleTableExpiryPoint(expiry_point)

    def read_os_schedule_tables(self, element: ET.Element, os: Os):
        """
        Parse all OsScheduleTable containers from XDM.

        Implements: SWR_OS_00005 (Schedule table parsing)
        """
        for ctr_tag in self.find_ctr_tag_list(element, "OsScheduleTable"):
            table = OsScheduleTable(os, ctr_tag.attrib["name"]) \
                .setOsScheduleTableDuration(self.read_value(ctr_tag, "OsScheduleTableDuration")) \
                .setOsScheduleTableRepeating(self.read_value(ctr_tag, "OsScheduleTableRepeating")) \
                .setOsScheduleTableCounterRef(self.read_ref_value(ctr_tag, "OsScheduleTableCounterRef")) \
                .setOsTimeUnit(self.read_optional_value(ctr_tag, "OsTimeUnit"))

            self.read_os_schedule_table_expiry_points(ctr_tag, table)

            self.logger.debug("Read OsScheduleTable <%s>" % table.getName())
            os.addOsScheduleTable(table)

    def read_os_counters(self, element: ET.Element, os: Os):
        """
        Parse all OsCounter containers from XDM.

        Implements: SWR_OS_00006 (Counter parsing)
        """
        for ctr_tag in self.find_ctr_tag_list(element, "OsCounter"):
            counter = OsCounter(os, ctr_tag.attrib["name"]) \
                .setOsCounterMaxAllowedValue(self.read_value(ctr_tag, "OsCounterMaxAllowedValue")) \
                .setOsCounterMinCycle(self.read_value(ctr_tag, "OsCounterMinCycle")) \
                .setOsCounterTicksPerBase(self.read_value(ctr_tag, "OsCounterTicksPerBase")) \
                .setOsCounterType(self.read_optional_value(ctr_tag, "OsCounterType")) \
                .setOsSecondsPerTick(self.read_optional_value(ctr_tag, "OsSecondsPerTick")) \
                .setOsCounterWindowsTimer(self.read_optional_value(ctr_tag, "OsCounterWindowsTimer")) \
                .setOsWindowsIrqLevel(self.read_optional_value(ctr_tag, "OsWindowsIrqLevel")) \
                .setOsConstName(self.read_optional_value(ctr_tag, "OsConstName")) \
                .setOsHwModule(self.read_optional_value(ctr_tag, "OsHwModule"))

            self.logger.debug("Read OsCounter <%s>" % counter.getName())
            os.addOsCounter(counter)

    def read_os_applications(self, element: ET.Element, os: Os):
        """
        Parse all OsApplication containers from XDM.

        Implements: SWR_OS_00007 (Application parsing)
        """
        for ctr_tag in self.find_ctr_tag_list(element, "OsApplication"):
            os_app = OsApplication(os, ctr_tag.attrib["name"])
            os_app.setOsTrusted(self.read_value(ctr_tag, "OsTrusted"))
            os_app.setOsApplicationCoreAssignment(self.read_value(ctr_tag, "OsApplicationCoreAssignment"))
            os_app.setOsAppEcucPartitionRef(self.read_ref_value(ctr_tag, "OsAppEcucPartitionRef"))
            os_app.setOsAppErrorHookStack(self.read_optional_value(ctr_tag, "OsAppErrorHookStack"))
            os_app.setOsAppShutdownHookStack(self.read_optional_value(ctr_tag, "OsAppShutdownHookStack"))
            os_app.setOsAppStartupHookStack(self.read_optional_value(ctr_tag, "OsAppStartupHookStack"))
            os_app.setOsTrustedFunctionName(self.read_optional_value(ctr_tag, "OsTrustedFunctionName"))

            for ref in self.read_ref_value_list(ctr_tag, "OsAppAlarmRef"):
                os_app.addOsAppAlarmRef(ref)

            for ref in self.read_ref_value_list(ctr_tag, "OsAppCounterRef"):
                os_app.addOsAppCounterRefs(ref)

            for ref in self.read_ref_value_list(ctr_tag, "OsAppIsrRef"):
                os_app.addOsAppIsrRef(ref)

            for ref in self.read_ref_value_list(ctr_tag, "OsAppResourceRef"):
                os_app.addOsAppResourceRef(ref)

            for ref in self.read_ref_value_list(ctr_tag, "OsAppScheduleTableRef"):
                os_app.addOsAppScheduleTableRef(ref)

            for ref in self.read_ref_value_list(ctr_tag, "OsAppTaskRef"):
                os_app.addOsAppTaskRef(ref)

            self.logger.debug("Read OsApplication <%s>" % os_app.getName())
            os.addOsApplication(os_app)

    def read_os_resources(self, element: ET.Element, os: Os):
        """
        Parse all OsResource containers from XDM.

        Implements: SWR_OS_00008 (Resource parsing)
        """
        for ctr_tag in self.find_ctr_tag_list(element, "OsResource"):
            os_res = OsResource(os, ctr_tag.attrib["name"])
            os_res.setImporterInfo(self.read_attrib(ctr_tag, "IMPORTER_INFO"))
            os_res.setOsResourceProperty(self.read_value(ctr_tag, "OsResourceProperty"))

            for ref in self.read_ref_value_list(ctr_tag, "OsResourceAccessingApplication"):
                os_res.addOsResourceAccessingApplicationRefs(ref)

            os.addOsResource(os_res)

    def read_mk_memory_regions(self, element: ET.Element, protection: MkMemoryProtection):
        """Parse MkMemoryRegion containers for memory protection."""
        for ctr_tag in self.find_ctr_tag_list(element, "MkMemoryRegion"):
            # self.logger.info("Read MkMemoryRegion %s" % ctr_tag.attrib["name"])
            region = MkMemoryRegion(protection, ctr_tag.attrib["name"])
            region.setMkMemoryRegionFlags(self.read_value(ctr_tag, "MkMemoryRegionFlags"))
            region.setMkMemoryRegionInitialize(self.read_value(ctr_tag, "MkMemoryRegionInitialize"))
            region.setMkMemoryRegionGlobal(self.read_value(ctr_tag, "MkMemoryRegionGlobal"))
            region.setMkMemoryRegionInitThreadAccess(self.read_value(ctr_tag, "MkMemoryRegionInitThreadAccess"))
            region.setMkMemoryRegionIdleThreadAccess(self.read_value(ctr_tag, "MkMemoryRegionIdleThreadAccess"))
            region.setMkMemoryRegionOsThreadAccess(self.read_value(ctr_tag, "MkMemoryRegionOsThreadAccess"))
            region.setMkMemoryRegionErrorHookAccess(self.read_value(ctr_tag, "MkMemoryRegionErrorHookAccess"))
            region.setMkMemoryRegionProtHookAccess(self.read_value(ctr_tag, "MkMemoryRegionProtHookAccess"))
            region.setMkMemoryRegionShutdownHookAccess(self.read_value(ctr_tag, "MkMemoryRegionShutdownHookAccess"))
            region.setMkMemoryRegionShutdownAccess(self.read_value(ctr_tag, "MkMemoryRegionShutdownAccess"))
            region.setMkMemoryRegionInitializePerCore(self.read_value(ctr_tag, "MkMemoryRegionInitializePerCore"))
            protection.addMkMemoryRegion(region)

    def read_mk_memory_protection(self, element: ET.Element, kernel: OsMicrokernel):
        """Parse MkMemoryProtection container for microkernel."""
        ctr_tag = self.find_ctr_tag(element, "MkMemoryProtection")
        if ctr_tag is not None:
            # self.logger.info("Read MkMemoryProtection")
            protection = MkMemoryProtection(kernel, ctr_tag.attrib["name"])
            self.read_mk_memory_regions(ctr_tag, protection)
            kernel.setMkMemoryProtection(protection)

    def read_os_microkernel(self, element: ET.Element, os: Os):
        """
        Parse OsMicrokernel container from XDM.

        Implements: SWR_OS_00009 (Microkernel parsing)
        """
        ctr_tag = self.find_ctr_tag(element, "OsMicrokernel")
        if ctr_tag is not None:
            kernel = OsMicrokernel(os, ctr_tag.attrib["name"])
            self.read_mk_memory_protection(ctr_tag, kernel)
            os.setOsMicrokernel(kernel)

    def read_common_published_information(self, element: ET.Element, os: Os):
        """Parse CommonPublishedInformation container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "CommonPublishedInformation")
        if ctr_tag is not None:
            pub_info = CommonPublishedInformation(os, ctr_tag.attrib["name"])
            pub_info.setArMajorVersion(self.read_value(ctr_tag, "ArMajorVersion"))
            pub_info.setArMinorVersion(self.read_value(ctr_tag, "ArMinorVersion"))
            pub_info.setArPatchVersion(self.read_value(ctr_tag, "ArPatchVersion"))
            pub_info.setSwMajorVersion(self.read_value(ctr_tag, "SwMajorVersion"))
            pub_info.setSwMinorVersion(self.read_value(ctr_tag, "SwMinorVersion"))
            pub_info.setSwPatchVersion(self.read_value(ctr_tag, "SwPatchVersion"))
            os.setCommonPublishedInformation(pub_info)
            self.logger.debug("Read CommonPublishedInformation")

    def read_published_information(self, element: ET.Element, os: Os):
        """Parse PublishedInformation container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "PublishedInformation")
        if ctr_tag is not None:
            pub_info = PublishedInformation(os, ctr_tag.attrib["name"])
            pub_info.setVendorId(self.read_value(ctr_tag, "VendorId"))
            pub_info.setArReleaseMajorVersion(self.read_value(ctr_tag, "ArReleaseMajorVersion"))
            pub_info.setArReleaseMinorVersion(self.read_value(ctr_tag, "ArReleaseMinorVersion"))
            pub_info.setArReleasePatchVersion(self.read_value(ctr_tag, "ArReleasePatchVersion"))
            pub_info.setSwMajorVersion(self.read_value(ctr_tag, "SwMajorVersion"))
            pub_info.setSwMinorVersion(self.read_value(ctr_tag, "SwMinorVersion"))
            pub_info.setSwPatchVersion(self.read_value(ctr_tag, "SwPatchVersion"))
            os.setPublishedInformation(pub_info)
            self.logger.debug("Read PublishedInformation")

    def read_os_hw_incrementer(self, element: ET.Element, os: Os):
        """Parse OsHwIncrementer container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "OsHwIncrementer")
        if ctr_tag is not None:
            hw_inc = OsHwIncrementer(os, ctr_tag.attrib["name"])
            hw_inc.setOsHwIncrementerBase(self.read_value(ctr_tag, "OsHwIncrementerBase"))
            hw_inc.setOsHwIncrementerMax(self.read_value(ctr_tag, "OsHwIncrementerMax"))
            os.setOsHwIncrementer(hw_inc)
            self.logger.debug("Read OsHwIncrementer")

    def read_os_events(self, element: ET.Element, os: Os):
        """Parse all OsEvent containers from XDM."""
        for ctr_tag in self.find_ctr_tag_list(element, "OsEvent"):
            event = OsEvent(os, ctr_tag.attrib["name"])
            event.setOsEventMask(self.read_value(ctr_tag, "OsEventMask"))
            os.addOsEvent(event)
            self.logger.debug("Read OsEvent <%s>" % event.getName())

    def read_os_spinlocks(self, element: ET.Element, os: Os):
        """Parse all OsSpinlock containers from XDM."""
        for ctr_tag in self.find_ctr_tag_list(element, "OsSpinlock"):
            spinlock = OsSpinlock(os, ctr_tag.attrib["name"])
            spinlock.setOsSpinlockType(self.read_value(ctr_tag, "OsSpinlockType"))
            spinlock.setOsSpinlockSpinCount(self.read_value(ctr_tag, "OsSpinlockSpinCount"))
            os.addOsSpinlock(spinlock)
            self.logger.debug("Read OsSpinlock <%s>" % spinlock.getName())

    def read_os_peripheral_areas(self, element: ET.Element, os: Os):
        """Parse all OsPeripheralArea containers from XDM."""
        for ctr_tag in self.find_ctr_tag_list(element, "OsPeripheralArea"):
            area = OsPeripheralArea(os, ctr_tag.attrib["name"])
            area.setOsPeripheralAreaStartAddress(self.read_value(ctr_tag, "OsPeripheralAreaStartAddress"))
            area.setOsPeripheralAreaEndAddress(self.read_value(ctr_tag, "OsPeripheralAreaEndAddress"))
            area.setOsPeripheralAreaAccessPermission(self.read_value(ctr_tag, "OsPeripheralAreaAccessPermission"))
            os.addOsPeripheralArea(area)
            self.logger.debug("Read OsPeripheralArea <%s>" % area.getName())

    def read_os_os(self, element: ET.Element, os: Os):
        """Parse OsOS container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "OsOS")
        if ctr_tag is not None:
            os_os = OsOS(os, ctr_tag.attrib["name"])
            os_os.setOsOSCoreAssignment(self.read_value(ctr_tag, "OsOSCoreAssignment"))
            os_os.setOsOsStackMonitoring(self.read_value(ctr_tag, "OsOsStackMonitoring"))
            os_os.setOsOsUseGetServiceId(self.read_value(ctr_tag, "OsOsUseGetServiceId"))
            os_os.setOsOsUseParameterAccess(self.read_value(ctr_tag, "OsOsUseParameterAccess"))
            os_os.setOsOsUseServiceId(self.read_value(ctr_tag, "OsOsUseServiceId"))
            os.setOsOS(os_os)
            self.logger.debug("Read OsOS")

    def read_os_hooks(self, element: ET.Element, os: Os):
        """Parse OsHooks container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "OsHooks")
        if ctr_tag is not None:
            hooks = OsHooks(os, ctr_tag.attrib["name"])
            hooks.setOsErrorHook(self.read_value(ctr_tag, "OsErrorHook"))
            hooks.setOsShutdownHook(self.read_value(ctr_tag, "OsShutdownHook"))
            hooks.setOsStartupHook(self.read_value(ctr_tag, "OsStartupHook"))
            hooks.setOsPreTaskHook(self.read_value(ctr_tag, "OsPreTaskHook"))
            hooks.setOsPostTaskHook(self.read_value(ctr_tag, "OsPostTaskHook"))
            hooks.setOsProtectionHook(self.read_value(ctr_tag, "OsProtectionHook"))
            os.setOsHooks(hooks)
            self.logger.debug("Read OsHooks")

    def read_os_core_configs(self, element: ET.Element, os: Os):
        """Parse all OsCoreConfig containers from XDM."""
        for ctr_tag in self.find_ctr_tag_list(element, "OsCoreConfig"):
            core_config = OsCoreConfig(os, ctr_tag.attrib["name"])
            core_config.setOsCoreId(self.read_value(ctr_tag, "OsCoreId"))
            core_config.setOsCoreMainFunction(self.read_value(ctr_tag, "OsCoreMainFunction"))
            core_config.setOsCoreStackStartAddress(self.read_value(ctr_tag, "OsCoreStackStartAddress"))
            core_config.setOsCoreStackSize(self.read_value(ctr_tag, "OsCoreStackSize"))
            os.addOsCoreConfig(core_config)
            self.logger.debug("Read OsCoreConfig <%s>" % core_config.getName())

    def read_os_autosar_customization(self, element: ET.Element, os: Os):
        """Parse OsAutosarCustomization container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "OsAutosarCustomization")
        if ctr_tag is not None:
            customization = OsAutosarCustomization(os, ctr_tag.attrib["name"])
            customization.setOsScalableClass(self.read_value(ctr_tag, "OsScalableClass"))
            customization.setOsApplicationType(self.read_value(ctr_tag, "OsApplicationType"))
            os.setOsAutosarCustomization(customization)
            self.logger.debug("Read OsAutosarCustomization")
