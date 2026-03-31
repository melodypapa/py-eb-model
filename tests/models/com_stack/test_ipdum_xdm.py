"""
IpduM Model Tests - Tests for IpduM module model classes.
"""
import pytest
from eb_model.models.com_stack.ipdum_xdm import IpduM, IpduMDynPdu
from eb_model.models.core.eb_doc import EBModel


class TestIpduMDynPdu:

    def test_initialization(self):
        root = EBModel.getInstance()
        dyn_pdu = IpduMDynPdu(root, "DynPdu1")

        assert dyn_pdu.getName() == "DynPdu1"
        assert dyn_pdu.getParent() == root
        assert dyn_pdu.getIpduMDynPduId() is None
        assert dyn_pdu.getIpduMDynPduLength() is None

    def test_set_ipdu_m_dyn_pdu_id(self):
        root = EBModel.getInstance()
        dyn_pdu = IpduMDynPdu(root, "DynPdu1")

        assert dyn_pdu.setIpduMDynPduId(1) == dyn_pdu
        assert dyn_pdu.getIpduMDynPduId() == 1

        assert dyn_pdu.setIpduMDynPduId(42) == dyn_pdu
        assert dyn_pdu.getIpduMDynPduId() == 42

    def test_set_ipdu_m_dyn_pdu_length(self):
        root = EBModel.getInstance()
        dyn_pdu = IpduMDynPdu(root, "DynPdu1")

        assert dyn_pdu.setIpduMDynPduLength(8) == dyn_pdu
        assert dyn_pdu.getIpduMDynPduLength() == 8

        assert dyn_pdu.setIpduMDynPduLength(64) == dyn_pdu
        assert dyn_pdu.getIpduMDynPduLength() == 64

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        dyn_pdu = IpduMDynPdu(root, "DynPdu1")

        result = (dyn_pdu
                  .setIpduMDynPduId(1)
                  .setIpduMDynPduLength(16))

        assert result == dyn_pdu
        assert dyn_pdu.getIpduMDynPduId() == 1
        assert dyn_pdu.getIpduMDynPduLength() == 16


class TestIpduM:

    def test_initialization(self):
        root = EBModel.getInstance()
        ipdum = IpduM(root)

        assert ipdum.getName() == "IpduM"
        assert ipdum.getParent() == root
        assert len(ipdum.getIpduMDynPduList()) == 0
        assert len(ipdum.ipduMDynPduList) == 0

    def test_add_ipdu_m_dyn_pdu(self):
        root = EBModel.getInstance()
        ipdum = IpduM(root)
        dyn_pdu1 = IpduMDynPdu(ipdum, "DynPdu1")
        dyn_pdu2 = IpduMDynPdu(ipdum, "DynPdu2")

        assert ipdum.addIpduMDynPdu(dyn_pdu1) == ipdum
        assert ipdum.addIpduMDynPdu(dyn_pdu2) == ipdum

        assert len(ipdum.getIpduMDynPduList()) == 2
        assert len(ipdum.ipduMDynPduList) == 2
        assert dyn_pdu1 in ipdum.getIpduMDynPduList()
        assert dyn_pdu2 in ipdum.getIpduMDynPduList()

    def test_get_ipdu_m_dyn_pdu_list_sorted(self):
        root = EBModel.getInstance()
        ipdum = IpduM(root)
        dyn_pdu2 = IpduMDynPdu(ipdum, "DynPdu2")
        dyn_pdu1 = IpduMDynPdu(ipdum, "DynPdu1")
        dyn_pdu3 = IpduMDynPdu(ipdum, "DynPdu3")

        ipdum.addIpduMDynPdu(dyn_pdu2)
        ipdum.addIpduMDynPdu(dyn_pdu1)
        ipdum.addIpduMDynPdu(dyn_pdu3)

        pdu_list = ipdum.getIpduMDynPduList()
        assert pdu_list[0] == dyn_pdu1
        assert pdu_list[1] == dyn_pdu2
        assert pdu_list[2] == dyn_pdu3

    def test_ipdu_m_dyn_pdu_registered_in_elements(self):
        root = EBModel.getInstance()
        ipdum = IpduM(root)
        dyn_pdu = IpduMDynPdu(ipdum, "DynPdu1")

        ipdum.addIpduMDynPdu(dyn_pdu)

        assert ipdum.getElement("DynPdu1") == dyn_pdu
        assert ipdum.getTotalElement() == 1
