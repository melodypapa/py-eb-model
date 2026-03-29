"""
Det XDM Parser Module - Extracts AUTOSAR Det configuration from EB Tresos XDM files.

Implements:
    - SWR_DET_00001: Det module parsing
    - SWR_DET_00002: Error hook parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.det_xdm import Det, DetGeneral, DetErrorHook, DetInitError
from ..models.det_xdm import CommonPublishedInformation, PublishedInformation, DetServiceAPI, DetNotification, DetDefensiveProgramming
from ..models.det_xdm import SoftwareComponentList, InstanceIdList
from ..parser.eb_parser import AbstractEbModelParser


class DetXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR Det (Development Error Tracer) module configuration.

    Extracts Det configuration including error hooks and init errors.

    Implements: SWR_DET_00001 (Det Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the Det XDM parser."""
        super().__init__()

        self.det = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse Det module configuration from XDM element.

        Implements: SWR_DET_00001
        """
        if self.get_component_name(element) != "Det":
            raise ValueError("Invalid <%s> xdm file" % "Det")

        det = doc.getDet()

        self.read_version(element, det)

        self.logger.info("Parse Det ARVersion:<%s> SwVersion:<%s>" % (det.getArVersion().getVersion(), det.getSwVersion().getVersion()))

        self.det = det

        self.read_common_published_information(element, det)
        self.read_published_information(element, det)
        self.read_det_service_api(element, det)
        self.read_det_notification(element, det)
        self.read_det_defensive_programming(element, det)
        self.read_software_component_list(element, det)
        self.read_instance_id_list(element, det)
        self.read_det_general(element, det)
        self.read_det_error_hook(element, det)
        self.read_det_init_error(element, det)

    def read_det_general(self, element: ET.Element, det: Det):
        ctr_tag = self.find_ctr_tag(element, "DetGeneral")
        if ctr_tag is not None:
            general = DetGeneral(det, ctr_tag.attrib["name"])
            general.setDetDevErrorDetect(self.read_value(ctr_tag, "DetDevErrorDetect"))
            general.setDetEnabled(self.read_value(ctr_tag, "DetEnabled"))
            general.setDetForwardToDlt(self.read_optional_value(ctr_tag, "DetForwardToDlt"))
            general.setDetVersionInfoApi(self.read_optional_value(ctr_tag, "DetVersionInfoApi"))
            general.setLoggingMode(self.read_optional_value(ctr_tag, "LoggingMode"))
            general.setBufferSize(self.read_optional_value(ctr_tag, "BufferSize"))
            det.setDetGeneral(general)
            self.logger.debug("Read DetGeneral")

    def read_det_error_hook(self, element: ET.Element, det: Det):
        ctr_tag = self.find_ctr_tag(element, "DetErrorHook")
        if ctr_tag is not None:
            error_hook = DetErrorHook(det, ctr_tag.attrib["name"])
            error_hook.setDetErrorHookCallbackName(self.read_value(ctr_tag, "DetErrorHookCallbackName"))
            det.setDetErrorHook(error_hook)
            self.logger.debug("Read DetErrorHook")

    def read_det_init_error(self, element: ET.Element, det: Det):
        ctr_tag = self.find_ctr_tag(element, "DetInitError")
        if ctr_tag is not None:
            init_error = DetInitError(det, ctr_tag.attrib["name"])
            init_error.setDetInitErrorRef(self.read_ref_value(ctr_tag, "DetInitErrorRef"))
            det.setDetInitError(init_error)
            self.logger.debug("Read DetInitError")

    def read_common_published_information(self, element: ET.Element, det: Det):
        """
        Parse CommonPublishedInformation container from XDM.
        """
        ctr_tag = self.find_ctr_tag(element, "CommonPublishedInformation")
        if ctr_tag is not None:
            pub_info = CommonPublishedInformation(det, ctr_tag.attrib["name"])
            pub_info.setArMajorVersion(self.read_value(ctr_tag, "ArMajorVersion"))
            pub_info.setArMinorVersion(self.read_value(ctr_tag, "ArMinorVersion"))
            pub_info.setArPatchVersion(self.read_value(ctr_tag, "ArPatchVersion"))
            pub_info.setSwMajorVersion(self.read_value(ctr_tag, "SwMajorVersion"))
            pub_info.setSwMinorVersion(self.read_value(ctr_tag, "SwMinorVersion"))
            pub_info.setSwPatchVersion(self.read_value(ctr_tag, "SwPatchVersion"))
            det.setCommonPublishedInformation(pub_info)
            self.logger.debug("Read CommonPublishedInformation")

    def read_published_information(self, element: ET.Element, det: Det):
        """
        Parse PublishedInformation container from XDM.
        """
        ctr_tag = self.find_ctr_tag(element, "PublishedInformation")
        if ctr_tag is not None:
            pub_info = PublishedInformation(det, ctr_tag.attrib["name"])
            pub_info.setVendorId(self.read_value(ctr_tag, "VendorId"))
            pub_info.setArReleaseMajorVersion(self.read_value(ctr_tag, "ArReleaseMajorVersion"))
            pub_info.setArReleaseMinorVersion(self.read_value(ctr_tag, "ArReleaseMinorVersion"))
            pub_info.setArReleasePatchVersion(self.read_value(ctr_tag, "ArReleasePatchVersion"))
            pub_info.setSwMajorVersion(self.read_value(ctr_tag, "SwMajorVersion"))
            pub_info.setSwMinorVersion(self.read_value(ctr_tag, "SwMinorVersion"))
            pub_info.setSwPatchVersion(self.read_value(ctr_tag, "SwPatchVersion"))
            det.setPublishedInformation(pub_info)
            self.logger.debug("Read PublishedInformation")

    def read_det_service_api(self, element: ET.Element, det: Det):
        """
        Parse DetServiceAPI container from XDM.
        """
        ctr_tag = self.find_ctr_tag(element, "DetServiceAPI")
        if ctr_tag is not None:
            service_api = DetServiceAPI(det, ctr_tag.attrib["name"])
            service_api.setDetVersionInfoApi(self.read_optional_value(ctr_tag, "DetVersionInfoApi"))
            service_api.setDetReportRuntimeErrorCallout(self.read_optional_value(ctr_tag, "DetReportRuntimeErrorCallout"))
            det.setDetServiceAPI(service_api)
            self.logger.debug("Read DetServiceAPI")

    def read_det_notification(self, element: ET.Element, det: Det):
        """
        Parse DetNotification container from XDM.
        """
        ctr_tag = self.find_ctr_tag(element, "DetNotification")
        if ctr_tag is not None:
            notification = DetNotification(det, ctr_tag.attrib["name"])
            notification.setDetErrorNotification(self.read_optional_value(ctr_tag, "DetErrorNotification"))
            notification.setDetRuntimeErrorNotification(self.read_optional_value(ctr_tag, "DetRuntimeErrorNotification"))
            notification.setDetTransitionErrorNotification(self.read_optional_value(ctr_tag, "DetTransitionErrorNotification"))
            det.setDetNotification(notification)
            self.logger.debug("Read DetNotification")

    def read_det_defensive_programming(self, element: ET.Element, det: Det):
        """
        Parse DetDefensiveProgramming container from XDM.
        """
        ctr_tag = self.find_ctr_tag(element, "DetDefensiveProgramming")
        if ctr_tag is not None:
            defensive = DetDefensiveProgramming(det, ctr_tag.attrib["name"])
            defensive.setDetNullPointerCheck(self.read_optional_value(ctr_tag, "DetNullPointerCheck"))
            defensive.setDetParameterCheck(self.read_optional_value(ctr_tag, "DetParameterCheck"))
            det.setDetDefensiveProgramming(defensive)
            self.logger.debug("Read DetDefensiveProgramming")

    def read_software_component_list(self, element: ET.Element, det: Det):
        """
        Parse SoftwareComponentList container from XDM.
        """
        ctr_tag = self.find_ctr_tag(element, "SoftwareComponentList")
        if ctr_tag is not None:
            sw_list = SoftwareComponentList(det, ctr_tag.attrib["name"])
            det.setSoftwareComponentList(sw_list)
            self.logger.debug("Read SoftwareComponentList")

    def read_instance_id_list(self, element: ET.Element, det: Det):
        """
        Parse InstanceIdList container from XDM.
        """
        ctr_tag = self.find_ctr_tag(element, "InstanceIdList")
        if ctr_tag is not None:
            id_list = InstanceIdList(det, ctr_tag.attrib["name"])
            det.setInstanceIdList(id_list)
            self.logger.debug("Read InstanceIdList")
