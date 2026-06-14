"""Parser for XDM schema files (v: prefix nodes).

Reads schema XDM and builds SchemaModel tree.

Implements: SWR_GEN_00002 (Schema Parser)
"""

import logging
import re
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional

from .schema_model import (
    SchemaChc, SchemaCtr, SchemaLst, SchemaRange, SchemaRef, SchemaRoot, SchemaVar,
)


logger = logging.getLogger(__name__)


class SchemaParser:
    """Parse XDM schema files into schema model objects."""

    def __init__(self) -> None:
        self.nsmap: Dict[str, str] = {}

    def parse(self, root_element: ET.Element) -> SchemaRoot:
        """Parse a schema XDM root element into a SchemaRoot model."""
        self._extract_namespaces(root_element)

        version = root_element.get('version', '7.0')

        xpath_d = self._xpath_d
        xpath_v = self._xpath_v

        top_lst = root_element.find('.//%slst[@type="TOP-LEVEL-PACKAGES"]' % xpath_d)
        if top_lst is None:
            raise ValueError("Cannot find TOP-LEVEL-PACKAGES in schema XDM")

        ar_pkg = top_lst.find('%sctr[@type="AR-PACKAGE"]' % xpath_d)
        if ar_pkg is None:
            raise ValueError("Cannot find AR-PACKAGE in schema XDM")

        ar_pkg_name = ar_pkg.get('name', '')
        elements_lst = ar_pkg.find('%slst[@type="ELEMENTS"]' % xpath_d)
        if elements_lst is None:
            raise ValueError("Cannot find ELEMENTS list in schema XDM")

        chc = elements_lst.find('%schc' % xpath_d)
        if chc is None:
            raise ValueError("Cannot find choice element in schema XDM")

        module_name = chc.get('name', 'Unknown')
        module_def_elem = chc.find('%sctr[@type="MODULE-DEF"]' % xpath_v)
        if module_def_elem is None:
            raise ValueError("Cannot find MODULE-DEF in schema XDM")

        module_def = self._parse_ctr(module_def_elem)

        return SchemaRoot(
            module_name=module_name,
            module_def=module_def,
            version=version,
            namespaces=dict(self.nsmap),
            ar_package_name=ar_pkg_name,
        )

    def _extract_namespaces(self, element: ET.Element) -> None:
        """Extract namespace mappings from element tree."""
        nsmap = {}

        # Check root element for default namespace
        tag = element.tag
        if tag.startswith('{'):
            nsmap[''] = tag[1:tag.index('}')]

        # Scan all elements for d:, v:, a: namespaces
        for elem in element.iter():
            tag = elem.tag
            if tag.startswith('{'):
                uri = tag[1:tag.index('}')]
                if 'data.xsd' in uri:
                    nsmap['d'] = uri
                elif 'schema.xsd' in uri:
                    nsmap['v'] = uri
                elif 'attribute.xsd' in uri:
                    nsmap['a'] = uri
                elif 'root.xsd' in uri and '' not in nsmap:
                    nsmap[''] = uri

            # Also check attributes for a: namespace
            for attr_name in elem.attrib:
                if attr_name.startswith('{'):
                    uri = attr_name[1:attr_name.index('}')]
                    if 'attribute.xsd' in uri:
                        nsmap['a'] = uri

        self.nsmap = nsmap

    @property
    def _xpath_d(self) -> str:
        """XPath prefix for data nodes (d:)."""
        uri = self.nsmap.get('d', '')
        if uri:
            return '{%s}' % uri
        return ''

    @property
    def _xpath_v(self) -> str:
        """XPath prefix for schema nodes (v:)."""
        uri = self.nsmap.get('v', '')
        if uri:
            return '{%s}' % uri
        return ''

    @property
    def _xpath_a(self) -> str:
        """XPath prefix for attribute nodes (a:)."""
        uri = self.nsmap.get('a', '')
        if uri:
            return '{%s}' % uri
        return ''

    def _parse_ctr(self, element: ET.Element) -> SchemaCtr:
        """Parse a v:ctr element into SchemaCtr."""
        name = element.get('name', '')
        ctr_type = element.get('type', 'IDENTIFIABLE')
        name_pattern = self._get_attribute_value(element, 'NAME_PATTERN')
        enabled = self._get_da_value(element, 'ENABLE')

        children = []
        for child in element:
            local_name = self._local_tag(child.tag)
            if local_name == 'var':
                children.append(self._parse_var(child))
            elif local_name == 'ctr':
                children.append(self._parse_ctr(child))
            elif local_name == 'lst':
                children.append(self._parse_lst(child))
            elif local_name == 'ref':
                children.append(self._parse_ref(child))
            elif local_name == 'chc':
                children.append(self._parse_chc(child))

        return SchemaCtr(
            name=name,
            ctr_type=ctr_type,
            children=children,
            name_pattern=name_pattern,
            enabled=enabled,
        )

    def _parse_var(self, element: ET.Element) -> SchemaVar:
        """Parse a v:var element into SchemaVar."""
        name = element.get('name', '')
        var_type = element.get('type', 'STRING')
        default = self._get_da_value(element, 'DEFAULT')
        label = self._get_attribute_value(element, 'LABEL')
        enabled = self._get_da_value(element, 'ENABLE')
        range_info = self._parse_range(element)

        return SchemaVar(
            name=name,
            var_type=var_type,
            default=default,
            range_info=range_info,
            label=label,
            enabled=enabled,
        )

    def _parse_lst(self, element: ET.Element) -> SchemaLst:
        """Parse a v:lst element into SchemaLst."""
        name = element.get('name', '')
        lst_type = element.get('type', '')
        name_pattern = self._get_attribute_value(element, 'NAME_PATTERN')

        min_entries = 0
        min_val = self._get_da_value(element, 'MIN')
        if min_val is not None:
            min_entries = int(min_val)

        max_entries = None
        max_val = self._get_da_value(element, 'MAX')
        if max_val is not None:
            max_entries = int(max_val)

        # Parse child schema (first v: node child)
        child = None
        xpath_v = self._xpath_v
        for child_tag in ['ctr', 'var', 'ref']:
            child_elem = element.find('%s%s' % (xpath_v, child_tag))
            if child_elem is not None:
                if child_tag == 'ctr':
                    child = self._parse_ctr(child_elem)
                elif child_tag == 'var':
                    child = self._parse_var(child_elem)
                elif child_tag == 'ref':
                    child = self._parse_ref(child_elem)
                break

        return SchemaLst(
            name=name,
            lst_type=lst_type,
            min_entries=min_entries,
            max_entries=max_entries,
            child=child,
            name_pattern=name_pattern,
        )

    def _parse_ref(self, element: ET.Element) -> SchemaRef:
        """Parse a v:ref element into SchemaRef."""
        name = element.get('name', '')
        ref_type = element.get('type', 'REFERENCE')
        enabled = self._get_da_value(element, 'ENABLE')

        ref_targets = []
        range_targets = []

        ref_val = self._get_da_value(element, 'REF')
        if ref_val:
            ref_targets = [v.strip() for v in ref_val.split() if v.strip()]

        range_info = self._parse_da_multi_value(element, 'RANGE')
        if range_info:
            range_targets = range_info

        return SchemaRef(
            name=name,
            ref_type=ref_type,
            ref_targets=ref_targets,
            range_targets=range_targets,
            enabled=enabled,
        )

    def _parse_chc(self, element: ET.Element) -> SchemaChc:
        """Parse a v:chc element into SchemaChc."""
        name = element.get('name', '')
        chc_type = element.get('type', 'IDENTIFIABLE')

        choices = []
        xpath_v = self._xpath_v
        for ctr_elem in element.findall('%sctr' % xpath_v):
            choices.append(self._parse_ctr(ctr_elem))

        return SchemaChc(
            name=name,
            chc_type=chc_type,
            choices=choices,
        )

    def _parse_range(self, element: ET.Element) -> Optional[SchemaRange]:
        """Parse RANGE data attribute from a v:var element."""
        range_values = self._parse_da_multi_value(element, 'RANGE')
        if not range_values:
            range_val = self._get_da_value(element, 'RANGE')
            if range_val is None:
                return None
            range_values = [range_val]

        if len(range_values) == 1:
            val = range_values[0]
            if val.startswith('~'):
                return SchemaRange(regex_pattern=val[1:])
            parsed = self._parse_numeric_range(val)
            if parsed:
                return parsed
            return SchemaRange(enum_values=[val])

        return SchemaRange(enum_values=range_values)

    def _parse_numeric_range(self, val: str) -> Optional[SchemaRange]:
        """Parse a numeric range string like '0-255'."""
        range_pattern = re.compile(r'^(-?\d+)\s*-\s*(-?\d+)$')
        m = range_pattern.match(val)
        if m:
            return SchemaRange(min_value=float(m.group(1)), max_value=float(m.group(2)))
        return None

    def _get_da_value(self, element: ET.Element, attr_name: str) -> Optional[str]:
        """Get a:da value by name from element's direct children."""
        xpath_a = self._xpath_a
        for da in element.findall('%sda' % xpath_a):
            if da.get('name') == attr_name:
                return da.get('value')
        return None

    def _get_attribute_value(self, element: ET.Element, attr_name: str) -> Optional[str]:
        """Get a:a value by name from element's direct children."""
        xpath_a = self._xpath_a
        for a_elem in element.findall('%sa' % xpath_a):
            if a_elem.get('name') == attr_name:
                return a_elem.get('value')
        return None

    def _parse_da_multi_value(self, element: ET.Element, attr_name: str) -> List[str]:
        """Parse a:da with multiple a:v children."""
        xpath_a = self._xpath_a
        values = []
        for da in element.findall('%sda' % xpath_a):
            if da.get('name') == attr_name:
                direct = da.get('value')
                if direct:
                    values.append(direct)
                for v_elem in da.findall('%sv' % xpath_a):
                    v_text = v_elem.text
                    if v_text:
                        values.append(v_text.strip())
        return values

    @staticmethod
    def _local_tag(tag: str) -> str:
        """Extract local tag name from Clark notation {uri}localname."""
        if tag.startswith('{'):
            return tag[tag.index('}') + 1:]
        return tag
