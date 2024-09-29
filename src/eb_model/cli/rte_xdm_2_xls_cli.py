import argparse
import pkg_resources
import logging
import sys
import os.path

from eb_model.parser.eb_parser_factory import EbParserFactory

from ..reporter.excel_reporter.rte_xdm import RteRunnableEntityXlsWriter, RteXdmXlsWriter
from ..parser.rte_xdm_parser import RteXdmParser
from ..models import EBModel

def main():
    version = pkg_resources.require("py_eb_model")[0].version

    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", required= False, help= "Print debug information", action= "store_true")
    ap.add_argument("-r", "--runnable", required= False, help= "Export the runnable entities", action= "store_true")
    ap.add_argument("INPUT", help = "The path of xdm file.", nargs='+')
    ap.add_argument("OUTPUT", help = "The path of excel file.")

    args = ap.parse_args()

    logger = logging.getLogger()
    
    formatter = logging.Formatter('[%(levelname)s] [%(asctime)s]: %(message)s')

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    base_path = os.path.dirname(args.OUTPUT)
    log_file = os.path.join(base_path, 'rte_xdm_2_xls.log')

    if os.path.exists(log_file):
        os.remove(log_file)

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)

    if args.verbose:
        stdout_handler.setLevel(logging.DEBUG)
        
    else:
        stdout_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)    

    try:
        doc = EBModel.getInstance()

        for input_file in args.INPUT:
            parser = EbParserFactory.create(input_file)
            parser.parse_xdm(input_file, doc)

        if args.runnable:
            writer = RteRunnableEntityXlsWriter()
            writer.write(args.OUTPUT, doc)
        else:
            writer = RteXdmXlsWriter()
            writer.write(args.OUTPUT, doc)
        
    except Exception as e:
        logger.error(e)
        raise e
