"""
Det Model Tests - Tests for DET module model classes.
"""
import pytest
from ...models.core.det_xdm import (
    Det, DetGeneral, DetErrorHook, DetInitError,
    CommonPublishedInformation, PublishedInformation, DetServiceAPI,
    DetNotification, DetDefensiveProgramming, SoftwareComponentList, InstanceIdList
)
from ...models.core.eb_doc import EBModel


class TestDetGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        general = DetGeneral(root, "DetGeneral")

        assert general.getName() == "DetGeneral"
        assert general.getParent() == root
        assert general.getDetDevErrorDetect() is None
        assert general.getDetEnabled() is None

    def test_set_det_dev_error_detect(self):
        root = EBModel.getInstance()
        general = DetGeneral(root, "DetGeneral")

        assert general.setDetDevErrorDetect(True) == general
        assert general.getDetDevErrorDetect() is True

        assert general.setDetDevErrorDetect(False) == general
        assert general.getDetDevErrorDetect() is False

    def test_set_det_enabled(self):
        root = EBModel.getInstance()
        general = DetGeneral(root, "DetGeneral")

        assert general.setDetEnabled(True) == general
        assert general.getDetEnabled() is True

        assert general.setDetEnabled(False) == general
        assert general.getDetEnabled() is False

    def test_set_det_forward_to_dlt(self):
        root = EBModel.getInstance()
        general = DetGeneral(root, "DetGeneral")

        assert general.setDetForwardToDlt(True) == general
        assert general.getDetForwardToDlt() is True

        assert general.setDetForwardToDlt(False) == general
        assert general.getDetForwardToDlt() is False

    def test_set_det_version_info_api(self):
        root = EBModel.getInstance()
        general = DetGeneral(root, "DetGeneral")

        assert general.setDetVersionInfoApi(True) == general
        assert general.getDetVersionInfoApi() is True

        assert general.setDetVersionInfoApi(False) == general
        assert general.getDetVersionInfoApi() is False

    def test_set_logging_mode(self):
        root = EBModel.getInstance()
        general = DetGeneral(root, "DetGeneral")

        assert general.setLoggingMode("BUFFER") == general
        assert general.getLoggingMode() == "BUFFER"

        assert general.setLoggingMode("DLT") == general
        assert general.getLoggingMode() == "DLT"

    def test_set_buffer_size(self):
        root = EBModel.getInstance()
        general = DetGeneral(root, "DetGeneral")

        assert general.setBufferSize(1024) == general
        assert general.getBufferSize() == 1024

        assert general.setBufferSize(2048) == general
        assert general.getBufferSize() == 2048


class TestDetErrorHook:

    def test_initialization(self):
        root = EBModel.getInstance()
        error_hook = DetErrorHook(root, "DetErrorHook")

        assert error_hook.getName() == "DetErrorHook"
        assert error_hook.getParent() == root
        assert error_hook.getDetErrorHookCallbackName() is None

    def test_set_det_error_hook_callback_name(self):
        root = EBModel.getInstance()
        error_hook = DetErrorHook(root, "DetErrorHook")

        assert error_hook.setDetErrorHookCallbackName("Det_ErrorHook") == error_hook
        assert error_hook.getDetErrorHookCallbackName() == "Det_ErrorHook"


class TestCommonPublishedInformation:

    def test_initialization(self):
        root = EBModel.getInstance()
        common_info = CommonPublishedInformation(root, "CommonPublishedInformation")

        assert common_info.getName() == "CommonPublishedInformation"
        assert common_info.getParent() == root
        assert common_info.getArMajorVersion() is None
        assert common_info.getArMinorVersion() is None
        assert common_info.getArPatchVersion() is None
        assert common_info.getSwMajorVersion() is None
        assert common_info.getSwMinorVersion() is None
        assert common_info.getSwPatchVersion() is None

    def test_set_ar_versions(self):
        root = EBModel.getInstance()
        common_info = CommonPublishedInformation(root, "CommonPublishedInformation")

        assert common_info.setArMajorVersion(4) == common_info
        assert common_info.getArMajorVersion() == 4

        assert common_info.setArMinorVersion(2) == common_info
        assert common_info.getArMinorVersion() == 2

        assert common_info.setArPatchVersion(1) == common_info
        assert common_info.getArPatchVersion() == 1

    def test_set_sw_versions(self):
        root = EBModel.getInstance()
        common_info = CommonPublishedInformation(root, "CommonPublishedInformation")

        assert common_info.setSwMajorVersion(1) == common_info
        assert common_info.getSwMajorVersion() == 1

        assert common_info.setSwMinorVersion(0) == common_info
        assert common_info.getSwMinorVersion() == 0

        assert common_info.setSwPatchVersion(3) == common_info
        assert common_info.getSwPatchVersion() == 3


class TestPublishedInformation:

    def test_initialization(self):
        root = EBModel.getInstance()
        published_info = PublishedInformation(root, "PublishedInformation")

        assert published_info.getName() == "PublishedInformation"
        assert published_info.getParent() == root
        assert published_info.getVendorId() is None
        assert published_info.getArReleaseMajorVersion() is None
        assert published_info.getArReleaseMinorVersion() is None
        assert published_info.getArReleasePatchVersion() is None
        assert published_info.getSwMajorVersion() is None
        assert published_info.getSwMinorVersion() is None
        assert published_info.getSwPatchVersion() is None

    def test_set_vendor_id(self):
        root = EBModel.getInstance()
        published_info = PublishedInformation(root, "PublishedInformation")

        assert published_info.setVendorId("Vector") == published_info
        assert published_info.getVendorId() == "Vector"

    def test_set_ar_release_versions(self):
        root = EBModel.getInstance()
        published_info = PublishedInformation(root, "PublishedInformation")

        assert published_info.setArReleaseMajorVersion("4") == published_info
        assert published_info.getArReleaseMajorVersion() == "4"

        assert published_info.setArReleaseMinorVersion("2") == published_info
        assert published_info.getArReleaseMinorVersion() == "2"

        assert published_info.setArReleasePatchVersion("1") == published_info
        assert published_info.getArReleasePatchVersion() == "1"

    def test_set_sw_versions(self):
        root = EBModel.getInstance()
        published_info = PublishedInformation(root, "PublishedInformation")

        assert published_info.setSwMajorVersion("1") == published_info
        assert published_info.getSwMajorVersion() == "1"

        assert published_info.setSwMinorVersion("0") == published_info
        assert published_info.getSwMinorVersion() == "0"

        assert published_info.setSwPatchVersion("3") == published_info
        assert published_info.getSwPatchVersion() == "3"


class TestDetServiceAPI:

    def test_initialization(self):
        root = EBModel.getInstance()
        service_api = DetServiceAPI(root, "DetServiceAPI")

        assert service_api.getName() == "DetServiceAPI"
        assert service_api.getParent() == root
        assert service_api.getDetVersionInfoApi() is None
        assert service_api.getDetReportRuntimeErrorCallout() is None

    def test_set_det_version_info_api(self):
        root = EBModel.getInstance()
        service_api = DetServiceAPI(root, "DetServiceAPI")

        assert service_api.setDetVersionInfoApi(True) == service_api
        assert service_api.getDetVersionInfoApi() is True

        assert service_api.setDetVersionInfoApi(False) == service_api
        assert service_api.getDetVersionInfoApi() is False

    def test_set_det_report_runtime_error_callout(self):
        root = EBModel.getInstance()
        service_api = DetServiceAPI(root, "DetServiceAPI")

        assert service_api.setDetReportRuntimeErrorCallout(True) == service_api
        assert service_api.getDetReportRuntimeErrorCallout() is True

        assert service_api.setDetReportRuntimeErrorCallout(False) == service_api
        assert service_api.getDetReportRuntimeErrorCallout() is False


class TestDetNotification:

    def test_initialization(self):
        root = EBModel.getInstance()
        notification = DetNotification(root, "DetNotification")

        assert notification.getName() == "DetNotification"
        assert notification.getParent() == root
        assert notification.getDetErrorNotification() is None
        assert notification.getDetRuntimeErrorNotification() is None
        assert notification.getDetTransitionErrorNotification() is None

    def test_set_det_error_notification(self):
        root = EBModel.getInstance()
        notification = DetNotification(root, "DetNotification")

        assert notification.setDetErrorNotification(True) == notification
        assert notification.getDetErrorNotification() is True

        assert notification.setDetErrorNotification(False) == notification
        assert notification.getDetErrorNotification() is False

    def test_set_det_runtime_error_notification(self):
        root = EBModel.getInstance()
        notification = DetNotification(root, "DetNotification")

        assert notification.setDetRuntimeErrorNotification(True) == notification
        assert notification.getDetRuntimeErrorNotification() is True

        assert notification.setDetRuntimeErrorNotification(False) == notification
        assert notification.getDetRuntimeErrorNotification() is False

    def test_set_det_transition_error_notification(self):
        root = EBModel.getInstance()
        notification = DetNotification(root, "DetNotification")

        assert notification.setDetTransitionErrorNotification(True) == notification
        assert notification.getDetTransitionErrorNotification() is True

        assert notification.setDetTransitionErrorNotification(False) == notification
        assert notification.getDetTransitionErrorNotification() is False


class TestDetDefensiveProgramming:

    def test_initialization(self):
        root = EBModel.getInstance()
        defensive_prog = DetDefensiveProgramming(root, "DetDefensiveProgramming")

        assert defensive_prog.getName() == "DetDefensiveProgramming"
        assert defensive_prog.getParent() == root
        assert defensive_prog.getDetNullPointerCheck() is None
        assert defensive_prog.getDetParameterCheck() is None

    def test_set_det_null_pointer_check(self):
        root = EBModel.getInstance()
        defensive_prog = DetDefensiveProgramming(root, "DetDefensiveProgramming")

        assert defensive_prog.setDetNullPointerCheck(True) == defensive_prog
        assert defensive_prog.getDetNullPointerCheck() is True

        assert defensive_prog.setDetNullPointerCheck(False) == defensive_prog
        assert defensive_prog.getDetNullPointerCheck() is False

    def test_set_det_parameter_check(self):
        root = EBModel.getInstance()
        defensive_prog = DetDefensiveProgramming(root, "DetDefensiveProgramming")

        assert defensive_prog.setDetParameterCheck(True) == defensive_prog
        assert defensive_prog.getDetParameterCheck() is True

        assert defensive_prog.setDetParameterCheck(False) == defensive_prog
        assert defensive_prog.getDetParameterCheck() is False


class TestSoftwareComponentList:

    def test_initialization(self):
        root = EBModel.getInstance()
        sw_comp_list = SoftwareComponentList(root, "SoftwareComponentList")

        assert sw_comp_list.getName() == "SoftwareComponentList"
        assert sw_comp_list.getParent() == root


class TestInstanceIdList:

    def test_initialization(self):
        root = EBModel.getInstance()
        instance_id_list = InstanceIdList(root, "InstanceIdList")

        assert instance_id_list.getName() == "InstanceIdList"
        assert instance_id_list.getParent() == root


class TestDetInitError:

    def test_initialization(self):
        root = EBModel.getInstance()
        init_error = DetInitError(root, "DetInitError")

        assert init_error.getName() == "DetInitError"
        assert init_error.getParent() == root
        assert init_error.getDetInitErrorRef() is None


class TestDet:

    def test_initialization(self):
        root = EBModel.getInstance()
        det = Det(root)

        assert det.getName() == "Det"
        assert det.getParent() == root
        assert det.getDetGeneral() is None
        assert det.getDetErrorHook() is None
        assert det.getDetInitError() is None
        assert det.getCommonPublishedInformation() is None
        assert det.getPublishedInformation() is None
        assert det.getDetServiceAPI() is None
        assert det.getDetNotification() is None
        assert det.getDetDefensiveProgramming() is None
        assert det.getSoftwareComponentList() is None
        assert det.getInstanceIdList() is None

    def test_set_det_general(self):
        root = EBModel.getInstance()
        det = Det(root)
        general = DetGeneral(root, "DetGeneral")

        assert det.setDetGeneral(general) == det
        assert det.getDetGeneral() == general

    def test_set_det_error_hook(self):
        root = EBModel.getInstance()
        det = Det(root)
        error_hook = DetErrorHook(root, "DetErrorHook")

        assert det.setDetErrorHook(error_hook) == det
        assert det.getDetErrorHook() == error_hook

    def test_set_det_init_error(self):
        root = EBModel.getInstance()
        det = Det(root)
        init_error = DetInitError(root, "DetInitError")

        assert det.setDetInitError(init_error) == det
        assert det.getDetInitError() == init_error

    def test_set_common_published_information(self):
        root = EBModel.getInstance()
        det = Det(root)
        common_info = CommonPublishedInformation(root, "CommonPublishedInformation")

        assert det.setCommonPublishedInformation(common_info) == det
        assert det.getCommonPublishedInformation() == common_info

    def test_set_published_information(self):
        root = EBModel.getInstance()
        det = Det(root)
        published_info = PublishedInformation(root, "PublishedInformation")

        assert det.setPublishedInformation(published_info) == det
        assert det.getPublishedInformation() == published_info

    def test_set_det_service_api(self):
        root = EBModel.getInstance()
        det = Det(root)
        service_api = DetServiceAPI(root, "DetServiceAPI")

        assert det.setDetServiceAPI(service_api) == det
        assert det.getDetServiceAPI() == service_api

    def test_set_det_notification(self):
        root = EBModel.getInstance()
        det = Det(root)
        notification = DetNotification(root, "DetNotification")

        assert det.setDetNotification(notification) == det
        assert det.getDetNotification() == notification

    def test_set_det_defensive_programming(self):
        root = EBModel.getInstance()
        det = Det(root)
        defensive_prog = DetDefensiveProgramming(root, "DetDefensiveProgramming")

        assert det.setDetDefensiveProgramming(defensive_prog) == det
        assert det.getDetDefensiveProgramming() == defensive_prog

    def test_set_software_component_list(self):
        root = EBModel.getInstance()
        det = Det(root)
        sw_comp_list = SoftwareComponentList(root, "SoftwareComponentList")

        assert det.setSoftwareComponentList(sw_comp_list) == det
        assert det.getSoftwareComponentList() == sw_comp_list

    def test_set_instance_id_list(self):
        root = EBModel.getInstance()
        det = Det(root)
        instance_id_list = InstanceIdList(root, "InstanceIdList")

        assert det.setInstanceIdList(instance_id_list) == det
        assert det.getInstanceIdList() == instance_id_list
