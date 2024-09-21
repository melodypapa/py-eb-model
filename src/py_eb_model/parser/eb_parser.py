#from xml.etree import cElementTree as ET
import xml.etree.ElementTree as ET
import re

from abc import ABCMeta
from typing import List

class EBModelParser(metaclass = ABCMeta):

    def __init__(self) -> None:
        self.ns = {}

        if type(self) == "EBModelParser":
            raise ValueError("Abstract EBModelParser cannot be initialized.")

    def validate_root(self, element: ET.Element):
        if (element.tag != "{%s}%s" % (self.ns[''], "datamodel")):
            raise ValueError("This document <%s> is not EB xdm format" % element.tag)

    def read_ref_raw_value(self, value):
        '''
            Internal function and please call _read_ref_value instead of it
        '''
        #match = re.match(r'ASPath.*\/(.*)', value)
        match = re.match(r'ASPath:(.*)', value)
        if (match):
            return match.group(1)
        return value

    def read_value(self, parent: ET.Element, name: str) -> str:
        tag = parent.find(".//d:var[@name='%s']" % name, self.ns)
        if tag == None:
            raise KeyError("XPath d:var[@name='%s'] is invalid" % name)
        if (tag.attrib['type'] == 'INTEGER'):
            return int(tag.attrib['value'])
        elif (tag.attrib['type'] == "FLOAT"):
            return float(tag.attrib['value'])
        elif (tag.attrib['type'] == 'BOOLEAN'):
            if (tag.attrib['value'] == 'true'):
                return True
            else:
                return False
        else:
            return tag.attrib['value']

    def read_optional_value(self, parent: ET.Element, name: str, default_value = None) -> str:
        tag = parent.find(".//d:var[@name='%s']" % name, self.ns)
        if tag is None:
            return default_value
        if ('value' not in tag.attrib):
            return default_value
        return tag.attrib['value']

    def find_choice_tag(self, parent: ET.Element, name: str) -> ET.Element:
        return parent.find(".//d:chc[@name='%s']" % name, self.ns)

    def read_choice_value(self, parent: ET.Element, name: str) -> str:
        tag = self.find_choice_tag(parent, name)
        return tag.attrib['value']

    def read_ref_value(self, parent: ET.Element, name: str) -> str:
        tag = parent.find(".//d:ref[@name='%s']" % name, self.ns)
        return self.read_ref_raw_value(tag.attrib['value'])

    def read_optional_ref_value(self, parent: ET.Element, name: str) -> str:
        tag = parent.find(".//d:ref[@name='%s']" % name, self.ns)
        enable = self.read_attrib(tag, 'ENABLE')
        if (enable == 'false'):
            return ""
        return self.read_ref_raw_value(tag.attrib['value'])

    def read_ref_value_list(self, parent: ET.Element, name: str) -> List[str]:
        ref_value_list = []
        for tag in parent.findall(".//d:lst[@name='%s']/d:ref" % name, self.ns):
            ref_value_list.append(
                self.read_ref_raw_value(tag.attrib['value']))
        return ref_value_list

    def find_ctr_tag_list(self, parent: ET.Element, name: str) -> List[ET.Element]:
        return parent.findall(".//d:lst[@name='%s']/d:ctr" % name, self.ns)
    
    def find_chc_tag_list(self, parent: ET.Element, name: str) -> List[ET.Element]:
        return parent.findall(".//d:lst[@name='%s']/d:chc" % name, self.ns)

    def find_ctr_tag(self, parent: ET.Element, name: str) -> ET.Element:
        '''
        Read the child ctr tag. 
        '''
        tag = parent.find(".//d:ctr[@name='%s']" % name, self.ns)
        if tag is None:
            return None
        enable = self.read_attrib(tag, 'ENABLE')
        # ctr has the value if 
        #   1. enable attribute do not exist
        #   2. enable attribute is not false
        if enable is not None and enable == "false":    
            return None
        return tag

    def create_ctr_tag(self, name: str, type: str)-> ET.Element:
        ctr_tag = ET.Element("d:ctr")
        ctr_tag.attrib['name'] = name
        ctr_tag.attrib['type'] = type
        return ctr_tag

    def create_ref_tag(self, name:str, type: str, value = "")-> ET.Element:
        ref_tag = ET.Element("d:ref")
        ref_tag.attrib['name'] = name
        ref_tag.attrib['type'] = type
        if (value != ""):
            ref_tag.attrib['value'] = "ASPath:%s" % value
        return ref_tag

    def create_choice_tag(self, name:str, type:str, value: str)-> ET.Element:
        choice_tag = ET.Element("d:chc")
        choice_tag.attrib['name'] = name
        choice_tag.attrib['type'] = type
        choice_tag.attrib['value'] = value
        return choice_tag

    def create_attrib_tag(self, name:str, value: str) -> ET.Element:
        attrib_tag = ET.Element("a:a")
        attrib_tag.attrib['name'] = name
        attrib_tag.attrib['value'] = value
        return attrib_tag

    def create_ref_lst_tag(self, name:str, type:str = "", ref_list: List[str] = []) -> ET.Element:
        lst_tag = ET.Element("d:lst")
        lst_tag.attrib['name'] = name
        for ref in ref_list:
            ref_tag = ET.Element("d:ref")
            ref_tag.attrib['type'] = type
            ref_tag.attrib['value'] = "ASPath:%s" % ref
            lst_tag.append(ref_tag)
        return lst_tag

    def find_lst_tag(self, parent: ET.Element, name: str) -> ET.Element:
        return parent.find(".//d:lst[@name='%s']" % name, self.ns)

    def read_attrib(self, parent: ET.Element, name: str) -> str:
        attrib_tag = parent.find(".//a:a[@name='%s']" % name, self.ns)
        if attrib_tag is None:
            return None
        return attrib_tag.attrib['value']

    def _read_namespaces(self, xdm: str):
        self.ns = dict([node for _, node in ET.iterparse(xdm, events=['start-ns'])])
