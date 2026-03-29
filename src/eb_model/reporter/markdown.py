import logging


# Note: This module is kept for future implementation.
# The required classes (OsAutoSARDoc, OsApplication, BswModuleInstance) are not currently
# available in the models module. This file is excluded from the
# reporter package exports.


class OsApplicationMarkdownWriter:
    def __init__(self) -> None:
        self._logger = logging.getLogger()

    def _write_line(self, f_in, line: str):
        f_in.write(line + "\n")

    def _write_instances(self, f_in, os_application):
        self._write_line(f_in, "|Instance|Instance Type|Component Type|ASIL|Runnable|Task")
        self._write_line(f_in, "|--|--|--|--|--|--|")
        for instance in os_application.get_instances():
            # TODO: Implement once BswModuleInstance is available
            component_type = "SW Component"
            if len(instance.get_mappings()) > 0:
                package = instance.get_mappings()[0].package
            else:
                package = ""
            self._write_line(f_in, "|%s|%s|%s|%s|%s|%s|" % (instance.name, instance.type, component_type, "", package, ""))
            for mapping in instance.get_mappings():
                self._write_line(f_in, "|%s|%s|%s|%s|%s|%s|" % ("", "", "", "", mapping.event, mapping.task))

    def _write_os_applications(self, f_in, doc):
        self._write_line(f_in, "# OS Application")
        for os_app in doc.get_os_applications():
            self._write_line(f_in, "## %s" % os_app.name)
            self._write_instances(f_in, os_app)

    def write(self, filename: str, doc):
        with open(filename, 'w') as f_in:
            self._write_os_applications(f_in, doc)