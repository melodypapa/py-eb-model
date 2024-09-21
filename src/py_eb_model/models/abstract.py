from abc import ABCMeta
from typing import Dict, List


class EcucObject(metaclass=ABCMeta):
    def __init__(self, parent, name) -> None:
        if type(self) == EcucObject:
            raise ValueError("Abstract EcucObject cannot be initialized.")
        
        self.Name = name
        self.Parent = parent                # type: EcucObject

        if isinstance(parent, EcucContainer):
            parent.addElement(self)

    def getName(self):
        return self.Name

    def setName(self, value):
        self.Name = value
        return self

    def getParent(self):
        return self.Parent

    def setParent(self, value):
        self.Parent = value
        return self

    def getFullName(self) -> str:
        return self.Parent.getFullName() + "/" + self.Name


class EcucContainer(EcucObject):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.elements = {}                  # type: Dict[str, EcucObject]

    def getTotalElement(self) -> int:
        #return len(list(filter(lambda a: not isinstance(a, ARPackage) , self.elements.values())))
        return len(self.elements)
    
    def addElement(self, object: EcucObject):
        if object.getName() not in self.elements:
            object.Parent = self
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
    def __init__(self) -> None:
        self.link  = ""