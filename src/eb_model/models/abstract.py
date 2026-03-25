from abc import ABCMeta
from typing import Dict, Optional
import re


class EcucObject(metaclass=ABCMeta):
    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        if type(self) is EcucObject:
            raise ValueError("Abstract EcucObject cannot be initialized.")
        
        self.name = name
        self.parent = parent

        if isinstance(parent, EcucParamConfContainerDef):
            parent.addElement(self)

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> 'EcucObject':
        self.name = value
        return self

    def getParent(self) -> Optional['EcucObject']:
        return self.parent

    def setParent(self, value: Optional['EcucObject']) -> 'EcucObject':
        self.parent = value
        return self

    def getFullName(self) -> str:
        if self.parent is None:
            return self.name
        return self.parent.getFullName() + "/" + self.name
    

class EcucEnumerationParamDef(EcucObject):
    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        super().__init__(parent, name)


class EcucParamConfContainerDef(EcucObject):
    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        super().__init__(parent, name)

        self.importerInfo: Optional[str] = None
        self.elements: Dict[str, EcucObject] = {}

    def getTotalElement(self) -> int:
        # return len(list(filter(lambda a: not isinstance(a, ARPackage) , self.elements.values())))
        return len(self.elements)
    
    def addElement(self, object: EcucObject):
        if object.getName() not in self.elements:
            object.parent = self
            self.elements[object.getName()] = object

        return self
    
    def removeElement(self, key):
        if key not in self.elements:
            raise KeyError("Invalid key <%s> for removing element" % key)
        self.elements.pop(key)

    def getElementList(self):
        return self.elements.values()

    def getElement(self, name: str) -> Optional[EcucObject]:
        if (name not in self.elements):
            return None
        return self.elements[name]
    
    def getImporterInfo(self) -> Optional[str]:
        return self.importerInfo

    def setImporterInfo(self, value: str) -> None:
        self.importerInfo = value

    def isCalculatedSvcAs(self) -> bool:
        if self.importerInfo is not None and self.importerInfo.startswith("@CALC(SvcAs"):
            return True
        return False


class EcucRefType:
    def __init__(self, value: str) -> None:
        self.value: str = value

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str) -> 'EcucRefType':
        self.value = value
        return self
    
    def __str__(self) -> str:
        return self.value
    
    def getShortName(self) -> str:
        if self.value is None:
            raise ValueError("Invalid value of EcucRefType")
        m = re.match(r'\/[\w\/]+\/(\w+)', self.value)
        if m:
            return m.group(1)
        return self.value
    
    
class Version:
    def __init__(self) -> None:
        self.majorVersion: Optional[int] = None
        self.minorVersion: Optional[int] = None
        self.patchVersion: Optional[int] = None

    def getMajorVersion(self) -> Optional[int]:
        return self.majorVersion

    def setMajorVersion(self, value: Optional[int]) -> 'Version':
        if value is not None:
            self.majorVersion = value
        return self

    def getMinorVersion(self) -> Optional[int]:
        return self.minorVersion

    def setMinorVersion(self, value: Optional[int]) -> 'Version':
        if value is not None:
            self.minorVersion = value
        return self

    def getPatchVersion(self) -> Optional[int]:
        return self.patchVersion

    def setPatchVersion(self, value: Optional[int]) -> 'Version':
        if value is not None:
            self.patchVersion = value
        return self
    
    def getVersion(self) -> str:
        major = self.majorVersion or 0
        minor = self.minorVersion or 0
        patch = self.patchVersion or 0
        return "%d.%d.%d" % (major, minor, patch)


class Module(EcucParamConfContainerDef):
    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        super().__init__(parent, name)

        self.arVersion: Version = Version()
        self.swVersion: Version = Version()

    def getArVersion(self) -> Version:
        return self.arVersion

    # def setArVersion(self, value):
    #    if value is not None:
    #        self.arVersion = value
    #    return self

    def getSwVersion(self) -> Version:
        return self.swVersion

    # def setSwVersion(self, value):
    #    if value is not None:
    #        self.swVersion = value
    #    return self
