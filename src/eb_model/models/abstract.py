from abc import ABCMeta
from typing import Dict
import re

class EcucObject(metaclass=ABCMeta):
    def __init__(self, parent, name) -> None:
        if type(self) == EcucObject:
            raise ValueError("Abstract EcucObject cannot be initialized.")
        
        self.name = name
        self.parent = parent                # type: EcucObject

        if isinstance(parent, EcucContainer):
            parent.addElement(self)

    def getName(self):
        return self.name

    def setName(self, value):
        self.name = value
        return self

    def getParent(self):
        return self.parent

    def setParent(self, value):
        self.parent = value
        return self

    def getFullName(self) -> str:
        return self.parent.getFullName() + "/" + self.name

class EcucContainer(EcucObject):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.elements = {}                  # type: Dict[str, EcucObject]

    def getTotalElement(self) -> int:
        #return len(list(filter(lambda a: not isinstance(a, ARPackage) , self.elements.values())))
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

    def getElement(self, name: str) -> EcucObject:
        if (name not in self.elements):
            return None
        return self.elements[name]

class EcucRefType:
    def __init__(self, value: str) -> None:
        self.value = value

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
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