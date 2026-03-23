---
name: code-2-req
description: Generate formal software requirements specification (SRS) from existing code implementation. **Use this whenever** the user wants to: create requirements documentation from code, document existing functionality, extract functional requirements from implementation, create SWR (Software Requirements) documents, reverse-engineer requirements from legacy code, document features that were never specified, prepare for enterprise code reviews/audits, generate requirement specs for inherited codebases, or create formal requirements before implementing new features. This is essential for legacy systems, audit preparation, and any situation where code exists without formal requirements. **Even if the user doesn't explicitly say "requirements"**, if they mention documenting, spec-ing out, or explaining what existing code does, this skill likely applies.
compatibility:
  - Read files (Read tool)
  - Search code (Grep tool)
  - Write files (Write tool)
---

# Code to Requirements (code-2-req)

This skill generates formal software requirements specifications by analyzing code implementation.

## Quick Start

1. **Determine scope**: What module, feature, or system needs requirements?
2. **Analyze code**: Read relevant source files to understand functionality
3. **Extract requirements**: Identify functional capabilities, inputs/outputs, constraints
4. **Write document**: Output to `docs/requirements/swr_[feature].md`

**Output format**: Markdown requirements spec saved to `docs/requirements/swr_[feature].md`

## When to Use

- Creating requirements documentation for existing code
- Documenting features that were never formally specified
- Preparing for enterprise code reviews or audits
- Generating SWR (Software Requirements) documents
- Extracting functional requirements from implementation
- Creating requirements from scratch based on intended implementation
- Reverse-engineering requirements from legacy/inherited code

## Not for Use

- Writing implementation code (use TDD skill instead)
- Creating test plans (use test skill instead)
- Code review (use code-review skill instead)
- Refactoring existing code (use simplify skill instead)

## Document Template

Use this exact structure for every requirements document:

```markdown
# Software Requirements Specification: [Feature Name]

## Document Information

| Field | Value |
|-------|-------|
| Document Title | [Feature Name] Software Requirements Specification |
| Document ID | SWR-[FEATURE]-001 |
| Version | 1.0 |
| Date | YYYY-MM-DD |
| Project | [Project Name] |
| Module | [Module Name] |

## Table of Contents

- [1. Introduction](#1-introduction)
  - [1.1 Purpose](#11-purpose)
  - [1.2 Scope](#12-scope)
  - [1.3 Definitions, Acronyms, and Abbreviations](#13-definitions-acronyms-and-abbreviations)
  - [1.4 References](#14-references)
- [2. General Description](#2-general-description)
  - [2.1 Product Perspective](#21-product-perspective)
  - [2.2 Product Functions](#22-product-functions)
  - [2.3 User Characteristics](#23-user-characteristics)
  - [2.4 Constraints](#24-constraints)
  - [2.5 Dependencies](#25-dependencies)
- [3. Functional Requirements](#3-functional-requirements)
- [4. Non-Functional Requirements](#4-non-functional-requirements)
- [Appendix A: Interface Specifications](#appendix-a-interface-specifications)
- [Appendix B: Data Requirements](#appendix-b-data-requirements)

## 1. Introduction

### 1.1 Purpose
Brief statement of what this feature/system does and why it exists.

### 1.2 Scope
What this feature/system does and doesn't do. Include boundaries and limitations.

### 1.3 Definitions, Acronyms, and Abbreviations
Define technical terms used throughout the document. Example:
- **XDM**: EB Tresos XML Data Model format
- **ASPath**: AUTOSAR path reference format

### 1.4 References
List related documents (API docs, design specs, standards).

## 2. General Description

### 2.1 Product Perspective
Where this feature fits in the overall system architecture. Mention relationships to other components.

### 2.2 Product Functions
High-level summary of main capabilities. 3-5 bullet points.

### 2.3 User Characteristics
Who uses this feature and their skill level (e.g., "AUTOSAR engineers familiar with EB Tresos").

### 2.4 Constraints
Technical, regulatory, or business constraints:
- File format limitations
- Platform dependencies
- Performance requirements
- Security considerations

### 2.5 Dependencies
External systems, libraries, or services this feature depends on.

## 3. Functional Requirements

[Use the inline format below - no sub-sections for each requirement]

**REQ-[MODULE]-3.1 - [Feature Name]**: The system shall [brief description].
- [Specific action 1]
- [Specific action 2]
- [Specific action 3]
- [Specific action 4]
- [Specific action 5]

**REQ-[MODULE]-3.2 - [Feature Name]**: The system shall [brief description].
- [Specific action 1]
- [Specific action 2]
- [Specific action 3]
- [Specific action 4]
- [Specific action 5]

## 4. Non-Functional Requirements

**NREQ-[MODULE]-4.1 - [Category]**: The system shall [performance/quality requirement].
- [Specific requirement 1]
- [Specific requirement 2]
- [Specific requirement 3]

## Appendix A: Interface Specifications

Document external interfaces (APIs, file formats, protocols) if not covered in main requirements.

## Appendix B: Data Requirements

Document data structures, schemas, or entity relationships if not covered in main requirements.
```

## Requirement ID Format

`TYPE-[MODULE]-SECTION.NUMBER` where:

- **TYPE**: `REQ` (functional) or `NREQ` (non-functional)
- **MODULE**: Component/feature abbreviation (e.g., OS, PARSER, AUTH)
- **SECTION**: 3 (functional) or 4 (non-functional)
- **NUMBER**: Sequential within section

Examples:
- `REQ-PARSER-3.1` - Parser layer functional requirement
- `NREQ-OS-4.1` - OS module non-functional requirement

## Requirement Writing Guidelines

### Language Standards

| Term | Meaning | When to Use |
|------|---------|-------------|
| **SHALL** | Mandatory requirement | Core functionality |
| **SHOULD** | Recommended | Best practices, optional features |
| **MAY** | Optional | Nice-to-have capabilities |
| **WILL** | Future commitment | Planned features |

### Be Specific and Verifiable

Bad: "The system shall process files efficiently"
Good: "The system shall parse XML files up to 10MB within 5 seconds"

Bad: "The system shall handle errors gracefully"
Good: "The system shall log error details and exit with non-zero status when input file validation fails"

### Granularity Rules

**Each requirement ID should represent a complete feature capability with 4-8 bullet points.**

- **Target**: 8-15 requirements total for typical modules
- **Group related actions** under one requirement ID
- **Focus on business value**, not implementation details

**GROUP together** when:
- Same functional capability
- Tested as a unit
- Coherent user story

**KEEP SEPARATE** when:
- Different functional areas
- Independent testability
- Different stakeholders

### Example: Good vs Bad

**BAD - Too granular:**
```
### 3.2 Tasks
- REQ-3.2.1: Parse task name
- REQ-3.2.2: Parse task priority
- REQ-3.2.3: Parse task activation
```

**GOOD - Appropriate:**
```
**REQ-OS-3.2 - Task Management**: The system shall parse and model task definitions.
- Extract name, priority, activation count, schedule type, and stack size
- Extract task type for memory planning
- Parse autostart configuration and resource references
- Provide IsPreemptable() method for schedule checking
- Map tasks to parent applications for O(1) lookup
```

## Analysis Process

### 1. Understand Scope
If ambiguous, clarify: "Which module/layer/feature needs requirements?"

### 2. Read Code
Read files in logical order:
- **Context**: Setup files, project docs
- **Base classes**: Abstract implementations, interfaces
- **Core logic**: Main implementation files
- **Outputs**: Writers, reporters, formatters
- **Interfaces**: CLI, API endpoints

### 3. Extract Requirements
For each component, ask:

**Models** → What entities/attributes/relationships/validation exist?
**Parsers/Processors** → What inputs/processing/error handling?
**Outputs** → What formats/locations/transformations?
**Interfaces** → What commands/arguments/behaviors?

### 4. Infer Non-Functional Requirements
From code patterns, identify:
- **Performance**: File sizes, batch processing, timeouts
- **Reliability**: Error handling, logging, validation
- **Security**: Input sanitization, safe parsing
- **Maintainability**: Code structure, test coverage

## Code Patterns to Requirements Mapping

| Pattern | Code Example | Requirement Statement |
|---------|--------------|----------------------|
| Factory | `Factory.create(input)` | "The system shall automatically determine the implementation type based on input characteristics" |
| Singleton | `Instance.getInstance()` | "The model shall be implemented as a singleton to ensure single point of truth" |
| Namespace handling | `self.nsmap = dict([...])` | "The parser shall extract namespaces and use them for queries" |
| Fluent interface | `obj.setX().setY()` | "Objects shall support method chaining for configuration" |
| Validation | `if not condition: raise Error` | "The system shall validate [condition] and raise [error] when invalid" |

## Determining the Feature Name

| Analysis Type | Feature Name Format | Example |
|--------------|---------------------|---------|
| Single module | `<module>-module` | `os-module`, `auth-module` |
| Layer | `<layer>-layer` | `parser-layer`, `api-layer` |
| Feature | `<feature-name>` | `xml-validation`, `user-auth` |
| System-wide | `overview` | `swr_overview.md` |

## Final Checklist

Before saving to `docs/requirements/swr_[feature].md`:

- [ ] **Granularity**: 4-8 bullet points per requirement, 8-15 total
- [ ] **Structure**: All template sections present
- [ ] **IDs**: Consistent requirement ID format
- [ ] **Language**: SHALL/SHOULD/MAY used correctly
- [ ] **Verifiability**: Each requirement testable
- [ ] **Completeness**: Non-functional requirements included
- [ ] **Definitions**: Technical terms defined in Section 1.3

## Example: Complete Requirement Entry

```markdown
**REQ-PARSER-3.1 - XML Parsing**: The system shall parse XML files with namespace support.
- Extract and store namespace definitions from the XML root element
- Use namespace prefixes in XPath queries to locate elements correctly
- Inherit common parsing methods from base parser class
- Raise ValueError with descriptive message when file format is invalid
- Support both absolute and relative XPath expressions
```