from ...parser.det_xdm_parser import DetXdmParser
from ...models.core.det_xdm import DetGeneral, DetErrorHook
from ...models.core.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestDetXdmParser:
    def test_read_det_general(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="DetGeneral" type="IDENTIFIABLE">
                <d:var name="DetDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="DetEnabled" type="BOOLEAN" value="true"/>
                <d:var name="DetForwardToDlt" type="BOOLEAN" value="true"/>
                <d:var name="DetVersionInfoApi" type="BOOLEAN" value="true"/>
                <d:var name="LoggingMode" type="ENUMERATION" value="BUFFERED"/>
                <d:var name="BufferSize" type="INTEGER" value="256"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock Det object
        model = EBModel.getInstance()
        det = model.getDet()

        # Create parser instance
        parser = DetXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_det_general(element, det)

        # Assertions
        general = det.getDetGeneral()
        assert general is not None
        assert general.getDetDevErrorDetect() is True
        assert general.getDetEnabled() is True
        assert general.getDetForwardToDlt() is True
        assert general.getDetVersionInfoApi() is True
        assert general.getLoggingMode() == "BUFFERED"
        assert general.getBufferSize() == 256

    def test_read_det_error_hook(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="DetErrorHook" type="IDENTIFIABLE">
                <d:var name="DetErrorHookCallbackName" type="STRING" value="Det_ErrorHook"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock Det object
        model = EBModel.getInstance()
        det = model.getDet()

        # Create parser instance
        parser = DetXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_det_error_hook(element, det)

        # Assertions
        error_hook = det.getDetErrorHook()
        assert error_hook is not None
        assert error_hook.getDetErrorHookCallbackName() == "Det_ErrorHook"

    def test_read_det_init_error(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="DetInitError" type="IDENTIFIABLE">
                <d:ref name="DetInitErrorRef" type="REFERENCE" value="ASPath:/Os/Os/InitError"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock Det object
        model = EBModel.getInstance()
        det = model.getDet()

        # Create parser instance
        parser = DetXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_det_init_error(element, det)

        # Assertions
        init_error = det.getDetInitError()
        assert init_error is not None
        assert init_error.getDetInitErrorRef().getValue() == "/Os/Os/InitError"

    def test_read_common_published_information(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CommonPublishedInformation" type="IDENTIFIABLE">
                <d:var name="ArMajorVersion" type="INTEGER" value="4"/>
                <d:var name="ArMinorVersion" type="INTEGER" value="3"/>
                <d:var name="ArPatchVersion" type="INTEGER" value="0"/>
                <d:var name="SwMajorVersion" type="INTEGER" value="1"/>
                <d:var name="SwMinorVersion" type="INTEGER" value="0"/>
                <d:var name="SwPatchVersion" type="INTEGER" value="0"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        det = model.getDet()

        parser = DetXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_common_published_information(element, det)

        pub_info = det.getCommonPublishedInformation()
        assert pub_info is not None
        assert pub_info.getArMajorVersion() == 4
        assert pub_info.getArMinorVersion() == 3

    def test_read_published_information(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="PublishedInformation" type="IDENTIFIABLE">
                <d:var name="VendorId" type="STRING" value="Vector"/>
                <d:var name="ArReleaseMajorVersion" type="STRING" value="4"/>
                <d:var name="ArReleaseMinorVersion" type="STRING" value="3"/>
                <d:var name="ArReleasePatchVersion" type="STRING" value="0"/>
                <d:var name="SwMajorVersion" type="STRING" value="1"/>
                <d:var name="SwMinorVersion" type="STRING" value="0"/>
                <d:var name="SwPatchVersion" type="STRING" value="0"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        det = model.getDet()

        parser = DetXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_published_information(element, det)

        pub_info = det.getPublishedInformation()
        assert pub_info is not None
        assert pub_info.getVendorId() == "Vector"

    def test_read_det_service_api(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="DetServiceAPI" type="IDENTIFIABLE">
                <d:var name="DetVersionInfoApi" type="BOOLEAN" value="true"/>
                <d:var name="DetReportRuntimeErrorCallout" type="BOOLEAN" value="false"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        det = model.getDet()

        parser = DetXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_det_service_api(element, det)

        service_api = det.getDetServiceAPI()
        assert service_api is not None
        assert service_api.getDetVersionInfoApi() is True
        assert service_api.getDetReportRuntimeErrorCallout() is False

    def test_read_det_notification(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="DetNotification" type="IDENTIFIABLE">
                <d:var name="DetErrorNotification" type="BOOLEAN" value="true"/>
                <d:var name="DetRuntimeErrorNotification" type="BOOLEAN" value="true"/>
                <d:var name="DetTransitionErrorNotification" type="BOOLEAN" value="false"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        det = model.getDet()

        parser = DetXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_det_notification(element, det)

        notification = det.getDetNotification()
        assert notification is not None
        assert notification.getDetErrorNotification() is True
        assert notification.getDetRuntimeErrorNotification() is True
        assert notification.getDetTransitionErrorNotification() is False

    def test_read_det_defensive_programming(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="DetDefensiveProgramming" type="IDENTIFIABLE">
                <d:var name="DetNullPointerCheck" type="BOOLEAN" value="true"/>
                <d:var name="DetParameterCheck" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        det = model.getDet()

        parser = DetXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_det_defensive_programming(element, det)

        defensive = det.getDetDefensiveProgramming()
        assert defensive is not None
        assert defensive.getDetNullPointerCheck() is True
        assert defensive.getDetParameterCheck() is True

    def test_read_software_component_list(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="SoftwareComponentList" type="IDENTIFIABLE"/>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        det = model.getDet()

        parser = DetXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_software_component_list(element, det)

        sw_list = det.getSoftwareComponentList()
        assert sw_list is not None
        assert sw_list.getName() == "SoftwareComponentList"

    def test_read_instance_id_list(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="InstanceIdList" type="IDENTIFIABLE"/>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        det = model.getDet()

        parser = DetXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_instance_id_list(element, det)

        id_list = det.getInstanceIdList()
        assert id_list is not None
        assert id_list.getName() == "InstanceIdList"
