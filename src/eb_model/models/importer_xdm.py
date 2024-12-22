import glob
from typing import List
from .abstract import EcucObject
import os
import re

class SystemDescriptionImporter(EcucObject):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.inputFiles = []        # type: List[str]

    def getInputFiles(self):
        return self.inputFiles

    def addInputFile(self, value):
        self.inputFiles.append(value)
        return self
    
    def parseWildcard(self, filename: str) -> List[str]:
        #path: str, file_pattern: str
        file_list = []
        for file in glob.iglob(filename):
            print(file)
            file_list.append(file)
        return file_list
    
    def getParsedInputFiles(self, base_path: str, wildcard: bool) -> List[str]:
        file_list = []
        for input_file in self.inputFiles:
            if base_path is not None:
                if wildcard:
                    m = re.match(r'(.+)\\(\*\.\w+)', input_file)
                    if m:
                        path, file_pattern = m.group(1), m.group(2)
                        #for file_name in self.parseWildcard(os.path.realpath(os.path.join(base_path, path)), file_pattern):
                        for file_name in self.parseWildcard(os.path.realpath(os.path.join(base_path, input_file))):
                            file_list.append(file_name)
                    else:
                        file_list.append(os.path.realpath(os.path.join(base_path, input_file)))
                else:
                    file_list.append(os.path.realpath(os.path.join(base_path, input_file)))
            else:
                file_list.append(input_file)
        return file_list