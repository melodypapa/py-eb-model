"""
Rte Model Tests - Tests for RTE module model classes.
"""
import pytest
from eb_model.models.core.rte_xdm import Rte, RteSwComponentInstance, RteBswModuleInstance
from eb_model.models.core.eb_doc import EBModel


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
