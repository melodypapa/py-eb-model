# OS Module Unit Test Cases

This document contains all unit test cases for the OS module following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_UNIT_OS_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00001 |
| Title | OS Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly extracts XML namespace definitions from EB Tresos XDM files, validates the module name, extracts AUTOSAR/software version information, and properly initializes the parser. This test ensures the foundation for all subsequent OS configuration parsing.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed and accessible |
| 2 | Test XDM file (valid Os.xdm) is available at known location |
| 3 | No other parsing operations are in progress |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/Os_valid.xdm` | Valid OS XDM file for testing |
| Module Name | "Os" | Expected root module name |
| AUTOSAR Version | "4.3.0" | Example AUTOSAR version |
| Software Version | "1.2.3" | Example software version |
| Namespace Prefix | "d" | Default namespace prefix |
| Namespace URI | "http://www.tresos.de/_projects/DataModel2/06/data.xsd" | Data namespace URI |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create OsXdmParser instance | Parser initialized successfully |
| 2 | Call parse_xdm() with valid Os.xdm file | File parses without errors |
| 3 | Verify namespace map is populated | nsmap contains namespace definitions |
| 4 | Verify module name validation | Module "Os" is accepted, others raise ValueError |
| 5 | Extract AUTOSAR version | Returns correct AUTOSAR version string |
| 6 | Extract software version | Returns correct software version string |
| 7 | Attempt parsing non-OS XDM file | Raises ValueError with descriptive message |

## Expected Results

- Namespace map contains at least 3 namespace definitions
- Module name "Os" is validated successfully
- AUTOSAR version matches expected value from file
- Software version matches expected value from file
- Parsing non-OS file raises ValueError with message "Invalid module name"
- Parsing completes within 2 seconds for 5MB file

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No temporary files created during test |
| 2 | Parser instance can be garbage collected |
| 3 | System returns to pre-test state |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00001 | Parser Layer - XDM file parsing and validation | Covered |
| SWR_OS_00012 | Non-Functional - Efficient processing of 10MB files | Covered |
| SWR_OS_00020 | Non-Functional - Inherit from AbstractEbModelParser | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Design Document | ../requirements/overview.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_OS_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00002 |
| Title | OS Model - Task Attribute Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly extracts all task attributes from XDM configuration containers, creates OsTask model objects, and establishes proper parent-child relationships. This test ensures task data is accurately modeled and accessible.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing OsTask containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Task Name | "Task1" | Example task identifier |
| Task Priority | 5 | Task priority value |
| Task Activation | 1 | Number of activations |
| Schedule Type | "FULL" | Preemptive/Non-preemptive scheduling |
| Stack Size | 1024 | Stack size in bytes |
| Autostart | true | Task auto-start flag |
| Application Reference | "App1" | Application mapping reference |
| Task Attributes List | All 15+ task attributes | Verify complete attribute extraction |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with OsTask container | OsTask object created successfully |
| 2 | Verify task name extraction | getName() returns "Task1" |
| 3 | Verify task priority extraction | getPriority() returns 5 |
| 4 | Verify task activation extraction | getActivation() returns 1 |
| 5 | Verify schedule type extraction | getScheduleType() returns "FULL" |
| 6 | Verify stack size extraction | getStackSize() returns 1024 |
| 7 | Verify autostart flag extraction | isAutostart() returns true |
| 8 | Verify application reference extraction | getApplication() returns "App1" |
| 9 | Verify parent-child relationship | Task's parent is OS module |
| 10 | Verify O(1) lookup performance | Task retrieval by name is constant time |

## Expected Results

- All task attributes are extracted correctly
- Task object is properly registered with parent module
- Parent-child relationship is established
- Task lookup by name is O(1) using dictionary
- Task full name includes parent hierarchy

## Post-conditions

| # | Description |
|---|-------------|
| 1 | OsTask objects remain in memory for verification |
| 2 | EBModel contains updated task collection |
| 3 | No orphaned task objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00002 | Task Management - Task attribute extraction and modeling | Covered |
| SWR_OS_00014 | Non-Functional - O(1) lookup performance using dictionary | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_OS_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00003 |
| Title | OS Model - ISR Attribute Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly extracts ISR (Interrupt Service Routine) attributes from XDM configuration containers, creates OsIsr model objects, and handles hardware-specific attributes for different processor types (TriCore, ARM, etc.).

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing OsIsr containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| ISR Name | "Isr1" | Example ISR identifier |
| ISR Category | 2 | ISR category (1=ISR1, 2=ISR2, etc.) |
| ISR Priority | 10 | ISR priority value |
| Interrupt Vector | 0x42 | Hardware interrupt vector |
| Stack Size | 512 | Stack size in bytes |
| Processor Type | "Tricore" | Hardware-specific attributes |
| Hardware Attributes | TriCore/ARM-specific fields | Verify hardware-specific extraction |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with OsIsr container (TriCore) | OsIsr object created successfully |
| 2 | Verify ISR name extraction | getName() returns "Isr1" |
| 3 | Verify ISR category extraction | getCategory() returns 2 |
| 4 | Verify ISR priority extraction | getPriority() returns 10 |
| 5 | Verify interrupt vector extraction | getInterruptVector() returns 0x42 |
| 6 | Verify stack size extraction | getStackSize() returns 512 |
| 7 | Verify TriCore-specific attributes | Hardware attributes extracted correctly |
| 8 | Parse XML fragment with OsIsr container (ARM) | OsIsr object created successfully |
| 9 | Verify ARM-specific attributes | ARM-specific attributes extracted correctly |
| 10 | Verify parent-child relationship | ISR's parent is OS module |

## Expected Results

- All ISR attributes are extracted correctly
- Hardware-specific attributes are handled based on processor type
- ISR object is properly registered with parent module
- Both TriCore and ARM configurations are supported
- ISR category mapping is correct (1=ISR1, 2=ISR2, etc.)

## Post-conditions

| # | Description |
|---|-------------|
| 1 | OsIsr objects remain in memory for verification |
| 2 | EBModel contains updated ISR collection |
| 3 | No orphaned ISR objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00003 | ISR Management - ISR attribute extraction and hardware-specific handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_OS_00004

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00004 |
| Title | OS Model - Schedule Table Parsing |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly extracts schedule table configurations from XDM containers, including table attributes and expiry points with their actions.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing OsScheduleTable containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Schedule Table Name | "Schedule1" | Example schedule table identifier |
| Duration | 100 | Schedule table duration in ticks |
| Repeating | true | Table repeats cyclically |
| Counter Reference | "Counter1" | Associated counter reference |
| Expiry Point Offset | 0 | First expiry point offset |
| Expiry Point Action | "ACTIVATE_TASK" | Action type (ActivateTask, SetEvent, etc.) |
| Action Target | "Task1" | Target task/event for action |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with OsScheduleTable container | OsScheduleTable object created successfully |
| 2 | Verify schedule table name extraction | getName() returns "Schedule1" |
| 3 | Verify duration extraction | getDuration() returns 100 |
| 4 | Verify repeating flag extraction | isRepeating() returns true |
| 5 | Verify counter reference extraction | getCounter() returns "Counter1" |
| 6 | Verify expiry point extraction | Expiry points list is populated |
| 7 | Verify expiry point offset | First expiry point offset is 0 |
| 8 | Verify expiry point action | Action type is "ACTIVATE_TASK" |
| 9 | Verify expiry point target | Target is "Task1" |
| 10 | Verify expiry point sorting | Expiry points are sorted by offset |

## Expected Results

- Schedule table attributes are extracted correctly
- All expiry points are extracted and maintained
- Expiry point actions are correctly mapped
- Expiry points are sorted by offset value
- Counter reference is correctly resolved

## Post-conditions

| # | Description |
|---|-------------|
| 1 | OsScheduleTable objects remain in memory for verification |
| 2 | EBModel contains updated schedule table collection |
| 3 | No orphaned expiry points exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00004 | Schedule Tables - Schedule table and expiry point extraction | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_OS_00005

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00005 |
| Title | OS Model - Counter Configuration Parsing |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly extracts counter configurations from XDM containers, including counter limits, cycle times, and driver references.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing OsCounter containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Counter Name | "Counter1" | Example counter identifier |
| Max Allowed Value | 65535 | Maximum counter value |
| Min Cycle | 1 | Minimum cycle in ticks |
| Ticks Per Base | 1000 | Ticks per base counter |
| Counter Type | "SOFTWARE" | Counter type (Software/Hardware) |
| Driver Reference | "GptChannel1" | Hardware driver reference |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with OsCounter container | OsCounter object created successfully |
| 2 | Verify counter name extraction | getName() returns "Counter1" |
| 3 | Verify max allowed value extraction | getMaxAllowedValue() returns 65535 |
| 4 | Verify min cycle extraction | getMinCycle() returns 1 |
| 5 | Verify ticks per base extraction | getTicksPerBase() returns 1000 |
| 6 | Verify counter type extraction | getCounterType() returns "SOFTWARE" |
| 7 | Verify driver reference extraction | getDriver() returns "GptChannel1" |
| 8 | Verify parent-child relationship | Counter's parent is OS module |
| 9 | Handle software counter (no driver) | Driver reference is null for software counters |
| 10 | Handle hardware counter | Driver reference is populated for hardware counters |

## Expected Results

- All counter attributes are extracted correctly
- Software counters have null driver reference
- Hardware counters have valid driver reference
- Counter limits are correctly validated
- Counter is properly registered with parent module

## Post-conditions

| # | Description |
|---|-------------|
| 1 | OsCounter objects remain in memory for verification |
| 2 | EBModel contains updated counter collection |
| 3 | No orphaned counter objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00005 | Counters - Counter configuration parsing including driver references | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_OS_00006

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00006 |
| Title | OS Model - Application Mapping |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly extracts application configurations from XDM containers and establishes mapping relationships between applications and their associated tasks and ISRs.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing OsApplication containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Application Name | "App1" | Example application identifier |
| Application Description | "Safety Application" | Application description |
| Application ID | 1 | Application identifier |
| Mapped Task | "Task1" | Task mapped to application |
| Mapped ISR | "Isr1" | ISR mapped to application |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with OsApplication container | OsApplication object created successfully |
| 2 | Verify application name extraction | getName() returns "App1" |
| 3 | Verify application description extraction | getDescription() returns "Safety Application" |
| 4 | Verify application ID extraction | getApplicationId() returns 1 |
| 5 | Verify task-to-application mapping | Task1 maps to App1 |
| 6 | Verify ISR-to-application mapping | Isr1 maps to App1 |
| 7 | Verify application-to-tasks lookup | getTasks() returns list of mapped tasks |
| 8 | Verify application-to-ISRs lookup | getIsrs() returns list of mapped ISRs |
| 9 | Verify bidirectional reference | Task's getApplication() returns App1 |
| 10 | Verify bidirectional reference | ISR's getApplication() returns App1 |

## Expected Results

- All application attributes are extracted correctly
- Task-to-application mappings are established bidirectionally
- ISR-to-application mappings are established bidirectionally
- Application lookup returns correct associated entities
- No orphaned mappings exist

## Post-conditions

| # | Description |
|---|-------------|
| 1 | OsApplication objects remain in memory for verification |
| 2 | EBModel contains updated application collection |
| 3 | Task and ISR objects have valid application references |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00006 | Applications - Application mapping and task/ISR lookup | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_OS_00007

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00007 |
| Title | OS Model - Alarm Action Parsing |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly extracts alarm configurations from XDM containers, including alarm attributes and action definitions with their targets.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing OsAlarm containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Alarm Name | "Alarm1" | Example alarm identifier |
| Alarm Action | "ACTIVATE_TASK" | Action type (ActivateTask, SetEvent, Callback, etc.) |
| Action Target | "Task1" | Target task/event for action |
| Cycle | 100 | Alarm cycle time in ticks |
| Counter Reference | "Counter1" | Associated counter reference |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with OsAlarm container | OsAlarm object created successfully |
| 2 | Verify alarm name extraction | getName() returns "Alarm1" |
| 3 | Verify alarm action extraction | getAction() returns "ACTIVATE_TASK" |
| 4 | Verify action target extraction | getActionTarget() returns "Task1" |
| 5 | Verify cycle extraction | getCycle() returns 100 |
| 6 | Verify counter reference extraction | getCounter() returns "Counter1" |
| 7 | Validate action type | Action is one of valid types (ActivateTask, SetEvent, Callback, IncrementCounter) |
| 8 | Validate target reference | Target reference resolves to valid object |
| 9 | Verify parent-child relationship | Alarm's parent is OS module |

## Expected Results

- All alarm attributes are extracted correctly
- Action type is validated against supported types
- Target reference is correctly resolved
- Counter reference is correctly resolved
- Alarm is properly registered with parent module

## Post-conditions

| # | Description |
|---|-------------|
| 1 | OsAlarm objects remain in memory for verification |
| 2 | EBModel contains updated alarm collection |
| 3 | No orphaned alarm objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00007 | Alarms - Alarm configuration and action parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_OS_00008

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00008 |
| Title | OS Model - Resource Configuration Parsing |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly extracts resource configurations from XDM containers, including resource properties and service access references.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing OsResource containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Resource Name | "Resource1" | Example resource identifier |
| Resource Property | "STANDARD" | Resource property (Standard, Link, etc.) |
| Scheduler Access | "FULL" | Scheduler access level |
| Service Access Reference | "Service1" | Service that uses this resource |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with OsResource container | OsResource object created successfully |
| 2 | Verify resource name extraction | getName() returns "Resource1" |
| 3 | Verify resource property extraction | getResourceProperty() returns "STANDARD" |
| 4 | Verify scheduler access extraction | getSchedulerAccess() returns "FULL" |
| 5 | Verify service access reference extraction | getServiceAccess() returns "Service1" |
| 6 | Validate resource property | Property is one of valid types (Standard, Link) |
| 7 | Validate scheduler access | Access level is valid (Full, Non) |
| 8 | Verify parent-child relationship | Resource's parent is OS module |

## Expected Results

- All resource attributes are extracted correctly
- Resource property is validated against supported types
- Scheduler access is validated
- Service access reference is correctly resolved
- Resource is properly registered with parent module

## Post-conditions

| # | Description |
|---|-------------|
| 1 | OsResource objects remain in memory for verification |
| 2 | EBModel contains updated resource collection |
| 3 | No orphaned resource objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00008 | Resources - Resource configuration and service access parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_OS_00009

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00009 |
| Title | OS Model - Memory Protection Parsing |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly extracts memory protection configurations from XDM containers, including microkernel configuration and memory region definitions.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing memory protection containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Microkernel Use | true | Microkernel enabled flag |
| Memory Region Name | "Region1" | Memory region identifier |
| Region Start Address | 0x10000000 | Region start address |
| Region End Address | 0x10000FFF | Region end address |
| Region Access | "READ_WRITE" | Access permissions |
| Region Application | "App1" | Application owning region |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with memory protection container | Memory protection object created successfully |
| 2 | Verify microkernel enabled extraction | isMicrokernelUsed() returns true |
| 3 | Verify memory region extraction | Memory region object created |
| 4 | Verify region name extraction | getName() returns "Region1" |
| 5 | Verify region start address extraction | getStartAddress() returns 0x10000000 |
| 6 | Verify region end address extraction | getEndAddress() returns 0x10000FFF |
| 7 | Verify region access permissions extraction | getAccess() returns "READ_WRITE" |
| 8 | Verify region application extraction | getApplication() returns "App1" |
| 9 | Validate address range | Start address < end address |

## Expected Results

- Microkernel configuration is extracted correctly
- Memory region attributes are extracted correctly
- Access permissions are validated
- Application ownership is established
- Address ranges are validated

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Memory protection objects remain in memory for verification |
| 2 | EBModel contains updated memory protection collection |
| 3 | No orphaned memory regions exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00009 | Memory Protection - Microkernel configuration and memory region parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_OS_00010

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00010 |
| Title | OS Reporter - Excel Worksheet Generation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS reporter correctly generates Excel worksheets for all OS entity types (tasks, ISRs, schedule tables, counters, alarms, resources, applications) with proper formatting.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |
| 3 | OS model objects are populated with test data |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Output File Path | "test_output/Os_report.xlsx" | Generated Excel file path |
| Worksheets to Generate | OsTask, OsIsr, OsScheduleTable, OsCounter, OsAlarm, OsResource, OsApplication | Expected worksheets |
| Task Count | 5-10 | Number of tasks for testing |
| ISR Count | 3-5 | Number of ISRs for testing |
| Schedule Table Count | 2-3 | Number of schedule tables |
| Column Headers | Name, Priority, Activation, Stack Size, etc. | Expected column structure |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create OsXdmXlsWriter instance | Writer initialized successfully |
| 2 | Generate OsTask worksheet | OsTask worksheet created with all data |
| 3 | Generate OsIsr worksheet | OsIsr worksheet created with all data |
| 4 | Generate OsScheduleTable worksheet | OsScheduleTable worksheet created with all data |
| 5 | Generate OsCounter worksheet | OsCounter worksheet created with all data |
| 6 | Generate OsAlarm worksheet | OsAlarm worksheet created with all data |
| 7 | Generate OsResource worksheet | OsResource worksheet created with all data |
| 8 | Generate OsApplication worksheet | OsApplication worksheet created with all data |
| 9 | Verify column auto-width formatting | Column widths sized to fit content |
| 10 | Verify numeric data centering | Numeric columns are center-aligned |

## Expected Results

- All expected worksheets are created
- All data is populated correctly
- Column formatting is applied (auto-width, centering for numeric)
- Data types are correct (strings for text, numbers for numeric values)
- File is valid and can be opened in Excel
- Performance meets requirements (< 5 seconds for typical file)

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file persists for review |
| 2 | No memory leaks in reporter |
| 3 | Model objects remain unchanged after export |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00010 | Reporter Layer - Excel worksheet generation and formatting | Covered |
| SWR_OS_00013 | Non-Functional - Excel generation performance | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Reporter Documentation | ../../src/eb_model/reporter/os_xdm_xls_writer.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_OS_00011

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00011 |
| Title | OS CLI - Command-Line Interface |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS CLI correctly parses command-line arguments, executes the parsing workflow, and handles various command options including verbose logging and worksheet filtering.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CLI entry point is registered (os-xdm-xlsx) |
| 3 | Test XDM file is available |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Command | `os-xdm-xlsx input.xdm output.xlsx` | Basic command execution |
| Input File | `data/test/Os_test.xdm` | Test input file |
| Output File | `test_output/Os_test.xlsx` | Test output file |
| Verbose Flag | `-v` or `--verbose` | Enable verbose logging |
| Skip Task Flag | `--skip-os-task` | Skip OsTask worksheet |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute basic command: `os-xdm-xlsx input.xdm output.xlsx` | Command completes successfully, Excel file generated |
| 2 | Verify output file exists | File created at specified path |
| 3 | Execute with verbose flag: `os-xdm-xlsx -v input.xdm output.xlsx` | Command completes with verbose logging output |
| 4 | Verify verbose output contains progress messages | Logs show parsing and export progress |
| 5 | Execute with skip flag: `os-xdm-xlsx --skip-os-task input.xdm output.xlsx` | Command completes, OsTask worksheet skipped |
| 6 | Verify output file missing OsTask worksheet | OsTask worksheet not present |
| 7 | Execute with missing input file: `os-xdm-xlsx missing.xdm output.xlsx` | Command exits with error, appropriate error message |
| 8 | Execute with invalid arguments: `os-xdm-xlsx` | Help message displayed |
| 9 | Verify help message includes usage and options | Help is complete and accurate |
| 10 | Execute with all worksheets skipped | Error message that at least one worksheet must be generated |

## Expected Results

- Basic command executes successfully
- Output Excel file is valid
- Verbose flag enables detailed logging
- Skip flags correctly filter worksheets
- Missing input file produces helpful error
- Invalid arguments display help message
- Exit codes are appropriate (0 for success, non-zero for error)

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Generated Excel files persist for review |
| 2 | No orphaned processes remain |
| 3 | System returns to pre-test state |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00011 | CLI Interface - Command-line argument parsing and execution | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| CLI Documentation | ../../src/eb_model/cli/os_xdm_2_xls_cli.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_OS_00012

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00012 |
| Title | OS Error Handling - Malformed XML |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly handles malformed XML files with missing tags, invalid nesting, or incorrect attribute types, providing appropriate error messages without crashing.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Malformed XDM test files are available |
| 3 | No other parsing operations are in progress |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Malformed File 1 | Missing closing tag | Verify missing tag handling |
| Malformed File 2 | Invalid attribute type (string for number) | Verify type validation |
| Malformed File 3 | Invalid enum value | Verify enum validation |
| Malformed File 4 | Duplicate element names | Verify duplicate handling |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XDM file with missing closing tag | Parser raises XMLSyntaxError or ValueError |
| 2 | Verify error message is descriptive | Error message indicates missing tag |
| 3 | Parse XDM file with invalid attribute type (priority="abc") | Parser raises ValueError with type mismatch message |
| 4 | Verify error message includes field name and expected type | Message is clear and actionable |
| 5 | Parse XDM file with invalid enum value (scheduleType="INVALID") | Parser raises ValueError with valid enum options |
| 6 | Verify error message includes valid options | User can see acceptable values |
| 7 | Parse XDM file with duplicate task names | Parser raises ValueError or handles with warning |
| 8 | Verify error indicates duplicate element | Message identifies conflicting element |

## Expected Results

- Malformed XML is detected and reported
- Error messages are clear, descriptive, and actionable
- Parser does not crash on malformed input
- Error messages include context (file, line, element, expected vs actual)
- Type mismatches are caught with helpful messages
- Invalid enum values show valid options
- Duplicate elements are detected

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No partial model objects created |
| 2 | System returns to clean state |
| 3 | Parser can be reused for subsequent operations |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00015 | Non-Functional - Malformed XML error handling | Covered |
| SWR_OS_00016 | Non-Functional - Missing optional elements handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Parser Documentation | ../../src/eb_model/parser/os_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_OS_00013

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00013 |
| Title | OS Error Handling - Required Element Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly validates required elements and references, detecting missing mandatory attributes and invalid path references.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XDM test files with missing required elements are available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Missing Required Attribute | Task without name | Verify required attribute validation |
| Invalid Counter Reference | Schedule table referencing non-existent counter | Verify reference validation |
| Invalid Application Reference | Task referencing non-existent application | Verify reference validation |
| Invalid Path Reference | Malformed ASPath reference | Verify path validation |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XDM file with task missing name attribute | Parser raises ValueError indicating missing required attribute |
| 2 | Verify error message includes element name and attribute | Message identifies exactly what's missing |
| 3 | Parse XDM file with schedule table referencing invalid counter | Parser raises ValueError or logs warning |
| 4 | Verify error message indicates unresolved reference | Message includes reference target |
| 5 | Parse XDM file with task referencing non-existent application | Parser raises ValueError or logs warning |
| 6 | Verify error handling allows optional application reference | Application reference is optional, no error if missing |
| 7 | Parse XDM file with malformed ASPath reference | Parser raises ValueError with path format details |
| 8 | Verify path validation accepts valid ASPath format | Valid paths like "ASPath:/Os/Task1" are accepted |

## Expected Results

- Missing required attributes are detected and reported
- Error messages clearly indicate what's missing and where
- Invalid references are detected with helpful messages
- Optional elements don't cause errors when missing
- Path references are validated for correct format
- Parser gracefully handles missing references (error or warning based on severity)

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No partial model objects created for invalid entities |
| 2 | System returns to clean state |
| 3 | Parser can be reused for subsequent operations |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00017 | Non-Functional - Required element validation | Covered |
| SWR_OS_00018 | Non-Functional - Path validation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Parser Documentation | ../../src/eb_model/parser/os_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |