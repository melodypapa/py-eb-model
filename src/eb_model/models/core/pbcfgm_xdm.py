from typing import List
import logging
from .abstract import EcucParamConfContainerDef, EcucRefType, Module  # noqa F401


class PbcfgMProtectionSet(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.pbcfgMProtectionSetName: str = None

    def getPbcfgMProtectionSetName(self) -> str:
        return self.pbcfgMProtectionSetName

    def setPbcfgMProtectionSetName(self, value: str):
        if value is not None:
            self.pbcfgMProtectionSetName = value
        return self


class PbcfgMCoreProtectionSet(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.pbcfgMCoreProtectionSetRef: EcucRefType = None

    def getPbcfgMCoreProtectionSetRef(self) -> EcucRefType:
        return self.pbcfgMCoreProtectionSetRef

    def setPbcfgMCoreProtectionSetRef(self, value: EcucRefType):
        if value is not None:
            self.pbcfgMCoreProtectionSetRef = value
        return self


class PbcfgMGeneral(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.pbcfgMDevErrorDetect: bool = None
        self.pbcfgMInitConfiguration: bool = None

    def getPbcfgMDevErrorDetect(self) -> bool:
        return self.pbcfgMDevErrorDetect

    def setPbcfgMDevErrorDetect(self, value: bool):
        if value is not None:
            self.pbcfgMDevErrorDetect = value
        return self

    def getPbcfgMInitConfiguration(self) -> bool:
        return self.pbcfgMInitConfiguration

    def setPbcfgMInitConfiguration(self, value: bool):
        if value is not None:
            self.pbcfgMInitConfiguration = value
        return self


class PbcfgM(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "PbcfgM")

        self.pbcfgMGeneral: PbcfgMGeneral = None
        self.pbcfgMProtectionSets: List[PbcfgMProtectionSet] = []
        self.pbcfgMCoreProtectionSets: List[PbcfgMCoreProtectionSet] = []

        self.logger = logging.getLogger()

    def getPbcfgMGeneral(self) -> PbcfgMGeneral:
        return self.pbcfgMGeneral

    def setPbcfgMGeneral(self, value: PbcfgMGeneral):
        if value is not None:
            self.pbcfgMGeneral = value
        return self

    def getPbcfgMProtectionSetList(self) -> List[PbcfgMProtectionSet]:
        return list(sorted(filter(lambda a: isinstance(a, PbcfgMProtectionSet), self.elements.values()), key=lambda o: o.getName()))

    def addPbcfgMProtectionSet(self, value: PbcfgMProtectionSet):
        self.addElement(value)
        self.pbcfgMProtectionSets.append(value)
        return self

    def getPbcfgMCoreProtectionSetList(self) -> List[PbcfgMCoreProtectionSet]:
        return list(sorted(filter(lambda a: isinstance(a, PbcfgMCoreProtectionSet), self.elements.values()), key=lambda o: o.getName()))

    def addPbcfgMCoreProtectionSet(self, value: PbcfgMCoreProtectionSet):
        self.addElement(value)
        self.pbcfgMCoreProtectionSets.append(value)
        return self
