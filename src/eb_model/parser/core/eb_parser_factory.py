import logging
import xml.etree.ElementTree as ET

# Core
from eb_model.parser.core.bswm_xdm_parser import BswMXdmParser
from eb_model.parser.core.rte_xdm_parser import RteXdmParser
from eb_model.parser.core.ecuc_xdm_parser import EcucXdmParser
from eb_model.parser.core.os_xdm_parser import OsXdmParser
from eb_model.parser.core.tm_xdm_parser import TmXdmParser
from eb_model.parser.core.pbcfgm_xdm_parser import PbcfgMXdmParser
from eb_model.parser.core.ecum_xdm_parser import EcuMXdmParser
from eb_model.parser.core.det_xdm_parser import DetXdmParser
from eb_model.parser.core.pref_xdm_parser import PerfXdmParser

# LIN Stack
from eb_model.parser.lin_stack.linif_xdm_parser import LinIfXdmParser
from eb_model.parser.lin_stack.linsm_xdm_parser import LinSMXdmParser
from eb_model.parser.lin_stack.lintp_xdm_parser import LinTpXdmParser

# CAN Stack
from eb_model.parser.can_stack.canif_xdm_parser import CanIfXdmParser
from eb_model.parser.can_stack.cannm_xdm_parser import CanNmXdmParser
from eb_model.parser.can_stack.cansm_xdm_parser import CanSMXdmParser
from eb_model.parser.can_stack.cantp_xdm_parser import CanTpXdmParser

# Ethernet Stack
from eb_model.parser.eth_stack.ethif_xdm_parser import EthIfXdmParser
from eb_model.parser.eth_stack.ethsm_xdm_parser import EthSMXdmParser
from eb_model.parser.eth_stack.tcpip_xdm_parser import TcpIpXdmParser
from eb_model.parser.eth_stack.soad_xdm_parser import SoAdXdmParser
from eb_model.parser.eth_stack.udpnm_xdm_parser import UdpNmXdmParser
from eb_model.parser.eth_stack.doip_xdm_parser import DoIPXdmParser
from eb_model.parser.eth_stack.someiptp_xdm_parser import SomeIpTpXdmParser

# FlexRay Stack
from eb_model.parser.fr_stack.frif_xdm_parser import FrIfXdmParser
from eb_model.parser.fr_stack.frtp_xdm_parser import FrTpXdmParser
from eb_model.parser.fr_stack.frnm_xdm_parser import FrNmXdmParser
from eb_model.parser.fr_stack.frsm_xdm_parser import FrSMXdmParser
from eb_model.parser.fr_stack.frartp_xdm_parser import FrArTpXdmParser

# Communication Stack
from eb_model.parser.com_stack.com_xdm_parser import ComXdmParser
from eb_model.parser.com_stack.comm_xdm_parser import ComMXdmParser
from eb_model.parser.com_stack.ldcom_xdm_parser import LdComXdmParser
from eb_model.parser.com_stack.pdur_xdm_parser import PduRXdmParser
from eb_model.parser.com_stack.ipdum_xdm_parser import IpduMXdmParser
from eb_model.parser.com_stack.nm_xdm_parser import NmXdmParser

# Memory Stack
from eb_model.parser.mem_stack.memif_xdm_parser import MemIfXdmParser
from eb_model.parser.mem_stack.fee_xdm_parser import FeeXdmParser
from eb_model.parser.mem_stack.ea_xdm_parser import EaXdmParser
from eb_model.parser.mem_stack.memmap_xdm_parser import MemMapXdmParser
from eb_model.parser.mem_stack.memacc_xdm_parser import MemAccXdmParser
from eb_model.parser.mem_stack.crc_xdm_parser import CrcXdmParser
from eb_model.parser.mem_stack.nvm_xdm_parser import NvMXdmParser

# Crypto/Security Stack
from eb_model.parser.crypto_stack.crypto_xdm_parser import CryptoXdmParser
from eb_model.parser.crypto_stack.cryif_xdm_parser import CryIfXdmParser
from eb_model.parser.crypto_stack.csm_xdm_parser import CsmXdmParser
from eb_model.parser.crypto_stack.secoc_xdm_parser import SecOCXdmParser

# Diagnostics/Events Stack
from eb_model.parser.diag_stack.fim_xdm_parser import FiMXdmParser
from eb_model.parser.diag_stack.dcm_xdm_parser import DcmXdmParser
from eb_model.parser.diag_stack.dem_xdm_parser import DemXdmParser
from eb_model.parser.diag_stack.dlt_xdm_parser import DltXdmParser

# J1939 Stack
from eb_model.parser.j1939_stack.j1939dcm_xdm_parser import J1939DcmXdmParser
from eb_model.parser.j1939_stack.j1939nm_xdm_parser import J1939NmXdmParser
from eb_model.parser.j1939_stack.j1939rm_xdm_parser import J1939RmXdmParser
from eb_model.parser.j1939_stack.j1939tp_xdm_parser import J1939TpXdmParser

from eb_model.parser.core.eb_parser import AbstractEbModelParser


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
