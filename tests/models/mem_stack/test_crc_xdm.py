"""
Crc Model Tests - Tests for Crc module model classes.
"""
import pytest
from eb_model.models.mem_stack.crc_xdm import Crc, CrcConfig
from eb_model.models.core.eb_doc import EBModel


class TestCrcConfig:

    def test_initialization(self):
        root = EBModel.getInstance()
        config = CrcConfig(root, "Config1")

        assert config.getName() == "Config1"
        assert config.getParent() == root
        assert config.getCrcId() is None
        assert config.getCrcCRCType() is None

    def test_set_crc_id(self):
        root = EBModel.getInstance()
        config = CrcConfig(root, "Config1")

        assert config.setCrcId(1) == config
        assert config.getCrcId() == 1

        assert config.setCrcId(42) == config
        assert config.getCrcId() == 42

    def test_set_crc_crc_type(self):
        root = EBModel.getInstance()
        config = CrcConfig(root, "Config1")

        assert config.setCrcCRCType("CRC8") == config
        assert config.getCrcCRCType() == "CRC8"

        assert config.setCrcCRCType("CRC16") == config
        assert config.getCrcCRCType() == "CRC16"

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        config = CrcConfig(root, "Config1")

        result = (config
                  .setCrcId(1)
                  .setCrcCRCType("CRC8"))

        assert result == config
        assert config.getCrcId() == 1
        assert config.getCrcCRCType() == "CRC8"


class TestCrc:

    def test_initialization(self):
        root = EBModel.getInstance()
        crc = Crc(root)

        assert crc.getName() == "Crc"
        assert crc.getParent() == root
        assert len(crc.getCrcConfigList()) == 0
        assert len(crc.crcConfigList) == 0

    def test_add_crc_config(self):
        root = EBModel.getInstance()
        crc = Crc(root)
        config1 = CrcConfig(crc, "Config1")
        config2 = CrcConfig(crc, "Config2")

        assert crc.addCrcConfig(config1) == crc
        assert crc.addCrcConfig(config2) == crc

        assert len(crc.getCrcConfigList()) == 2
        assert len(crc.crcConfigList) == 2
        assert config1 in crc.getCrcConfigList()
        assert config2 in crc.getCrcConfigList()

    def test_get_crc_config_list_sorted(self):
        root = EBModel.getInstance()
        crc = Crc(root)
        config2 = CrcConfig(crc, "Config2")
        config1 = CrcConfig(crc, "Config1")
        config3 = CrcConfig(crc, "Config3")

        crc.addCrcConfig(config2)
        crc.addCrcConfig(config1)
        crc.addCrcConfig(config3)

        config_list = crc.getCrcConfigList()
        assert config_list[0] == config1
        assert config_list[1] == config2
        assert config_list[2] == config3

    def test_crc_config_registered_in_elements(self):
        root = EBModel.getInstance()
        crc = Crc(root)
        config = CrcConfig(crc, "Config1")

        crc.addCrcConfig(config)

        assert crc.getElement("Config1") == config
        assert crc.getTotalElement() == 1
