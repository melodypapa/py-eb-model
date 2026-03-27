# Test Case Template (ISO/IEC/IEEE 29119-3 Compliant)

This template follows the ISO/IEC/IEEE 29119-3 software testing standard for test case documentation.

---

# Test Case: TC_<TYPE>_<MODULE>_<NUMBER>

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_<TYPE>_<MODULE>_<NUMBER> |
| Title | [Brief descriptive title of what the test verifies] |
| Version | 1.0 |
| Date | YYYY-MM-DD |
| Author | [Author Name] |
| Test Type | Unit / Integration / System |
| Priority | High / Medium / Low |

## Purpose/Objective

[Clear statement of what the test case verifies and why it is needed. This should explain:
- What functionality is being tested
- Why this test is important
- What scenarios/conditions are covered]

## Preconditions

| # | Description |
|---|-------------|
| 1 | [Required system state before test execution] |
| 2 | [Required data/configuration files] |
| 3 | [Required dependencies or services] |
| N | [Additional preconditions as needed] |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| [Element 1] | [Value or description of test input] | [Why this data is needed] |
| [Element 2] | [Value or description of test input] | [Why this data is needed] |
| [Element N] | [Value or description of test input] | [Why this data is needed] |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | [Action to perform - specific and unambiguous] | [Expected result of this step] |
| 2 | [Action to perform - specific and unambiguous] | [Expected result of this step] |
| 3 | [Action to perform - specific and unambiguous] | [Expected result of this step] |
| N | [Action to perform - specific and unambiguous] | [Expected result of this step] |

## Expected Results

[Detailed description of expected outcomes, including:
- Successful completion criteria
- Specific data values or states
- Error handling expectations
- Performance requirements if applicable]

## Post-conditions

| # | Description |
|---|-------------|
| 1 | [System state after test execution] |
| 2 | [Data created/modified during test] |
| 3 | [Cleanup or restoration required] |
| N | [Additional post-conditions as needed] |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_<MODULE>_<NUMBER> | [Requirement title/description from requirements doc] | Covered |
| SWR_<MODULE>_<NUMBER> | [Requirement title/description from requirements doc] | Covered |
| SWR_<MODULE>_<NUMBER> | [Requirement title/description from requirements doc] | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | [Path to requirement document, e.g., ../requirements/swr_os-module.md] |
| Design Document | [Path to design document if applicable] |
| Related Test Cases | [List of related test case IDs] |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | YYYY-MM-DD | [Name] | Initial test case creation |
| 1.1 | YYYY-MM-DD | [Name] | [Description of changes] |

---

## Template Usage Instructions

### Filling Out the Template

1. **Test Case ID**: Replace `TC_<TYPE>_<MODULE>_<NUMBER>` with the actual test case ID
   - TYPE: UNIT or INT
   - MODULE: Uppercase module identifier (OS, RTE, NVM, etc.)
   - NUMBER: 5-digit sequential number

2. **Title**: Write a concise, descriptive title (max 100 characters)

3. **Purpose/Objective**: Explain what and why - 2-4 sentences typically

4. **Preconditions**: List all conditions that must be true before test execution

5. **Test Data**: Specify all inputs needed for the test

6. **Test Steps**: Number each step with clear action and expected result

7. **Expected Results**: Describe success criteria comprehensively

8. **Post-conditions**: Document state after test execution

9. **Requirements Coverage**: Reference all SWR IDs covered by this test case

10. **References**: Link to requirement documents and related artifacts

### Guidelines

- Be specific and unambiguous in all descriptions
- Use present tense for test steps (e.g., "Click OK button" not "Clicked OK button")
- Include both positive and negative test scenarios where applicable
- Ensure traceability to requirements is complete
- Update change history when making modifications
- Keep test case descriptions focused on WHAT to test, not HOW to implement

### ISO/IEC/IEEE 29119-3 Reference

This template is based on:
- ISO/IEC/IEEE 29119-3:2013 - Software and systems engineering — Software testing — Part 3: Test documentation
- Section 6.2: Test case specification