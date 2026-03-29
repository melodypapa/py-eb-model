"""
CLI entry point for converting Fee XDM files to Excel.
"""
import sys
import argparse
import os.path
import logging
import pkg_resources

from eb_model.parser.eb_parser_factory import EbParserFactory
from eb_model.models.core.eb_doc import EBModel
from eb_model.reporter.excel_reporter.fee_xdm import FeeXdmXlsWriter


def main():
    """Convert Fee XDM file to Excel format."""
    version = pkg_resources.require("py_eb_model")[0].version

    ap = argparse.ArgumentParser(description='Version: %s' % version)
    ap.add_argument("-v", "--verbose", required=False, help="Print debug information.", action="store_true")
    ap.add_argument("INPUT", help="The path of Fee.xdm.")
    ap.add_argument("OUTPUT", help="The path of excel file.")

    args = ap.parse_args()

    logger = logging.getLogger()
    formatter = logging.Formatter('[%(levelname)s] : %(message)s')

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    base_path = os.path.dirname(args.OUTPUT)
    log_file = os.path.join(base_path, 'fee_xdm_2_xls.log')

    if os.path.exists(log_file):
        os.remove(log_file)

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

        parser = EbParserFactory.create(args.INPUT)
        parser.parse_xdm(args.INPUT, doc)

        writer = FeeXdmXlsWriter()
        writer.write(args.OUTPUT, doc)
        logger.info("Successfully exported to %s" % args.OUTPUT)
        return 0
    except Exception as e:
        logger.error(e)
        return 1