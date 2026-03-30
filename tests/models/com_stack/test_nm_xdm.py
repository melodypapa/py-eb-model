"""
Nm Model Tests - Tests for Nm module model classes.
"""
import pytest
from eb_model.models.com_stack.nm_xdm import Nm, NmChannel
from eb_model.models.core.eb_doc import EBModel


class TestNmChannel:

    def test_initialization(self):
        root = EBModel.getInstance()
        channel = NmChannel(root, "Channel1")

        assert channel.getName() == "Channel1"
        assert channel.getParent() == root
        assert channel.getNmChannelId() is None
        assert channel.getNmBusType() is None
        assert channel.getNmMsgCycleTime() is None
        assert channel.getNmTimeoutTime() is None
        assert channel.getNmNetworkHandle() is None
        assert channel.getNmComMNetworkHandleRef() is None
        assert channel.getNmNodeEnabled() is None

    def test_set_nm_channel_id(self):
        root = EBModel.getInstance()
        channel = NmChannel(root, "Channel1")

        assert channel.setNmChannelId(1) == channel
        assert channel.getNmChannelId() == 1

        assert channel.setNmChannelId(42) == channel
        assert channel.getNmChannelId() == 42

    def test_set_nm_bus_type(self):
        root = EBModel.getInstance()
        channel = NmChannel(root, "Channel1")

        assert channel.setNmBusType("CAN") == channel
        assert channel.getNmBusType() == "CAN"

        assert channel.setNmBusType("ETH") == channel
        assert channel.getNmBusType() == "ETH"

    def test_set_nm_msg_cycle_time(self):
        root = EBModel.getInstance()
        channel = NmChannel(root, "Channel1")

        assert channel.setNmMsgCycleTime(100.0) == channel
        assert channel.getNmMsgCycleTime() == 100.0

        assert channel.setNmMsgCycleTime(500.5) == channel
        assert channel.getNmMsgCycleTime() == 500.5

    def test_set_nm_timeout_time(self):
        root = EBModel.getInstance()
        channel = NmChannel(root, "Channel1")

        assert channel.setNmTimeoutTime(200.0) == channel
        assert channel.getNmTimeoutTime() == 200.0

        assert channel.setNmTimeoutTime(1000.0) == channel
        assert channel.getNmTimeoutTime() == 1000.0

    def test_set_nm_network_handle(self):
        root = EBModel.getInstance()
        channel = NmChannel(root, "Channel1")

        assert channel.setNmNetworkHandle(1) == channel
        assert channel.getNmNetworkHandle() == 1

        assert channel.setNmNetworkHandle(5) == channel
        assert channel.getNmNetworkHandle() == 5

    def test_set_nm_comm_m_network_handle_ref(self):
        root = EBModel.getInstance()
        channel = NmChannel(root, "Channel1")
        from eb_model.models.core.abstract import EcucRefType

        ref = EcucRefType("/ComM/Channel1")
        assert channel.setNmComMNetworkHandleRef(ref) == channel
        assert channel.getNmComMNetworkHandleRef() == ref

    def test_set_nm_node_enabled(self):
        root = EBModel.getInstance()
        channel = NmChannel(root, "Channel1")

        assert channel.setNmNodeEnabled(True) == channel
        assert channel.getNmNodeEnabled() is True

        assert channel.setNmNodeEnabled(False) == channel
        assert channel.getNmNodeEnabled() is False

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        channel = NmChannel(root, "Channel1")
        from eb_model.models.core.abstract import EcucRefType

        ref = EcucRefType("/ComM/Channel1")

        result = (channel
                  .setNmChannelId(1)
                  .setNmBusType("CAN")
                  .setNmMsgCycleTime(100.0)
                  .setNmTimeoutTime(200.0)
                  .setNmNetworkHandle(1)
                  .setNmComMNetworkHandleRef(ref)
                  .setNmNodeEnabled(True))

        assert result == channel
        assert channel.getNmChannelId() == 1
        assert channel.getNmBusType() == "CAN"
        assert channel.getNmMsgCycleTime() == 100.0
        assert channel.getNmTimeoutTime() == 200.0
        assert channel.getNmNetworkHandle() == 1
        assert channel.getNmNodeEnabled() is True


class TestNm:

    def test_initialization(self):
        root = EBModel.getInstance()
        nm = Nm(root)

        assert nm.getName() == "Nm"
        assert nm.getParent() == root
        assert len(nm.getNmChannelList()) == 0
        assert len(nm.nmChannelList) == 0

    def test_add_nm_channel(self):
        root = EBModel.getInstance()
        nm = Nm(root)
        channel1 = NmChannel(nm, "Channel1")
        channel2 = NmChannel(nm, "Channel2")

        assert nm.addNmChannel(channel1) == nm
        assert nm.addNmChannel(channel2) == nm

        assert len(nm.getNmChannelList()) == 2
        assert len(nm.nmChannelList) == 2
        assert channel1 in nm.getNmChannelList()
        assert channel2 in nm.getNmChannelList()

    def test_get_nm_channel_list_sorted(self):
        root = EBModel.getInstance()
        nm = Nm(root)
        channel2 = NmChannel(nm, "Channel2")
        channel1 = NmChannel(nm, "Channel1")
        channel3 = NmChannel(nm, "Channel3")

        nm.addNmChannel(channel2)
        nm.addNmChannel(channel1)
        nm.addNmChannel(channel3)

        channel_list = nm.getNmChannelList()
        assert channel_list[0] == channel1
        assert channel_list[1] == channel2
        assert channel_list[2] == channel3

    def test_nm_channel_registered_in_elements(self):
        root = EBModel.getInstance()
        nm = Nm(root)
        channel = NmChannel(nm, "Channel1")

        nm.addNmChannel(channel)

        assert nm.getElement("Channel1") == channel
        assert nm.getTotalElement() == 1
