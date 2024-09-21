
from typing import List

from .os_xdm import Os
from .abstract import EcucContainer, EcucObject


class EBModel(EcucContainer):
    __instance = None

    @staticmethod
    def getInstance():
        if (EBModel.__instance == None):
            EBModel()
        return EBModel.__instance

    def __init__(self):
        if (EBModel.__instance != None):
            raise Exception("The EBModel is singleton!")
        
        EcucContainer.__init__(self, None, "")
        EBModel.__instance = self

    def getFullName(self):
        return self.Name

    def clear(self):
        self.elements = {}

    def find(self, referred_name: str) -> EcucObject:
        name_list = referred_name.split("/")
        element = EBModel.getInstance()
        for name in name_list:
            if (name == ""):
                continue
            element = element.getElement(name)
            if (element == None):
                return element
            #    raise ValueError("The %s of reference <%s> does not exist." % (short_name, referred_name))
        return element
    
    def getOs(self) -> Os:
        container = EcucContainer(self, "Os")
        os = Os(container)
        return self.find("/Os/Os")
        

    

        

    
