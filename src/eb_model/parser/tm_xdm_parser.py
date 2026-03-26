"""
Tm XDM Parser Module - Extracts AUTOSAR Tm configuration from EB Tresos XDM files.

Implements:
    - SWR_TM_00001: Tm module parsing
    - SWR_TM_00002: Tick time configuration parsing
    - SWR_TM_00003: Trigger configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.tm_xdm import Tm, TmGeneral, TmInterruptSynchronization, TmTickTime, TmTrigger
from ..parser.eb_parser import AbstractEbModelParser


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

        self.logger.info("Parse Tm ARVersion:<%s> SwVersion:<%s>" % (tm.getArVersion().getVersion(), tm.getSwVersion().getVersion()))

        self.tm = tm

        self.read_tm_general(element, tm)
        self.read_tm_interrupt_synchronization(element, tm)
        self.read_tm_tick_time(element, tm)
        self.read_tm_triggers(element, tm)

    def read_tm_general(self, element: ET.Element, tm: Tm):
        ctr_tag = self.find_ctr_tag(element, "TmGeneral")
        if ctr_tag is not None:
            general = TmGeneral(tm, ctr_tag.attrib["name"])
            general.setTmDevErrorDetect(self.read_value(ctr_tag, "TmDevErrorDetect"))
            general.setTmMainWindowProtect(self.read_optional_value(ctr_tag, "TmMainWindowProtect"))
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
