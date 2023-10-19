from itertools import product

import pytest
from pydantic import ValidationError

from libraries_io_scraper.models import Dependency
from tests.conftest import RESERVED_CHARACTERS


class TestDependency:
    def test_no_error(self):
        Dependency(name="@numpy/", version="1.20.0b0", platform="pypi")

    @pytest.mark.parametrize(
        "name, version",
        product(
            ("numpy", "1.20.0b0"),
            (RESERVED_CHARACTERS, RESERVED_CHARACTERS),
        ),
    )
    def test_no_reserved_characters(self, name: str, version: str, request):
        for par in (name, version):
            try:
                par = request.getfixturevalue(par)
            except Exception:
                pass

        with pytest.raises(ValidationError):
            _ = Dependency(name=name, version=version)

    def test_get_sourcerank(self, mocker, numpy_sourcerank_return):
        get_sourcerank_mock = mocker.patch(
            "libraries_io_scraper.models.get_project_sourcerank"
        )
        get_sourcerank_mock.ok.return_value = True
        get_sourcerank_mock.return_value.json.return_value = numpy_sourcerank_return

        dep = Dependency(name="numpy", version="1.20.0", platform="pypi")
        dep.get_sourcerank("pypi")

        assert get_sourcerank_mock.return_value.ok
        assert dep.sourcerank["follows_semver"] == 0
