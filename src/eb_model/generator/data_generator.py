"""Generate model XDM data tree from schema model.

Implements: SWR_GEN_00004 (Data Generator)
"""

import xml.etree.ElementTree as ET
from typing import Dict, Optional

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

# Additional namespaces for AUTOSAR container element (authentic EB Tresos config format)
_AUTOSAR_NS = {
    'ad': 'http://www.tresos.de/_projects/DataModel2/08/admindata.xsd',
    'ce': 'http://www.tresos.de/_projects/DataModel2/18/childenable.xsd',
    'cd': 'http://www.tresos.de/_projects/DataModel2/08/customdata.xsd',
    'f': 'http://www.tresos.de/_projects/DataModel2/14/formulaexpr.xsd',
    'icc': 'http://www.tresos.de/_projects/DataModel2/08/implconfigclass.xsd',
    'mt': 'http://www.tresos.de/_projects/DataModel2/11/multitest.xsd',
    'variant': 'http://www.tresos.de/_projects/DataModel2/11/variant.xsd',
}

# Schema/data attribute names and special values (avoid typo-driven divergence)
_ATTR_ENABLE = 'ENABLE'
_ATTR_DERIVED = 'DERIVED'
_ATTR_TARGET = 'TARGET'
_ATTR_CONTEXT = 'CONTEXT'
_ATTR_IMPORTER_INFO = 'IMPORTER_INFO'
_VALUE_TRUE = 'true'
_VALUE_DEF = '@DEF'
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
        # Schema-source namespaces kept for AUTOSAR-version-aware logic (e.g. chc
        # default type). Independent of output namespaces, which are always v16.
        # See docs/usage/model-xdm-generator.md "Schema Version and Namespaces".
        self._ns_for_schema_source: Dict[str, str] = {}

    def generate(self, schema_root: SchemaRoot) -> ET.ElementTree:
        """Generate a complete model XDM element tree from schema root."""
        # Output always declares the DataModel2/16 namespace set and version 7.0,
        # regardless of what the schema source declares. Authentic EB Tresos
        # config files use this version set; matching it is required for output
        # to align with doc/config/* format.
        # See docs/usage/model-xdm-generator.md "Schema Version and Namespaces".
        ns = dict(_XDM_NS)
        self._ns_for_schema_source = dict(schema_root.namespaces or {})

        d_ns = ns.get('d', '')
        d_prefix = '{%s}' % d_ns if d_ns else ''

        # Register d: prefix so ET uses it instead of auto-generated ns0
        if d_ns:
            ET.register_namespace('d', d_ns)
        # Register a: prefix for ENABLE attributes
        a_ns = ns.get('a', '')
        if a_ns:
            ET.register_namespace('a', a_ns)
        # Register AUTOSAR-specific namespace prefixes
        for prefix, uri in _AUTOSAR_NS.items():
            ET.register_namespace(prefix, uri)
        self._ns_for_output = dict(ns)

        # Build datamodel root
        datamodel = ET.Element('datamodel')
        datamodel.set('version', '7.0')

        # d:ctr AUTOSAR wrapper
        root_ctr = ET.SubElement(datamodel, '%sctr' % d_prefix)
        root_ctr.set('type', 'AUTOSAR')
        root_ctr.set('factory', 'autosar')
        # Add AUTOSAR-specific namespace declarations (authentic EB Tresos config format)
        for prefix, uri in _AUTOSAR_NS.items():
            root_ctr.set('xmlns:%s' % prefix, uri)

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

        self._emit_enable_attribute(elem, var.optional)

        # IMPORTER_INFO=@DEF marks values pulled from schema DEFAULT. Authentic
        # config carries this attribute on defaulted elements. Emitted only when
        # value equals the schema-declared default — type-based fallback values
        # are not schema-declared so @DEF cannot be soundly claimed.
        # See docs/usage/model-xdm-generator.md "IMPORTER_INFO Emission".
        if var.default is not None and value == var.default:
            self._emit_attr(elem, 'a', _ATTR_IMPORTER_INFO, _VALUE_DEF)

    def _emit_enable_attribute(self, elem: ET.Element, optional: Optional[str]) -> None:
        """Emit ENABLE attribute for optional elements, matching authentic config style.

        - CombinedStrategy + optional → ENABLE=true (element activated)
        - Other strategies + optional → ENABLE=false (element inactive but present)
        - Non-optional → no ENABLE attribute

        Always uses <a:a> tag in output, never <a:da> (which is schema-side only).
        See docs/usage/model-xdm-generator.md "Optional Elements".
        """
        if optional != _VALUE_TRUE:
            return
        if isinstance(self.strategy, CombinedStrategy):
            self._emit_attr(elem, 'a', _ATTR_ENABLE, _VALUE_TRUE)
        else:
            self._emit_attr(elem, 'a', _ATTR_ENABLE, 'false')

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
        # Emit ENABLE attribute before children (matches authentic config format)
        self._emit_enable_attribute(elem, ctr.optional)
        self._generate_children(ctr.children, elem, d_prefix)

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

        self._emit_enable_attribute(elem, ref.optional)

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

        Uses schema-source namespaces (not output namespaces, which are always v16).
        DataModel2/08 schema source → AUTOSAR 2.x style → 'CHOICE'.
        DataModel2/16 (or unknown) → AUTOSAR 3.x+ → 'IDENTIFIABLE'.
        """
        for uri in self._ns_for_schema_source.values():
            if _NS_LEGACY_VERSION in uri:
                return _CHC_CHOICE
        return _CHC_IDENTIFIABLE

    def toString(self, tree: ET.ElementTree) -> str:
        """Serialize element tree to XML string with proper namespace declarations."""
        ET.indent(tree, space='  ')
        root = tree.getroot()

        xml_bytes = ET.tostring(root, encoding='unicode', xml_declaration=False)

        # Build xmlns declarations for the root <datamodel> tag in the correct order.
        # Authentic EB Tresos config files use this specific order:
        # 1. version="7.0"
        # 2. xmlns (default namespace)
        # 3. xmlns:a (attribute namespace)
        # 4. xmlns:v (schema namespace)
        # 5. xmlns:d (data namespace)
        # ElementTree emits xmlns:a and xmlns:d automatically, but in wrong order.
        # We need to rebuild the entire opening tag with correct ordering.

        # Extract the closing part of the datamodel tag (after all attributes)
        # Find where the opening tag ends (either > or />)
        import re
        match = re.search(r'<datamodel[^>]*(>|/>)', xml_bytes)
        if not match:
            # Fallback: just add namespaces if we can't parse
            return "<?xml version='1.0'?>\n" + xml_bytes

        tag_end = match.group(1)

        # Build the correct datamodel opening tag
        parts = ['version="7.0"']

        # Add default namespace
        default_ns = self._ns_for_output.get('', '')
        if default_ns:
            parts.append('xmlns="%s"' % default_ns)

        # Add xmlns:a
        a_ns = self._ns_for_output.get('a', '')
        if a_ns:
            parts.append('xmlns:a="%s"' % a_ns)

        # Add xmlns:v
        v_ns = self._ns_for_output.get('v', '')
        if v_ns:
            parts.append('xmlns:v="%s"' % v_ns)

        # Add xmlns:d
        d_ns = self._ns_for_output.get('d', '')
        if d_ns:
            parts.append('xmlns:d="%s"' % d_ns)

        # Format with proper indentation (matching EB Tresos format)
        ns_decls = '\n           '.join(parts)

        # Build new opening tag
        new_opening = '<datamodel %s%s' % (ns_decls, tag_end)

        # Replace the old opening tag with the new one
        # Find the complete old opening tag
        old_opening_pattern = r'<datamodel[^>]*(>|/>)'
        xml_bytes = re.sub(old_opening_pattern, new_opening, xml_bytes, count=1)

        return "<?xml version='1.0'?>\n" + xml_bytes
