"""
Crypto XDM Parser Module - Extracts AUTOSAR Crypto configuration from EB Tresos XDM files.

Implements:
    - SWR_CRYPTO_00001: Crypto module parsing
    - SWR_CRYPTO_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.crypto_xdm import Crypto, CryptoGeneral
from ..parser.eb_parser import AbstractEbModelParser


class CryptoXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR Crypto (Cryptographic) module configuration.

    Implements: SWR_CRYPTO_00001 (Crypto Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the Crypto XDM parser."""
        super().__init__()

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse Crypto module configuration from XDM element.

        Implements: SWR_CRYPTO_00001
        """
        if self.get_component_name(element) != "Crypto":
            raise ValueError("Invalid <%s> xdm file" % "Crypto")

        crypto = doc.getCrypto()

        self.read_version(element, crypto)

        self.logger.info("Parse Crypto ARVersion:<%s> SwVersion:<%s>" %
                        (crypto.getArVersion().getVersion(), crypto.getSwVersion().getVersion()))

        self.read_crypto_general(element, crypto)

    def read_crypto_general(self, element: ET.Element, crypto: Crypto):
        """
        Parse CryptoGeneral container from XDM.

        Implements: SWR_CRYPTO_00002 (General configuration parsing)
        """
        ctr_tag = self.find_ctr_tag(element, "CryptoGeneral")
        if ctr_tag is not None:
            general = CryptoGeneral(crypto, ctr_tag.attrib["name"])
            general.setCryptoDevErrorDetect(self.read_value(ctr_tag, "CryptoDevErrorDetect"))
            general.setCryptoEnabled(self.read_value(ctr_tag, "CryptoEnabled"))
            crypto.setCryptoGeneral(general)
            self.logger.debug("Read CryptoGeneral")