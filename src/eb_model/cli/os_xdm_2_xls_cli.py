import argparse
import pkg_resources
import logging
import sys
import os.path

from ..parser import OsXdmParser
from ..models import EBModel
from ..reporter import OsXdmXlsWriter

def main():
    version = pkg_resources.require("py_eb_model")[0].version

    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", required= False, help= "Print debug information", action= "store_true")
    ap.add_argument("INPUT", help = "The path of Os.xdm.")
    ap.add_argument("OUTPUT", help = "The path of excel file.")

    args = ap.parse_args()

    logger = logging.getLogger()
    
    formatter = logging.Formatter('[%(levelname)s] : %(message)s')

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    base_path = os.path.dirname(args.OUTPUT)
    log_file = os.path.join(base_path, 'os_xdm_2_xls.log')

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
        parser = OsXdmParser()
        writer = OsXdmXlsWriter()

        parser.parse(args.INPUT, doc)
        writer.write(args.OUTPUT, doc)
        
    except Exception as e:
        logger.error(e)
        raise e