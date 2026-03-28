"""
FrIf XDM Parser Module - Extracts AUTOSAR FrIf configuration from EB Tresos XDM files.

Implements:
    - SWR_FRIF_00001: FrIf module parsing
    - SWR_FRIF_00002: General configuration parsing
    - SWR_FRIF_00003: Controller configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.frif_xdm import (
    FrIf, FrIfGeneral, FrIfController, FrIfCluster
)
from ..parser.eb_parser import AbstractEbModelParser


class FrIfXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR FrIf (FlexRay Interface) module configuration.

    Extracts FrIf configuration including general parameters and controllers.

    Implements: SWR_FRIF_00001 (FrIf Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the FrIf XDM parser."""
        super().__init__()
        self.frif = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse FrIf module configuration from XDM element.

        Implements: SWR_FRIF_00001
        """
        if self.get_component_name(element) != "FrIf":
            raise ValueError("Invalid <%s> xdm file" % "FrIf")

        frif = doc.getFrIf()

        self.read_version(element, frif)

        self.logger.info("Parse FrIf ARVersion:<%s> SwVersion:<%s>" % (frif.getArVersion().getVersion(), frif.getSwVersion().getVersion()))

        self.frif = frif

        self.read_frif_general(element, frif)
        self.read_frif_clusters(element, frif)
        self.read_frif_controllers(element, frif)

    def read_frif_general(self, element: ET.Element, frif: FrIf):
        """
        Parse FrIf general configuration.

        Implements: SWR_FRIF_00002
        """
        ctr_tag = self.find_ctr_tag(element, "FrIfGeneral")
        if ctr_tag is not None:
            general = FrIfGeneral(frif, ctr_tag.attrib["name"])
            general.setFrIfDevErrorDetect(self.read_value(ctr_tag, "FrIfDevErrorDetect"))
            general.setFrIfMainFunctionPeriod(self.read_value(ctr_tag, "FrIfMainFunctionPeriod"))
            general.setFrIfMaxNumOfClusters(self.read_value(ctr_tag, "FrIfMaxNumOfClusters"))
            general.setFrIfSupportFrApi(self.read_value(ctr_tag, "FrIfSupportFrApi"))
            general.setFrIfPolarizationSelection(self.read_optional_value(ctr_tag, "FrIfPolarizationSelection"))
            general.setFrIfTransceiverAssignment(self.read_optional_value(ctr_tag, "FrIfTransceiverAssignment"))
            general.setFrIfWakeupPatternSupport(self.read_optional_value(ctr_tag, "FrIfWakeupPatternSupport"))
            general.setFrIfVTPSupport(self.read_optional_value(ctr_tag, "FrIfVTPSupport"))
            general.setFrIfPublicHandleTypeEnum(self.read_optional_value(ctr_tag, "FrIfPublicHandleTypeEnum"))
            general.setFrIfRelocatablePbcfgEnable(self.read_optional_value(ctr_tag, "FrIfRelocatablePbcfgEnable"))
            frif.setFrIfGeneral(general)
            self.logger.debug("Read FrIfGeneral")

    def read_frif_clusters(self, element: ET.Element, frif: FrIf):
        """Parse FrIf cluster configurations."""
        # FrIfConfig is a list, not a ctr, so find the list directly
        config_lst = element.findall(".//d:lst[@name='FrIfConfig']", self.nsmap)
        if config_lst:
            for lst_tag in config_lst:
                for ctr_tag in lst_tag.findall(".//d:ctr[@name[starts-with(., 'FrIfCluster')]]", self.nsmap):
                    cluster = FrIfCluster(frif, ctr_tag.attrib["name"])
                    frif.addFrIfCluster(cluster)
                    self.logger.debug("Read FrIfCluster <%s>" % cluster.getName())

    def read_frif_controllers(self, element: ET.Element, frif: FrIf):
        """
        Parse FrIf controller configurations.

        Implements: SWR_FRIF_00003
        """
        # FrIfConfig is a list, not a ctr, so find the list directly
        config_lst = element.findall(".//d:lst[@name='FrIfConfig']", self.nsmap)
        if config_lst:
            for lst_tag in config_lst:
                # Find controllers in nested FrIfController list or directly in FrIfConfig
                nested_lst = lst_tag.find(".//d:lst[@name='FrIfController']", self.nsmap)
                if nested_lst is not None:
                    for ctr_tag in nested_lst.findall("d:ctr", self.nsmap):
                        controller = FrIfController(frif, ctr_tag.attrib["name"])
                        controller.setFrIfCtrlIdx(self.read_value(ctr_tag, "FrIfCtrlIdx"))
                        controller.setFrIfCtrlMtu(self.read_value(ctr_tag, "FrIfCtrlMtu"))
                        frif.addFrIfController(controller)
                        self.logger.debug("Read FrIfController <%s>" % controller.getName())
                else:
                    # Look for controllers directly in FrIfConfig
                    controllers = lst_tag.findall(".//d:ctr[starts-with(@name, 'FrIfController')]", self.nsmap)
                    for ctr_tag in controllers:
                        controller = FrIfController(frif, ctr_tag.attrib["name"])
                        controller.setFrIfCtrlIdx(self.read_value(ctr_tag, "FrIfCtrlIdx"))
                        controller.setFrIfCtrlMtu(self.read_value(ctr_tag, "FrIfCtrlMtu"))
                        frif.addFrIfController(controller)
                        self.logger.debug("Read FrIfController <%s>" % controller.getName())
