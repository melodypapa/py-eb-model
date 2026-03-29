"""
EcuC Model Tests - Tests for ECUC module model classes.
"""
import pytest
from ...models.ecuc_xdm import EcuC, EcucPartition, EcucPartitionCollection
from ...models.eb_doc import EBModel


class TestEcucPartition:

    def test_initialization(self):
        root = EBModel.getInstance()
        partition = EcucPartition(root, "EcucPartition")

        assert partition.getName() == "EcucPartition"
        assert partition.getParent() == root
        assert partition.getEcucPartitionId() is None
        assert partition.getEcucDefaultBswPartition() is None
        assert partition.getEcucPartitionCanBeRestarted() is None

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


class TestCommonPublishedInformation:

    def test_initialization(self):
        root = EBModel.getInstance()
        # Will be implemented in Task 2
        pass


class TestPublishedInformation:

    def test_initialization(self):
        root = EBModel.getInstance()
        # Will be implemented in Task 2
        pass


class TestEcucGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        # Will be implemented in Task 2
        pass