"""
ComM Model Tests - Tests for ComM module model classes.
"""
import pytest
from ....models.com_stack.comm_xdm import ComM, ComMChannel
from ....models.core.eb_doc import EBModel


class TestComMChannel:

    def test_initialization(self):
        root = EBModel.getInstance()
        channel = ComMChannel(root, "Channel1")

        assert channel.getName() == "Channel1"
        assert channel.getParent() == root
        assert channel.getComMChannelName() is None
        assert channel.getComMChannelId() is None

    def test_set_com_m_channel_name(self):
        root = EBModel.getInstance()
        channel = ComMChannel(root, "Channel1")

        assert channel.setComMChannelName("TestChannel") == channel
        assert channel.getComMChannelName() == "TestChannel"

        assert channel.setComMChannelName("AnotherChannel") == channel
        assert channel.getComMChannelName() == "AnotherChannel"

    def test_set_com_m_channel_id(self):
        root = EBModel.getInstance()
        channel = ComMChannel(root, "Channel1")

        assert channel.setComMChannelId(1) == channel
        assert channel.getComMChannelId() == 1

        assert channel.setComMChannelId(42) == channel
        assert channel.getComMChannelId() == 42

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        channel = ComMChannel(root, "Channel1")

        result = (channel
                  .setComMChannelName("TestChannel")
                  .setComMChannelId(5))

        assert result == channel
        assert channel.getComMChannelName() == "TestChannel"
        assert channel.getComMChannelId() == 5


class TestComM:

    def test_initialization(self):
        root = EBModel.getInstance()
        comm = ComM(root)

        assert comm.getName() == "ComM"
        assert comm.getParent() == root
        assert len(comm.getComMChannelList()) == 0
        assert len(comm.comMChannelList) == 0

    def test_add_com_m_channel(self):
        root = EBModel.getInstance()
        comm = ComM(root)
        channel1 = ComMChannel(comm, "Channel1")
        channel2 = ComMChannel(comm, "Channel2")

        assert comm.addComMChannel(channel1) == comm
        assert comm.addComMChannel(channel2) == comm

        assert len(comm.getComMChannelList()) == 2
        assert len(comm.comMChannelList) == 2
        assert channel1 in comm.getComMChannelList()
        assert channel2 in comm.getComMChannelList()

    def test_get_com_m_channel_list_sorted(self):
        root = EBModel.getInstance()
        comm = ComM(root)
        channel2 = ComMChannel(comm, "Channel2")
        channel1 = ComMChannel(comm, "Channel1")
        channel3 = ComMChannel(comm, "Channel3")

        comm.addComMChannel(channel2)
        comm.addComMChannel(channel1)
        comm.addComMChannel(channel3)

        channel_list = comm.getComMChannelList()
        assert channel_list[0] == channel1
        assert channel_list[1] == channel2
        assert channel_list[2] == channel3

    def test_com_m_channel_registered_in_elements(self):
        root = EBModel.getInstance()
        comm = ComM(root)
        channel = ComMChannel(comm, "Channel1")

        comm.addComMChannel(channel)

        assert comm.getElement("Channel1") == channel
        assert comm.getTotalElement() == 1
