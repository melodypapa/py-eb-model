import argparse
import pkg_resources
import logging
import sys
import os.path

from ..parser import NvMXdmParser
from ..models import EBModel
from ..reporter import NvMXdmXlsWriter


def main():
    version = pkg_resources.require("py_eb_model")[0].version

    ap = argparse.ArgumentParser()
    ap.description = "Version: %s" % version
    ap.add_argument("-v", "--verbose", required=False, help="Print debug information.", action="store_true")
    ap.add_argument("--log", required=False, help="Specify the log file name.")
    ap.add_argument("INPUT", help="The path of NvM.xdm.")
    ap.add_argument("OUTPUT", help="The path of excel file.")

    args = ap.parse_args()

    logger = logging.getLogger()
    
    formatter = logging.Formatter('[%(levelname)s] : %(message)s')

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    if args.log:
        if os.path.exists(args.log):
            os.remove(args.log)

        file_handler = logging.FileHandler(args.log)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)

    logger.setLevel(logging.DEBUG)

    if args.verbose:
        stdout_handler.setLevel(logging.DEBUG)
    else:
        stdout_handler.setLevel(logging.INFO)

    if args.log:
        logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)

    try:
        doc = EBModel.getInstance()
        
        parser = NvMXdmParser()
        parser.parse_xdm(args.INPUT, doc)

        options = {}

        writer = NvMXdmXlsWriter()
        writer.write(args.OUTPUT, doc, options)
        
    except Exception as e:
        logger.error(e)
        raise e
