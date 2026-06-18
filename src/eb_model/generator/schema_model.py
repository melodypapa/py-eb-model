"""Schema model dataclasses representing XDM schema node structure.

Implements: SWR_GEN_00001 (Schema Model)
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class SchemaRange:
    """Parsed RANGE constraints for a schema variable."""
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    enum_values: List[str] = field(default_factory=list)
    regex_pattern: Optional[str] = None


@dataclass
class SchemaVar:
    """Schema variable definition (v:var)."""
    name: str
    var_type: str  # BOOLEAN, INTEGER, FLOAT, STRING, ENUMERATION, FUNCTION-NAME
    default: Optional[str] = None
    range_info: Optional[SchemaRange] = None
    label: Optional[str] = None
    desc: Optional[str] = None
    enabled: Optional[str] = None  # ENABLE data attribute value
    derived: Optional[str] = None  # DERIVED attribute value (XDM Spec 5.2.1.14.3)
    optional: Optional[str] = None  # OPTIONAL attribute value (XDM Spec 5.2.5.1)
    lower_multiplicity: Optional[int] = None  # LOWER-MULTIPLICITY (XDM Spec 5.2.5)
    upper_multiplicity: Optional[int] = None  # UPPER-MULTIPLICITY (XDM Spec 5.2.5)


@dataclass
class SchemaRef:
    """Schema reference definition (v:ref)."""
    name: str
    ref_type: str  # REFERENCE
    ref_targets: List[str] = field(default_factory=list)
    range_targets: List[str] = field(default_factory=list)
    enabled: Optional[str] = None  # ENABLE data attribute value
    optional: Optional[str] = None  # OPTIONAL attribute value (XDM Spec 5.2.5.1)
    lower_multiplicity: Optional[int] = None  # LOWER-MULTIPLICITY (XDM Spec 5.2.5)
    upper_multiplicity: Optional[int] = None  # UPPER-MULTIPLICITY (XDM Spec 5.2.5)


@dataclass
class SchemaCtr:
    """Schema container definition (v:ctr)."""
    name: str
    ctr_type: str  # IDENTIFIABLE, MODULE-DEF, AR-PACKAGE, etc.
    children: List = field(default_factory=list)  # List of schema nodes
    name_pattern: Optional[str] = None
    label: Optional[str] = None
    enabled: Optional[str] = None  # ENABLE data attribute value
    optional: Optional[str] = None  # OPTIONAL attribute value (XDM Spec 5.2.5.1)
    lower_multiplicity: Optional[int] = None  # LOWER-MULTIPLICITY (XDM Spec 5.2.5)
    upper_multiplicity: Optional[int] = None  # UPPER-MULTIPLICITY (XDM Spec 5.2.5)
    target: Optional[str] = None  # INSTANCE TARGET (XDM Spec 5.2.1.6.1)
    context: Optional[str] = None  # INSTANCE CONTEXT (XDM Spec 5.2.1.6.1)


@dataclass
class SchemaLst:
    """Schema list definition (v:lst)."""
    name: str
    lst_type: str  # MAP or empty string
    min_entries: int = 0
    max_entries: Optional[int] = None
    child: Optional[object] = None  # SchemaCtr, SchemaVar, or SchemaRef
    name_pattern: Optional[str] = None


@dataclass
class SchemaChc:
    """Schema choice definition (v:chc)."""
    name: str
    chc_type: str
    choices: List = field(default_factory=list)  # List of SchemaCtr


@dataclass
class SchemaRoot:
    """Root of a parsed schema tree."""
    module_name: str
    module_def: Optional[SchemaCtr] = None
    version: str = "7.0"
    namespaces: Dict[str, str] = field(default_factory=dict)
    ar_package_name: str = ""
