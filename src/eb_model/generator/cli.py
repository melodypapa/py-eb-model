"""CLI entry point for XDM model generator.

Implements: SWR_GEN_00005 (CLI)
"""

import argparse
import sys
import xml.etree.ElementTree as ET

from .schema_parser import SchemaParser
from .data_generator import DataGenerator
from .strategies import DefaultsStrategy, BoundaryStrategy, RandomStrategy


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser."""
    parser = argparse.ArgumentParser(
        prog='model-xdm-generator',
        description='Generate model (instance) XDM files from schema XDM files for testing.',
    )
    parser.add_argument(
        'input',
        help='Path to the schema XDM file',
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Output path for the generated model XDM file',
    )
    parser.add_argument(
        '--variant',
        choices=['defaults', 'boundary', 'random'],
        default='defaults',
        help='Value generation variant (default: defaults)',
    )
    parser.add_argument(
        '--seed',
        type=int,
        default=None,
        help='Random seed for reproducible output (used with --variant random)',
    )
    parser.add_argument(
        '--list-entries',
        type=int,
        default=None,
        help='Number of entries per list (overrides MIN from schema)',
    )
    return parser


def getStrategy(variant: str, seed=None):
    """Get the appropriate strategy for the variant."""
    strategies = {
        'defaults': DefaultsStrategy,
        'boundary': BoundaryStrategy,
        'random': RandomStrategy,
    }
    cls = strategies.get(variant)
    if cls is None:
        raise ValueError("Unknown variant: %s" % variant)
    return cls(seed=seed) if variant == 'random' else cls()


def main(args=None) -> int:
    """Main entry point."""
    parser = create_parser()
    opts = parser.parse_args(args)

    schema_parser = SchemaParser()
    try:
        tree = ET.parse(opts.input)
        schema_root = schema_parser.parse(tree.getroot())
    except Exception as e:
        print("Error parsing schema XDM: %s" % str(e), file=sys.stderr)
        return 1

    strategy = getStrategy(opts.variant, opts.seed)

    generator = DataGenerator(strategy=strategy, list_entries=opts.list_entries)
    result_tree = generator.generate(schema_root)

    xml_str = generator.toString(result_tree)
    try:
        with open(opts.output, 'w', encoding='utf-8') as f:
            f.write(xml_str)
        print("Generated model XDM: %s" % opts.output)
    except Exception as e:
        print("Error writing output: %s" % str(e), file=sys.stderr)
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
