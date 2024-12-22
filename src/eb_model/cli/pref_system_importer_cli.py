import argparse
import pkg_resources
import logging
import sys
import os.path

from ..writer import TextPreferenceModelWriter
from ..parser import PerfXdmParser
from ..models import PreferenceModel

def main():
    version = pkg_resources.require("py_eb_model")[0].version

    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", required= False, help = "Print debug information", action = "store_true")
    ap.add_argument("--file-list", required=False, help = "Generate the file list (Default)", action = "store_true")
    ap.add_argument("--ab-project", required=False, help = "Generate the AUTOSAR builder project", action = "store_true")
    ap.add_argument("--base-path", required=False, help="Base Path for EB tresos")
    ap.add_argument("INPUTS", nargs='+', help = "The path of perf_imp_xxx.xdm.")
    ap.add_argument("OUTPUT", help = "The path of output file.")

    args = ap.parse_args()

    logger = logging.getLogger()
    
    formatter = logging.Formatter('[%(levelname)s] : %(message)s')

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    base_path = os.path.dirname(args.OUTPUT)
    log_file = os.path.join(base_path, 'pref_system_importer.log')

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

    format = "file_list"
    if args.ab_project:
        format = "ab_project"

    try:
        doc = PreferenceModel.getInstance()

        parser = PerfXdmParser()
        for file in args.INPUTS:
            if args.base_path is not None:
                file_name = os.path.realpath(os.path.join(args.base_path, file))
            else:
                file_name = file
            parser.parse_preference_xdm(file_name, doc)

        if format == "file_list":
            writer = TextPreferenceModelWriter()
            writer.writer_import_files(args.OUTPUT, doc.getSystemDescriptionImporter(), {
                'base_path': args.base_path,
                'wildcard':  True,
            })
        
    except Exception as e:
        logger.error(e)
        raise e
