import argparse
import pkg_resources
import logging
import sys
import os.path

from eb_model.parser.eb_parser_factory import EbParserFactory

from ..reporter.excel_reporter.rte_xdm import RteRunnableEntityXlsWriter, RteXdmXlsWriter
from ..parser.ecuc_xdm_parser import EcucXdmXlsWriter
from ..models import EBModel


def process_logger(args):
    logger = logging.getLogger()
    formatter = logging.Formatter('[%(levelname)s] : %(message)s')
    logger.setLevel(logging.DEBUG)
    
    if args.verbose:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)
    stdout_handler.setLevel(log_level)
    logger.addHandler(stdout_handler)

    if args.log:
        if os.path.exists(args.log):
            os.remove(args.log)

        file_handler = logging.FileHandler(args.log)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(log_level)
        logger.addHandler(file_handler)
    return logger


def main():
    # version = pkg_resources.require("py_eb_model")[0].version

    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", required=False, help="Print debug information", action="store_true")
    ap.add_argument("--log", required=False, help="The Log file name.")
    ap.add_argument("INPUT", help="The path of xdm file.", nargs='+')
    ap.add_argument("OUTPUT", help="The path of excel file.")

    args = ap.parse_args()
    logger = process_logger(args)
    
    try:
        doc = EBModel.getInstance()

        for input_file in args.INPUT:
            parser = EbParserFactory.create(input_file)
            parser.parse_xdm(input_file, doc)

        writer = EcucXdmXlsWriter()
        writer.write(args.OUTPUT, doc)
        
    except Exception as e:
        logger.error(e)
        raise e
