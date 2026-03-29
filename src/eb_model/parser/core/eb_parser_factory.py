import logging
import xml.etree.ElementTree as ET

# Core
from .bswm_xdm_parser import BswMXdmParser
from .rte_xdm_parser import RteXdmParser
from .ecuc_xdm_parser import EcucXdmParser
from .os_xdm_parser import OsXdmParser
from .tm_xdm_parser import TmXdmParser
from .pbcfgm_xdm_parser import PbcfgMXdmParser
from .ecum_xdm_parser import EcuMXdmParser
from .det_xdm_parser import DetXdmParser
from .pref_xdm_parser import PerfXdmParser

# LIN Stack
from ..lin_stack.linif_xdm_parser import LinIfXdmParser
from ..lin_stack.linsm_xdm_parser import LinSMXdmParser
from ..lin_stack.lintp_xdm_parser import LinTpXdmParser

# CAN Stack
from ..can_stack.canif_xdm_parser import CanIfXdmParser
from ..can_stack.cannm_xdm_parser import CanNmXdmParser
from ..can_stack.cansm_xdm_parser import CanSMXdmParser
from ..can_stack.cantp_xdm_parser import CanTpXdmParser

# Ethernet Stack
from ..eth_stack.ethif_xdm_parser import EthIfXdmParser
from ..eth_stack.ethsm_xdm_parser import EthSMXdmParser
from ..eth_stack.tcpip_xdm_parser import TcpIpXdmParser
from ..eth_stack.soad_xdm_parser import SoAdXdmParser
from ..eth_stack.udpnm_xdm_parser import UdpNmXdmParser
from ..eth_stack.doip_xdm_parser import DoIPXdmParser
from ..eth_stack.someiptp_xdm_parser import SomeIpTpXdmParser

# FlexRay Stack
from ..fr_stack.frif_xdm_parser import FrIfXdmParser
from ..fr_stack.frtp_xdm_parser import FrTpXdmParser
from ..fr_stack.frnm_xdm_parser import FrNmXdmParser
from ..fr_stack.frsm_xdm_parser import FrSMXdmParser
from ..fr_stack.frartp_xdm_parser import FrArTpXdmParser

# Communication Stack
from ..com_stack.com_xdm_parser import ComXdmParser
from ..com_stack.comm_xdm_parser import ComMXdmParser
from ..com_stack.ldcom_xdm_parser import LdComXdmParser
from ..com_stack.pdur_xdm_parser import PduRXdmParser
from ..com_stack.ipdum_xdm_parser import IpduMXdmParser
from ..com_stack.nm_xdm_parser import NmXdmParser

# Memory Stack
from ..mem_stack.memif_xdm_parser import MemIfXdmParser
from ..mem_stack.fee_xdm_parser import FeeXdmParser
from ..mem_stack.ea_xdm_parser import EaXdmParser
from ..mem_stack.memmap_xdm_parser import MemMapXdmParser
from ..mem_stack.memacc_xdm_parser import MemAccXdmParser
from ..mem_stack.crc_xdm_parser import CrcXdmParser
from ..mem_stack.nvm_xdm_parser import NvMXdmParser

# Crypto/Security Stack
from ..crypto_stack.crypto_xdm_parser import CryptoXdmParser
from ..crypto_stack.cryif_xdm_parser import CryIfXdmParser
from ..crypto_stack.csm_xdm_parser import CsmXdmParser
from ..crypto_stack.secoc_xdm_parser import SecOCXdmParser

# Diagnostics/Events Stack
from ..diag_stack.fim_xdm_parser import FiMXdmParser
from ..diag_stack.dcm_xdm_parser import DcmXdmParser
from ..diag_stack.dem_xdm_parser import DemXdmParser
from ..diag_stack.dlt_xdm_parser import DltXdmParser

# J1939 Stack
from ..j1939_stack.j1939dcm_xdm_parser import J1939DcmXdmParser
from ..j1939_stack.j1939nm_xdm_parser import J1939NmXdmParser
from ..j1939_stack.j1939rm_xdm_parser import J1939RmXdmParser
from ..j1939_stack.j1939tp_xdm_parser import J1939TpXdmParser

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
        "Crypto": CryptoXdmParser,
        "CryIf": CryIfXdmParser,
        "Csm": CsmXdmParser,
        "SecOC": SecOCXdmParser,
        "FiM": FiMXdmParser,
        "Dcm": DcmXdmParser,
        "Dem": DemXdmParser,
        "Dlt": DltXdmParser,
        "J1939Dcm": J1939DcmXdmParser,
        "J1939Nm": J1939NmXdmParser,
        "J1939Rm": J1939RmXdmParser,
        "J1939Tp": J1939TpXdmParser,
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