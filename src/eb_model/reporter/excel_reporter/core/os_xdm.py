"""
OS XDM Excel Reporter - Generates Excel reports for OS module configuration.

Implements:
    - SWR_OS_REPORTER_00001: Excel Workbook Creation
    - SWR_OS_REPORTER_00002: General Sheet
    - SWR_OS_REPORTER_00003: Tasks Sheet
    - SWR_OS_REPORTER_00004: ISRs Sheet
    - SWR_OS_REPORTER_00005: Alarms Sheet
    - SWR_OS_REPORTER_00006: Counters Sheet
    - SWR_OS_REPORTER_00007: Applications Sheet
    - SWR_OS_REPORTER_00008: Resources Sheet
    - SWR_OS_REPORTER_00009: Events Sheet
    - SWR_OS_REPORTER_00010: Spinlocks Sheet
    - SWR_OS_REPORTER_00011: Schedule Tables Sheet
    - SWR_OS_REPORTER_00012: Application Resolution
    - SWR_OS_REPORTER_00013: Application Modes Sheet
    - SWR_OS_REPORTER_00014: Peripheral Areas Sheet
"""
import re
from openpyxl.styles import Alignment
from eb_model.models.core.eb_doc import EBModel
from eb_model.reporter.excel_reporter.core.abstract import ExcelReporter

RTE_RESOURCE_PATTERN = re.compile(r"Rte_\w+")


class OsXdmXlsWriter(ExcelReporter):
    """
    Excel reporter for AUTOSAR OS module configuration.

    Generates Excel workbook with sheets for tasks, ISRs, alarms,
    schedule tables, counters, applications, resources, events,
    spinlocks, application modes, and peripheral areas.

    Implements: SWR_OS_REPORTER_00001 (Excel Workbook Creation)
    """

    def __init__(self) -> None:
        """Initialize the OS Excel reporter."""
        super().__init__()

    def write_os_spinlocks(self, doc: EBModel):
        """
        Write spinlock configuration to the OsSpinlock worksheet.

        Creates a sheet with columns: Name, LockMethod, Successor, AccessingApplications.

        Args:
            doc: EBModel document containing OS configuration data.

        Implements: SWR_OS_REPORTER_00010 (Spinlocks Sheet)
        """
        sheet = self.wb.create_sheet("OsSpinlock", 0)

        title_row = ["Name", "LockMethod", "Successor", "AccessingApplications"]
        self.write_title_row(sheet, title_row)

        row = 2
        for spinlock in doc.getOs().getOsSpinlockList():
            self.write_cell(sheet, row, 1, spinlock.getName())
            self.write_cell(sheet, row, 2, spinlock.getOsSpinlockLockMethod())

            successor = spinlock.getOsSpinlockSuccessor()
            if successor is not None:
                self.write_cell(sheet, row, 3, successor.getShortName())

            accessing_apps = [ref.getShortName() for ref in spinlock.getOsSpinlockAccessingApplications()]
            if len(accessing_apps) > 0:
                cell = self.write_cell(sheet, row, 4, "\n".join(accessing_apps))
                if len(accessing_apps) > 1:
                    cell.alignment = Alignment(wrapText=True)

            row += 1
            self.logger.debug("Write OsSpinlock <%s>" % spinlock.getName())

        self.auto_width(sheet, {"D": 30})

    def write_os_os(self, doc: EBModel):
        """
        Write OS-level configuration to the OsOS worksheet.

        Creates a sheet with OS parameters including scalability class,
        number of cores, and various OS features.

        Args:
            doc: EBModel document containing OS configuration data.

        Implements: SWR_OS_REPORTER_00002 (General Sheet)
        """
        os_os = doc.getOs().getOsOS()
        if os_os is not None:
            sheet = self.wb.create_sheet("OsOS", 0)

            title_row = ["Parameter", "Value"]
            self.write_title_row(sheet, title_row)

            row = 2
            self.write_cell(sheet, row, 1, "ScalabilityClass")
            self.write_cell(sheet, row, 2, os_os.getOsScalabilityClass())
            row += 1

            self.write_cell(sheet, row, 1, "NumberOfCores")
            self.write_cell(sheet, row, 2, os_os.getOsNumberOfCores())
            row += 1

            self.write_cell(sheet, row, 1, "StackMonitoring")
            self.write_cell(sheet, row, 2, self.format_boolean(os_os.getOsStackMonitoring()))
            row += 1

            self.write_cell(sheet, row, 1, "UseGetServiceId")
            self.write_cell(sheet, row, 2, self.format_boolean(os_os.getOsUseGetServiceId()))
            row += 1

            self.write_cell(sheet, row, 1, "UseParameterAccess")
            self.write_cell(sheet, row, 2, self.format_boolean(os_os.getOsUseParameterAccess()))
            row += 1

            self.write_cell(sheet, row, 1, "UseResScheduler")
            self.write_cell(sheet, row, 2, self.format_boolean(os_os.getOsUseResScheduler()))
            row += 1

            self.write_cell(sheet, row, 1, "Status")
            self.write_cell(sheet, row, 2, os_os.getOsStatus())
            row += 1

            self.logger.debug("Write OsOS")
            self.auto_width(sheet, {"A": 20, "B": 25})

    def write_os_hooks(self, doc: EBModel):
        """
        Write hook configuration to the OsHooks worksheet.

        Creates a sheet with hook function enable/disable settings.

        Args:
            doc: EBModel document containing OS configuration data.

        Implements: SWR_OS_REPORTER_00012 (Application Resolution)
        """
        hooks = doc.getOs().getOsHooks()
        if hooks is not None:
            sheet = self.wb.create_sheet("OsHooks", 0)

            title_row = ["Hook", "Enabled"]
            self.write_title_row(sheet, title_row)

            row = 2
            self.write_cell(sheet, row, 1, "ErrorHook")
            self.write_cell(sheet, row, 2, self.format_boolean(hooks.getOsErrorHook()))
            row += 1

            self.write_cell(sheet, row, 1, "ShutdownHook")
            self.write_cell(sheet, row, 2, self.format_boolean(hooks.getOsShutdownHook()))
            row += 1

            self.write_cell(sheet, row, 1, "StartupHook")
            self.write_cell(sheet, row, 2, self.format_boolean(hooks.getOsStartupHook()))
            row += 1

            self.write_cell(sheet, row, 1, "PreTaskHook")
            self.write_cell(sheet, row, 2, self.format_boolean(hooks.getOsPreTaskHook()))
            row += 1

            self.write_cell(sheet, row, 1, "PostTaskHook")
            self.write_cell(sheet, row, 2, self.format_boolean(hooks.getOsPostTaskHook()))
            row += 1

            self.write_cell(sheet, row, 1, "ProtectionHook")
            self.write_cell(sheet, row, 2, self.format_boolean(hooks.getOsProtectionHook()))
            row += 1

            self.write_cell(sheet, row, 1, "PreISRHook")
            self.write_cell(sheet, row, 2, self.format_boolean(hooks.getOsPreISRHook()))
            row += 1

            self.write_cell(sheet, row, 1, "PostISRHook")
            self.write_cell(sheet, row, 2, self.format_boolean(hooks.getOsPostISRHook()))
            row += 1

            self.logger.debug("Write OsHooks")
            self.auto_width(sheet, {"A": 15, "B": 10})

    def write_os_tasks(self, doc: EBModel):
        """
        Write task configuration to the OsTask worksheet.

        Creates a sheet with columns: Name, OsApplication, OsTaskActivation,
        OsTaskPriority, OsTaskAutostart, OsTaskSchedule, OsTaskType, OsStacksize.

        Args:
            doc: EBModel document containing OS configuration data.

        Implements: SWR_OS_REPORTER_00003 (Tasks Sheet)
        """
        sheet = self.wb.create_sheet("OsTask", 0)

        title_row = ["Name", "OsApplication", "OsTaskActivation", "OsTaskPriority", "OsTaskAutostart",
                     "OsTaskSchedule", "OsStacksize", "OsTaskType", "OsResourceRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for os_task in doc.getOs().getOsTaskList():
            self.write_cell(sheet, row, 1, os_task.getName())
            os_app = doc.getOs().getOsTaskOsApplication(os_task.getName())
            self.write_cell(sheet, row, 2, os_app.getName())
            self.write_cell(sheet, row, 3, os_task.getOsTaskActivation())
            self.write_cell(sheet, row, 4, os_task.getOsTaskPriority())
            self.write_cell(sheet, row, 5, os_task.isOsTaskAutostart())

            self.write_cell(sheet, row, 6, os_task.getOsTaskSchedule())
            self.write_cell(sheet, row, 7, os_task.getOsStacksize())
            self.write_cell(sheet, row, 8, os_task.getOsTaskType())
            resources = []
            for resource_ref in os_task.getOsTaskResourceRefList():
                if RTE_RESOURCE_PATTERN.match(resource_ref.getValue()):
                    resources.append(resource_ref.getValue())
            total_resources = len(resources)
            if total_resources > 10:
                cell = self.write_cell(sheet, row, 9, "Total: %d OsResources" % (total_resources))
            else:
                cell = self.write_cell(sheet, row, 9, "\n".join(resources))
            if total_resources > 1 and total_resources < 10:
                cell.alignment = Alignment(wrapText=True)
            row += 1

            self.logger.debug("Write OsTask <%s>" % os_task.getName())

        self.auto_width(sheet)

    def write_os_applications(self, doc: EBModel):
        """
        Write application configuration to the OsApplications worksheet.

        Creates a sheet with columns: Name, OsTrusted, OsApplicationCoreAssignment,
        OsAppEcucPartitionRef.

        Args:
            doc: EBModel document containing OS configuration data.

        Implements: SWR_OS_REPORTER_00007 (Applications Sheet)
        """
        sheet = self.wb.create_sheet("OsApplications", 0)

        title_row = ["Name", "OsTrusted", "OsApplicationCoreAssignment", "OsAppEcucPartitionRef"]
        self.write_title_row(sheet, title_row)

        row = 2
        for os_app in doc.getOs().getOsApplicationList():
            self.write_cell(sheet, row, 1, os_app.getName())
            self.write_cell(sheet, row, 2, os_app.getOsTrusted())
            self.write_cell(sheet, row, 3, os_app.getOsApplicationCoreAssignment())
            if os_app.getOsAppEcucPartitionRef() is not None:
                self.write_cell(sheet, row, 4, os_app.getOsAppEcucPartitionRef().getShortName())
            # self.write_cell(sheet, row, 5, os_app.getOsAppMkPermitShutdownAllCores())
            # self.write_cell(sheet, row, 6, os_app.getOsAppMkCreateMemoryRegion())

            self.logger.debug("Write OsApplication <%s>" % os_app.getName())

        self.auto_width(sheet)

    def write_os_isrs(self, doc: EBModel):
        """
        Write ISR configuration to the OsIsr worksheet.

        Creates a sheet with columns: Name, OsApplication, OsIsrCategory,
        OsStacksize, OsIsrPriority, OsIsrVector, MkMemoryRegion.

        Args:
            doc: EBModel document containing OS configuration data.

        Implements: SWR_OS_REPORTER_00004 (ISRs Sheet)
        """
        sheet = self.wb.create_sheet("OsIsr", 1)

        title_row = ["Name", "OsApplication", "OsIsrCategory", "OsStacksize", "OsIsrPriority", "OsIsrVector", "MkMemoryRegion"]
        self.write_title_row(sheet, title_row)

        row = 2
        for os_isr in doc.getOs().getOsIsrList():
            self.write_cell(sheet, row, 1, os_isr.getName(), {'alignment': Alignment(vertical="top")})
            os_app = doc.getOs().getOsIsrOsApplication(os_isr.getName())
            if os_app is not None:
                self.write_cell(sheet, row, 2, os_app.getName(), format={'alignment': Alignment(horizontal="center", vertical="top")})
            self.write_cell(sheet, row, 3, os_isr.getOsIsrCategory(), format={'alignment': Alignment(horizontal="center", vertical="top")})
            self.write_cell(sheet, row, 4, os_isr.getOsStacksize(), format={'alignment': Alignment(horizontal="center", vertical="top")})
            self.write_cell(sheet, row, 5, os_isr.getOsIsrPriority(), format={'alignment': Alignment(horizontal="center", vertical="top")})
            self.write_cell(sheet, row, 6, os_isr.getOsIsrVector(), format={'alignment': Alignment(horizontal="center", vertical="top")})
            memory_region_names = [a.getShortName() for a in os_isr.getOsIsrMkMemoryRegionRefs()]
            alignment = Alignment(wrapText=(len(memory_region_names) > 1), vertical="top")
            self.write_cell(sheet, row, 7, "\n".join(memory_region_names),
                            {'alignment': alignment})
            row += 1

            self.logger.debug("Write OsIsr <%s>" % os_isr.getName())

        self.auto_width(sheet, {"G": 25})

    def write_os_schedule_tables(self, doc: EBModel):
        """
        Write schedule table configuration to the OsScheduleTable worksheet.

        Creates a sheet with columns: Name, Duration, Repeating, OsCount.

        Args:
            doc: EBModel document containing OS configuration data.

        Implements: SWR_OS_REPORTER_00011 (Schedule Tables Sheet)
        """
        sheet = self.wb.create_sheet("OsScheduleTable", 2)

        title_row = ["Name", "Duration", "Repeating", "OsCount"]
        self.write_title_row(sheet, title_row)

        row = 2
        for os_schedule_table in doc.getOs().getOsScheduleTableList():
            self.write_cell(sheet, row, 1, os_schedule_table.getName())
            self.write_cell_center(sheet, row, 2, os_schedule_table.getOsScheduleTableDuration())
            self.write_cell_center(sheet, row, 3, os_schedule_table.getOsScheduleTableRepeating())
            self.write_cell_center(sheet, row, 4, os_schedule_table.getOsScheduleTableCounterRef().getShortName())
            row += 1

            self.logger.debug("Write OsScheduleTable <%s>" % os_schedule_table.getName())

        self.auto_width(sheet)

    def write_os_counters(self, doc: EBModel):
        """
        Write counter configuration to the OsCounter worksheet.

        Creates a sheet with columns: Name, MaxAllowedValue, MinCycle,
        TicksPerBase, Type, SecondsPerTick.

        Args:
            doc: EBModel document containing OS configuration data.

        Implements: SWR_OS_REPORTER_00006 (Counters Sheet)
        """
        sheet = self.wb.create_sheet("OsCounter", 3)

        title_row = ["Name", "MaxAllowedValue", "MinCycle", "TicksPerBase", "Type", "SecondsPerTick"]
        self.write_title_row(sheet, title_row)

        row = 2
        for os_counter in doc.getOs().getOsCounterList():
            self.write_cell(sheet, row, 1, os_counter.getName())
            self.write_cell_center(sheet, row, 2, os_counter.getOsCounterMaxAllowedValue())
            self.write_cell_center(sheet, row, 3, os_counter.getOsCounterMinCycle())
            self.write_cell_center(sheet, row, 4, os_counter.getOsCounterTicksPerBase())
            self.write_cell_center(sheet, row, 5, os_counter.getOsCounterType())
            self.write_cell_center(sheet, row, 6, os_counter.getOsSecondsPerTick())
            row += 1

            self.logger.debug("Write OsScheduleTable <%s>" % os_counter.getName())

        self.auto_width(sheet)

    def write_expiry_points(self, doc: EBModel):
        sheet = self.wb.create_sheet("OsScheduleTableExpiryPoint", 4)

        title_row = ["ExpiryPoint", "OsScheduleTable", "OsCounter", "Offset (ms)", "Task"]
        self.write_title_row(sheet, title_row)

        row = 2
        for table in doc.getOs().getOsScheduleTableList():
            expiry_point_list = sorted(table.getOsScheduleTableExpiryPointList(),
                                       key=lambda o: o.getOsScheduleTblExpPointOffset())
            for expiry_point in expiry_point_list:
                self.write_cell(sheet, row, 1, expiry_point.getName())
                self.write_cell(sheet, row, 2, table.getName())
                self.write_cell_center(sheet, row, 3, table.getOsScheduleTableCounterRef().getShortName())
                self.write_cell_center(sheet, row, 4, expiry_point.getOsScheduleTblExpPointOffset())
                self.write_cell_center(sheet, row, 5, len(expiry_point.getOsScheduleTableTaskActivationList()))
                row += 1

            self.logger.debug("Write OsScheduleTable <%s>" % table.getName())

        self.auto_width(sheet)

    def mk_memory_region_exists(self, doc: EBModel) -> bool:
        mk = doc.getOs().getOsMicrokernel()
        if mk is None:
            return False

        protection = mk.getMkMemoryProtection()
        if protection is None:
            return False

        if len(protection.getMkMemoryRegionList()) <= 0:
            return False

        return True

    def write_mk_memory_regions(self, doc: EBModel):
        if self.mk_memory_region_exists(doc) is True:
            sheet = self.wb.create_sheet("MkMemoryRegion", 5)

            title_row = [
                "Name", "Flags", "Initialize", "Global", "InitThread", "IdleThread", "OsThread", "ErrorHook", "ProtHook", "ShutdownHook",
                "Shutdown", "Kernel", "InitializePerCore"
            ]
            self.write_title_row(sheet, title_row)

            row = 2
            for region in doc.getOs().getOsMicrokernel().getMkMemoryProtection().getMkMemoryRegionList():
                self.write_cell(sheet, row, 1, region.getName())
                self.write_cell_center(sheet, row, 2, region.getMkMemoryRegionFlags())
                self.write_cell_center(sheet, row, 3, self.format_boolean(region.getMkMemoryRegionInitialize()))
                self.write_cell_center(sheet, row, 4, self.format_boolean(region.getMkMemoryRegionGlobal()))
                self.write_cell_center(sheet, row, 5, self.format_boolean(region.getMkMemoryRegionInitThreadAccess()))
                self.write_cell_center(sheet, row, 6, self.format_boolean(region.getMkMemoryRegionIdleThreadAccess()))
                self.write_cell_center(sheet, row, 7, self.format_boolean(region.getMkMemoryRegionOsThreadAccess()))
                self.write_cell_center(sheet, row, 8, self.format_boolean(region.getMkMemoryRegionErrorHookAccess()))
                self.write_cell_center(sheet, row, 9, self.format_boolean(region.getMkMemoryRegionProtHookAccess()))
                self.write_cell_center(sheet, row, 10, self.format_boolean(region.getMkMemoryRegionShutdownHookAccess()))
                self.write_cell_center(sheet, row, 11, self.format_boolean(region.getMkMemoryRegionShutdownAccess()))
                self.write_cell_center(sheet, row, 12, self.format_boolean(region.getMkMemoryRegionKernelAccess()))
                self.write_cell_center(sheet, row, 13, self.format_boolean(region.getMkMemoryRegionInitializePerCore()))

                row += 1

                self.logger.debug("Write MkMemoryRegion <%s>" % region.getName())

            self.auto_width(sheet, {"B": 15})

    def write_os_appmodes(self, doc: EBModel):
        """
        Write application mode configuration to the OsAppMode worksheet.

        Creates a sheet with column: Name.

        Args:
            doc: EBModel document containing OS configuration data.

        Implements: SWR_OS_REPORTER_00013 (Application Modes Sheet)
        """
        appmodes = doc.getOs().getOsAppModeList()
        if len(appmodes) > 0:
            sheet = self.wb.create_sheet("OsAppMode", 0)

            title_row = ["Name"]
            self.write_title_row(sheet, title_row)

            row = 2
            for appmode in appmodes:
                self.write_cell(sheet, row, 1, appmode.getName())
                row += 1
                self.logger.debug("Write OsAppMode <%s>" % appmode.getName())

            self.auto_width(sheet, {"A": 30})

    def write_os_peripheral_areas(self, doc: EBModel):
        """
        Write peripheral area configuration to the OsPeripheralArea worksheet.

        Creates a sheet with columns: Name, Start Address, End Address, ID,
        Access Permission.

        Args:
            doc: EBModel document containing OS configuration data.

        Implements: SWR_OS_REPORTER_00014 (Peripheral Areas Sheet)
        """
        areas = doc.getOs().getOsPeripheralAreaList()
        if len(areas) > 0:
            sheet = self.wb.create_sheet("OsPeripheralArea", 0)

            title_row = ["Name", "Start Address", "End Address", "ID", "Access Permission"]
            self.write_title_row(sheet, title_row)

            row = 2
            for area in areas:
                self.write_cell(sheet, row, 1, area.getName())
                self.write_cell(sheet, row, 2, area.getOsPeripheralAreaStartAddress())
                self.write_cell(sheet, row, 3, area.getOsPeripheralAreaEndAddress())
                self.write_cell(sheet, row, 4, area.getOsPeripheralAreaId())
                self.write_cell(sheet, row, 5, area.getOsPeripheralAreaAccessPermission())
                row += 1
                self.logger.debug("Write OsPeripheralArea <%s>" % area.getName())

            self.auto_width(sheet, {"A": 30, "B": 15, "C": 15, "D": 10, "E": 20})

    def write(self, filename, doc: EBModel, options={"skip_os_task": False}):
        self.logger.info("Writing <%s>" % filename)

        # if not options['skip_os_task']:
        self.write_os_spinlocks(doc)
        self.write_os_os(doc)
        self.write_os_hooks(doc)
        self.write_os_tasks(doc)
        self.write_os_applications(doc)
        self.write_os_isrs(doc)
        self.write_os_schedule_tables(doc)
        self.write_os_counters(doc)
        self.write_expiry_points(doc)
        self.write_mk_memory_regions(doc)
        self.write_os_appmodes(doc)
        self.write_os_peripheral_areas(doc)

        self.save(filename)
