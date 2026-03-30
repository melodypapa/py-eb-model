"""
Tm XDM Parser Module - Extracts AUTOSAR Tm configuration from EB Tresos XDM files.

Implements:
    - SWR_TM_00001: Tm module parsing
    - SWR_TM_00002: Tick time configuration parsing
    - SWR_TM_00003: Trigger configuration parsing
"""
import xml.etree.ElementTree as ET
from eb_model.models.core.eb_doc import EBModel
from eb_model.models.core.tm_xdm import (
    Tm, TmGeneral, TmInterruptSynchronization, TmTickTime,
    TmTrigger, CommonPublishedInformation, PublishedInformation
)
from eb_model.parser.core.eb_parser import AbstractEbModelParser


class TmXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR Tm (Timing) module configuration.

    Extracts Tm configuration including tick times and triggers.

    Implements: SWR_TM_00001 (Tm Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the Tm XDM parser."""
        super().__init__()

        self.tm = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse Tm module configuration from XDM element.

        Implements: SWR_TM_00001
        """
        if self.get_component_name(element) != "Tm":
            raise ValueError("Invalid <%s> xdm file" % "Tm")

        tm = doc.getTm()

        self.read_version(element, tm)
        self.read_common_published_information(element, tm)
        self.read_published_information(element, tm)

        self.logger.info("Parse Tm ARVersion:<%s> SwVersion:<%s>" % (tm.getArVersion().getVersion(), tm.getSwVersion().getVersion()))

        self.tm = tm

        self.read_tm_general(element, tm)
        self.read_tm_interrupt_synchronization(element, tm)
        self.read_tm_tick_time(element, tm)
        self.read_tm_triggers(element, tm)

    def read_common_published_information(self, element: ET.Element, tm: Tm):
        """
        Parse CommonPublishedInformation container from XDM.
        """
        ctr_tag = self.find_ctr_tag(element, "CommonPublishedInformation")
        if ctr_tag is not None:
            pub_info = CommonPublishedInformation(tm, ctr_tag.attrib["name"])
            pub_info.setArMajorVersion(self.read_value(ctr_tag, "ArMajorVersion"))
            pub_info.setArMinorVersion(self.read_value(ctr_tag, "ArMinorVersion"))
            pub_info.setArPatchVersion(self.read_value(ctr_tag, "ArPatchVersion"))
            pub_info.setSwMajorVersion(self.read_value(ctr_tag, "SwMajorVersion"))
            pub_info.setSwMinorVersion(self.read_value(ctr_tag, "SwMinorVersion"))
            pub_info.setSwPatchVersion(self.read_value(ctr_tag, "SwPatchVersion"))
            tm.setCommonPublishedInformation(pub_info)
            self.logger.debug("Read CommonPublishedInformation")

    def read_published_information(self, element: ET.Element, tm: Tm):
        """
        Parse PublishedInformation container from XDM.
        """
        ctr_tag = self.find_ctr_tag(element, "PublishedInformation")
        if ctr_tag is not None:
            pub_info = PublishedInformation(tm, ctr_tag.attrib["name"])
            pub_info.setVendorId(self.read_value(ctr_tag, "VendorId"))
            pub_info.setArReleaseMajorVersion(self.read_value(ctr_tag, "ArReleaseMajorVersion"))
            pub_info.setArReleaseMinorVersion(self.read_value(ctr_tag, "ArReleaseMinorVersion"))
            pub_info.setArReleasePatchVersion(self.read_value(ctr_tag, "ArReleasePatchVersion"))
            pub_info.setSwMajorVersion(self.read_value(ctr_tag, "SwMajorVersion"))
            pub_info.setSwMinorVersion(self.read_value(ctr_tag, "SwMinorVersion"))
            pub_info.setSwPatchVersion(self.read_value(ctr_tag, "SwPatchVersion"))
            tm.setPublishedInformation(pub_info)
            self.logger.debug("Read PublishedInformation")

    def read_tm_general(self, element: ET.Element, tm: Tm):
        ctr_tag = self.find_ctr_tag(element, "TmGeneral")
        if ctr_tag is not None:
            general = TmGeneral(tm, ctr_tag.attrib["name"])
            general.setTmDevErrorDetect(self.read_value(ctr_tag, "TmDevErrorDetect"))
            general.setTmMainWindowProtect(self.read_optional_value(ctr_tag, "TmMainWindowProtect"))
            general.setTmVersionInfoApi(self.read_optional_value(ctr_tag, "TmVersionInfoApi"))
            general.setTmEnablePredefTimer1us16bit(self.read_optional_value(ctr_tag, "TmEnablePredefTimer1us16bit"))
            general.setTmEnablePredefTimer1us24bit(self.read_optional_value(ctr_tag, "TmEnablePredefTimer1us24bit"))
            general.setTmEnablePredefTimer1us32bit(self.read_optional_value(ctr_tag, "TmEnablePredefTimer1us32bit"))
            general.setTmEnablePredefTimer100us32bit(self.read_optional_value(ctr_tag, "TmEnablePredefTimer100us32bit"))
            tm.setTmGeneral(general)
            self.logger.debug("Read TmGeneral")

    def read_tm_interrupt_synchronization(self, element: ET.Element, tm: Tm):
        ctr_tag = self.find_ctr_tag(element, "TmInterruptSynchronization")
        if ctr_tag is not None:
            sync = TmInterruptSynchronization(tm, ctr_tag.attrib["name"])
            sync.setTmSyncMode(self.read_value(ctr_tag, "TmSyncMode"))
            tm.setTmInterruptSynchronization(sync)
            self.logger.debug("Read TmInterruptSynchronization")

    def read_tm_tick_time(self, element: ET.Element, tm: Tm):
        ctr_tag = self.find_ctr_tag(element, "TmTickTime")
        if ctr_tag is not None:
            tick_time = TmTickTime(tm, ctr_tag.attrib["name"])
            tick_time.setTmTickTimeBase(self.read_value(ctr_tag, "TmTickTimeBase"))
            tick_time.setTmTickPriority(self.read_value(ctr_tag, "TmTickPriority"))
            tm.setTmTickTime(tick_time)
            self.logger.debug("Read TmTickTime")

    def read_tm_triggers(self, element: ET.Element, tm: Tm):
        for ctr_tag in self.find_ctr_tag_list(element, "TmTrigger"):
            trigger = TmTrigger(tm, ctr_tag.attrib["name"])
            trigger.setTmTriggerChannelRef(self.read_ref_value(ctr_tag, "TmTriggerChannelRef"))
            tm.addTmTrigger(trigger)
            self.logger.debug("Read TmTrigger <%s>" % trigger.getName())
