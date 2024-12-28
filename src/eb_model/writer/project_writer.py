from typing import List
from xml.dom import minidom
import xml.etree.ElementTree as ET
import logging

from ..models.eclipse_project import Link
from ..models.importer_xdm import SystemDescriptionImporter

class EclipseProjectWriter:
    def __init__(self):
        self.logger = logging.getLogger()

    def write_element(self, element: ET.Element, key: str, content: str) -> ET.Element:
        child_element = ET.SubElement(element, key)
        child_element.text = str(content)

        return child_element

    def write(self, links: List[Link]):
        pass

class ABProjectWriter(EclipseProjectWriter):
    def __init__(self):
        super().__init__()

    def _write_link(self, element: ET.Element, link: Link):
        child_element = ET.SubElement(element, "link")
        self.write_element(child_element, "name", link.name)
        self.write_element(child_element, "type", link.type)
        self.write_element(child_element, "locationURI", link.locationURI)
    
    def _write_links(self, element: ET.Element, links: List[Link]):
        child_element = ET.SubElement(element, "linkedResources")
        for link in links:
            self._write_link(child_element, link)

        self.logger.info("Total <%d> Links are written." % len(links))
        

    def _write_file_head(self, element: ET.Element, project: str):
        if project is not None:
            self.write_element(element, "name", project)
        else:
            self.write_element(element, "name", "project")

        self.write_element(element, "comment", "")
        self.write_element(element, "projects", "")
        self.write_element(element, "buildSpec", "")
        child_element = ET.SubElement(element, "natures")
        self.write_element(child_element, "nature", "org.artop.aal.workspace.autosarnature")

    def write(self, filename: str, project: str, links: List[Link]):
        root = ET.Element("projectDescription")

        self._write_file_head(root, project)
        self._write_links(root, links)

        xml = ET.tostring(root, encoding = "UTF-8", xml_declaration = True, short_empty_elements = False)

        dom = minidom.parseString(xml.decode())
        xml = dom.toprettyxml(indent = "  ", encoding = "UTF-8")

        with open(filename, "w", encoding="utf-8") as f_out:
            f_out.write(xml.decode())
        

    def writer_import_files(self, filename: str, importer: SystemDescriptionImporter, params = {'base_path': None, 'wildcard': None, "project": None}):
        self.logger.info("Generate AB project <%s>" % filename)
        file_list =  sorted(importer.getParsedInputFiles(params))
        links = importer.getLinks(file_list)
        self.write(filename, params['project'], links)
