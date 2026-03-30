"""
Os Model Tests - Tests for OS module model classes.
"""
import pytest
from eb_model.models.core.os_xdm import Os, OsTask, OsApplication, OsAlarm
from eb_model.models.core.eb_doc import EBModel


class TestOsTask:

    def test_initialization(self):
        root = EBModel.getInstance()
        task = OsTask(root, "OsTask")

        assert task.getName() == "OsTask"
        assert task.getParent() == root
        assert task.getOsTaskActivation() is None
        assert task.getOsTaskPriority() is None

    def test_set_os_task_activation(self):
        root = EBModel.getInstance()
        task = OsTask(root, "OsTask")

        assert task.setOsTaskActivation(1) == task
        assert task.getOsTaskActivation() == 1


class TestOsApplication:

    def test_initialization(self):
        root = EBModel.getInstance()
        app = OsApplication(root, "OsApplication")

        assert app.getName() == "OsApplication"
        assert app.getParent() == root
        assert app.getOsTrusted() is False


class TestOsAlarm:

    def test_initialization(self):
        root = EBModel.getInstance()
        alarm = OsAlarm(root, "OsAlarm")

        assert alarm.getName() == "OsAlarm"
        assert alarm.getParent() == root
        assert alarm.getOsAlarmCounterRef() is None
