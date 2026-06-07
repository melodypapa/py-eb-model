# Core Concepts

## What is EB Tresos XDM?

EB Tresos (Elektrobit Tresos) is an AUTOSAR configuration tool. It exports configuration in XDM (XML Data Model) format - a proprietary XML schema representing AUTOSAR module configurations.

**Example XDM structure:**
```xml
<MODULE-CONFIGURATION>
  <d:ctr name="OsGeneral">
    <d:var name="OsStatus" type="BOOLEAN" value="true"/>
  </d:ctr>
  <d:lst name="OsTask">
    <d:ctr name="Task1">
      <d:var name="Priority" type="INTEGER" value="5"/>
    </d:ctr>
  </d:lst>
</MODULE-CONFIGURATION>
```

## Architecture Overview

py-eb-model has three layers:

### 1. Parser Layer (`src/eb_model/parser/`)

**Purpose**: Convert XDM XML to Python objects

**Key components:**
- `AbstractEbModelParser`: Base parser with common XML parsing methods
- `OsXdmParser`, `CanIfXdmParser`, etc.: Module-specific parsers
- `EbParserFactory`: Auto-detects module type from XDM

**How it works:**
1. Read XDM file with ElementTree
2. Extract namespace information
3. Parse MODULE-CONFIGURATION tag
4. Walk XML tree, extract values
5. Create model objects

### 2. Model Layer (`src/eb_model/models/`)

**Purpose**: Represent AUTOSAR domain as Python objects

**Key components:**
- `EcucObject`: Base class for all configuration objects
- `Module`: Root container (e.g., `Os`, `CanIf`)
- `OsTask`, `CanIfRxPduCfg`, etc.: Specific configuration objects

**Features:**
- Hierarchical naming (e.g., `Os/Task1`)
- Fluent interface for chaining
- Type-safe accessors

### 3. Reporter Layer (`src/eb_model/reporter/`)

**Purpose**: Export model objects to various formats

**Key components:**
- `AbstractEbModelXlsWriter`: Base Excel writer
- `OsXdmXlsWriter`, `CanIfXdmXlsWriter`, etc.: Module-specific writers
- `ExcelReporter`: Utility class for formatting

**How it works:**
1. Receive model object
2. Create Excel workbook
3. Write sheets for each configuration container
4. Save to file

## Module Mapping

py-eb-model supports 50+ AUTOSAR modules organized by stack:

| Stack | Modules |
|-------|---------|
| **Core** | Os, EcuC, RTE, BswM, Det, EcuM, PbcfgM, Tm |
| **CAN** | CanIf, CanNm, CanSM, CanTp |
| **Ethernet** | EthIf, EthSM, SoAd, TcpIp, SomeIpTp, UdpNm, DoIP |
| **LIN** | LinIf, LinSM, LinTp |
| **FlexRay** | FrIf, FrNm, FrSM, FrTp, FrArTp |
| **COM** | Com, LdCom, ComM, PduR, IpduM, Nm |
| **Memory** | NvM, Fee, Ea, MemIf, MemAcc, MemMap, Crc |
| **Crypto** | Crypto, CryIf, Csm, SecOC |
| **Diagnostic** | Dcm, Dem, DLT, FiM |
| **J1939** | J1939Dcm, J1939Nm, J1939Rm, J1939Tp |

## CLI vs Python API

### CLI (Recommended for most users)

```bash
eb-convert Os.xdm output/
```

**When to use:**
- Converting files
- Batch processing
- Quick data extraction
- No custom logic needed

### Python API

```python
from eb_model.parser import OsXdmParser
from eb_model.reporter import OsXdmXlsWriter

parser = OsXdmParser()
os_model = parser.parse("Os.xdm")
writer = OsXdmXlsWriter()
writer.write(os_model, "Os.xlsx")
```

**When to use:**
- Custom data processing
- Integrating into tools
- Validation scripts
- Generating multiple outputs

## Next Steps

- Try [converting your first XDM](first-xdm.md)
- Learn about the [generator](generator-quickstart.md)
- See [CLI usage](../usage/cli.md)