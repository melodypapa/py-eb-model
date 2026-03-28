"""
PduR Model Tests - Tests for PduR module model classes.
"""
import pytest
from ...models.pdur_xdm import PduR, PduRRoutingTableEntry
from ...models.eb_doc import EBModel


class TestPduRRoutingTableEntry:

    def test_initialization(self):
        root = EBModel.getInstance()
        entry = PduRRoutingTableEntry(root, "RoutingEntry1")

        assert entry.getName() == "RoutingEntry1"
        assert entry.getParent() == root
        assert entry.getPduRRoutingTableEntryID() is None
        assert entry.getPduRRoutingPduSID() is None
        assert entry.getPduRDestPduRef() is None
        assert entry.getPduRSrcPduRef() is None

    def test_set_pdu_r_routing_table_entry_id(self):
        root = EBModel.getInstance()
        entry = PduRRoutingTableEntry(root, "RoutingEntry1")

        assert entry.setPduRRoutingTableEntryID(1) == entry
        assert entry.getPduRRoutingTableEntryID() == 1

        assert entry.setPduRRoutingTableEntryID(42) == entry
        assert entry.getPduRRoutingTableEntryID() == 42

    def test_set_pdu_r_routing_pdu_sid(self):
        root = EBModel.getInstance()
        entry = PduRRoutingTableEntry(root, "RoutingEntry1")

        assert entry.setPduRRoutingPduSID(100) == entry
        assert entry.getPduRRoutingPduSID() == 100

    def test_set_pdu_r_dest_pdu_ref(self):
        root = EBModel.getInstance()
        entry = PduRRoutingTableEntry(root, "RoutingEntry1")
        from ...models.abstract import EcucRefType

        ref = EcucRefType("/Can/CanIfTxPdu1")
        assert entry.setPduRDestPduRef(ref) == entry
        assert entry.getPduRDestPduRef() == ref

    def test_set_pdu_r_src_pdu_ref(self):
        root = EBModel.getInstance()
        entry = PduRRoutingTableEntry(root, "RoutingEntry1")
        from ...models.abstract import EcucRefType

        ref = EcucRefType("/Can/CanIfRxPdu1")
        assert entry.setPduRSrcPduRef(ref) == entry
        assert entry.getPduRSrcPduRef() == ref

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        entry = PduRRoutingTableEntry(root, "RoutingEntry1")
        from ...models.abstract import EcucRefType

        dest_ref = EcucRefType("/Can/DestPdu")
        src_ref = EcucRefType("/Can/SrcPdu")

        result = (entry
                  .setPduRRoutingTableEntryID(1)
                  .setPduRRoutingPduSID(100)
                  .setPduRDestPduRef(dest_ref)
                  .setPduRSrcPduRef(src_ref))

        assert result == entry
        assert entry.getPduRRoutingTableEntryID() == 1
        assert entry.getPduRRoutingPduSID() == 100


class TestPduR:

    def test_initialization(self):
        root = EBModel.getInstance()
        pdur = PduR(root)

        assert pdur.getName() == "PduR"
        assert pdur.getParent() == root
        assert len(pdur.getPduRRoutingTableEntryList()) == 0
        assert len(pdur.pduRRoutingTableEntryList) == 0

    def test_add_pdu_r_routing_table_entry(self):
        root = EBModel.getInstance()
        pdur = PduR(root)
        entry1 = PduRRoutingTableEntry(pdur, "RoutingEntry1")
        entry2 = PduRRoutingTableEntry(pdur, "RoutingEntry2")

        assert pdur.addPduRRoutingTableEntry(entry1) == pdur
        assert pdur.addPduRRoutingTableEntry(entry2) == pdur

        assert len(pdur.getPduRRoutingTableEntryList()) == 2
        assert len(pdur.pduRRoutingTableEntryList) == 2
        assert entry1 in pdur.getPduRRoutingTableEntryList()
        assert entry2 in pdur.getPduRRoutingTableEntryList()

    def test_get_pdu_r_routing_table_entry_list_sorted(self):
        root = EBModel.getInstance()
        pdur = PduR(root)
        entry2 = PduRRoutingTableEntry(pdur, "RoutingEntry2")
        entry1 = PduRRoutingTableEntry(pdur, "RoutingEntry1")
        entry3 = PduRRoutingTableEntry(pdur, "RoutingEntry3")

        pdur.addPduRRoutingTableEntry(entry2)
        pdur.addPduRRoutingTableEntry(entry1)
        pdur.addPduRRoutingTableEntry(entry3)

        entry_list = pdur.getPduRRoutingTableEntryList()
        assert entry_list[0] == entry1
        assert entry_list[1] == entry2
        assert entry_list[2] == entry3

    def test_pdu_r_routing_table_entry_registered_in_elements(self):
        root = EBModel.getInstance()
        pdur = PduR(root)
        entry = PduRRoutingTableEntry(pdur, "RoutingEntry1")

        pdur.addPduRRoutingTableEntry(entry)

        assert pdur.getElement("RoutingEntry1") == entry
        assert pdur.getTotalElement() == 1
