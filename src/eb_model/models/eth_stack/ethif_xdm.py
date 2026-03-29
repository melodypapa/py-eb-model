from typing import List, Optional
import logging
from eb_model.models.core.abstract import EcucParamConfContainerDef, EcucRefType, Module


class EthIfGeneral(EcucParamConfContainerDef):
    """EthIf general configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ethIfDevErrorDetect: bool = None
        self.ethIfEnableRxInterrupt: bool = None
        self.ethIfMainFunctionPeriod: float = None
        self.ethIfMaxTrcvsTotal: int = None
        self.ethIfSupportEthAPI: str = None
        self.ethIfPublicHandleTypeEnum: str = None
        self.ethIfMaxCtrl: int = None
        self.ethIfMaxPhyCtrl: int = None
        self.ethIfMaxEthSwitches: int = None
        self.ethIfMaxSwtPorts: int = None
        self.ethIfRelocatablePbcfgEnable: bool = None
        self.ethIfVLANSupportEnable: bool = None

        # Defensive programming
        self.ethIfDefProgEnabled: bool = None
        self.ethIfPrecondAssertEnabled: bool = None
        self.ethIfPostcondAssertEnabled: bool = None
        self.ethIfStaticAssertEnabled: bool = None
        self.ethIfUnreachAssertEnabled: bool = None
        self.ethIfInvariantAssertEnabled: bool = None

    def getEthIfDevErrorDetect(self) -> bool:
        return self.ethIfDevErrorDetect

    def setEthIfDevErrorDetect(self, value: bool):
        if value is not None:
            self.ethIfDevErrorDetect = value
        return self

    def getEthIfEnableRxInterrupt(self) -> bool:
        return self.ethIfEnableRxInterrupt

    def setEthIfEnableRxInterrupt(self, value: bool):
        if value is not None:
            self.ethIfEnableRxInterrupt = value
        return self

    def getEthIfMainFunctionPeriod(self) -> float:
        return self.ethIfMainFunctionPeriod

    def setEthIfMainFunctionPeriod(self, value: float):
        if value is not None:
            self.ethIfMainFunctionPeriod = value
        return self

    def getEthIfMaxTrcvsTotal(self) -> int:
        return self.ethIfMaxTrcvsTotal

    def setEthIfMaxTrcvsTotal(self, value: int):
        if value is not None:
            self.ethIfMaxTrcvsTotal = value
        return self

    def getEthIfSupportEthAPI(self) -> str:
        return self.ethIfSupportEthAPI

    def setEthIfSupportEthAPI(self, value: str):
        if value is not None:
            self.ethIfSupportEthAPI = value
        return self

    def getEthIfPublicHandleTypeEnum(self) -> str:
        return self.ethIfPublicHandleTypeEnum

    def setEthIfPublicHandleTypeEnum(self, value: str):
        if value is not None:
            self.ethIfPublicHandleTypeEnum = value
        return self

    def getEthIfMaxCtrl(self) -> int:
        return self.ethIfMaxCtrl

    def setEthIfMaxCtrl(self, value: int):
        if value is not None:
            self.ethIfMaxCtrl = value
        return self

    def getEthIfMaxPhyCtrl(self) -> int:
        return self.ethIfMaxPhyCtrl

    def setEthIfMaxPhyCtrl(self, value: int):
        if value is not None:
            self.ethIfMaxPhyCtrl = value
        return self

    def getEthIfMaxEthSwitches(self) -> int:
        return self.ethIfMaxEthSwitches

    def setEthIfMaxEthSwitches(self, value: int):
        if value is not None:
            self.ethIfMaxEthSwitches = value
        return self

    def getEthIfMaxSwtPorts(self) -> int:
        return self.ethIfMaxSwtPorts

    def setEthIfMaxSwtPorts(self, value: int):
        if value is not None:
            self.ethIfMaxSwtPorts = value
        return self

    def getEthIfRelocatablePbcfgEnable(self) -> bool:
        return self.ethIfRelocatablePbcfgEnable

    def setEthIfRelocatablePbcfgEnable(self, value: bool):
        if value is not None:
            self.ethIfRelocatablePbcfgEnable = value
        return self

    def getEthIfVLANSupportEnable(self) -> bool:
        return self.ethIfVLANSupportEnable

    def setEthIfVLANSupportEnable(self, value: bool):
        if value is not None:
            self.ethIfVLANSupportEnable = value
        return self

    # Defensive programming getters/setters
    def getEthIfDefProgEnabled(self) -> bool:
        return self.ethIfDefProgEnabled

    def setEthIfDefProgEnabled(self, value: bool):
        if value is not None:
            self.ethIfDefProgEnabled = value
        return self

    def getEthIfPrecondAssertEnabled(self) -> bool:
        return self.ethIfPrecondAssertEnabled

    def setEthIfPrecondAssertEnabled(self, value: bool):
        if value is not None:
            self.ethIfPrecondAssertEnabled = value
        return self

    def getEthIfPostcondAssertEnabled(self) -> bool:
        return self.ethIfPostcondAssertEnabled

    def setEthIfPostcondAssertEnabled(self, value: bool):
        if value is not None:
            self.ethIfPostcondAssertEnabled = value
        return self

    def getEthIfStaticAssertEnabled(self) -> bool:
        return self.ethIfStaticAssertEnabled

    def setEthIfStaticAssertEnabled(self, value: bool):
        if value is not None:
            self.ethIfStaticAssertEnabled = value
        return self

    def getEthIfUnreachAssertEnabled(self) -> bool:
        return self.ethIfUnreachAssertEnabled

    def setEthIfUnreachAssertEnabled(self, value: bool):
        if value is not None:
            self.ethIfUnreachAssertEnabled = value
        return self

    def getEthIfInvariantAssertEnabled(self) -> bool:
        return self.ethIfInvariantAssertEnabled

    def setEthIfInvariantAssertEnabled(self, value: bool):
        if value is not None:
            self.ethIfInvariantAssertEnabled = value
        return self


class EthIfController(EcucParamConfContainerDef):
    """EthIf controller configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ethIfCtrlIdx: int = None
        self.ethIfCtrlMtu: int = None
        self.ethIfMaxTxBufsTotal: int = None
        self.ethIfVlanId: int = None
        self.ethIfEthTrcvRef: EcucRefType = None
        self.ethIfPhysControllerRef: EcucRefType = None
        self.ethIfSwitchRefOrPortGroupRef: EcucRefType = None

    def getEthIfCtrlIdx(self) -> int:
        return self.ethIfCtrlIdx

    def setEthIfCtrlIdx(self, value: int):
        if value is not None:
            self.ethIfCtrlIdx = value
        return self

    def getEthIfCtrlMtu(self) -> int:
        return self.ethIfCtrlMtu

    def setEthIfCtrlMtu(self, value: int):
        if value is not None:
            self.ethIfCtrlMtu = value
        return self

    def getEthIfMaxTxBufsTotal(self) -> int:
        return self.ethIfMaxTxBufsTotal

    def setEthIfMaxTxBufsTotal(self, value: int):
        if value is not None:
            self.ethIfMaxTxBufsTotal = value
        return self

    def getEthIfVlanId(self) -> int:
        return self.ethIfVlanId

    def setEthIfVlanId(self, value: int):
        if value is not None:
            self.ethIfVlanId = value
        return self

    def getEthIfEthTrcvRef(self) -> EcucRefType:
        return self.ethIfEthTrcvRef

    def setEthIfEthTrcvRef(self, value: EcucRefType):
        if value is not None:
            self.ethIfEthTrcvRef = value
        return self

    def getEthIfPhysControllerRef(self) -> EcucRefType:
        return self.ethIfPhysControllerRef

    def setEthIfPhysControllerRef(self, value: EcucRefType):
        if value is not None:
            self.ethIfPhysControllerRef = value
        return self

    def getEthIfSwitchRefOrPortGroupRef(self) -> EcucRefType:
        return self.ethIfSwitchRefOrPortGroupRef

    def setEthIfSwitchRefOrPortGroupRef(self, value: EcucRefType):
        if value is not None:
            self.ethIfSwitchRefOrPortGroupRef = value
        return self


class EthIfFrameOwnerConfig(EcucParamConfContainerDef):
    """EthIf frame owner configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ethIfFrameType: int = None
        self.ethIfOwner: int = None

    def getEthIfFrameType(self) -> int:
        return self.ethIfFrameType

    def setEthIfFrameType(self, value: int):
        if value is not None:
            self.ethIfFrameType = value
        return self

    def getEthIfOwner(self) -> int:
        return self.ethIfOwner

    def setEthIfOwner(self, value: int):
        if value is not None:
            self.ethIfOwner = value
        return self


class EthIfPhysController(EcucParamConfContainerDef):
    """EthIf physical controller configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ethIfPhysControllerIdx: int = None
        self.ethIfEthCtrlRef: EcucRefType = None
        self.ethIfWEthCtrlRef: EcucRefType = None

    def getEthIfPhysControllerIdx(self) -> int:
        return self.ethIfPhysControllerIdx

    def setEthIfPhysControllerIdx(self, value: int):
        if value is not None:
            self.ethIfPhysControllerIdx = value
        return self

    def getEthIfEthCtrlRef(self) -> EcucRefType:
        return self.ethIfEthCtrlRef

    def setEthIfEthCtrlRef(self, value: EcucRefType):
        if value is not None:
            self.ethIfEthCtrlRef = value
        return self

    def getEthIfWEthCtrlRef(self) -> EcucRefType:
        return self.ethIfWEthCtrlRef

    def setEthIfWEthCtrlRef(self, value: EcucRefType):
        if value is not None:
            self.ethIfWEthCtrlRef = value
        return self


class EthIfSwitch(EcucParamConfContainerDef):
    """EthIf switch configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ethIfSwitchIdx: int = None
        self.ethIfSwitchRef: EcucRefType = None

    def getEthIfSwitchIdx(self) -> int:
        return self.ethIfSwitchIdx

    def setEthIfSwitchIdx(self, value: int):
        if value is not None:
            self.ethIfSwitchIdx = value
        return self

    def getEthIfSwitchRef(self) -> EcucRefType:
        return self.ethIfSwitchRef

    def setEthIfSwitchRef(self, value: EcucRefType):
        if value is not None:
            self.ethIfSwitchRef = value
        return self


class EthIfSwitchPortGroup(EcucParamConfContainerDef):
    """EthIf switch port group configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ethIfSwitchPortGroupIdx: int = None
        self.ethIfPortRef: EcucRefType = None

    def getEthIfSwitchPortGroupIdx(self) -> int:
        return self.ethIfSwitchPortGroupIdx

    def setEthIfSwitchPortGroupIdx(self, value: int):
        if value is not None:
            self.ethIfSwitchPortGroupIdx = value
        return self

    def getEthIfPortRef(self) -> EcucRefType:
        return self.ethIfPortRef

    def setEthIfPortRef(self, value: EcucRefType):
        if value is not None:
            self.ethIfPortRef = value
        return self


class EthIfTransceiver(EcucParamConfContainerDef):
    """EthIf transceiver configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.ethIfTransceiverIdx: int = None
        self.ethIfEthTrcvRef: EcucRefType = None
        self.ethIfWEthTrcvRef: EcucRefType = None

    def getEthIfTransceiverIdx(self) -> int:
        return self.ethIfTransceiverIdx

    def setEthIfTransceiverIdx(self, value: int):
        if value is not None:
            self.ethIfTransceiverIdx = value
        return self

    def getEthIfEthTrcvRef(self) -> EcucRefType:
        return self.ethIfEthTrcvRef

    def setEthIfEthTrcvRef(self, value: EcucRefType):
        if value is not None:
            self.ethIfEthTrcvRef = value
        return self

    def getEthIfWEthTrcvRef(self) -> EcucRefType:
        return self.ethIfWEthTrcvRef

    def setEthIfWEthTrcvRef(self, value: EcucRefType):
        if value is not None:
            self.ethIfWEthTrcvRef = value
        return self


class EthIfRxIndicationConfig(EcucParamConfContainerDef):
    """EthIf RX indication configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class EthIfTxConfirmationConfig(EcucParamConfContainerDef):
    """EthIf TX confirmation configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class EthIfEthControllerType(EcucParamConfContainerDef):
    """EthIf EthControllerType configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class EthIfEthTrcvType(EcucParamConfContainerDef):
    """EthIf EthTrcvType configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class EthIfEthSwtType(EcucParamConfContainerDef):
    """EthIf EthSwtType configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class EthIf(Module):
    """EthIf module model."""
    def __init__(self, parent) -> None:
        super().__init__(parent, "EthIf")

        self.ethIfGeneral: EthIfGeneral = None
        self.ethIfControllers: List[EthIfController] = []
        self.ethIfFrameOwnerConfigs: List[EthIfFrameOwnerConfig] = []
        self.ethIfPhysControllers: List[EthIfPhysController] = []
        self.ethIfSwitches: List[EthIfSwitch] = []
        self.ethIfSwitchPortGroups: List[EthIfSwitchPortGroup] = []
        self.ethIfTransceivers: List[EthIfTransceiver] = []
        self.ethIfRxIndicationConfigs: List[EthIfRxIndicationConfig] = []
        self.ethIfTxConfirmationConfigs: List[EthIfTxConfirmationConfig] = []
        self.ethIfEthControllerTypes: List[EthIfEthControllerType] = []
        self.ethIfEthTrcvTypes: List[EthIfEthTrcvType] = []
        self.ethIfEthSwtTypes: List[EthIfEthSwtType] = []

        self.logger = logging.getLogger()

    def getEthIfGeneral(self) -> EthIfGeneral:
        return self.ethIfGeneral

    def setEthIfGeneral(self, value: EthIfGeneral):
        if value is not None:
            self.ethIfGeneral = value
        return self

    def getEthIfControllerList(self) -> List[EthIfController]:
        return list(sorted(filter(lambda a: isinstance(a, EthIfController), self.elements.values()), key=lambda o: o.getName()))

    def addEthIfController(self, value: EthIfController):
        self.addElement(value)
        self.ethIfControllers.append(value)
        return self

    def getEthIfFrameOwnerConfigList(self) -> List[EthIfFrameOwnerConfig]:
        return list(sorted(filter(lambda a: isinstance(a, EthIfFrameOwnerConfig), self.elements.values()), key=lambda o: o.getName()))

    def addEthIfFrameOwnerConfig(self, value: EthIfFrameOwnerConfig):
        self.addElement(value)
        self.ethIfFrameOwnerConfigs.append(value)
        return self

    def getEthIfPhysControllerList(self) -> List[EthIfPhysController]:
        return list(sorted(filter(lambda a: isinstance(a, EthIfPhysController), self.elements.values()), key=lambda o: o.getName()))

    def addEthIfPhysController(self, value: EthIfPhysController):
        self.addElement(value)
        self.ethIfPhysControllers.append(value)
        return self

    def getEthIfSwitchList(self) -> List[EthIfSwitch]:
        return list(sorted(filter(lambda a: isinstance(a, EthIfSwitch), self.elements.values()), key=lambda o: o.getName()))

    def addEthIfSwitch(self, value: EthIfSwitch):
        self.addElement(value)
        self.ethIfSwitches.append(value)
        return self

    def getEthIfSwitchPortGroupList(self) -> List[EthIfSwitchPortGroup]:
        return list(sorted(filter(lambda a: isinstance(a, EthIfSwitchPortGroup), self.elements.values()), key=lambda o: o.getName()))

    def addEthIfSwitchPortGroup(self, value: EthIfSwitchPortGroup):
        self.addElement(value)
        self.ethIfSwitchPortGroups.append(value)
        return self

    def getEthIfTransceiverList(self) -> List[EthIfTransceiver]:
        return list(sorted(filter(lambda a: isinstance(a, EthIfTransceiver), self.elements.values()), key=lambda o: o.getName()))

    def addEthIfTransceiver(self, value: EthIfTransceiver):
        self.addElement(value)
        self.ethIfTransceivers.append(value)
        return self

    def getEthIfRxIndicationConfigList(self) -> List[EthIfRxIndicationConfig]:
        return list(sorted(filter(lambda a: isinstance(a, EthIfRxIndicationConfig), self.elements.values()), key=lambda o: o.getName()))

    def addEthIfRxIndicationConfig(self, value: EthIfRxIndicationConfig):
        self.addElement(value)
        self.ethIfRxIndicationConfigs.append(value)
        return self

    def getEthIfTxConfirmationConfigList(self) -> List[EthIfTxConfirmationConfig]:
        return list(sorted(filter(lambda a: isinstance(a, EthIfTxConfirmationConfig), self.elements.values()), key=lambda o: o.getName()))

    def addEthIfTxConfirmationConfig(self, value: EthIfTxConfirmationConfig):
        self.addElement(value)
        self.ethIfTxConfirmationConfigs.append(value)
        return self

    def getEthIfEthControllerTypeList(self) -> List[EthIfEthControllerType]:
        return list(sorted(filter(lambda a: isinstance(a, EthIfEthControllerType), self.elements.values()), key=lambda o: o.getName()))

    def addEthIfEthControllerType(self, value: EthIfEthControllerType):
        self.addElement(value)
        self.ethIfEthControllerTypes.append(value)
        return self

    def getEthIfEthTrcvTypeList(self) -> List[EthIfEthTrcvType]:
        return list(sorted(filter(lambda a: isinstance(a, EthIfEthTrcvType), self.elements.values()), key=lambda o: o.getName()))

    def addEthIfEthTrcvType(self, value: EthIfEthTrcvType):
        self.addElement(value)
        self.ethIfEthTrcvTypes.append(value)
        return self

    def getEthIfEthSwtTypeList(self) -> List[EthIfEthSwtType]:
        return list(sorted(filter(lambda a: isinstance(a, EthIfEthSwtType), self.elements.values()), key=lambda o: o.getName()))

    def addEthIfEthSwtType(self, value: EthIfEthSwtType):
        self.addElement(value)
        self.ethIfEthSwtTypes.append(value)
        return self
