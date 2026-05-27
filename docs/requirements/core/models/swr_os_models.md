# Software Requirements: Os Module - Model Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | Os Module Model Layer Requirements |
| Document ID | SWR_OS_MODELS_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | Os (Operating System) - Model Layer |

---

## Overview

The Os Model Layer provides Python classes representing AUTOSAR OS configuration entities extracted from EB Tresos XDM files.

**Implementation:** `src/eb_model/models/core/os_xdm.py`

---

## Requirements

### SWR_OS_MODELS_00001 - OsTask Model

The system shall provide an `OsTask` model class for OS task configuration.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsTaskActivation | int | ACTIVATION is a UINT32 attribute whose value defines the maximum number of activations that a task can have at any on... (1-255) | AUTOSAR |
| OsTaskPriority | int | OsTaskPriority is a UINT32 attribute whose value defines the relative base priority of the task. The lowest priority ... (0-2147483647) | AUTOSAR |
| OsTaskPeriod | float | OsTaskPeriod specifies the period in seconds of a periodically-activated task. The value can be used by the RTE modul... (0.0-86400.0) (disabled by default) | AUTOSAR |
| OsMeasure_Max_Runtime | bool | OsMeasure_Max_Runtime is a boolean attribute that tells the kernel to record the longest-observed executiontime for t... (default false) (disabled by default) | EB |
| OsTaskUse_Hw_Fp | bool | OsTaskUse_Hw_Fp is a boolean attribute that tells the kernel whether to provide a full floating-point environment for... (disabled by default) | EB |
| OsTaskCallScheduler | OsTaskCallScheduler | The OsTaskCallScheduler attribute informs the generator whether the task calls the Schedule() service. If OsTaskCallS... (DONTKNOW/YES/NO) (disabled by default) | EB |
| OsTaskType | OsTaskType | OsTaskType is an enumerated type whose value is one of: BASIC EXTENDED BASIC specifies that the task is a basic task.... (BASIC/EXTENDED) (disabled by default) | EB |
| OsStacksize | int | Note : Specification of task stack sizes is not needed, because Windows manages stacks automatically. (0-2000000000) | EB |
| OsTaskSchedule | OsTaskSchedule | OsTaskSchedule is an enumerated type whose value is one of: NON FULL FULL specifies that the task is preemptable. NON... (FULL/NON, default FULL) | AUTOSAR |
| OsMemoryMappingCodeLocationRef | EcucRefType | Reference to the memory mapping containing details about the section where the code is placed. This configuration par... (disabled by default) | AUTOSAR |
| OsTaskAccessingApplication | List[EcucRefType] | Reference to applications which have an access to this object. Objects of the referenced OsAplication can change the ... | AUTOSAR |
| OsTaskEventRef | List[EcucRefType] | This reference defines the list of events the extended task may react on. | AUTOSAR |
| OsTaskResourceRef | List[EcucRefType] | This reference defines a list of resources accessed by this task. | AUTOSAR |

**Implementation:** `os_xdm.py:OsTask`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00002 - OsIsr Model

The system shall provide an `OsIsr` model class for Interrupt Service Routines.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsIsrCategory | OsIsrCategory | OsIsrCategory is a UINT32 attribute that defines the IRS's Category. Only the values "CATEGORY_1" and "CATEGORY_2" ar... (CATEGORY_1/CATEGORY_2) | AUTOSAR |
| OsIsrPeriod | float | OsIsrPeriod specifies the period in seconds of a periodically-triggered ISR. The value can be used by the RTE module ... (0.0-86400.0) (disabled by default) | AUTOSAR |
| OsMeasure_Max_Runtime | bool | OsMeasure_Max_Runtime is a boolean attribute that tells the kernel to record the longest-observed execution-time for ... (default false) (disabled by default) | EB |
| OsEnable_On_Startup | bool | OsEnable_On_Startup is a boolean attribute that determines whether the kernel should automatically enable the interru... (default true) (disabled by default) | EB |
| OsWindowsVector | OsIsrOsWindowsVector | Note : There is no interrupt vector concept for AUTOSAR software running on Windows. Hence, the actual value for OsWi... (INTUSER00/INTUSER01/INTUSER02/INTUSER03/INTUSER04/INTUSER05/INTUSER06/INTUSER07/INTUSER08/INTUSER09/INTUSER10/INTUSER11/INTUSER12/INTUSER13/INTUSER14/INTUSER15/INTUSER16/INTUSER17/INTUSER18/INTUSER19/INTUSER20/INTUSER21/INTUSER22/INTUSER23/INTUSER24/INTUSER25/INTUSER26/INTUSER27/INTUSER28/INTUSER29/INTUSER30/INTUSER31/TIMER0/TIMER1/TIMER2/TIMER3/XCORE0/XCORE1/XCORE2/XCORE3) | EB |
| OsWindowsIrqLevel | int | Select the relative interrupt level (0-31) | EB |
| OsStacksize | int | Note : Specification of ISR stack sizes is not needed, because Windows manages stacks automatically. (0-2000000000) | EB |
| OsMemoryMappingCodeLocationRef | EcucRefType | Reference to the memory mapping containing details about the section where the code is placed. This configuration par... (disabled by default) | AUTOSAR |
| OsIsrResourceRef | List[EcucRefType] | This reference defines the resources accessed by this ISR. | AUTOSAR |
| OsIsrAccessingApplication | List[EcucRefType] | Reference to OsApplications that have an access to this object. Objects of the referenced OsApplication can enable or... | EB |

**Implementation:** `os_xdm.py:OsIsr`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00003 - OsCounter Model

The system shall provide an `OsCounter` model class for time measurement counters.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsCounterMaxAllowedValue | int | Maximum possible allowed value of the system counter in ticks. When the counter reaches this value, the next advancem... (1-4294967295) | AUTOSAR |
| OsCounterMinCycle | int | The MINCYCLE attribute specifies the minimum allowed number of counter ticks for a cyclic alarm linked to the counter. | AUTOSAR |
| OsCounterTicksPerBase | int | OsCounterTicksPerBase is a UINT32 value that specifies how many ticks of the counter represent a known unit of counti... (1-4294967295) | AUTOSAR |
| OsCounterType | OsCounterType | This parameter contains the natural type or unit of the counter. (HARDWARE/SOFTWARE) | AUTOSAR |
| OsCounterWindowsTimer | OsCounterWindowsTimer | Os Counter Windows Timer (TIMER0/TIMER1/TIMER2/TIMER3/TSIM_00/TSIM_01/TSIM_10/TSIM_11) | EB |
| OsWindowsIrqLevel | int | Select the relative interrupt level of the timer (1-32) | EB |
| OsSecondsPerTick | float | Note : If OsCounterType is set to HARDWARE, one tick always lasts 1 millisecond and hence, OsSecondsPerTick must alwa... (0.0-86400.0) (disabled by default) | AUTOSAR |
| OsCounterAccessingApplication | List[EcucRefType] | Reference to applications which have an access to this object. The objects of referenced OsAplication can access and ... | AUTOSAR |

**Implementation:** `os_xdm.py:OsCounter`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00004 - OsAlarm Model

The system shall provide an `OsAlarm` model class for time-based alarms.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsAlarmCounterRef | EcucRefType | The OsAlarmCounterRef attribute specifies the Counter with which the alarm is associated. Each alarm must be associat... | AUTOSAR |
| OsAlarmAccessingApplication | List[EcucRefType] | Reference to applications which have an access to this object. The objects of referenced OsAplication can access and ... | AUTOSAR |

**Implementation:** `os_xdm.py:OsAlarm`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00005 - OsAlarmAction Models

The system shall provide choice action model classes.

| Class | Purpose |
|-------|---------|
| OsAlarmActivateTask | This container specifies the parameters to activate a task. |
| OsAlarmCallback | This container specifies the parameters to call a callback for alarm. |
| OsAlarmIncrementCounter | This container specifies the parameters to increment a counter. |
| OsAlarmSetEvent | This container specifies the parameters to set an event |

**Implementation:** `os_xdm.py:OsAlarmActivateTask`, `os_xdm.py:OsAlarmCallback`, `os_xdm.py:OsAlarmIncrementCounter`, `os_xdm.py:OsAlarmSetEvent`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00006 - OsApplication Model

The system shall provide an `OsApplication` model class for OS application boundaries.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsTrustedApplicationWithProtection | bool | Parameter to specify if a trusted OS-Application is executed with memory protection or not. This configuration parame... (default false) | AUTOSAR |
| OsTrustedApplicationDelayTimingViolationCall | bool | Parameter to specify if a timing violation which occurs within an trusted OS-Application is raised immediately of if ... (default false) | AUTOSAR |
| OsTrusted | bool | OsTrusted is a boolean attribute that specifies whether Tasks, ISRs etc. associated with the application are to run w... (default false) | AUTOSAR |
| OsApplicationCoreAssignment | int | ID of the core onto which the OsApplication is bound. (disabled by default) | EB |
| OsApplicationCoreRef | EcucRefType | Reference to the Core Definition in the Ecuc Module where the CoreId is defined. This reference is used to describe t... | AUTOSAR |
| OsRestartTask | EcucRefType | If OsRestartTask parameter is enabled, the value of OsRestartTask specifies which task shall be automatically activat... (disabled by default) | AUTOSAR |
| OsAppEcucPartitionRef | EcucRefType | Denotes which EcucPartition is implemented by this OS application . This reference is not used by the Os generator. (disabled by default) | AUTOSAR |
| OsAppResourceRef | List[EcucRefType] | References the OsResources that belong to the OsApplication. | EB |
| OsAppAlarmRef | List[EcucRefType] | Specifies the OsAlarms that belong to the OsApplication. | AUTOSAR |
| OsAppCounterRef | List[EcucRefType] | References the OsCounters that belong to the OsApplication. | AUTOSAR |
| OsAppIsrRef | List[EcucRefType] | References which OsIsrs belong to the OsApplication. | AUTOSAR |
| OsAppScheduleTableRef | List[EcucRefType] | References the OsScheduleTables that belong to the OsApplication. | AUTOSAR |
| OsAppTaskRef | List[EcucRefType] | References which OsTasks belong to the OsApplication. | AUTOSAR |

**Implementation:** `os_xdm.py:OsApplication`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00007 - OsResource Model

The system shall provide an `OsResource` model class for resource management.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsResourceProperty | OsResourceProperty | RESOURCEPROPERTY is an enumerated attribute that whose values are: STANDARD a normal resource that can be expicitly t... (INTERNAL/LINKED/STANDARD, default STANDARD) | AUTOSAR |
| OsResourceLinkedResourceRef | EcucRefType | The link to the resource. Must be valid if OsResourceProperty is LINKED. If OsResourceProperty is not LINKED the valu... (disabled by default) | AUTOSAR |
| OsResourceAccessingApplication | List[EcucRefType] | Reference to OsApplications that have an access to this object. Objects of the referenced OsApplication can acquire o... | AUTOSAR |

**Implementation:** `os_xdm.py:OsResource`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00008 - OsHooks Model

The system shall provide an `OsHooks` model class for OS hook configuration.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsErrorHook | bool | OsErrorHook is a boolean attribute. If it is TRUE , the kernel calls the user-supplied void ErrorHook(StatusType erro... (default true) | AUTOSAR |
| OsPostTaskHook | bool | OsPostTaskHook is a boolean attribute. If it is TRUE , the kernel calls the user-supplied void PostTask-Hook(void) wh... (default false) | AUTOSAR |
| OsPreTaskHook | bool | OsPreTaskHook is a boolean attribute. If it is TRUE , the kernel calls the user-supplied void PreTaskHook(void) just ... (default false) | AUTOSAR |
| OsProtectionHook | bool | OsProtectionHook is a boolean attribute. If it is TRUE , the kernel calls the user-supplied ProtectionReturn-Type Pro... (default true) | AUTOSAR |
| OsShutdownHook | bool | OsShutdownHook is a boolean attribute. If it is TRUE , the kernel calls the user-supplied void ShutdownHook(StatusTyp... (default true) | AUTOSAR |
| OsStartupHook | bool | OsStartupHook is a boolean attribute. If it is TRUE , the kernel calls the user-supplied void StartupHook(void) immed... (default false) | AUTOSAR |
| OsPreISRHook | bool | OsPreISRHook is a boolean attribute. If it is TRUE , the kernel calls the user-supplied void PreIsrHook(os_isrid_t is... (default false) | EB |
| OsPostISRHook | bool | OsPostISRHook is a boolean attribute. If it is TRUE , the kernel calls the user-supplied void PostIsrHook(os_isrid_t ... (default false) | EB |
| OsMemoryMappingCodeLocationRef | EcucRefType | Reference to the memory mapping containing details about the section where the code is placed. This configuration par... (disabled by default) | AUTOSAR |

**Implementation:** `os_xdm.py:OsHooks`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00009 - OsScheduleTable Model

The system shall provide an `OsScheduleTable` model class for cyclic scheduling.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsScheduleTableDuration | int | The OsScheduleTableDuration attribute specifies the length of time for which the schedule table runs, from start to f... (default 0) | AUTOSAR |
| OsScheduleTableRepeating | bool | The OsScheduleTableRepeating attribute specifies whether the schedule table is periodic. TRUE periodic schedule table... (default false) | AUTOSAR |
| OsTimeUnit | OsScheduleTableOsTimeUnit | OsTimeUnit contains the time unit type used for this schedule table. (NANOSECONDS/TICKS, default TICKS) (disabled by default) | EB |
| OsScheduleTableCounterRef | EcucRefType | This parameter contains a reference to the counter which drives the schedule table.Each Schedule Table must be associ... | AUTOSAR |
| OsSchTblAccessingApplication | List[EcucRefType] | Reference to OsApplications that have an access to this object. Objects of the referenced OsApplication can start, st... | AUTOSAR |

**Implementation:** `os_xdm.py:OsScheduleTable`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00010 - OsEvent Model

The system shall provide an `OsEvent` model class for event masks.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsEventMask | int | The OsEventMask attribute is a UINT64 attribute that specifies the set of bits to be associated with the event. The E... (1-4294967295) (disabled by default) | AUTOSAR |

**Implementation:** `os_xdm.py:OsEvent`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00011 - OsSpinlock Model

The system shall provide an `OsSpinlock` model class for multi-core synchronization.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsSpinlockLockMethod | OsSpinlockLockMethod | OsSpinlockLockMethod is an enumerated type whose value is one of: LOCK_NOTHING LOCK_ALL_INTERRUPTS LOCK_CAT2_INTERRUP... (LOCK_NOTHING/LOCK_ALL_INTERRUPTS/LOCK_CAT2_INTERRUPTS/LOCK_WITH_RES_SCHEDULER, default LOCK_NOTHING) | AUTOSAR |
| OsSpinlockSuccessor | EcucRefType | Reference to the next OsSpinlock object in the linked list. To check whether a spinlock can be occupied (in a nested ... | AUTOSAR |
| OsSpinlockAccessingApplication | List[EcucRefType] | Reference to OsApplications that have an access to this object. Objects of the referenced OsApplication can acquire o... | AUTOSAR |

**Implementation:** `os_xdm.py:OsSpinlock`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00012 - OsPeripheralArea Model

The system shall provide an `OsPeripheralArea` model class for peripheral memory area configuration.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsPeripheralAreaEndAddress | int | Last valid address of a peripheral area. This configuration parameter is not supported by AutoCore OS. (0-9223372036854775807) | AUTOSAR |
| OsPeripheralAreaId | int | ID of the peripheral area. This configuration parameter is not supported by AutoCore OS. (0-9223372036854775807) | AUTOSAR |
| OsPeripheralAreaStartAddress | int | First valid address of a peripheral area. This configuration parameter is not supported by AutoCore OS. (0-9223372036854775807) | AUTOSAR |
| OsPeripheralAreaAccessingApplication | EcucRefType | Reference to application which have access to this object. This configuration parameter is not supported by EB tresos... | AUTOSAR |

**Implementation:** `os_xdm.py:OsPeripheralArea`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00013 - OsOS Model

The system shall provide an `OsOS` model class for OS-level kernel configuration.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsUseArti | bool | The OsUseArti attribute defines whether the OS uses and calls ARTI hooks. This includes also the generation of relate... (default false) | AUTOSAR |
| OsScalabilityClass | OsOSOsScalabilityClass | A scalability class for each System Object OS has to be selected. In order to customize the operating system to the n... (SC1/SC2/SC3/SC4) (disabled by default) | AUTOSAR |
| OsNumberOfCores | int | Maximum number of cores that are controlled by EB tresos AutoCore OS. (default 1) | AUTOSAR |
| OsStackMonitoring | bool | Note : Windows system calls do not allow safe estimates about how much stack space is actually used. Therefore stack ... (default false) | AUTOSAR |
| OsStatus | OsOSOsStatus | STATUS is an enumerated type whose value is one of: STANDARD EXTENDED In OS there is no possibility of the system ent... (EXTENDED/STANDARD, default STANDARD) | AUTOSAR |
| OsUseGetServiceId | bool | In the precompiled OS kernel the OSErrorGetServiceID() API is always available within the ErrorHook() . However, if y... (default false) | AUTOSAR |
| OsUseParameterAccess | bool | In the precompiled OS kernel the OSError_x1_x2() APIs are always available within the ErrorHook() . However, if you a... (default false) | AUTOSAR |
| OsUseResScheduler | bool | OsUseResScheduler is a boolean attribute. If it is TRUE , the Generator creates a resource called RES_SCHEDULER whose... (default true) | AUTOSAR |
| OsCC | OsOSOsCC | Choose automatic selection or one of the following conformance classes: BCC1 BCC2 ECC1 ECC2 The precompiled OS kernel... (BCC1/BCC2/ECC1/ECC2) (disabled by default) | EB |
| OsTrace | bool | OsTrace is a boolean attribute. If it is TRUE , the macro OS_USE_TRACE will be passed via the Make environment to the... (default false) | EB |
| OsExtra_Runtime_Checks | bool | OsExtra_Runtime_Checks is a boolean attribute. If it is TRUE , the kernel makes a range of extra checks at specific p... (default false) | EB |
| OsStartupChecks | bool | OsStartupChecks is a boolean attribute. If it is TRUE , the kernel makes a range of extra checks at system start-up. ... (default false) | EB |
| OsServiceTrace | bool | Check this if you want to trace system calls via ORTI (default false) | EB |
| OsSourceOptimization | bool | Check this if you want to build a library optimized according to the configuration. (default false) | EB |
| OsMicrocontroller | OsOSOsMicrocontroller | Os Microcontroller (WIN32X86, default WIN32X86) | EB |
| OsWindowsExecutionTimer | OsOSOsWindowsExecutionTimer | Note: AUTOSAR protection features are not supported on Windows. (TIMER0/TIMER1/TIMER2/TIMER3) (disabled by default) | EB |
| OsUseLastError | bool | OsUseLastError is a boolean attribute. If it is TRUE , the last error is stored internally and can be accessed via OR... (default false) | EB |
| OsTracebuffer | int | OsTracebuffer defines the size of the trace buffer for tracing. A value of 0 disables tracing. (0-65536) | EB |
| OsSchedule | OsOSOsSchedule | NON FULL MIXED NON means that all Tasks must have their OsTaskSchedule attribute set to NON . FULL means that all Tas... (NON/FULL/MIXED, default MIXED) (disabled by default) | EB |
| OsGenerateSWCD | bool | OsGenerateSWCD is a boolean attribute. If it is enabled, the OS specific software component description (SWCD) files ... (default false) | EB |
| OsTrappingKernel | bool | OsTrappingKernel is an optional boolean attribute. If it is TRUE , the kernel is entered via a Systrap mechanism. Thi... (default true) (disabled by default) | EB |
| OsUseLogicalCoreIDs | bool | Note: Advanced logical core mapping is currently not supported. The default setting and behavior is as for disabled. ... (default false) | EB |
| OsTimestampTimer | OsOSOsTimestampTimer | The timestamp timer is always based on the API QueryPerformanceCounter (QPC) of Microsoft Windows. (INTERNAL, default INTERNAL) | EB |
| OsInitCoreId | int | OsInitCoreId designates the processor core, which will control the OS start-up. If this value is disabled, the genera... (disabled by default) | EB |
| OsMaxNumberOfCores | int | This is the number of cores provided by the hardware. (default 4) | EB |
| OsProtection | OsOSOsProtection | Note: AUTOSAR protection features are not supported on Windows. (OFF/ON, default OFF) | EB |
| OsStackOptimization | OsOSOsStackOptimization | Note: Windows is in charge of stack management. Hence, there are no stack optimization options available. (GLOBAL/NO/WITHIN_APPLICATIONS, default NO) | EB |
| OsWindowsTimeWarpFactor | int | OsWindowsTimeWarpFactor The time warp factor may be used to slow down the time perceived by an AUTOSAR application pr... (1-4294967296) | EB |

**Implementation:** `os_xdm.py:OsOS`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00014 - OsAppMode Model

The system shall provide an `OsAppMode` model class for application mode definitions.


**Implementation:** `os_xdm.py:OsAppMode`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00015 - OsCoreConfig Model

The system shall provide an `OsCoreConfig` model class for multi-core configuration.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsCoreId | int | OsCoreId physical core index based on the CPU core ID. Values range from 0 to OsMaxNumberOfCores-1. The logical core ... (default 0) | EB |
| OsLogicalCoreId | int | OsLogicalCoreId manually changes the logical core ID for the physical core with index OsCoreId. To change this config... (default -1) | EB |
| OsWindowsExecutionTimer | OsCoreConfigOsWindowsExecutionTimer | Choose a timer for the execution protection. (TIMER0/TIMER1/TIMER2/TIMER3) (disabled by default) | EB |

**Implementation:** `os_xdm.py:OsCoreConfig`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00016 - OsAutosarCustomization Model

The system shall provide an `OsAutosarCustomization` model class for AUTOSAR-specific customizations.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsExceptionHandling | bool | Note: Exceptions are always handled by Windows. (default false) | EB |
| OsErrorHandling | OsAutosarCustomizationOsErrorHandling | This parameter can be used to restrict the amount of error handling that is performed by the OS. The permitted values... (MINIMAL/AUTOSAR/FULL, default AUTOSAR) | EB |
| OsStrictServiceProtection | bool | Setting this option to FALSE disables most of the calling-context checks in the System Services. The OS will then onl... (default true) | EB |
| OsCat1DirectCall | bool | This parameter selects whether a category 1 ISR is called directly or via the operating system's category 1 interrupt... (default false) | EB |
| OsInterruptLockingChecks | OsAutosarCustomizationOsInterruptLockingChecks | MINIMAL : Select MINIMAL to only check the interrupt lock status when it affects the kernel's operation. The interrup... (MINIMAL/EXTRACHECK/AUTOSAR, default AUTOSAR) | EB |
| OsUserTaskReturn | OsAutosarCustomizationOsUserTaskReturn | Note: On Windows, each task is executed by a separate thread, hence there is no danger of executing undefined code in... (KILL_TASK/LOOP, default KILL_TASK) | EB |
| OsCallIsr | OsAutosarCustomizationOsCallIsr | Note: On Windows, ISRs are always called directly. This means, it is not possible to kill a running ISR. (DIRECTLY/VIA_WRAPPER, default DIRECTLY) | EB |
| OsCallAppErrorHook | OsAutosarCustomizationOsCallAppErrorHook | Note: On Windows, hook functions are always called directly. This means, there is no possibility to kill or to termin... (DIRECTLY/VIA_WRAPPER, default DIRECTLY) | EB |
| OsPermitSystemObjects | bool | Setting this option to TRUE inhibits the check that, if an OS application exists, all Tasks and ISRs must belong to a... (default false) | EB |
| OsCallAppStartupShutdownHook | OsAutosarCustomizationOsCallAppStartupShutdownHook | Note: On Windows, hook functions are always called directly. This means, there is no possibility to kill or to termin... (DIRECTLY/VIA_WRAPPER, default DIRECTLY) | EB |

**Implementation:** `os_xdm.py:OsAutosarCustomization`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00017 - Os Model (Root)

The system shall provide an `Os` root model class containing all OS entities.

**Methods:**
- `getOsTaskList()` - Get all tasks
- `getOsIsrList()` - Get all ISRs
- `getOsAlarmList()` - Get all alarms
- `getOsCounterList()` - Get all counters
- `getOsApplicationList()` - Get all applications
- `getOsResourceList()` - Get all resources
- `getOsEventList()` - Get all events
- `getOsSpinlockList()` - Get all spinlocks
- `getOsScheduleTableList()` - Get all schedule tables
- `getOsPeripheralAreaList()` - Get all peripheral areas
- `getOsCoreConfigList()` - Get all core configs
- `getOsAppModeList()` - Get all application modes
- `getOsTaskOsApplication(taskName)` - Get application for task (O(1) lookup)
- `getOsIsrOsApplication(isrName)` - Get application for ISR (O(1) lookup)

**Implementation:** `os_xdm.py:Os`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_OS_MODELS_00001 | os_xdm.py:OsTask | UTS_OS_MODEL_00001 |
| SWR_OS_MODELS_00002 | os_xdm.py:OsIsr | UTS_OS_MODEL_00002 |
| SWR_OS_MODELS_00003 | os_xdm.py:OsCounter | UTS_OS_MODEL_00005 |
| SWR_OS_MODELS_00004 | os_xdm.py:OsAlarm | UTS_OS_MODEL_00003 |
| SWR_OS_MODELS_00005 | os_xdm.py:OsAlarmAction | UTS_OS_MODEL_00001 |
| SWR_OS_MODELS_00006 | os_xdm.py:OsApplication | UTS_OS_MODEL_00008 |
| SWR_OS_MODELS_00007 | os_xdm.py:OsResource | UTS_OS_MODEL_00009 |
| SWR_OS_MODELS_00008 | os_xdm.py:OsHooks | UTS_OS_MODEL_00010 |
| SWR_OS_MODELS_00009 | os_xdm.py:OsScheduleTable | UTS_OS_MODEL_00004 |
| SWR_OS_MODELS_00010 | os_xdm.py:OsEvent | UTS_OS_MODEL_00007 |
| SWR_OS_MODELS_00011 | os_xdm.py:OsSpinlock | UTS_OS_MODEL_00006 |
| SWR_OS_MODELS_00012 | os_xdm.py:OsPeripheralArea | UTS_OS_MODEL_00000 |
| SWR_OS_MODELS_00013 | os_xdm.py:OsOS | UTS_OS_MODEL_00000 |
| SWR_OS_MODELS_00014 | os_xdm.py:OsAppMode | UTS_OS_MODEL_00000 |
| SWR_OS_MODELS_00015 | os_xdm.py:OsCoreConfig | UTS_OS_MODEL_00000 |
| SWR_OS_MODELS_00016 | os_xdm.py:OsAutosarCustomization | UTS_OS_MODEL_00000 |
| SWR_OS_MODELS_00017 | os_xdm.py:Os (Root) | UTS_OS_MODEL_00000 |
