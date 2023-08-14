from itertools import product
from libraries_io_scraper.models import Dependency

import pytest


class TestDependency:

    def test_no_error(self):
        Dependency(name='@numpy/', version='1.20.0b0')

    @pytest.mark.parametrize(
        'name, version',
        product(
            ('numpy', '1.20.0b0'),
            ('reserved_characters', 'reserved_characters')
        )
    )
    def test_no_reserved_characters(
        self,
        name: str,
        version: str,
        reserved_characters: list[str],
        request
    ):
        for par in (name, version):
            try:
                par = request.getfixturevalue(par)
            except Exception:
                pass

        dep = Dependency(name=name, version=version)
        assert not any([ch in dep.name for ch in reserved_characters])
        assert not any([ch in dep.version for ch in reserved_characters])
        assert dep.sourcerank is None

    def test_get_sourcerank(self, mocker, numpy_sourcerank_return):
        get_sourcerank_mock = mocker.patch(
            "libraries_io_scraper.models.get_project_sourcerank")
        get_sourcerank_mock.ok.return_value = True
        get_sourcerank_mock.return_value.json.return_value = numpy_sourcerank_return

        dep = Dependency(name='numpy', version='1.20.0')
        dep.get_sourcerank('pypi')

        assert get_sourcerank_mock.return_value.ok
        assert dep.sourcerank["follows_semver"] == 0
