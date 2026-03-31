"""
CLI Options Registry.

Centralized registry for module-specific CLI options.
Keeps parsers pure by separating CLI concerns.
"""
from typing import List, Dict, Any

# Registry mapping parser class names to their CLI-specific options
# Each option is a dict with keys: name, help, action, default, etc.
CLI_OPTIONS: Dict[str, List[Dict[str, Any]]] = {
    "OsXdmParser": [
        {
            "name": "--skip-os-task",
            "help": "Skip generating Os task",
            "action": "store_true",
            "default": False
        }
    ],
    "RteXdmParser": [
        {
            "name": "--runnable",
            "help": "Export the runnable entities",
            "action": "store_true",
            "default": False
        }
    ],
    # Add other module-specific options as needed
    # Most modules have no specific options
}


def get_cli_options(parser_name: str) -> List[Dict[str, Any]]:
    """
    Get CLI options for a specific parser class.

    Args:
        parser_name: Name of the parser class (e.g., "OsXdmParser")

    Returns:
        List of option definitions, empty list if not found
    """
    return CLI_OPTIONS.get(parser_name, [])


def get_all_cli_options() -> Dict[str, List[Dict[str, Any]]]:
    """
    Get all registered CLI options.

    Returns:
        Dictionary mapping parser names to their options
    """
    return CLI_OPTIONS.copy()
