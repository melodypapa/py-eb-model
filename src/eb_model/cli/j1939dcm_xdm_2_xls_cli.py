"""
J1939Dcm XDM to Excel CLI - Command-line interface for J1939Dcm module extraction.

Implements:
    - SWR_J1939DCM_00004: CLI interface
"""
import argparse
import pkg_resources
import logging
import sys
import os.path

from ..parser import J1939DcmXdmParser
from ..models import EBModel
from ..reporter import J1939DcmXdmXlsWriter


def main():
    """
    Main entry point for j1939dcm-xdm-xlsx CLI command.

    Implements: SWR_J1939DCM_00004 (CLI Interface)
    """
    version = pkg_resources.require("py_eb_model")[0].version

    ap = argparse.ArgumentParser()
    ap.description = "Version: %s" % version
    ap.add_argument("-v", "--verbose", required=False, help="Print debug information.", action="store_true")
    ap.add_argument("INPUT", help="The path of J1939Dcm.xdm.")
    ap.add_argument("OUTPUT", help="The path of excel file.")

    args = ap.parse_args()

    logger = logging.getLogger()

    formatter = logging.Formatter('[%(levelname)s] : %(message)s')

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    base_path = os.path.dirname(args.OUTPUT)
    log_file = os.path.join(base_path, 'j1939dcm_xdm_2_xls.log')

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

        parser = J1939DcmXdmParser()
        parser.parse_xdm(args.INPUT, doc)

        writer = J1939DcmXdmXlsWriter()
        writer.write(args.OUTPUT, doc)

    except Exception as e:
        logger.error(e)
        raise e