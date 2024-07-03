from libraries_io_scraper.dependency_operations.python import (
    parse_dependencies_file,
)
from libraries_io_scraper.models import Dependency


class TestParseDependenciesFile:
    def test_expected_behaviour(self, mocker, tmp_path):
        parsed_yaml_mock = mocker.patch("yaml.safe_load")
        parsed_yaml_mock.return_value = {
            "dependencies": ["python=3.8.0", "numpy<1.20.0", "scipy"],
            "tools": [
                "black^0.19.0",
            ],
        }

        fake_file = tmp_path / "fake_file.yaml"
        fake_file.write_text("fake")

        return_value = parse_dependencies_file(fake_file)

        assert return_value == {
            "dependencies": [
                Dependency(name="python", version="3.8.0"),
                Dependency(name="numpy", version="1.20.0"),
                Dependency(name="scipy"),
            ],
            "tools": [Dependency(name="black", version="0.19.0")],
        }
