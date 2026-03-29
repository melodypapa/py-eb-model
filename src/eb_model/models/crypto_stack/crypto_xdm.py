"""
Crypto Model Module - Represents AUTOSAR Crypto configuration.

Implements:
    - SWR_CRYPTO_00001: Crypto module model
    - SWR_CRYPTO_00002: General configuration
"""
from typing import List, Optional
import logging
from eb_model.models.core.abstract import EcucParamConfContainerDef, EcucRefType, Module


class CryptoGeneral(EcucParamConfContainerDef):
    """
    General configuration for Crypto module.

    Implements: SWR_CRYPTO_00002 (General configuration)
    """

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.cryptoDevErrorDetect: bool = None
        self.cryptoEnabled: bool = None

    def getCryptoDevErrorDetect(self) -> bool:
        return self.cryptoDevErrorDetect

    def setCryptoDevErrorDetect(self, value: bool):
        if value is not None:
            self.cryptoDevErrorDetect = value
        return self

    def getCryptoEnabled(self) -> bool:
        return self.cryptoEnabled

    def setCryptoEnabled(self, value: bool):
        if value is not None:
            self.cryptoEnabled = value
        return self


class Crypto(Module):
    """
    AUTOSAR Crypto module.

    Provides cryptographic services for secure communication,
    key management, and cryptographic operations.

    Implements: SWR_CRYPTO_00001 (Crypto Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "Crypto")
        self.cryptoGeneral: CryptoGeneral = None

    def getCryptoGeneral(self) -> CryptoGeneral:
        return self.cryptoGeneral

    def setCryptoGeneral(self, value: CryptoGeneral):
        if value is not None:
            self.cryptoGeneral = value
        return self
