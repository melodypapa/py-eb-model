# Test Case: TC_UNIT_REPORTER_00005

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00005 |
| Title | Reporter Layer - Markdown Output |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | Medium |

## Purpose/Objective

Verify that the reporter layer correctly generates Markdown formatted output for OS application data.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | OS application model objects are available |
| 3 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Output File Path | "test_output/OsApp_report.md" | Markdown output file |
| Application Name | "App1" | Application identifier |
| Application Description | "Safety Application" | Application description |
| Mapped Tasks | List of task names | Tasks mapped to application |
| Mapped ISRs | List of ISR names | ISRs mapped to application |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create OsApplicationMarkdownWriter instance | Writer initialized successfully |
| 2 | Generate Markdown output for application | Markdown file created |
| 3 | Verify output file exists | File created at specified path |
| 4 | Verify Markdown structure | File has valid Markdown format |
| 5 | Verify application header | Application name in heading |
| 6 | Verify application description | Description formatted correctly |
| 7 | Verify task list | Tasks listed with correct formatting |
| 8 | Verify ISR list | ISRs listed with correct formatting |
| 9 | Verify table formatting | Tables use correct Markdown syntax |
| 10 | Verify file can be rendered | Markdown renders correctly in viewer |

## Expected Results

- Markdown file is created successfully
- File has valid Markdown structure
- Application data is formatted correctly
- Tables use correct Markdown syntax
- File renders correctly in Markdown viewers
- All application information is included

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Markdown file exists at output path |
| 2 | File can be opened and read |
| 3 | No side effects from generation |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00005 | Reporter Layer - Markdown output | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/os_application_markdown_writer.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |