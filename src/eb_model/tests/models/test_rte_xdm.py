"""
Rte Model Tests - Tests for RTE module model classes.
"""
import pytest
from ...models.rte_xdm import Rte, RteSwComponentInstance, RteBswModuleInstance
from ...models.eb_doc import EBModel


class TestRteSwComponentInstance:

    def test_initialization(self):
        root = EBModel.getInstance()
        instance = RteSwComponentInstance(root, "RteSwComponentInstance")

        assert instance.getName() == "RteSwComponentInstance"
        assert instance.getParent() == root


class TestRteBswModuleInstance:

    def test_initialization(self):
        root = EBModel.getInstance()
        instance = RteBswModuleInstance(root, "RteBswModuleInstance")

        assert instance.getName() == "RteBswModuleInstance"
        assert instance.getParent() == root


class TestRte:

    def test_initialization(self):
        root = EBModel.getInstance()
        rte = Rte(root)

        assert rte.getName() == "Rte"
        assert rte.getParent() == root
        assert len(rte.getRteBswModuleInstanceList()) == 0
        assert len(rte.getRteSwComponentInstanceList()) == 0
