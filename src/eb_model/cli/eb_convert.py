"""
Unified CLI for converting EB Tresos XDM files to Excel.

This is the single entry point that replaces 54 separate CLI commands.
Auto-detects module(s) from XDM file and generates Excel output.
"""
import argparse
import os
import sys
from typing import List

from eb_model.parser.core.eb_parser_factory import EbParserFactory
from eb_model.models import EBModel
from eb_model.core.parser_writer_registry import get_writer, get_module_name
from eb_model.core.cli_options_registry import get_cli_options
from eb_model.cli.cli_utils import setup_logger


def create_argument_parser() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser.

    Collects module-specific options from CLI options registry.

    Returns:
        Configured ArgumentParser instance
    """
    parser = argparse.ArgumentParser(
        prog="eb-convert",
        description="Convert EB Tresos XDM files to Excel. Auto-detects module from file.",
        epilog="Example: eb-convert input.xdm output_dir/"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose (DEBUG) logging"
    )

    parser.add_argument(
        "--log",
        help="Log file path (for file-based logging)"
    )

    parser.add_argument(
        "inputs",
        nargs="+",
        help="One or more XDM input files"
    )

    parser.add_argument(
        "output_dir",
        help="Output directory for Excel files"
    )

    # Add module-specific options from registry
    cli_options = get_cli_options("OsXdmParser")  # Get Os options as example
    for option_def in cli_options:
        option_name = option_def["name"]
        option_kwargs = {k: v for k, v in option_def.items() if k != "name"}
        parser.add_argument(option_name, **option_kwargs)

    return parser


def parse_arguments(args: List[str]) -> argparse.Namespace:
    """
    Parse command-line arguments.

    Args:
        args: List of argument strings (typically sys.argv[1:])

    Returns:
        Parsed arguments as Namespace
    """
    parser = create_argument_parser()
    return parser.parse_args(args)


def process_file(input_file: str, output_dir: str, logger, args: argparse.Namespace) -> bool:
    """
    Process a single XDM file.

    Args:
        input_file: Path to input XDM file
        output_dir: Path to output directory
        logger: Logger instance
        args: Parsed command-line arguments

    Returns:
        True if successful, False otherwise
    """
    # Check input file exists
    if not os.path.exists(input_file):
        logger.error(f"Input file not found: {input_file}")
        return False

    logger.info(f"Processing: {input_file}")

    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Auto-detect parser from XDM file
        parser = EbParserFactory.create(input_file)
        module_name = get_module_name(parser.__class__)
        logger.info(f"Detected module: {module_name}")

        # Get writer for this parser
        writer_class = get_writer(parser.__class__)
        if writer_class is None:
            logger.error(f"No writer found for module: {module_name}")
            return False

        # Parse XDM file
        doc = EBModel.getInstance()
        parser.parse_xdm(input_file, doc)

        # Build options dict for writer
        options = {}
        # Add module-specific options
        if hasattr(args, 'skip_os_task'):
            options['skip_os_task'] = args.skip_os_task

        # Generate output filename
        output_file = os.path.join(output_dir, f"{module_name}.xlsx")

        # Write Excel output
        logger.info(f"Writing: {output_file}")
        writer = writer_class()
        writer.write(output_file, doc, options)

        logger.info(f"Successfully converted {input_file} -> {output_file}")
        return True

    except Exception as e:
        logger.error(f"Error processing {input_file}: {e}")
        import traceback
        logger.debug(traceback.format_exc())
        return False


def main() -> int:
    """
    Main entry point for eb-convert CLI.

    Returns:
        Exit code (0 for success, 1 for error)
    """
    # Parse arguments
    args = parse_arguments(sys.argv[1:])

    # Set up logging
    logger = setup_logger(verbose=args.verbose, log_file=args.log)

    # Process each input file
    success_count = 0
    for input_file in args.inputs:
        if process_file(input_file, args.output_dir, logger, args):
            success_count += 1

    # Return error if any file failed
    if success_count < len(args.inputs):
        logger.error(f"Failed to process {len(args.inputs) - success_count} of {len(args.inputs)} files")
        return 1

    logger.info(f"Successfully processed {success_count} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())