from ..models.bswm_xdm import BswM
from ..models.ecuc_xdm import EcuC
from ..models.nvm_xdm import NvM
from ..models.importer_xdm import SystemDescriptionImporter
from ..models.rte_xdm import Rte
from ..models.os_xdm import Os
from ..models.tm_xdm import Tm
from ..models.pbcfgm_xdm import PbcfgM
from ..models.ecum_xdm import EcuM
from ..models.det_xdm import Det
from ..models.canif_xdm import CanIf
from ..models.cannm_xdm import CanNm
from ..models.cansm_xdm import CanSM
from ..models.cantp_xdm import CanTp
from ..models.linif_xdm import LinIf
from ..models.linsm_xdm import LinSM
from ..models.lintp_xdm import LinTp
from ..models.ethif_xdm import EthIf
from ..models.ethsm_xdm import EthSM
from ..models.tcpip_xdm import TcpIp
from ..models.soad_xdm import SoAd
from ..models.udpnm_xdm import UdpNm
from ..models.doip_xdm import DoIP
from ..models.someiptp_xdm import SomeIpTp
from ..models.frif_xdm import FrIf
from ..models.frtp_xdm import FrTp
from ..models.frnm_xdm import FrNm
from ..models.frsm_xdm import FrSM
from ..models.frartp_xdm import FrArTp
from ..models.com_xdm import Com
from ..models.ldcom_xdm import LdCom
from ..models.comm_xdm import ComM
from ..models.pdur_xdm import PduR
from ..models.ipdum_xdm import IpduM
from ..models.nm_xdm import Nm
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

    def getTm(self) -> Tm:
        container = EcucParamConfContainerDef(self, "Tm")
        Tm(container)
        return self.find("/Tm/Tm")

    def getPbcfgM(self) -> PbcfgM:
        container = EcucParamConfContainerDef(self, "PbcfgM")
        PbcfgM(container)
        return self.find("/PbcfgM/PbcfgM")

    def getEcuM(self) -> EcuM:
        container = EcucParamConfContainerDef(self, "EcuM")
        EcuM(container)
        return self.find("/EcuM/EcuM")

    def getDet(self) -> Det:
        container = EcucParamConfContainerDef(self, "Det")
        Det(container)
        return self.find("/Det/Det")

    def getCanIf(self) -> CanIf:
        container = EcucParamConfContainerDef(self, "CanIf")
        CanIf(container)
        return self.find("/CanIf/CanIf")

    def getCanNm(self) -> CanNm:
        container = EcucParamConfContainerDef(self, "CanNm")
        CanNm(container)
        return self.find("/CanNm/CanNm")

    def getCanSM(self) -> CanSM:
        container = EcucParamConfContainerDef(self, "CanSM")
        CanSM(container)
        return self.find("/CanSM/CanSM")

    def getCanTp(self) -> CanTp:
        container = EcucParamConfContainerDef(self, "CanTp")
        CanTp(container)
        return self.find("/CanTp/CanTp")

    def getLinIf(self) -> LinIf:
        container = EcucParamConfContainerDef(self, "LinIf")
        LinIf(container)
        return self.find("/LinIf/LinIf")

    def getLinSM(self) -> LinSM:
        container = EcucParamConfContainerDef(self, "LinSM")
        LinSM(container)
        return self.find("/LinSM/LinSM")

    def getLinTp(self) -> LinTp:
        container = EcucParamConfContainerDef(self, "LinTp")
        LinTp(container)
        return self.find("/LinTp/LinTp")

    def getEthIf(self) -> EthIf:
        container = EcucParamConfContainerDef(self, "EthIf")
        EthIf(container)
        return self.find("/EthIf/EthIf")

    def getEthSM(self) -> EthSM:
        container = EcucParamConfContainerDef(self, "EthSM")
        EthSM(container)
        return self.find("/EthSM/EthSM")

    def getTcpIp(self) -> TcpIp:
        container = EcucParamConfContainerDef(self, "TcpIp")
        TcpIp(container)
        return self.find("/TcpIp/TcpIp")

    def getSoAd(self) -> SoAd:
        container = EcucParamConfContainerDef(self, "SoAd")
        SoAd(container)
        return self.find("/SoAd/SoAd")

    def getUdpNm(self) -> UdpNm:
        container = EcucParamConfContainerDef(self, "UdpNm")
        UdpNm(container)
        return self.find("/UdpNm/UdpNm")

    def getDoIP(self) -> DoIP:
        container = EcucParamConfContainerDef(self, "DoIP")
        DoIP(container)
        return self.find("/DoIP/DoIP")

    def getSomeIpTp(self) -> SomeIpTp:
        container = EcucParamConfContainerDef(self, "SomeIpTp")
        SomeIpTp(container)
        return self.find("/SomeIpTp/SomeIpTp")

    def getFrIf(self) -> FrIf:
        container = EcucParamConfContainerDef(self, "FrIf")
        FrIf(container)
        return self.find("/FrIf/FrIf")

    def getFrTp(self) -> FrTp:
        container = EcucParamConfContainerDef(self, "FrTp")
        FrTp(container)
        return self.find("/FrTp/FrTp")

    def getFrNm(self) -> FrNm:
        container = EcucParamConfContainerDef(self, "FrNm")
        FrNm(container)
        return self.find("/FrNm/FrNm")

    def getFrSM(self) -> FrSM:
        container = EcucParamConfContainerDef(self, "FrSM")
        FrSM(container)
        return self.find("/FrSM/FrSM")

    def getFrArTp(self) -> FrArTp:
        container = EcucParamConfContainerDef(self, "FrArTp")
        FrArTp(container)
        return self.find("/FrArTp/FrArTp")

    def getCom(self) -> Com:
        container = EcucParamConfContainerDef(self, "Com")
        Com(container)
        return self.find("/Com/Com")

    def getComM(self) -> ComM:
        container = EcucParamConfContainerDef(self, "ComM")
        ComM(container)
        return self.find("/ComM/ComM")

    def getLdCom(self) -> LdCom:
        container = EcucParamConfContainerDef(self, "LdCom")
        LdCom(container)
        return self.find("/LdCom/LdCom")

    def getPduR(self) -> PduR:
        container = EcucParamConfContainerDef(self, "PduR")
        PduR(container)
        return self.find("/PduR/PduR")

    def getIpduM(self) -> IpduM:
        container = EcucParamConfContainerDef(self, "IpduM")
        IpduM(container)
        return self.find("/IpduM/IpduM")

    def getNm(self) -> Nm:
        container = EcucParamConfContainerDef(self, "Nm")
        Nm(container)
        return self.find("/Nm/Nm")

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
