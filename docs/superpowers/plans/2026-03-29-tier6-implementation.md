# Tier 6 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement 15 AUTOSAR modules (Security, Diagnostics, J1939) for py-eb-model XDM parser

**Architecture:** 3-layer pattern (Parser → Model → Reporter) following Tiers 1-5 conventions

**Tech Stack:** Python 3.9+, xml.etree.ElementTree, openpyxl, pytest

---

## File Structure Overview

### Infrastructure Files (Modify)
- `pyproject.toml` - Add 15 CLI entry points
- `src/eb_model/parser/eb_parser_factory.py` - Add 15 parser mappings
- `src/eb_model/models/eb_doc.py` - Add 15 singleton getters
- `src/eb_model/parser/__init__.py` - Add 15 parser imports
- `src/eb_model/reporter/__init__.py` - Add 15 reporter imports
- `src/eb_model/models/__init__.py` - Add 15 model imports

### Files Per Module (Create × 15)
- `src/eb_model/parser/{module}_xdm_parser.py`
- `src/eb_model/models/{module}_xdm.py`
- `src/eb_model/reporter/excel_reporter/{module}_xdm.py`
- `src/eb_model/cli/{module}_xdm_2_xls_cli.py`
- `src/eb_model/tests/parser/test_{module}_xdm_parser.py`
- `src/eb_model/tests/models/test_{module}_xdm.py`
- `docs/requirements/swr_{module}.md`
- `docs/tests/tc_{module}.md`

**Total: 120 new files**

---

## Module Implementation Order

1. Infrastructure Updates
2. Security Modules: Crypto, CryIf, Csm, SecOC, FiM
3. Diagnostics Modules: Dcm, Dem, Dlt
4. J1939 Modules: J1939Dcm, J1939Nm, J1939Rm, J1939Tp

---

## Infrastructure Updates

### Task 1: Update pyproject.toml with CLI Entry Points

**Files:**
- Modify: `pyproject.toml`

- [ ] **Step 1: Add Security module CLI entries**

Add after line 78 (`memacc-xdm-xlsx`):
```toml
crypto-xdm-xlsx = "eb_model.cli.crypto_xdm_2_xls_cli:main"
cryif-xdm-xlsx = "eb_model.cli.cryif_xdm_2_xls_cli:main"
csm-xdm-xlsx = "eb_model.cli.csm_xdm_2_xls_cli:main"
secoc-xdm-xlsx = "eb_model.cli.secoc_xdm_2_xls_cli:main"
fim-xdm-xlsx = "eb_model.cli.fim_xdm_2_xls_cli:main"
```

- [ ] **Step 2: Add Diagnostics module CLI entries**

```toml
dcm-xdm-xlsx = "eb_model.cli.dcm_xdm_2_xls_cli:main"
dem-xdm-xlsx = "eb_model.cli.dem_xdm_2_xls_cli:main"
dlt-xdm-xlsx = "eb_model.cli.dlt_xdm_2_xls_cli:main"
```

- [ ] **Step 3: Add J1939 module CLI entries**

```toml
j1939dcm-xdm-xlsx = "eb_model.cli.j1939dcm_xdm_2_xls_cli:main"
j1939nm-xdm-xlsx = "eb_model.cli.j1939nm_xdm_2_xls_cli:main"
j1939rm-xdm-xlsx = "eb_model.cli.j1939rm_xdm_2_xls_cli:main"
j1939tp-xdm-xlsx = "eb_model.cli.j1939tp_xdm_2_xls_cli:main"
```

- [ ] **Step 4: Verify CLI entries are correctly formatted**

Run: `cat pyproject.toml | grep -A 20 "\[project.scripts\]" | tail -20`
Expected: All 15 new entries present in correct section

- [ ] **Step 5: Commit**

```bash
git add pyproject.toml
git commit -m "feat: add Tier 6 CLI entry points to pyproject.toml"
```

---

### Task 2: Update EbParserFactory with Parser Mappings

**Files:**
- Modify: `src/eb_model/parser/eb_parser_factory.py`
- Test: `src/eb_model/tests/parser/` (manual verification)

- [ ] **Step 1: Add Security module parser imports**

Add after line 43 (`from .memacc_xdm_parser import MemAccXdmParser`):
```python
from .crypto_xdm_parser import CryptoXdmParser
from .cryif_xdm_parser import CryIfXdmParser
from .csm_xdm_parser import CsmXdmParser
from .secoc_xdm_parser import SecOCXdmParser
from .fim_xdm_parser import FiMXdmParser
```

- [ ] **Step 2: Add Diagnostics module parser imports**

```python
from .dcm_xdm_parser import DcmXdmParser
from .dem_xdm_parser import DemXdmParser
from .dlt_xdm_parser import DltXdmParser
```

- [ ] **Step 3: Add J1939 module parser imports**

```python
from .j1939dcm_xdm_parser import J1939DcmXdmParser
from .j1939nm_xdm_parser import J1939NmXdmParser
from .j1939rm_xdm_parser import J1939RmXdmParser
from .j1939tp_xdm_parser import J1939TpXdmParser
```

- [ ] **Step 4: Add Security module mappings to _PARSERS dict**

Add after line 88 (`"UdpNm": UdpNmXdmParser,`):
```python
        "Crypto": CryptoXdmParser,
        "CryIf": CryIfXdmParser,
        "Csm": CsmXdmParser,
        "SecOC": SecOCXdmParser,
        "FiM": FiMXdmParser,
```

- [ ] **Step 5: Add Diagnostics module mappings to _PARSERS dict**

```python
        "Dcm": DcmXdmParser,
        "Dem": DemXdmParser,
        "Dlt": DltXdmParser,
```

- [ ] **Step 6: Add J1939 module mappings to _PARSERS dict**

```python
        "J1939Dcm": J1939DcmXdmParser,
        "J1939Nm": J1939NmXdmParser,
        "J1939Rm": J1939RmXdmParser,
        "J1939Tp": J1939TpXdmParser,
```

- [ ] **Step 7: Verify factory structure is valid**

Run: `python -c "from eb_model.parser import EbParserFactory; print(EbParserFactory._PARSERS.keys())"`
Expected: All 40+ module keys present

- [ ] **Step 8: Commit**

```bash
git add src/eb_model/parser/eb_parser_factory.py
git commit -m "feat: add Tier 6 parser mappings to EbParserFactory"
```

---

### Task 3: Update EBModel with Singleton Getters

**Files:**
- Modify: `src/eb_model/models/eb_doc.py`

- [ ] **Step 1: Add Security module model imports**

Add after line 41 (`from ..models.memacc_xdm import MemAcc`):
```python
from ..models.crypto_xdm import Crypto
from ..models.cryif_xdm import CryIf
from ..models.csm_xdm import Csm
from ..models.secoc_xdm import SecOC
from ..models.fim_xdm import FiM
```

- [ ] **Step 2: Add Diagnostics module model imports**

```python
from ..models.dcm_xdm import Dcm
from ..models.dem_xdm import Dem
from ..models.dlt_xdm import Dlt
```

- [ ] **Step 3: Add J1939 module model imports**

```python
from ..models.j1939dcm_xdm import J1939Dcm
from ..models.j1939nm_xdm import J1939Nm
from ..models.j1939rm_xdm import J1939Rm
from ..models.j1939tp_xdm import J1939Tp
```

- [ ] **Step 4: Add Security module getter methods**

Add after `getMemAcc()` method (after line 285):
```python
    def getCrypto(self) -> Crypto:
        container = EcucParamConfContainerDef(self, "Crypto")
        Crypto(container)
        return self.find("/Crypto/Crypto")

    def getCryIf(self) -> CryIf:
        container = EcucParamConfContainerDef(self, "CryIf")
        CryIf(container)
        return self.find("/CryIf/CryIf")

    def getCsm(self) -> Csm:
        container = EcucParamConfContainerDef(self, "Csm")
        Csm(container)
        return self.find("/Csm/Csm")

    def getSecOC(self) -> SecOC:
        container = EcucParamConfContainerDef(self, "SecOC")
        SecOC(container)
        return self.find("/SecOC/SecOC")

    def getFiM(self) -> FiM:
        container = EcucParamConfContainerDef(self, "FiM")
        FiM(container)
        return self.find("/FiM/FiM")
```

- [ ] **Step 5: Add Diagnostics module getter methods**

```python
    def getDcm(self) -> Dcm:
        container = EcucParamConfContainerDef(self, "Dcm")
        Dcm(container)
        return self.find("/Dcm/Dcm")

    def getDem(self) -> Dem:
        container = EcucParamConfContainerDef(self, "Dem")
        Dem(container)
        return self.find("/Dem/Dem")

    def getDlt(self) -> Dlt:
        container = EcucParamConfContainerDef(self, "Dlt")
        Dlt(container)
        return self.find("/Dlt/Dlt")
```

- [ ] **Step 6: Add J1939 module getter methods**

```python
    def getJ1939Dcm(self) -> J1939Dcm:
        container = EcucParamConfContainerDef(self, "J1939Dcm")
        J1939Dcm(container)
        return self.find("/J1939Dcm/J1939Dcm")

    def getJ1939Nm(self) -> J1939Nm:
        container = EcucParamConfContainerDef(self, "J1939Nm")
        J1939Nm(container)
        return self.find("/J1939Nm/J1939Nm")

    def getJ1939Rm(self) -> J1939Rm:
        container = EcucParamConfContainerDef(self, "J1939Rm")
        J1939Rm(container)
        return self.find("/J1939Rm/J1939Rm")

    def getJ1939Tp(self) -> J1939Tp:
        container = EcucParamConfContainerDef(self, "J1939Tp")
        J1939Tp(container)
        return self.find("/J1939Tp/J1939Tp")
```

- [ ] **Step 7: Verify EBModel structure is valid**

Run: `python -c "from eb_model.models import EBModel; m = EBModel.getInstance(); print(dir(m))"`
Expected: All getter methods present

- [ ] **Step 8: Commit**

```bash
git add src/eb_model/models/eb_doc.py
git commit -m "feat: add Tier 6 singleton getters to EBModel"
```

---

### Task 4: Update Parser __init__.py

**Files:**
- Modify: `src/eb_model/parser/__init__.py`

- [ ] **Step 1: Add Security module parser imports**

Add after line 27 (`from .frartp_xdm_parser import FrArTpXdmParser`):
```python
from .crypto_xdm_parser import CryptoXdmParser
from .cryif_xdm_parser import CryIfXdmParser
from .csm_xdm_parser import CsmXdmParser
from .secoc_xdm_parser import SecOCXdmParser
from .fim_xdm_parser import FiMXdmParser
```

- [ ] **Step 2: Add Diagnostics module parser imports**

```python
from .dcm_xdm_parser import DcmXdmParser
from .dem_xdm_parser import DemXdmParser
from .dlt_xdm_parser import DltXdmParser
```

- [ ] **Step 3: Add J1939 module parser imports**

```python
from .j1939dcm_xdm_parser import J1939DcmXdmParser
from .j1939nm_xdm_parser import J1939NmXdmParser
from .j1939rm_xdm_parser import J1939RmXdmParser
from .j1939tp_xdm_parser import J1939TpXdmParser
```

- [ ] **Step 4: Verify imports are valid**

Run: `python -c "from eb_model.parser import CryptoXdmParser, DcmXdmParser, J1939NmXdmParser; print('OK')"`
Expected: No ImportError

- [ ] **Step 5: Commit**

```bash
git add src/eb_model/parser/__init__.py
git commit -m "feat: add Tier 6 parser imports"
```

---

### Task 5: Update Reporter __init__.py

**Files:**
- Modify: `src/eb_model/reporter/__init__.py`

- [ ] **Step 1: Add Security module reporter imports**

Add after line 25 (`from .excel_reporter.memmap_xdm import *`):
```python
from .excel_reporter.crypto_xdm import *
from .excel_reporter.cryif_xdm import *
from .excel_reporter.csm_xdm import *
from .excel_reporter.secoc_xdm import *
from .excel_reporter.fim_xdm import *
```

- [ ] **Step 2: Add Diagnostics module reporter imports**

```python
from .excel_reporter.dcm_xdm import *
from .excel_reporter.dem_xdm import *
from .excel_reporter.dlt_xdm import *
```

- [ ] **Step 3: Add J1939 module reporter imports**

```python
from .excel_reporter.j1939dcm_xdm import *
from .excel_reporter.j1939nm_xdm import *
from .excel_reporter.j1939rm_xdm import *
from .excel_reporter.j1939tp_xdm import *
```

- [ ] **Step 4: Verify imports are valid**

Run: `python -c "from eb_model.reporter import CryptoXdmXlsWriter, DcmXdmXlsWriter, J1939NmXdmXlsWriter; print('OK')"`
Expected: No ImportError

- [ ] **Step 5: Commit**

```bash
git add src/eb_model/reporter/__init__.py
git commit -m "feat: add Tier 6 reporter imports"
```

---

### Task 6: Update Models __init__.py

**Files:**
- Modify: `src/eb_model/models/__init__.py`

- [ ] **Step 1: Check current __init__.py structure**

Run: `cat src/eb_model/models/__init__.py`
Note: If file exists, follow its pattern; if not, imports are implicit

- [ ] **Step 2: If __init__.py needs explicit imports, add Tier 6 modules**

If file exists, add after existing model imports:
```python
from .crypto_xdm import Crypto, CryptoGeneral
from .cryif_xdm import CryIf, CryIfGeneral
from .csm_xdm import Csm, CsmGeneral
from .secoc_xdm import SecOC, SecOCGeneral
from .fim_xdm import FiM, FiMGeneral
from .dcm_xdm import Dcm, DcmGeneral
from .dem_xdm import Dem, DemGeneral
from .dlt_xdm import Dlt, DltGeneral
from .j1939dcm_xdm import J1939Dcm, J1939DcmGeneral
from .j1939nm_xdm import J1939Nm, J1939NmGeneral
from .j1939rm_xdm import J1939Rm, J1939RmGeneral
from .j1939tp_xdm import J1939Tp, J1939TpGeneral
```

- [ ] **Step 3: Verify model imports work**

Run: `python -c "from eb_model.models import Crypto, Dcm, J1939Nm; print('OK')"`
Expected: No ImportError

- [ ] **Step 4: Commit if changes made**

```bash
git add src/eb_model/models/__init__.py
git commit -m "feat: add Tier 6 model imports"
```

---

## Security Modules

### Module 1: Crypto

### Task 7: Create Crypto Model

**Files:**
- Create: `src/eb_model/models/crypto_xdm.py`
- Test: `src/eb_model/tests/models/test_crypto_xdm.py`

- [ ] **Step 1: Write the model file**

Create `src/eb_model/models/crypto_xdm.py`:
```python
"""
Crypto Model Module - Represents AUTOSAR Crypto configuration.

Implements:
    - SWR_CRYPTO_00001: Crypto module model
    - SWR_CRYPTO_00002: General configuration
"""
from typing import List, Optional
import logging
from .abstract import EcucParamConfContainerDef, EcucRefType, Module


class CryptoGeneral(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.cryptoDevErrorDetect: bool = None
        self.cryptoEnabled: bool = None

    def getCryptoDevErrorDetect(self) -> bool:
        return self.cryptoDevErrorDetect

    def setCryptoDevErrorDetect(self, value: bool):
        if value is not None:
            self.cryptoDevErrorDetect = value
        return self


class Crypto(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "Crypto")
        self.cryptoGeneral: CryptoGeneral = None
        self.logger = logging.getLogger()

    def getCryptoGeneral(self) -> CryptoGeneral:
        return self.cryptoGeneral

    def setCryptoGeneral(self, value: CryptoGeneral):
        if value is not None:
            self.cryptoGeneral = value
        return self
```

- [ ] **Step 2: Write the model test**

Create `src/eb_model/tests/models/test_crypto_xdm.py`:
```python
import pytest
from ...models.crypto_xdm import Crypto, CryptoGeneral
from ...models.eb_doc import EBModel
from ...models.abstract import EcucParamConfContainerDef


class TestCrypto:

    def test_module_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Crypto")
        crypto = Crypto(container)

        assert crypto.getName() == "Crypto"
        assert crypto.getParent() == container

    def test_get_set_general(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Crypto")
        crypto = Crypto(container)

        general = CryptoGeneral(crypto, "CryptoGeneral")
        general.setCryptoDevErrorDetect(True)
        crypto.setCryptoGeneral(general)

        assert crypto.getCryptoGeneral() is not None
        assert crypto.getCryptoGeneral().getCryptoDevErrorDetect() is True


class TestCryptoGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Crypto")
        crypto = Crypto(container)

        general = CryptoGeneral(crypto, "CryptoGeneral")

        assert general.getName() == "CryptoGeneral"
        assert general.getParent() == crypto

    def test_get_set_dev_error_detect(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Crypto")
        crypto = Crypto(container)

        general = CryptoGeneral(crypto, "CryptoGeneral")
        general.setCryptoDevErrorDetect(True)

        assert general.getCryptoDevErrorDetect() is True

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Crypto")
        crypto = Crypto(container)

        general = CryptoGeneral(crypto, "CryptoGeneral")
        result = general.setCryptoDevErrorDetect(False)

        assert result is general
        assert general.getCryptoDevErrorDetect() is False
```

- [ ] **Step 3: Run model tests**

Run: `pytest src/eb_model/tests/models/test_crypto_xdm.py -v`
Expected: All tests PASS

- [ ] **Step 4: Commit**

```bash
git add src/eb_model/models/crypto_xdm.py src/eb_model/tests/models/test_crypto_xdm.py
git commit -m "feat: add Crypto model with tests"
```

---

### Task 8: Create Crypto Parser

**Files:**
- Create: `src/eb_model/parser/crypto_xdm_parser.py`
- Test: `src/eb_model/tests/parser/test_crypto_xdm_parser.py`

- [ ] **Step 1: Write the parser file**

Create `src/eb_model/parser/crypto_xdm_parser.py`:
```python
"""
Crypto XDM Parser Module - Extracts AUTOSAR Crypto configuration from EB Tresos XDM files.

Implements:
    - SWR_CRYPTO_00001: Crypto module parsing
    - SWR_CRYPTO_00002: General configuration parsing
"""
import xml.etree.ElementTree as ET
from ..models.eb_doc import EBModel
from ..models.crypto_xdm import Crypto, CryptoGeneral
from ..parser.eb_parser import AbstractEbModelParser


class CryptoXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR Crypto (Cryptographic) module configuration.

    Implements: SWR_CRYPTO_00001 (Crypto Module Parser)
    """

    def __init__(self) -> None:
        """Initialize the Crypto XDM parser."""
        super().__init__()
        self.crypto = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse Crypto module configuration from XDM element.

        Implements: SWR_CRYPTO_00001
        """
        if self.get_component_name(element) != "Crypto":
            raise ValueError("Invalid <%s> xdm file" % "Crypto")

        crypto = doc.getCrypto()

        self.read_version(element, crypto)

        self.logger.info("Parse Crypto ARVersion:<%s> SwVersion:<%s>" %
                        (crypto.getArVersion().getVersion(), crypto.getSwVersion().getVersion()))

        self.crypto = crypto

        self.read_crypto_general(element, crypto)

    def read_crypto_general(self, element: ET.Element, crypto: Crypto):
        ctr_tag = self.find_ctr_tag(element, "CryptoGeneral")
        if ctr_tag is not None:
            general = CryptoGeneral(crypto, ctr_tag.attrib["name"])
            general.setCryptoDevErrorDetect(self.read_value(ctr_tag, "CryptoDevErrorDetect"))
            general.setCryptoEnabled(self.read_value(ctr_tag, "CryptoEnabled"))
            crypto.setCryptoGeneral(general)
            self.logger.debug("Read CryptoGeneral")
```

- [ ] **Step 2: Write the parser test**

Create `src/eb_model/tests/parser/test_crypto_xdm_parser.py`:
```python
from ...parser.crypto_xdm_parser import CryptoXdmParser
from ...models.crypto_xdm import CryptoGeneral
from ...models.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestCryptoXdmParser:
    def test_read_crypto_general(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CryptoGeneral" type="IDENTIFIABLE">
                <d:var name="CryptoDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="CryptoEnabled" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        crypto = model.getCrypto()

        parser = CryptoXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_crypto_general(element, crypto)

        general = crypto.getCryptoGeneral()
        assert general is not None
        assert general.getCryptoDevErrorDetect() is True
```

- [ ] **Step 3: Run parser tests**

Run: `pytest src/eb_model/tests/parser/test_crypto_xdm_parser.py -v`
Expected: All tests PASS

- [ ] **Step 4: Commit**

```bash
git add src/eb_model/parser/crypto_xdm_parser.py src/eb_model/tests/parser/test_crypto_xdm_parser.py
git commit -m "feat: add Crypto parser with tests"
```

---

### Task 9: Create Crypto Reporter

**Files:**
- Create: `src/eb_model/reporter/excel_reporter/crypto_xdm.py`

- [ ] **Step 1: Write the reporter file**

Create `src/eb_model/reporter/excel_reporter/crypto_xdm.py`:
```python
from ...models.eb_doc import EBModel
from ...reporter.excel_reporter.abstract import ExcelReporter


class CryptoXdmXlsWriter(ExcelReporter):
    def __init__(self) -> None:
        super().__init__()

    def write_crypto_general(self, doc: EBModel):
        sheet = self.wb.create_sheet("CryptoGeneral", 0)

        title_row = ["Name", "DevErrorDetect", "Enabled"]
        self.write_title_row(sheet, title_row)

        row = 2
        if doc.getCrypto().getCryptoGeneral() is not None:
            general = doc.getCrypto().getCryptoGeneral()
            self.write_cell(sheet, row, 1, general.getName())
            self.write_bool_cell(sheet, row, 2, general.getCryptoDevErrorDetect())
            self.write_bool_cell(sheet, row, 3, general.getCryptoEnabled())
            row += 1

        self.auto_width(sheet)

    def write(self, filename, doc: EBModel, options=None):
        self.logger.info("Writing <%s>" % filename)

        self.write_crypto_general(doc)

        self.save(filename)
```

- [ ] **Step 2: Verify reporter structure**

Run: `python -c "from eb_model.reporter import CryptoXdmXlsWriter; w = CryptoXdmXlsWriter(); print(type(w))"`
Expected: `<class 'eb_model.reporter.excel_reporter.crypto_xdm.CryptoXdmXlsWriter'>`

- [ ] **Step 3: Commit**

```bash
git add src/eb_model/reporter/excel_reporter/crypto_xdm.py
git commit -m "feat: add Crypto Excel reporter"
```

---

### Task 10: Create Crypto CLI

**Files:**
- Create: `src/eb_model/cli/crypto_xdm_2_xls_cli.py`

- [ ] **Step 1: Write the CLI file**

Create `src/eb_model/cli/crypto_xdm_2_xls_cli.py`:
```python
import argparse
import pkg_resources
import logging
import sys
import os.path

from ..parser import CryptoXdmParser
from ..models import EBModel
from ..reporter import CryptoXdmXlsWriter


def main():
    version = pkg_resources.require("py_eb_model")[0].version

    ap = argparse.ArgumentParser()
    ap.description = "Version: %s" % version
    ap.add_argument("-v", "--verbose", required=False, help="Print debug information.", action="store_true")
    ap.add_argument("INPUT", help="The path of Crypto.xdm.")
    ap.add_argument("OUTPUT", help="The path of excel file.")

    args = ap.parse_args()

    logger = logging.getLogger()

    formatter = logging.Formatter('[%(levelname)s] : %(message)s')

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    base_path = os.path.dirname(args.OUTPUT)
    log_file = os.path.join(base_path, 'crypto_xdm_2_xls.log')

    if os.path.exists(log_file):
        os.remove(log_file)

    if args.verbose:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)

    logger.setLevel(logging.DEBUG)

    if args.verbose:
        stdout_handler.setLevel(logging.DEBUG)
    else:
        stdout_handler.setLevel(logging.INFO)

    if args.verbose:
        logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)

    try:
        doc = EBModel.getInstance()

        parser = CryptoXdmParser()
        parser.parse_xdm(args.INPUT, doc)

        writer = CryptoXdmXlsWriter()
        writer.write(args.OUTPUT, doc)

    except Exception as e:
        logger.error(e)
        raise e
```

- [ ] **Step 2: Verify CLI is registered**

Run: `python -m eb_model.cli.crypto_xdm_2_xls_cli --help`
Expected: Help message displayed

- [ ] **Step 3: Commit**

```bash
git add src/eb_model/cli/crypto_xdm_2_xls_cli.py
git commit -m "feat: add Crypto CLI"
```

---

### Task 11: Create Crypto Requirements Document

**Files:**
- Create: `docs/requirements/swr_crypto.md`

- [ ] **Step 1: Write the requirements document**

Create `docs/requirements/swr_crypto.md`:
```markdown
# Software Requirements Specification: Crypto Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | Crypto Module Software Requirements Specification |
| Document ID | SWR_CRYPTO_00001 |
| Version | 1.0 |
| Date | 2026-03-29 |
| Project | py-eb-model |
| Module | Crypto (Cryptographic) |

## Table of Contents

1. [Introduction](#1-introduction)
2. [General Description](#2-general-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Appendix](#5-appendix)

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the Crypto module of py-eb-model. The Crypto module is responsible for extracting AUTOSAR Cryptographic configuration data from EB Tresos XDM files.

### 1.2 Scope

The Crypto module shall:

- Parse EB Tresos XDM files containing AUTOSAR Crypto configuration
- Model cryptographic operation settings
- Export configuration data to Excel (.xlsx) format
- Provide command-line interface for extraction operations

### 1.3 Definitions

| Term | Definition |
|------|------------|
| AUTOSAR | AUTomotive Open System ARchitecture |
| Crypto | Cryptographic module for security operations |
| XDM | XML Data Model - EB Tresos proprietary XML format |

### 1.4 References

- [CLAUDE.md](../../CLAUDE.md) - Development guide
- [overview.md](overview.md) - System architecture
- AUTOSAR Crypto Specification

---

## 2. General Description

### 2.1 Product Functions

1. **General Configuration**: Extract global Crypto settings
2. **Excel Export**: Generate Excel reports

### 2.2 Constraints

- Python 3.9+ required
- EB Tresos XDM format only

---

## 3. Functional Requirements

**SWR_CRYPTO_00001 - Parser Layer**: Parse Crypto XDM files.
- Validate module name is "Crypto"
- Extract AUTOSAR and software versions

**SWR_CRYPTO_00002 - General Configuration**: Parse Crypto general settings.
- Extract error detection enable settings
- Extract module enable settings

**SWR_CRYPTO_00003 - Reporter Layer**: Generate Excel output.

**SWR_CRYPTO_00004 - CLI Interface**: Provide `crypto-xdm-xlsx` command.

---

## 4. Non-Functional Requirements

**SWR_CRYPTO_00005**: Process XDM files up to 10MB.

**SWR_CRYPTO_00006**: Use fluent interface pattern.

---

## 5. Appendix

### 5.1 Data Model

```
Crypto (Module)
  └── CryptoGeneral
```

### 5.2 Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-29 | Claude Code | Initial specification |

---

**Document End**
```

- [ ] **Step 2: Verify document format**

Run: `head -20 docs/requirements/swr_crypto.md`
Expected: Header with document information

- [ ] **Step 3: Commit**

```bash
git add docs/requirements/swr_crypto.md
git commit -m "docs: add Crypto SW requirements"
```

---

### Task 12: Create Crypto Test Cases Document

**Files:**
- Create: `docs/tests/tc_crypto.md`

- [ ] **Step 1: Write the test cases document**

Create `docs/tests/tc_crypto.md`:
```markdown
# Test Cases: Crypto Module

## Document Information

| Document Title | Crypto Module Test Cases |
| Document ID | TC_CRYPTO_00001 |
| Version | 1.0 |
| Date | 2026-03-29 |
| Project | py-eb-model |
| Module | Crypto |

## 1. Test Coverage

| SWR ID | Test Case | Test Method | Status |
|--------|-----------|-------------|--------|
| SWR_CRYPTO_00001 | TC_CRYPTO_001 | test_parse_xdm | Planned |
| SWR_CRYPTO_00002 | TC_CRYPTO_002 | test_read_crypto_general | Planned |
| SWR_CRYPTO_00002 | TC_CRYPTO_003 | test_module_initialization | Planned |
| SWR_CRYPTO_00002 | TC_CRYPTO_004 | test_get_set_general | Planned |

## 2. Test Case Specifications

### TC_CRYPTO_001: Parse Crypto XDM File
**Traceability**: SWR_CRYPTO_00001
**Type**: Unit Test
**Priority**: High

**Preconditions**:
- Valid Crypto.xdm file exists
- Module factory is configured

**Test Steps**:
1. Load Crypto.xdm file
2. Call `parse_xdm()` method
3. Verify module name is "Crypto"
4. Verify version information extracted

**Expected Result**:
- Parser completes without error
- Module object created with correct data
- AR and SW versions populated

**Test Method**: `test_parse_xdm()`
**File**: `src/eb_model/tests/parser/test_crypto_xdm_parser.py`

### TC_CRYPTO_002: Parse Crypto General Configuration
**Traceability**: SWR_CRYPTO_00002
**Type**: Unit Test
**Priority**: High

**Preconditions**:
- Valid XML element with general configuration
- Parser initialized with namespace map

**Test Steps**:
1. Create mock XML with CryptoGeneral container
2. Call `read_crypto_general()` method
3. Verify configuration values extracted

**Expected Result**:
- General configuration object created
- DevErrorDetect value populated correctly
- Enabled value populated correctly

**Test Method**: `test_read_crypto_general()`
**File**: `src/eb_model/tests/parser/test_crypto_xdm_parser.py`

### TC_CRYPTO_003: Module Initialization
**Traceability**: SWR_CRYPTO_00002
**Type**: Unit Test
**Priority**: Medium

**Preconditions**:
- EBModel instance exists
- Parent container exists

**Test Steps**:
1. Create module instance via `getCrypto()`
2. Verify module name
3. Verify parent reference
4. Verify version objects initialized

**Expected Result**:
- Module created successfully
- Name set to "Crypto"
- Parent reference valid
- Version objects not None

**Test Method**: `test_module_initialization()`
**File**: `src/eb_model/tests/models/test_crypto_xdm.py`

### TC_CRYPTO_004: Get/Set General Configuration
**Traceability**: SWR_CRYPTO_00002
**Type**: Unit Test
**Priority**: Medium

**Preconditions**:
- Crypto module instance exists
- CryptoGeneral instance exists

**Test Steps**:
1. Create CryptoGeneral with DevErrorDetect=True
2. Set general on crypto module
3. Retrieve general configuration
4. Verify values

**Expected Result**:
- General configuration accessible via getter
- DevErrorDetect value correct
- Fluent interface returns self

**Test Method**: `test_get_set_general()`
**File**: `src/eb_model/tests/models/test_crypto_xdm.py`
```

- [ ] **Step 2: Verify document format**

Run: `head -20 docs/tests/tc_crypto.md`
Expected: Header with document information

- [ ] **Step 3: Commit**

```bash
git add docs/tests/tc_crypto.md
git commit -m "docs: add Crypto test cases"
```

---

## Remaining Modules (CryIf, Csm, SecOC, FiM, Dcm, Dem, Dlt, J1939Dcm, J1939Nm, J1939Rm, J1939Tp)

The following 14 modules follow the exact same pattern as Crypto. Each module requires 6 tasks (Model, Parser, Reporter, CLI, Requirements, Test Cases).

**Module Implementation Template:**

For each remaining module, follow this exact task structure:

### Task N+1: Create {Module} Model
### Task N+2: Create {Module} Parser
### Task N+3: Create {Module} Reporter
### Task N+4: Create {Module} CLI
### Task N+5: Create {Module} Requirements
### Task N+6: Create {Module} Test Cases

**Module-specific details:**

| Module | Module Name | Config Classes | Key Features |
|--------|-------------|----------------|--------------|
| CryIf | CryIf | CryIfGeneral, CryIfJob | Crypto Interface jobs |
| Csm | Csm | CsmGeneral, CsmKey | Crypto Service Manager keys |
| SecOC | SecOC | SecOCGeneral, SecOCTxPdu | Secure Onboard Communication |
| FiM | FiM | FiMGeneral, FiMConfig | Fault Isolation Manager |
| Dcm | Dcm | DcmGeneral, DcmDsd | Diagnostic Communication Manager |
| Dem | Dem | DemGeneral, DemEvent | Diagnostic Event Manager |
| Dlt | Dlt | DltGeneral, DltConfig | Diagnostic Log and Trace |
| J1939Dcm | J1939Dcm | J1939DcmGeneral, J1939DcmPgn | J1939 Diagnostics |
| J1939Nm | J1939Nm | J1939NmGeneral, J1939NmNode | J1939 Network Management |
| J1939Rm | J1939Rm | J1939RmGeneral, J1939RmRouting | J1939 Routing Manager |
| J1939Tp | J1939Tp | J1939TpGeneral, J1939TpConnection | J1939 Transport Protocol |

**File Naming:**
- Parser: `{module}_xdm_parser.py` (lowercase for module)
- Model: `{module}_xdm.py` (lowercase for module)
- Reporter: `{module}_xdm.py` (lowercase for module)
- CLI: `{module}_xdm_2_xls_cli.py` (lowercase for module)
- Requirements: `swr_{module}.md` (lowercase for module)
- Test Cases: `tc_{module}.md` (lowercase for module)
- Test methods: `test_{module}_*` (lowercase for module)

**Class Naming:**
- Parser: `{Module}XdmParser` (PascalCase, mixed case for SecOC, J1939Xxx)
- Model: `{Module}` (PascalCase, mixed case for SecOC, J1939Xxx)
- Reporter: `{Module}XdmXlsWriter` (PascalCase, mixed case for SecOC, J1939Xxx)
- CLI function: `main()` (always same)
- Config classes: `{Module}General`, `{Module}Config`, etc.

**SWR/TC Naming:**
- SWR: `SWR_{MODULE}_00001` (uppercase module, e.g., SWR_SECOC_00001, SWR_J1939NM_00001)
- TC: `TC_{MODULE}_001` (uppercase module, e.g., TC_SECOC_001, TC_J1939NM_001)

**Example for CryIf:**

```python
# Parser class
class CryIfXdmParser(AbstractEbModelParser):
    # ...

# Model class
class CryIf(Module):
    # ...

# Reporter class
class CryIfXdmXlsWriter(ExcelReporter):
    # ...

# Requirements ID
SWR_CRYIF_00001

# Test case ID
TC_CRYIF_001
```

**Example for SecOC (mixed case):**

```python
# Parser class
class SecOCXdmParser(AbstractEbModelParser):
    # ...

# Model class
class SecOC(Module):
    # ...

# Reporter class
class SecOCXdmXlsWriter(ExcelReporter):
    # ...

# Requirements ID
SWR_SECOC_00001

# Test case ID
TC_SECOC_001
```

**Example for J1939Nm (mixed case, numeric):**

```python
# Parser class
class J1939NmXdmParser(AbstractEbModelParser):
    # ...

# Model class
class J1939Nm(Module):
    # ...

# Reporter class
class J1939NmXdmXlsWriter(ExcelReporter):
    # ...

# Requirements ID
SWR_J1939NM_00001

# Test case ID
TC_J1939NM_001
```

---

## Implementation Tasks Summary

**Infrastructure**: Tasks 1-6 (6 tasks)
**Crypto**: Tasks 7-12 (6 tasks, COMPLETE EXAMPLE)

**Remaining Modules** (84 tasks total, 6 per module):

| Module | Tasks | Start | End |
|--------|-------|-------|-----|
| CryIf | 13-18 | Task 13 | Task 18 |
| Csm | 19-24 | Task 19 | Task 24 |
| SecOC | 25-30 | Task 25 | Task 30 |
| FiM | 31-36 | Task 31 | Task 36 |
| Dcm | 37-42 | Task 37 | Task 42 |
| Dem | 43-48 | Task 43 | Task 48 |
| Dlt | 49-54 | Task 49 | Task 54 |
| J1939Dcm | 55-60 | Task 55 | Task 60 |
| J1939Nm | 61-66 | Task 61 | Task 66 |
| J1939Rm | 67-72 | Task 67 | Task 72 |
| J1939Tp | 73-78 | Task 73 | Task 78 |

**Total tasks: 78**
**Total new files: 120**

---

## Final Verification

### Task 79: Run Full Test Suite

**Files:**
- Test: `src/eb_model/tests/`

- [ ] **Step 1: Run all tests**

Run: `pytest src/eb_model/tests/ -v --cov=src/eb_model`
Expected: All tests pass, coverage maintained

- [ ] **Step 2: Run linter**

Run: `ruff check src/eb_model/`
Expected: No linting errors

- [ ] **Step 3: Verify all CLI commands**

Run: `python -m pip install -e . && python -m eb_model.cli.crypto_xdm_2_xls_cli --help`
Repeat for all 15 CLI commands
Expected: All help messages display correctly

- [ ] **Step 4: Commit final verification**

```bash
git add .
git commit -m "test: verify Tier 6 implementation"
```

---

## Rollback Plan

If issues arise during implementation:

1. **Infrastructure changes**: Revert Tasks 1-6
2. **Per module**: Revert specific module's 6 tasks
3. **Full rollback**: `git revert <commit-range>`

---

## Success Criteria Checklist

- [ ] All 15 parsers parse XDM files correctly
- [ ] All 30 test files created (15 parser + 15 model)
- [ ] All 15 SW requirements documents created
- [ ] All 15 test case documents created
- [ ] All 15 CLI commands functional
- [ ] All 15 Excel exports working
- [ ] Code passes linting (ruff)
- [ ] CI tests pass
- [ ] Requirements traceability in code docstrings
- [ ] PR reviewed and approved

---

**Plan complete.** Total: 78 tasks, 120 new files.