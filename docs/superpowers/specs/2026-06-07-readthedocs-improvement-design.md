# ReadTheDocs Documentation Improvement Design

**Date:** 2026-06-07
**Author:** melodypapa
**Status:** Draft

## Overview

Comprehensive documentation overhaul for py-eb-model ReadTheDocs site. Target audience: AUTOSAR engineers using EB Tresos XDM files.

**Current State:**
- Sphinx setup exists with RTD theme
- index.rst outdated (v1.0.0, Python 3.8)
- Broken toctree links (requirements/index, testing/index don't exist)
- getting-started/ empty
- testing/ empty
- New generator feature undocumented

**Goal:** Complete, navigable documentation for AUTOSAR engineers

## Phase Structure

### Phase 1: Fix Foundation (Day 1-2)

**Objective:** Make existing docs navigable and accurate

**Tasks:**

1. **Create missing index files**
   - `docs/requirements/index.rst` - Navigate to SWR documents
   - `docs/testing/index.rst` - Navigate to test specifications

2. **Update version information**
   - Fix index.rst: version 1.0.0 → 1.3.1
   - Fix Python requirement: 3.8 → 3.9+
   - Add dynamic version from `__version__`

3. **Verify navigation**
   - Test all toctree links
   - Fix broken references

**Deliverables:**
- Working documentation navigation
- Accurate version information

---

### Phase 2: Getting Started (Day 3-6)

**Objective:** Onboard AUTOSAR engineers new to the tool

**File Structure:**
```
docs/getting-started/
├── index.rst           # Navigation hub
├── installation.md     # Setup guide
├── first-xdm.md        # First conversion walkthrough
└── concepts.md         # Architecture concepts
```

**Content Specifications:**

#### installation.md
- Requirements (Python 3.9+, dependencies)
- Installation methods (pip, development)
- Verification steps
- Troubleshooting

#### first-xdm.md
- Scenario: Convert first OS XDM
- Step-by-step walkthrough
  - Obtain XDM file
  - Run conversion
  - Understand Excel output
  - Verify key data
- Common issues (ENABLE attributes, namespaces, empty outputs)

#### concepts.md
- What is EB Tresos XDM?
- Architecture overview
  - Parser layer: XML → Python objects
  - Model layer: Domain objects
  - Reporter layer: Objects → Excel
- Module mapping (which AUTOSAR modules supported)
- When to use CLI vs Python API

**Deliverables:**
- Complete getting-started section
- New user onboarding path

---

### Phase 3: Generator Documentation (Day 7-10)

**Objective:** Complete user-facing docs for new model-xdm-generator feature

**File Structure:**
```
docs/
├── getting-started/
│   └── generator-quickstart.md   # 5-minute intro
├── usage/
│   └── model-xdm-generator.md    # Full user manual
├── examples/
│   ├── generator-basic.py        # Simple usage
│   ├── generator-advanced.py     # Combined strategies
│   └── sample-xdm-output.xlsx    # Example output
└── api/
    └── generator.rst             # Auto-generated API
```

**Content Specifications:**

#### generator-quickstart.md
- What is XDM model generator?
- Install + verify
- Generate basic OS model
- Generate with custom schema
- Next steps

#### model-xdm-generator.md
- Introduction
  - Purpose and use cases
  - When to use vs real XDM files
- CLI reference
  - All options explained
  - Example commands
- Strategy patterns
  - RandomStrategy
  - CombinedStrategy
  - When to use each
- Schema guide
  - XDM schema structure
  - Creating custom schemas
  - Common schema patterns
- Examples
  - OS model generation
  - CAN stack generation
  - Custom module generation
- Troubleshooting

#### examples/
- Working Python code samples
- Real XDM schemas
- Example outputs

**Deliverables:**
- Complete generator documentation
- Code examples
- API reference

---

### Phase 4: Complete Reference (Ongoing)

**Objective:** Fill remaining gaps incrementally

**File Structure:**
```
docs/
├── api/
│   ├── parser.rst               # Parser layer docs
│   ├── models.rst               # Model layer docs
│   └── reporters.rst            # Reporter layer docs
├── examples/
│   ├── cli-usage.md             # CLI examples
│   ├── python-api.md            # API usage examples
│   └── batch-processing.md      # Bulk conversions
└── usage/
    └── python-api.md             # Python API guide
```

**Approach:** Document by stack priority (core → CAN → ETH → LIN → FR → MEM → DIAG)

**Deliverables:**
- Complete API reference
- Usage examples
- Python API guide

---

## Technical Implementation

### Tools
- Sphinx (existing)
- sphinx_rtd_theme (existing)
- myst_parser for markdown support (existing)
- sphinx.ext.autodoc for API docs (existing)

### File Conventions
- Markdown for user-facing content (.md)
- RST for API reference (.rst)
- Code examples in `examples/`

### Review Process
- Build docs locally: `cd docs && make html`
- Test navigation
- Verify ReadTheDocs build

## Success Criteria

1. All toctree links work
2. Version information accurate
3. Getting-started guides new users
4. Generator docs comprehensive
5. API reference complete for documented modules

## Timeline

- Phase 1: Day 1-2
- Phase 2: Day 3-6
- Phase 3: Day 7-10
- Phase 4: Ongoing
