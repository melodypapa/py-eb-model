from typing import Dict, List

from ..models.eclipse_project import Link
from ..models.abstract import EcucObject
import glob
import os
import re
import logging


class SystemDescriptionImporter(EcucObject):
    def __init__(self, parent, name):
        super().__init__(parent, name)
        
        self.logger = logging.getLogger()
        self.inputFiles = []        # type: List[str]

    def getInputFiles(self):
        return self.inputFiles

    def addInputFile(self, value: str):
        self.logger.debug("Add the file <%s>" % value)
        self.inputFiles.append(value)
        return self
    
    def parseWildcard(self, filename: str) -> List[str]:
        file_list = []
        for file in glob.iglob(filename, recursive=True):
            file_list.append(file)
        return file_list
    
    def getParsedInputFiles(self, params={}) -> List[str]:
        file_list = []
        for input_file in self.inputFiles:
            m = re.match(r'\$\{(env_var:\w+)\}(.*)', input_file)
            if m and m.group(1) in params:
                old_input_file = input_file
                input_file = params[m.group(1)] + m.group(2)
                # self.logger.info("Replace Environment Variable Path: %s => %s" % (old_input_file, os.path.realpath(input_file)))
                self.logger.info("Replace Environment Variable Path: %s => %s" % (old_input_file, input_file))
            if params['base_path'] is not None:
                if params['wildcard']:
                    m = re.match(r'(.+)\\(\*\.\w+)', input_file)
                    if m:
                        for file_name in self.parseWildcard(os.path.realpath(os.path.join(params['base_path'], input_file))):
                            self.logger.debug("Add the file <%s>." % file_name)
                            file_list.append(file_name)
                    else:
                        name = os.path.realpath(os.path.join(params['base_path'], input_file))
                        # self.logger.debug("Add the file <%s>." % name)
                        file_list.append(name)
                else:
                    file_list.append(os.path.realpath(os.path.join(params['base_path'], input_file)))
            else:
                file_list.append(input_file)
        return file_list
    
    def getAllPaths(self, path: str) -> List[str]:
        path_segments = path.split("/")

        result = []
        long_path = ""
        for path_segment in path_segments:
            if path_segment == "..":
                continue
            if long_path == "":
                long_path = path_segment
            else:
                long_path = long_path + "/" + path_segment
            result.append(long_path)
        return result
    
    def getNameByPath(self, path: str):
        path_segments = path.split("/")

        result = []
        count = 0
        for path_segment in path_segments:
            if path_segment == "..":
                count += 1
            else:
                result.append(path_segment)
        
        return (count, "/".join(result))
    
    def getLinks(self, file_list: List[str]) -> List[Link]:
        path_sets = {}                              # type: Dict[str, List[str]]
        path_segment_sets = []

        for file in file_list:
            path, basename = os.path.split(file)
            path = os.path.relpath(path).replace("\\", "/")
            if path not in path_sets:
                path_sets[path] = []
            
            # To avoid the duplicate file
            if basename not in path_sets[path]:
                path_sets[path].append(basename)

        links = []
        for name in path_sets:
            for path_segment in self.getAllPaths(name):
                if path_segment not in path_sets:
                    if path_segment not in path_segment_sets:
                        path_segment_sets.append(path_segment)
        
        for segment in path_segment_sets:
            link = Link(segment, 2, "virtual:/virtual")
            links.append(link)
        
        for path_set in path_sets:
            for basename in path_sets[path_set]:
                path = os.path.relpath(os.path.join(path_set, basename)).replace("\\", "/")
                count, name = self.getNameByPath(path)
                link = Link(name, 1, "PARENT-%d-PROJECT_LOC/%s" % (count, name))
                links.append(link)
        
        return links
