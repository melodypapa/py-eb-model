# Tier 4 Communication Modules Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add support for Tier 4 AUTOSAR communication layer modules (Com, LdCom, PduR, IpduM, ComM, Nm, Crc) to parse EB Tresos XDM files and export to Excel.

**Architecture:** Each module follows the established 3-layer pattern: Parser (XDM → Model), Model (domain objects), Reporter (Model → Excel). All parsers inherit from `AbstractEbModelParser` for namespace-aware XPath parsing.

**Tech Stack:** Python 3.9+, xml.etree.ElementTree for XML parsing, openpyxl for Excel output, pytest for testing.

---

## Scope

This plan implements **7 modules** from Tier 4:
1. **Com** - Communication layer for signal-based communication
2. **LdCom** - Low-level communication module
3. **PduR** - PDU Router for routing PDUs between modules
4. **IpduM** - I-PDU multiplexer for signal groups
5. **ComM** - Communication Manager for bus mode control
6. **Nm** - Network Management (CAN/LIN/Ethernet)
7. **Crc** - Cyclic Redundancy Check module

## File Structure

Each module requires 5 files:
```
src/eb_model/
├── parser/
│   └── com_xdm_parser.py          # NEW (7 total)
├── models/
│   ├── com_xdm.py                 # NEW (7 total)
│   └── eb_doc.py                  # MODIFY (add 7 getter methods)
├── reporter/excel_reporter/
│   └── com_xdm.py                 # NEW (7 total)
├── cli/
│   └── com_xdm_2_xls_cli.py       # NEW (7 total)
├── tests/parser/
│   └── test_com_xdm_parser.py     # NEW (7 total)
└── pyproject.toml                 # MODIFY (add 7 console_scripts)
```

Total files: **35 new, 2 modified** = 37 files

---

## Task 1: Create Com Module Parser

**Files:**
- Create: `src/eb_model/parser/com_xdm_parser.py`
- Test: `src/eb_model/tests/parser/test_com_xdm_parser.py`

- [ ] **Step 1: Write the failing test for ComGeneral parsing**

```python
# src/eb_model/tests/parser/test_com_xdm_parser.py
import xml.etree.ElementTree as ET
from ...parser.com_xdm_parser import ComXdmParser
from ...models.com_xdm import Com, ComGeneral
from ...models.eb_doc import EBModel


class TestComXdmParser:
    def test_read_com_general(self):
        model = EBModel.getInstance()
        com = model.getCom()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="ComConfig" type="IDENTIFIABLE">
                <d:var name="ComEnableUserSupport" type="BOOLEAN" value="true"/>
                <d:var name="ComUserInitSignal" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = ComXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_com_general(element, com)

        general = com.getComGeneral()
        assert general is not None
        assert general.getComEnableUserSupport() is True
        assert general.getComUserInitSignal() is True
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest src/eb_model/tests/parser/test_com_xdm_parser.py::TestComXdmParser::test_read_com_general -v`

Expected: `ImportError: cannot import name 'ComXdmParser' from 'eb_model.parser.com_xdm_parser'` or similar

- [ ] **Step 3: Create Com model classes**

```python
# src/eb_model/models/com_xdm.py
from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class ComGeneral(EcucParamConfContainerDef):
    """General configuration for Com module."""

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.comEnableUserSupport: bool = None
        self.comUserInitSignal: bool = None
        self.comUserStatusSupport: bool = None
        self.comUserTxConfirmation: bool = None
        self.comUserRxIndication: bool = None

    def getComEnableUserSupport(self) -> bool:
        return self.comEnableUserSupport

    def setComEnableUserSupport(self, value: bool):
        if value is not None:
            self.comEnableUserSupport = value
        return self

    def getComUserInitSignal(self) -> bool:
        return self.comUserInitSignal

    def setComUserInitSignal(self, value: bool):
        if value is not None:
            self.comUserInitSignal = value
        return self

    def getComUserStatusSupport(self) -> bool:
        return self.comUserStatusSupport

    def setComUserStatusSupport(self, value: bool):
        if value is not None:
            self.comUserStatusSupport = value
        return self

    def getComUserTxConfirmation(self) -> bool:
        return self.comUserTxConfirmation

    def setComUserTxConfirmation(self, value: bool):
        if value is not None:
            self.comUserTxConfirmation = value
        return self

    def getComUserRxIndication(self) -> bool:
        return self.comUserRxIndication

    def setComUserRxIndication(self, value: bool):
        if value is not None:
            self.comUserRxIndication = value
        return self


class Com(Module):
    """
    AUTOSAR Communication (Com) module.

    Implements: SWR_COM_00001 (Com Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "Com")
        self.comGeneral: ComGeneral = None
        self.logger = logging.getLogger()

    def getComGeneral(self) -> ComGeneral:
        return self.comGeneral

    def setComGeneral(self, value: ComGeneral):
        if value is not None:
            self.comGeneral = value
        return self
```

- [ ] **Step 4: Create Com parser class**

```python
# src/eb_model/parser/com_xdm_parser.py
"""
Com XDM Parser Module - Extracts AUTOSAR Com configuration from EB Tresos XDM files.

Implements:
    - SWR_COM_00001: Com module parsing
    - SWR_COM_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.com_xdm import Com, ComGeneral
from ..parser.eb_parser import AbstractEbModelParser


class ComXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR Com (Communication) module configuration.

    Extracts Com configuration including general settings, signals, and PDUs.

    Implements: SWR_COM_00001 (Com Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the Com XDM parser."""
        super().__init__()
        self.com = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse Com module configuration from XDM element.

        Implements: SWR_COM_00001
        """
        if self.get_component_name(element) != "Com":
            raise ValueError("Invalid <%s> xdm file" % "Com")

        com = doc.getCom()
        self.read_version(element, com)

        self.logger.info("Parse Com ARVersion:<%s> SwVersion:<%s>" %
                        (com.getArVersion().getVersion(), com.getSwVersion().getVersion()))

        self.com = com
        self.read_com_general(element, com)

    def read_com_general(self, element: ET.Element, com: Com):
        """
        Parse ComGeneral configuration from XDM.

        Implements: SWR_COM_00002
        """
        ctr_tag = self.find_ctr_tag(element, "ComConfig")
        if ctr_tag is not None:
            general = ComGeneral(com, ctr_tag.attrib["name"])
            general.setComEnableUserSupport(self.read_value(ctr_tag, "ComEnableUserSupport"))
            general.setComUserInitSignal(self.read_value(ctr_tag, "ComUserInitSignal"))
            general.setComUserStatusSupport(self.read_optional_value(ctr_tag, "ComUserStatusSupport"))
            general.setComUserTxConfirmation(self.read_optional_value(ctr_tag, "ComUserTxConfirmation"))
            general.setComUserRxIndication(self.read_optional_value(ctr_tag, "ComUserRxIndication"))
            com.setComGeneral(general)
            self.logger.debug("Read ComGeneral")
```

- [ ] **Step 5: Add Com to EBModel**

```python
# Modify src/eb_model/models/eb_doc.py - Add to imports at top:
from ..models.com_xdm import Com

# Add method after existing getters:
def getCom(self) -> Com:
    container = EcucParamConfContainerDef(self, "Com")
    Com(container)
    return self.find("/Com/Com")
```

- [ ] **Step 6: Add Com to EbParserFactory**

```python
# Modify src/eb_model/parser/eb_parser_factory.py - Add to imports:
from .com_xdm_parser import ComXdmParser

# Add to _PARSERS dict:
_PARSERS = {
    # ... existing entries ...
    "Com": ComXdmParser,
}
```

- [ ] **Step 7: Run test to verify it passes**

Run: `pytest src/eb_model/tests/parser/test_com_xdm_parser.py::TestComXdmParser::test_read_com_general -v`

Expected: PASS

- [ ] **Step 8: Commit**

```bash
git add src/eb_model/parser/com_xdm_parser.py src/eb_model/models/com_xdm.py src/eb_model/models/eb_doc.py src/eb_model/parser/eb_parser_factory.py src/eb_model/tests/parser/test_com_xdm_parser.py
git commit -m "$(cat <<'EOF'
feat: Add Com module parser

- Implement ComXdmParser with basic general configuration parsing
- Add Com model classes (Com, ComGeneral)
- Register in EbParserFactory and EBModel
- Add unit tests for ComGeneral parsing

Implements: SWR_COM_00001, SWR_COM_00002

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

## Task 2: Create LdCom Module Parser

**Files:**
- Create: `src/eb_model/parser/ldcom_xdm_parser.py`
- Create: `src/eb_model/models/ldcom_xdm.py`
- Modify: `src/eb_model/models/eb_doc.py`
- Modify: `src/eb_model/parser/eb_parser_factory.py`
- Test: `src/eb_model/tests/parser/test_ldcom_xdm_parser.py`

- [ ] **Step 1: Write failing test for LdCom initialization**

```python
# src/eb_model/tests/parser/test_ldcom_xdm_parser.py
import xml.etree.ElementTree as ET
from ...parser.ldcom_xdm_parser import LdComXdmParser
from ...models.ldcom_xdm import LdCom
from ...models.eb_doc import EBModel


class TestLdComXdmParser:
    def test_parse_ldcom(self):
        model = EBModel.getInstance()
        ldcom = model.getLdCom()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:chc type="AR-ELEMENT" value="MODULE-CONFIGURATION" name="LdCom"/>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = LdComXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.parse(element, model)

        assert parser.get_component_name(element) == "LdCom"
        assert ldcom is not None
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest src/eb_model/tests/parser/test_ldcom_xdm_parser.py::TestLdComXdmParser::test_parse_ldcom -v`

Expected: `ImportError` or `NotImplementedError`

- [ ] **Step 3: Create LdCom model**

```python
# src/eb_model/models/ldcom_xdm.py
from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class LdCom(Module):
    """
    AUTOSAR Low-level Communication (LdCom) module.

    Implements: SWR_LDCOM_00001 (LdCom Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "LdCom")
        self.logger = logging.getLogger()
```

- [ ] **Step 4: Create LdCom parser**

```python
# src/eb_model/parser/ldcom_xdm_parser.py
"""
LdCom XDM Parser Module - Extracts AUTOSAR LdCom configuration from EB Tresos XDM files.

Implements:
    - SWR_LDCOM_00001: LdCom module parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.ldcom_xdm import LdCom
from ..parser.eb_parser import AbstractEbModelParser


class LdComXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR LdCom (Low-level Communication) module configuration.

    Implements: SWR_LDCOM_00001 (LdCom Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the LdCom XDM parser."""
        super().__init__()
        self.ldcom = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse LdCom module configuration from XDM element.

        Implements: SWR_LDCOM_00001
        """
        if self.get_component_name(element) != "LdCom":
            raise ValueError("Invalid <%s> xdm file" % "LdCom")

        ldcom = doc.getLdCom()
        self.read_version(element, ldcom)

        self.logger.info("Parse LdCom ARVersion:<%s> SwVersion:<%s>" %
                        (ldcom.getArVersion().getVersion(), ldcom.getSwVersion().getVersion()))

        self.ldcom = ldcom
```

- [ ] **Step 5: Add LdCom to EBModel and EbParserFactory**

```python
# Modify src/eb_model/models/eb_doc.py:
from ..models.ldcom_xdm import LdCom

def getLdCom(self) -> LdCom:
    container = EcucParamConfContainerDef(self, "LdCom")
    LdCom(container)
    return self.find("/LdCom/LdCom")

# Modify src/eb_model/parser/eb_parser_factory.py:
from .ldcom_xdm_parser import LdComXdmParser

# Add to _PARSERS:
"LdCom": LdComXdmParser,
```

- [ ] **Step 6: Run test to verify it passes**

Run: `pytest src/eb_model/tests/parser/test_ldcom_xdm_parser.py::TestLdComXdmParser::test_parse_ldcom -v`

Expected: PASS

- [ ] **Step 7: Commit**

```bash
git add src/eb_model/parser/ldcom_xdm_parser.py src/eb_model/models/ldcom_xdm.py src/eb_model/models/eb_doc.py src/eb_model/parser/eb_parser_factory.py src/eb_model/tests/parser/test_ldcom_xdm_parser.py
git commit -m "$(cat <<'EOF'
feat: Add LdCom module parser

- Implement LdComXdmParser with basic parsing
- Add LdCom model class
- Register in EbParserFactory and EBModel
- Add unit tests for LdCom parsing

Implements: SWR_LDCOM_00001

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

## Task 3: Create PduR Module Parser

**Files:**
- Create: `src/eb_model/parser/pdur_xdm_parser.py`
- Create: `src/eb_model/models/pdur_xdm.py`
- Modify: `src/eb_model/models/eb_doc.py`
- Modify: `src/eb_model/parser/eb_parser_factory.py`
- Test: `src/eb_model/tests/parser/test_pdur_xdm_parser.py`

- [ ] **Step 1: Write failing test for PduR routing configuration**

```python
# src/eb_model/tests/parser/test_pdur_xdm_parser.py
import xml.etree.ElementTree as ET
from ...parser.pdur_xdm_parser import PduRXdmParser
from ...models.pdur_xdm import PduR, PduRRoutingTableEntry
from ...models.eb_doc import EBModel


class TestPduRXdmParser:
    def test_read_pdur_routing_cfgs(self):
        model = EBModel.getInstance()
        pdur = model.getPduR()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="PduRRoutingTable" type="MAP">
                <d:ctr name="PduRRoutingTable_0" type="IDENTIFIABLE">
                    <d:var name="PduRRoutingTableEntryID" type="INTEGER" value="1"/>
                    <d:var name="PduRRoutingPduSID" type="INTEGER" value="100"/>
                    <d:ref name="PduRDestPduRef" type="REFERENCE" value="ASPath:/Com/Com/ComIPdu/ComTxIPdu_0"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = PduRXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_pdur_routing_cfgs(element, pdur)

        routing_cfgs = pdur.getPduRRoutingTableEntryList()
        assert len(routing_cfgs) == 1
        assert routing_cfgs[0].getPduRRoutingTableEntryID() == 1
        assert routing_cfgs[0].getPduRRoutingPduSID() == 100
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest src/eb_model/tests/parser/test_pdur_xdm_parser.py::TestPduRXdmParser::test_read_pdur_routing_cfgs -v`

Expected: `ImportError`

- [ ] **Step 3: Create PduR model**

```python
# src/eb_model/models/pdur_xdm.py
from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class PduRRoutingTableEntry(EcucParamConfContainerDef):
    """PDU routing table entry for PduR."""

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.pduRRoutingTableEntryID: int = None
        self.pduRRoutingPduSID: int = None
        self.pduRDestPduRef: EcucRefType = None
        self.pduRSrcPduRef: EcucRefType = None

    def getPduRRoutingTableEntryID(self) -> int:
        return self.pduRRoutingTableEntryID

    def setPduRRoutingTableEntryID(self, value: int):
        if value is not None:
            self.pduRRoutingTableEntryID = value
        return self

    def getPduRRoutingPduSID(self) -> int:
        return self.pduRRoutingPduSID

    def setPduRRoutingPduSID(self, value: int):
        if value is not None:
            self.pduRRoutingPduSID = value
        return self

    def getPduRDestPduRef(self) -> EcucRefType:
        return self.pduRDestPduRef

    def setPduRDestPduRef(self, value: EcucRefType):
        if value is not None:
            self.pduRDestPduRef = value
        return self

    def getPduRSrcPduRef(self) -> EcucRefType:
        return self.pduRSrcPduRef

    def setPduRSrcPduRef(self, value: EcucRefType):
        if value is not None:
            self.pduRSrcPduRef = value
        return self


class PduR(Module):
    """
    AUTOSAR PDU Router (PduR) module.

    Implements: SWR_PDUR_00001 (PduR Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "PduR")
        self.pduRRoutingTableEntryList: List[PduRRoutingTableEntry] = []
        self.logger = logging.getLogger()

    def getPduRRoutingTableEntryList(self) -> List[PduRRoutingTableEntry]:
        return list(sorted(filter(lambda a: isinstance(a, PduRRoutingTableEntry), self.elements.values()), key=lambda o: o.getName()))

    def addPduRRoutingTableEntry(self, value: PduRRoutingTableEntry):
        self.addElement(value)
        self.pduRRoutingTableEntryList.append(value)
        return self
```

- [ ] **Step 4: Create PduR parser**

```python
# src/eb_model/parser/pdur_xdm_parser.py
"""
PduR XDM Parser Module - Extracts AUTOSAR PduR configuration from EB Tresos XDM files.

Implements:
    - SWR_PDUR_00001: PduR module parsing
    - SWR_PDUR_00002: Routing table parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.pdur_xdm import PduR, PduRRoutingTableEntry
from ..parser.eb_parser import AbstractEbModelParser


class PduRXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR PduR (PDU Router) module configuration.

    Extracts PduR configuration including routing tables and PDU mappings.

    Implements: SWR_PDUR_00001 (PduR Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the PduR XDM parser."""
        super().__init__()
        self.pdur = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse PduR module configuration from XDM element.

        Implements: SWR_PDUR_00001
        """
        if self.get_component_name(element) != "PduR":
            raise ValueError("Invalid <%s> xdm file" % "PduR")

        pdur = doc.getPduR()
        self.read_version(element, pdur)

        self.logger.info("Parse PduR ARVersion:<%s> SwVersion:<%s>" %
                        (pdur.getArVersion().getVersion(), pdur.getSwVersion().getVersion()))

        self.pdur = pdur
        self.read_pdur_routing_cfgs(element, pdur)

    def read_pdur_routing_cfgs(self, element: ET.Element, pdur: PduR):
        """
        Parse PduR routing table entries from XDM.

        Implements: SWR_PDUR_00002
        """
        for ctr_tag in self.find_ctr_tag_list(element, "PduRRoutingTable"):
            cfg = PduRRoutingTableEntry(pdur, ctr_tag.attrib["name"])
            cfg.setPduRRoutingTableEntryID(self.read_value(ctr_tag, "PduRRoutingTableEntryID"))
            cfg.setPduRRoutingPduSID(self.read_optional_value(ctr_tag, "PduRRoutingPduSID"))
            cfg.setPduRDestPduRef(self.read_optional_ref_value(ctr_tag, "PduRDestPduRef"))
            cfg.setPduRSrcPduRef(self.read_optional_ref_value(ctr_tag, "PduRSrcPduRef"))
            pdur.addPduRRoutingTableEntry(cfg)
            self.logger.debug("Read PduRRoutingTableEntry <%s>" % cfg.getName())
```

- [ ] **Step 5: Add PduR to EBModel and EbParserFactory**

```python
# Modify src/eb_model/models/eb_doc.py:
from ..models.pdur_xdm import PduR

def getPduR(self) -> PduR:
    container = EcucParamConfContainerDef(self, "PduR")
    PduR(container)
    return self.find("/PduR/PduR")

# Modify src/eb_model/parser/eb_parser_factory.py:
from .pdur_xdm_parser import PduRXdmParser

# Add to _PARSERS:
"PduR": PduRXdmParser,
```

- [ ] **Step 6: Run test to verify it passes**

Run: `pytest src/eb_model/tests/parser/test_pdur_xdm_parser.py::TestPduRXdmParser::test_read_pdur_routing_cfgs -v`

Expected: PASS

- [ ] **Step 7: Commit**

```bash
git add src/eb_model/parser/pdur_xdm_parser.py src/eb_model/models/pdur_xdm.py src/eb_model/models/eb_doc.py src/eb_model/parser/eb_parser_factory.py src/eb_model/tests/parser/test_pdur_xdm_parser.py
git commit -m "$(cat <<'EOF'
feat: Add PduR module parser

- Implement PduRXdmParser with routing table parsing
- Add PduR model classes (PduR, PduRRoutingTableEntry)
- Register in EbParserFactory and EBModel
- Add unit tests for routing configuration parsing

Implements: SWR_PDUR_00001, SWR_PDUR_00002

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

## Task 4: Create IpduM Module Parser

**Files:**
- Create: `src/eb_model/parser/ipdum_xdm_parser.py`
- Create: `src/eb_model/models/ipdum_xdm.py`
- Modify: `src/eb_model/models/eb_doc.py`
- Modify: `src/eb_model/parser/eb_parser_factory.py`
- Test: `src/eb_model/tests/parser/test_ipdum_xdm_parser.py`

- [ ] **Step 1: Write failing test for IpduM configuration**

```python
# src/eb_model/tests/parser/test_ipdum_xdm_parser.py
import xml.etree.ElementTree as ET
from ...parser.ipdum_xdm_parser import IpduMXdmParser
from ...models.ipdum_xdm import IpduM, IpduMDynPdu
from ...models.eb_doc import EBModel


class TestIpduMXdmParser:
    def test_read_ipdum_dynamic_pdus(self):
        model = EBModel.getInstance()
        ipdum = model.getIpduM()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="IpduMDynamicPdu" type="MAP">
                <d:ctr name="IpduMDynamicPdu_0" type="IDENTIFIABLE">
                    <d:var name="IpduMDynPduId" type="INTEGER" value="1"/>
                    <d:var name="IpduMDynPduLength" type="INTEGER" value="8"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = IpduMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_ipdum_dynamic_pdus(element, ipdum)

        dyn_pdus = ipdum.getIpduMDynPduList()
        assert len(dyn_pdus) == 1
        assert dyn_pdus[0].getIpduMDynPduId() == 1
        assert dyn_pdus[0].getIpduMDynPduLength() == 8
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest src/eb_model/tests/parser/test_ipdum_xdm_parser.py::TestIpduMXdmParser::test_read_ipdum_dynamic_pdus -v`

Expected: `ImportError`

- [ ] **Step 3: Create IpduM model**

```python
# src/eb_model/models/ipdum_xdm.py
from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class IpduMDynPdu(EcucParamConfContainerDef):
    """Dynamic PDU configuration for IpduM."""

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.ipduMDynPduId: int = None
        self.ipduMDynPduLength: int = None
        self.ipduMDynPduRef: EcucRefType = None

    def getIpduMDynPduId(self) -> int:
        return self.ipduMDynPduId

    def setIpduMDynPduId(self, value: int):
        if value is not None:
            self.ipduMDynPduId = value
        return self

    def getIpduMDynPduLength(self) -> int:
        return self.ipduMDynPduLength

    def setIpduMDynPduLength(self, value: int):
        if value is not None:
            self.ipduMDynPduLength = value
        return self

    def getIpduMDynPduRef(self) -> EcucRefType:
        return self.ipduMDynPduRef

    def setIpduMDynPduRef(self, value: EcucRefType):
        if value is not None:
            self.ipduMDynPduRef = value
        return self


class IpduM(Module):
    """
    AUTOSAR I-PDU Multiplexer (IpduM) module.

    Implements: SWR_IPDUM_00001 (IpduM Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "IpduM")
        self.ipduMDynPduList: List[IpduMDynPdu] = []
        self.logger = logging.getLogger()

    def getIpduMDynPduList(self) -> List[IpduMDynPdu]:
        return list(sorted(filter(lambda a: isinstance(a, IpduMDynPdu), self.elements.values()), key=lambda o: o.getName()))

    def addIpduMDynPdu(self, value: IpduMDynPdu):
        self.addElement(value)
        self.ipduMDynPduList.append(value)
        return self
```

- [ ] **Step 4: Create IpduM parser**

```python
# src/eb_model/parser/ipdum_xdm_parser.py
"""
IpduM XDM Parser Module - Extracts AUTOSAR IpduM configuration from EB Tresos XDM files.

Implements:
    - SWR_IPDUM_00001: IpduM module parsing
    - SWR_IPDUM_00002: Dynamic PDU parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.ipdum_xdm import IpduM, IpduMDynPdu
from ..parser.eb_parser import AbstractEbModelParser


class IpduMXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR IpduM (I-PDU Multiplexer) module configuration.

    Extracts IpduM configuration including dynamic PDUs and multiplexing.

    Implements: SWR_IPDUM_00001 (IpduM Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the IpduM XDM parser."""
        super().__init__()
        self.ipdum = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse IpduM module configuration from XDM element.

        Implements: SWR_IPDUM_00001
        """
        if self.get_component_name(element) != "IpduM":
            raise ValueError("Invalid <%s> xdm file" % "IpduM")

        ipdum = doc.getIpduM()
        self.read_version(element, ipdum)

        self.logger.info("Parse IpduM ARVersion:<%s> SwVersion:<%s>" %
                        (ipdum.getArVersion().getVersion(), ipdum.getSwVersion().getVersion()))

        self.ipdum = ipdum
        self.read_ipdum_dynamic_pdus(element, ipdum)

    def read_ipdum_dynamic_pdus(self, element: ET.Element, ipdum: IpduM):
        """
        Parse IpduM dynamic PDU entries from XDM.

        Implements: SWR_IPDUM_00002
        """
        for ctr_tag in self.find_ctr_tag_list(element, "IpduMDynamicPdu"):
            cfg = IpduMDynPdu(ipdum, ctr_tag.attrib["name"])
            cfg.setIpduMDynPduId(self.read_value(ctr_tag, "IpduMDynPduId"))
            cfg.setIpduMDynPduLength(self.read_value(ctr_tag, "IpduMDynPduLength"))
            cfg.setIpduMDynPduRef(self.read_optional_ref_value(ctr_tag, "IpduMDynPduRef"))
            ipdum.addIpduMDynPdu(cfg)
            self.logger.debug("Read IpduMDynPdu <%s>" % cfg.getName())
```

- [ ] **Step 5: Add IpduM to EBModel and EbParserFactory**

```python
# Modify src/eb_model/models/eb_doc.py:
from ..models.ipdum_xdm import IpduM

def getIpduM(self) -> IpduM:
    container = EcucParamConfContainerDef(self, "IpduM")
    IpduM(container)
    return self.find("/IpduM/IpduM")

# Modify src/eb_model/parser/eb_parser_factory.py:
from .ipdum_xdm_parser import IpduMXdmParser

# Add to _PARSERS:
"IpduM": IpduMXdmParser,
```

- [ ] **Step 6: Run test to verify it passes**

Run: `pytest src/eb_model/tests/parser/test_ipdum_xdm_parser.py::TestIpduMXdmParser::test_read_ipdum_dynamic_pdus -v`

Expected: PASS

- [ ] **Step 7: Commit**

```bash
git add src/eb_model/parser/ipdum_xdm_parser.py src/eb_model/models/ipdum_xdm.py src/eb_model/models/eb_doc.py src/eb_model/parser/eb_parser_factory.py src/eb_model/tests/parser/test_ipdum_xdm_parser.py
git commit -m "$(cat <<'EOF'
feat: Add IpduM module parser

- Implement IpduMXdmParser with dynamic PDU parsing
- Add IpduM model classes (IpduM, IpduMDynPdu)
- Register in EbParserFactory and EBModel
- Add unit tests for dynamic PDU parsing

Implements: SWR_IPDUM_00001, SWR_IPDUM_00002

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

## Task 5: Create ComM Module Parser

**Files:**
- Create: `src/eb_model/parser/comm_xdm_parser.py`
- Create: `src/eb_model/models/comm_xdm.py`
- Modify: `src/eb_model/models/eb_doc.py`
- Modify: `src/eb_model/parser/eb_parser_factory.py`
- Test: `src/eb_model/tests/parser/test_comm_xdm_parser.py`

- [ ] **Step 1: Write failing test for ComM channel configuration**

```python
# src/eb_model/tests/parser/test_comm_xdm_parser.py
import xml.etree.ElementTree as ET
from ...parser.comm_xdm_parser import ComMXdmParser
from ...models.comm_xdm import ComM, ComMChannel
from ...models.eb_doc import EBModel


class TestComMXdmParser:
    def test_read_comm_channels(self):
        model = EBModel.getInstance()
        comm = model.getComM()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="ComMChannel" type="MAP">
                <d:ctr name="ComMChannel_Can" type="IDENTIFIABLE">
                    <d:var name="ComMChannelName" type="STRING" value="CanIf"/>
                    <d:var name="ComMChannelId" type="INTEGER" value="1"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = ComMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_comm_channels(element, comm)

        channels = comm.getComMChannelList()
        assert len(channels) == 1
        assert channels[0].getComMChannelName() == "CanIf"
        assert channels[0].getComMChannelId() == 1
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest src/eb_model/tests/parser/test_comm_xdm_parser.py::TestComMXdmParser::test_read_comm_channels -v`

Expected: `ImportError`

- [ ] **Step 3: Create ComM model**

```python
# src/eb_model/models/comm_xdm.py
from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class ComMChannel(EcucParamConfContainerDef):
    """Communication Manager channel configuration."""

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.comMChannelName: str = None
        self.comMChannelId: int = None
        self.comMChannelType: str = None

    def getComMChannelName(self) -> str:
        return self.comMChannelName

    def setComMChannelName(self, value: str):
        if value is not None:
            self.comMChannelName = value
        return self

    def getComMChannelId(self) -> int:
        return self.comMChannelId

    def setComMChannelId(self, value: int):
        if value is not None:
            self.comMChannelId = value
        return self

    def getComMChannelType(self) -> str:
        return self.comMChannelType

    def setComMChannelType(self, value: str):
        if value is not None:
            self.comMChannelType = value
        return self


class ComM(Module):
    """
    AUTOSAR Communication Manager (ComM) module.

    Implements: SWR_COMM_00001 (ComM Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "ComM")
        self.comMChannelList: List[ComMChannel] = []
        self.logger = logging.getLogger()

    def getComMChannelList(self) -> List[ComMChannel]:
        return list(sorted(filter(lambda a: isinstance(a, ComMChannel), self.elements.values()), key=lambda o: o.getName()))

    def addComMChannel(self, value: ComMChannel):
        self.addElement(value)
        self.comMChannelList.append(value)
        return self
```

- [ ] **Step 4: Create ComM parser**

```python
# src/eb_model/parser/comm_xdm_parser.py
"""
ComM XDM Parser Module - Extracts AUTOSAR ComM configuration from EB Tresos XDM files.

Implements:
    - SWR_COMM_00001: ComM module parsing
    - SWR_COMM_00002: Channel configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.comm_xdm import ComM, ComMChannel
from ..parser.eb_parser import AbstractEbModelParser


class ComMXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR ComM (Communication Manager) module configuration.

    Extracts ComM configuration including channels and bus mode control.

    Implements: SWR_COMM_00001 (ComM Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the ComM XDM parser."""
        super().__init__()
        self.comm = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse ComM module configuration from XDM element.

        Implements: SWR_COMM_00001
        """
        if self.get_component_name(element) != "ComM":
            raise ValueError("Invalid <%s> xdm file" % "ComM")

        comm = doc.getComM()
        self.read_version(element, comm)

        self.logger.info("Parse ComM ARVersion:<%s> SwVersion:<%s>" %
                        (comm.getArVersion().getVersion(), comm.getSwVersion().getVersion()))

        self.comm = comm
        self.read_comm_channels(element, comm)

    def read_comm_channels(self, element: ET.Element, comm: ComM):
        """
        Parse ComM channel configurations from XDM.

        Implements: SWR_COMM_00002
        """
        for ctr_tag in self.find_ctr_tag_list(element, "ComMChannel"):
            cfg = ComMChannel(comm, ctr_tag.attrib["name"])
            cfg.setComMChannelName(self.read_value(ctr_tag, "ComMChannelName"))
            cfg.setComMChannelId(self.read_value(ctr_tag, "ComMChannelId"))
            cfg.setComMChannelType(self.read_optional_value(ctr_tag, "ComMChannelType"))
            comm.addComMChannel(cfg)
            self.logger.debug("Read ComMChannel <%s>" % cfg.getName())
```

- [ ] **Step 5: Add ComM to EBModel and EbParserFactory**

```python
# Modify src/eb_model/models/eb_doc.py:
from ..models.comm_xdm import ComM

def getComM(self) -> ComM:
    container = EcucParamConfContainerDef(self, "ComM")
    ComM(container)
    return self.find("/ComM/ComM")

# Modify src/eb_model/parser/eb_parser_factory.py:
from .comm_xdm_parser import ComMXdmParser

# Add to _PARSERS:
"ComM": ComMXdmParser,
```

- [ ] **Step 6: Run test to verify it passes**

Run: `pytest src/eb_model/tests/parser/test_comm_xdm_parser.py::TestComMXdmParser::test_read_comm_channels -v`

Expected: PASS

- [ ] **Step 7: Commit**

```bash
git add src/eb_model/parser/comm_xdm_parser.py src/eb_model/models/comm_xdm.py src/eb_model/models/eb_doc.py src/eb_model/parser/eb_parser_factory.py src/eb_model/tests/parser/test_comm_xdm_parser.py
git commit -m "$(cat <<'EOF'
feat: Add ComM module parser

- Implement ComMXdmParser with channel configuration parsing
- Add ComM model classes (ComM, ComMChannel)
- Register in EbParserFactory and EBModel
- Add unit tests for channel parsing

Implements: SWR_COMM_00001, SWR_COMM_00002

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

## Task 6: Create Nm Module Parser

**Files:**
- Create: `src/eb_model/parser/nm_xdm_parser.py`
- Create: `src/eb_model/models/nm_xdm.py`
- Modify: `src/eb_model/models/eb_doc.py`
- Modify: `src/eb_model/parser/eb_parser_factory.py`
- Test: `src/eb_model/tests/parser/test_nm_xdm_parser.py`

- [ ] **Step 1: Write failing test for Nm channel configuration**

```python
# src/eb_model/tests/parser/test_nm_xdm_parser.py
import xml.etree.ElementTree as ET
from ...parser.nm_xdm_parser import NmXdmParser
from ...models.nm_xdm import Nm, NmChannel
from ...models.eb_doc import EBModel


class TestNmXdmParser:
    def test_read_nm_channels(self):
        model = EBModel.getInstance()
        nm = model.getNm()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="NmChannel" type="MAP">
                <d:ctr name="NmChannel_Can" type="IDENTIFIABLE">
                    <d:var name="NmChannelId" type="INTEGER" value="1"/>
                    <d:var name="NmBusType" type="ENUMERATION" value="CAN"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = NmXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_nm_channels(element, nm)

        channels = nm.getNmChannelList()
        assert len(channels) == 1
        assert channels[0].getNmChannelId() == 1
        assert channels[0].getNmBusType() == "CAN"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest src/eb_model/tests/parser/test_nm_xdm_parser.py::TestNmXdmParser::test_read_nm_channels -v`

Expected: `ImportError`

- [ ] **Step 3: Create Nm model**

```python
# src/eb_model/models/nm_xdm.py
from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class NmChannel(EcucParamConfContainerDef):
    """Network Management channel configuration."""

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.nmChannelId: int = None
        self.nmBusType: str = None
        self.nmIfRef: EcucRefType = None

    def getNmChannelId(self) -> int:
        return self.nmChannelId

    def setNmChannelId(self, value: int):
        if value is not None:
            self.nmChannelId = value
        return self

    def getNmBusType(self) -> str:
        return self.nmBusType

    def setNmBusType(self, value: str):
        if value is not None:
            self.nmBusType = value
        return self

    def getNmIfRef(self) -> EcucRefType:
        return self.nmIfRef

    def setNmIfRef(self, value: EcucRefType):
        if value is not None:
            self.nmIfRef = value
        return self


class Nm(Module):
    """
    AUTOSAR Network Management (Nm) module.

    Implements: SWR_NM_00001 (Nm Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "Nm")
        self.nmChannelList: List[NmChannel] = []
        self.logger = logging.getLogger()

    def getNmChannelList(self) -> List[NmChannel]:
        return list(sorted(filter(lambda a: isinstance(a, NmChannel), self.elements.values()), key=lambda o: o.getName()))

    def addNmChannel(self, value: NmChannel):
        self.addElement(value)
        self.nmChannelList.append(value)
        return self
```

- [ ] **Step 4: Create Nm parser**

```python
# src/eb_model/parser/nm_xdm_parser.py
"""
Nm XDM Parser Module - Extracts AUTOSAR Nm configuration from EB Tresos XDM files.

Implements:
    - SWR_NM_00001: Nm module parsing
    - SWR_NM_00002: Channel configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.nm_xdm import Nm, NmChannel
from ..parser.eb_parser import AbstractEbModelParser


class NmXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR Nm (Network Management) module configuration.

    Extracts Nm configuration including channels and bus type settings.

    Implements: SWR_NM_00001 (Nm Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the Nm XDM parser."""
        super().__init__()
        self.nm = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse Nm module configuration from XDM element.

        Implements: SWR_NM_00001
        """
        if self.get_component_name(element) != "Nm":
            raise ValueError("Invalid <%s> xdm file" % "Nm")

        nm = doc.getNm()
        self.read_version(element, nm)

        self.logger.info("Parse Nm ARVersion:<%s> SwVersion:<%s>" %
                        (nm.getArVersion().getVersion(), nm.getSwVersion().getVersion()))

        self.nm = nm
        self.read_nm_channels(element, nm)

    def read_nm_channels(self, element: ET.Element, nm: Nm):
        """
        Parse Nm channel configurations from XDM.

        Implements: SWR_NM_00002
        """
        for ctr_tag in self.find_ctr_tag_list(element, "NmChannel"):
            cfg = NmChannel(nm, ctr_tag.attrib["name"])
            cfg.setNmChannelId(self.read_value(ctr_tag, "NmChannelId"))
            cfg.setNmBusType(self.read_value(ctr_tag, "NmBusType"))
            cfg.setNmIfRef(self.read_optional_ref_value(ctr_tag, "NmIfRef"))
            nm.addNmChannel(cfg)
            self.logger.debug("Read NmChannel <%s>" % cfg.getName())
```

- [ ] **Step 5: Add Nm to EBModel and EbParserFactory**

```python
# Modify src/eb_model/models/eb_doc.py:
from ..models.nm_xdm import Nm

def getNm(self) -> Nm:
    container = EcucParamConfContainerDef(self, "Nm")
    Nm(container)
    return self.find("/Nm/Nm")

# Modify src/eb_model/parser/eb_parser_factory.py:
from .nm_xdm_parser import NmXdmParser

# Add to _PARSERS:
"Nm": NmXdmParser,
```

- [ ] **Step 6: Run test to verify it passes**

Run: `pytest src/eb_model/tests/parser/test_nm_xdm_parser.py::TestNmXdmParser::test_read_nm_channels -v`

Expected: PASS

- [ ] **Step 7: Commit**

```bash
git add src/eb_model/parser/nm_xdm_parser.py src/eb_model/models/nm_xdm.py src/eb_model/models/eb_doc.py src/eb_model/parser/eb_parser_factory.py src/eb_model/tests/parser/test_nm_xdm_parser.py
git commit -m "$(cat <<'EOF'
feat: Add Nm module parser

- Implement NmXdmParser with channel configuration parsing
- Add Nm model classes (Nm, NmChannel)
- Register in EbParserFactory and EBModel
- Add unit tests for channel parsing

Implements: SWR_NM_00001, SWR_NM_00002

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

## Task 7: Create Crc Module Parser

**Files:**
- Create: `src/eb_model/parser/crc_xdm_parser.py`
- Create: `src/eb_model/models/crc_xdm.py`
- Modify: `src/eb_model/models/eb_doc.py`
- Modify: `src/eb_model/parser/eb_parser_factory.py`
- Test: `src/eb_model/tests/parser/test_crc_xdm_parser.py`

- [ ] **Step 1: Write failing test for Crc configuration**

```python
# src/eb_model/tests/parser/test_crc_xdm_parser.py
import xml.etree.ElementTree as ET
from ...parser.crc_xdm_parser import CrcXdmParser
from ...models.crc_xdm import Crc, CrcConfig
from ...models.eb_doc import EBModel


class TestCrcXdmParser:
    def test_read_crc_config(self):
        model = EBModel.getInstance()
        crc = model.getCrc()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="CrcConfig" type="MAP">
                <d:ctr name="CrcConfig_0" type="IDENTIFIABLE">
                    <d:var name="CrcId" type="INTEGER" value="1"/>
                    <d:var name="CrcCRCType" type="ENUMERATION" value="CRC_8"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = CrcXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_crc_configs(element, crc)

        configs = crc.getCrcConfigList()
        assert len(configs) == 1
        assert configs[0].getCrcId() == 1
        assert configs[0].getCrcCRCType() == "CRC_8"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest src/eb_model/tests/parser/test_crc_xdm_parser.py::TestCrcXdmParser::test_read_crc_config -v`

Expected: `ImportError`

- [ ] **Step 3: Create Crc model**

```python
# src/eb_model/models/crc_xdm.py
from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class CrcConfig(EcucParamConfContainerDef):
    """CRC configuration for data integrity verification."""

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.crcId: int = None
        self.crcCRCType: str = None
        self.crcLength: int = None

    def getCrcId(self) -> int:
        return self.crcId

    def setCrcId(self, value: int):
        if value is not None:
            self.crcId = value
        return self

    def getCrcCRCType(self) -> str:
        return self.crcCRCType

    def setCrcCRCType(self, value: str):
        if value is not None:
            self.crcCRCType = value
        return self

    def getCrcLength(self) -> int:
        return self.crcLength

    def setCrcLength(self, value: int):
        if value is not None:
            self.crcLength = value
        return self


class Crc(Module):
    """
    AUTOSAR Cyclic Redundancy Check (Crc) module.

    Implements: SWR_CRC_00001 (Crc Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "Crc")
        self.crcConfigList: List[CrcConfig] = []
        self.logger = logging.getLogger()

    def getCrcConfigList(self) -> List[CrcConfig]:
        return list(sorted(filter(lambda a: isinstance(a, CrcConfig), self.elements.values()), key=lambda o: o.getName()))

    def addCrcConfig(self, value: CrcConfig):
        self.addElement(value)
        self.crcConfigList.append(value)
        return self
```

- [ ] **Step 4: Create Crc parser**

```python
# src/eb_model/parser/crc_xdm_parser.py
"""
Crc XDM Parser Module - Extracts AUTOSAR Crc configuration from EB Tresos XDM files.

Implements:
    - SWR_CRC_00001: Crc module parsing
    - SWR_CRC_00002: CRC configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.crc_xdm import Crc, CrcConfig
from ..parser.eb_parser import AbstractEbModelParser


class CrcXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR Crc (Cyclic Redundancy Check) module configuration.

    Extracts Crc configuration including CRC type and length settings.

    Implements: SWR_CRC_00001 (Crc Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the Crc XDM parser."""
        super().__init__()
        self.crc = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse Crc module configuration from XDM element.

        Implements: SWR_CRC_00001
        """
        if self.get_component_name(element) != "Crc":
            raise ValueError("Invalid <%s> xdm file" % "Crc")

        crc = doc.getCrc()
        self.read_version(element, crc)

        self.logger.info("Parse Crc ARVersion:<%s> SwVersion:<%s>" %
                        (crc.getArVersion().getVersion(), crc.getSwVersion().getVersion()))

        self.crc = crc
        self.read_crc_configs(element, crc)

    def read_crc_configs(self, element: ET.Element, crc: Crc):
        """
        Parse Crc configurations from XDM.

        Implements: SWR_CRC_00002
        """
        for ctr_tag in self.find_ctr_tag_list(element, "CrcConfig"):
            cfg = CrcConfig(crc, ctr_tag.attrib["name"])
            cfg.setCrcId(self.read_value(ctr_tag, "CrcId"))
            cfg.setCrcCRCType(self.read_value(ctr_tag, "CrcCRCType"))
            cfg.setCrcLength(self.read_optional_value(ctr_tag, "CrcLength"))
            crc.addCrcConfig(cfg)
            self.logger.debug("Read CrcConfig <%s>" % cfg.getName())
```

- [ ] **Step 5: Add Crc to EBModel and EbParserFactory**

```python
# Modify src/eb_model/models/eb_doc.py:
from ..models.crc_xdm import Crc

def getCrc(self) -> Crc:
    container = EcucParamConfContainerDef(self, "Crc")
    Crc(container)
    return self.find("/Crc/Crc")

# Modify src/eb_model/parser/eb_parser_factory.py:
from .crc_xdm_parser import CrcXdmParser

# Add to _PARSERS:
"Crc": CrcXdmParser,
```

- [ ] **Step 6: Run test to verify it passes**

Run: `pytest src/eb_model/tests/parser/test_crc_xdm_parser.py::TestCrcXdmParser::test_read_crc_config -v`

Expected: PASS

- [ ] **Step 7: Commit**

```bash
git add src/eb_model/parser/crc_xdm_parser.py src/eb_model/models/crc_xdm.py src/eb_model/models/eb_doc.py src/eb_model/parser/eb_parser_factory.py src/eb_model/tests/parser/test_crc_xdm_parser.py
git commit -m "$(cat <<'EOF'
feat: Add Crc module parser

- Implement CrcXdmParser with CRC configuration parsing
- Add Crc model classes (Crc, CrcConfig)
- Register in EbParserFactory and EBModel
- Add unit tests for CRC configuration parsing

Implements: SWR_CRC_00001, SWR_CRC_00002

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

## Task 8: Create CLI Entry Points for All Tier 4 Modules

**Files:**
- Create: `src/eb_model/cli/com_xdm_2_xls_cli.py` (7 CLI files)
- Modify: `pyproject.toml`

- [ ] **Step 1: Create Com CLI**

```python
# src/eb_model/cli/com_xdm_2_xls_cli.py
"""
CLI entry point for converting Com XDM files to Excel.
"""
import sys
import argparse
from eb_model.parser.eb_parser_factory import EbParserFactory
from eb_model.models.eb_doc import EBModel
from eb_model.reporter.excel_reporter.com_xdm import ComXdmXlsWriter


def main():
    """Convert Com XDM file to Excel format."""
    parser = argparse.ArgumentParser(description='Convert Com XDM file to Excel')
    parser.add_argument('input_xdm', help='Input Com XDM file path')
    parser.add_argument('-o', '--output', help='Output Excel file path', default='Com.xlsx')
    args = parser.parse_args()

    try:
        model = EBModel.getInstance()
        parser = EbParserFactory.create(args.input_xdm)
        parser.load_xdm(args.input_xdm)
        parser.parse(parser.root, model)

        writer = ComXdmXlsWriter()
        writer.write(model, args.output)
        print(f"Successfully exported to {args.output}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Create LdCom CLI** (same pattern as Com CLI, just replace "Com" with "LdCom")

```python
# src/eb_model/cli/ldcom_xdm_2_xls_cli.py
import sys
import argparse
from eb_model.parser.eb_parser_factory import EbParserFactory
from eb_model.models.eb_doc import EBModel
from eb_model.reporter.excel_reporter.ldcom_xdm import LdComXdmXlsWriter


def main():
    parser = argparse.ArgumentParser(description='Convert LdCom XDM file to Excel')
    parser.add_argument('input_xdm', help='Input LdCom XDM file path')
    parser.add_argument('-o', '--output', help='Output Excel file path', default='LdCom.xlsx')
    args = parser.parse_args()

    try:
        model = EBModel.getInstance()
        parser = EbParserFactory.create(args.input_xdm)
        parser.load_xdm(args.input_xdm)
        parser.parse(parser.root, model)

        writer = LdComXdmXlsWriter()
        writer.write(model, args.output)
        print(f"Successfully exported to {args.output}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 3: Create remaining CLI files** (PduR, IpduM, ComM, Nm, Crc)

Use the same pattern, replacing module names accordingly.

- [ ] **Step 4: Add CLI entries to pyproject.toml**

```toml
# Modify pyproject.toml - Add to [project.scripts]:
com-xdm-xlsx = "eb_model.cli.com_xdm_2_xls_cli:main"
ldcom-xdm-xlsx = "eb_model.cli.ldcom_xdm_2_xls_cli:main"
pdur-xdm-xlsx = "eb_model.cli.pdur_xdm_2_xls_cli:main"
ipdum-xdm-xlsx = "eb_model.cli.ipdum_xdm_2_xls_cli:main"
comm-xdm-xlsx = "eb_model.cli.comm_xdm_2_xls_cli:main"
nm-xdm-xlsx = "eb_model.cli.nm_xdm_2_xls_cli:main"
crc-xdm-xlsx = "eb_model.cli.crc_xdm_2_xls_cli:main"
```

- [ ] **Step 5: Verify CLI installation**

Run: `pip install -e .` then test with `com-xdm-xlsx --help`

Expected: Success with help text

- [ ] **Step 6: Commit**

```bash
git add src/eb_model/cli/com_xdm_2_xls_cli.py src/eb_model/cli/ldcom_xdm_2_xls_cli.py src/eb_model/cli/pdur_xdm_2_xls_cli.py src/eb_model/cli/ipdum_xdm_2_xls_cli.py src/eb_model/cli/comm_xdm_2_xls_cli.py src/eb_model/cli/nm_xdm_2_xls_cli.py src/eb_model/cli/crc_xdm_2_xls_cli.py pyproject.toml
git commit -m "$(cat <<'EOF'
feat: Add CLI entry points for Tier 4 modules

- Add CLI scripts for Com, LdCom, PduR, IpduM, ComM, Nm, Crc
- Register console_scripts in pyproject.toml
- Provide XDM to Excel conversion commands

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

## Task 9: Create Excel Reporters for All Tier 4 Modules

**Files:**
- Create: `src/eb_model/reporter/excel_reporter/com_xdm.py` (7 reporter files)

**Note:** Excel reporters currently have no corresponding test files in the codebase. This task creates the reporter classes following the existing pattern.

- [ ] **Step 1: Create Com Excel reporter**

```python
# src/eb_model/reporter/excel_reporter/com_xdm.py
from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class ComXdmXlsWriter(ExcelReporter):
    """Excel reporter for Com module configuration."""

    def __init__(self) -> None:
        super().__init__()

    def write(self, filename, doc: EBModel, options=None):
        """Write Com configuration to Excel file."""
        self.wb = self.create_workbook()

        self.write_com_general(doc)

        self.save(filename)

    def write_com_general(self, doc: EBModel):
        """Write ComGeneral configuration to Excel sheet."""
        sheet = self.wb.create_sheet("ComGeneral", 0)

        title_row = ["Name", "EnableUserSupport", "UserInitSignal", "UserStatusSupport", "UserTxConfirmation", "UserRxIndication"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getCom().getComGeneral() is not None:
            general = doc.getCom().getComGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getComEnableUserSupport())
            self.write_bool_cell(sheet, row, 3, general.getComUserInitSignal())
            self.write_bool_cell(sheet, row, 4, general.getComUserStatusSupport())
            self.write_bool_cell(sheet, row, 5, general.getComUserTxConfirmation())
            self.write_bool_cell(sheet, row, 6, general.getComUserRxIndication())
            row += 1

        self.auto_width(sheet)
```

- [ ] **Step 2: Verify reporter works with manual test**

Run: Create a test Python script:

```python
import sys
sys.path.insert(0, 'src')
from eb_model.models.eb_doc import EBModel
from eb_model.models.com_xdm import Com, ComGeneral
from eb_model.reporter.excel_reporter.com_xdm import ComXdmXlsWriter

model = EBModel.getInstance()
com = model.getCom()
general = ComGeneral(com, "ComConfig")
general.setComEnableUserSupport(True)
com.setComGeneral(general)

writer = ComXdmXlsWriter()
writer.write_com_general(com)
writer.save('/tmp/test_com.xlsx')
print("Excel generated successfully")
```

Expected: Excel file created at /tmp/test_com.xlsx with "ComGeneral" sheet

- [ ] **Step 3: Create remaining Excel reporters** (LdCom, PduR, IpduM, ComM, Nm, Crc)

Each follows the same pattern with module-specific sheets.

- [ ] **Step 4: Commit**

```bash
git add src/eb_model/reporter/excel_reporter/com_xdm.py src/eb_model/tests/reporter/test_com_xdm_xls_writer.py
git commit -m "$(cat <<'EOF'
feat: Add Excel reporter for Com module

- Implement ComXdmXlsWriter with ComGeneral sheet
- Add unit tests for Excel output generation
- Follow existing Excel reporter patterns

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

Repeat similar commits for other 6 modules.

---

## Task 10: Create Requirements Documentation

**Files:**
- Create: `docs/requirements/swr_com.md`
- Create: `docs/requirements/swr_ldcom.md`
- Create: `docs/requirements/swr_pdur.md`
- Create: `docs/requirements/swr_ipdum.md`
- Create: `docs/requirements/swr_comm.md`
- Create: `docs/requirements/swr_nm.md`
- Create: `docs/requirements/swr_crc.md`

- [ ] **Step 1: Create Com requirements document**

```markdown
# AUTOSAR Communication (Com) Module Requirements

**Document ID**: SWR_COM
**Version**: 1.0
**Date**: 2026-03-28

## SWR_COM_00001: Com Module Parser
**Description**: The system shall provide a parser for AUTOSAR Com module XDM files.

**Priority**: High

**Rationale**: Com module is core to AUTOSAR communication layer.

**Acceptance Criteria**:
- ComXdmParser class inherits from AbstractEbModelParser
- parse() method validates MODULE-CONFIGURATION = "Com"
- Successfully extracts ARVersion and SwVersion from XDM

**Verification**: Unit tests in test_com_xdm_parser.py

## SWR_COM_00002: Com General Configuration Parsing
**Description**: The parser shall extract Com general configuration parameters.

**Priority**: High

**Rationale**: General settings control Com module behavior.

**Acceptance Criteria**:
- Extracts ComEnableUserSupport (BOOLEAN)
- Extracts ComUserInitSignal (BOOLEAN)
- Extracts ComUserStatusSupport (BOOLEAN, optional)
- Extracts ComUserTxConfirmation (BOOLEAN, optional)
- Extracts ComUserRxIndication (BOOLEAN, optional)

**Verification**: Unit test test_read_com_general()
```

- [ ] **Step 2: Create remaining requirements documents**

Follow the same pattern for LdCom, PduR, IpduM, ComM, Nm, Crc.

- [ ] **Step 3: Commit**

```bash
git add docs/requirements/swr_com.md docs/requirements/swr_ldcom.md docs/requirements/swr_pdur.md docs/requirements/swr_ipdum.md docs/requirements/swr_comm.md docs/requirements/swr_nm.md docs/requirements/swr_crc.md
git commit -m "$(cat <<'EOF'
docs: Add Tier 4 module requirements specifications

- Add SWR_COM requirements documentation
- Add SWR_LDCOM requirements documentation
- Add SWR_PDUR requirements documentation
- Add SWR_IPDUM requirements documentation
- Add SWR_COMM requirements documentation
- Add SWR_NM requirements documentation
- Add SWR_CRC requirements documentation

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

## Task 11: Update CLAUDE.md with Tier 4 Modules

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Add Tier 4 modules to CLAUDE.md**

```markdown
# Modify CLAUDE.md - Add to the list of currently registered CLI entry points:
- `com-xdm-xlsx`: Com module XDM to Excel conversion
- `ldcom-xdm-xlsx`: LdCom module XDM to Excel conversion
- `pdur-xdm-xlsx`: PduR module XDM to Excel conversion
- `ipdum-xdm-xlsx`: IpduM module XDM to Excel conversion
- `comm-xdm-xlsx`: ComM module XDM to Excel conversion
- `nm-xdm-xlsx`: Nm module XDM to Excel conversion
- `crc-xdm-xlsx`: Crc module XDM to Excel conversion
```

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "$(cat <<'EOF'
docs: Update CLAUDE.md with Tier 4 module CLI entries

- Add documentation for Tier 4 module commands
- Update CLI entry points list

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

## Task 12: Full Integration Testing

**Files:**
- None (verification only)

- [ ] **Step 1: Run all tests**

Run: `pytest --tb=short -v`

Expected: All tests pass (should include new Tier 4 module tests)

- [ ] **Step 2: Verify linting**

Run: `ruff check src/eb_model/parser/com_xdm_parser.py src/eb_model/models/com_xdm.py`

Expected: No linting errors

Repeat for all 7 modules.

- [ ] **Step 3: Verify CI checks**

Run: `ruff check . --select=E9,F63,F7,F82`

Expected: No critical errors

- [ ] **Step 4: Run integration test**

Create a minimal XDM file for one module and test full flow:

```bash
# Create test XDM
cat > /tmp/test_com.xdm << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<datamodel version="8.0"
    xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
    xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
    xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
    xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
    <d:chc type="AR-ELEMENT" value="MODULE-CONFIGURATION" name="Com"/>
    <d:ctr name="ComConfig" type="IDENTIFIABLE">
        <d:var name="ComEnableUserSupport" type="BOOLEAN" value="true"/>
        <d:var name="ComUserInitSignal" type="BOOLEAN" value="true"/>
    </d:ctr>
</datamodel>
EOF

# Test CLI
com-xdm-xlsx /tmp/test_com.xdm -o /tmp/test_com.xlsx

# Verify output exists
test -f /tmp/test_com.xlsx && echo "Integration test PASSED" || echo "Integration test FAILED"
```

- [ ] **Step 5: Final cleanup**

```bash
rm /tmp/test_com.xdm /tmp/test_com.xlsx
```

---

## Task 13: Final Verification and Documentation

**Files:**
- None (verification only)

- [ ] **Step 1: Verify all files created**

Run: `git status`

Expected: 35 new files + 2 modified files (eb_doc.py, eb_parser_factory.py, pyproject.toml)

- [ ] **Step 2: Verify test coverage**

Run: `pytest --cov=src/eb_model/parser/com_xdm_parser.py --cov=src/eb_model/models/com_xdm.py`

Expected: Reasonable coverage for new modules

- [ ] **Step 3: Final commit summary**

```bash
git log --oneline -n 15
```

Should show commits for all 7 modules with their parsers, models, reporters, CLI, and tests.

- [ ] **Step 4: Prepare PR description**

Document the following for PR:
- Summary of Tier 4 implementation
- Modules added (Com, LdCom, PduR, IpduM, ComM, Nm, Crc)
- Breaking changes: None
- New CLI commands added
- SWR IDs implemented
- Test coverage summary

---

## Success Criteria

This plan is complete when:

- [ ] All 7 parsers inherit from AbstractEbModelParser
- [ ] All 7 models follow the existing Module pattern
- [ ] All 7 modules registered in EbParserFactory
- [ ] All 7 modules registered in EBModel
- [ ] All 7 CLI entry points work correctly
- [ ] All 7 Excel reporters generate valid output
- [ ] Unit tests pass for all parsers and models
- [ ] Integration tests pass (XDM → Model → Excel)
- [ ] Linting passes with no errors
- [ ] Requirements documentation exists for all modules
- [ ] CLAUDE.md updated with new CLI commands
- [ ] All parsers successfully parse at least one real XDM file from ACG-9_2_0_WIN32X86 (if available)

## Estimated Time

- **Task 1-7** (Parser + Model + Tests): 7 modules × 15 min = ~2 hours
- **Task 8** (CLI): 30 min
- **Task 9** (Reporters): 7 modules × 10 min = ~1 hour
- **Task 10** (Requirements): 30 min
- **Task 11** (Documentation): 10 min
- **Task 12** (Integration Testing): 30 min
- **Task 13** (Final Verification): 20 min

**Total**: ~5 hours

## Risks and Notes

1. **XDM File Availability**: The plan assumes sample XDM files exist. If not available, tests use mocked XML.
2. **Module Complexity**: Some Tier 4 modules (PduR, ComM) have complex configurations. Plan focuses on core features.
3. **Reference Dependencies**: Some modules reference each other (e.g., PduR references Com). Tests use mock references.
4. **Excel Reporter Complexity**: Current implementation focuses on basic sheets. Complex layouts deferred to follow-up.

## References

- Design spec: `docs/superpowers/specs/2026-03-23-multi-module-xdm-parser-design.md`
- Existing implementation: CanIf, CanNm modules (Tier 2 reference)
- AUTOSAR specification: R22-11 (Classic Platform)