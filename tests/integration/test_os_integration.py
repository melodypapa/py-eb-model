"""
Integration tests for OS module end-to-end workflow.

Tests complete OS XDM file parsing covering all entity types:
tasks, ISRs, schedule tables, counters, alarms, applications,
resources, spinlocks, OS configuration, and hooks.

Uses self-contained mock XDM data (no dependency on external data files).

Implements: TC_INT_OS_00001 through TC_INT_OS_00004
"""
import sys
import pytest

from eb_model.parser.core.eb_parser_factory import EbParserFactory
from eb_model.models import EBModel
from eb_model.reporter.excel_reporter.core.os_xdm import OsXdmXlsWriter
from eb_model.cli.os_xdm_2_xls_cli import main as os_xdm_cli
from tests.mock_data import MOCK_OS_XDM


@pytest.fixture
def mock_xdm(tmp_path):
    """Write mock OS XDM to a temporary file and return its path."""
    path = tmp_path / "Os_mock.xdm"
    path.write_text(MOCK_OS_XDM, encoding="utf-8")
    return str(path)


@pytest.mark.integration
class TestOsIntegration:

    def test_os_parser_creation_and_detection(self, mock_xdm):
        """
        Verify OS parser is correctly created and module detected.

        Implements: TC_INT_OS_00001 Step 1
        """
        parser = EbParserFactory.create(mock_xdm)
        assert parser is not None
        assert parser.__class__.__name__ == "OsXdmParser"

    def test_os_end_to_end_parsing(self, mock_xdm):
        """
        Verify complete OS XDM file parsing produces all entity types.

        Implements: TC_INT_OS_00001 Steps 2-6
        """
        parser = EbParserFactory.create(mock_xdm)
        model = EBModel.getInstance()
        parser.parse_xdm(mock_xdm, model)

        os_mod = model.getOs()

        # Verify all entity types are populated (TC_INT_OS_00001 Steps 5-6)
        assert len(os_mod.getOsTaskList()) > 0, "No tasks parsed"
        assert len(os_mod.getOsIsrList()) > 0, "No ISRs parsed"
        assert len(os_mod.getOsScheduleTableList()) > 0, "No schedule tables parsed"
        assert len(os_mod.getOsCounterList()) > 0, "No counters parsed"
        assert len(os_mod.getOsAlarmList()) > 0, "No alarms parsed"
        assert len(os_mod.getOsApplicationList()) > 0, "No applications parsed"
        assert len(os_mod.getOsResourceList()) > 0, "No resources parsed"
        assert len(os_mod.getOsSpinlockList()) > 0, "No spinlocks parsed"
        assert os_mod.getOsOS() is not None, "No OS configuration parsed"
        assert os_mod.getOsHooks() is not None, "No hooks parsed"

    def test_os_entity_relationships(self, mock_xdm):
        """
        Verify entity references resolve correctly.

        Implements: TC_INT_OS_00002
        """
        parser = EbParserFactory.create(mock_xdm)
        model = EBModel.getInstance()
        parser.parse_xdm(mock_xdm, model)

        os_mod = model.getOs()

        # Verify applications have task references
        for app in os_mod.getOsApplicationList():
            app_task_refs = app.getOsAppTaskRefs()
            assert app_task_refs is not None, f"Application {app.getName()} has no task ref list"

        # Verify schedule tables have counter references
        for table in os_mod.getOsScheduleTableList():
            counter_ref = table.getOsScheduleTableCounterRef()
            if counter_ref is not None:
                assert counter_ref.getValue() is not None

        # Verify alarms have counter references and actions
        for alarm in os_mod.getOsAlarmList():
            assert alarm.getOsAlarmCounterRef() is not None, \
                f"Alarm {alarm.getName()} missing counter ref"
            assert alarm.getOsAlarmAction() is not None, \
                f"Alarm {alarm.getName()} missing action"

    def test_os_excel_export(self, mock_xdm, tmp_path):
        """
        Verify Excel export produces correct output.

        Implements: TC_INT_OS_00003
        """
        parser = EbParserFactory.create(mock_xdm)
        model = EBModel.getInstance()
        parser.parse_xdm(mock_xdm, model)

        output_path = tmp_path / "Os_test.xlsx"
        writer = OsXdmXlsWriter()
        writer.write(str(output_path), model)

        # Verify file exists and has content
        assert output_path.exists(), "Excel file was not created"
        assert output_path.stat().st_size > 0, "Excel file is empty"


@pytest.mark.integration
def test_os_cli_execution(mock_xdm, tmp_path):
    """
    Verify CLI command produces Excel output.

    Implements: TC_INT_OS_00004
    """
    output_path = tmp_path / "Os_cli_test.xlsx"

    # Simulate CLI invocation
    sys.argv = ["os-xdm-xlsx", mock_xdm, str(output_path)]
    os_xdm_cli()

    assert output_path.exists(), "CLI did not create Excel file"
    assert output_path.stat().st_size > 0, "CLI Excel file is empty"
