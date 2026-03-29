from ....parser.memif_xdm_parser import MemIfXdmParser
from ....models.mem_stack.memif_xdm import MemIf, MemIfInit
from ....models.core.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestMemIfXdmParser:
    def test_read_memif_init(self):

        model = EBModel.getInstance()
        memif = model.getMemIf()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="MemIfInit" type="IDENTIFIABLE">
                <d:var name="MemIfDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="MemIfIndex" type="INTEGER" value="1"/>
                <d:var name="MemIfJobPriority" type="ENUMERATION" value="MEMIF_JOB_PRIORITY_LOW"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = MemIfXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_memif_init(element, memif)

        init = memif.getMemIfInit()
        assert init is not None
        assert init.getMemIfDevErrorDetect() is True
        assert init.getMemIfIndex() == 1
        assert init.getMemIfJobPriority() == "MEMIF_JOB_PRIORITY_LOW"