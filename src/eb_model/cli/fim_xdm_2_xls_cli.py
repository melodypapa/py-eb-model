"""
FiM XDM to Excel CLI - Command-line interface for FiM module extraction.

Implements:
    - SWR_FIM_00004: CLI interface
"""
import argparse
import pkg_resources
import logging
import sys
import os.path

from eb_model.parser import FiMXdmParser
from eb_model.models import EBModel
from eb_model.reporter import FiMXdmXlsWriter


def main():
    """
    Main entry point for fim-xdm-xlsx CLI command.

    Implements: SWR_FIM_00004 (CLI Interface)
    """
    version = pkg_resources.require("py_eb_model")[0].version

    ap = argparse.ArgumentParser()
    ap.description = "Version: %s" % version
    ap.add_argument("-v", "--verbose", required=False, help="Print debug information.", action="store_true")
    ap.add_argument("INPUT", help="The path of FiM.xdm.")
    ap.add_argument("OUTPUT", help="The path of excel file.")

    args = ap.parse_args()

    logger = logging.getLogger()

    formatter = logging.Formatter('[%(levelname)s] : %(message)s')

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    base_path = os.path.dirname(args.OUTPUT)
    log_file = os.path.join(base_path, 'fim_xdm_2_xls.log')

    try:
        os.remove(log_file)
    except FileNotFoundError:
        pass

    if args.verbose:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)

    logger.setLevel(logging.DEBUG)

    if args.verbose:
        stdout_handler.setLevel(logging.DEBUG)
    else:
        stdout_handler.setLevel(logging.INFO)

    if args.verbose:
        logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)

    try:
        doc = EBModel.getInstance()

        parser = FiMXdmParser()
        parser.parse_xdm(args.INPUT, doc)

        writer = FiMXdmXlsWriter()
        writer.write(args.OUTPUT, doc)

    except Exception as e:
        logger.error(e)
        raise e
