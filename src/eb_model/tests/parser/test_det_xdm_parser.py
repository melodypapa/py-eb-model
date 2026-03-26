from ...parser.det_xdm_parser import DetXdmParser
from ...models.det_xdm import DetGeneral, DetErrorHook
from ...models.eb_doc import EBModel

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
