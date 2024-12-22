from .importer_xdm import SystemDescriptionImporter
from .rte_xdm import Rte
from .os_xdm import Os
from .abstract import EcucContainer, EcucObject

class AbstractModel(EcucContainer):
    def getFullName(self):
        return self.name

    def clear(self):
        self.elements = {}

    def find_object(self, referred_name:str, element:EcucContainer) -> EcucObject:
        name_list = referred_name.split("/")
        #element = EBModel.getInstance()
        for name in name_list:
            if (name == ""):
                continue
            element = element.getElement(name)
            if (element == None):
                return element
            #    raise ValueError("The %s of reference <%s> does not exist." % (short_name, referred_name))
        return element


class EBModel(AbstractModel):
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

    def find(self, referred_name: str) -> EcucObject:
        return self.find_object(referred_name, EBModel.getInstance())

    def getOs(self) -> Os:
        container = EcucContainer(self, "Os")
        os = Os(container)
        return self.find("/Os/Os")
    
    def getRte(self) -> Rte:
        container = EcucContainer(self, "Rte")
        rte = Rte(container)
        return self.find("/Rte/Rte")

class PreferenceModel(AbstractModel):
    __instance = None

    @staticmethod
    def getInstance():
        if (PreferenceModel.__instance == None):
            PreferenceModel()
        return PreferenceModel.__instance

    def __init__(self):
        if (PreferenceModel.__instance != None):
            raise Exception("The PreferenceModel is singleton!")
        
        EcucContainer.__init__(self, None, "")
        PreferenceModel.__instance = self

        container = EcucContainer(self, "ImporterExporterAdditions")
        SystemDescriptionImporter(container, "SystemDescriptionImporters")

    def find(self, referred_name: str) -> EcucObject:
        return self.find_object(referred_name, PreferenceModel.getInstance())

    def getSystemDescriptionImporter(self) -> SystemDescriptionImporter:
        return self.find("/ImporterExporterAdditions/SystemDescriptionImporters")