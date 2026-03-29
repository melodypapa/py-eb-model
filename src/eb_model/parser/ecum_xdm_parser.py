"""
EcuM XDM Parser Module - Extracts AUTOSAR EcuM configuration from EB Tresos XDM files.

Implements:
    - SWR_ECUM_00001: EcuM module parsing
    - SWR_ECUM_00002: Startup configuration parsing
    - SWR_ECUM_00003: Shutdown configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.ecum_xdm import EcuM, EcuMGeneral, EcuMStartup, EcuMShutdown, EcuMAlarm
from ..models.ecum_xdm import CommonPublishedInformation, PublishedInformation, EcuMCommonConfiguration
from ..models.ecum_xdm import EcuMDefaultShutdownTarget, EcuMDriverInitItem, EcuMDriverInitListOne
from ..models.ecum_xdm import EcuMDriverInitListZero, EcuMDriverRestartList, EcuMSleepMode
from ..models.ecum_xdm import EcuMWakeupSource, EcuMDemEventParameterRefs, EcuMFixedConfiguration
from ..models.ecum_xdm import EcuMDriverInitListThree, EcuMDriverInitListTwo, EcuMFixedUserConfig
from ..models.ecum_xdm import EcuMTTII, EcuMWdgM, EcuMFlexConfiguration, EcuMAlarmClock
from ..models.ecum_xdm import EcuMFlexUserConfig, EcuMGoDownAllowedUsers, EcuMResetMode
from ..models.ecum_xdm import EcuMSetClockAllowedUsers, EcuMShutdownCause, EcuMShutdownTarget
from ..models.ecum_xdm import EcuMDefensiveProgramming, EcuMFixedGeneral, EcuMFlexGeneral
from ..models.ecum_xdm import EcuMServiceAPI, ReportToDem
from ..parser.eb_parser import AbstractEbModelParser


class EcuMXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR EcuM (ECU State Manager) module configuration.

    Extracts EcuM configuration including startup, shutdown, and alarm settings.

    Implements: SWR_ECUM_00001 (EcuM Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the EcuM XDM parser."""
        super().__init__()

        self.ecum = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse EcuM module configuration from XDM element.

        Implements: SWR_ECUM_00001
        """
        if self.get_component_name(element) != "EcuM":
            raise ValueError("Invalid <%s> xdm file" % "EcuM")

        ecum = doc.getEcuM()

        self.read_version(element, ecum)

        self.logger.info("Parse EcuM ARVersion:<%s> SwVersion:<%s>" % (ecum.getArVersion().getVersion(), ecum.getSwVersion().getVersion()))

        self.ecum = ecum

        self.read_common_published_information(element, ecum)
        self.read_published_information(element, ecum)
        self.read_ecum_common_configuration(element, ecum)
        self.read_ecum_default_shutdown_target(element, ecum)
        self.read_ecum_driver_init_list_one(element, ecum)
        self.read_ecum_driver_init_list_zero(element, ecum)
        self.read_ecum_driver_restart_list(element, ecum)
        self.read_ecum_sleep_modes(element, ecum)
        self.read_ecum_wakeup_sources(element, ecum)
        self.read_ecum_dem_event_parameter_refs(element, ecum)
        self.read_ecum_fixed_configuration(element, ecum)
        self.read_ecum_driver_init_list_three(element, ecum)
        self.read_ecum_driver_init_list_two(element, ecum)
        self.read_ecum_fixed_user_config(element, ecum)
        self.read_ecum_ttii(element, ecum)
        self.read_ecum_wdgm(element, ecum)
        self.read_ecum_flex_configuration(element, ecum)
        self.read_ecum_alarm_clock(element, ecum)
        self.read_ecum_flex_user_config(element, ecum)
        self.read_ecum_go_down_allowed_users(element, ecum)
        self.read_ecum_reset_modes(element, ecum)
        self.read_ecum_set_clock_allowed_users(element, ecum)
        self.read_ecum_shutdown_causes(element, ecum)
        self.read_ecum_shutdown_targets(element, ecum)
        self.read_ecum_defensive_programming(element, ecum)
        self.read_ecum_fixed_general(element, ecum)
        self.read_ecum_flex_general(element, ecum)
        self.read_ecum_service_api(element, ecum)
        self.read_report_to_dem(element, ecum)
        self.read_ecum_general(element, ecum)
        self.read_ecum_startup(element, ecum)
        self.read_ecum_shutdown(element, ecum)
        self.read_ecum_alarms(element, ecum)

    def read_common_published_information(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "CommonPublishedInformation")
        if ctr_tag is not None:
            common_info = CommonPublishedInformation(ecum, ctr_tag.attrib["name"])
            common_info.setArMajorVersion(self.read_optional_value(ctr_tag, "ArMajorVersion"))
            common_info.setArMinorVersion(self.read_optional_value(ctr_tag, "ArMinorVersion"))
            common_info.setArPatchVersion(self.read_optional_value(ctr_tag, "ArPatchVersion"))
            common_info.setSwMajorVersion(self.read_optional_value(ctr_tag, "SwMajorVersion"))
            common_info.setSwMinorVersion(self.read_optional_value(ctr_tag, "SwMinorVersion"))
            common_info.setSwPatchVersion(self.read_optional_value(ctr_tag, "SwPatchVersion"))
            ecum.setCommonPublishedInformation(common_info)
            self.logger.debug("Read CommonPublishedInformation")

    def read_published_information(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "PublishedInformation")
        if ctr_tag is not None:
            pub_info = PublishedInformation(ecum, ctr_tag.attrib["name"])
            pub_info.setVendorId(self.read_optional_value(ctr_tag, "VendorId"))
            pub_info.setArReleaseMajorVersion(self.read_optional_value(ctr_tag, "ArReleaseMajorVersion"))
            pub_info.setArReleaseMinorVersion(self.read_optional_value(ctr_tag, "ArReleaseMinorVersion"))
            pub_info.setArReleasePatchVersion(self.read_optional_value(ctr_tag, "ArReleasePatchVersion"))
            pub_info.setSwMajorVersion(self.read_optional_value(ctr_tag, "SwMajorVersion"))
            pub_info.setSwMinorVersion(self.read_optional_value(ctr_tag, "SwMinorVersion"))
            pub_info.setSwPatchVersion(self.read_optional_value(ctr_tag, "SwPatchVersion"))
            ecum.setPublishedInformation(pub_info)
            self.logger.debug("Read PublishedInformation")

    def read_ecum_common_configuration(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMCommonConfiguration")
        if ctr_tag is not None:
            common_config = EcuMCommonConfiguration(ecum, ctr_tag.attrib["name"])
            common_config.setEcumDevErrorDetect(self.read_optional_value(ctr_tag, "EcuMDevErrorDetect"))
            common_config.setEcumIncludeDem(self.read_optional_value(ctr_tag, "EcuMIncludeDem"))
            common_config.setEcumIncludeDet(self.read_optional_value(ctr_tag, "EcuMIncludeDet"))
            common_config.setEcumMainFunctionPeriod(self.read_optional_value(ctr_tag, "EcuMMainFunctionPeriod"))
            ecum.setEcumCommonConfiguration(common_config)
            self.logger.debug("Read EcuMCommonConfiguration")

    def read_ecum_default_shutdown_target(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMDefaultShutdownTarget")
        if ctr_tag is not None:
            shutdown_target = EcuMDefaultShutdownTarget(ecum, ctr_tag.attrib["name"])
            shutdown_ref = self.read_optional_ref_value(ctr_tag, "EcuMDefaultShutdownTargetRef")
            if shutdown_ref is not None:
                shutdown_target.setEcumDefaultShutdownTargetRef(shutdown_ref)
            ecum.setEcumDefaultShutdownTarget(shutdown_target)
            self.logger.debug("Read EcuMDefaultShutdownTarget")

    def read_ecum_driver_init_list_one(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMDriverInitListOne")
        if ctr_tag is not None:
            init_list = EcuMDriverInitListOne(ecum, ctr_tag.attrib["name"])
            for item_tag in self.find_ctr_tag_list(ctr_tag, "EcuMDriverInitItem"):
                item = EcuMDriverInitItem(init_list, item_tag.attrib["name"])
                item_ref = self.read_optional_ref_value(item_tag, "EcuMDriverInitRef")
                if item_ref is not None:
                    item.setEcumDriverInitRef(item_ref)
                init_list.addEcumDriverInitItem(item)
            ecum.setEcumDriverInitListOne(init_list)
            self.logger.debug("Read EcuMDriverInitListOne")

    def read_ecum_driver_init_list_zero(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMDriverInitListZero")
        if ctr_tag is not None:
            init_list = EcuMDriverInitListZero(ecum, ctr_tag.attrib["name"])
            for item_tag in self.find_ctr_tag_list(ctr_tag, "EcuMDriverInitItem"):
                item = EcuMDriverInitItem(init_list, item_tag.attrib["name"])
                item_ref = self.read_optional_ref_value(item_tag, "EcuMDriverInitRef")
                if item_ref is not None:
                    item.setEcumDriverInitRef(item_ref)
                init_list.addEcumDriverInitItem(item)
            ecum.setEcumDriverInitListZero(init_list)
            self.logger.debug("Read EcuMDriverInitListZero")

    def read_ecum_driver_restart_list(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMDriverRestartList")
        if ctr_tag is not None:
            restart_list = EcuMDriverRestartList(ecum, ctr_tag.attrib["name"])
            for item_tag in self.find_ctr_tag_list(ctr_tag, "EcuMDriverInitItem"):
                item = EcuMDriverInitItem(restart_list, item_tag.attrib["name"])
                item_ref = self.read_optional_ref_value(item_tag, "EcuMDriverInitRef")
                if item_ref is not None:
                    item.setEcumDriverInitRef(item_ref)
                restart_list.addEcumDriverInitItem(item)
            ecum.setEcumDriverRestartList(restart_list)
            self.logger.debug("Read EcuMDriverRestartList")

    def read_ecum_sleep_modes(self, element: ET.Element, ecum: EcuM):
        for ctr_tag in self.find_ctr_tag_list(element, "EcuMSleepMode"):
            sleep_mode = EcuMSleepMode(ecum, ctr_tag.attrib["name"])
            sleep_ref = self.read_optional_ref_value(ctr_tag, "EcuMSleepModeRef")
            if sleep_ref is not None:
                sleep_mode.setEcumSleepModeRef(sleep_ref)
            sleep_mode.setEcumCancelShutdown(self.read_optional_value(ctr_tag, "EcuMCancelShutdown"))
            ecum.addEcumSleepMode(sleep_mode)
            self.logger.debug("Read EcuMSleepMode <%s>" % sleep_mode.getName())

    def read_ecum_wakeup_sources(self, element: ET.Element, ecum: EcuM):
        for ctr_tag in self.find_ctr_tag_list(element, "EcuMWakeupSource"):
            wakeup_source = EcuMWakeupSource(ecum, ctr_tag.attrib["name"])
            wakeup_ref = self.read_optional_ref_value(ctr_tag, "EcuMWakeupSourceRef")
            if wakeup_ref is not None:
                wakeup_source.setEcumWakeupSourceRef(wakeup_ref)
            wakeup_source.setEcumEnableWakeupValidation(self.read_optional_value(ctr_tag, "EcuMEnableWakeupValidation"))
            ecum.addEcumWakeupSource(wakeup_source)
            self.logger.debug("Read EcuMWakeupSource <%s>" % wakeup_source.getName())

    def read_ecum_dem_event_parameter_refs(self, element: ET.Element, ecum: EcuM):
        for ctr_tag in self.find_ctr_tag_list(element, "EcuMDemEventParameterRefs"):
            dem_ref = EcuMDemEventParameterRefs(ecum, ctr_tag.attrib["name"])
            event_ref = self.read_optional_ref_value(ctr_tag, "EcuMDemEventParameterRef")
            if event_ref is not None:
                dem_ref.setEcumDemEventParameterRef(event_ref)
            ecum.addEcumDemEventParameterRef(dem_ref)
            self.logger.debug("Read EcuMDemEventParameterRefs <%s>" % dem_ref.getName())

    def read_ecum_fixed_configuration(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMFixedConfiguration")
        if ctr_tag is not None:
            fixed_config = EcuMFixedConfiguration(ecum, ctr_tag.attrib["name"])
            fixed_config.setEcumMaxSleepModeCounter(self.read_optional_value(ctr_tag, "EcuMMaxSleepModeCounter"))
            fixed_config.setEcumInitCheck(self.read_optional_value(ctr_tag, "EcuMInitCheck"))
            ecum.setEcumFixedConfiguration(fixed_config)
            self.logger.debug("Read EcuMFixedConfiguration")

    def read_ecum_driver_init_list_three(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMDriverInitListThree")
        if ctr_tag is not None:
            init_list = EcuMDriverInitListThree(ecum, ctr_tag.attrib["name"])
            for item_tag in self.find_ctr_tag_list(ctr_tag, "EcuMDriverInitItem"):
                item = EcuMDriverInitItem(init_list, item_tag.attrib["name"])
                item_ref = self.read_optional_ref_value(item_tag, "EcuMDriverInitRef")
                if item_ref is not None:
                    item.setEcumDriverInitRef(item_ref)
                init_list.addEcumDriverInitItem(item)
            ecum.setEcumDriverInitListThree(init_list)
            self.logger.debug("Read EcuMDriverInitListThree")

    def read_ecum_driver_init_list_two(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMDriverInitListTwo")
        if ctr_tag is not None:
            init_list = EcuMDriverInitListTwo(ecum, ctr_tag.attrib["name"])
            for item_tag in self.find_ctr_tag_list(ctr_tag, "EcuMDriverInitItem"):
                item = EcuMDriverInitItem(init_list, item_tag.attrib["name"])
                item_ref = self.read_optional_ref_value(item_tag, "EcuMDriverInitRef")
                if item_ref is not None:
                    item.setEcumDriverInitRef(item_ref)
                init_list.addEcumDriverInitItem(item)
            ecum.setEcumDriverInitListTwo(init_list)
            self.logger.debug("Read EcuMDriverInitListTwo")

    def read_ecum_fixed_user_config(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMFixedUserConfig")
        if ctr_tag is not None:
            fixed_user_config = EcuMFixedUserConfig(ecum, ctr_tag.attrib["name"])
            fixed_user_config.setEcumEnableUserPostBuild(self.read_optional_value(ctr_tag, "EcuMEnableUserPostBuild"))
            ecum.setEcumFixedUserConfig(fixed_user_config)
            self.logger.debug("Read EcuMFixedUserConfig")

    def read_ecum_ttii(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMTTII")
        if ctr_tag is not None:
            ttii = EcuMTTII(ecum, ctr_tag.attrib["name"])
            ttii.setEcumTtiiPrepSleepDuration(self.read_optional_value(ctr_tag, "EcuMTtiiPrepSleepDuration"))
            ttii.setEcumTtiiWakeupDuration(self.read_optional_value(ctr_tag, "EcuMTtiiWakeupDuration"))
            ecum.setEcumTtii(ttii)
            self.logger.debug("Read EcuMTTII")

    def read_ecum_wdgm(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMWdgM")
        if ctr_tag is not None:
            wdgm = EcuMWdgM(ecum, ctr_tag.attrib["name"])
            wdgm.setEcumWdgMTriggerWithOs(self.read_optional_value(ctr_tag, "EcuMWdgMTriggerWithOs"))
            wdgm_ref = self.read_optional_ref_value(ctr_tag, "EcuMWdgMSupervisionRef")
            if wdgm_ref is not None:
                wdgm.setEcumWdgMSupervisionRef(wdgm_ref)
            ecum.setEcumWdgM(wdgm)
            self.logger.debug("Read EcuMWdgM")

    def read_ecum_flex_configuration(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMFlexConfiguration")
        if ctr_tag is not None:
            flex_config = EcuMFlexConfiguration(ecum, ctr_tag.attrib["name"])
            flex_config.setEcumRunPostBuild(self.read_optional_value(ctr_tag, "EcuMRunPostBuild"))
            ecum.setEcumFlexConfiguration(flex_config)
            self.logger.debug("Read EcuMFlexConfiguration")

    def read_ecum_alarm_clock(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMAlarmClock")
        if ctr_tag is not None:
            alarm_clock = EcuMAlarmClock(ecum, ctr_tag.attrib["name"])
            alarm_ref = self.read_optional_ref_value(ctr_tag, "EcuMAlarmClockRef")
            if alarm_ref is not None:
                alarm_clock.setEcumAlarmClockRef(alarm_ref)
            ecum.setEcumAlarmClock(alarm_clock)
            self.logger.debug("Read EcuMAlarmClock")

    def read_ecum_flex_user_config(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMFlexUserConfig")
        if ctr_tag is not None:
            flex_user_config = EcuMFlexUserConfig(ecum, ctr_tag.attrib["name"])
            flex_user_config.setEcumEnableUserPostBuild(self.read_optional_value(ctr_tag, "EcuMEnableUserPostBuild"))
            ecum.setEcumFlexUserConfig(flex_user_config)
            self.logger.debug("Read EcuMFlexUserConfig")

    def read_ecum_go_down_allowed_users(self, element: ET.Element, ecum: EcuM):
        for ctr_tag in self.find_ctr_tag_list(element, "EcuMGoDownAllowedUsers"):
            go_down_user = EcuMGoDownAllowedUsers(ecum, ctr_tag.attrib["name"])
            user_ref = self.read_optional_ref_value(ctr_tag, "EcuMGoDownAllowedUserRef")
            if user_ref is not None:
                go_down_user.setEcumGoDownAllowedUserRef(user_ref)
            ecum.addEcumGoDownAllowedUser(go_down_user)
            self.logger.debug("Read EcuMGoDownAllowedUsers <%s>" % go_down_user.getName())

    def read_ecum_reset_modes(self, element: ET.Element, ecum: EcuM):
        for ctr_tag in self.find_ctr_tag_list(element, "EcuMResetMode"):
            reset_mode = EcuMResetMode(ecum, ctr_tag.attrib["name"])
            mode_ref = self.read_optional_ref_value(ctr_tag, "EcuMResetModeRef")
            if mode_ref is not None:
                reset_mode.setEcumResetModeRef(mode_ref)
            ecum.addEcumResetMode(reset_mode)
            self.logger.debug("Read EcuMResetMode <%s>" % reset_mode.getName())

    def read_ecum_set_clock_allowed_users(self, element: ET.Element, ecum: EcuM):
        for ctr_tag in self.find_ctr_tag_list(element, "EcuMSetClockAllowedUsers"):
            set_clock_user = EcuMSetClockAllowedUsers(ecum, ctr_tag.attrib["name"])
            user_ref = self.read_optional_ref_value(ctr_tag, "EcuMSetClockAllowedUserRef")
            if user_ref is not None:
                set_clock_user.setEcumSetClockAllowedUserRef(user_ref)
            ecum.addEcumSetClockAllowedUser(set_clock_user)
            self.logger.debug("Read EcuMSetClockAllowedUsers <%s>" % set_clock_user.getName())

    def read_ecum_shutdown_causes(self, element: ET.Element, ecum: EcuM):
        for ctr_tag in self.find_ctr_tag_list(element, "EcuMShutdownCause"):
            shutdown_cause = EcuMShutdownCause(ecum, ctr_tag.attrib["name"])
            cause_ref = self.read_optional_ref_value(ctr_tag, "EcuMShutdownCauseRef")
            if cause_ref is not None:
                shutdown_cause.setEcumShutdownCauseRef(cause_ref)
            target_ref = self.read_optional_ref_value(ctr_tag, "EcuMShutdownTargetRef")
            if target_ref is not None:
                shutdown_cause.setEcumShutdownTargetRef(target_ref)
            ecum.addEcumShutdownCause(shutdown_cause)
            self.logger.debug("Read EcuMShutdownCause <%s>" % shutdown_cause.getName())

    def read_ecum_shutdown_targets(self, element: ET.Element, ecum: EcuM):
        for ctr_tag in self.find_ctr_tag_list(element, "EcuMShutdownTarget"):
            shutdown_target = EcuMShutdownTarget(ecum, ctr_tag.attrib["name"])
            shutdown_target.setEcumShutdownTargetType(self.read_optional_value(ctr_tag, "EcuMShutdownTargetType"))
            mode_ref = self.read_optional_ref_value(ctr_tag, "EcuMResetModeRef")
            if mode_ref is not None:
                shutdown_target.setEcumResetModeRef(mode_ref)
            ecum.addEcumShutdownTarget(shutdown_target)
            self.logger.debug("Read EcuMShutdownTarget <%s>" % shutdown_target.getName())

    def read_ecum_defensive_programming(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMDefensiveProgramming")
        if ctr_tag is not None:
            def_prog = EcuMDefensiveProgramming(ecum, ctr_tag.attrib["name"])
            def_prog.setEcumDevErrorDetect(self.read_optional_value(ctr_tag, "EcuMDevErrorDetect"))
            def_prog.setEcumNullPointerCheck(self.read_optional_value(ctr_tag, "EcuMNullPointerCheck"))
            ecum.setEcumDefensiveProgramming(def_prog)
            self.logger.debug("Read EcuMDefensiveProgramming")

    def read_ecum_fixed_general(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMFixedGeneral")
        if ctr_tag is not None:
            fixed_general = EcuMFixedGeneral(ecum, ctr_tag.attrib["name"])
            fixed_general.setEcumDevErrorDetect(self.read_optional_value(ctr_tag, "EcuMDevErrorDetect"))
            fixed_general.setEcumMainFunctionPeriod(self.read_optional_value(ctr_tag, "EcuMMainFunctionPeriod"))
            ecum.setEcumFixedGeneral(fixed_general)
            self.logger.debug("Read EcuMFixedGeneral")

    def read_ecum_flex_general(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMFlexGeneral")
        if ctr_tag is not None:
            flex_general = EcuMFlexGeneral(ecum, ctr_tag.attrib["name"])
            flex_general.setEcumDevErrorDetect(self.read_optional_value(ctr_tag, "EcuMDevErrorDetect"))
            flex_general.setEcumMainFunctionPeriod(self.read_optional_value(ctr_tag, "EcuMMainFunctionPeriod"))
            ecum.setEcumFlexGeneral(flex_general)
            self.logger.debug("Read EcuMFlexGeneral")

    def read_ecum_service_api(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMServiceAPI")
        if ctr_tag is not None:
            service_api = EcuMServiceAPI(ecum, ctr_tag.attrib["name"])
            service_api.setEcumReportErrorNotification(self.read_optional_value(ctr_tag, "EcuMReportErrorNotification"))
            service_api.setEcumVersionInfoApi(self.read_optional_value(ctr_tag, "EcuMVersionInfoApi"))
            ecum.setEcumServiceAPI(service_api)
            self.logger.debug("Read EcuMServiceAPI")

    def read_report_to_dem(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "ReportToDem")
        if ctr_tag is not None:
            report_to_dem = ReportToDem(ecum, ctr_tag.attrib["name"])
            event_ref = self.read_optional_ref_value(ctr_tag, "EcuMDemEventIdRef")
            if event_ref is not None:
                report_to_dem.setEcumDemEventIdRef(event_ref)
            ecum.setReportToDem(report_to_dem)
            self.logger.debug("Read ReportToDem")

    def read_ecum_general(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMGeneral")
        if ctr_tag is not None:
            general = EcuMGeneral(ecum, ctr_tag.attrib["name"])
            general.setEcumDevErrorDetect(self.read_value(ctr_tag, "EcuMDevErrorDetect"))
            general.setEcumConfigurationVariant(self.read_value(ctr_tag, "EcuMConfigurationVariant"))
            general.setEcumIncludeDem(self.read_optional_value(ctr_tag, "EcuMIncludeDem"))
            general.setEcumIncludeDet(self.read_optional_value(ctr_tag, "EcuMIncludeDet"))
            general.setEcumMainFunctionPeriod(self.read_optional_value(ctr_tag, "EcuMMainFunctionPeriod"))
            ecum.setEcumGeneral(general)
            self.logger.debug("Read EcuMGeneral")

    def read_ecum_startup(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMStartup")
        if ctr_tag is not None:
            startup = EcuMStartup(ecum, ctr_tag.attrib["name"])
            startup.setEcumEnableUserMcuStartup(self.read_value(ctr_tag, "EcuMEnableUserMcuStartup"))
            startup_ref = self.read_optional_ref_value(ctr_tag, "EcuMUserMcuStartupRef")
            if startup_ref is not None:
                startup.setEcumUserMcuStartupRef(startup_ref)
            ecum.setEcumStartup(startup)
            self.logger.debug("Read EcuMStartup")

    def read_ecum_shutdown(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMShutdown")
        if ctr_tag is not None:
            shutdown = EcuMShutdown(ecum, ctr_tag.attrib["name"])
            shutdown.setEcumEnableUserMcuShutdown(self.read_value(ctr_tag, "EcuMEnableUserMcuShutdown"))
            shutdown_ref = self.read_optional_ref_value(ctr_tag, "EcuMUserMcuShutdownRef")
            if shutdown_ref is not None:
                shutdown.setEcumUserMcuShutdownRef(shutdown_ref)
            ecum.setEcumShutdown(shutdown)
            self.logger.debug("Read EcuMShutdown")

    def read_ecum_alarms(self, element: ET.Element, ecum: EcuM):
        for ctr_tag in self.find_ctr_tag_list(element, "EcuMAlarm"):
            alarm = EcuMAlarm(ecum, ctr_tag.attrib["name"])
            alarm.setEcumAlarmCounterRef(self.read_ref_value(ctr_tag, "EcuMAlarmCounterRef"))
            alarm.setEcumAlarmActionRef(self.read_ref_value(ctr_tag, "EcuMAlarmActionRef"))
            ecum.addEcumAlarm(alarm)
            self.logger.debug("Read EcuMAlarm <%s>" % alarm.getName())
