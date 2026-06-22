"""Value generation strategies for XDM model data.

Implements: SWR_GEN_00003 (Generation Strategies)
"""

import random
import re
import string
from typing import List, Optional

from .schema_model import SchemaRange, SchemaRef, SchemaVar


_TYPE_DEFAULTS = {
    'BOOLEAN': 'false',
    'INTEGER': '0',
    'FLOAT': '0.0',
    'STRING': '',
    'ENUMERATION': '',
    'FUNCTION-NAME': '',
    'MULTILINE-STRING': '',
    'LINKER-SYMBOL': '',
}

_ASPATH_TRANSFORM = re.compile(r'^ASPath\w*:')
_DEF_PATH_MARKER = 'AUTOSAR/EcucDefs/'


def _generate_mock_refpath(targets: List[str], chooser) -> Optional[str]:
    """Generate a mock ASPath reference value from target list.

    Returns None when the chosen target is a schema-definition path (contains
    `AUTOSAR/EcucDefs/`), because authentic EB Tresos config never carries
    definition paths in ref values — only real cross-module config paths.
    See docs/usage/model-xdm-generator.md "Reference Types".
    """
    if not targets:
        return None
    target = chooser(targets)
    if _DEF_PATH_MARKER in target:
        return None
    return _ASPATH_TRANSFORM.sub('ASPath:', target)


class DefaultsStrategy:
    """Generate values using DEFAULT attributes from schema."""

    def generateValue(self, var: SchemaVar) -> str:
        """Generate a value for a schema variable using its default."""
        if var.default is not None:
            return var.default
        if var.var_type == 'ENUMERATION' and var.range_info and var.range_info.enum_values:
            return var.range_info.enum_values[0]
        return _TYPE_DEFAULTS.get(var.var_type, '')

    def generateRefValue(self, ref: SchemaRef) -> Optional[str]:
        """Generate a mock ASPath reference value."""
        return _generate_mock_refpath(ref.ref_targets, lambda t: t[0])


class BoundaryStrategy:
    """Generate boundary values (min, max, edge cases)."""

    def generateValue(self, var: SchemaVar) -> str:
        """Generate a boundary value for a schema variable."""
        if var.var_type == 'BOOLEAN':
            return 'true'

        if var.var_type in ('INTEGER', 'FLOAT'):
            if var.range_info and var.range_info.min_value is not None:
                return str(int(var.range_info.min_value))
            return '0'

        if var.var_type == 'ENUMERATION':
            if var.range_info and var.range_info.enum_values:
                return var.range_info.enum_values[0]
            return var.default or ''

        if var.var_type in ('STRING', 'MULTILINE-STRING'):
            return ''

        if var.var_type in ('FUNCTION-NAME', 'LINKER-SYMBOL'):
            return 'Func_%s' % var.name

        return var.default or ''

    def generateRefValue(self, ref: SchemaRef) -> Optional[str]:
        """Generate a mock ASPath reference value."""
        return _generate_mock_refpath(ref.ref_targets, lambda t: t[0])


class RandomStrategy:
    """Generate random valid values within RANGE constraints."""

    def __init__(self, seed: Optional[int] = None) -> None:
        self.rng = random.Random(seed)

    def generateValue(self, var: SchemaVar) -> str:
        """Generate a random value for a schema variable."""
        if var.var_type == 'BOOLEAN':
            return 'true' if self.rng.random() > 0.5 else 'false'

        if var.var_type == 'INTEGER':
            min_val = int(var.range_info.min_value) if var.range_info and var.range_info.min_value is not None else 0
            max_val = int(var.range_info.max_value) if var.range_info and var.range_info.max_value is not None else 100
            if min_val > max_val:
                max_val = min_val + 100
            return str(self.rng.randint(min_val, max_val))

        if var.var_type == 'FLOAT':
            min_val = var.range_info.min_value if var.range_info and var.range_info.min_value is not None else 0.0
            max_val = var.range_info.max_value if var.range_info and var.range_info.max_value is not None else 100.0
            return str(round(self.rng.uniform(min_val, max_val), 6))

        if var.var_type == 'ENUMERATION':
            if var.range_info and var.range_info.enum_values:
                return self.rng.choice(var.range_info.enum_values)
            return var.default or ''

        if var.var_type in ('STRING', 'MULTILINE-STRING'):
            length = self.rng.randint(0, 10)
            return ''.join(self.rng.choices(string.ascii_letters + string.digits, k=length))

        if var.var_type in ('FUNCTION-NAME', 'LINKER-SYMBOL'):
            prefix = self.rng.choice(['Func', 'Cb', 'Hook', 'Notify'])
            return '%s_%s' % (prefix, var.name)

        return var.default or ''

    def generateRefValue(self, ref: SchemaRef) -> Optional[str]:
        """Generate a mock ASPath reference value."""
        return _generate_mock_refpath(ref.ref_targets, self.rng.choice)


class CombinedStrategy:
    """Generate values cycling through defaults, boundary, and random strategies.

    Entry 0 uses defaults, entry 1 uses boundary, entry 2+ uses random.
    This ensures comprehensive test coverage in a single generated XDM.

    Implements: SWR_GEN_00003 (Combined Strategy)
    """

    def __init__(self, seed: Optional[int] = None) -> None:
        self._counter = 0
        self._defaults = DefaultsStrategy()
        self._boundary = BoundaryStrategy()
        self._random = RandomStrategy(seed)

    def generateValue(self, var: SchemaVar) -> str:
        """Generate a value cycling through defaults, boundary, random."""
        idx = self._counter
        self._counter += 1

        if idx % 3 == 0:
            return self._defaults.generateValue(var)
        elif idx % 3 == 1:
            return self._boundary.generateValue(var)
        else:
            return self._random.generateValue(var)

    def generateRefValue(self, ref: SchemaRef) -> Optional[str]:
        """Generate a mock ASPath reference value (random choice)."""
        return self._random.generateRefValue(ref)
