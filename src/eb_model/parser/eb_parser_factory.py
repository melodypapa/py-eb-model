import logging
import xml.etree.ElementTree as ET

from .bswm_xdm_parser import BswMXdmParser
from .rte_xdm_parser import RteXdmParser
from .ecuc_xdm_parser import EcucXdmParser
from .os_xdm_parser import OsXdmParser
from .nvm_xdm_parser import NvMXdmParser
from .tm_xdm_parser import TmXdmParser
from .pbcfgm_xdm_parser import PbcfgMXdmParser
from .ecum_xdm_parser import EcuMXdmParser
from .det_xdm_parser import DetXdmParser
from .canif_xdm_parser import CanIfXdmParser
from .cannm_xdm_parser import CanNmXdmParser
from .cansm_xdm_parser import CanSMXdmParser
from .cantp_xdm_parser import CanTpXdmParser
from .linif_xdm_parser import LinIfXdmParser
from .linsm_xdm_parser import LinSMXdmParser
from .lintp_xdm_parser import LinTpXdmParser
from .ethif_xdm_parser import EthIfXdmParser
from .ethsm_xdm_parser import EthSMXdmParser
from .tcpip_xdm_parser import TcpIpXdmParser
from .soad_xdm_parser import SoAdXdmParser
from .udpnm_xdm_parser import UdpNmXdmParser
from .doip_xdm_parser import DoIPXdmParser
from .someiptp_xdm_parser import SomeIpTpXdmParser
from .frif_xdm_parser import FrIfXdmParser
from .frtp_xdm_parser import FrTpXdmParser
from .frnm_xdm_parser import FrNmXdmParser
from .frsm_xdm_parser import FrSMXdmParser
from .frartp_xdm_parser import FrArTpXdmParser
from .com_xdm_parser import ComXdmParser
from .comm_xdm_parser import ComMXdmParser
from .crc_xdm_parser import CrcXdmParser
from .ldcom_xdm_parser import LdComXdmParser
from .pdur_xdm_parser import PduRXdmParser
from .ipdum_xdm_parser import IpduMXdmParser
from .nm_xdm_parser import NmXdmParser
from .memif_xdm_parser import MemIfXdmParser
from .fee_xdm_parser import FeeXdmParser
from .ea_xdm_parser import EaXdmParser
from .memmap_xdm_parser import MemMapXdmParser
from .memacc_xdm_parser import MemAccXdmParser
from .eb_parser import AbstractEbModelParser


class EbParserFactory:
    _PARSERS = {
        "BswM": BswMXdmParser,
        "CanIf": CanIfXdmParser,
        "CanNm": CanNmXdmParser,
        "CanSM": CanSMXdmParser,
        "CanTp": CanTpXdmParser,
        "Com": ComXdmParser,
        "ComM": ComMXdmParser,
        "Crc": CrcXdmParser,
        "Det": DetXdmParser,
        "DoIP": DoIPXdmParser,
        "EcuC": EcucXdmParser,
        "EcuM": EcuMXdmParser,
        "Ea": EaXdmParser,
        "EthIf": EthIfXdmParser,
        "EthSM": EthSMXdmParser,
        "FrArTp": FrArTpXdmParser,
        "FrIf": FrIfXdmParser,
        "FrNm": FrNmXdmParser,
        "FrSM": FrSMXdmParser,
        "Fee": FeeXdmParser,
        "FrTp": FrTpXdmParser,
        "IpduM": IpduMXdmParser,
        "LinIf": LinIfXdmParser,
        "LinSM": LinSMXdmParser,
        "LinTp": LinTpXdmParser,
        "LdCom": LdComXdmParser,
        "MemIf": MemIfXdmParser,
        "MemMap": MemMapXdmParser,
        "MemAcc": MemAccXdmParser,
        "NvM": NvMXdmParser,
        "Nm": NmXdmParser,
        "Os": OsXdmParser,
        "PbcfgM": PbcfgMXdmParser,
        "PduR": PduRXdmParser,
        "Rte": RteXdmParser,
        "SoAd": SoAdXdmParser,
        "SomeIpTp": SomeIpTpXdmParser,
        "TcpIp": TcpIpXdmParser,
        "Tm": TmXdmParser,
        "UdpNm": UdpNmXdmParser,
    }

    @classmethod
    def get_component_name(cls, filename: str) -> str:
        tree = ET.parse(filename)
        ns = dict([node for _, node in ET.iterparse(filename, events=['start-ns'])])
        tag = tree.getroot().find(".//d:chc[@type='AR-ELEMENT'][@value='MODULE-CONFIGURATION']", ns)
        return tag.attrib['name']

    @classmethod
    def create(cls, xdm: str) -> AbstractEbModelParser:
        logging.getLogger().info("Analyzing file <%s>" % xdm)

        name = cls.get_component_name(xdm)

        if name in cls._PARSERS:
            return cls._PARSERS[name]()
        else:
            raise NotImplementedError("Unsupported EB xdm file <%s>" % name)
