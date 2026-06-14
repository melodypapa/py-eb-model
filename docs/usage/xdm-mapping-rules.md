# Schema XDM to Model XDM Mapping Rules

Reference for developers maintaining the `DataGenerator` (`src/eb_model/generator/data_generator.py`).

Source: EB Tresos Studio Developer's Guide, section 5.2 "Concepts: Mapping AUTOSAR ECU Configuration to XDM" (`doc/2.4_Studio_documentation_developers_guide.md`).

## Overview

The XDM format uses two parallel tree structures:

- **Schema Tree** (`v:` prefix) — ECU Parameter Definition (ECU-PD). Defines structure, types, defaults, ranges. Metadata only.
- **Data Tree** (`d:` prefix) — ECU Configuration Description (ECU-CD). Contains actual configuration values.

Every data-node references one schema-node via the `DEF` attribute (see [DEF Attribute Linkage](#def-attribute-linkage)). Multiple data-trees may reference the same schema-tree because the schema only holds meta-information.

## Node Type Mapping

### Schema-Nodes (`v:`) → Data-Nodes (`d:`)

Verified against section 5.2.1.1 (Schema-Nodes) and 5.2.1.14 (Data-Nodes).

| Schema Node (`v:`) | Data Node (`d:`) | Notes |
|--------------------|------------------|-------|
| `v:ctr` type="MODULE-DEF" | `d:ctr` type="MODULE-CONFIGURATION" | Module configuration container |
| `v:ctr` type="IDENTIFIABLE" | `d:ctr` type="IDENTIFIABLE" | Parameter configuration container |
| `v:ctr` type="MULTIPLE-CONFIGURATION-CONTAINER" | `d:ctr` wrapped in `d:lst` | Always wrapped in list |
| `v:ctr` type="INSTANCE" | `d:ctr` type="INSTANCE" | Instance reference (TARGET + CONTEXT) |
| `v:var` type="BOOLEAN" | `d:var` type="BOOLEAN" | Boolean parameter |
| `v:var` type="INTEGER" | `d:var` type="INTEGER" | Integer parameter |
| `v:var` type="FLOAT" | `d:var` type="FLOAT" | Float parameter |
| `v:var` type="STRING" | `d:var` type="STRING" | String parameter |
| `v:var` type="ENUMERATION" | `d:var` type="ENUMERATION" | Enumeration parameter |
| `v:var` type="FUNCTION-NAME" | `d:var` type="FUNCTION-NAME" | Function name parameter |
| `v:var` type="LINKER-SYMBOL" | `d:var` type="LINKER-SYMBOL" | Linker symbol parameter |
| `v:var` (with `DERIVED=true`) | `d:var` (with `DERIVED=true`) | Derived parameter — value computed |
| `v:lst` type="MAP" | `d:lst` type="MAP" | List of named entries |
| `v:chc` | `d:chc` | Choice container |
| `v:ref` type="REFERENCE" | `d:ref` type="REFERENCE" | Reference value |
| `v:ref` type="FOREIGN-REFERENCE" | `d:ref` type="FOREIGN-REFERENCE" | Foreign reference |
| `v:ref` type="SYMBOLIC-NAME-REFERENCE" | `d:ref` type="SYMBOLIC-NAME-REFERENCE" | Symbolic name reference |
| `v:ref` type="CHOICE-REFERENCE" | `d:ref` type="CHOICE-REFERENCE" | Choice reference |
| `v:ref` type="URI-REFERENCE" | `d:ref` type="URI-REFERENCE" | URI reference |

**Rules:**
- `AR-PACKAGE` schema-node has no corresponding data-node — it appears in both trees with the same tag.
- `ECU-CONFIGURATION` data-node has no corresponding schema-node.
- Tag name changes from `v:` to `d:` prefix; attributes (`name`, `type`, `value`) carry over.

## List Handling

Verified against section 5.2.5 (List-Nodes).

**Rule**: Any element with `LOWER-MULTIPLICITY != 1` or `UPPER-MULTIPLICITY != 1` is wrapped in a list-node. The list gets the SHORT-NAME of the ECU Parameter Definition-node.

**Schema** (with multiplicity):
```xml
<v:lst name="OsTask" type="MAP">
  <v:ctr name="OsTask" type="IDENTIFIABLE"/>
</v:lst>
```

**Data** (multiple entries):
```xml
<d:lst name="OsTask" type="MAP">
  <d:ctr name="OsTask_0" type="IDENTIFIABLE">...</d:ctr>
  <d:ctr name="OsTask_1" type="IDENTIFIABLE">...</d:ctr>
</d:lst>
```

**Entry naming** (from `data_generator.py:157`):
- If schema defines `NAME_PATTERN`: use pattern with `?` replaced by index
- Otherwise: `<childName>_<index>` (e.g., `OsTask_0`, `OsTask_1`)

**Multiplicity from schema attributes**:
- `a:da name="MIN"` — minimum entries
- `a:da name="MAX"` — maximum entries (absent = unbounded)

**XPath access** (within data-tree):
- `topDef/OsTask` — selects the list
- `topDef/OsTask/*[1]` — selects first container
- `topDef/OsTask/*[1]/Priority` — selects field within first container

## Optional Elements

Verified against section 5.2.5.1 (Optional elements).

**Definition**: `LOWER-MULTIPLICITY == 0` AND `UPPER-MULTIPLICITY == 1`.

### Old Representation (not recommended)

Wraps optional element in a list with MIN=0, MAX=1:
```xml
<v:lst name="MyOptional" type="MAP">
  <a:da name="MIN" value="0"/>
  <a:da name="MAX" value="1"/>
  <v:ctr name="MyOptional"/>
</v:lst>
```

### New Representation (recommended)

Marks element as optional without wrapping:
```xml
<v:var name="myOptional" type="BOOLEAN">
  <a:a name="OPTIONAL" value="true"/>
  <a:da name="ENABLE" value="false"/>
</v:var>
```

**ENABLE attribute** controls whether the element is active:
- `ENABLE="false"` — element inactive (default in schema)
- `ENABLE="true"` — element active (set by configuration or generator)

The `CombinedStrategy` in the generator adds `<a:a name="ENABLE" value="true"/>` to activate optional elements.

## Choice Nodes

Verified against section 5.2.6 (Choice-Nodes) and 5.2.1.14.4 (Choices data-node).

A choice-data-node always exists in the data-tree. Its `value` attribute holds the SHORT-NAME of the selected container.

### AUTOSAR 2.x

```xml
<!-- Schema -->
<v:chc name="OsAlarmAction">
  <v:ctr name="OsAlarmActivateTask"/>
  <v:ctr name="OsAlarmSetEvent"/>
</v:chc>

<!-- Data -->
<d:chc name="OsAlarmAction" type="CHOICE" value="OsAlarmActivateTask">
  <d:ctr name="OsAlarmActivateTask" type="IDENTIFIABLE">...</d:ctr>
  <d:ctr name="OsAlarmSetEvent" type="IDENTIFIABLE">...</d:ctr>
</d:chc>
```

### AUTOSAR 3.x+

```xml
<!-- Schema -->
<v:chc name="OsAlarmAction" type="IDENTIFIABLE">
  <v:ctr name="OsAlarmActivateTask"/>
  <v:ctr name="OsAlarmSetEvent"/>
</v:chc>

<!-- Data -->
<d:chc name="OsAlarmAction" type="IDENTIFIABLE" value="OsAlarmActivateTask">
  <d:ctr name="OsAlarmActivateTask" type="IDENTIFIABLE">...</d:ctr>
</d:chc>
```

**XPath access**: `topDef/OsAlarmAction` returns the **selected container** (e.g., `OsAlarmActivateTask`), not the choice-node itself.

**Generator behavior** (`data_generator.py:199-218`):
- Non-combined strategies: emit first choice, set `value` to first choice name
- `CombinedStrategy`: emit all choices (each as separate `d:chc` element), each with its own `value`

## Reference Values

Verified against section 5.2.7 (References) and 5.1.9 (Path addressing).

### Schema Definition

References define their target via data attributes:
```xml
<v:ref name="OsAlarmCounterRef" type="REFERENCE">
  <a:da name="REF" value="ASPathDataOfSchema:/AUTOSAR/EcucDefs/Os/OsCounter"/>
  <a:da name="REF-TYPE" value="ASPath"/>
</v:ref>
```

### Data Value

Data references hold the resolved path in the `value` attribute:
```xml
<d:ref name="OsAlarmCounterRef" type="REFERENCE" value="ASPath:/Os/OsCounter/OsCounter_0"/>
```

### Addressing Schemes (section 5.1.9)

| Scheme | Description |
|--------|-------------|
| `ASPath:` | AUTOSAR path expression (e.g., `ASPath:/Os/OsTask`) |
| `ASPathDataOfSchema:` | All data-nodes bound to schema node at AUTOSAR path |
| `ASPathParentNode:` | Parent of node at AUTOSAR path |
| `XPath:` | Generic XPath path |
| `XPathDataOfSchema:` | All data-nodes bound to schema node at XPath |
| `ASTyped:` | Reference by type (e.g., `ASTyped:SwAddrMethod`) |
| `SchemaViaParent:` | Schema-child by name from parent's schema |
| `SchemaViaParentByIdx:` | Schema-child by index from parent's schema |

**Generator behavior**: Extracts target from schema `REF` attribute, strips `ASPathDataOfSchema:` prefix, rewrites as `ASPath:` pointing to a mock target (e.g., `ASPath:/Os/OsCounter`).

## DEF Attribute Linkage

Verified against section 5.1.9 and 5.2.3 (XPath-addressing of ECU-CD using ECU-PD).

Every data-node may carry a `DEF` attribute linking to its schema-node:

```xml
<d:ctr name="myCtr">
  <a:a name="DEF" value="ASPath:/myPkg/myModuleDef/myCtr"/>
</d:ctr>
```

Or with XPath addressing:
```xml
<a:a name="DEF" value="XPath:/AUTOSAR/TOP-LEVEL-PACKAGES/myPkg/ELEMENTS/myModuleDef/myCtr"/>
```

**Note**: The generator does not emit `DEF` attributes — they are optional. Schema linkage is implicit via tree structure (same position + same SHORT-NAME).

## Top-Level Structure

Verified against section 5.2.4 (Top level Structure).

Fixed wrapper hierarchy for all generated model XDM files:

```
datamodel (version attribute)
└── d:ctr type="AUTOSAR" factory="autosar"
    └── d:lst type="TOP-LEVEL-PACKAGES"
        └── d:ctr name="<ModuleName>" type="AR-PACKAGE"
            └── d:lst type="ELEMENTS"
                └── d:chc name="<ModuleName>" type="AR-ELEMENT" value="MODULE-CONFIGURATION"
                    └── d:ctr type="MODULE-CONFIGURATION"
                        └── ... module configuration content ...
```

**XPath shortcuts** (section 5.2.4):
- `/AUTOSAR/TOP-LEVEL-PACKAGES/<pkg>` — select package by name
- `/AUTOSAR/TOP-LEVEL-PACKAGES/*/ELEMENTS/<module>` — select module regardless of package
- `ASPath:/<pkg>/<module>` — select module in specific package
- `as:modconf(<module>)` — select module configuration by name

## Namespaces

| Prefix | URI | Purpose |
|--------|-----|---------|
| (default) | `http://www.tresos.de/_projects/DataModel2/16/root.xsd` | Root schema |
| `a:` | `http://www.tresos.de/_projects/DataModel2/16/attribute.xsd` | Attributes (ENABLE, DEF, DERIVED, etc.) |
| `v:` | `http://www.tresos.de/_projects/DataModel2/06/schema.xsd` | Schema definition nodes |
| `d:` | `http://www.tresos.de/_projects/DataModel2/06/data.xsd` | Data configuration nodes |

**Note**: Schema XDM files may use namespace version `08` instead of `16` (e.g., `DataModel2/08/root.xsd`). The generator reads namespaces dynamically from the input file.

## See Also

- [Model XDM Generator User Manual](model-xdm-generator.md)
- [XDM Model Generator Design](../superpowers/specs/2026-06-06-xdm-model-generator-design.md)
- [Core Concepts](../getting-started/concepts.md)
- EB Tresos Studio Developer's Guide section 5.2 (`doc/2.4_Studio_documentation_developers_guide.md`)
