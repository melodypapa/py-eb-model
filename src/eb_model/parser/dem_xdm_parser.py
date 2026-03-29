"""
Dem XDM Parser Module - Extracts AUTOSAR Dem configuration from EB Tresos XDM files.

Implements:
    - SWR_DEM_00001: Dem module parsing
    - SWR_DEM_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.dem_xdm import Dem, DemGeneral
from ..parser.eb_parser import AbstractEbModelParser


class DemXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR Dem module configuration from EB Tresos XDM files.

    Implements: SWR_DEM_00001 (Dem Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the Dem XDM parser."""
        super().__init__()
        self.dem = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse Dem module configuration from XDM element.

        Implements: SWR_DEM_00001
        """
        if self.get_component_name(element) != "Dem":
            raise ValueError("Invalid <%s> xdm file" % "Dem")

        dem = doc.getDem()
        self.read_version(element, dem)

        self.logger.info("Parse Dem ARVersion:<%s> SwVersion:<%s>" %
                        (dem.getArVersion().getVersion(), dem.getSwVersion().getVersion()))

        self.dem = dem
        self.read_dem_general(element, dem)

    def read_dem_general(self, element: ET.Element, dem: Dem):
        """
        Parse DemGeneral container from XDM.

        Implements: SWR_DEM_00002 (General configuration parsing)
        """
        ctr_tag = self.find_ctr_tag(element, "DemGeneral")
        if ctr_tag is not None:
            general = DemGeneral(dem, ctr_tag.attrib["name"])
            general.setDemDevErrorDetect(self.read_value(ctr_tag, "DemDevErrorDetect"))
            general.setDemEnabled(self.read_value(ctr_tag, "DemEnabled"))
            dem.setDemGeneral(general)
            self.logger.debug("Read DemGeneral")