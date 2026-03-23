import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.det_xdm import Det, DetGeneral, DetErrorHook, DetInitError
from ..parser.eb_parser import AbstractEbModelParser


class DetXdmParser(AbstractEbModelParser):
    def __init__(self) -> None:
        super().__init__()

        self.det = None

    def parse(self, element: ET.Element, doc: EBModel):
        if self.get_component_name(element) != "Det":
            raise ValueError("Invalid <%s> xdm file" % "Det")

        det = doc.getDet()

        self.read_version(element, det)

        self.logger.info("Parse Det ARVersion:<%s> SwVersion:<%s>" % (det.getArVersion().getVersion(), det.getSwVersion().getVersion()))

        self.det = det

        self.read_det_general(element, det)
        self.read_det_error_hook(element, det)
        self.read_det_init_error(element, det)

    def read_det_general(self, element: ET.Element, det: Det):
        ctr_tag = self.find_ctr_tag(element, "DetGeneral")
        if ctr_tag is not None:
            general = DetGeneral(det, ctr_tag.attrib["name"])
            general.setDetDevErrorDetect(self.read_value(ctr_tag, "DetDevErrorDetect"))
            general.setDetEnabled(self.read_value(ctr_tag, "DetEnabled"))
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
