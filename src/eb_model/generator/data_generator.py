"""Generate model XDM data tree from schema model.

Implements: SWR_GEN_00004 (Data Generator)
"""

import xml.etree.ElementTree as ET
from typing import Optional

from .schema_model import (
    SchemaChc, SchemaCtr, SchemaLst, SchemaRef, SchemaRoot, SchemaVar,
)
from .strategies import DefaultsStrategy, CombinedStrategy


# Standard XDM namespaces
_XDM_NS = {
    '': 'http://www.tresos.de/_projects/DataModel2/16/root.xsd',
    'a': 'http://www.tresos.de/_projects/DataModel2/16/attribute.xsd',
    'v': 'http://www.tresos.de/_projects/DataModel2/06/schema.xsd',
    'd': 'http://www.tresos.de/_projects/DataModel2/06/data.xsd',
}


class DataGenerator:
    """Generate d: element tree from schema model."""

    def __init__(self, strategy=None, list_entries: Optional[int] = None) -> None:
        self.strategy = strategy or DefaultsStrategy()
        self.list_entries = list_entries
        self._ns_for_output = dict(_XDM_NS)

    def generate(self, schema_root: SchemaRoot) -> ET.ElementTree:
        """Generate a complete model XDM element tree from schema root."""
        ns = schema_root.namespaces or _XDM_NS

        d_ns = ns.get('d', '')
        d_prefix = '{%s}' % d_ns if d_ns else ''

        # Register d: prefix so ET uses it instead of auto-generated ns0
        if d_ns:
            ET.register_namespace('d', d_ns)
        # Register a: prefix for ENABLE attributes
        a_ns = ns.get('a', '')
        if a_ns:
            ET.register_namespace('a', a_ns)
        self._ns_for_output = dict(ns)

        # Build datamodel root
        datamodel = ET.Element('datamodel')
        datamodel.set('version', schema_root.version)

        # d:ctr AUTOSAR wrapper
        root_ctr = ET.SubElement(datamodel, '%sctr' % d_prefix)
        root_ctr.set('type', 'AUTOSAR')
        root_ctr.set('factory', 'autosar')

        # d:lst TOP-LEVEL-PACKAGES
        top_lst = ET.SubElement(root_ctr, '%slst' % d_prefix)
        top_lst.set('type', 'TOP-LEVEL-PACKAGES')

        # d:ctr AR-PACKAGE
        pkg_ctr = ET.SubElement(top_lst, '%sctr' % d_prefix)
        pkg_ctr.set('name', schema_root.module_name)
        pkg_ctr.set('type', 'AR-PACKAGE')

        # d:lst ELEMENTS
        elements_lst = ET.SubElement(pkg_ctr, '%slst' % d_prefix)
        elements_lst.set('type', 'ELEMENTS')

        # d:chc MODULE-CONFIGURATION
        chc = ET.SubElement(elements_lst, '%schc' % d_prefix)
        chc.set('name', schema_root.module_name)
        chc.set('type', 'AR-ELEMENT')
        chc.set('value', 'MODULE-CONFIGURATION')

        # d:ctr MODULE-CONFIGURATION
        mod_ctr = ET.SubElement(chc, '%sctr' % d_prefix)
        mod_ctr.set('type', 'MODULE-CONFIGURATION')

        # Generate content from schema
        if schema_root.module_def:
            self._generate_children(schema_root.module_def.children, mod_ctr, d_prefix)

        return ET.ElementTree(datamodel)

    def _generate_children(self, children, parent_elem, d_prefix: str) -> None:
        """Generate d: elements for schema children."""
        for child in children:
            if isinstance(child, SchemaVar):
                self._generate_var(child, parent_elem, d_prefix)
            elif isinstance(child, SchemaCtr):
                self._generate_ctr(child, parent_elem, d_prefix)
            elif isinstance(child, SchemaLst):
                self._generate_lst(child, parent_elem, d_prefix)
            elif isinstance(child, SchemaRef):
                self._generate_ref(child, parent_elem, d_prefix)
            elif isinstance(child, SchemaChc):
                self._generate_chc(child, parent_elem, d_prefix)

    def _generate_var(self, var: SchemaVar, parent: ET.Element, d_prefix: str) -> None:
        """Generate a d:var element."""
        elem = ET.SubElement(parent, '%svar' % d_prefix)
        elem.set('name', var.name)
        elem.set('type', var.var_type)
        value = self.strategy.generateValue(var)
        if value:
            elem.set('value', value)

        # For combined variant, add ENABLE attribute to ensure optional items are active
        if isinstance(self.strategy, CombinedStrategy):
            a_ns = self._ns_for_output.get('a', '')
            a_prefix = '{%s}' % a_ns if a_ns else ''
            enable = ET.SubElement(elem, '%sa' % a_prefix)
            enable.set('name', 'ENABLE')
            enable.set('value', 'true')

    def _generate_ctr(self, ctr: SchemaCtr, parent: ET.Element, d_prefix: str) -> None:
        """Generate a d:ctr element."""
        elem = ET.SubElement(parent, '%sctr' % d_prefix)
        elem.set('name', ctr.name)
        elem.set('type', ctr.ctr_type)
        self._generate_children(ctr.children, elem, d_prefix)

        # For combined variant, add ENABLE attribute to ensure optional items are active
        if isinstance(self.strategy, CombinedStrategy):
            a_ns = self._ns_for_output.get('a', '')
            a_prefix = '{%s}' % a_ns if a_ns else ''
            enable = ET.SubElement(elem, '%sa' % a_prefix)
            enable.set('name', 'ENABLE')
            enable.set('value', 'true')

    def _generate_lst(self, lst: SchemaLst, parent: ET.Element, d_prefix: str) -> None:
        """Generate a d:lst element with entries."""
        elem = ET.SubElement(parent, '%slst' % d_prefix)
        elem.set('name', lst.name)
        if lst.lst_type:
            elem.set('type', lst.lst_type)

        # Determine number of entries
        # If min_entries == 0: generate 2 entries (basic coverage)
        # If min_entries > 0: generate min_entries + 2 (verify multiplicity)
        # Cap at max_entries if set
        if lst.min_entries == 0:
            num_entries = 2
        else:
            num_entries = max(lst.min_entries + 2, 3)
        if lst.max_entries is not None:
            num_entries = min(num_entries, lst.max_entries)

        # Override if explicit list_entries specified
        if self.list_entries is not None:
            num_entries = min(self.list_entries, lst.max_entries or self.list_entries)

        # Generate entries
        if lst.child and num_entries > 0:
            for i in range(num_entries):
                name = '%s_%d' % (lst.child.name, i) if lst.name_pattern is None else lst.name_pattern.replace('?', str(i))
                if isinstance(lst.child, SchemaCtr):
                    entry = SchemaCtr(
                        name=name,
                        ctr_type=lst.child.ctr_type,
                        children=list(lst.child.children),
                        name_pattern=lst.child.name_pattern,
                    )
                    self._generate_ctr(entry, elem, d_prefix)
                elif isinstance(lst.child, SchemaVar):
                    entry = SchemaVar(
                        name=name,
                        var_type=lst.child.var_type,
                        default=lst.child.default,
                        range_info=lst.child.range_info,
                    )
                    self._generate_var(entry, elem, d_prefix)
                elif isinstance(lst.child, SchemaRef):
                    entry = SchemaRef(
                        name=name,
                        ref_type=lst.child.ref_type,
                        ref_targets=list(lst.child.ref_targets),
                    )
                    self._generate_ref(entry, elem, d_prefix)

    def _generate_ref(self, ref: SchemaRef, parent: ET.Element, d_prefix: str) -> None:
        """Generate a d:ref element."""
        elem = ET.SubElement(parent, '%sref' % d_prefix)
        elem.set('name', ref.name)
        elem.set('type', ref.ref_type)
        value = self.strategy.generateRefValue(ref)
        if value:
            elem.set('value', value)

        # For combined variant, add ENABLE attribute to ensure optional items are active
        if isinstance(self.strategy, CombinedStrategy):
            a_ns = self._ns_for_output.get('a', '')
            a_prefix = '{%s}' % a_ns if a_ns else ''
            enable = ET.SubElement(elem, '%sa' % a_prefix)
            enable.set('name', 'ENABLE')
            enable.set('value', 'true')

    def _generate_chc(self, chc: SchemaChc, parent: ET.Element, d_prefix: str) -> None:
        """Generate a d:chc element using first choice (or all for combined variant)."""
        # For combined variant, generate all choice options
        if isinstance(self.strategy, CombinedStrategy) and chc.choices:
            for choice in chc.choices:
                elem = ET.SubElement(parent, '%schc' % d_prefix)
                elem.set('name', chc.name)
                elem.set('type', chc.chc_type)
                self._generate_ctr(choice, elem, d_prefix)
        else:
            # Other variants: generate first choice only
            elem = ET.SubElement(parent, '%schc' % d_prefix)
            elem.set('name', chc.name)
            elem.set('type', chc.chc_type)

            if chc.choices:
                first = chc.choices[0]
                self._generate_ctr(first, elem, d_prefix)

    def toString(self, tree: ET.ElementTree) -> str:
        """Serialize element tree to XML string with proper namespace declarations."""
        ET.indent(tree, space='  ')
        root = tree.getroot()

        xml_bytes = ET.tostring(root, encoding='unicode', xml_declaration=False)

        # Build xmlns declarations for the root <datamodel> tag.
        # ET already emits xmlns:d and xmlns:a (registered prefixes), so skip them here.
        parts = []
        for prefix, uri in self._ns_for_output.items():
            if prefix in ('d', 'a'):
                continue
            if prefix:
                parts.append('xmlns:%s="%s"' % (prefix, uri))
            else:
                parts.append('xmlns="%s"' % uri)

        ns_decls = '\n           '.join(parts)
        xml_bytes = xml_bytes.replace(
            '<datamodel ',
            '<datamodel %s\n           ' % ns_decls,
            1,
        )

        return "<?xml version='1.0'?>\n" + xml_bytes
