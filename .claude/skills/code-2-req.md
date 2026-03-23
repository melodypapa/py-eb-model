---
name: code-2-req
description: Generate formal software requirements specification (SRS) from existing code implementation. Use this when the user wants to: create requirements documentation from code, document existing functionality, extract functional requirements from implementation, create SWR (Software Requirements) documents, reverse-engineer requirements from legacy code, document features that were never specified, or prepare for enterprise code reviews/audits.
compatibility:
  - Read files (Read tool)
  - Search code (Grep tool)
  - Write files (Write tool)
---

# Code to Requirements (code-2-req)

This skill generates formal software requirements specifications from code implementation.

## Quick Start

Choose your scope and provide the feature name:

| Scope | Feature Name | Example Command |
|-------|-------------|-----------------|
| Single module | `os-module`, `rte-module`, `nvm-module`, `ecuc-module`, `bswm-module` | "Generate requirements for OS module" |
| Layer | `parser-layer`, `model-layer`, `reporter-layer` | "Generate requirements for parser layer" |
| System-wide | `overview` | "Generate system overview requirements" |
| Custom feature | `<feature-name>` | "Generate requirements for XML validation" |

Output location: `docs/requirements/swr_[feature].md`

## When to Use

- Creating requirements documentation for existing code
- Documenting features that were never formally specified
- Preparing for enterprise code reviews or audits
- Generating SWR (Software Requirements) documents
- Extracting functional requirements from implementation
- Creating requirements from scratch based on intended implementation

## Not for Use

- Writing implementation code (use TDD skill instead)
- Creating test plans (use test skill instead)
- Code review (use code-review skill instead)
- Refactoring existing code (use simplify skill instead)

## Output

A formal requirements specification in Markdown format, saved to `docs/requirements/swr_[feature].md`.

## Requirements Document Structure

Generate requirements documents with the following sections:

```markdown
# Software Requirements Specification: [Feature Name]

## Document Information

| Field | Value |
|-------|-------|
| Document Title | [Feature Name] Software Requirements Specification |
| Document ID | SWR-[FEATURE]-001 |
| Version | 1.0 |
| Date | YYYY-MM-DD |
| Project | py-eb-model |
| Module | [Module Name] |

## Table of Contents

...

## 1. Introduction

### 1.1 Purpose
Brief statement of the purpose of the feature/system.

### 1.2 Scope
What this feature/system does and doesn't do.

### 1.3 Definitions, Acronyms, and Abbreviations
Define any technical terms, acronyms, or abbreviations used.

### 1.4 References
List of related documents (if any).

## 2. General Description

### 2.1 Product Perspective
Where this feature fits in the overall system architecture.

### 2.2 Product Functions
High-level summary of what the feature does.

### 2.3 User Characteristics
Who uses this feature and their skill level.

### 2.4 Constraints
Technical, regulatory, or other constraints.

### 2.5 Dependencies
What this feature depends on (libraries, external systems, etc.).

## 3. Functional Requirements

```
**REQ-[MODULE]-3.X - [Feature Name]**: The system shall [brief description].
- [Specific action 1]
- [Specific action 2]
- [Specific action 3]

**REQ-[MODULE]-3.Y - [Feature Name]**: The system shall [brief description].
- [Specific action 1]
- [Specific action 2]
- [Specific action 3]
```

**Key Principle**: Each requirement ID represents a complete feature capability with 4-8 specific actions listed as bullet points. Do not create sub-sections for each requirement - use the inline format shown above.

**Requirement ID Format**: `TYPE-[MODULE]-SECTION.NUMBER` where:
- `TYPE` - Requirement type identifier
- `[MODULE]` - Module name abbreviation (e.g., OS, RTE, NVM, ECUC, BSWM)
- `SECTION` - Section number (e.g., 3 for Functional Requirements, 4 for Non-Functional Requirements)
- `NUMBER` - Sequential requirement number within section

**Requirement Types**:
- `REQ-[MODULE]-3.X` - Functional Requirements (section 3)
- `NREQ-[MODULE]-4.X` - Non-Functional Requirements (section 4)

**Examples**:
- `REQ-OS-3.1 - Parser Layer` for OS module functional requirement
- `NREQ-OS-4.1 - Performance` for OS module non-functional requirement

**Simplified Structure**: Only two main requirement sections - Functional Requirements (what the system does) and Non-Functional Requirements (how the system behaves). Other details like interfaces, data requirements, use cases, and test requirements are documented in the General Description and Appendix sections for a cleaner, more focused requirements document.
```

## Execution Process

### Phase 1: Clarify Scope
If the user's request is ambiguous, ask what they want requirements for:
- "Which module/layer/feature needs requirements documentation?"
- Or start with the most logical choice (e.g., if they mentioned OS, generate for os-module)

### Phase 2: Analyze Code
Read files in this order:
1. **Context**: `setup.py`, `CLAUDE.md` (if exists)
2. **Base classes**: `src/eb_model/models/abstract.py`, `src/eb_model/parser/eb_parser.py`
3. **Module model**: `src/eb_model/models/[module].py`
4. **Module parser**: `src/eb_model/parser/[module]_xdm_parser.py`
5. **Reporter/Writer**: `src/eb_model/reporter/[module]_xls_writer.py`
6. **CLI entry**: `src/eb_model/cli/[module]_xdm_2_xls_cli.py`

### Phase 3: Extract Requirements
For each component, extract by asking:

**Models** → What entities/attributes/relationships/validation?
**Parsers** → What inputs/processing/error handling?
**Reporters** → What outputs/formatting/locations?
**CLI** → What commands/arguments/help/errors?

### Phase 4: Write Document
Follow the template below, write to `docs/requirements/swr_[feature].md`

## Requirements Document Template

## Requirement Writing Guidelines

### Use Standard Language

- **SHALL** - Mandatory requirement
- **SHOULD** - Recommended but not mandatory
- **MAY** - Optional feature
- **WILL** - Future commitment

### Be Specific and Verifiable

Bad: "The system shall process files efficiently"
Good: "The system shall parse XDM files up to 10MB in size within 5 seconds"

Bad: "The system shall handle errors"
Good: "The system shall log an error message and exit with non-zero status when the input file is not found"

### Use Requirement IDs

Assign unique IDs to each feature-level requirement for traceability:
- REQ-3.1: First feature requirement in section 3.1
- REQ-3.2: Second feature requirement in section 3.2

**Key Principle**: Group related sub-requirements under a single requirement ID. Each requirement ID represents a complete feature capability with multiple specific actions listed as bullet points. This reduces requirement bloat while maintaining clarity and traceability.

## Requirement Granularity Guidelines

### Core Principles

1. **Feature Completeness** - Each requirement ID represents a complete, coherent feature capability
2. **Testability** - Each requirement can be tested as a unit
3. **Business Value** - Focus on features users care about, not implementation details
4. **Single Responsibility** - Each requirement focuses on one functional area

### Target Metrics

- **4-8 bullet points** per requirement
- **8-15 requirements** for a typical module
- **100% feature coverage**

### When to Group vs. Split

**GROUP TOGETHER** when:
- Same functional capability (e.g., all task parsing attributes)
- Tested as a unit
- Coherent user story
- Implementation detail of same feature

**KEEP SEPARATE** when:
- Different functional areas (tasks vs ISRs)
- Different layers (parser vs reporter vs CLI)
- Independent testability
- Different stakeholders

### Example: Good vs Bad

**BAD - Too Granular:**
```
### 3.2 Task Management
- REQ-3.2.1: Parse task name
- REQ-3.2.2: Parse task priority
- REQ-3.2.3: Parse task activation
...
```

**GOOD - Appropriate Granularity:**
```
**REQ-3.2 - Task Management**: The system shall parse and model OS task definitions.
- Extract name, priority, activation count, schedule type, and stack size
- Extract task type for memory planning
- Parse autostart configuration and resource references
- Provide IsPreemptable() method
- Map tasks to parent applications for O(1) lookup
```

## Determining the Feature Name

When determining the feature name for `swr_[feature].md`:

1. **For module-specific analysis** (e.g., analyzing `src/eb_model/parser/os_xdm_parser.py`):
   - Use the module name: `os-module`, `rte-module`, `nvm-module`, `ecuc-module`, `bswm-module`

2. **For layer-specific analysis** (e.g., analyzing the parser layer):
   - Use the layer name: `parser-layer`, `model-layer`, `reporter-layer`

3. **For new features being documented before implementation**:
   - Use the descriptive feature name provided by the user
   - Convert to lowercase with hyphens (e.g., `xml-validation` → `xml-validation`)

4. **For general system analysis**:
   - Use `overview` for system-wide requirements

Examples:
- `swr_os-module.md` - OS module requirements
- `swr_parser-layer.md` - Parser layer requirements
- `swr_xml-validation.md` - XML validation feature
- `swr_overview.md` - System overview requirements

## Analysis Strategy

### Reading Order for Code Analysis

1. **Setup and context**: `setup.py`, `CLAUDE.md`
2. **Base classes**: `src/eb_model/models/abstract.py`, `src/eb_model/parser/eb_parser.py`
3. **Model definition**: Module-specific model file
4. **Parser implementation**: Module-specific parser file
5. **Reporter/Writer**: Output generation logic
6. **CLI entry point**: User interface

### Analysis Scope

**Full Project Analysis**: Start with setup.py, read CLAUDE.md, explore directory structure, then read each module's parser, model, reporter, and CLI files.

**Single Module Analysis**: Identify module by name (Os, Rte, NvM, EcuC, BswM), then read parser → model → reporter → CLI files.

**New Feature Documentation**: Ask user for feature description, inputs/outputs, constraints/dependencies, then generate requirements.

## Writing Guidelines

### Language Style

- **Be concise but complete** - Include all relevant information without fluff
- **Use present tense** - "The system parses" not "The system will parse"
- **Be consistent** - Use the same terminology throughout
- **Focus on what** not **how** - Describe functionality, not implementation details
- **Include examples** - Show actual command usage and output formats
- **Document limitations** - Be honest about what doesn't work or isn't supported

### Common Code Patterns to Requirements

| Pattern | Code Example | Requirement Statement |
|---------|--------------|----------------------|
| Factory | `EbParserFactory.create(xdm_file)` | "The system shall automatically determine the parser type based on the XDM file's MODULE-CONFIGURATION tag." |
| Singleton | `EBModel.getInstance()` | "The document model shall be implemented as a singleton to ensure single point of truth." |
| Namespace | `self.nsmap = dict([...])` | "The parser shall extract XML namespaces from the XDM file and use them for XPath queries." |
| Fluent Interface | `task.setName("Task1").setPriority(5)` | "Model objects shall support method chaining for convenient configuration." |

## Final Review Checklist

Before saving to `docs/requirements/swr_[feature].md`:

- [ ] **Granularity**: 4-8 bullet points per requirement, 8-15 total for typical module
- [ ] **Structure**: All sections present, requirements numbered and verifiable
- [ ] **Content**: Consistent terminology, technical terms defined
- [ ] **Completeness**: All functionality covered, non-functional requirements included

## Example: Functional Requirements Format

```markdown
**REQ-OS-3.1 - Parser Layer**: The system shall parse EB Tresos XDM files containing OS configuration.
- Extract XML namespace definitions and store in namespace map for XPath queries
- Validate that the datamodel root element module name is "Os" (raise ValueError if not)
- Extract AUTOSAR version and software version from the OS configuration
- Inherit common XML parsing methods from AbstractEbModelParser base class

**REQ-OS-3.2 - Task Management**: The system shall parse and model OS task definitions.
- Extract name, priority, activation count, schedule type, and stack size
- Extract task type for memory planning
- Parse autostart configuration and resource references
- Provide IsPreemptable() method for schedule type checking
- Map tasks to parent applications for O(1) lookup
```