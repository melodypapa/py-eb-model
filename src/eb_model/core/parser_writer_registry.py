"""
Parser-Writer Registry with Auto-Discovery.

Maps parser classes to their corresponding writer classes.
Uses naming convention for auto-discovery, with explicit registry fallback.

Implements:
    - SWR_CORE_00005: Parser-writer mapping registry
    - SWR_CORE_00006: Auto-discovery of writer classes
    - SWR_CORE_00007: Module name extraction from parser classes
"""
import importlib
from typing import Type, Optional, Dict

# Explicit registry for non-standard mappings
# Maps parser classes to writer classes
REGISTRY: Dict[Type, Type] = {}


def get_module_name(parser_class: Type) -> str:
    """
    Extract module name from parser class name.

    Examples:
        OsXdmParser -> "Os"
        NvMXdmParser -> "NvM"
        PduRXdmParser -> "PduR"
        BswMXdmParser -> "BswM"

    Args:
        parser_class: Parser class

    Returns:
        Module name string

    Implements: SWR_CORE_00007
    """
    class_name = parser_class.__name__
    # Remove "XdmParser" suffix (9 characters: XdmParser)
    if class_name.endswith("XdmParser"):
        return class_name[:-9]
    elif class_name.endswith("Parser"):
        return class_name[:-6]
    return class_name


def get_writer(parser_class: Type) -> Optional[Type]:
    """
    Get writer class for a parser using auto-discovery or registry.

    Auto-discovery pattern: OsXdmParser -> OsXdmXlsWriter in
    eb_model.reporter.excel_reporter.core.os_xdm module

    Module path transformation:
        eb_model.parser.core.os_xdm_parser -> eb_model.reporter.excel_reporter.core.os_xdm
        eb_model.parser.mem_stack.nvm_xdm_parser -> eb_model.reporter.excel_reporter.mem_stack.nvm_xdm

    Args:
        parser_class: Parser class to get writer for

    Returns:
        Writer class or None if not found

    Implements: SWR_CORE_00006
    """
    # Check explicit registry first
    if parser_class in REGISTRY:
        return REGISTRY[parser_class]

    # Auto-discover by naming convention
    parser_name = parser_class.__name__
    writer_name = parser_name.replace("Parser", "XlsWriter")

    # Determine the reporter module based on parser location
    module_name = parser_class.__module__
    # Transform: eb_model.parser.*.module_xdm_parser -> eb_model.reporter.excel_reporter.*.module_xdm
    reporter_module = module_name.replace(".parser.", ".reporter.excel_reporter.").replace("_parser", "")

    try:
        module = importlib.import_module(reporter_module)
        writer = getattr(module, writer_name, None)
        if writer is not None:
            return writer
    except (ImportError, AttributeError):
        pass

    return None


def get_writer_for_module(module_name: str) -> Optional[Type]:
    """
    Get writer class for a module name.

    Args:
        module_name: Module name (e.g., "Os", "NvM", "BswM")

    Returns:
        Writer class or None if not found

    Implements: SWR_CORE_00005
    """
    try:
        from eb_model.parser.core.eb_parser_factory import EbParserFactory
        parser_class = EbParserFactory._PARSERS.get(module_name)
        if parser_class:
            return get_writer(parser_class)
    except (ImportError, AttributeError):
        pass

    return None


def register_writer(parser_class: Type, writer_class: Type) -> None:
    """
    Explicitly register a writer for a parser.

    Use this for non-standard naming patterns where auto-discovery
    cannot determine the correct writer class.

    Args:
        parser_class: Parser class
        writer_class: Writer class

    Implements: SWR_CORE_00005
    """
    REGISTRY[parser_class] = writer_class
