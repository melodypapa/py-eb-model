"""
AUTOSAR model classes organized by functional stack.

This module provides access to all AUTOSAR model classes used for parsing
EB Tresos XDM configuration files.

Implements: SWR_MODEL_00001 (Model layer organization)
"""

# Core/Base
from eb_model.models.core.abstract import (
    EcucObject,
    EcucEnumerationParamDef,
    EcucParamConfContainerDef,
    EcucRefType,
    Version,
    Module,
)
from eb_model.models.core.eb_doc import AbstractModel, EBModel, PreferenceModel
from eb_model.models.core.importer_xdm import SystemDescriptionImporter
from eb_model.models.core.os_xdm import (
    OsAlarmAction,
    OsAlarmAutostart,
    OsAlarmActivateTask,
    OsAlarmCallback,
    OsAlarmIncrementCounter,
    OsAlarmSetEvent,
    OsAlarm,
    OsApplicationHooks,
    OsApplicationTrustedFunction,
    OsAppMode,
    OsApplication,
    OsDriver,
    OsTimeConstant,
    OsCounter,
    OsResource,
    OsIsrResourceLock,
    OsIsrTimingProtection,
    OsIsr,
    OsTaskAutostart,
    OsTaskResourceLock,
    OsTaskTimingProtection,
    OsTask,
    OsScheduleTableAutostart,
    OsScheduleTblAdjustableExpPoint,
    OsScheduleTableTaskActivation,
    OsScheduleTableEventSetting,
    OsScheduleTableExpiryPoint,
    OsScheduleTable,
    MkMemoryRegion,
    MkMemoryProtection,
    MkFunction,
    MkStack,
    MkThreadCustomization,
    MkOptimization,
    OsMicrokernel,
    CommonPublishedInformation,
    PublishedInformation,
    OsHwIncrementer,
    OsEvent,
    OsSpinlock,
    OsPeripheralArea,
    OsOS,
    OsHooks,
    OsCoreConfig,
    OsAutosarCustomization,
    Os,
)
from eb_model.models.core.rte_xdm import (
    RteBswGeneral,
    RteBswEventToIsrMapping,
    RteBswExclusiveAreaImpl,
    RteBswExternalTriggerConfig,
    RteBswInternalTriggerConfig,
    RteBswRequiredModeGroupConnection,
    RteBswRequiredSenderReceiverConnection,
    RteBswRequiredClientServerConnection,
    RteBswRequiredTriggerConnection,
    RteGeneration,
    ComTaskConfiguration,
    BswConfiguration,
    OsCounterAssignments,
    CooperativeTasks,
    TaskChain,
    RteImplicitCommunication,
    RteInitializationBehavior,
    RteInitializationRunnableBatch,
    RteOsInteraction,
    RteModeToScheduleTableMapping,
    RteRips,
    DataMappings,
    RteExclusiveAreaImplementation,
    RteExternalTriggerConfig,
    RteInternalTriggerConfig,
    RteNvRamAllocation,
    RteSwComponentType,
    RteEventToIsrMapping,
    AbstractEventToTaskMapping,
    RteEventToTaskMapping,
    RteEventToTaskMappingV3,
    RteEventToTaskMappingV4,
    RteBswEventToTaskMapping,
    RteBswEventToTaskMappingV3,
    RteBswEventToTaskMappingV4,
    AbstractRteInstance,
    RteSwComponentInstance,
    RteBswModuleInstance,
    Rte,
)
from eb_model.models.core.tm_xdm import (
    TmGeneral,
    TmInterruptSynchronization,
    TmTickTime,
    TmTrigger,
    Tm,
)
from eb_model.models.core.pbcfgm_xdm import PbcfgMProtectionSet, PbcfgMCoreProtectionSet, PbcfgMGeneral, PbcfgM
from eb_model.models.core.ecum_xdm import (
    EcuMCommonConfiguration,
    EcuMDefaultShutdownTarget,
    EcuMDriverInitItem,
    EcuMDriverInitListOne,
    EcuMDriverInitListZero,
    EcuMDriverRestartList,
    EcuMSleepMode,
    EcuMWakeupSource,
    EcuMDemEventParameterRefs,
    EcuMFixedConfiguration,
    EcuMDriverInitListThree,
    EcuMDriverInitListTwo,
    EcuMFixedUserConfig,
    EcuMTTII,
    EcuMWdgM,
    EcuMFlexConfiguration,
    EcuMAlarmClock,
    EcuMFlexUserConfig,
    EcuMGoDownAllowedUsers,
    EcuMResetMode,
    EcuMSetClockAllowedUsers,
    EcuMShutdownCause,
    EcuMShutdownTarget,
    EcuMDefensiveProgramming,
    EcuMFixedGeneral,
    EcuMFlexGeneral,
    EcuMServiceAPI,
    ReportToDem,
    EcuMStartup,
    EcuMShutdown,
    EcuMAlarm,
    EcuMGeneral,
    EcuM,
)
from eb_model.models.core.ecuc_xdm import (
    EcucPartitionSoftwareComponentInstanceRef,
    EcucPartition,
    EcucGeneral,
    EcucHardware,
    EcucCoreDefinition,
    EcucPduCollection,
    MetaDataType,
    MetaDataItem,
    Pdu,
    EcucPduDedicatedPartition,
    EcucPostBuildVariants,
    EcucVariationResolver,
    EcucPartitionCollection,
    EcuC,
)
from eb_model.models.core.det_xdm import (
    DetServiceAPI,
    DetNotification,
    DetDefensiveProgramming,
    SoftwareComponentList,
    InstanceIdList,
    DetErrorHook,
    DetInitError,
    DetGeneral,
    Det,
)
from eb_model.models.core.bswm_xdm import BswMModeCondition, BswMModeDeclaration, BswMGeneral, BswM

# LIN Family
from eb_model.models.lin_stack.linif_xdm import LinIfGeneral, LinIfChannel, LinIfFrame, LinIf
from eb_model.models.lin_stack.linsm_xdm import LinSMGeneral, LinSMChannel, LinSM
from eb_model.models.lin_stack.lintp_xdm import LinTpGeneral, LinTpRxNSdu, LinTpTxNSdu, LinTp

# CAN Family
from eb_model.models.can_stack.canif_xdm import (
    CanIfGeneral,
    CanIfCtrlCfg,
    CanIfTrcvCfg,
    CanIfDispatchCfg,
    CanIfBufferCfg,
    CanIfHrhCfg,
    CanIfHthCfg,
    CanIfRxPduCfg,
    CanIfTxPduCfg,
    CanIf,
)
from eb_model.models.can_stack.cannm_xdm import (
    CanNmGeneral,
    CanNmGlobalConfig,
    CanNmChannel,
    CanNmRxPdu,
    CanNmTxPdu,
    CanNmPnFilterMaskByte,
    CanNmPnInfo,
    CanNm,
)
from eb_model.models.can_stack.cansm_xdm import CanSMGeneral, CanSMManagerNetwork, CanSMController, CanSMDemEventParameterRefs, CanSM
from eb_model.models.can_stack.cantp_xdm import CanTpGeneral, CanTpChannel, CanTpRxNSdu, CanTpTxNSdu, CanTp

# Ethernet Family
from eb_model.models.eth_stack.ethif_xdm import (
    EthIfGeneral,
    EthIfController,
    EthIfFrameOwnerConfig,
    EthIfPhysController,
    EthIfSwitch,
    EthIfSwitchPortGroup,
    EthIfTransceiver,
    EthIfRxIndicationConfig,
    EthIfTxConfirmationConfig,
    EthIfEthControllerType,
    EthIfEthTrcvType,
    EthIfEthSwtType,
    EthIf,
)
from eb_model.models.eth_stack.ethsm_xdm import EthSMGeneral, EthSMDemEventParameterRefs, EthSMNetwork, EthSM
from eb_model.models.eth_stack.tcpip_xdm import TcpIpGeneral, TcpIpOffloadChecksum, TcpIpIpV4Ctrl, TcpIpIpV6Ctrl, TcpIpCtrl, TcpIpLocalAddr, TcpIp
from eb_model.models.eth_stack.soad_xdm import (
    SoAdGeneral,
    SoAdSocketRemoteAddress,
    SoAdSocketUdp,
    SoAdSocketTcp,
    SoAdSocketConnection,
    SoAdSocketConnectionGroup,
    SoAdPduRouteDest,
    SoAdPduRoute,
    SoAdSocketRouteDest,
    SoAdSocketRoute,
    SoAdRoutingGroup,
    SoAd,
)
from eb_model.models.eth_stack.udpnm_xdm import (
    UdpNmGeneral,
    UdpNmChannelIdentifiers,
    UdpNmRxPdu,
    UdpNmTxPdu,
    UdpNmUserDataTxPdu,
    UdpNmUserDataRxPdu,
    UdpNmChannel,
    UdpNm,
)
from eb_model.models.eth_stack.doip_xdm import (
    DoIPGeneral,
    DoIPPduRRxPdu,
    DoIPPduRTxPdu,
    DoIPChannel,
    DoIPSoAdRxPdu,
    DoIPSoAdTxPdu,
    DoIPTcpConnection,
    DoIPUdpConnection,
    DoIPUdpVehicleAnnouncement,
    DoIPConnections,
    DoIP,
)
from eb_model.models.eth_stack.someiptp_xdm import (
    SomeIpTpGeneral,
    SomeIpTpRxNPdu,
    SomeIpTpRxNSdu,
    SomeIpTpTxNPdu,
    SomeIpTpTxNSdu,
    SomeIpTpChannel,
    SomeIpTp,
)

# FlexRay Family
from eb_model.models.fr_stack.frif_xdm import FrIfGeneral, FrIfCluster, FrIfController, FrIf
from eb_model.models.fr_stack.frnm_xdm import FrNmGeneral, FrNmChannelIdentifiers, FrNmRxPdu, FrNmTxPdu, FrNmChannel, FrNm
from eb_model.models.fr_stack.frsm_xdm import FrSMGeneral, FrSMClusterDemEventParameterRefs, FrSMCluster, FrSM
from eb_model.models.fr_stack.frtp_xdm import (
    FrTpGeneral,
    FrTpConnectionLimitConfig,
    FrTpConnectionControl,
    FrTpRxSdu,
    FrTpTxSdu,
    FrTpConnection,
    FrTp,
)
from eb_model.models.fr_stack.frartp_xdm import FrArTpGeneral, FrArTpRxSdu, FrArTpTxSdu, FrArTpPdu, FrArTpConnection, FrArTpChannel, FrArTp

# Communication
from eb_model.models.com_stack.com_xdm import ComGeneral, Com
from eb_model.models.com_stack.ldcom_xdm import LdCom
from eb_model.models.com_stack.comm_xdm import ComMChannel, ComM
from eb_model.models.com_stack.pdur_xdm import PduRRoutingTableEntry, PduR
from eb_model.models.com_stack.ipdum_xdm import IpduMDynPdu, IpduM
from eb_model.models.com_stack.nm_xdm import NmChannel, Nm

# Memory
from eb_model.models.mem_stack.memif_xdm import MemIfInit, MemIf
from eb_model.models.mem_stack.fee_xdm import FeeGeneral, Fee
from eb_model.models.mem_stack.ea_xdm import EaGeneral, Ea
from eb_model.models.mem_stack.memmap_xdm import MemMapCommon, MemMap
from eb_model.models.mem_stack.memacc_xdm import MemAccCommon, MemAcc
from eb_model.models.mem_stack.crc_xdm import CrcConfig, Crc
from eb_model.models.mem_stack.nvm_xdm import (
    NvMTargetBlockReference,
    NvMEaRef,
    NvMFeeRef,
    NvMCommon,
    NvMSingleBlockCallback,
    NvMInitBlockCallback,
    NvMDefensiveProgramming,
    NvMCommonCryptoSecurityParameters,
    NvMServiceAPI,
    NvmDemEventParameterRefs,
    MultiCoreCallout,
    NvMBlockDescriptor,
    NvM,
)

# Crypto/Security
from eb_model.models.crypto_stack.crypto_xdm import CryptoGeneral, Crypto
from eb_model.models.crypto_stack.cryif_xdm import CryIfGeneral, CryIf
from eb_model.models.crypto_stack.csm_xdm import CsmGeneral, Csm
from eb_model.models.crypto_stack.secoc_xdm import SecOCGeneral, SecOC

# Diagnostics/Events
from eb_model.models.diag_stack.dcm_xdm import DcmGeneral, Dcm
from eb_model.models.diag_stack.dem_xdm import DemGeneral, Dem
from eb_model.models.diag_stack.dlt_xdm import DltGeneral, Dlt
from eb_model.models.diag_stack.fim_xdm import FiMGeneral, FiM

# J1939 Family
from eb_model.models.j1939_stack.j1939dcm_xdm import J1939DcmGeneral, J1939Dcm
from eb_model.models.j1939_stack.j1939nm_xdm import J1939NmGeneral, J1939Nm
from eb_model.models.j1939_stack.j1939rm_xdm import J1939RmGeneral, J1939Rm
from eb_model.models.j1939_stack.j1939tp_xdm import J1939TpGeneral, J1939Tp

__all__ = [
    "EcucObject", "EcucEnumerationParamDef", "EcucParamConfContainerDef", "EcucRefType",
    "Version", "Module", "AbstractModel", "EBModel", "PreferenceModel",
    "SystemDescriptionImporter",
    "OsAlarmAction", "OsAlarmAutostart", "OsAlarmActivateTask", "OsAlarmCallback",
    "OsAlarmIncrementCounter", "OsAlarmSetEvent", "OsAlarm", "OsApplicationHooks",
    "OsApplicationTrustedFunction", "OsAppMode", "OsApplication", "OsDriver",
    "OsTimeConstant", "OsCounter", "OsResource", "OsIsrResourceLock",
    "OsIsrTimingProtection", "OsIsr", "OsTaskAutostart", "OsTaskResourceLock",
    "OsTaskTimingProtection", "OsTask", "OsScheduleTableAutostart",
    "OsScheduleTblAdjustableExpPoint", "OsScheduleTableTaskActivation",
    "OsScheduleTableEventSetting", "OsScheduleTableExpiryPoint", "OsScheduleTable",
    "MkMemoryRegion", "MkMemoryProtection", "MkFunction", "MkStack",
    "MkThreadCustomization", "MkOptimization", "OsMicrokernel",
    "CommonPublishedInformation", "PublishedInformation", "OsHwIncrementer",
    "OsEvent", "OsSpinlock", "OsPeripheralArea", "OsOS", "OsHooks",
    "OsCoreConfig", "OsAutosarCustomization", "Os",
    "RteBswGeneral", "RteBswEventToIsrMapping", "RteBswExclusiveAreaImpl",
    "RteBswExternalTriggerConfig", "RteBswInternalTriggerConfig",
    "RteBswRequiredModeGroupConnection", "RteBswRequiredSenderReceiverConnection",
    "RteBswRequiredClientServerConnection", "RteBswRequiredTriggerConnection",
    "RteGeneration", "ComTaskConfiguration", "BswConfiguration",
    "OsCounterAssignments", "CooperativeTasks", "TaskChain",
    "RteImplicitCommunication", "RteInitializationBehavior",
    "RteInitializationRunnableBatch", "RteOsInteraction",
    "RteModeToScheduleTableMapping", "RteRips", "DataMappings",
    "RteExclusiveAreaImplementation", "RteExternalTriggerConfig",
    "RteInternalTriggerConfig", "RteNvRamAllocation", "RteSwComponentType",
    "RteEventToIsrMapping", "AbstractEventToTaskMapping", "RteEventToTaskMapping",
    "RteEventToTaskMappingV3", "RteEventToTaskMappingV4", "RteBswEventToTaskMapping",
    "RteBswEventToTaskMappingV3", "RteBswEventToTaskMappingV4",
    "AbstractRteInstance", "RteSwComponentInstance", "RteBswModuleInstance", "Rte",
    "TmGeneral", "TmInterruptSynchronization", "TmTickTime", "TmTrigger", "Tm",
    "PbcfgMProtectionSet", "PbcfgMCoreProtectionSet", "PbcfgMGeneral", "PbcfgM",
    "EcuMCommonConfiguration", "EcuMDefaultShutdownTarget", "EcuMDriverInitItem",
    "EcuMDriverInitListOne", "EcuMDriverInitListZero", "EcuMDriverRestartList",
    "EcuMSleepMode", "EcuMWakeupSource", "EcuMDemEventParameterRefs",
    "EcuMFixedConfiguration", "EcuMDriverInitListThree", "EcuMDriverInitListTwo",
    "EcuMFixedUserConfig", "EcuMTTII", "EcuMWdgM", "EcuMFlexConfiguration",
    "EcuMAlarmClock", "EcuMFlexUserConfig", "EcuMGoDownAllowedUsers",
    "EcuMResetMode", "EcuMSetClockAllowedUsers", "EcuMShutdownCause",
    "EcuMShutdownTarget", "EcuMDefensiveProgramming", "EcuMFixedGeneral",
    "EcuMFlexGeneral", "EcuMServiceAPI", "ReportToDem", "EcuMStartup",
    "EcuMShutdown", "EcuMAlarm", "EcuMGeneral", "EcuM",
    "EcucPartitionSoftwareComponentInstanceRef", "EcucPartition", "EcucGeneral",
    "EcucHardware", "EcucCoreDefinition", "EcucPduCollection", "MetaDataType",
    "MetaDataItem", "Pdu", "EcucPduDedicatedPartition", "EcucPostBuildVariants",
    "EcucVariationResolver", "EcucPartitionCollection", "EcuC",
    "DetServiceAPI", "DetNotification", "DetDefensiveProgramming",
    "SoftwareComponentList", "InstanceIdList", "DetErrorHook", "DetInitError",
    "DetGeneral", "Det",
    "BswMModeCondition", "BswMModeDeclaration", "BswMGeneral", "BswM",
    "LinIfGeneral", "LinIfChannel", "LinIfFrame", "LinIf", "LinSMGeneral",
    "LinSMChannel", "LinSM", "LinTpGeneral", "LinTpRxNSdu", "LinTpTxNSdu",
    "LinTp",
    "CanIfGeneral", "CanIfCtrlCfg", "CanIfTrcvCfg", "CanIfDispatchCfg",
    "CanIfBufferCfg", "CanIfHrhCfg", "CanIfHthCfg", "CanIfRxPduCfg",
    "CanIfTxPduCfg", "CanIf",
    "CanNmGeneral", "CanNmGlobalConfig", "CanNmChannel", "CanNmRxPdu",
    "CanNmTxPdu", "CanNmPnFilterMaskByte", "CanNmPnInfo", "CanNm",
    "CanSMGeneral", "CanSMManagerNetwork", "CanSMController",
    "CanSMDemEventParameterRefs", "CanSM",
    "CanTpGeneral", "CanTpChannel", "CanTpRxNSdu", "CanTpTxNSdu", "CanTp",
    "EthIfGeneral", "EthIfController", "EthIfFrameOwnerConfig",
    "EthIfPhysController", "EthIfSwitch", "EthIfSwitchPortGroup", "EthIfTransceiver",
    "EthIfRxIndicationConfig", "EthIfTxConfirmationConfig",
    "EthIfEthControllerType", "EthIfEthTrcvType", "EthIfEthSwtType", "EthIf",
    "EthSMGeneral", "EthSMDemEventParameterRefs", "EthSMNetwork", "EthSM",
    "TcpIpGeneral", "TcpIpOffloadChecksum", "TcpIpIpV4Ctrl", "TcpIpIpV6Ctrl",
    "TcpIpCtrl", "TcpIpLocalAddr", "TcpIp",
    "SoAdGeneral", "SoAdSocketRemoteAddress", "SoAdSocketUdp", "SoAdSocketTcp",
    "SoAdSocketConnection", "SoAdSocketConnectionGroup", "SoAdPduRouteDest",
    "SoAdPduRoute", "SoAdSocketRouteDest", "SoAdSocketRoute", "SoAdRoutingGroup",
    "SoAd",
    "UdpNmGeneral", "UdpNmChannelIdentifiers", "UdpNmRxPdu", "UdpNmTxPdu",
    "UdpNmUserDataTxPdu", "UdpNmUserDataRxPdu", "UdpNmChannel", "UdpNm",
    "DoIPGeneral", "DoIPPduRRxPdu", "DoIPPduRTxPdu", "DoIPChannel",
    "DoIPSoAdRxPdu", "DoIPSoAdTxPdu", "DoIPTcpConnection", "DoIPUdpConnection",
    "DoIPUdpVehicleAnnouncement", "DoIPConnections", "DoIP",
    "SomeIpTpGeneral", "SomeIpTpRxNPdu", "SomeIpTpRxNSdu", "SomeIpTpTxNPdu",
    "SomeIpTpTxNSdu", "SomeIpTpChannel", "SomeIpTp",
    "FrIfGeneral", "FrIfCluster", "FrIfController", "FrIf", "FrNmGeneral",
    "FrNmChannelIdentifiers", "FrNmRxPdu", "FrNmTxPdu", "FrNmChannel", "FrNm",
    "FrSMGeneral", "FrSMClusterDemEventParameterRefs", "FrSMCluster", "FrSM",
    "FrTpGeneral", "FrTpConnectionLimitConfig", "FrTpConnectionControl",
    "FrTpRxSdu", "FrTpTxSdu", "FrTpConnection", "FrTp",
    "FrArTpGeneral", "FrArTpRxSdu", "FrArTpTxSdu", "FrArTpPdu",
    "FrArTpConnection", "FrArTpChannel", "FrArTp",
    "ComGeneral", "Com", "LdCom", "ComMChannel", "ComM",
    "PduRRoutingTableEntry", "PduR", "IpduMDynPdu", "IpduM", "NmChannel", "Nm",
    "MemIfInit", "MemIf", "FeeGeneral", "Fee", "EaGeneral", "Ea",
    "MemMapCommon", "MemMap", "MemAccCommon", "MemAcc", "CrcConfig", "Crc",
    "NvMTargetBlockReference", "NvMEaRef", "NvMFeeRef", "NvMCommon",
    "NvMSingleBlockCallback", "NvMInitBlockCallback", "NvMDefensiveProgramming",
    "NvMCommonCryptoSecurityParameters", "NvMServiceAPI", "NvmDemEventParameterRefs",
    "MultiCoreCallout", "NvMBlockDescriptor", "NvM",
    "CryptoGeneral", "Crypto", "CryIfGeneral", "CryIf", "CsmGeneral", "Csm",
    "SecOCGeneral", "SecOC",
    "DcmGeneral", "Dcm", "DemGeneral", "Dem", "DltGeneral", "Dlt", "FiMGeneral",
    "FiM",
    "J1939DcmGeneral", "J1939Dcm", "J1939NmGeneral", "J1939Nm", "J1939RmGeneral",
    "J1939Rm", "J1939TpGeneral", "J1939Tp",
]
