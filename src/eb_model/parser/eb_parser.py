import logging
import xml.etree.ElementTree as ET
import re

from abc import ABCMeta
from typing import List

from ..models.eb_doc import EBModel, PreferenceModel
from ..models.abstract import EcucRefType, Module


class AbstractEbModelParser(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.nsmap = {}

        self.logger = logging.getLogger()

        if type(self) is AbstractEbModelParser:
            raise ValueError("Abstract EBModelParser cannot be initialized.")
        
    def validate_root(self, element: ET.Element):
        if (element.tag != "{%s}%s" % (self.nsmap[''], "datamodel")):
            raise ValueError("This document <%s> is not EB xdm format" % element.tag)
        
    def read_version(self, parent: ET.Element, module: Module):
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
        '''
            Internal function and please call _read_ref_value instead of it
        '''
        match = re.match(r'ASPath:(.*)', value)
        if (match):
            return match.group(1)
        return value

    def _convert_value(self, tag: ET.Element):
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
        return tag.attrib['value']

    def read_value(self, parent: ET.Element, name: str) -> str:
        tag = parent.find(".//d:var[@name='%s']" % name, self.nsmap)
        if tag is None:
            raise KeyError("XPath d:var[@name='%s'] is invalid" % name)
        return self._convert_value(tag)

    def read_optional_value(self, parent: ET.Element, name: str, default_value=None) -> str:
        tag = parent.find(".//d:var[@name='%s']" % name, self.nsmap)
        if tag is None:
            return default_value
        if 'value' not in tag.attrib:
            return default_value
        enable = self.read_attrib(tag, 'ENABLE')
        if enable is None:
            return default_value
        if enable.upper() == "FALSE":
            return default_value
        return self._convert_value(tag)

    def find_choice_tag(self, parent: ET.Element, name: str) -> ET.Element:
        return parent.find(".//d:chc[@name='%s']" % name, self.nsmap)

    def read_choice_value(self, parent: ET.Element, name: str) -> str:
        tag = self.find_choice_tag(parent, name)
        return tag.attrib['value']

    def read_ref_value(self, parent: ET.Element, name: str) -> EcucRefType:
        tag = parent.find(".//d:ref[@name='%s']" % name, self.nsmap)
        if tag is None:
            raise KeyError("XPath d:ref[@name='%s'] is invalid" % name)
        if 'value' in tag.attrib:
            return EcucRefType(self.read_ref_raw_value(tag.attrib['value']))
        return None

    def read_optional_ref_value(self, parent: ET.Element, name: str) -> EcucRefType:
        tag = parent.find(".//d:ref[@name='%s']" % name, self.nsmap)
        enable = self.read_attrib(tag, 'ENABLE')
        if enable is None:
            return None
        if enable.upper() == "FALSE":
            return None
        
        return EcucRefType(self.read_ref_raw_value(tag.attrib['value']))

    def read_ref_value_list(self, parent: ET.Element, name: str) -> List[EcucRefType]:
        ref_value_list = []
        for tag in parent.findall(".//d:lst[@name='%s']/d:ref" % name, self.nsmap):
            ref_value_list.append(EcucRefType(self.read_ref_raw_value(tag.attrib['value'])))
        return ref_value_list
    
    def find_ctr_tag_list(self, parent: ET.Element, name: str) -> List[ET.Element]:
        return parent.findall(".//d:lst[@name='%s']/d:ctr" % name, self.nsmap)
    
    def find_chc_tag_list(self, parent: ET.Element, name: str) -> List[ET.Element]:
        return parent.findall(".//d:lst[@name='%s']/d:chc" % name, self.nsmap)

    def find_ctr_tag(self, parent: ET.Element, name: str) -> ET.Element:
        '''
        Read the child ctr tag.
        '''
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
        attrib_tag = parent.find(".//a:a[@name='%s']" % name, self.nsmap)
        if attrib_tag is None:
            return None
        return attrib_tag.attrib['value']

    def read_namespaces(self, xdm: str):
        self.nsmap = dict([node for _, node in ET.iterparse(xdm, events=['start-ns'])])

    def parse(self, element: ET.Element, doc: EBModel):
        pass

    def parse_preference(self, element: ET.Element, doc: PreferenceModel):
        pass

    def load_xdm(self, filename: str) -> ET.Element:
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
