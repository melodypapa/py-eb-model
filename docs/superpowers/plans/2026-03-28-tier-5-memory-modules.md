# Tier 5 Memory Management Modules Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add support for Tier 5 AUTOSAR memory management modules (MemIf, Fee, Ea, MemMap, MemAcc) to parse EB Tresos XDM files and export to Excel.

**Architecture:** Each module follows the established 3-layer pattern: Parser (XDM → Model), Model (domain objects), Reporter (Model → Excel). All parsers inherit from `AbstractEbModelParser` for namespace-aware XPath parsing.

**Tech Stack:** Python 3.9+, xml.etree.ElementTree for XML parsing, openpyxl for Excel output, pytest for testing.

---

## Scope

This plan implements **5 modules** from Tier 5:
1. **MemIf** - Memory Abstraction Interface layer (sits between NvM and lower-level drivers)
2. **Fee** - Flash EEPROM Emulation driver
3. **Ea** - EEPROM Abstraction driver
4. **MemMap** - Memory Mapping module
5. **MemAcc** - Memory Access module

**Note:** NvM is already implemented in the codebase.

## Module Dependencies

```
NvM (existing)
  ↓
MemIf ←─┐
  ↓     │
Fee ───┤
  ↓     │
Ea ←────┘
  ↓
MemMap
  ↓
MemAcc
```

- NvM uses MemIf for abstracted memory access
- MemIf uses Fee (Flash Emulation) and Ea (EEPROM) as drivers
- MemMap handles memory layout definitions
- MemAcc provides runtime memory access validation

## File Structure

Each module requires 5 files:
```
src/eb_model/
├── parser/
│   ├── memif_xdm_parser.py          # NEW (5 total)
│   ├── fee_xdm_parser.py
│   ├── ea_xdm_parser.py
│   ├── memmap_xdm_parser.py
│   ├── memacc_xdm_parser.py
├── models/
│   ├── memif_xdm.py                 # NEW (5 total)
│   ├── fee_xdm.py
│   ├── ea_xdm.py
│   ├── memmap_xdm.py
│   ├── memacc_xdm.py
│   └── eb_doc.py                    # MODIFY (add 5 getter methods)
├── reporter/excel_reporter/
│   ├── memif_xdm.py                 # NEW (5 total)
│   ├── fee_xdm.py
│   ├── ea_xdm.py
│   ├── memmap_xdm.py
│   └── memacc_xdm.py
├── cli/
│   ├── memif_xdm_2_xls_cli.py       # NEW (5 total)
│   ├── fee_xdm_2_xls_cli.py
│   ├── ea_xdm_2_xls_cli.py
│   ├── memmap_xdm_2_xls_cli.py
│   └── memacc_xdm_2_xls_cli.py
├── tests/parser/
│   ├── test_memif_xdm_parser.py     # NEW (5 total)
│   ├── test_fee_xdm_parser.py
│   ├── test_ea_xdm_parser.py
│   ├── test_memmap_xdm_parser.py
│   └── test_memacc_xdm_parser.py
└── pyproject.toml                   # MODIFY (add 5 console_scripts)
```

Total files: **25 new, 2 modified** = 27 files

---

## Task 1: Create MemIf Module Parser

**Files:**
- Create: `src/eb_model/parser/memif_xdm_parser.py`
- Create: `src/eb_model/models/memif_xdm.py`
- Modify: `src/eb_model/models/eb_doc.py`
- Modify: `src/eb_model/parser/eb_parser_factory.py`
- Test: `src/eb_model/tests/parser/test_memif_xdm_parser.py`

- [ ] **Step 1: Write the failing test for MemIf configuration**

```python
# src/eb_model/tests/parser/test_memif_xdm_parser.py
import xml.etree.ElementTree as ET
from ...parser.memif_xdm_parser import MemIfXdmParser
from ...models.memif_xdm import MemIf, MemIfInit
from ...models.eb_doc import EBModel


class TestMemIfXdmParser:
    def test_read_memif_init(self):
        model = EBModel.getInstance()
        memif = model.getMemIf()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="MemIfInit" type="IDENTIFIABLE">
                <d:var name="MemIfDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="MemIfIndex" type="INTEGER" value="1"/>
                <d:var name="MemIfJobPriority" type="ENUMERATION" value="MEMIF_JOB_PRIORITY_LOW"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = MemIfXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_memif_init(element, memif)

        init = memif.getMemIfInit()
        assert init is not None
        assert init.getMemIfDevErrorDetect() is True
        assert init.getMemIfIndex() == 1
        assert init.getMemIfJobPriority() == "MEMIF_JOB_PRIORITY_LOW"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest src/eb_model/tests/parser/test_memif_xdm_parser.py::TestMemIfXdmParser::test_read_memif_init -v`

Expected: `ImportError: cannot import name 'MemIfXdmParser' from 'eb_model.parser.memif_xdm_parser'`

- [ ] **Step 3: Create MemIf model classes**

```python
# src/eb_model/models/memif_xdm.py
from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class MemIfInit(EcucParamConfContainerDef):
    """Initialization configuration for MemIf module."""

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.memIfDevErrorDetect: bool = None
        self.memIfIndex: int = None
        self.memIfJobPriority: str = None
        self.memIfMaxNumberJobs: int = None

    def getMemIfDevErrorDetect(self) -> bool:
        return self.memIfDevErrorDetect

    def setMemIfDevErrorDetect(self, value: bool):
        if value is not None:
            self.memIfDevErrorDetect = value
        return self

    def getMemIfIndex(self) -> int:
        return self.memIfIndex

    def setMemIfIndex(self, value: int):
        if value is not None:
            self.memIfIndex = value
        return self

    def getMemIfJobPriority(self) -> str:
        return self.memIfJobPriority

    def setMemIfJobPriority(self, value: str):
        if value is not None:
            self.memIfJobPriority = value
        return self

    def getMemIfMaxNumberJobs(self) -> int:
        return self.memIfMaxNumberJobs

    def setMemIfMaxNumberJobs(self, value: int):
        if value is not None:
            self.memIfMaxNumberJobs = value
        return self


class MemIf(Module):
    """
    AUTOSAR Memory Abstraction Interface (MemIf) module.

    Provides a standardized interface between upper layer modules
    and hardware-specific memory drivers (Fee, Ea).

    Implements: SWR_MEMIF_00001 (MemIf Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "MemIf")
        self.memIfInit: MemIfInit = None
        self.logger = logging.getLogger()

    def getMemIfInit(self) -> MemIfInit:
        return self.memIfInit

    def setMemIfInit(self, value: MemIfInit):
        if value is not None:
            self.memIfInit = value
        return self
```

- [ ] **Step 4: Create MemIf parser class**

```python
# src/eb_model/parser/memif_xdm_parser.py
"""
MemIf XDM Parser Module - Extracts AUTOSAR MemIf configuration from EB Tresos XDM files.

Implements:
    - SWR_MEMIF_00001: MemIf module parsing
    - SWR_MEMIF_00002: Init configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.memif_xdm import MemIf, MemIfInit
from ..parser.eb_parser import AbstractEbModelParser


class MemIfXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR MemIf (Memory Abstraction Interface) module configuration.

    Extracts MemIf configuration including initialization settings and
    device abstraction parameters.

    Implements: SWR_MEMIF_00001 (MemIf Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the MemIf XDM parser."""
        super().__init__()
        self.memif = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse MemIf module configuration from XDM element.

        Implements: SWR_MEMIF_00001
        """
        if self.get_component_name(element) != "MemIf":
            raise ValueError("Invalid <%s> xdm file" % "MemIf")

        memif = doc.getMemIf()
        self.read_version(element, memif)

        self.logger.info("Parse MemIf ARVersion:<%s> SwVersion:<%s>" %
                        (memif.getArVersion().getVersion(), memif.getSwVersion().getVersion()))

        self.memif = memif
        self.read_memif_init(element, memif)

    def read_memif_init(self, element: ET.Element, memif: MemIf):
        """
        Parse MemIfInit configuration from XDM.

        Implements: SWR_MEMIF_00002
        """
        ctr_tag = self.find_ctr_tag(element, "MemIfInit")
        if ctr_tag is not None:
            init = MemIfInit(memif, ctr_tag.attrib["name"])
            init.setMemIfDevErrorDetect(self.read_value(ctr_tag, "MemIfDevErrorDetect"))
            init.setMemIfIndex(self.read_value(ctr_tag, "MemIfIndex"))
            init.setMemIfJobPriority(self.read_value(ctr_tag, "MemIfJobPriority"))
            init.setMemIfMaxNumberJobs(self.read_optional_value(ctr_tag, "MemIfMaxNumberJobs"))
            memif.setMemIfInit(init)
            self.logger.debug("Read MemIfInit")
```

- [ ] **Step 5: Add MemIf to EBModel**

```python
# Modify src/eb_model/models/eb_doc.py - Add to imports at top:
from ..models.memif_xdm import MemIf

# Add method after existing getters:
def getMemIf(self) -> MemIf:
    container = EcucParamConfContainerDef(self, "MemIf")
    MemIf(container)
    return self.find("/MemIf/MemIf")
```

- [ ] **Step 6: Add MemIf to EbParserFactory**

```python
# Modify src/eb_model/parser/eb_parser_factory.py - Add to imports:
from .memif_xdm_parser import MemIfXdmParser

# Add to _PARSERS dict:
_PARSERS = {
    # ... existing entries ...
    "MemIf": MemIfXdmParser,
}
```

- [ ] **Step 7: Run test to verify it passes**

Run: `pytest src/eb_model/tests/parser/test_memif_xdm_parser.py::TestMemIfXdmParser::test_read_memif_init -v`

Expected: PASS

- [ ] **Step 8: Commit**

```bash
git add src/eb_model/parser/memif_xdm_parser.py src/eb_model/models/memif_xdm.py src/eb_model/models/eb_doc.py src/eb_model/parser/eb_parser_factory.py src/eb_model/tests/parser/test_memif_xdm_parser.py
git commit -m "$(cat <<'EOF'
feat: Add MemIf module parser

- Implement MemIfXdmParser with init configuration parsing
- Add MemIf model classes (MemIf, MemIfInit)
- Register in EbParserFactory and EBModel
- Add unit tests for MemIf initialization parsing

Implements: SWR_MEMIF_00001, SWR_MEMIF_00002
EOF
)"
```

---

## Task 2: Create Fee Module Parser

**Files:**
- Create: `src/eb_model/parser/fee_xdm_parser.py`
- Create: `src/eb_model/models/fee_xdm.py`
- Modify: `src/eb_model/models/eb_doc.py`
- Modify: `src/eb_model/parser/eb_parser_factory.py`
- Test: `src/eb_model/tests/parser/test_fee_xdm_parser.py`

- [ ] **Step 1: Write failing test for Fee configuration**

```python
# src/eb_model/tests/parser/test_fee_xdm_parser.py
import xml.etree.ElementTree as ET
from ...parser.fee_xdm_parser import FeeXdmParser
from ...models.fee_xdm import Fee, FeeGeneral
from ...models.eb_doc import EBModel


class TestFeeXdmParser:
    def test_read_fee_general(self):
        model = EBModel.getInstance()
        fee = model.getFee()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="FeeGeneral" type="IDENTIFIABLE">
                <d:var name="FeeDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="FeePageSize" type="INTEGER" value="256"/>
                <d:var name="FeeVirtualPageSize" type="INTEGER" value="8"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = FeeXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_fee_general(element, fee)

        general = fee.getFeeGeneral()
        assert general is not None
        assert general.getFeeDevErrorDetect() is True
        assert general.getFeePageSize() == 256
        assert general.getFeeVirtualPageSize() == 8
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest src/eb_model/tests/parser/test_fee_xdm_parser.py::TestFeeXdmParser::test_read_fee_general -v`

Expected: `ImportError`

- [ ] **Step 3: Create Fee model**

```python
# src/eb_model/models/fee_xdm.py
from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class FeeGeneral(EcucParamConfContainerDef):
    """General configuration for Fee module."""

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.feeDevErrorDetect: bool = None
        self.feePageSize: int = None
        self.feeVirtualPageSize: int = None
        self.feeNumberOfSectors: int = None

    def getFeeDevErrorDetect(self) -> bool:
        return self.feeDevErrorDetect

    def setFeeDevErrorDetect(self, value: bool):
        if value is not None:
            self.feeDevErrorDetect = value
        return self

    def getFeePageSize(self) -> int:
        return self.feePageSize

    def setFeePageSize(self, value: int):
        if value is not None:
            self.feePageSize = value
        return self

    def getFeeVirtualPageSize(self) -> int:
        return self.feeVirtualPageSize

    def setFeeVirtualPageSize(self, value: int):
        if value is not None:
            self.feeVirtualPageSize = value
        return self

    def getFeeNumberOfSectors(self) -> int:
        return self.feeNumberOfSectors

    def setFeeNumberOfSectors(self, value: int):
        if value is not None:
            self.feeNumberOfSectors = value
        return self


class Fee(Module):
    """
    AUTOSAR Flash EEPROM Emulation (Fee) module.

    Simulates EEPROM behavior on Flash memory by implementing
    wear-leveling and data consistency mechanisms.

    Implements: SWR_FEE_00001 (Fee Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "Fee")
        self.feeGeneral: FeeGeneral = None
        self.logger = logging.getLogger()

    def getFeeGeneral(self) -> FeeGeneral:
        return self.feeGeneral

    def setFeeGeneral(self, value: FeeGeneral):
        if value is not None:
            self.feeGeneral = value
        return self
```

- [ ] **Step 4: Create Fee parser**

```python
# src/eb_model/parser/fee_xdm_parser.py
"""
Fee XDM Parser Module - Extracts AUTOSAR Fee configuration from EB Tresos XDM files.

Implements:
    - SWR_FEE_00001: Fee module parsing
    - SWR_FEE_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.fee_xdm import Fee, FeeGeneral
from ..parser.eb_parser import AbstractEbModelParser


class FeeXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR Fee (Flash EEPROM Emulation) module configuration.

    Extracts Fee configuration including page size, sector definitions,
    and wear-leveling parameters.

    Implements: SWR_FEE_00001 (Fee Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the Fee XDM parser."""
        super().__init__()
        self.fee = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse Fee module configuration from XDM element.

        Implements: SWR_FEE_00001
        """
        if self.get_component_name(element) != "Fee":
            raise ValueError("Invalid <%s> xdm file" % "Fee")

        fee = doc.getFee()
        self.read_version(element, fee)

        self.logger.info("Parse Fee ARVersion:<%s> SwVersion:<%s>" %
                        (fee.getArVersion().getVersion(), fee.getSwVersion().getVersion()))

        self.fee = fee
        self.read_fee_general(element, fee)

    def read_fee_general(self, element: ET.Element, fee: Fee):
        """
        Parse FeeGeneral configuration from XDM.

        Implements: SWR_FEE_00002
        """
        ctr_tag = self.find_ctr_tag(element, "FeeGeneral")
        if ctr_tag is not None:
            general = FeeGeneral(fee, ctr_tag.attrib["name"])
            general.setFeeDevErrorDetect(self.read_value(ctr_tag, "FeeDevErrorDetect"))
            general.setFeePageSize(self.read_value(ctr_tag, "FeePageSize"))
            general.setFeeVirtualPageSize(self.read_value(ctr_tag, "FeeVirtualPageSize"))
            general.setFeeNumberOfSectors(self.read_optional_value(ctr_tag, "FeeNumberOfSectors"))
            fee.setFeeGeneral(general)
            self.logger.debug("Read FeeGeneral")
```

- [ ] **Step 5: Add Fee to EBModel and EbParserFactory**

```python
# Modify src/eb_model/models/eb_doc.py:
from ..models.fee_xdm import Fee

def getFee(self) -> Fee:
    container = EcucParamConfContainerDef(self, "Fee")
    Fee(container)
    return self.find("/Fee/Fee")

# Modify src/eb_model/parser/eb_parser_factory.py:
from .fee_xdm_parser import FeeXdmParser

# Add to _PARSERS:
"Fee": FeeXdmParser,
```

- [ ] **Step 6: Run test to verify it passes**

Run: `pytest src/eb_model/tests/parser/test_fee_xdm_parser.py::TestFeeXdmParser::test_read_fee_general -v`

Expected: PASS

- [ ] **Step 7: Commit**

```bash
git add src/eb_model/parser/fee_xdm_parser.py src/eb_model/models/fee_xdm.py src/eb_model/models/eb_doc.py src/eb_model/parser/eb_parser_factory.py src/eb_model/tests/parser/test_fee_xdm_parser.py
git commit -m "$(cat <<'EOF'
feat: Add Fee module parser

- Implement FeeXdmParser with general configuration parsing
- Add Fee model classes (Fee, FeeGeneral)
- Register in EbParserFactory and EBModel
- Add unit tests for Fee configuration parsing

Implements: SWR_FEE_00001, SWR_FEE_00002
EOF
)"
```

---

## Task 3: Create Ea Module Parser

**Files:**
- Create: `src/eb_model/parser/ea_xdm_parser.py`
- Create: `src/eb_model/models/ea_xdm.py`
- Modify: `src/eb_model/models/eb_doc.py`
- Modify: `src/eb_model/parser/eb_parser_factory.py`
- Test: `src/eb_model/tests/parser/test_ea_xdm_parser.py`

- [ ] **Step 1: Write failing test for Ea configuration**

```python
# src/eb_model/tests/parser/test_ea_xdm_parser.py
import xml.etree.ElementTree as ET
from ...parser.ea_xdm_parser import EaXdmParser
from ...models.ea_xdm import Ea, EaGeneral
from ...models.eb_doc import EBModel


class TestEaXdmParser:
    def test_read_ea_general(self):
        model = EBModel.getInstance()
        ea = model.getEa()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="EaGeneral" type="IDENTIFIABLE">
                <d:var name="EaDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="EaPageSize" type="INTEGER" value="8"/>
                <d:var name="EaAddressAlignment" type="INTEGER" value="8"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = EaXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_ea_general(element, ea)

        general = ea.getEaGeneral()
        assert general is not None
        assert general.getEaDevErrorDetect() is True
        assert general.getEaPageSize() == 8
        assert general.getEaAddressAlignment() == 8
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest src/eb_model/tests/parser/test_ea_xdm_parser.py::TestEaXdmParser::test_read_ea_general -v`

Expected: `ImportError`

- [ ] **Step 3: Create Ea model**

```python
# src/eb_model/models/ea_xdm.py
from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class EaGeneral(EcucParamConfContainerDef):
    """General configuration for Ea module."""

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.eaDevErrorDetect: bool = None
        self.eaPageSize: int = None
        self.eaAddressAlignment: int = None
        self.eaReadMode: str = None

    def getEaDevErrorDetect(self) -> bool:
        return self.eaDevErrorDetect

    def setEaDevErrorDetect(self, value: bool):
        if value is not None:
            self.eaDevErrorDetect = value
        return self

    def getEaPageSize(self) -> int:
        return self.eaPageSize

    def setEaPageSize(self, value: int):
        if value is not None:
            self.eaPageSize = value
        return self

    def getEaAddressAlignment(self) -> int:
        return self.eaAddressAlignment

    def setEaAddressAlignment(self, value: int):
        if value is not None:
            self.eaAddressAlignment = value
        return self

    def getEaReadMode(self) -> str:
        return self.eaReadMode

    def setEaReadMode(self, value: str):
        if value is not None:
            self.eaReadMode = value
        return self


class Ea(Module):
    """
    AUTOSAR EEPROM Abstraction (Ea) module.

    Provides hardware-independent access to EEPROM memory,
    abstracting the specific EEPROM device characteristics.

    Implements: SWR_EA_00001 (Ea Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "Ea")
        self.eaGeneral: EaGeneral = None
        self.logger = logging.getLogger()

    def getEaGeneral(self) -> EaGeneral:
        return self.eaGeneral

    def setEaGeneral(self, value: EaGeneral):
        if value is not None:
            self.eaGeneral = value
        return self
```

- [ ] **Step 4: Create Ea parser**

```python
# src/eb_model/parser/ea_xdm_parser.py
"""
Ea XDM Parser Module - Extracts AUTOSAR Ea configuration from EB Tresos XDM files.

Implements:
    - SWR_EA_00001: Ea module parsing
    - SWR_EA_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.ea_xdm import Ea, EaGeneral
from ..parser.eb_parser import AbstractEbModelParser


class EaXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR Ea (EEPROM Abstraction) module configuration.

    Extracts Ea configuration including page size, address alignment,
    and device-specific parameters.

    Implements: SWR_EA_00001 (Ea Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the Ea XDM parser."""
        super().__init__()
        self.ea = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse Ea module configuration from XDM element.

        Implements: SWR_EA_00001
        """
        if self.get_component_name(element) != "Ea":
            raise ValueError("Invalid <%s> xdm file" % "Ea")

        ea = doc.getEa()
        self.read_version(element, ea)

        self.logger.info("Parse Ea ARVersion:<%s> SwVersion:<%s>" %
                        (ea.getArVersion().getVersion(), ea.getSwVersion().getVersion()))

        self.ea = ea
        self.read_ea_general(element, ea)

    def read_ea_general(self, element: ET.Element, ea: Ea):
        """
        Parse EaGeneral configuration from XDM.

        Implements: SWR_EA_00002
        """
        ctr_tag = self.find_ctr_tag(element, "EaGeneral")
        if ctr_tag is not None:
            general = EaGeneral(ea, ctr_tag.attrib["name"])
            general.setEaDevErrorDetect(self.read_value(ctr_tag, "EaDevErrorDetect"))
            general.setEaPageSize(self.read_value(ctr_tag, "EaPageSize"))
            general.setEaAddressAlignment(self.read_value(ctr_tag, "EaAddressAlignment"))
            general.setEaReadMode(self.read_optional_value(ctr_tag, "EaReadMode"))
            ea.setEaGeneral(general)
            self.logger.debug("Read EaGeneral")
```

- [ ] **Step 5: Add Ea to EBModel and EbParserFactory**

```python
# Modify src/eb_model/models/eb_doc.py:
from ..models.ea_xdm import Ea

def getEa(self) -> Ea:
    container = EcucParamConfContainerDef(self, "Ea")
    Ea(container)
    return self.find("/Ea/Ea")

# Modify src/eb_model/parser/eb_parser_factory.py:
from .ea_xdm_parser import EaXdmParser

# Add to _PARSERS:
"Ea": EaXdmParser,
```

- [ ] **Step 6: Run test to verify it passes**

Run: `pytest src/eb_model/tests/parser/test_ea_xdm_parser.py::TestEaXdmParser::test_read_ea_general -v`

Expected: PASS

- [ ] **Step 7: Commit**

```bash
git add src/eb_model/parser/ea_xdm_parser.py src/eb_model/models/ea_xdm.py src/eb_model/models/eb_doc.py src/eb_model/parser/eb_parser_factory.py src/eb_model/tests/parser/test_ea_xdm_parser.py
git commit -m "$(cat <<'EOF'
feat: Add Ea module parser

- Implement EaXdmParser with general configuration parsing
- Add Ea model classes (Ea, EaGeneral)
- Register in EbParserFactory and EBModel
- Add unit tests for Ea configuration parsing

Implements: SWR_EA_00001, SWR_EA_00002
EOF
)"
```

---

## Task 4: Create MemMap Module Parser

**Files:**
- Create: `src/eb_model/parser/memmap_xdm_parser.py`
- Create: `src/eb_model/models/memmap_xdm.py`
- Modify: `src/eb_model/models/eb_doc.py`
- Modify: `src/eb_model/parser/eb_parser_factory.py`
- Test: `src/eb_model/tests/parser/test_memmap_xdm_parser.py`

- [ ] **Step 1: Write failing test for MemMap configuration**

```python
# src/eb_model/tests/parser/test_memmap_xdm_parser.py
import xml.etree.ElementTree as ET
from ...parser.memmap_xdm_parser import MemMapXdmParser
from ...models.memmap_xdm import MemMap, MemMapCommon
from ...models.eb_doc import EBModel


class TestMemMapXdmParser:
    def test_read_memmap_common(self):
        model = EBModel.getInstance()
        memmap = model.getMemMap()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="MemMapCommon" type="IDENTIFIABLE">
                <d:var name="MemMapDevErrorDetect" type="BOOLEAN" value="false"/>
                <d:var name="MemMapApi" type="ENUMERATION" value="MEMMAP_AR_MAJOR_VERSION_4_0_3"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = MemMapXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_memmap_common(element, memmap)

        common = memmap.getMemMapCommon()
        assert common is not None
        assert common.getMemMapDevErrorDetect() is False
        assert common.getMemMapApi() == "MEMMAP_AR_MAJOR_VERSION_4_0_3"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest src/eb_model/tests/parser/test_memmap_xdm_parser.py::TestMemMapXdmParser::test_read_memmap_common -v`

Expected: `ImportError`

- [ ] **Step 3: Create MemMap model**

```python
# src/eb_model/models/memmap_xdm.py
from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class MemMapCommon(EcucParamConfContainerDef):
    """Common configuration for MemMap module."""

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.memMapDevErrorDetect: bool = None
        self.memMapApi: str = None
        self.memMapInitStatus: str = None

    def getMemMapDevErrorDetect(self) -> bool:
        return self.memMapDevErrorDetect

    def setMemMapDevErrorDetect(self, value: bool):
        if value is not None:
            self.memMapDevErrorDetect = value
        return self

    def getMemMapApi(self) -> str:
        return self.memMapApi

    def setMemMapApi(self, value: str):
        if value is not None:
            self.memMapApi = value
        return self

    def getMemMapInitStatus(self) -> str:
        return self.memMapInitStatus

    def setMemMapInitStatus(self, value: str):
        if value is not None:
            self.memMapInitStatus = value
        return self


class MemMap(Module):
    """
    AUTOSAR Memory Mapping (MemMap) module.

    Defines memory layout and section assignments for AUTOSAR
    applications and BSW modules.

    Implements: SWR_MEMMAP_00001 (MemMap Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "MemMap")
        self.memMapCommon: MemMapCommon = None
        self.logger = logging.getLogger()

    def getMemMapCommon(self) -> MemMapCommon:
        return self.memMapCommon

    def setMemMapCommon(self, value: MemMapCommon):
        if value is not None:
            self.memMapCommon = value
        return self
```

- [ ] **Step 4: Create MemMap parser**

```python
# src/eb_model/parser/memmap_xdm_parser.py
"""
MemMap XDM Parser Module - Extracts AUTOSAR MemMap configuration from EB Tresos XDM files.

Implements:
    - SWR_MEMMAP_00001: MemMap module parsing
    - SWR_MEMMAP_00002: Common configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.memmap_xdm import MemMap, MemMapCommon
from ..parser.eb_parser import AbstractEbModelParser


class MemMapXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR MemMap (Memory Mapping) module configuration.

    Extracts MemMap configuration including memory section definitions
    and segment mappings.

    Implements: SWR_MEMMAP_00001 (MemMap Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the MemMap XDM parser."""
        super().__init__()
        self.memmap = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse MemMap module configuration from XDM element.

        Implements: SWR_MEMMAP_00001
        """
        if self.get_component_name(element) != "MemMap":
            raise ValueError("Invalid <%s> xdm file" % "MemMap")

        memmap = doc.getMemMap()
        self.read_version(element, memmap)

        self.logger.info("Parse MemMap ARVersion:<%s> SwVersion:<%s>" %
                        (memmap.getArVersion().getVersion(), memmap.getSwVersion().getVersion()))

        self.memmap = memmap
        self.read_memmap_common(element, memmap)

    def read_memmap_common(self, element: ET.Element, memmap: MemMap):
        """
        Parse MemMapCommon configuration from XDM.

        Implements: SWR_MEMMAP_00002
        """
        ctr_tag = self.find_ctr_tag(element, "MemMapCommon")
        if ctr_tag is not None:
            common = MemMapCommon(memmap, ctr_tag.attrib["name"])
            common.setMemMapDevErrorDetect(self.read_value(ctr_tag, "MemMapDevErrorDetect"))
            common.setMemMapApi(self.read_value(ctr_tag, "MemMapApi"))
            common.setMemMapInitStatus(self.read_optional_value(ctr_tag, "MemMapInitStatus"))
            memmap.setMemMapCommon(common)
            self.logger.debug("Read MemMapCommon")
```

- [ ] **Step 5: Add MemMap to EBModel and EbParserFactory**

```python
# Modify src/eb_model/models/eb_doc.py:
from ..models.memmap_xdm import MemMap

def getMemMap(self) -> MemMap:
    container = EcucParamConfContainerDef(self, "MemMap")
    MemMap(container)
    return self.find("/MemMap/MemMap")

# Modify src/eb_model/parser/eb_parser_factory.py:
from .memmap_xdm_parser import MemMapXdmParser

# Add to _PARSERS:
"MemMap": MemMapXdmParser,
```

- [ ] **Step 6: Run test to verify it passes**

Run: `pytest src/eb_model/tests/parser/test_memmap_xdm_parser.py::TestMemMapXdmParser::test_read_memmap_common -v`

Expected: PASS

- [ ] **Step 7: Commit**

```bash
git add src/eb_model/parser/memmap_xdm_parser.py src/eb_model/models/memmap_xdm.py src/eb_model/models/eb_doc.py src/eb_model/parser/eb_parser_factory.py src/eb_model/tests/parser/test_memmap_xdm_parser.py
git commit -m "$(cat <<'EOF'
feat: Add MemMap module parser

- Implement MemMapXdmParser with common configuration parsing
- Add MemMap model classes (MemMap, MemMapCommon)
- Register in EbParserFactory and EBModel
- Add unit tests for MemMap configuration parsing

Implements: SWR_MEMMAP_00001, SWR_MEMMAP_00002
EOF
)"
```

---

## Task 5: Create MemAcc Module Parser

**Files:**
- Create: `src/eb_model/parser/memacc_xdm_parser.py`
- Create: `src/eb_model/models/memacc_xdm.py`
- Modify: `src/eb_model/models/eb_doc.py`
- Modify: `src/eb_model/parser/eb_parser_factory.py`
- Test: `src/eb_model/tests/parser/test_memacc_xdm_parser.py`

- [ ] **Step 1: Write failing test for MemAcc configuration**

```python
# src/eb_model/tests/parser/test_memacc_xdm_parser.py
import xml.etree.ElementTree as ET
from ...parser.memacc_xdm_parser import MemAccXdmParser
from ...models.memacc_xdm import MemAcc, MemAccCommon
from ...models.eb_doc import EBModel


class TestMemAccXdmParser:
    def test_read_memacc_common(self):
        model = EBModel.getInstance()
        memacc = model.getMemAcc()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="MemAccCommon" type="IDENTIFIABLE">
                <d:var name="MemAccDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="MemAccProtectionApi" type="ENUMERATION" value="MEMACC_PROTECTION_FALSE"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = MemAccXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_memacc_common(element, memacc)

        common = memacc.getMemAccCommon()
        assert common is not None
        assert common.getMemAccDevErrorDetect() is True
        assert common.getMemAccProtectionApi() == "MEMACC_PROTECTION_FALSE"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest src/eb_model/tests/parser/test_memacc_xdm_parser.py::TestMemAccXdmParser::test_read_memacc_common -v`

Expected: `ImportError`

- [ ] **Step 3: Create MemAcc model**

```python
# src/eb_model/models/memacc_xdm.py
from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class MemAccCommon(EcucParamConfContainerDef):
    """Common configuration for MemAcc module."""

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.memAccDevErrorDetect: bool = None
        self.memAccProtectionApi: str = None
        self.memAccVirtualProtection: bool = None

    def getMemAccDevErrorDetect(self) -> bool:
        return self.memAccDevErrorDetect

    def setMemAccDevErrorDetect(self, value: bool):
        if value is not None:
            self.memAccDevErrorDetect = value
        return self

    def getMemAccProtectionApi(self) -> str:
        return self.memAccProtectionApi

    def setMemAccProtectionApi(self, value: str):
        if value is not None:
            self.memAccProtectionApi = value
        return self

    def getMemAccVirtualProtection(self) -> bool:
        return self.memAccVirtualProtection

    def setMemAccVirtualProtection(self, value: bool):
        if value is not None:
            self.memAccVirtualProtection = value
        return self


class MemAcc(Module):
    """
    AUTOSAR Memory Access (MemAcc) module.

    Provides memory access protection and runtime address validation
    for application and BSW modules.

    Implements: SWR_MEMACC_00001 (MemAcc Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "MemAcc")
        self.memAccCommon: MemAccCommon = None
        self.logger = logging.getLogger()

    def getMemAccCommon(self) -> MemAccCommon:
        return self.memAccCommon

    def setMemAccCommon(self, value: MemAccCommon):
        if value is not None:
            self.memAccCommon = value
        return self
```

- [ ] **Step 4: Create MemAcc parser**

```python
# src/eb_model/parser/memacc_xdm_parser.py
"""
MemAcc XDM Parser Module - Extracts AUTOSAR MemAcc configuration from EB Tresos XDM files.

Implements:
    - SWR_MEMACC_00001: MemAcc module parsing
    - SWR_MEMACC_00002: Common configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.memacc_xdm import MemAcc, MemAccCommon
from ..parser.eb_parser import AbstractEbModelParser


class MemAccXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR MemAcc (Memory Access) module configuration.

    Extracts MemAcc configuration including protection zones,
    access permissions, and address validation.

    Implements: SWR_MEMACC_00001 (MemAcc Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the MemAcc XDM parser."""
        super().__init__()
        self.memacc = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse MemAcc module configuration from XDM element.

        Implements: SWR_MEMACC_00001
        """
        if self.get_component_name(element) != "MemAcc":
            raise ValueError("Invalid <%s> xdm file" % "MemAcc")

        memacc = doc.getMemAcc()
        self.read_version(element, memacc)

        self.logger.info("Parse MemAcc ARVersion:<%s> SwVersion:<%s>" %
                        (memacc.getArVersion().getVersion(), memacc.getSwVersion().getVersion()))

        self.memacc = memacc
        self.read_memacc_common(element, memacc)

    def read_memacc_common(self, element: ET.Element, memacc: MemAcc):
        """
        Parse MemAccCommon configuration from XDM.

        Implements: SWR_MEMACC_00002
        """
        ctr_tag = self.find_ctr_tag(element, "MemAccCommon")
        if ctr_tag is not None:
            common = MemAccCommon(memacc, ctr_tag.attrib["name"])
            common.setMemAccDevErrorDetect(self.read_value(ctr_tag, "MemAccDevErrorDetect"))
            common.setMemAccProtectionApi(self.read_value(ctr_tag, "MemAccProtectionApi"))
            common.setMemAccVirtualProtection(self.read_optional_value(ctr_tag, "MemAccVirtualProtection"))
            memacc.setMemAccCommon(common)
            self.logger.debug("Read MemAccCommon")
```

- [ ] **Step 5: Add MemAcc to EBModel and EbParserFactory**

```python
# Modify src/eb_model/models/eb_doc.py:
from ..models.memacc_xdm import MemAcc

def getMemAcc(self) -> MemAcc:
    container = EcucParamConfContainerDef(self, "MemAcc")
    MemAcc(container)
    return self.find("/MemAcc/MemAcc")

# Modify src/eb_model/parser/eb_parser_factory.py:
from .memacc_xdm_parser import MemAccXdmParser

# Add to _PARSERS:
"MemAcc": MemAccXdmParser,
```

- [ ] **Step 6: Run test to verify it passes**

Run: `pytest src/eb_model/tests/parser/test_memacc_xdm_parser.py::TestMemAccXdmParser::test_read_memacc_common -v`

Expected: PASS

- [ ] **Step 7: Commit**

```bash
git add src/eb_model/parser/memacc_xdm_parser.py src/eb_model/models/memacc_xdm.py src/eb_model/models/eb_doc.py src/eb_model/parser/eb_parser_factory.py src/eb_model/tests/parser/test_memacc_xdm_parser.py
git commit -m "$(cat <<'EOF'
feat: Add MemAcc module parser

- Implement MemAccXdmParser with common configuration parsing
- Add MemAcc model classes (MemAcc, MemAccCommon)
- Register in EbParserFactory and EBModel
- Add unit tests for MemAcc configuration parsing

Implements: SWR_MEMACC_00001, SWR_MEMACC_00002
EOF
)"
```

---

## Task 6: Create CLI Entry Points for All Tier 5 Modules

**Files:**
- Create: `src/eb_model/cli/memif_xdm_2_xls_cli.py` (5 CLI files)
- Modify: `pyproject.toml`

- [ ] **Step 1: Create MemIf CLI**

```python
# src/eb_model/cli/memif_xdm_2_xls_cli.py
"""
CLI entry point for converting MemIf XDM files to Excel.
"""
import sys
import argparse
from eb_model.parser.eb_parser_factory import EbParserFactory
from eb_model.models.eb_doc import EBModel
from eb_model.reporter.excel_reporter.memif_xdm import MemIfXdmXlsWriter


def main():
    """Convert MemIf XDM file to Excel format."""
    parser = argparse.ArgumentParser(description='Convert MemIf XDM file to Excel')
    parser.add_argument('input_xdm', help='Input MemIf XDM file path')
    parser.add_argument('-o', '--output', help='Output Excel file path', default='MemIf.xlsx')
    args = parser.parse_args()

    try:
        model = EBModel.getInstance()
        parser = EbParserFactory.create(args.input_xdm)
        parser.load_xdm(args.input_xdm)
        parser.parse(parser.root, model)

        writer = MemIfXdmXlsWriter()
        writer.write(model, args.output)
        print(f"Successfully exported to {args.output}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Create remaining CLI files** (Fee, Ea, MemMap, MemAcc)

Use the same pattern as MemIf CLI, replacing module names accordingly:
- `src/eb_model/cli/fee_xdm_2_xls_cli.py`
- `src/eb_model/cli/ea_xdm_2_xls_cli.py`
- `src/eb_model/cli/memmap_xdm_2_xls_cli.py`
- `src/eb_model/cli/memacc_xdm_2_xls_cli.py`

- [ ] **Step 3: Add CLI entries to pyproject.toml**

```toml
# Modify pyproject.toml - Add to [project.scripts]:
memif-xdm-xlsx = "eb_model.cli.memif_xdm_2_xls_cli:main"
fee-xdm-xlsx = "eb_model.cli.fee_xdm_2_xls_cli:main"
ea-xdm-xlsx = "eb_model.cli.ea_xdm_2_xls_cli:main"
memmap-xdm-xlsx = "eb_model.cli.memmap_xdm_2_xls_cli:main"
memacc-xdm-xlsx = "eb_model.cli.memacc_xdm_2_xls_cli:main"
```

- [ ] **Step 4: Verify CLI installation**

Run: `pip install -e .` then test with `memif-xdm-xlsx --help`

Expected: Success with help text

- [ ] **Step 5: Commit**

```bash
git add src/eb_model/cli/memif_xdm_2_xls_cli.py src/eb_model/cli/fee_xdm_2_xls_cli.py src/eb_model/cli/ea_xdm_2_xls_cli.py src/eb_model/cli/memmap_xdm_2_xls_cli.py src/eb_model/cli/memacc_xdm_2_xls_cli.py pyproject.toml
git commit -m "$(cat <<'EOF'
feat: Add CLI entry points for Tier 5 modules

- Add CLI scripts for MemIf, Fee, Ea, MemMap, MemAcc
- Register console_scripts in pyproject.toml
- Provide XDM to Excel conversion commands
EOF
)"
```

---

## Task 7: Create Excel Reporters for All Tier 5 Modules

**Files:**
- Create: `src/eb_model/reporter/excel_reporter/memif_xdm.py` (5 reporter files)

- [ ] **Step 1: Create MemIf Excel reporter**

```python
# src/eb_model/reporter/excel_reporter/memif_xdm.py
from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class MemIfXdmXlsWriter(ExcelReporter):
    """Excel reporter for MemIf module configuration."""

    def __init__(self) -> None:
        super().__init__()

    def write(self, filename, doc: EBModel, options=None):
        """Write MemIf configuration to Excel file."""
        self.wb = self.create_workbook()

        self.write_memif_init(doc)

        self.save(filename)

    def write_memif_init(self, doc: EBModel):
        """Write MemIfInit configuration to Excel sheet."""
        sheet = self.wb.create_sheet("MemIfInit", 0)

        title_row = ["Name", "DevErrorDetect", "Index", "JobPriority", "MaxNumberJobs"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getMemIf().getMemIfInit() is not None:
            init = doc.getMemIf().getMemIfInit()
            self.write_cell(sheet, row, 1, init.getName())
            self.write_bool_cell(sheet, row, 2, init.getMemIfDevErrorDetect())
            self.write_int_cell(sheet, row, 3, init.getMemIfIndex())
            self.write_cell(sheet, row, 4, init.getMemIfJobPriority())
            self.write_int_cell(sheet, row, 5, init.getMemIfMaxNumberJobs())
            row += 1

        self.auto_width(sheet)
```

- [ ] **Step 2: Create remaining Excel reporters** (Fee, Ea, MemMap, MemAcc)

Each follows the same pattern with module-specific sheets and configuration fields.

- [ ] **Step 3: Commit**

```bash
git add src/eb_model/reporter/excel_reporter/memif_xdm.py src/eb_model/reporter/excel_reporter/fee_xdm.py src/eb_model/reporter/excel_reporter/ea_xdm.py src/eb_model/reporter/excel_reporter/memmap_xdm.py src/eb_model/reporter/excel_reporter/memacc_xdm.py
git commit -m "$(cat <<'EOF'
feat: Add Excel reporters for Tier 5 modules

- Implement Excel reporters for MemIf, Fee, Ea, MemMap, MemAcc
- Each reporter exports module configuration to Excel sheets
- Follow existing Excel reporter patterns
EOF
)"
```

---

## Task 8: Create Requirements Documentation

**Files:**
- Create: `docs/requirements/swr_memif.md`
- Create: `docs/requirements/swr_fee.md`
- Create: `docs/requirements/swr_ea.md`
- Create: `docs/requirements/swr_memmap.md`
- Create: `docs/requirements/swr_memacc.md`

- [ ] **Step 1: Create MemIf requirements document**

```markdown
# AUTOSAR Memory Abstraction Interface (MemIf) Module Requirements

**Document ID**: SWR_MEMIF
**Version**: 1.0
**Date**: 2026-03-28

## SWR_MEMIF_00001: MemIf Module Parser
**Description**: The system shall provide a parser for AUTOSAR MemIf module XDM files.

**Priority**: High

**Rationale**: MemIf is the abstraction layer between NvM and hardware drivers.

**Acceptance Criteria**:
- MemIfXdmParser class inherits from AbstractEbModelParser
- parse() method validates MODULE-CONFIGURATION = "MemIf"
- Successfully extracts ARVersion and SwVersion from XDM

**Verification**: Unit tests in test_memif_xdm_parser.py

## SWR_MEMIF_00002: MemIf Init Configuration Parsing
**Description**: The parser shall extract MemIf initialization configuration parameters.

**Priority**: High

**Rationale**: Init configuration controls MemIf behavior and job priorities.

**Acceptance Criteria**:
- Extracts MemIfDevErrorDetect (BOOLEAN)
- Extracts MemIfIndex (INTEGER)
- Extracts MemIfJobPriority (ENUMERATION)
- Extracts MemIfMaxNumberJobs (INTEGER, optional)

**Verification**: Unit test test_read_memif_init()
```

- [ ] **Step 2: Create remaining requirements documents**

Follow the same pattern for Fee, Ea, MemMap, MemAcc.

- [ ] **Step 3: Commit**

```bash
git add docs/requirements/swr_memif.md docs/requirements/swr_fee.md docs/requirements/swr_ea.md docs/requirements/swr_memmap.md docs/requirements/swr_memacc.md
git commit -m "$(cat <<'EOF'
docs: Add Tier 5 module requirements specifications

- Add SWR_MEMIF requirements documentation
- Add SWR_FEE requirements documentation
- Add SWR_EA requirements documentation
- Add SWR_MEMMAP requirements documentation
- Add SWR_MEMACC requirements documentation
EOF
)"
```

---

## Task 9: Update CLAUDE.md with Tier 5 Modules

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Add Tier 5 modules to CLAUDE.md**

```markdown
# Modify CLAUDE.md - Add to the list of currently registered CLI entry points:
- `memif-xdm-xlsx`: MemIf module XDM to Excel conversion
- `fee-xdm-xlsx`: Fee module XDM to Excel conversion
- `ea-xdm-xlsx`: Ea module XDM to Excel conversion
- `memmap-xdm-xlsx`: MemMap module XDM to Excel conversion
- `memacc-xdm-xlsx`: MemAcc module XDM to Excel conversion
```

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "$(cat <<'EOF'
docs: Update CLAUDE.md with Tier 5 module CLI entries

- Add documentation for Tier 5 module commands
- Update CLI entry points list
EOF
)"
```

---

## Task 10: Full Integration Testing

**Files:**
- None (verification only)

- [ ] **Step 1: Run all tests**

Run: `pytest --tb=short -v`

Expected: All tests pass (should include new Tier 5 module tests)

- [ ] **Step 2: Verify linting**

Run: `ruff check src/eb_model/parser/memif_xdm_parser.py src/eb_model/models/memif_xdm.py`

Expected: No linting errors

Repeat for all 5 modules.

- [ ] **Step 3: Verify CI checks**

Run: `ruff check . --select=E9,F63,F7,F82`

Expected: No critical errors

- [ ] **Step 4: Run integration test**

Create a minimal XDM file for one module and test full flow:

```bash
# Create test XDM
cat > /tmp/test_memif.xdm << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<datamodel version="8.0"
    xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
    xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
    xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
    xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
    <d:chc type="AR-ELEMENT" value="MODULE-CONFIGURATION" name="MemIf"/>
    <d:ctr name="MemIfInit" type="IDENTIFIABLE">
        <d:var name="MemIfDevErrorDetect" type="BOOLEAN" value="true"/>
        <d:var name="MemIfIndex" type="INTEGER" value="1"/>
    </d:ctr>
</datamodel>
EOF

# Test CLI
memif-xdm-xlsx /tmp/test_memif.xdm -o /tmp/test_memif.xlsx

# Verify output exists
test -f /tmp/test_memif.xlsx && echo "Integration test PASSED" || echo "Integration test FAILED"
```

- [ ] **Step 5: Final cleanup**

```bash
rm /tmp/test_memif.xdm /tmp/test_memif.xlsx
```

---

## Task 11: Final Verification and Documentation

**Files:**
- None (verification only)

- [ ] **Step 1: Verify all files created**

Run: `git status`

Expected: 25 new files + 2 modified files (eb_doc.py, eb_parser_factory.py, pyproject.toml)

- [ ] **Step 2: Verify test coverage**

Run: `pytest --cov=src/eb_model/parser/memif_xdm_parser.py --cov=src/eb_model/models/memif_xdm.py`

Expected: Reasonable coverage for new modules

- [ ] **Step 3: Final commit summary**

```bash
git log --oneline -n 10
```

Should show commits for all 5 modules with their parsers, models, reporters, CLI, and tests.

- [ ] **Step 4: Prepare PR description**

Document the following for PR:
- Summary of Tier 5 implementation
- Modules added (MemIf, Fee, Ea, MemMap, MemAcc)
- Breaking changes: None
- New CLI commands added
- SWR IDs implemented
- Test coverage summary

---

## Success Criteria

This plan is complete when:

- [ ] All 5 parsers inherit from AbstractEbModelParser
- [ ] All 5 models follow the existing Module pattern
- [ ] All 5 modules registered in EbParserFactory
- [ ] All 5 modules registered in EBModel
- [ ] All 5 CLI entry points work correctly
- [ ] All 5 Excel reporters generate valid output
- [ ] Unit tests pass for all parsers and models
- [ ] Integration tests pass (XDM → Model → Excel)
- [ ] Linting passes with no errors
- [ ] Requirements documentation exists for all modules
- [ ] CLAUDE.md updated with new CLI commands
- [ ] All parsers successfully parse at least one real XDM file from ACG-9_2_0_WIN32X86 (if available)

## Estimated Time

- **Task 1-5** (Parser + Model + Tests): 5 modules × 15 min = ~1.5 hours
- **Task 6** (CLI): 20 min
- **Task 7** (Reporters): 5 modules × 10 min = ~50 min
- **Task 8** (Requirements): 20 min
- **Task 9** (Documentation): 5 min
- **Task 10** (Integration Testing): 20 min
- **Task 11** (Final Verification): 15 min

**Total**: ~3.5 hours

## Risks and Notes

1. **XDM File Availability**: The plan assumes sample XDM files exist. If not available, tests use mocked XML.
2. **Module Complexity**: Some Tier 5 modules (MemMap, MemAcc) may have complex configuration structures. Plan focuses on core features.
3. **Reference Dependencies**: NvM references MemIf, Fee, and Ea. These should be tested with real XDM files if available.
4. **Flash Emulation Details**: Fee module may have sector configuration that's not covered in basic implementation.
5. **Memory Protection**: MemAcc may have protection zone definitions not covered in initial implementation.

## References

- Design spec: `docs/superpowers/specs/2026-03-23-multi-module-xdm-parser-design.md`
- Existing implementation: NvM module (Tier 5 reference)
- AUTOSAR specification: R22-11 (Classic Platform)
- Memory management stack: NvM → MemIf → Fee/Ea → MemMap/MemAcc