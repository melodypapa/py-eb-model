"""
Crypto Model Tests - Tests for Crypto module model classes.
"""
import pytest
from ...models.crypto_xdm import Crypto, CryptoGeneral
from ...models.eb_doc import EBModel
from ...models.abstract import EcucParamConfContainerDef


class TestCrypto:

    def test_module_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Crypto")
        crypto = Crypto(container)

        assert crypto.getName() == "Crypto"
        assert crypto.getParent() == container

    def test_module_properties(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Crypto")
        crypto = Crypto(container)

        # Verify inherited Module properties
        assert isinstance(crypto.getArVersion(), type(root.getOs().getArVersion()))
        assert isinstance(crypto.getSwVersion(), type(root.getOs().getSwVersion()))
        assert crypto.getTotalElement() == 0

    def test_get_set_general(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Crypto")
        crypto = Crypto(container)

        general = CryptoGeneral(crypto, "CryptoGeneral")
        general.setCryptoDevErrorDetect(True)
        crypto.setCryptoGeneral(general)

        assert crypto.getCryptoGeneral() is not None
        assert crypto.getCryptoGeneral().getCryptoDevErrorDetect() is True


class TestCryptoGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Crypto")
        crypto = Crypto(container)

        general = CryptoGeneral(crypto, "CryptoGeneral")

        assert general.getName() == "CryptoGeneral"
        assert general.getParent() == crypto

    def test_get_set_dev_error_detect(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Crypto")
        crypto = Crypto(container)

        general = CryptoGeneral(crypto, "CryptoGeneral")
        general.setCryptoDevErrorDetect(True)

        assert general.getCryptoDevErrorDetect() is True

    def test_get_set_crypto_enabled(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Crypto")
        crypto = Crypto(container)

        general = CryptoGeneral(crypto, "CryptoGeneral")
        general.setCryptoEnabled(True)

        assert general.getCryptoEnabled() is True

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Crypto")
        crypto = Crypto(container)

        general = CryptoGeneral(crypto, "CryptoGeneral")
        result = general.setCryptoDevErrorDetect(False)

        assert result is general
        assert general.getCryptoDevErrorDetect() is False

        # Test chain setter returns self
        result = general.setCryptoEnabled(True)

        assert result is general
        assert general.getCryptoEnabled() is True
