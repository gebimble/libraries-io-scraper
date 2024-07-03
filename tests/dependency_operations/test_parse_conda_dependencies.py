from libraries_io_scraper.dependency_operations.conda import (
    parse_dependencies_file,
)
from libraries_io_scraper.models import Dependency


class TestParseDependenciesFile:
    def test_it_parses_versioned_dependencies(self, mocker, tmp_path):
        parsed_yaml_mock = mocker.patch("yaml.safe_load")
        parsed_yaml_mock.return_value = {
            "name": "aems_server",
            "dependencies": ["python=3.10"],
        }

        platform = "conda"
        fake_file = tmp_path / "fake_file.yaml"
        fake_file.write_text("fake")

        return_value = parse_dependencies_file(fake_file)

        assert return_value == {
            "dependencies": [
                Dependency(name="python", version="3.10", platform=platform),
            ],
            "tools": [],
        }

    def test_it_parses_versioned_and_unversioned_dependencies(
        self, mocker, tmp_path
    ):
        parsed_yaml_mock = mocker.patch("yaml.safe_load")
        parsed_yaml_mock.return_value = {
            "name": "aems_server",
            "dependencies": [
                "python=3.10",
                "sqlalchemy",
                "pydantic<=1.8.2",
            ],
        }

        platform = "conda"
        fake_file = tmp_path / "fake_file.yaml"
        fake_file.write_text("fake")

        return_value = parse_dependencies_file(fake_file)

        assert return_value == {
            "dependencies": [
                Dependency(name="python", version="3.10", platform=platform),
                Dependency(name="sqlalchemy", version="", platform=platform),
                Dependency(name="pydantic", version="1.8.2", platform=platform),
            ],
            "tools": [],
        }

    def test_it_parses_versioned_and_unversioned_and_pip_dependencies(
        self, mocker, tmp_path
    ):
        parsed_yaml_mock = mocker.patch("yaml.safe_load")
        parsed_yaml_mock.return_value = {
            "name": "aems_server",
            "dependencies": [
                "python=3.10",
                "sqlalchemy",
                "pydantic<=1.8.2",
                {"pip": ["pydantic-sqlalchemy"]},
            ],
        }

        platform = "conda"
        fake_file = tmp_path / "fake_file.yaml"
        fake_file.write_text("fake")

        return_value = parse_dependencies_file(fake_file)

        assert return_value == {
            "dependencies": [
                Dependency(name="python", version="3.10", platform=platform),
                Dependency(name="sqlalchemy", version="", platform=platform),
                Dependency(name="pydantic", version="1.8.2", platform=platform),
                Dependency(name="pydantic-sqlalchemy", version="", platform=platform),
            ],
            "tools": [],
        }
