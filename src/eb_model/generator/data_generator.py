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

# Schema/data attribute names and special values (avoid typo-driven divergence)
_ATTR_ENABLE = 'ENABLE'
_ATTR_DERIVED = 'DERIVED'
_ATTR_TARGET = 'TARGET'
_ATTR_CONTEXT = 'CONTEXT'
_VALUE_TRUE = 'true'
_CTR_MULTI_CONFIG = 'MULTIPLE-CONFIGURATION-CONTAINER'
_CTR_INSTANCE = 'INSTANCE'
_CHC_CHOICE = 'CHOICE'
_CHC_IDENTIFIABLE = 'IDENTIFIABLE'
_NS_LEGACY_VERSION = 'DataModel2/08/'


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
            # Multiplicity auto-wrap rule (XDM Spec 5.2.5): any element with
            # LOWER-MULTIPLICITY != 1 or UPPER-MULTIPLICITY != 1 is wrapped in d:lst.
            if not isinstance(child, SchemaLst) and self._needs_multiplicity_wrap(child):
                self._generate_wrapped(child, parent_elem, d_prefix)
                continue
            if isinstance(child, SchemaVar):
                self._generate_var(child, parent_elem, d_prefix)
            elif isinstance(child, SchemaCtr):
                # Standalone MULTI-CONFIG-CONTAINER is always wrapped in d:lst (XDM Spec 5.2.5)
                if child.ctr_type == _CTR_MULTI_CONFIG:
                    wrap_lst = ET.SubElement(parent_elem, '%slst' % d_prefix)
                    wrap_lst.set('name', child.name)
                    self._generate_ctr(child, wrap_lst, d_prefix)
                else:
                    self._generate_ctr(child, parent_elem, d_prefix)
            elif isinstance(child, SchemaLst):
                self._generate_lst(child, parent_elem, d_prefix)
            elif isinstance(child, SchemaRef):
                self._generate_ref(child, parent_elem, d_prefix)
            elif isinstance(child, SchemaChc):
                self._generate_chc(child, parent_elem, d_prefix)

    @staticmethod
    def _needs_multiplicity_wrap(child) -> bool:
        """Check if a non-lst child has multiplicity requiring d:lst wrap."""
        lower = getattr(child, 'lower_multiplicity', None)
        upper = getattr(child, 'upper_multiplicity', None)
        if lower is not None and lower != 1:
            return True
        if upper is not None and upper != 1:
            return True
        return False

    def _generate_wrapped(self, child, parent_elem, d_prefix: str) -> None:
        """Wrap a non-lst child in synthetic SchemaLst and emit via _generate_lst."""
        synth_lst = SchemaLst(
            name=child.name,
            lst_type="MAP",
            min_entries=getattr(child, 'lower_multiplicity', None) or 0,
            max_entries=getattr(child, 'upper_multiplicity', None),
            child=child,
        )
        self._generate_lst(synth_lst, parent_elem, d_prefix)

    def _generate_var(self, var: SchemaVar, parent: ET.Element, d_prefix: str) -> None:
        """Generate a d:var element."""
        elem = ET.SubElement(parent, '%svar' % d_prefix)
        elem.set('name', var.name)
        elem.set('type', var.var_type)
        value = self.strategy.generateValue(var)
        if value:
            elem.set('value', value)

        if var.derived:
            self._emit_attr(elem, 'a', _ATTR_DERIVED, var.derived)

        # Combined variant activates optional elements via ENABLE=true (XDM Spec 5.2.5.1)
        if isinstance(self.strategy, CombinedStrategy) and var.optional == _VALUE_TRUE:
            self._emit_attr(elem, 'a', _ATTR_ENABLE, _VALUE_TRUE)

    def _emit_attr(self, parent: ET.Element, tag: str, name: str, value: str) -> None:
        """Emit <a:{tag} name=... value=.../> as child of parent. tag is 'a' or 'da'."""
        a_ns = self._ns_for_output.get('a', '')
        a_prefix = '{%s}' % a_ns if a_ns else ''
        attr = ET.SubElement(parent, '%s%s' % (a_prefix, tag))
        attr.set('name', name)
        attr.set('value', value)

    def _generate_ctr(self, ctr: SchemaCtr, parent: ET.Element, d_prefix: str) -> None:
        """Generate a d:ctr element."""
        elem = ET.SubElement(parent, '%sctr' % d_prefix)
        elem.set('name', ctr.name)
        elem.set('type', ctr.ctr_type)
        # INSTANCE containers carry TARGET/CONTEXT data attributes (XDM Spec 5.2.1.6.1)
        if ctr.ctr_type == _CTR_INSTANCE:
            if ctr.target:
                self._emit_attr(elem, 'da', _ATTR_TARGET, ctr.target)
            if ctr.context:
                self._emit_attr(elem, 'da', _ATTR_CONTEXT, ctr.context)
        self._generate_children(ctr.children, elem, d_prefix)

        # Combined variant activates optional elements via ENABLE=true (XDM Spec 5.2.5.1)
        if isinstance(self.strategy, CombinedStrategy) and ctr.optional == _VALUE_TRUE:
            self._emit_attr(elem, 'a', _ATTR_ENABLE, _VALUE_TRUE)

    def _generate_lst(self, lst: SchemaLst, parent: ET.Element, d_prefix: str) -> None:
        """Generate a d:lst element with entries."""
        elem = ET.SubElement(parent, '%slst' % d_prefix)
        elem.set('name', lst.name)
        if lst.lst_type:
            elem.set('type', lst.lst_type)

        # Optional element old-style representation: list with MIN=0, MAX=1 (XDM Spec 5.2.5.1)
        is_optional = lst.min_entries == 0 and lst.max_entries == 1
        entry_optional = None
        if is_optional:
            if isinstance(self.strategy, CombinedStrategy):
                num_entries = 1
                entry_optional = _VALUE_TRUE
            else:
                # Non-combined: optional stays inactive by default
                num_entries = 0
        elif lst.min_entries == 0:
            # Non-optional list with min=0: generate 2 entries (basic coverage)
            num_entries = 2
        else:
            # min>0: generate min+2 (verify multiplicity), at least 3
            num_entries = max(lst.min_entries + 2, 3)
        if lst.max_entries is not None and not is_optional:
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
                        optional=entry_optional,
                    )
                    self._generate_ctr(entry, elem, d_prefix)
                elif isinstance(lst.child, SchemaVar):
                    entry = SchemaVar(
                        name=name,
                        var_type=lst.child.var_type,
                        default=lst.child.default,
                        range_info=lst.child.range_info,
                        optional=entry_optional,
                    )
                    self._generate_var(entry, elem, d_prefix)
                elif isinstance(lst.child, SchemaRef):
                    entry = SchemaRef(
                        name=name,
                        ref_type=lst.child.ref_type,
                        ref_targets=list(lst.child.ref_targets),
                        optional=entry_optional,
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

        # Combined variant activates optional elements via ENABLE=true (XDM Spec 5.2.5.1)
        if isinstance(self.strategy, CombinedStrategy) and ref.optional == _VALUE_TRUE:
            self._emit_attr(elem, 'a', _ATTR_ENABLE, _VALUE_TRUE)

    def _generate_chc(self, chc: SchemaChc, parent: ET.Element, d_prefix: str) -> None:
        """Generate a d:chc element using first choice (or all for combined variant)."""
        # Determine chc type, falling back to AUTOSAR-version-aware default if missing
        chc_type = chc.chc_type or self._chc_default_type()

        # For combined variant, generate all choice options
        if isinstance(self.strategy, CombinedStrategy) and chc.choices:
            for choice in chc.choices:
                elem = ET.SubElement(parent, '%schc' % d_prefix)
                elem.set('name', chc.name)
                elem.set('type', chc_type)
                elem.set('value', choice.name)
                self._generate_ctr(choice, elem, d_prefix)
        else:
            # Other variants: generate first choice only
            elem = ET.SubElement(parent, '%schc' % d_prefix)
            elem.set('name', chc.name)
            elem.set('type', chc_type)

            if chc.choices:
                first = chc.choices[0]
                elem.set('value', first.name)
                self._generate_ctr(first, elem, d_prefix)

    def _chc_default_type(self) -> str:
        """Return default chc type based on schema namespace version (XDM Spec 5.2.6).

        DataModel2/08 namespaces → AUTOSAR 2.x style → 'CHOICE'.
        DataModel2/16 (or unknown) → AUTOSAR 3.x+ → 'IDENTIFIABLE'.
        """
        for uri in self._ns_for_output.values():
            if _NS_LEGACY_VERSION in uri:
                return _CHC_CHOICE
        return _CHC_IDENTIFIABLE

    def toString(self, tree: ET.ElementTree) -> str:
        """Serialize element tree to XML string with proper namespace declarations."""
        ET.indent(tree, space='  ')
        root = tree.getroot()

        xml_bytes = ET.tostring(root, encoding='unicode', xml_declaration=False)

        # Build xmlns declarations for the root <datamodel> tag.
        # ET already emits xmlns:d (registered prefix), so skip it here.
        # Always emit xmlns:a even if unused - parser may need it for ENABLE attribute lookups.
        parts = []
        for prefix, uri in self._ns_for_output.items():
            if prefix == 'd':
                continue
            # Skip if this xmlns already exists in the output (ET may have added it)
            decl = 'xmlns:%s="%s"' % (prefix, uri) if prefix else 'xmlns="%s"' % uri
            if decl not in xml_bytes:
                parts.append(decl)

        ns_decls = '\n           '.join(parts)
        xml_bytes = xml_bytes.replace(
            '<datamodel ',
            '<datamodel %s\n           ' % ns_decls,
            1,
        )

        return "<?xml version='1.0'?>\n" + xml_bytes
