import pytest
from ...models.eb_doc import EBModel, PreferenceModel


class TestEBModel:

    def test_ebmodel_singleton_exception(self):
        EBModel.getInstance()
        with pytest.raises(Exception) as err:
            EBModel()
        assert (str(err.value) == "The EBModel is singleton!")

    def test_cannot_find_element(self):
        document = EBModel.getInstance()
        assert (document.find("/os/os") is None)

    def test_ebmodel(self):
        document = EBModel.getInstance()
        assert (isinstance(document, EBModel))
        assert (isinstance(document, EBModel))
        assert (document.getFullName() == "")

    def test_clear(self):
        document = EBModel.getInstance()
        document.clear()
        assert (document.getTotalElement() == 0)
        document.getOs()
        assert (document.getTotalElement() == 1)
        document.clear()
        assert (document.getTotalElement() == 0)

    def test_ebmodel_get_os(self):
        document = EBModel.getInstance()
        os = document.getOs()
        assert (os.getFullName() == "/Os/Os")

    def test_ebmodel_get_rte(self):
        document = EBModel.getInstance()
        rte = document.getRte()
        assert (rte.getFullName() == "/Rte/Rte")

    def test_ebmodel_get_nvm(self):
        document = EBModel.getInstance()
        nvm = document.getNvM()
        assert (nvm.getFullName() == "/NvM/NvM")


class TestPreferenceModel:

    def test_preference_model_singleton_exception(self):
        PreferenceModel.getInstance()
        with pytest.raises(Exception) as err:
            PreferenceModel()
        assert (str(err.value) == "The PreferenceModel is singleton!")

    def test_mode_get_system_description_importer(self):
        document = PreferenceModel.getInstance()
        importer = document.getSystemDescriptionImporter()
        assert importer.getFullName() == "/ImporterExporterAdditions/SystemDescriptionImporters"

        importer = document.find(
            "/ImporterExporterAdditions/SystemDescriptionImporters")
        assert importer.getFullName() == "/ImporterExporterAdditions/SystemDescriptionImporters"

        importer = document.getSystemDescriptionImporter()
        assert importer.getFullName() == "/ImporterExporterAdditions/SystemDescriptionImporters"
