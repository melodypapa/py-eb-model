import pytest
from ...models.abstract import Module, EcucParamConfContainerDef, Version, EcucRefType, EcucObject, EcucEnumerationParamDef
from ...models.eb_doc import EBModel


class TestModule:

    def test_module_initialization(self):
        root = EBModel.getInstance()
        parent = EcucParamConfContainerDef(root, "Parent")
        module = Module(parent, "TestModule")

        assert module.getName() == "TestModule"
        assert module.getParent() == parent
        assert isinstance(module.getArVersion(), Version)
        assert isinstance(module.getSwVersion(), Version)

    def test_module_ar_version(self):
        root = EBModel.getInstance()
        parent = EcucParamConfContainerDef(root, "Parent")
        module = Module(parent, "TestModule")

        ar_version = module.getArVersion()
        ar_version.setMajorVersion(1).setMinorVersion(2).setPatchVersion(3)

        assert ar_version.getMajorVersion() == 1
        assert ar_version.getMinorVersion() == 2
        assert ar_version.getPatchVersion() == 3

        # Check the version string format
        assert ar_version.getVersion() == "1.2.3"

    def test_module_sw_version(self):
        root = EBModel.getInstance()
        parent = EcucParamConfContainerDef(root, "Parent")
        module = Module(parent, "TestModule")

        sw_version = module.getSwVersion()
        sw_version.setMajorVersion(4).setMinorVersion(5).setPatchVersion(6)

        assert sw_version.getMajorVersion() == 4
        assert sw_version.getMinorVersion() == 5
        assert sw_version.getPatchVersion() == 6

        # Check the version string format
        assert sw_version.getVersion() == "4.5.6"

    def test_module_add_and_get_element(self):
        root = EBModel.getInstance()
        parent = EcucParamConfContainerDef(root, "Parent")
        module = Module(parent, "TestModule")

        element = EcucParamConfContainerDef(module, "ChildElement")
        module.addElement(element)

        assert module.getTotalElement() == 1
        assert module.getElement("ChildElement") == element

    def test_module_remove_element(self):
        root = EBModel.getInstance()
        parent = EcucParamConfContainerDef(root, "Parent")
        module = Module(parent, "TestModule")

        element = EcucParamConfContainerDef(module, "ChildElement")
        module.addElement(element)

        assert module.getTotalElement() == 1

        module.removeElement("ChildElement")
        assert module.getTotalElement() == 0
        assert module.getElement("ChildElement") is None

    def test_module_get_full_name(self):
        root = EBModel.getInstance()
        parent = EcucParamConfContainerDef(root, "Parent")
        module = Module(parent, "TestModule")

        assert module.getFullName() == "/Parent/TestModule"


class TestEcucRefType:

    def test_initialization(self):
        ref = EcucRefType("/Parent/Child")
        assert ref.getValue() == "/Parent/Child"

    def test_set_value(self):
        ref = EcucRefType("/Parent/Child")
        ref.setValue("/NewParent/NewChild")
        assert ref.getValue() == "/NewParent/NewChild"

    def test_str_representation(self):
        ref = EcucRefType("/Parent/Child")
        assert str(ref) == "/Parent/Child"

    def test_get_short_name_valid(self):
        ref = EcucRefType("/Parent/Child")
        assert ref.getShortName() == "Child"

    def test_get_short_name_invalid(self):
        ref = EcucRefType("InvalidValue")
        assert ref.getShortName() == "InvalidValue"

    def test_get_short_name_raises_error_on_none(self):
        ref = EcucRefType(None)
        with pytest.raises(ValueError, match="Invalid value of EcucRefType"):
            ref.getShortName()


class TestEcucParamConfContainerDef:

    def test_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "TestContainer")

        assert container.getName() == "TestContainer"
        assert container.getParent() == root
        assert container.getTotalElement() == 0

    def test_add_element(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "TestContainer")
        child = EcucParamConfContainerDef(container, "ChildElement")

        container.addElement(child)

        assert container.getTotalElement() == 1
        assert container.getElement("ChildElement") == child

    def test_remove_element(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "TestContainer")
        child = EcucParamConfContainerDef(container, "ChildElement")

        container.addElement(child)
        assert container.getTotalElement() == 1

        container.removeElement("ChildElement")
        assert container.getTotalElement() == 0
        assert container.getElement("ChildElement") is None

    def test_remove_element_invalid_key(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "TestContainer")

        with pytest.raises(KeyError, match="Invalid key <InvalidKey> for removing element"):
            container.removeElement("InvalidKey")

    def test_get_element_list(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "TestContainer")
        child1 = EcucParamConfContainerDef(container, "Child1")
        child2 = EcucParamConfContainerDef(container, "Child2")

        container.addElement(child1)
        container.addElement(child2)

        element_list = list(container.getElementList())
        assert len(element_list) == 2
        assert child1 in element_list
        assert child2 in element_list

    def test_get_element_not_found(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "TestContainer")

        assert container.getElement("NonExistent") is None


class TestEcucObject:

    def test_initialization_raises_error(self):
        root = EBModel.getInstance()
        with pytest.raises(ValueError, match="Abstract EcucObject cannot be initialized."):
            EcucObject(root, "AbstractObject")

    def test_get_and_set_name(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Parent")
        obj = EcucEnumerationParamDef(container, "TestObject")

        assert obj.getName() == "TestObject"
        obj.setName("NewName")
        assert obj.getName() == "NewName"

    def test_get_and_set_parent(self):
        root = EBModel.getInstance()
        container1 = EcucParamConfContainerDef(root, "Parent1")
        container2 = EcucParamConfContainerDef(root, "Parent2")
        obj = EcucEnumerationParamDef(container1, "TestObject")

        assert obj.getParent() == container1
        obj.setParent(container2)
        assert obj.getParent() == container2

    def test_get_full_name(self):
        root = EBModel.getInstance()
        parent = EcucParamConfContainerDef(root, "Parent")
        obj = EcucEnumerationParamDef(parent, "Child")

        assert obj.getFullName() == "/Parent/Child"
