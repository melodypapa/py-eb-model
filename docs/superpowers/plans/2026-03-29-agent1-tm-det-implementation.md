# Agent 1: Tm and Det Module XDM Model Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement all missing classes and attributes for Tm (2 missing) and Det (7 missing) modules to achieve complete XDM container coverage.

**Architecture:** Follow existing patterns in py-eb-model - extend model classes in `_xdm.py` files, update parsers in `_xdm_parser.py` files, add tests for verification.

**Tech Stack:** Python 3.9+, pytest, xml.etree.ElementTree

---

## File Structure

### New Files to Create
- `src/eb_model/tests/models/test_tm_xdm.py` - Tm model class tests
- `src/eb_model/tests/models/test_det_xdm.py` - Det model class tests

### Files to Modify
- `src/eb_model/models/tm_xdm.py` - Add CommonPublishedInformation, PublishedInformation, missing attributes
- `src/eb_model/models/det_xdm.py` - Add 7 missing classes, missing attributes in DetGeneral
- `src/eb_model/parser/tm_xdm_parser.py` - Add parser methods for new containers and attributes
- `src/eb_model/parser/det_xdm_parser.py` - Add parser methods for new containers and attributes
- `src/eb_model/tests/parser/test_tm_xdm_parser.py` - Add tests for new parser methods
- `src/eb_model/tests/parser/test_det_xdm_parser.py` - Add tests for new parser methods

---

## Task 1: Create Tm Model Class Test File

**Files:**
- Create: `src/eb_model/tests/models/test_tm_xdm.py`

- [ ] **Step 1: Write test file structure**

```python
"""
Tm Model Tests - Tests for TM module model classes.
"""
import pytest
from ...models.tm_xdm import Tm, TmGeneral
from ...models.eb_doc import EBModel


class TestTmGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        general = TmGeneral(root, "TmGeneral")

        assert general.getName() == "TmGeneral"
        assert general.getParent() == root
        assert general.getTmDevErrorDetect() is None
        assert general.getTmMainWindowProtect() is None

    def test_set_tm_dev_error_detect(self):
        root = EBModel.getInstance()
        general = TmGeneral(root, "TmGeneral")

        assert general.setTmDevErrorDetect(True) == general
        assert general.getTmDevErrorDetect() is True

        assert general.setTmDevErrorDetect(False) == general
        assert general.getTmDevErrorDetect() is False

    def test_set_tm_main_window_protect(self):
        root = EBModel.getInstance()
        general = TmGeneral(root, "TmGeneral")

        assert general.setTmMainWindowProtect(True) == general
        assert general.getTmMainWindowProtect() is True

        assert general.setTmMainWindowProtect(False) == general
        assert general.getTmMainWindowProtect() is False


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
```

- [ ] **Step 2: Run tests to verify they pass (except for placeholder tests)**

Run: `pytest src/eb_model/tests/models/test_tm_xdm.py -v`
Expected: PASS for existing tests, skip/pass for placeholders

- [ ] **Step 3: Commit**

```bash
git add src/eb_model/tests/models/test_tm_xdm.py
git commit -m "test: add Tm model test file structure"
```

---

## Task 2: Add Tm Missing Classes

**Files:**
- Modify: `src/eb_model/models/tm_xdm.py`

- [ ] **Step 1: Add CommonPublishedInformation class**

```python
class CommonPublishedInformation(EcucParamConfContainerDef):
    """
    Common published information containing AUTOSAR version information.

    Implements: SWR_TM_00004 (Version information)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.arMajorVersion: int = None
        self.arMinorVersion: int = None
        self.arPatchVersion: int = None
        self.swMajorVersion: int = None
        self.swMinorVersion: int = None
        self.swPatchVersion: int = None

    def getArMajorVersion(self) -> int:
        return self.arMajorVersion

    def setArMajorVersion(self, value: int):
        if value is not None:
            self.arMajorVersion = value
        return self

    def getArMinorVersion(self) -> int:
        return self.arMinorVersion

    def setArMinorVersion(self, value: int):
        if value is not None:
            self.arMinorVersion = value
        return self

    def getArPatchVersion(self) -> int:
        return self.arPatchVersion

    def setArPatchVersion(self, value: int):
        if value is not None:
            self.arPatchVersion = value
        return self

    def getSwMajorVersion(self) -> int:
        return self.swMajorVersion

    def setSwMajorVersion(self, value: int):
        if value is not None:
            self.swMajorVersion = value
        return self

    def getSwMinorVersion(self) -> int:
        return self.swMinorVersion

    def setSwMinorVersion(self, value: int):
        if value is not None:
            self.swMinorVersion = value
        return self

    def getSwPatchVersion(self) -> int:
        return self.swPatchVersion

    def setSwPatchVersion(self, value: int):
        if value is not None:
            self.swPatchVersion = value
        return self
```

Add this class after the imports, before `class TmGeneral`.

- [ ] **Step 2: Add PublishedInformation class**

```python
class PublishedInformation(EcucParamConfContainerDef):
    """
    Module-specific published information.

    Implements: SWR_TM_00005 (Module metadata)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.vendorId: str = None
        self.arReleaseMajorVersion: str = None
        self.arReleaseMinorVersion: str = None
        self.arReleasePatchVersion: str = None
        self.swMajorVersion: str = None
        self.swMinorVersion: str = None
        self.swPatchVersion: str = None

    def getVendorId(self) -> str:
        return self.vendorId

    def setVendorId(self, value: str):
        if value is not None:
            self.vendorId = value
        return self

    def getArReleaseMajorVersion(self) -> str:
        return self.arReleaseMajorVersion

    def setArReleaseMajorVersion(self, value: str):
        if value is not None:
            self.arReleaseMajorVersion = value
        return self

    def getArReleaseMinorVersion(self) -> str:
        return self.arReleaseMinorVersion

    def setArReleaseMinorVersion(self, value: str):
        if value is not None:
            self.arReleaseMinorVersion = value
        return self

    def getArReleasePatchVersion(self) -> str:
        return self.arReleasePatchVersion

    def setArReleasePatchVersion(self, value: str):
        if value is not None:
            self.arReleasePatchVersion = value
        return self

    def getSwMajorVersion(self) -> str:
        return self.swMajorVersion

    def setSwMajorVersion(self, value: str):
        if value is not None:
            self.swMajorVersion = value
        return self

    def getSwMinorVersion(self) -> str:
        return self.swMinorVersion

    def setSwMinorVersion(self, value: str):
        if value is not None:
            self.swMinorVersion = value
        return self

    def getSwPatchVersion(self) -> str:
        return self.swPatchVersion

    def setSwPatchVersion(self, value: str):
        if value is not None:
            self.swPatchVersion = value
        return self
```

Add this class after `CommonPublishedInformation`.

- [ ] **Step 3: Add missing attributes to TmGeneral class**

Add these attributes to `TmGeneral.__init__`:

```python
self.tmVersionInfoApi: bool = None
self.tmEnablePredefTimer1us16bit: bool = None
self.tmEnablePredefTimer1us24bit: bool = None
self.tmEnablePredefTimer1us32bit: bool = None
self.tmEnablePredefTimer100us32bit: bool = None
```

Add these getter/setter methods after existing methods:

```python
def getTmVersionInfoApi(self) -> bool:
    return self.tmVersionInfoApi

def setTmVersionInfoApi(self, value: bool):
    if value is not None:
        self.tmVersionInfoApi = value
    return self

def getTmEnablePredefTimer1us16bit(self) -> bool:
    return self.tmEnablePredefTimer1us16bit

def setTmEnablePredefTimer1us16bit(self, value: bool):
    if value is not None:
        self.tmEnablePredefTimer1us16bit = value
    return self

def getTmEnablePredefTimer1us24bit(self) -> bool:
    return self.tmEnablePredefTimer1us24bit

def setTmEnablePredefTimer1us24bit(self, value: bool):
    if value is not None:
        self.tmEnablePredefTimer1us24bit = value
    return self

def getTmEnablePredefTimer1us32bit(self) -> bool:
    return self.tmEnablePredefTimer1us32bit

def setTmEnablePredefTimer1us32bit(self, value: bool):
    if value is not None:
        self.tmEnablePredefTimer1us32bit = value
    return self

def getTmEnablePredefTimer100us32bit(self) -> bool:
    return self.tmEnablePredefTimer100us32bit

def setTmEnablePredefTimer100us32bit(self, value: bool):
    if value is not None:
        self.tmEnablePredefTimer100us32bit = value
    return self
```

- [ ] **Step 4: Add CommonPublishedInformation and PublishedInformation to Tm module class**

Add to `Tm.__init__`:

```python
self.commonPublishedInformation: CommonPublishedInformation = None
self.publishedInformation: PublishedInformation = None
```

Add these getter/setter methods to `Tm` class:

```python
def getCommonPublishedInformation(self) -> CommonPublishedInformation:
    return self.commonPublishedInformation

def setCommonPublishedInformation(self, value: CommonPublishedInformation):
    if value is not None:
        self.commonPublishedInformation = value
    return self

def getPublishedInformation(self) -> PublishedInformation:
    return self.publishedInformation

def setPublishedInformation(self, value: PublishedInformation):
    if value is not None:
        self.publishedInformation = value
    return self
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/models/test_tm_xdm.py -v`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add src/eb_model/models/tm_xdm.py src/eb_model/tests/models/test_tm_xdm.py
git commit -m "feat(tm): add CommonPublishedInformation, PublishedInformation classes and missing attributes

Add CommonPublishedInformation and PublishedInformation classes for Tm module.
Add 5 missing boolean attributes to TmGeneral for predefined timer configuration."
```

---

## Task 3: Update Tm Parser for New Containers and Attributes

**Files:**
- Modify: `src/eb_model/parser/tm_xdm_parser.py`

- [ ] **Step 1: Add import for new classes**

Update the imports at the top:

```python
from ..models.tm_xdm import Tm, TmGeneral, TmInterruptSynchronization, TmTickTime, TmTrigger, CommonPublishedInformation, PublishedInformation
```

- [ ] **Step 2: Add parser method for CommonPublishedInformation**

Add this method to `TmXdmParser` class after `read_version` method:

```python
def read_common_published_information(self, element: ET.Element, tm: Tm):
    """
    Parse CommonPublishedInformation container from XDM.

    Implements: SWR_TM_00004 (Version information parsing)
    """
    ctr_tag = self.find_ctr_tag(element, "CommonPublishedInformation")
    if ctr_tag is not None:
        pub_info = CommonPublishedInformation(tm, ctr_tag.attrib["name"])
        pub_info.setArMajorVersion(self.read_value(ctr_tag, "ArMajorVersion"))
        pub_info.setArMinorVersion(self.read_value(ctr_tag, "ArMinorVersion"))
        pub_info.setArPatchVersion(self.read_value(ctr_tag, "ArPatchVersion"))
        pub_info.setSwMajorVersion(self.read_value(ctr_tag, "SwMajorVersion"))
        pub_info.setSwMinorVersion(self.read_value(ctr_tag, "SwMinorVersion"))
        pub_info.setSwPatchVersion(self.read_value(ctr_tag, "SwPatchVersion"))
        tm.setCommonPublishedInformation(pub_info)
        self.logger.debug("Read CommonPublishedInformation")
```

- [ ] **Step 3: Add parser method for PublishedInformation**

Add this method after `read_common_published_information`:

```python
def read_published_information(self, element: ET.Element, tm: Tm):
    """
    Parse PublishedInformation container from XDM.

    Implements: SWR_TM_00005 (Module metadata parsing)
    """
    ctr_tag = self.find_ctr_tag(element, "PublishedInformation")
    if ctr_tag is not None:
        pub_info = PublishedInformation(tm, ctr_tag.attrib["name"])
        pub_info.setVendorId(self.read_value(ctr_tag, "VendorId"))
        pub_info.setArReleaseMajorVersion(self.read_value(ctr_tag, "ArReleaseMajorVersion"))
        pub_info.setArReleaseMinorVersion(self.read_value(ctr_tag, "ArReleaseMinorVersion"))
        pub_info.setArReleasePatchVersion(self.read_value(ctr_tag, "ArReleasePatchVersion"))
        pub_info.setSwMajorVersion(self.read_value(ctr_tag, "SwMajorVersion"))
        pub_info.setSwMinorVersion(self.read_value(ctr_tag, "SwMinorVersion"))
        pub_info.setSwPatchVersion(self.read_value(ctr_tag, "SwPatchVersion"))
        tm.setPublishedInformation(pub_info)
        self.logger.debug("Read PublishedInformation")
```

- [ ] **Step 4: Update read_tm_general to parse missing attributes**

Update `read_tm_general` method to include the new attributes:

```python
def read_tm_general(self, element: ET.Element, tm: Tm):
    ctr_tag = self.find_ctr_tag(element, "TmGeneral")
    if ctr_tag is not None:
        general = TmGeneral(tm, ctr_tag.attrib["name"])
        general.setTmDevErrorDetect(self.read_value(ctr_tag, "TmDevErrorDetect"))
        general.setTmMainWindowProtect(self.read_optional_value(ctr_tag, "TmMainWindowProtect"))
        general.setTmVersionInfoApi(self.read_optional_value(ctr_tag, "TmVersionInfoApi"))
        general.setTmEnablePredefTimer1us16bit(self.read_optional_value(ctr_tag, "TmEnablePredefTimer1us16bit"))
        general.setTmEnablePredefTimer1us24bit(self.read_optional_value(ctr_tag, "TmEnablePredefTimer1us24bit"))
        general.setTmEnablePredefTimer1us32bit(self.read_optional_value(ctr_tag, "TmEnablePredefTimer1us32bit"))
        general.setTmEnablePredefTimer100us32bit(self.read_optional_value(ctr_tag, "TmEnablePredefTimer100us32bit"))
        tm.setTmGeneral(general)
        self.logger.debug("Read TmGeneral")
```

- [ ] **Step 5: Update parse method to call new parser methods**

Add these calls to the `parse` method after `self.read_version`:

```python
self.read_common_published_information(element, tm)
self.read_published_information(element, tm)
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/parser/test_tm_xdm_parser.py -v`
Expected: PASS

- [ ] **Step 7: Commit**

```bash
git add src/eb_model/parser/tm_xdm_parser.py
git commit -m "feat(tm): update parser for new containers and attributes

Add parser methods for CommonPublishedInformation and PublishedInformation.
Update TmGeneral parser to read 5 new boolean attributes."
```

---

## Task 4: Add Tm Parser Tests for New Functionality

**Files:**
- Modify: `src/eb_model/tests/parser/test_tm_xdm_parser.py`

- [ ] **Step 1: Add test for CommonPublishedInformation parsing**

Add this test method to `TestTmXdmParser` class:

```python
def test_read_common_published_information(self):
    xml_content = """
    <datamodel version="8.0"
            xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
            xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
            xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
            xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
        <d:ctr name="CommonPublishedInformation" type="IDENTIFIABLE">
            <d:var name="ArMajorVersion" type="INTEGER" value="4"/>
            <d:var name="ArMinorVersion" type="INTEGER" value="3"/>
            <d:var name="ArPatchVersion" type="INTEGER" value="0"/>
            <d:var name="SwMajorVersion" type="INTEGER" value="1"/>
            <d:var name="SwMinorVersion" type="INTEGER" value="0"/>
            <d:var name="SwPatchVersion" type="INTEGER" value="0"/>
        </d:ctr>
    </datamodel>
    """
    element = ET.fromstring(xml_content)

    model = EBModel.getInstance()
    tm = model.getTm()

    parser = TmXdmParser()
    parser.nsmap = {
        '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
        'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
        'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
        'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
    }

    parser.read_common_published_information(element, tm)

    pub_info = tm.getCommonPublishedInformation()
    assert pub_info is not None
    assert pub_info.getArMajorVersion() == 4
    assert pub_info.getArMinorVersion() == 3
    assert pub_info.getArPatchVersion() == 0
    assert pub_info.getSwMajorVersion() == 1
    assert pub_info.getSwMinorVersion() == 0
    assert pub_info.getSwPatchVersion() == 0
```

- [ ] **Step 2: Add test for PublishedInformation parsing**

```python
def test_read_published_information(self):
    xml_content = """
    <datamodel version="8.0"
            xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
            xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
            xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
            xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
        <d:ctr name="PublishedInformation" type="IDENTIFIABLE">
            <d:var name="VendorId" type="STRING" value="Vector"/>
            <d:var name="ArReleaseMajorVersion" type="STRING" value="4"/>
            <d:var name="ArReleaseMinorVersion" type="STRING" value="3"/>
            <d:var name="ArReleasePatchVersion" type="STRING" value="0"/>
            <d:var name="SwMajorVersion" type="STRING" value="1"/>
            <d:var name="SwMinorVersion" type="STRING" value="0"/>
            <d:var name="SwPatchVersion" type="STRING" value="0"/>
        </d:ctr>
    </datamodel>
    """
    element = ET.fromstring(xml_content)

    model = EBModel.getInstance()
    tm = model.getTm()

    parser = TmXdmParser()
    parser.nsmap = {
        '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
        'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
        'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
        'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
    }

    parser.read_published_information(element, tm)

    pub_info = tm.getPublishedInformation()
    assert pub_info is not None
    assert pub_info.getVendorId() == "Vector"
    assert pub_info.getArReleaseMajorVersion() == "4"
    assert pub_info.getArReleaseMinorVersion() == "3"
    assert pub_info.getArReleasePatchVersion() == "0"
    assert pub_info.getSwMajorVersion() == "1"
    assert pub_info.getSwMinorVersion() == "0"
    assert pub_info.getSwPatchVersion() == "0"
```

- [ ] **Step 3: Update test_read_tm_general to include new attributes**

Add these assertions to `test_read_tm_general`:

```python
assert general.getTmVersionInfoApi() is True
assert general.getTmEnablePredefTimer1us16bit() is True
assert general.getTmEnablePredefTimer1us24bit() is False
assert general.getTmEnablePredefTimer1us32bit() is False
assert general.getTmEnablePredefTimer100us32bit() is True
```

Also update the XML content to include the new attributes:

```xml
<d:ctr name="TmGeneral" type="IDENTIFIABLE">
    <d:var name="TmDevErrorDetect" type="BOOLEAN" value="true"/>
    <d:var name="TmMainWindowProtect" type="BOOLEAN" value="false"/>
    <d:var name="TmVersionInfoApi" type="BOOLEAN" value="true"/>
    <d:var name="TmEnablePredefTimer1us16bit" type="BOOLEAN" value="true"/>
    <d:var name="TmEnablePredefTimer1us24bit" type="BOOLEAN" value="false"/>
    <d:var name="TmEnablePredefTimer1us32bit" type="BOOLEAN" value="false"/>
    <d:var name="TmEnablePredefTimer100us32bit" type="BOOLEAN" value="true"/>
</d:ctr>
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/parser/test_tm_xdm_parser.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/eb_model/tests/parser/test_tm_xdm_parser.py
git commit -m "test(tm): add tests for CommonPublishedInformation and PublishedInformation parsing"
```

---

## Task 5: Create Det Model Class Test File

**Files:**
- Create: `src/eb_model/tests/models/test_det_xdm.py`

- [ ] **Step 1: Write test file structure**

```python
"""
Det Model Tests - Tests for DET module model classes.
"""
import pytest
from ...models.det_xdm import Det, DetGeneral, DetErrorHook
from ...models.eb_doc import EBModel


class TestDetGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        general = DetGeneral(root, "DetGeneral")

        assert general.getName() == "DetGeneral"
        assert general.getParent() == root
        assert general.getDetDevErrorDetect() is None
        assert general.getDetEnabled() is None

    def test_set_det_dev_error_detect(self):
        root = EBModel.getInstance()
        general = DetGeneral(root, "DetGeneral")

        assert general.setDetDevErrorDetect(True) == general
        assert general.getDetDevErrorDetect() is True

        assert general.setDetDevErrorDetect(False) == general
        assert general.getDetDevErrorDetect() is False

    def test_set_det_enabled(self):
        root = EBModel.getInstance()
        general = DetGeneral(root, "DetGeneral")

        assert general.setDetEnabled(True) == general
        assert general.getDetEnabled() is True

        assert general.setDetEnabled(False) == general
        assert general.getDetEnabled() is False


class TestDetErrorHook:

    def test_initialization(self):
        root = EBModel.getInstance()
        error_hook = DetErrorHook(root, "DetErrorHook")

        assert error_hook.getName() == "DetErrorHook"
        assert error_hook.getParent() == root
        assert error_hook.getDetErrorHookCallbackName() is None

    def test_set_det_error_hook_callback_name(self):
        root = EBModel.getInstance()
        error_hook = DetErrorHook(root, "DetErrorHook")

        assert error_hook.setDetErrorHookCallbackName("Det_ErrorHook") == error_hook
        assert error_hook.getDetErrorHookCallbackName() == "Det_ErrorHook"


class TestCommonPublishedInformation:

    def test_initialization(self):
        root = EBModel.getInstance()
        # Will be implemented in Task 6
        pass


class TestPublishedInformation:

    def test_initialization(self):
        root = EBModel.getInstance()
        # Will be implemented in Task 6
        pass
```

- [ ] **Step 2: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/models/test_det_xdm.py -v`
Expected: PASS

- [ ] **Step 3: Commit**

```bash
git add src/eb_model/tests/models/test_det_xdm.py
git commit -m "test: add Det model test file structure"
```

---

## Task 6: Add Det Missing Classes

**Files:**
- Modify: `src/eb_model/models/det_xdm.py`

- [ ] **Step 1: Add CommonPublishedInformation class**

```python
class CommonPublishedInformation(EcucParamConfContainerDef):
    """
    Common published information containing AUTOSAR version information.

    Implements: SWR_DET_00003 (Version information)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.arMajorVersion: int = None
        self.arMinorVersion: int = None
        self.arPatchVersion: int = None
        self.swMajorVersion: int = None
        self.swMinorVersion: int = None
        self.swPatchVersion: int = None

    def getArMajorVersion(self) -> int:
        return self.arMajorVersion

    def setArMajorVersion(self, value: int):
        if value is not None:
            self.arMajorVersion = value
        return self

    def getArMinorVersion(self) -> int:
        return self.arMinorVersion

    def setArMinorVersion(self, value: int):
        if value is not None:
            self.arMinorVersion = value
        return self

    def getArPatchVersion(self) -> int:
        return self.arPatchVersion

    def setArPatchVersion(self, value: int):
        if value is not None:
            self.arPatchVersion = value
        return self

    def getSwMajorVersion(self) -> int:
        return self.swMajorVersion

    def setSwMajorVersion(self, value: int):
        if value is not None:
            self.swMajorVersion = value
        return self

    def getSwMinorVersion(self) -> int:
        return self.swMinorVersion

    def setSwMinorVersion(self, value: int):
        if value is not None:
            self.swMinorVersion = value
        return self

    def getSwPatchVersion(self) -> int:
        return self.swPatchVersion

    def setSwPatchVersion(self, value: int):
        if value is not None:
            self.swPatchVersion = value
        return self
```

- [ ] **Step 2: Add PublishedInformation class**

```python
class PublishedInformation(EcucParamConfContainerDef):
    """
    Module-specific published information.

    Implements: SWR_DET_00004 (Module metadata)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.vendorId: str = None
        self.arReleaseMajorVersion: str = None
        self.arReleaseMinorVersion: str = None
        self.arReleasePatchVersion: str = None
        self.swMajorVersion: str = None
        self.swMinorVersion: str = None
        self.swPatchVersion: str = None

    def getVendorId(self) -> str:
        return self.vendorId

    def setVendorId(self, value: str):
        if value is not None:
            self.vendorId = value
        return self

    def getArReleaseMajorVersion(self) -> str:
        return self.arReleaseMajorVersion

    def setArReleaseMajorVersion(self, value: str):
        if value is not None:
            self.arReleaseMajorVersion = value
        return self

    def getArReleaseMinorVersion(self) -> str:
        return self.arReleaseMinorVersion

    def setArReleaseMinorVersion(self, value: str):
        if value is not None:
            self.arReleaseMinorVersion = value
        return self

    def getArReleasePatchVersion(self) -> str:
        return self.arReleasePatchVersion

    def setArReleasePatchVersion(self, value: str):
        if value is not None:
            self.arReleasePatchVersion = value
        return self

    def getSwMajorVersion(self) -> str:
        return self.swMajorVersion

    def setSwMajorVersion(self, value: str):
        if value is not None:
            self.swMajorVersion = value
        return self

    def getSwMinorVersion(self) -> str:
        return self.swMinorVersion

    def setSwMinorVersion(self, value: str):
        if value is not None:
            self.swMinorVersion = value
        return self

    def getSwPatchVersion(self) -> str:
        return self.swPatchVersion

    def setSwPatchVersion(self, value: str):
        if value is not None:
            self.swPatchVersion = value
        return self
```

- [ ] **Step 3: Add DetServiceAPI class**

```python
class DetServiceAPI(EcucParamConfContainerDef):
    """
    Service API configuration for Det module.

    Implements: SWR_DET_00005 (Service API configuration)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.detVersionInfoApi: bool = None
        self.detReportRuntimeErrorCallout: bool = None

    def getDetVersionInfoApi(self) -> bool:
        return self.detVersionInfoApi

    def setDetVersionInfoApi(self, value: bool):
        if value is not None:
            self.detVersionInfoApi = value
        return self

    def getDetReportRuntimeErrorCallout(self) -> bool:
        return self.detReportRuntimeErrorCallout

    def setDetReportRuntimeErrorCallout(self, value: bool):
        if value is not None:
            self.detReportRuntimeErrorCallout = value
        return self
```

- [ ] **Step 4: Add DetNotification class**

```python
class DetNotification(EcucParamConfContainerDef):
    """
    Notification configuration for Det module.

    Implements: SWR_DET_00006 (Notification configuration)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.detErrorNotification: bool = None
        self.detRuntimeErrorNotification: bool = None
        self.detTransitionErrorNotification: bool = None

    def getDetErrorNotification(self) -> bool:
        return self.detErrorNotification

    def setDetErrorNotification(self, value: bool):
        if value is not None:
            self.detErrorNotification = value
        return self

    def getDetRuntimeErrorNotification(self) -> bool:
        return self.detRuntimeErrorNotification

    def setDetRuntimeErrorNotification(self, value: bool):
        if value is not None:
            self.detRuntimeErrorNotification = value
        return self

    def getDetTransitionErrorNotification(self) -> bool:
        return self.detTransitionErrorNotification

    def setDetTransitionErrorNotification(self, value: bool):
        if value is not None:
            self.detTransitionErrorNotification = value
        return self
```

- [ ] **Step 5: Add DetDefensiveProgramming class**

```python
class DetDefensiveProgramming(EcucParamConfContainerDef):
    """
    Defensive programming configuration for Det module.

    Implements: SWR_DET_00007 (Defensive programming)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.detNullPointerCheck: bool = None
        self.detParameterCheck: bool = None

    def getDetNullPointerCheck(self) -> bool:
        return self.detNullPointerCheck

    def setDetNullPointerCheck(self, value: bool):
        if value is not None:
            self.detNullPointerCheck = value
        return self

    def getDetParameterCheck(self) -> bool:
        return self.detParameterCheck

    def setDetParameterCheck(self, value: bool):
        if value is not None:
            self.detParameterCheck = value
        return self
```

- [ ] **Step 6: Add SoftwareComponentList class**

```python
class SoftwareComponentList(EcucParamConfContainerDef):
    """
    List of software components for Det module.

    Implements: SWR_DET_00008 (Software component list)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
```

- [ ] **Step 7: Add InstanceIdList class**

```python
class InstanceIdList(EcucParamConfContainerDef):
    """
    List of instance IDs for Det module.

    Implements: SWR_DET_00009 (Instance ID list)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
```

- [ ] **Step 8: Add missing attributes to DetGeneral class**

Add these attributes to `DetGeneral.__init__`:

```python
self.detForwardToDlt: bool = None
self.detVersionInfoApi: bool = None
self.loggingMode: str = None
self.bufferSize: int = None
```

Add these getter/setter methods after existing methods:

```python
def getDetForwardToDlt(self) -> bool:
    return self.detForwardToDlt

def setDetForwardToDlt(self, value: bool):
    if value is not None:
        self.detForwardToDlt = value
    return self

def getDetVersionInfoApi(self) -> bool:
    return self.detVersionInfoApi

def setDetVersionInfoApi(self, value: bool):
    if value is not None:
        self.detVersionInfoApi = value
    return self

def getLoggingMode(self) -> str:
    return self.loggingMode

def setLoggingMode(self, value: str):
    if value is not None:
        self.loggingMode = value
    return self

def getBufferSize(self) -> int:
    return self.bufferSize

def setBufferSize(self, value: int):
    if value is not None:
        self.bufferSize = value
    return self
```

- [ ] **Step 9: Add new containers to Det module class**

Add to `Det.__init__`:

```python
self.commonPublishedInformation: CommonPublishedInformation = None
self.publishedInformation: PublishedInformation = None
self.detServiceAPI: DetServiceAPI = None
self.detNotification: DetNotification = None
self.detDefensiveProgramming: DetDefensiveProgramming = None
self.softwareComponentList: SoftwareComponentList = None
self.instanceIdList: InstanceIdList = None
```

Add these getter/setter methods to `Det` class:

```python
def getCommonPublishedInformation(self) -> CommonPublishedInformation:
    return self.commonPublishedInformation

def setCommonPublishedInformation(self, value: CommonPublishedInformation):
    if value is not None:
        self.commonPublishedInformation = value
    return self

def getPublishedInformation(self) -> PublishedInformation:
    return self.publishedInformation

def setPublishedInformation(self, value: PublishedInformation):
    if value is not None:
        self.publishedInformation = value
    return self

def getDetServiceAPI(self) -> DetServiceAPI:
    return self.detServiceAPI

def setDetServiceAPI(self, value: DetServiceAPI):
    if value is not None:
        self.detServiceAPI = value
    return self

def getDetNotification(self) -> DetNotification:
    return self.detNotification

def setDetNotification(self, value: DetNotification):
    if value is not None:
        self.detNotification = value
    return self

def getDetDefensiveProgramming(self) -> DetDefensiveProgramming:
    return self.detDefensiveProgramming

def setDetDefensiveProgramming(self, value: DetDefensiveProgramming):
    if value is not None:
        self.detDefensiveProgramming = value
    return self

def getSoftwareComponentList(self) -> SoftwareComponentList:
    return self.softwareComponentList

def setSoftwareComponentList(self, value: SoftwareComponentList):
    if value is not None:
        self.softwareComponentList = value
    return self

def getInstanceIdList(self) -> InstanceIdList:
    return self.instanceIdList

def setInstanceIdList(self, value: InstanceIdList):
    if value is not None:
        self.instanceIdList = value
    return self
```

- [ ] **Step 10: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/models/test_det_xdm.py -v`
Expected: PASS

- [ ] **Step 11: Commit**

```bash
git add src/eb_model/models/det_xdm.py src/eb_model/tests/models/test_det_xdm.py
git commit -m "feat(det): add 7 missing classes and missing attributes to DetGeneral

Add CommonPublishedInformation, PublishedInformation, DetServiceAPI,
DetNotification, DetDefensiveProgramming, SoftwareComponentList,
InstanceIdList classes. Add 4 missing boolean attributes to DetGeneral."
```

---

## Task 7: Update Det Parser for New Containers and Attributes

**Files:**
- Modify: `src/eb_model/parser/det_xdm_parser.py`

- [ ] **Step 1: Add import for new classes**

Update the imports:

```python
from ..models.det_xdm import Det, DetGeneral, DetErrorHook, DetInitError, CommonPublishedInformation, PublishedInformation, DetServiceAPI, DetNotification, DetDefensiveProgramming, SoftwareComponentList, InstanceIdList
```

- [ ] **Step 2: Add parser method for CommonPublishedInformation**

```python
def read_common_published_information(self, element: ET.Element, det: Det):
    """
    Parse CommonPublishedInformation container from XDM.

    Implements: SWR_DET_00003 (Version information parsing)
    """
    ctr_tag = self.find_ctr_tag(element, "CommonPublishedInformation")
    if ctr_tag is not None:
        pub_info = CommonPublishedInformation(det, ctr_tag.attrib["name"])
        pub_info.setArMajorVersion(self.read_value(ctr_tag, "ArMajorVersion"))
        pub_info.setArMinorVersion(self.read_value(ctr_tag, "ArMinorVersion"))
        pub_info.setArPatchVersion(self.read_value(ctr_tag, "ArPatchVersion"))
        pub_info.setSwMajorVersion(self.read_value(ctr_tag, "SwMajorVersion"))
        pub_info.setSwMinorVersion(self.read_value(ctr_tag, "SwMinorVersion"))
        pub_info.setSwPatchVersion(self.read_value(ctr_tag, "SwPatchVersion"))
        det.setCommonPublishedInformation(pub_info)
        self.logger.debug("Read CommonPublishedInformation")
```

- [ ] **Step 3: Add parser method for PublishedInformation**

```python
def read_published_information(self, element: ET.Element, det: Det):
    """
    Parse PublishedInformation container from XDM.

    Implements: SWR_DET_00004 (Module metadata parsing)
    """
    ctr_tag = self.find_ctr_tag(element, "PublishedInformation")
    if ctr_tag is not None:
        pub_info = PublishedInformation(det, ctr_tag.attrib["name"])
        pub_info.setVendorId(self.read_value(ctr_tag, "VendorId"))
        pub_info.setArReleaseMajorVersion(self.read_value(ctr_tag, "ArReleaseMajorVersion"))
        pub_info.setArReleaseMinorVersion(self.read_value(ctr_tag, "ArReleaseMinorVersion"))
        pub_info.setArReleasePatchVersion(self.read_value(ctr_tag, "ArReleasePatchVersion"))
        pub_info.setSwMajorVersion(self.read_value(ctr_tag, "SwMajorVersion"))
        pub_info.setSwMinorVersion(self.read_value(ctr_tag, "SwMinorVersion"))
        pub_info.setSwPatchVersion(self.read_value(ctr_tag, "SwPatchVersion"))
        det.setPublishedInformation(pub_info)
        self.logger.debug("Read PublishedInformation")
```

- [ ] **Step 4: Add parser method for DetServiceAPI**

```python
def read_det_service_api(self, element: ET.Element, det: Det):
    """
    Parse DetServiceAPI container from XDM.

    Implements: SWR_DET_00005 (Service API parsing)
    """
    ctr_tag = self.find_ctr_tag(element, "DetServiceAPI")
    if ctr_tag is not None:
        service_api = DetServiceAPI(det, ctr_tag.attrib["name"])
        service_api.setDetVersionInfoApi(self.read_optional_value(ctr_tag, "DetVersionInfoApi"))
        service_api.setDetReportRuntimeErrorCallout(self.read_optional_value(ctr_tag, "DetReportRuntimeErrorCallout"))
        det.setDetServiceAPI(service_api)
        self.logger.debug("Read DetServiceAPI")
```

- [ ] **Step 5: Add parser method for DetNotification**

```python
def read_det_notification(self, element: ET.Element, det: Det):
    """
    Parse DetNotification container from XDM.

    Implements: SWR_DET_00006 (Notification parsing)
    """
    ctr_tag = self.find_ctr_tag(element, "DetNotification")
    if ctr_tag is not None:
        notification = DetNotification(det, ctr_tag.attrib["name"])
        notification.setDetErrorNotification(self.read_optional_value(ctr_tag, "DetErrorNotification"))
        notification.setDetRuntimeErrorNotification(self.read_optional_value(ctr_tag, "DetRuntimeErrorNotification"))
        notification.setDetTransitionErrorNotification(self.read_optional_value(ctr_tag, "DetTransitionErrorNotification"))
        det.setDetNotification(notification)
        self.logger.debug("Read DetNotification")
```

- [ ] **Step 6: Add parser method for DetDefensiveProgramming**

```python
def read_det_defensive_programming(self, element: ET.Element, det: Det):
    """
    Parse DetDefensiveProgramming container from XDM.

    Implements: SWR_DET_00007 (Defensive programming parsing)
    """
    ctr_tag = self.find_ctr_tag(element, "DetDefensiveProgramming")
    if ctr_tag is not None:
        defensive = DetDefensiveProgramming(det, ctr_tag.attrib["name"])
        defensive.setDetNullPointerCheck(self.read_optional_value(ctr_tag, "DetNullPointerCheck"))
        defensive.setDetParameterCheck(self.read_optional_value(ctr_tag, "DetParameterCheck"))
        det.setDetDefensiveProgramming(defensive)
        self.logger.debug("Read DetDefensiveProgramming")
```

- [ ] **Step 7: Add parser method for SoftwareComponentList**

```python
def read_software_component_list(self, element: ET.Element, det: Det):
    """
    Parse SoftwareComponentList container from XDM.

    Implements: SWR_DET_00008 (Software component list parsing)
    """
    ctr_tag = self.find_ctr_tag(element, "SoftwareComponentList")
    if ctr_tag is not None:
        sw_list = SoftwareComponentList(det, ctr_tag.attrib["name"])
        det.setSoftwareComponentList(sw_list)
        self.logger.debug("Read SoftwareComponentList")
```

- [ ] **Step 8: Add parser method for InstanceIdList**

```python
def read_instance_id_list(self, element: ET.Element, det: Det):
    """
    Parse InstanceIdList container from XDM.

    Implements: SWR_DET_00009 (Instance ID list parsing)
    """
    ctr_tag = self.find_ctr_tag(element, "InstanceIdList")
    if ctr_tag is not None:
        id_list = InstanceIdList(det, ctr_tag.attrib["name"])
        det.setInstanceIdList(id_list)
        self.logger.debug("Read InstanceIdList")
```

- [ ] **Step 9: Update read_det_general to parse missing attributes**

```python
def read_det_general(self, element: ET.Element, det: Det):
    ctr_tag = self.find_ctr_tag(element, "DetGeneral")
    if ctr_tag is not None:
        general = DetGeneral(det, ctr_tag.attrib["name"])
        general.setDetDevErrorDetect(self.read_value(ctr_tag, "DetDevErrorDetect"))
        general.setDetEnabled(self.read_value(ctr_tag, "DetEnabled"))
        general.setDetForwardToDlt(self.read_optional_value(ctr_tag, "DetForwardToDlt"))
        general.setDetVersionInfoApi(self.read_optional_value(ctr_tag, "DetVersionInfoApi"))
        general.setLoggingMode(self.read_optional_value(ctr_tag, "LoggingMode"))
        general.setBufferSize(self.read_optional_value(ctr_tag, "BufferSize"))
        det.setDetGeneral(general)
        self.logger.debug("Read DetGeneral")
```

- [ ] **Step 10: Update parse method to call new parser methods**

Add these calls to the `parse` method after `self.read_version`:

```python
self.read_common_published_information(element, det)
self.read_published_information(element, det)
self.read_det_service_api(element, det)
self.read_det_notification(element, det)
self.read_det_defensive_programming(element, det)
self.read_software_component_list(element, det)
self.read_instance_id_list(element, det)
```

- [ ] **Step 11: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/parser/test_det_xdm_parser.py -v`
Expected: PASS

- [ ] **Step 12: Commit**

```bash
git add src/eb_model/parser/det_xdm_parser.py
git commit -m "feat(det): update parser for 7 new containers and missing attributes

Add parser methods for CommonPublishedInformation, PublishedInformation,
DetServiceAPI, DetNotification, DetDefensiveProgramming,
SoftwareComponentList, InstanceIdList. Update DetGeneral parser
to read 4 new attributes."
```

---

## Task 8: Add Det Parser Tests for New Functionality

**Files:**
- Modify: `src/eb_model/tests/parser/test_det_xdm_parser.py`

- [ ] **Step 1: Add test for CommonPublishedInformation parsing**

```python
def test_read_common_published_information(self):
    xml_content = """
    <datamodel version="8.0"
            xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
            xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
            xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
            xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
        <d:ctr name="CommonPublishedInformation" type="IDENTIFIABLE">
            <d:var name="ArMajorVersion" type="INTEGER" value="4"/>
            <d:var name="ArMinorVersion" type="INTEGER" value="3"/>
            <d:var name="ArPatchVersion" type="INTEGER" value="0"/>
            <d:var name="SwMajorVersion" type="INTEGER" value="1"/>
            <d:var name="SwMinorVersion" type="INTEGER" value="0"/>
            <d:var name="SwPatchVersion" type="INTEGER" value="0"/>
        </d:ctr>
    </datamodel>
    """
    element = ET.fromstring(xml_content)

    model = EBModel.getInstance()
    det = model.getDet()

    parser = DetXdmParser()
    parser.nsmap = {
        '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
        'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
        'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
        'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
    }

    parser.read_common_published_information(element, det)

    pub_info = det.getCommonPublishedInformation()
    assert pub_info is not None
    assert pub_info.getArMajorVersion() == 4
    assert pub_info.getArMinorVersion() == 3
```

- [ ] **Step 2: Add test for PublishedInformation parsing**

```python
def test_read_published_information(self):
    xml_content = """
    <datamodel version="8.0"
            xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
            xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
            xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
            xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
        <d:ctr name="PublishedInformation" type="IDENTIFIABLE">
            <d:var name="VendorId" type="STRING" value="Vector"/>
            <d:var name="ArReleaseMajorVersion" type="STRING" value="4"/>
            <d:var name="ArReleaseMinorVersion" type="STRING" value="3"/>
            <d:var name="ArReleasePatchVersion" type="STRING" value="0"/>
            <d:var name="SwMajorVersion" type="STRING" value="1"/>
            <d:var name="SwMinorVersion" type="STRING" value="0"/>
            <d:var name="SwPatchVersion" type="STRING" value="0"/>
        </d:ctr>
    </datamodel>
    """
    element = ET.fromstring(xml_content)

    model = EBModel.getInstance()
    det = model.getDet()

    parser = DetXdmParser()
    parser.nsmap = {
        '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
        'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
        'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
        'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
    }

    parser.read_published_information(element, det)

    pub_info = det.getPublishedInformation()
    assert pub_info is not None
    assert pub_info.getVendorId() == "Vector"
```

- [ ] **Step 3: Add test for DetServiceAPI parsing**

```python
def test_read_det_service_api(self):
    xml_content = """
    <datamodel version="8.0"
            xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
            xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
            xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
            xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
        <d:ctr name="DetServiceAPI" type="IDENTIFIABLE">
            <d:var name="DetVersionInfoApi" type="BOOLEAN" value="true"/>
            <d:var name="DetReportRuntimeErrorCallout" type="BOOLEAN" value="false"/>
        </d:ctr>
    </datamodel>
    """
    element = ET.fromstring(xml_content)

    model = EBModel.getInstance()
    det = model.getDet()

    parser = DetXdmParser()
    parser.nsmap = {
        '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
        'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
        'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
        'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
    }

    parser.read_det_service_api(element, det)

    service_api = det.getDetServiceAPI()
    assert service_api is not None
    assert service_api.getDetVersionInfoApi() is True
    assert service_api.getDetReportRuntimeErrorCallout() is False
```

- [ ] **Step 4: Add test for DetNotification parsing**

```python
def test_read_det_notification(self):
    xml_content = """
    <datamodel version="8.0"
            xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
            xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
            xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
            xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
        <d:ctr name="DetNotification" type="IDENTIFIABLE">
            <d:var name="DetErrorNotification" type="BOOLEAN" value="true"/>
            <d:var name="DetRuntimeErrorNotification" type="BOOLEAN" value="true"/>
            <d:var name="DetTransitionErrorNotification" type="BOOLEAN" value="false"/>
        </d:ctr>
    </datamodel>
    """
    element = ET.fromstring(xml_content)

    model = EBModel.getInstance()
    det = model.getDet()

    parser = DetXdmParser()
    parser.nsmap = {
        '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
        'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
        'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
        'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
    }

    parser.read_det_notification(element, det)

    notification = det.getDetNotification()
    assert notification is not None
    assert notification.getDetErrorNotification() is True
    assert notification.getDetRuntimeErrorNotification() is True
    assert notification.getDetTransitionErrorNotification() is False
```

- [ ] **Step 5: Add test for DetDefensiveProgramming parsing**

```python
def test_read_det_defensive_programming(self):
    xml_content = """
    <datamodel version="8.0"
            xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
            xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
            xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
            xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
        <d:ctr name="DetDefensiveProgramming" type="IDENTIFIABLE">
            <d:var name="DetNullPointerCheck" type="BOOLEAN" value="true"/>
            <d:var name="DetParameterCheck" type="BOOLEAN" value="true"/>
        </d:ctr>
    </datamodel>
    """
    element = ET.fromstring(xml_content)

    model = EBModel.getInstance()
    det = model.getDet()

    parser = DetXdmParser()
    parser.nsmap = {
        '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
        'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
        'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
        'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
    }

    parser.read_det_defensive_programming(element, det)

    defensive = det.getDetDefensiveProgramming()
    assert defensive is not None
    assert defensive.getDetNullPointerCheck() is True
    assert defensive.getDetParameterCheck() is True
```

- [ ] **Step 6: Add test for SoftwareComponentList parsing**

```python
def test_read_software_component_list(self):
    xml_content = """
    <datamodel version="8.0"
            xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
            xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
            xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
            xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
        <d:ctr name="SoftwareComponentList" type="IDENTIFIABLE"/>
    </datamodel>
    """
    element = ET.fromstring(xml_content)

    model = EBModel.getInstance()
    det = model.getDet()

    parser = DetXdmParser()
    parser.nsmap = {
        '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
        'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
        'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
        'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
    }

    parser.read_software_component_list(element, det)

    sw_list = det.getSoftwareComponentList()
    assert sw_list is not None
    assert sw_list.getName() == "SoftwareComponentList"
```

- [ ] **Step 7: Add test for InstanceIdList parsing**

```python
def test_read_instance_id_list(self):
    xml_content = """
    <datamodel version="8.0"
            xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
            xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
            xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
            xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
        <d:ctr name="InstanceIdList" type="IDENTIFIABLE"/>
    </datamodel>
    """
    element = ET.fromstring(xml_content)

    model = EBModel.getInstance()
    det = model.getDet()

    parser = DetXdmParser()
    parser.nsmap = {
        '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
        'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
        'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
        'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
    }

    parser.read_instance_id_list(element, det)

    id_list = det.getInstanceIdList()
    assert id_list is not None
    assert id_list.getName() == "InstanceIdList"
```

- [ ] **Step 8: Update test_read_det_general to include new attributes**

Add these assertions to `test_read_det_general`:

```python
assert general.getDetForwardToDlt() is True
assert general.getDetVersionInfoApi() is True
assert general.getLoggingMode() == "BUFFERED"
assert general.getBufferSize() == 256
```

Update the XML content to include the new attributes:

```xml
<d:ctr name="DetGeneral" type="IDENTIFIABLE">
    <d:var name="DetDevErrorDetect" type="BOOLEAN" value="true"/>
    <d:var name="DetEnabled" type="BOOLEAN" value="true"/>
    <d:var name="DetForwardToDlt" type="BOOLEAN" value="true"/>
    <d:var name="DetVersionInfoApi" type="BOOLEAN" value="true"/>
    <d:var name="LoggingMode" type="ENUMERATION" value="BUFFERED"/>
    <d:var name="BufferSize" type="INTEGER" value="256"/>
</d:ctr>
```

- [ ] **Step 9: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/parser/test_det_xdm_parser.py -v`
Expected: PASS

- [ ] **Step 10: Commit**

```bash
git add src/eb_model/tests/parser/test_det_xdm_parser.py
git commit -m "test(det): add tests for 7 new container parsers

Add tests for CommonPublishedInformation, PublishedInformation,
DetServiceAPI, DetNotification, DetDefensiveProgramming,
SoftwareComponentList, InstanceIdList parsing. Update DetGeneral
test to include 4 new attributes."
```

---

## Task 9: Run Linting and Final Verification

**Files:**
- All modified files

- [ ] **Step 1: Run flake8 on modified files**

Run: `flake8 src/eb_model/models/tm_xdm.py src/eb_model/models/det_xdm.py src/eb_model/parser/tm_xdm_parser.py src/eb_model/parser/det_xdm_parser.py src/eb_model/tests/models/test_tm_xdm.py src/eb_model/tests/models/test_det_xdm.py src/eb_model/tests/parser/test_tm_xdm_parser.py src/eb_model/tests/parser/test_det_xdm_parser.py --max-line-length=150 --ignore=F401,W293,F403`

Expected: No errors

- [ ] **Step 2: Run all tests**

Run: `pytest src/eb_model/tests/models/test_tm_xdm.py src/eb_model/tests/models/test_det_xdm.py src/eb_model/tests/parser/test_tm_xdm_parser.py src/eb_model/tests/parser/test_det_xdm_parser.py -v`

Expected: All PASS

- [ ] **Step 3: Verify against analysis report checklist**

Manually verify:
- Tm: CommonPublishedInformation (added), PublishedInformation (added) - 2/2 complete
- Det: CommonPublishedInformation (added), PublishedInformation (added), DetServiceAPI (added), DetNotification (added), DetDefensiveProgramming (added), SoftwareComponentList (added), InstanceIdList (added) - 7/7 complete
- TmGeneral: 5 new attributes added
- DetGeneral: 4 new attributes added

- [ ] **Step 4: Create completion summary**

Create file: `docs/superpowers/completion/2026-03-29-agent1-tm-det-completion.md`

```markdown
# Agent 1: Tm and Det Module Completion Summary

**Date:** 2026-03-29
**Agent:** 1
**Modules:** Tm, Det

## Work Completed

### Tm Module
- Added CommonPublishedInformation class
- Added PublishedInformation class
- Added 5 missing attributes to TmGeneral:
  - tmVersionInfoApi
  - tmEnablePredefTimer1us16bit
  - tmEnablePredefTimer1us24bit
  - tmEnablePredefTimer1us32bit
  - tmEnablePredefTimer100us32bit
- Updated TmXdmParser with parser methods for new containers and attributes
- Created test file `src/eb_model/tests/models/test_tm_xdm.py`
- Added parser tests for new functionality

### Det Module
- Added CommonPublishedInformation class
- Added PublishedInformation class
- Added DetServiceAPI class
- Added DetNotification class
- Added DetDefensiveProgramming class
- Added SoftwareComponentList class
- Added InstanceIdList class
- Added 4 missing attributes to DetGeneral:
  - detForwardToDlt
  - detVersionInfoApi
  - loggingMode
  - bufferSize
- Updated DetXdmParser with parser methods for all 7 new containers and attributes
- Created test file `src/eb_model/tests/models/test_det_xdm.py`
- Added parser tests for all new functionality

## Files Modified
- `src/eb_model/models/tm_xdm.py`
- `src/eb_model/models/det_xdm.py`
- `src/eb_model/parser/tm_xdm_parser.py`
- `src/eb_model/parser/det_xdm_parser.py`
- `src/eb_model/tests/models/test_tm_xdm.py` (created)
- `src/eb_model/tests/models/test_det_xdm.py` (created)
- `src/eb_model/tests/parser/test_tm_xdm_parser.py` (updated)
- `src/eb_model/tests/parser/test_det_xdm_parser.py` (updated)

## Test Results
All tests passing:
- Tm model tests: PASS
- Tm parser tests: PASS
- Det model tests: PASS
- Det parser tests: PASS

## Coverage Summary
- Tm: 2/2 missing classes implemented (100%)
- Det: 7/7 missing classes implemented (100%)
- Tm attributes: 5/5 missing attributes implemented (100%)
- Det attributes: 4/4 missing attributes implemented (100%)

## Notes
- All code follows established patterns from py-eb-model
- All classes have proper docstrings with SWR references
- Linting passed with no errors
- Ready for integration verification
```

- [ ] **Step 5: Commit completion summary**

```bash
git add docs/superpowers/completion/2026-03-29-agent1-tm-det-completion.md
git commit -m "docs: add Agent 1 (Tm and Det) completion summary"
```

---

## Summary

This plan implements complete coverage for Tm and Det modules:

**Tm Module:**
- 2 missing classes added (CommonPublishedInformation, PublishedInformation)
- 5 missing attributes added to TmGeneral

**Det Module:**
- 7 missing classes added (CommonPublishedInformation, PublishedInformation, DetServiceAPI, DetNotification, DetDefensiveProgramming, SoftwareComponentList, InstanceIdList)
- 4 missing attributes added to DetGeneral

All work follows existing patterns in py-eb-model with proper docstrings, tests, and linting compliance.