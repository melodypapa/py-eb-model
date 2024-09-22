
from ...models.eb_doc import EBModel
from ...models.abstract import EcucContainer, EcucObject

class TestEcucContainer:

    def test_create_container(self):
        document = EBModel.getInstance()
        os_container = EcucContainer(document, "Os")

        assert (os_container.getFullName() == "/Os")
        assert (os_container.getParent() == document)
        assert (os_container.getName() == "Os")

        container = document.find("/Os")

        assert (container.getFullName() == "/Os")
        assert (container.getParent() == document)
        assert (container.getName() == "Os")

        assert(isinstance(container, EcucContainer))
        assert(isinstance(container, EcucObject))