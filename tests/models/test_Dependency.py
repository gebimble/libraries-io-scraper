from itertools import product

import pytest

from libraries_io_scraper.models import Dependency
from tests.conftest import RESERVED_CHARACTERS


URL_ENCODING_CHARACTER = "%"


class TestDependency:
    def test_no_error(self):
        Dependency(name="@numpy/", version="1.20.0b0")

    @pytest.mark.parametrize(
        "name, version",
        product(
            [
                "numpy",
            ]
            + list(RESERVED_CHARACTERS),
            [
                "1.20.0b0",
            ]
            + list(RESERVED_CHARACTERS),
        ),
    )
    def test_no_reserved_characters(self, name: str, version: str):
        dep = Dependency(name=name, version=version)

        assert all(
            [
                x not in dep.safe_name
                for x in RESERVED_CHARACTERS
                if x != URL_ENCODING_CHARACTER
            ]
        )

        assert all(
            [
                x not in dep.safe_version
                for x in RESERVED_CHARACTERS
                if x != URL_ENCODING_CHARACTER
            ]
        )

    def test_get_sourcerank(self, mocker, numpy_sourcerank_return):
        get_sourcerank_mock = mocker.patch(
            "libraries_io_scraper.models.get_project_sourcerank"
        )
        get_sourcerank_mock.ok.return_value = True
        get_sourcerank_mock.return_value.json.return_value = numpy_sourcerank_return  # noqa: E501

        dep = Dependency(name="numpy", version="1.20.0")
        dep.get_sourcerank("conda")

        assert get_sourcerank_mock.return_value.ok
        assert dep.sourcerank["follows_semver"] == 0

    # TODO write test for unhappy response
