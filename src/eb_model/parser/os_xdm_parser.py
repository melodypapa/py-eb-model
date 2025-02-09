import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.os_xdm import Os, OsAlarm, OsAlarmActivateTask, OsAlarmCallback, OsAlarmIncrementCounter, OsAlarmSetEvent, OsCounter, OsResource
from ..models.os_xdm import OsScheduleTable
from ..models.os_xdm import OsTask, OsIsr, OsApplication, OsScheduleTableEventSetting, OsScheduleTableExpiryPoint, OsScheduleTableTaskActivation
from ..models.os_xdm import OsScheduleTblAdjustableExpPoint, OsTaskAutostart
from ..parser.eb_parser import AbstractEbModelParser


class OsXdmParser(AbstractEbModelParser):
    def __init__(self, ) -> None:
        super().__init__()

        self.os = None

    def parse(self, element: ET.Element, doc: EBModel):
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

    def read_os_task_autostart(self, element: ET.Element, os_task: OsTask):
        ctr_tag = self.find_ctr_tag(element, "OsTaskAutostart")
        if ctr_tag is not None:
            autostart = OsTaskAutostart(os_task, ctr_tag.attrib["name"])
            for app_mode_ref in self.read_ref_value_list(ctr_tag, "OsTaskAppModeRef"):
                autostart.addOsTaskAppModeRef(app_mode_ref)
            os_task.setOsTaskAutostart(autostart)

    def read_os_tasks(self, element: ET.Element, os: Os):
        for ctr_tag in self.find_ctr_tag_list(element, "OsTask"):
            os_task = OsTask(os, ctr_tag.attrib["name"])
            os_task.setOsTaskPriority(int(self.read_value(ctr_tag, "OsTaskPriority"))) \
                .setOsTaskActivation(self.read_value(ctr_tag, "OsTaskActivation")) \
                .setOsTaskSchedule(self.read_value(ctr_tag, "OsTaskSchedule")) \
                .setOsTaskType(self.read_optional_value(ctr_tag, "OsTaskType")) \
                .setOsStacksize(int(self.read_optional_value(ctr_tag, "OsStacksize", 0)))

            for resource_ref in self.read_ref_value_list(ctr_tag, "OsTaskResourceRef"):
                os_task.addOsTaskResourceRef(resource_ref)

            self.read_os_task_autostart(ctr_tag, os_task)

            self.logger.debug("Read OsTask <%s>" % os_task.getName())
            os.addOsTask(os_task)

    def read_os_isrs(self, element: ET.Element, os: Os):
        for ctr_tag in self.find_ctr_tag_list(element, "OsIsr"):
            os_isr = OsIsr(os, ctr_tag.attrib["name"])
            os_isr.setOsIsrCategory(self.read_value(ctr_tag, "OsIsrCategory")) \
                .setOsIsrPeriod(self.read_optional_value(ctr_tag, "OsIsrPeriod", 0.0)) \
                .setOsStacksize(int(self.read_value(ctr_tag, "OsStacksize"))) \
                .setOsIsrPriority(self.read_optional_value(ctr_tag, "OsIsrPriority"))
            
            # patch for the infineon Aurix
            os_isr.setOsIsrPriority(self.read_optional_value(ctr_tag, "OsTricoreIrqLevel"))
            # patch for the ARM
            os_isr.setOsIsrPriority(self.read_optional_value(ctr_tag, "OsARMIrqLevel"))
            os_isr.setOsIsrVector(self.read_optional_value(ctr_tag, "OsARMVector"))

            self.logger.debug("Read OsIsr <%s>" % os_isr.getName())
            os.addOsIsr(os_isr)

    def read_os_alarm_action(self, element: ET.Element, os_alarm: OsAlarm):
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

    def read_os_alarms(self, element: ET.Element, os: Os):
        for ctr_tag in self.find_ctr_tag_list(element, "OsAlarm"):
            os_alarm = OsAlarm(os, ctr_tag.attrib["name"]) \
                .setOsAlarmCounterRef(self.read_ref_value(ctr_tag, "OsAlarmCounterRef"))

            for ref in self.read_ref_value_list(ctr_tag, "OsAlarmAccessingApplication"):
                os_alarm.addOsAlarmAccessingApplicationRef(ref)

            self.read_os_alarm_action(ctr_tag, os_alarm)

            self.logger.debug("Read OsAlarm <%s>" % os_alarm.getName())
            os.addOsAlarm(os_alarm)

    def read_os_schedule_table_event_settings(self, element: ET.Element, expiry_point: OsScheduleTableExpiryPoint):
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
        for ctr_tag in self.find_ctr_tag_list(element, "OsCounter"):
            counter = OsCounter(os, ctr_tag.attrib["name"]) \
                .setOsCounterMaxAllowedValue(self.read_value(ctr_tag, "OsCounterMaxAllowedValue")) \
                .setOsCounterMinCycle(self.read_value(ctr_tag, "OsCounterMinCycle")) \
                .setOsCounterTicksPerBase(self.read_value(ctr_tag, "OsCounterTicksPerBase")) \
                .setOsCounterType(self.read_optional_value(ctr_tag, "OsCounterType")) \
                .setOsSecondsPerTick(self.read_optional_value(ctr_tag, "OsSecondsPerTick")) \
                

            self.logger.debug("Read OsCounter <%s>" % counter.getName())
            os.addOsScheduleTable(counter)

    def read_os_applications(self, element: ET.Element, os: Os):
        for ctr_tag in self.find_ctr_tag_list(element, "OsApplication"):
            os_app = OsApplication(os, ctr_tag.attrib["name"]) \
                .setOsTrusted(self.read_value(ctr_tag, "OsTrusted"))
            
            for ref in self.read_ref_value_list(ctr_tag, "OsAppResourceRef"):
                os_app.addOsAppResourceRef(ref)

            for ref in self.read_ref_value_list(ctr_tag, "OsAppTaskRef"):
                os_app.addOsAppTaskRef(ref)

            for ref in self.read_ref_value_list(ctr_tag, "OsAppIsrRef"):
                os_app.addOsAppIsrRef(ref)

            self.logger.debug("Read OsApplication <%s>" % os_app.getName())
            os.addOsApplication(os_app)

    def read_os_resources(self, element: ET.Element, os: Os):
        for ctr_tag in self.find_ctr_tag_list(element, "OsResource"):
            os_res = OsResource(os, ctr_tag.attrib["name"])
            os_res.setOsResourceProperty(self.read_value(ctr_tag, "OsResourceProperty"))

            for ref in self.read_ref_value_list(ctr_tag, "OsResourceAccessingApplication"):
                os_res.addOsResourceAccessingApplicationRefs(ref)

            os.addOsResource(os_res)
