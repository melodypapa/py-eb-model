"""
EcuC Model Tests - Tests for ECUC module model classes.
"""
import pytest
from eb_model.models.core.ecuc_xdm import EcuC, EcucPartition, EcucPartitionCollection, CommonPublishedInformation, PublishedInformation, EcucGeneral
from eb_model.models.core.eb_doc import EBModel


class TestEcucPartition:

    def test_initialization(self):
        root = EBModel.getInstance()
        partition = EcucPartition(root, "EcucPartition")

        assert partition.getName() == "EcucPartition"
        assert partition.getParent() == root
        assert partition.getEcucPartitionId() is None
        assert partition.getEcucDefaultBswPartition() is None
        assert partition.getEcucPartitionCanBeRestarted() is None
        assert partition.getEcucPartitionBswModuleExecution() is None
        assert partition.getEcucPartitionQmBswModuleExecution() is None

    def test_set_ecuc_partition_id(self):
        root = EBModel.getInstance()
        partition = EcucPartition(root, "EcucPartition")

        assert partition.setEcucPartitionId(1) == partition
        assert partition.getEcucPartitionId() == 1

    def test_set_ecuc_default_bsw_partition(self):
        root = EBModel.getInstance()
        partition = EcucPartition(root, "EcucPartition")

        assert partition.setEcucDefaultBswPartition(True) == partition
        assert partition.getEcucDefaultBswPartition() is True

    def test_set_ecuc_partition_can_be_restarted(self):
        root = EBModel.getInstance()
        partition = EcucPartition(root, "EcucPartition")

        assert partition.setEcucPartitionCanBeRestarted(True) == partition
        assert partition.getEcucPartitionCanBeRestarted() is True

    def test_set_ecuc_partition_bsw_module_execution(self):
        root = EBModel.getInstance()
        partition = EcucPartition(root, "EcucPartition")

        assert partition.setEcucPartitionBswModuleExecution(True) == partition
        assert partition.getEcucPartitionBswModuleExecution() is True

    def test_set_ecuc_partition_qm_bsw_module_execution(self):
        root = EBModel.getInstance()
        partition = EcucPartition(root, "EcucPartition")

        assert partition.setEcucPartitionQmBswModuleExecution(False) == partition
        assert partition.getEcucPartitionQmBswModuleExecution() is False


class TestCommonPublishedInformation:

    def test_initialization(self):
        root = EBModel.getInstance()
        pub_info = CommonPublishedInformation(root, "CommonPublishedInformation")

        assert pub_info.getName() == "CommonPublishedInformation"
        assert pub_info.getParent() == root
        assert pub_info.getArMajorVersion() is None
        assert pub_info.getArMinorVersion() is None
        assert pub_info.getArPatchVersion() is None
        assert pub_info.getSwMajorVersion() is None
        assert pub_info.getSwMinorVersion() is None
        assert pub_info.getSwPatchVersion() is None

    def test_set_ar_major_version(self):
        root = EBModel.getInstance()
        pub_info = CommonPublishedInformation(root, "CommonPublishedInformation")

        assert pub_info.setArMajorVersion(4) == pub_info
        assert pub_info.getArMajorVersion() == 4

    def test_set_ar_minor_version(self):
        root = EBModel.getInstance()
        pub_info = CommonPublishedInformation(root, "CommonPublishedInformation")

        assert pub_info.setArMinorVersion(3) == pub_info
        assert pub_info.getArMinorVersion() == 3


class TestPublishedInformation:

    def test_initialization(self):
        root = EBModel.getInstance()
        pub_info = PublishedInformation(root, "PublishedInformation")

        assert pub_info.getName() == "PublishedInformation"
        assert pub_info.getParent() == root
        assert pub_info.getVendorId() is None
        assert pub_info.getArReleaseMajorVersion() is None
        assert pub_info.getArReleaseMinorVersion() is None
        assert pub_info.getArReleasePatchVersion() is None

    def test_set_vendor_id(self):
        root = EBModel.getInstance()
        pub_info = PublishedInformation(root, "PublishedInformation")

        assert pub_info.setVendorId("Vector") == pub_info
        assert pub_info.getVendorId() == "Vector"

    def test_set_ar_release_major_version(self):
        root = EBModel.getInstance()
        pub_info = PublishedInformation(root, "PublishedInformation")

        assert pub_info.setArReleaseMajorVersion("4") == pub_info
        assert pub_info.getArReleaseMajorVersion() == "4"


class TestEcucGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        general = EcucGeneral(root, "EcucGeneral")

        assert general.getName() == "EcucGeneral"
        assert general.getParent() == root
        assert general.getDevErrorDetect() is None
        assert general.getLoadTolerant() is None

    def test_set_dev_error_detect(self):
        root = EBModel.getInstance()
        general = EcucGeneral(root, "EcucGeneral")

        assert general.setDevErrorDetect(True) == general
        assert general.getDevErrorDetect() is True

    def test_set_load_tolerant(self):
        root = EBModel.getInstance()
        general = EcucGeneral(root, "EcucGeneral")

        assert general.setLoadTolerant(False) == general
        assert general.getLoadTolerant() is False
