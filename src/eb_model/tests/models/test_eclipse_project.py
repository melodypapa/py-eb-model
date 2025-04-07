import pytest
from ...models.eclipse_project import Link


class TestLink:

    def test_initialization(self):
        link = Link("TestLink", "File", "file:///path/to/resource")
        assert link.name == "TestLink"
        assert link.type == "File"
        assert link.locationURI == "file:///path/to/resource"

    def test_set_attributes(self):
        link = Link("InitialName", "Folder", "file:///initial/path")
        link.name = "UpdatedName"
        link.type = "File"
        link.locationURI = "file:///updated/path"

        assert link.name == "UpdatedName"
        assert link.type == "File"
        assert link.locationURI == "file:///updated/path"
