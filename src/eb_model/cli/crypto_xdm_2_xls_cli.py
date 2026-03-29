"""
Crypto XDM to Excel CLI - Command-line interface for Crypto module extraction.

Implements:
    - SWR_CRYPTO_00004: CLI interface
"""
import argparse
import pkg_resources
import logging
import sys
import os.path

from eb_model.parser import CryptoXdmParser
from eb_model.models import EBModel
from eb_model.reporter import CryptoXdmXlsWriter


def main():
    """
    Main entry point for crypto-xdm-xlsx CLI command.

    Implements: SWR_CRYPTO_00004 (CLI Interface)
    """
    version = pkg_resources.require("py_eb_model")[0].version

    ap = argparse.ArgumentParser()
    ap.description = "Version: %s" % version
    ap.add_argument("-v", "--verbose", required=False, help="Print debug information.", action="store_true")
    ap.add_argument("INPUT", help="The path of Crypto.xdm.")
    ap.add_argument("OUTPUT", help="The path of excel file.")

    args = ap.parse_args()

    logger = logging.getLogger()

    formatter = logging.Formatter('[%(levelname)s] : %(message)s')

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    base_path = os.path.dirname(args.OUTPUT)
    log_file = os.path.join(base_path, 'crypto_xdm_2_xls.log')

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

        parser = CryptoXdmParser()
        parser.parse_xdm(args.INPUT, doc)

        writer = CryptoXdmXlsWriter()
        writer.write(args.OUTPUT, doc)

    except Exception as e:
        logger.error(e)
        raise e
