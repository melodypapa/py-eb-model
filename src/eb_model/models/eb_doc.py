from ..models.bswm_xdm import BswM
from ..models.ecuc_xdm import EcuC
from ..models.nvm_xdm import NvM
from ..models.importer_xdm import SystemDescriptionImporter
from ..models.rte_xdm import Rte
from ..models.os_xdm import Os
from ..models.abstract import EcucParamConfContainerDef, EcucObject


class AbstractModel(EcucParamConfContainerDef):
    def getFullName(self):
        return self.name

    def clear(self):
        self.elements = {}

    def find_object(self, referred_name: str, element: EcucParamConfContainerDef) -> EcucObject:
        name_list = referred_name.split("/")
        # element = EBModel.getInstance()
        for name in name_list:
            if (name == ""):
                continue
            element = element.getElement(name)
            if (element is None):
                return element
            #    raise ValueError("The %s of reference <%s> does not exist." % (short_name, referred_name))
        return element


class EBModel(AbstractModel):
    __instance = None

    @staticmethod
    def getInstance():
        if (EBModel.__instance is None):
            EBModel()
        return EBModel.__instance

    def __init__(self):
        if (EBModel.__instance is not None):
            raise Exception("The EBModel is singleton!")
        
        EcucParamConfContainerDef.__init__(self, None, "")
        EBModel.__instance = self

    def find(self, referred_name: str) -> EcucObject:
        return self.find_object(referred_name, EBModel.getInstance())

    def getOs(self) -> Os:
        '''
            get the Os Container
        '''
        container = EcucParamConfContainerDef(self, "Os")
        Os(container)
        return self.find("/Os/Os")
    
    def getRte(self) -> Rte:
        container = EcucParamConfContainerDef(self, "Rte")
        Rte(container)
        return self.find("/Rte/Rte")
    
    def getNvM(self) -> NvM:
        container = EcucParamConfContainerDef(self, "NvM")
        NvM(container)
        return self.find("/NvM/NvM")
    
    def getEcuC(self) -> EcuC:
        container = EcucParamConfContainerDef(self, "EcuC")
        EcuC(container)
        return self.find("/EcuC/EcuC")
    
    def getBswM(self) -> BswM:
        container = EcucParamConfContainerDef(self, "BswM")
        BswM(container)
        return self.find("/BswM/BswM")
    
    def addContainer(self, container: EcucParamConfContainerDef):
        if (container is None):
            raise ValueError("The container to be added cannot be None.")
        self.elements[container.name] = container
        container.parent = self
        return container
    
    def getContainer(self, name: str) -> EcucParamConfContainerDef:
        if (name not in self.elements):
            raise KeyError("The container <%s> does not exist." % name)
        return self.elements[name]


class PreferenceModel(AbstractModel):
    __instance = None

    @staticmethod
    def getInstance():
        if (PreferenceModel.__instance is None):
            PreferenceModel()
        return PreferenceModel.__instance

    def __init__(self):
        if (PreferenceModel.__instance is not None):
            raise Exception("The PreferenceModel is singleton!")
        
        EcucParamConfContainerDef.__init__(self, None, "")
        PreferenceModel.__instance = self

        container = EcucParamConfContainerDef(self, "ImporterExporterAdditions")
        SystemDescriptionImporter(container, "SystemDescriptionImporters")

    def find(self, referred_name: str) -> EcucObject:
        return self.find_object(referred_name, PreferenceModel.getInstance())

    def getSystemDescriptionImporter(self) -> SystemDescriptionImporter:
        return self.find("/ImporterExporterAdditions/SystemDescriptionImporters")
