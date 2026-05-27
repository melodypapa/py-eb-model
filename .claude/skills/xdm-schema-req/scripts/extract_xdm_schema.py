#!/usr/bin/env python3
"""Extract structured data from EB Tresos XDM schema files.

Parses an XDM schema and outputs a compact JSON representation suitable for
use by the xdm-schema-req skill. The JSON is significantly smaller than the
raw XML (~10x reduction for large schemas like Os_schema.xdm).

Usage:
    python tools/extract_xdm_schema.py data/Os_schema.xdm
    python tools/extract_xdm_schema.py data/Os_schema.xdm --pretty

Output JSON schema:
    {
      "module": "Os",
      "stack": "core",
      "module_abbr": "OS",
      "containers": [
        {
          "name": "OsTask",
          "is_map": true,
          "fields": [...],
          "sub_containers": [...]
        }
      ]
    }
"""

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

# ---------------------------------------------------------------------------
# Namespace URIs
# ---------------------------------------------------------------------------
_NS = {
    "v": "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
    "a": "http://www.tresos.de/_projects/DataModel2/08/attribute.xsd",
    "d": "http://www.tresos.de/_projects/DataModel2/06/data.xsd",
}

# ---------------------------------------------------------------------------
# Stack / module-abbr mapping (matches SKILL.md Step 4 table)
# ---------------------------------------------------------------------------
_STACK_MAP = {
    "Os": ("core", "OS"),
    "EcuC": ("core", "ECUC"),
    "BswM": ("core", "BSWM"),
    "Det": ("core", "DET"),
    "EcuM": ("core", "ECUM"),
    "Tm": ("core", "TM"),
    "PbcfgM": ("core", "PBCFGM"),
    "Rte": ("core", "RTE"),
    "NvM": ("mem_stack", "NVM"),
    "MemIf": ("mem_stack", "MEMIF"),
    "Fee": ("mem_stack", "FEE"),
    "Ea": ("mem_stack", "EA"),
    "MemMap": ("mem_stack", "MEMMAP"),
    "MemAcc": ("mem_stack", "MEMACC"),
    "CanIf": ("can_stack", "CANIF"),
    "CanNm": ("can_stack", "CANNM"),
    "CanSm": ("can_stack", "CANSM"),
    "CanTp": ("can_stack", "CANTP"),
    "LinIf": ("lin_stack", "LINIF"),
    "LinSm": ("lin_stack", "LINSM"),
    "LinTp": ("lin_stack", "LINTP"),
    "FrIf": ("fr_stack", "FRIF"),
    "FrNm": ("fr_stack", "FRNM"),
    "FrSm": ("fr_stack", "FRSM"),
    "FrTp": ("fr_stack", "FRTP"),
    "FrArTp": ("fr_stack", "FRARTP"),
    "EthIf": ("eth_stack", "ETHIF"),
    "EthSm": ("eth_stack", "ETHSM"),
    "TcpIp": ("eth_stack", "TCPIP"),
    "SoAd": ("eth_stack", "SOAD"),
    "UdpNm": ("eth_stack", "UDPNM"),
    "DoIp": ("eth_stack", "DOIP"),
    "SomeIpTp": ("eth_stack", "SOMEIPTP"),
    "PduR": ("com_stack", "PDUR"),
    "IpduM": ("com_stack", "IPDUM"),
    "Com": ("com_stack", "COM"),
    "LdCom": ("com_stack", "LDCOM"),
    "ComM": ("com_stack", "COMM"),
    "Nm": ("com_stack", "NM"),
    "Crc": ("com_stack", "CRC"),
    "Crypto": ("crypto_stack", "CRYPTO"),
    "CryIf": ("crypto_stack", "CRYIF"),
    "Csm": ("crypto_stack", "CSM"),
    "SecOc": ("crypto_stack", "SECOC"),
    "FiM": ("diag_stack", "FIM"),
    "Dcm": ("diag_stack", "DCM"),
    "Dem": ("diag_stack", "DEM"),
    "Dlt": ("diag_stack", "DLT"),
    "J1939Dcm": ("j1939_stack", "J1939DCM"),
    "J1939Nm": ("j1939_stack", "J1939NM"),
    "J1939Rm": ("j1939_stack", "J1939RM"),
    "J1939Tp": ("j1939_stack", "J1939TP"),
}

# Schema type → Python requirements type
_TYPE_MAP = {
    "INTEGER": "int",
    "FLOAT": "float",
    "BOOLEAN": "bool",
    "STRING": "str",
    "MULTILINE-STRING": "str",
    "FUNCTION-NAME": "str",
    "ENUMERATION": None,       # resolved per-field as <Container><Field>
    "REFERENCE": "EcucRefType",
    "FOREIGN-REFERENCE": "EcucRefType",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _attr(element, attr_name, ns=_NS):
    """Get value of <a:a name="attr_name" value="..."> child."""
    el = element.find(f'a:a[@name="{attr_name}"]', ns)
    if el is None:
        return None
    return el.get("value")


def _da(element, da_name, ns=_NS):
    """Get <a:da name="da_name"> child element."""
    return element.find(f'a:da[@name="{da_name}"]', ns)


def _extract_desc(element, ns=_NS):
    """Extract and clean DESC text from an element."""
    desc_el = element.find('a:a[@name="DESC"]', ns)
    if desc_el is None:
        return ""
    # Simple value attribute
    val = desc_el.get("value", "")
    if val:
        return _clean_desc(val)
    # Child <a:v> with possible HTML
    v_el = desc_el.find("a:v", ns)
    if v_el is not None:
        text = ET.tostring(v_el, encoding="unicode", method="text")
        return _clean_desc(text)
    return ""


def _clean_desc(text):
    """Strip EN: prefix, HTML tags, and excess whitespace."""
    text = re.sub(r"<[^>]+>", " ", text)   # remove HTML tags
    text = re.sub(r"^EN:\s*", "", text.strip())
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _extract_origin(element, ns=_NS):
    """Return 'AUTOSAR' or 'EB' from ORIGIN attribute."""
    origin = _attr(element, "ORIGIN", ns) or _attr(element, "__ORIGIN", ns) or ""
    if "AUTOSAR" in origin.upper():
        return "AUTOSAR"
    if origin:
        return "EB"
    return "EB"


def _extract_range(element, ns=_NS):
    """
    Extract numeric range from INVALID type=Range or RANGE da.
    Returns dict like {"min": 0, "max": 255} or None.
    """
    # Method 1: INVALID type=Range with a:tst expressions
    invalid_da = element.find('a:da[@name="INVALID"]', ns)
    if invalid_da is not None and invalid_da.get("type") == "Range":
        lo, hi = None, None
        for tst in invalid_da.findall("a:tst", ns):
            expr = tst.get("expr", "")
            m = re.match(r"^([<>]=?)\s*([0-9.eE+-]+)$", expr)
            if m:
                op, val_str = m.group(1), m.group(2)
                val = float(val_str) if "." in val_str or "e" in val_str.lower() else int(val_str)
                # Expressions define the VALID range:
                # "<= N" means valid upper bound = N (strict "<" means N-1 for int)
                # ">= N" means valid lower bound = N (strict ">" means N+1 for int)
                if op == "<=":
                    hi = val
                elif op == "<":
                    hi = val - (1 if isinstance(val, int) else 0)
                elif op == ">=":
                    lo = val
                elif op == ">":
                    lo = val + (1 if isinstance(val, int) else 0)
        if lo is not None or hi is not None:
            return {"min": lo, "max": hi}

    # Method 2: RANGE da with value attribute or a:v children (direct range spec)
    range_da = _da(element, "RANGE", ns)
    if range_da is not None:
        # Check value attribute first (e.g., RANGE value="64-65536")
        range_val = range_da.get("value", "")
        if range_val:
            m = re.match(r"^([0-9.]+)\s*-\s*([0-9.]+)$", range_val)
            if m:
                lo_s, hi_s = m.group(1), m.group(2)
                lo_v = float(lo_s) if "." in lo_s else int(lo_s)
                hi_v = float(hi_s) if "." in hi_s else int(hi_s)
                return {"min": lo_v, "max": hi_v}
        # Child a:v elements
        vals = [v.text.strip() for v in range_da.findall("a:v", ns) if v.text]
        if len(vals) == 1:
            m = re.match(r"^([0-9.]+)\s*-\s*([0-9.]+)$", vals[0])
            if m:
                lo_s, hi_s = m.group(1), m.group(2)
                lo_v = float(lo_s) if "." in lo_s else int(lo_s)
                hi_v = float(hi_s) if "." in hi_s else int(hi_s)
                return {"min": lo_v, "max": hi_v}
            # Single bound expressions like ">=0"
            lo, hi = None, None
            for v in vals:
                m2 = re.match(r"^([<>]=?)\s*([0-9.eE+-]+)$", v)
                if m2:
                    op, val_str = m2.group(1), m2.group(2)
                    val = float(val_str) if "." in val_str else int(val_str)
                    if op in (">=", ">"):
                        lo = val
                    elif op in ("<=", "<"):
                        hi = val
            if lo is not None or hi is not None:
                return {"min": lo, "max": hi}
    return None


def _extract_enum_values(element, ns=_NS):
    """Return list of enum values and default from RANGE/DEFAULT da."""
    range_da = _da(element, "RANGE", ns)
    values = []
    if range_da is not None:
        values = [v.text.strip() for v in range_da.findall("a:v", ns) if v.text]
    default_da = _da(element, "DEFAULT", ns)
    default = default_da.get("value") if default_da is not None else None
    return values, default


def _extract_bool_default(element, ns=_NS):
    """Return boolean default value string or None."""
    default_da = _da(element, "DEFAULT", ns)
    if default_da is not None:
        val = default_da.get("value", "").lower()
        return val if val in ("true", "false") else None
    return None


def _extract_enable(element, ns=_NS):
    """
    Return (enabled: bool, xpath: str|None).
    - enabled=False, xpath=None → disabled by default, skip
    - enabled=True, xpath=str  → conditionally enabled, include
    - enabled=True, xpath=None → always enabled
    """
    enable_da = _da(element, "ENABLE", ns)
    if enable_da is None:
        return True, None
    val = enable_da.get("value", "").lower()
    etype = enable_da.get("type", "")
    if etype == "XPath":
        # Conditionally enabled
        return True, val
    if val == "false":
        return False, None
    return True, None


def _req_type(schema_type, container_name, field_name):
    """Map schema type to requirements type string.

    For ENUMERATION, AUTOSAR field names often embed the container prefix
    (e.g., OsTask.OsTaskSchedule). In that case the type is just the field
    name. When the field name is short (e.g., TestContainer.TestMode), the
    type is <ContainerName><FieldName>.
    """
    if schema_type == "ENUMERATION":
        # If field already starts with container name, use field name as type
        if field_name.lower().startswith(container_name.lower()):
            return field_name
        return f"{container_name}{field_name}"
    return _TYPE_MAP.get(schema_type, schema_type)


# ---------------------------------------------------------------------------
# Field extractors
# ---------------------------------------------------------------------------

def _extract_var(var_el, container_name, ns=_NS):
    """Extract a v:var field descriptor."""
    name = var_el.get("name", "")
    schema_type = var_el.get("type", "")
    enabled, xpath = _extract_enable(var_el, ns)

    field = {
        "name": name,
        "field_type": "var",
        "schema_type": schema_type,
        "req_type": _req_type(schema_type, container_name, name),
        "origin": _extract_origin(var_el, ns),
        "desc": _extract_desc(var_el, ns),
        "enabled": enabled,
    }

    if not enabled:
        return field  # skip heavy extraction for disabled fields

    if xpath:
        field["enable_xpath"] = xpath

    if schema_type == "ENUMERATION":
        values, default = _extract_enum_values(var_el, ns)
        field["enum_values"] = values
        if default:
            field["enum_default"] = default
    elif schema_type in ("INTEGER", "FLOAT"):
        rng = _extract_range(var_el, ns)
        if rng:
            field["range"] = rng
    elif schema_type == "BOOLEAN":
        default = _extract_bool_default(var_el, ns)
        if default:
            field["bool_default"] = default

    return field


def _extract_ref(ref_el, container_name, is_list=False, ns=_NS):
    """Extract a v:ref field descriptor."""
    name = ref_el.get("name", "")
    schema_type = ref_el.get("type", "REFERENCE")
    enabled, xpath = _extract_enable(ref_el, ns)

    req_t = "List[EcucRefType]" if is_list else "EcucRefType"
    return {
        "name": name,
        "field_type": "ref",
        "schema_type": schema_type,
        "req_type": req_t,
        "origin": _extract_origin(ref_el, ns),
        "desc": _extract_desc(ref_el, ns),
        "enabled": enabled,
        **({"enable_xpath": xpath} if xpath else {}),
    }


# ---------------------------------------------------------------------------
# Container extractor (recursive)
# ---------------------------------------------------------------------------

def _extract_container(ctr_el, parent_name=None, ns=_NS):
    """
    Recursively extract a v:ctr element into a container descriptor.
    parent_name is used for determining req_type of nested containers.
    """
    name = ctr_el.get("name", "")
    fields = []
    sub_containers = []

    for child in ctr_el:
        local = child.tag.split("}")[-1] if "}" in child.tag else child.tag
        c_name = child.get("name", "")

        if local == "var":
            fields.append(_extract_var(child, name, ns))

        elif local == "ref":
            fields.append(_extract_ref(child, name, is_list=False, ns=ns))

        elif local == "lst":
            lst_type = child.get("type")
            # List of references
            ref_el = child.find("v:ref", ns)
            if ref_el is not None:
                fields.append(_extract_ref(ref_el, name, is_list=True, ns=ns))
            # Nested MAP sub-container
            elif lst_type == "MAP":
                sub_ctr = child.find("v:ctr", ns)
                if sub_ctr is not None:
                    sub_containers.append(_extract_container(sub_ctr, name, ns))
            # Nested choice (v:chc inside lst)
            chc_el = child.find("v:chc", ns)
            if chc_el is not None:
                sub_containers.append(_extract_choice(chc_el, name, ns))

        elif local == "ctr":
            sub_containers.append(_extract_container(child, name, ns))

        elif local == "chc":
            sub_containers.append(_extract_choice(child, name, ns))

    result = {"name": name, "fields": fields}
    if sub_containers:
        result["sub_containers"] = sub_containers
    return result


def _extract_choice(chc_el, parent_name, ns=_NS):
    """Extract a v:chc choice element."""
    name = chc_el.get("name", parent_name + "Choice")
    variants = []
    for ctr in chc_el.findall("v:ctr", ns):
        variants.append(_extract_container(ctr, parent_name, ns))
    return {
        "name": name,
        "is_choice": True,
        "variants": variants,
    }


# ---------------------------------------------------------------------------
# Module extractor
# ---------------------------------------------------------------------------

def extract_module(xdm_path: str) -> dict:
    """Parse an XDM schema file and return structured dict."""
    try:
        tree = ET.parse(xdm_path)
    except ET.ParseError as e:
        raise ValueError(f"XML parse error in {xdm_path}: {e}") from e

    root = tree.getroot()
    ns = _NS

    # Find module name from d:chc element
    chc_el = root.find(".//d:chc", ns)
    if chc_el is None:
        raise ValueError("No d:chc element found — is this an XDM schema file?")

    module_name = chc_el.get("name", "Unknown")
    stack, abbr = _STACK_MAP.get(module_name, ("core", module_name.upper()))

    mod_ctr = chc_el.find("v:ctr", ns)
    if mod_ctr is None:
        raise ValueError(f"No v:ctr found under d:chc for module {module_name}")

    containers = []
    for lst_el in mod_ctr.findall("v:lst", ns):
        lst_name = lst_el.get("name", "")
        lst_type = lst_el.get("type", "")
        ctr_el = lst_el.find("v:ctr", ns)
        if ctr_el is None:
            continue
        container = _extract_container(ctr_el, None, ns)
        container["is_map"] = (lst_type == "MAP")
        containers.append(container)

    return {
        "module": module_name,
        "stack": stack,
        "module_abbr": abbr,
        "output_path": f"docs/requirements/{stack}/models/swr_{module_name.lower()}_models.md",
        "containers": containers,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Extract structured data from EB Tresos XDM schema files."
    )
    parser.add_argument("xdm_file", help="Path to .xdm schema file")
    parser.add_argument(
        "--pretty", "-p", action="store_true", help="Pretty-print JSON output"
    )
    args = parser.parse_args()

    xdm_path = Path(args.xdm_file)
    if not xdm_path.exists():
        print(f"Error: file not found: {xdm_path}", file=sys.stderr)
        sys.exit(1)

    try:
        data = extract_module(str(xdm_path))
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    indent = 2 if args.pretty else None
    print(json.dumps(data, indent=indent, ensure_ascii=False))


if __name__ == "__main__":
    main()
