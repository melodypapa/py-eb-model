import logging
from typing import List
from ..models.eb_doc import SystemDescriptionImporter


class TextWriter:
    def __init__(self):
        self.logger = logging.getLogger()

    def write(self, filename: str, lines: List[str]):
        with open(filename, "w") as f_out:
            for line in lines:
                f_out.write("%s\n" % line)


class TextPreferenceModelWriter(TextWriter):
    def __init__(self):
        super().__init__()

    def writer_import_files(self, filename: str, importer: SystemDescriptionImporter,
                            params={'base_path': None, 'wildcard': None, "tresos_output_base_dir": None}):
        self.logger.info("Generate import files list <%s>" % filename)
        lines = []
        for file in sorted(importer.getParsedInputFiles(params)):
            if file in lines:
                self.logger.warning("file <%s> is duplicated." % file)
            else:
                lines.append(file)

        self.write(filename, lines)
