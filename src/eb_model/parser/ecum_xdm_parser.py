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

        self.read_ecum_general(element, ecum)
        self.read_ecum_startup(element, ecum)
        self.read_ecum_shutdown(element, ecum)
        self.read_ecum_alarms(element, ecum)

    def read_ecum_general(self, element: ET.Element, ecum: EcuM):
        ctr_tag = self.find_ctr_tag(element, "EcuMGeneral")
        if ctr_tag is not None:
            general = EcuMGeneral(ecum, ctr_tag.attrib["name"])
            general.setEcumDevErrorDetect(self.read_value(ctr_tag, "EcuMDevErrorDetect"))
            general.setEcumConfigurationVariant(self.read_value(ctr_tag, "EcuMConfigurationVariant"))
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
