"""
Os Excel Reporter Tests.

Implements:
    - TC_UNIT_REPORTER_00016: Os Excel Reporter - File Creation
    - TC_UNIT_REPORTER_00017: Os Excel Reporter - Edge Cases

Implements: SWR_REPORTER_00002
"""
import os
import tempfile
from openpyxl import load_workbook
from eb_model.models.core.abstract import EcucRefType
from eb_model.models.core.eb_doc import EBModel
from eb_model.models.core.os_xdm import (
    Os, OsSpinlock, OsTask, OsApplication, OsOS, OsHooks,
    OsMicrokernel, MkMemoryProtection, MkMemoryRegion,
    OsScheduleTable
)
from eb_model.reporter.excel_reporter.core.os_xdm import OsXdmXlsWriter


class TestOsXdmXlsWriter:

    def test_write_creates_excel_file(self):
        """Test that write() creates a valid Excel file.

        Implements: TC_UNIT_REPORTER_00016
        """
        writer = OsXdmXlsWriter()

        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
            filename = f.name

        try:
            doc = EBModel.getInstance()
            writer.write(filename, doc, options={"skip_os_task": True})

            assert os.path.exists(filename)
            assert os.path.getsize(filename) > 0

            wb = load_workbook(filename)
            # OS reporter creates multiple sheets
            assert len(wb.sheetnames) > 0
            wb.close()
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_write_creates_expected_sheets(self):
        """Test that write() creates expected sheets.

        Implements: TC_UNIT_REPORTER_00016
        """
        writer = OsXdmXlsWriter()

        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
            filename = f.name

        try:
            doc = EBModel.getInstance()
            writer.write(filename, doc, options={"skip_os_task": True})

            wb = load_workbook(filename)

            # Check for expected sheets
            expected_sheets = ["OsApplications", "OsIsr"]
            for sheet_name in expected_sheets:
                assert sheet_name in wb.sheetnames, f"Sheet {sheet_name} not found"

            wb.close()
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_write_spinlock_multiple_accessing_apps(self):
        """
        Test spinlock sheet with multiple accessing applications (wrap text).

        Implements: TC_UNIT_REPORTER_00017
        """
        writer = OsXdmXlsWriter()

        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
            filename = f.name

        try:
            doc = EBModel.getInstance()
            os_mod = doc.getOs()

            spinlock = OsSpinlock(os_mod, "TestSpinlock")
            spinlock.setOsSpinlockLockMethod("STANDARD")
            spinlock.addOsSpinlockAccessingApplication(EcucRefType("ASPath:/Os/App1"))
            spinlock.addOsSpinlockAccessingApplication(EcucRefType("ASPath:/Os/App2"))
            os_mod.addOsSpinlock(spinlock)

            writer.write(filename, doc)

            wb = load_workbook(filename)
            assert "OsSpinlock" in wb.sheetnames
            sheet = wb["OsSpinlock"]
            # Row 2 should have the spinlock data
            assert sheet.cell(row=2, column=1).value == "TestSpinlock"
            assert sheet.cell(row=2, column=2).value == "STANDARD"
            wb.close()
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_write_os_task_rte_resources(self):
        """
        Test task sheet with RTE-pattern resources.

        Implements: TC_UNIT_REPORTER_00017
        """
        writer = OsXdmXlsWriter()

        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
            filename = f.name

        try:
            doc = EBModel.getInstance()
            os_mod = doc.getOs()

            # Create an application for task mapping.
            # The ref's short name (last path segment) must match the task name.
            app = OsApplication(os_mod, "App1")
            app.setOsTrusted(True)
            app.setOsApplicationCoreAssignment(0)
            app.addOsAppTaskRef(EcucRefType("/Os/TaskRte"))
            os_mod.addOsApplication(app)

            task = OsTask(os_mod, "TaskRte")
            task.setOsTaskPriority(10)
            task.setOsTaskActivation(1)
            task.setOsTaskSchedule("FULL")
            task.setOsStacksize(1024)
            # Add RTE-pattern resources (lines 161-162)
            task.addOsTaskResourceRef(EcucRefType("Rte_CanIf"))
            task.addOsTaskResourceRef(EcucRefType("Rte_Com"))
            # Add non-RTE resource that should be filtered
            task.addOsTaskResourceRef(EcucRefType("Res_Standard"))
            os_mod.addOsTask(task)

            writer.write(filename, doc)

            wb = load_workbook(filename)
            assert "OsTask" in wb.sheetnames
            sheet = wb["OsTask"]
            # Row 2 should have the task data
            assert sheet.cell(row=2, column=1).value == "TaskRte"
            # Column 9 should contain RTE resources (2 items, wrapped)
            cell_value = sheet.cell(row=2, column=9).value
            assert cell_value is not None
            assert "Rte_CanIf" in cell_value
            assert "Rte_Com" in cell_value
            # Non-RTE resource should not be in the cell
            assert "Res_Standard" not in cell_value
            wb.close()
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_write_os_task_many_rte_resources(self):
        """
        Test task sheet with >10 RTE resources (Total: N summary).

        Implements: TC_UNIT_REPORTER_00017
        """
        writer = OsXdmXlsWriter()

        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
            filename = f.name

        try:
            doc = EBModel.getInstance()
            os_mod = doc.getOs()

            # Create an application for task mapping
            app = OsApplication(os_mod, "App1")
            app.setOsTrusted(True)
            app.setOsApplicationCoreAssignment(0)
            app.addOsAppTaskRef(EcucRefType("/Os/TaskManyRte"))
            os_mod.addOsApplication(app)

            task = OsTask(os_mod, "TaskManyRte")
            task.setOsTaskPriority(5)
            task.setOsTaskActivation(1)
            task.setOsTaskSchedule("FULL")
            task.setOsStacksize(4096)
            # Add 12 RTE-pattern resources (>10 triggers total summary on line 165)
            for i in range(12):
                task.addOsTaskResourceRef(EcucRefType("Rte_Resource_%d" % i))
            os_mod.addOsTask(task)

            writer.write(filename, doc)

            wb = load_workbook(filename)
            assert "OsTask" in wb.sheetnames
            sheet = wb["OsTask"]
            # Column 9 should show total count summary
            cell_value = sheet.cell(row=2, column=9).value
            assert cell_value is not None
            assert "Total: 12 OsResources" in cell_value
            wb.close()
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_write_os_os_and_hooks(self):
        """
        Test OsOS and OsHooks sheets are produced when data exists.

        Implements: TC_UNIT_REPORTER_00017
        """
        writer = OsXdmXlsWriter()

        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
            filename = f.name

        try:
            doc = EBModel.getInstance()
            os_mod = doc.getOs()

            os_os = OsOS(os_mod, "OsOS")
            os_os.setOsScalabilityClass("SC1")
            os_os.setOsNumberOfCores(2)
            os_os.setOsStackMonitoring(True)
            os_os.setOsUseGetServiceId(False)
            os_os.setOsUseParameterAccess(True)
            os_os.setOsUseResScheduler(True)
            os_os.setOsStatus("STANDARD")
            os_mod.setOsOS(os_os)

            hooks = OsHooks(os_mod, "OsHooks")
            hooks.setOsErrorHook(True)
            hooks.setOsShutdownHook(False)
            hooks.setOsStartupHook(True)
            hooks.setOsPreTaskHook(False)
            hooks.setOsPostTaskHook(True)
            hooks.setOsProtectionHook(False)
            os_mod.setOsHooks(hooks)

            writer.write(filename, doc)

            wb = load_workbook(filename)
            assert "OsOS" in wb.sheetnames
            assert "OsHooks" in wb.sheetnames

            os_sheet = wb["OsOS"]
            assert os_sheet.cell(row=2, column=1).value == "ScalabilityClass"
            assert os_sheet.cell(row=2, column=2).value == "SC1"
            assert os_sheet.cell(row=3, column=1).value == "NumberOfCores"
            assert os_sheet.cell(row=3, column=2).value == 2

            hooks_sheet = wb["OsHooks"]
            assert hooks_sheet.cell(row=2, column=1).value == "ErrorHook"
            assert hooks_sheet.cell(row=2, column=2).value == "Y"
            wb.close()
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_write_mk_memory_regions(self):
        """
        Test MkMemoryRegion sheet production with microkernel data.

        Implements: TC_UNIT_REPORTER_00017
        """
        writer = OsXdmXlsWriter()

        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
            filename = f.name

        try:
            doc = EBModel.getInstance()
            os_mod = doc.getOs()

            kernel = OsMicrokernel(os_mod, "OsMicrokernel")
            protection = MkMemoryProtection(kernel, "MkMemoryProtection")
            region = MkMemoryRegion(protection, "Region1")
            region.setMkMemoryRegionFlags(1)
            region.setMkMemoryRegionInitialize(True)
            region.setMkMemoryRegionGlobal(False)
            protection.addMkMemoryRegion(region)
            kernel.setMkMemoryProtection(protection)
            os_mod.setOsMicrokernel(kernel)

            writer.write(filename, doc)

            wb = load_workbook(filename)
            assert "MkMemoryRegion" in wb.sheetnames
            sheet = wb["MkMemoryRegion"]
            assert sheet.cell(row=2, column=1).value == "Region1"
            assert sheet.cell(row=2, column=2).value == 1
            assert sheet.cell(row=2, column=3).value == "Y"
            wb.close()
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_write_mk_memory_region_exists_false_paths(self):
        """
        Test mk_memory_region_exists returns False for missing data paths.

        Implements: TC_UNIT_REPORTER_00017
        """
        doc = EBModel.getInstance()
        os_mod = doc.getOs()
        writer = OsXdmXlsWriter()

        # No microkernel set
        assert writer.mk_memory_region_exists(doc) is False

        # Microkernel without protection
        kernel = OsMicrokernel(os_mod, "OsMicrokernel")
        os_mod.setOsMicrokernel(kernel)
        assert writer.mk_memory_region_exists(doc) is False

        # Protection without regions
        protection = MkMemoryProtection(kernel, "MkMemoryProtection")
        kernel.setMkMemoryProtection(protection)
        assert writer.mk_memory_region_exists(doc) is False

        # Protection with regions
        region = MkMemoryRegion(protection, "Region1")
        protection.addMkMemoryRegion(region)
        assert writer.mk_memory_region_exists(doc) is True
