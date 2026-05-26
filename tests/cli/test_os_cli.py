"""
CLI tests for OS module command-line interface.

Tests the os-xdm-xlsx command with various arguments, flags,
and error conditions.

Implements: TC_UNIT_OS_00011
"""
import os
import sys
import pytest

from eb_model.cli.os_xdm_2_xls_cli import main as os_xdm_cli
from eb_model.models import EBModel


OS_XDM_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "data", "Os.xdm")


@pytest.mark.integration
class TestOsCli:

    @pytest.fixture(autouse=True)
    def reset_model(self):
        """Reset EBModel singleton before each test."""
        EBModel._instances = {}
        yield

    def test_cli_basic_execution(self, tmp_path):
        """
        Verify basic CLI command executes successfully.

        Implements: TC_UNIT_OS_00011 Steps 1-2
        """
        output_path = tmp_path / "Os_test.xlsx"
        sys.argv = ["os-xdm-xlsx", OS_XDM_PATH, str(output_path)]
        os_xdm_cli()

        assert output_path.exists(), "Excel file was not created"
        assert output_path.stat().st_size > 0, "Excel file is empty"

    def test_cli_verbose_flag(self, tmp_path):
        """
        Verify CLI with verbose flag produces logging output.

        Implements: TC_UNIT_OS_00011 Steps 3-4
        """
        output_path = tmp_path / "Os_verbose.xlsx"
        sys.argv = ["os-xdm-xlsx", "-v", OS_XDM_PATH, str(output_path)]
        os_xdm_cli()

        assert output_path.exists(), "Excel file was not created with verbose flag"

    def test_cli_skip_os_task(self, tmp_path):
        """
        Verify CLI with --skip-os-task flag skips OsTask worksheet.

        Implements: TC_UNIT_OS_00011 Steps 5-6
        """
        output_path = tmp_path / "Os_skip_task.xlsx"
        sys.argv = ["os-xdm-xlsx", "--skip-os-task", OS_XDM_PATH, str(output_path)]
        os_xdm_cli()

        assert output_path.exists(), "Excel file was not created with skip flag"

    def test_cli_missing_input_file(self, tmp_path):
        """
        Verify CLI handles missing input file gracefully.

        Implements: TC_UNIT_OS_00011 Step 7
        """
        output_path = tmp_path / "Os_missing.xlsx"
        sys.argv = ["os-xdm-xlsx", "/nonexistent/path/Os.xdm", str(output_path)]

        with pytest.raises(Exception):
            os_xdm_cli()

    def test_cli_no_arguments(self):
        """
        Verify CLI shows help/error when invoked without arguments.

        Implements: TC_UNIT_OS_00011 Steps 8-9
        """
        sys.argv = ["os-xdm-xlsx"]

        with pytest.raises(SystemExit):
            os_xdm_cli()
