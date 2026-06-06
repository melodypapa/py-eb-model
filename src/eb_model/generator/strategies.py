"""Value generation strategies for XDM model data.

Implements: SWR_GEN_00003 (Generation Strategies)
"""

import random
import re
import string
from typing import Optional

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
        if not ref.ref_targets:
            return None
        target = ref.ref_targets[0]
        mock_path = re.sub(r'^ASPath\w*:', 'ASPath:', target)
        return mock_path


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
        if not ref.ref_targets:
            return None
        target = ref.ref_targets[0]
        mock_path = re.sub(r'^ASPath\w*:', 'ASPath:', target)
        return mock_path


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
        if not ref.ref_targets:
            return None
        target = self.rng.choice(ref.ref_targets)
        mock_path = re.sub(r'^ASPath\w*:', 'ASPath:', target)
        return mock_path
