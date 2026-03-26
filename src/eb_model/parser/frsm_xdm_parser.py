"""
FrSM XDM Parser Module - Extracts AUTOSAR FrSM configuration from EB Tresos XDM files.

Implements:
    - SWR_FRSM_00001: FrSM module parsing
    - SWR_FRSM_00002: General configuration parsing
    - SWR_FRSM_00003: Cluster configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.frsm_xdm import (
    FrSM, FrSMGeneral, FrSMCluster, FrSMClusterDemEventParameterRefs
)
from ..parser.eb_parser import AbstractEbModelParser


class FrSMXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR FrSM (FlexRay State Manager) module configuration.

    Extracts FrSM configuration including general parameters and cluster configurations.

    Implements: SWR_FRSM_00001 (FrSM Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the FrSM XDM parser."""
        super().__init__()
        self.frsm = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse FrSM module configuration from XDM element.

        Implements: SWR_FRSM_00001
        """
        if self.get_component_name(element) != "FrSM":
            raise ValueError("Invalid <%s> xdm file" % "FrSM")

        frsm = doc.getFrSM()

        self.read_version(element, frsm)

        self.logger.info("Parse FrSM ARVersion:<%s> SwVersion:<%s>" % (frsm.getArVersion().getVersion(), frsm.getSwVersion().getVersion()))

        self.frsm = frsm

        self.read_frsm_general(element, frsm)
        self.read_frsm_defensive_programming(element, frsm)
        self.read_frsm_clusters(element, frsm)

    def read_frsm_general(self, element: ET.Element, frsm: FrSM):
        """
        Parse FrSM general configuration.

        Implements: SWR_FRSM_00002
        """
        ctr_tag = self.find_ctr_tag(element, "FrSMGeneral")
        if ctr_tag is not None:
            general = FrSMGeneral(frsm, ctr_tag.attrib["name"])
            general.setFrSMDevErrorDetect(self.read_value(ctr_tag, "FrSMDevErrorDetect"))
            general.setFrSMSyncLossErrorIndicationName(self.read_optional_value(ctr_tag, "FrSMSyncLossErrorIndicationName"))
            general.setFrSMVersionInfoApi(self.read_value(ctr_tag, "FrSMVersionInfoApi"))
            general.setFrSMFrTrcvControlEnable(self.read_optional_value(ctr_tag, "FrSMFrTrcvControlEnable"))
            general.setFrSMComMIndicationEnable(self.read_value(ctr_tag, "FrSMComMIndicationEnable"))
            general.setFrSMSingleClstOptEnable(self.read_value(ctr_tag, "FrSMSingleClstOptEnable"))
            general.setFrSMReportToBswMEnable(self.read_value(ctr_tag, "FrSMReportToBswMEnable"))
            general.setFrSMSetEcuPassiveEnable(self.read_optional_value(ctr_tag, "FrSMSetEcuPassiveEnable"))
            general.setFrSMFrNmStartupErrorEnable(self.read_value(ctr_tag, "FrSMFrNmStartupErrorEnable"))
            general.setFrSMKeySlotOnlyModeEnable(self.read_optional_value(ctr_tag, "FrSMKeySlotOnlyModeEnable"))
            general.setFrSMSyncLossErrorIndicationHeaderName(self.read_optional_value(ctr_tag, "FrSMSyncLossErrorIndicationHeaderName"))
            general.setFrSMMultiCoreSupportEnable(self.read_optional_value(ctr_tag, "FrSMMultiCoreSupportEnable"))
            frsm.setFrSMGeneral(general)
            self.logger.debug("Read FrSMGeneral")

    def read_frsm_defensive_programming(self, element: ET.Element, frsm: FrSM):
        """Parse FrSM defensive programming configuration."""
        ctr_tag = self.find_ctr_tag(element, "FrSMDefensiveProgramming")
        if ctr_tag is not None:
            general = frsm.getFrSMGeneral()
            if general is not None:
                general.setFrSMDefProgEnabled(self.read_value(ctr_tag, "FrSMDefProgEnabled"))
                general.setFrSMPrecondAssertEnabled(self.read_value(ctr_tag, "FrSMPrecondAssertEnabled"))
                general.setFrSMPostcondAssertEnabled(self.read_value(ctr_tag, "FrSMPostcondAssertEnabled"))
                general.setFrSMStaticAssertEnabled(self.read_value(ctr_tag, "FrSMStaticAssertEnabled"))
                general.setFrSMUnreachAssertEnabled(self.read_value(ctr_tag, "FrSMUnreachAssertEnabled"))
                general.setFrSMInvariantAssertEnabled(self.read_value(ctr_tag, "FrSMInvariantAssertEnabled"))
            self.logger.debug("Read FrSMDefensiveProgramming")

    def read_frsm_clusters(self, element: ET.Element, frsm: FrSM):
        """
        Parse FrSM cluster configurations.

        Implements: SWR_FRSM_00003
        """
        config_lst = self.find_ctr_tag_list(element, "FrSMConfig")
        if config_lst:
            for lst_tag in config_lst:
                for ctr_tag in self.find_ctr_tag_list(lst_tag, "FrSMCluster"):
                    cluster = FrSMCluster(frsm, ctr_tag.attrib["name"])

                    # Read cluster-level parameters
                    cluster.setFrSMCheckWakeupReason(self.read_optional_value(ctr_tag, "FrSMCheckWakeupReason"))
                    cluster.setFrSMDelayStartupWithoutWakeup(self.read_optional_value(ctr_tag, "FrSMDelayStartupWithoutWakeup"))
                    cluster.setFrSMDurationT1(self.read_value(ctr_tag, "FrSMDurationT1"))
                    cluster.setFrSMDurationT2(self.read_value(ctr_tag, "FrSMDurationT2"))
                    cluster.setFrSMDurationT3(self.read_value(ctr_tag, "FrSMDurationT3"))
                    cluster.setFrSMIsColdstartEcu(self.read_optional_value(ctr_tag, "FrSMIsColdstartEcu"))
                    cluster.setFrSMIsWakeupEcu(self.read_optional_value(ctr_tag, "FrSMIsWakeupEcu"))
                    cluster.setFrSMMainFunctionCycleTime(self.read_value(ctr_tag, "FrSMMainFunctionCycleTime"))
                    cluster.setFrSMMinNumberOfColdstarter(self.read_optional_value(ctr_tag, "FrSMMinNumberOfColdstarter"))
                    cluster.setFrSMNumWakeupPatterns(self.read_value(ctr_tag, "FrSMNumWakeupPatterns"))
                    cluster.setFrSMStartupRepetitions(self.read_optional_value(ctr_tag, "FrSMStartupRepetitions"))
                    cluster.setFrSMStartupRepetitionsWithWakeup(self.read_optional_value(ctr_tag, "FrSMStartupRepetitionsWithWakeup"))

                    # Read references
                    cluster.setFrSMComMNetworkHandleRef(self.read_ref_value(ctr_tag, "FrSMComMNetworkHandleRef"))
                    cluster.setFrSMFrIfClusterRef(self.read_ref_value(ctr_tag, "FrSMFrIfClusterRef"))

                    # Read DemEventParameterRefs if present
                    dem_ctr = self.find_ctr_tag(ctr_tag, "FrSMClusterDemEventParameterRefs")
                    if dem_ctr is not None:
                        dem_refs = FrSMClusterDemEventParameterRefs(cluster, dem_ctr.attrib["name"])
                        dem_refs.setFrSMClusterStartupRef(self.read_ref_value(dem_ctr, "FRSM_E_CLUSTER_STARTUP"))
                        dem_refs.setFrSMClusterSyncLossRef(self.read_ref_value(dem_ctr, "FRSM_E_CLUSTER_SYNC_LOSS"))
                        cluster.setFrSMClusterDemEventParameterRefs(dem_refs)

                    frsm.addFrSMCluster(cluster)
                    self.logger.debug("Read FrSMCluster <%s>" % cluster.getName())