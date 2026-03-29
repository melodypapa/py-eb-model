from typing import List
import logging
from .abstract import EcucParamConfContainerDef, Module


class BswMModeCondition(EcucParamConfContainerDef):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.bswmModeConditionSourceRef = None

    def getBswMModeConditionSourceRef(self):
        return self.bswmModeConditionSourceRef

    def setBswMModeConditionSourceRef(self, value):
        if value is not None:
            self.bswmModeConditionSourceRef = value
        return self


class BswMModeDeclaration(EcucParamConfContainerDef):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.bswmAvailableForScheduler = None
        self.bswmModeParentRef = None
        self.bswmModeType = None
        self.bswmModeConditions: List[BswMModeCondition] = []

    def getBswMAvailableForScheduler(self):
        return self.bswmAvailableForScheduler

    def setBswMAvailableForScheduler(self, value):
        if value is not None:
            self.bswmAvailableForScheduler = value
        return self

    def getBswMModeParentRef(self):
        return self.bswmModeParentRef

    def setBswMModeParentRef(self, value):
        if value is not None:
            self.bswmModeParentRef = value
        return self

    def getBswMModeType(self):
        return self.bswmModeType

    def setBswMModeType(self, value):
        if value is not None:
            self.bswmModeType = value
        return self

    def getBswMModeConditionList(self) -> List[BswMModeCondition]:
        return list(sorted(filter(lambda a: isinstance(a, BswMModeCondition), self.elements.values()), key=lambda o: o.getName()))

    def addBswMModeCondition(self, value: BswMModeCondition):
        self.addElement(value)
        self.bswmModeConditions.append(value)
        return self


class BswMGeneral(EcucParamConfContainerDef):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.bswmDevErrorDetect = None

    def getBswMDevErrorDetect(self):
        return self.bswmDevErrorDetect

    def setBswMDevErrorDetect(self, value):
        if value is not None:
            self.bswmDevErrorDetect = value
        return self


class BswM(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "BswM")

        self.bswmGeneral: BswMGeneral = None
        self.bswmModeDeclarations: List[BswMModeDeclaration] = []

        self.logger = logging.getLogger()

    def getBswMGeneral(self) -> BswMGeneral:
        return self.bswmGeneral

    def setBswMGeneral(self, value: BswMGeneral):
        if value is not None:
            self.bswmGeneral = value
        return self

    def getBswMModeDeclarationList(self) -> List[BswMModeDeclaration]:
        return list(sorted(filter(lambda a: isinstance(a, BswMModeDeclaration), self.elements.values()), key=lambda o: o.getName()))

    def addBswMModeDeclaration(self, value: BswMModeDeclaration):
        self.addElement(value)
        self.bswmModeDeclarations.append(value)
        return self
