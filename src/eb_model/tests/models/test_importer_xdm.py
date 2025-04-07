
from ...models.eb_doc import PreferenceModel
from ...models.importer_xdm import SystemDescriptionImporter


class TestSystemDescriptionImporter:

    def test_get_parsed_input_files(self):
        document = PreferenceModel.getInstance()
        importer = document.getSystemDescriptionImporter()
        importer.addInputFile("${env_var:TRESOS_OUTPUT_DIR}\\**\\*.arxml")
        input_files = importer.getParsedInputFiles(
            {"env_var:TRESOS_OUTPUT_DIR": "c:/EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte/output/generated/swcd", "base_path": None})

        assert len(input_files) == 1
        assert input_files[0] == "c:/EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte/output/generated/swcd\\**\\*.arxml"

        document = PreferenceModel.getInstance()
        importer = document.getSystemDescriptionImporter()
        path_segments = importer.getAllPaths("../../EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte/output/generated/swcd")
        assert len(path_segments) == 7
        assert path_segments[0] == "EB"
        assert path_segments[1] == "EB/ACG-8_8_8_WIN32X86"
        assert path_segments[2] == "EB/ACG-8_8_8_WIN32X86/workspace"
        assert path_segments[6] == "EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte/output/generated/swcd"

    def test_get_links(self):
        document = PreferenceModel.getInstance()
        importer = document.getSystemDescriptionImporter()
        file_list = []
        file_list.append(
            "../../EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte/output/generated/swcd/Atomics_Bswmd.arxml")
        file_list.append(
            "../../EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte/output/generated/swcd/BswM.arxml")
        file_list.append(
            "../../EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte/output/generated/swcd/Atomics_Bswmd.arxml")

        links = importer.getLinks(file_list)
        assert len(links) == 9
        assert links[0].name == "EB"
        assert links[0].type == 2
        assert links[0].locationURI == "virtual:/virtual"

        assert links[1].name == "EB/ACG-8_8_8_WIN32X86"
        assert links[1].type == 2
        assert links[1].locationURI == "virtual:/virtual"

        assert links[2].name == "EB/ACG-8_8_8_WIN32X86/workspace"
        assert links[2].type == 2
        assert links[2].locationURI == "virtual:/virtual"

        assert links[3].name == "EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte"
        assert links[3].type == 2
        assert links[3].locationURI == "virtual:/virtual"

        assert links[6].name == "EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte/output/generated/swcd"
        assert links[6].type == 2
        assert links[6].locationURI == "virtual:/virtual"

        assert links[7].name == "EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte/output/generated/swcd/Atomics_Bswmd.arxml"
        assert links[7].type == 1
        assert links[7].locationURI == "PARENT-2-PROJECT_LOC/EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte/output/generated/swcd/Atomics_Bswmd.arxml"             # noqa E501  

        assert links[8].name == "EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte/output/generated/swcd/BswM.arxml"
        assert links[8].type == 1
        assert links[8].locationURI == "PARENT-2-PROJECT_LOC/EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte/output/generated/swcd/BswM.arxml"
