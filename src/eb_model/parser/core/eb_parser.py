"""
Abstract Parser Module - Infrastructure for XDM parsing.

Implements: SWR_PARSER_00001 (Abstract Parser)
"""
import logging
import xml.etree.ElementTree as ET
import re

from abc import ABCMeta
from typing import List

from ...models.core.eb_doc import EBModel, PreferenceModel
from ...models.core.abstract import EcucRefType, Module


class AbstractEbModelParser(metaclass=ABCMeta):
    """
    Abstract base class for all EB Tresos XDM module parsers.

    Provides common XML parsing infrastructure including namespace handling,
    XPath queries, value reading, and reference extraction.

    Implements:
        - SWR_PARSER_00001: Abstract parser base class
        - SWR_PARSER_00002: Namespace handling
        - SWR_PARSER_00003: Value reading methods
        - SWR_PARSER_00004: Reference handling (ASPath format)
        - SWR_PARSER_00006: Container tag finding
    """

    # Pre-compiled regex for efficiency
    _ASPATH_PATTERN = re.compile(r'ASPath:(.*)')

    def __init__(self) -> None:
        """
        Initialize the parser with empty namespace map.

        Implements: SWR_PARSER_00001
        """
        self.nsmap = {}

        self.logger = logging.getLogger()

        if type(self) is AbstractEbModelParser:
            raise ValueError("Abstract EBModelParser cannot be initialized.")

    def validate_root(self, element: ET.Element):
        """
        Validate that the XML root element is a valid EB XDM datamodel.

        Implements: SWR_PARSER_00008 (Handle malformed XML gracefully)
        """
        if (element.tag != "{%s}%s" % (self.nsmap[''], "datamodel")):
            raise ValueError("This document <%s> is not EB xdm format" % element.tag)

    def read_version(self, parent: ET.Element, module: Module):
        """
        Read AR and SW version information from CommonPublishedInformation container.

        Implements: SWR_PARSER_00003 (Value reading)
        """
        ctr_tag = self.find_ctr_tag(parent, "CommonPublishedInformation")
        if ctr_tag is not None:
            ar_version = module.getArVersion()
            ar_version.setMajorVersion(self.read_value(ctr_tag, "ArMajorVersion"))
            ar_version.setMinorVersion(self.read_value(ctr_tag, "ArMinorVersion"))
            ar_version.setPatchVersion(self.read_value(ctr_tag, "ArPatchVersion"))

            sw_version = module.getSwVersion()
            sw_version.setMajorVersion(self.read_value(ctr_tag, "SwMajorVersion"))
            sw_version.setMinorVersion(self.read_value(ctr_tag, "SwMinorVersion"))
            sw_version.setPatchVersion(self.read_value(ctr_tag, "SwPatchVersion"))

    def read_ref_raw_value(self, value):
        """
        Extract the path from ASPath format reference.

        Internal method - use read_ref_value() instead.

        Implements: SWR_PARSER_00004 (Reference handling)
        """
        match = self._ASPATH_PATTERN.match(value)
        if match:
            return match.group(1)
        return value

    def _convert_value(self, tag: ET.Element):
        """
        Convert XML attribute value to appropriate Python type.

        Implements: SWR_PARSER_00003 (Value reading - type conversion)
        """
        if 'type' in tag.attrib:
            if (tag.attrib['type'] == 'INTEGER'):
                return int(tag.attrib['value'])
            elif (tag.attrib['type'] == "FLOAT"):
                return float(tag.attrib['value'])
            elif (tag.attrib['type'] == 'BOOLEAN'):
                if (tag.attrib['value'] == 'true'):
                    return True
                else:
                    return False
        if 'value' in tag.attrib:
            return tag.attrib['value']
        return None

    def read_value(self, parent: ET.Element, name: str) -> str:
        """
        Read a mandatory value from XML element.

        Raises KeyError if the value does not exist.

        Implements: SWR_PARSER_00003 (Value reading - mandatory values)
        """
        tag = parent.find(".//d:var[@name='%s']" % name, self.nsmap)
        if tag is None:
            raise KeyError("XPath d:var[@name='%s'] is invalid" % name)
        return self._convert_value(tag)
    
    def read_eb_origin_value(self, parent: ET.Element, name: str) -> str:
        tag = parent.find(".//d:var[@name='%s']" % name, self.nsmap)
        if tag is None:
            return None
        return self._convert_value(tag)

    def read_optional_value(self, parent: ET.Element, name: str, default_value=None) -> str:
        """
        Read an optional value from XML element with default fallback.

        Checks ENABLE attribute and returns default if disabled.

        Implements: SWR_PARSER_00003 (Value reading - optional values)
        """
        tag = parent.find(".//d:var[@name='%s']" % name, self.nsmap)
        if tag is None:
            return default_value
        if 'value' not in tag.attrib:
            return default_value
        enable = self.read_attrib(tag, 'ENABLE')
        if enable is not None and enable.upper() == "FALSE":
            return default_value
        return self._convert_value(tag)

    def find_choice_tag(self, parent: ET.Element, name: str) -> ET.Element:
        return parent.find(".//d:chc[@name='%s']" % name, self.nsmap)

    def read_choice_value(self, parent: ET.Element, name: str) -> str:
        """
        Read a mandatory choice value from XML element.

        Raises KeyError if the choice does not exist or has no value attribute.

        Implements: SWR_PARSER_00003 (Value reading - mandatory choice)
        """
        tag = self.find_choice_tag(parent, name)
        return tag.attrib['value']

    def read_optional_choice_value(self, parent: ET.Element, name: str, default_value=None) -> str:
        """
        Read an optional choice value from XML element with default fallback.

        Returns default_value if the choice tag doesn't exist or has no 'value' attribute.

        Implements: SWR_PARSER_00003 (Value reading - optional choice)
        """
        tag = self.find_choice_tag(parent, name)
        if tag is None:
            return default_value
        return tag.attrib.get('value', default_value)

    def read_ref_value(self, parent: ET.Element, name: str) -> EcucRefType:
        """
        Read a mandatory reference value in ASPath format.

        Implements: SWR_PARSER_00004 (Reference handling - single reference)
        """
        tag = parent.find(".//d:ref[@name='%s']" % name, self.nsmap)
        if tag is None:
            raise KeyError("XPath d:ref[@name='%s'] is invalid" % name)
        if 'value' in tag.attrib:
            return EcucRefType(self.read_ref_raw_value(tag.attrib['value']))
        return None

    def read_optional_ref_value(self, parent: ET.Element, name: str) -> EcucRefType:
        """
        Read an optional reference value in ASPath format.

        Implements: SWR_PARSER_00004 (Reference handling - optional reference)
        """
        tag = parent.find(".//d:ref[@name='%s']" % name, self.nsmap)
        if tag is None:
            return None
        if 'value' not in tag.attrib:
            return None
        enable = self.read_attrib(tag, 'ENABLE')
        if enable is not None and enable.upper() == "FALSE":
            return None

        return EcucRefType(self.read_ref_raw_value(tag.attrib['value']))

    def read_ref_value_list(self, parent: ET.Element, name: str) -> List[EcucRefType]:
        """
        Read a list of reference values in ASPath format.

        Implements: SWR_PARSER_00004 (Reference handling - multiple references)
        """
        ref_value_list = []
        for tag in parent.findall(".//d:lst[@name='%s']/d:ref" % name, self.nsmap):
            if 'value' not in tag.attrib:
                self.logger.warning("Reference tag <%s> does not have value attribute." % name)
                continue
            ref_value_list.append(EcucRefType(self.read_ref_raw_value(tag.attrib['value'])))
        return ref_value_list

    def find_ctr_tag_list(self, parent: ET.Element, name: str) -> List[ET.Element]:
        """
        Find all container tags with the given name.

        Implements: SWR_PARSER_00006 (Container tag finding - multiple)
        """
        return parent.findall(".//d:lst[@name='%s']/d:ctr" % name, self.nsmap)

    def find_chc_tag_list(self, parent: ET.Element, name: str) -> List[ET.Element]:
        """Find all choice tags with the given name."""
        return parent.findall(".//d:lst[@name='%s']/d:chc" % name, self.nsmap)

    def find_ctr_tag(self, parent: ET.Element, name: str) -> ET.Element:
        """
        Find a single container tag by name, checking ENABLE attribute.

        Returns None if not found or disabled.

        Implements: SWR_PARSER_00006 (Container tag finding - single)
        """
        tag = parent.find(".//d:ctr[@name='%s']" % name, self.nsmap)
        if tag is None:
            return None
        enable = self.read_attrib(tag, 'ENABLE')
        # ctr has the value if
        #   1. enable attribute do not exist
        #   2. enable attribute is not false
        if enable is not None and enable.upper() == "FALSE":
            return None
        return tag

    def create_ctr_tag(self, name: str, type: str) -> ET.Element:
        ctr_tag = ET.Element("d:ctr")
        ctr_tag.attrib['name'] = name
        ctr_tag.attrib['type'] = type
        return ctr_tag

    def create_ref_tag(self, name: str, type: str, value: str = "") -> ET.Element:
        ref_tag = ET.Element("d:ref")
        ref_tag.attrib['name'] = name
        ref_tag.attrib['type'] = type
        if (value != ""):
            ref_tag.attrib['value'] = "ASPath:%s" % value
        return ref_tag

    def create_choice_tag(self, name: str, type: str, value: str) -> ET.Element:
        choice_tag = ET.Element("d:chc")
        choice_tag.attrib['name'] = name
        choice_tag.attrib['type'] = type
        choice_tag.attrib['value'] = value
        return choice_tag

    def create_attrib_tag(self, name: str, value: str) -> ET.Element:
        attrib_tag = ET.Element("a:a")
        attrib_tag.attrib['name'] = name
        attrib_tag.attrib['value'] = value
        return attrib_tag

    def create_ref_lst_tag(self, name: str, type: str = "", ref_list: List[str] = []) -> ET.Element:
        lst_tag = ET.Element("d:lst")
        lst_tag.attrib['name'] = name
        for ref in ref_list:
            ref_tag = ET.Element("d:ref")
            ref_tag.attrib['type'] = type
            ref_tag.attrib['value'] = "ASPath:%s" % ref
            lst_tag.append(ref_tag)
        return lst_tag
    
    def get_component_name(self, parent: ET.Element) -> str:
        tag = parent.find(".//d:chc[@type='AR-ELEMENT'][@value='MODULE-CONFIGURATION']", self.nsmap)
        return tag.attrib['name']

    def find_lst_tag(self, parent: ET.Element, name: str) -> ET.Element:
        return parent.find(".//d:lst[@name='%s']" % name, self.nsmap)

    def read_attrib(self, parent: ET.Element, name: str) -> str:
        attrib_tag = parent.find("a:a[@name='%s']" % name, self.nsmap)
        if attrib_tag is None:
            return None
        return attrib_tag.attrib['value']

    def read_namespaces(self, xdm: str):
        """
        Extract XML namespaces from XDM file for XPath queries.

        Stores namespaces in self.nsmap with 'd' as default namespace prefix.

        Implements: SWR_PARSER_00002 (Namespace handling)
        """
        self.nsmap = dict([node for _, node in ET.iterparse(xdm, events=['start-ns'])])

    # def set_namespace(self, key: str, value: str):
    #    self.nsmap[key] = value

    def parse(self, element: ET.Element, doc: EBModel):
        """Parse XDM element and populate the document model. Override in subclasses."""
        pass

    def parse_preference(self, element: ET.Element, doc: PreferenceModel):
        """Parse preference XDM element. Override in subclasses."""
        pass

    def load_xdm(self, filename: str) -> ET.Element:
        """
        Load and validate an XDM file, returning the root element.

        Implements: SWR_PARSER_00007 (Process XDM files)
        """
        self.logger.info("Loading <%s>" % filename)

        self.read_namespaces(filename)
        tree = ET.parse(filename)
        self.root_tag = tree.getroot()
        self.validate_root(self.root_tag)

        return self.root_tag

    def parse_xdm(self, filename: str, doc: EBModel):
        root_tag = self.load_xdm(filename)
        self.parse(root_tag, doc)

    def parse_preference_xdm(self, filename: str, doc: EBModel):
        root_tag = self.load_xdm(filename)
        self.parse_preference(root_tag, doc)
