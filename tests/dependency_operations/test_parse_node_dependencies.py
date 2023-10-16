


from libraries_io_scraper.models import Dependency
from libraries_io_scraper.node_dependency_operations import parse_node_dependencies_file


class TestParseNodeDependenciesFile:

    def test_it_parses_dependencies(self, mocker, tmp_path):
        json_loads_mock = mocker.patch("json.loads")
        json_loads_mock.return_value = {
            "name": "aems-client",
            "version": "0.1.0",
            "dependencies": {
                "@emotion/react": "^11.10.5",
                "@emotion/styled": "^11.10.5",
            },
            "devDependencies": {}
        }

        fake_file = tmp_path / 'fake_file.yaml'
        fake_file.write_text('fake')

        return_value = parse_node_dependencies_file(
            fake_file)
        print(return_value)
        assert return_value == {
            'dependencies': [
                Dependency(name='@emotion/react', version='^11.10.5'),
                Dependency(name='@emotion/styled', version="^11.10.5"),
            ],
            "tools": []
     
        }
    def test_it_parses_dev_dependencies(self, mocker, tmp_path):
        json_loads_mock = mocker.patch("json.loads")
        json_loads_mock.return_value = {
            "name": "aems-client",
            "version": "0.1.0",
            "dependencies": {
                "@emotion/react": "^11.10.5",
                "@emotion/styled": "^11.10.5",},
            "devDependencies": {
                "@testing-library/jest-dom": "^5.16.5",
                "@testing-library/react": "^13.4.0",
        }}

        fake_file = tmp_path / 'fake_file.yaml'
        fake_file.write_text('fake')

        return_value = parse_node_dependencies_file(
            fake_file)
        print(return_value)
        assert return_value == {
            'dependencies': [
                Dependency(name='@emotion/react', version='^11.10.5'),
                Dependency(name='@emotion/styled', version="^11.10.5"),
            ],
            'tools': [
                Dependency(name="@testing-library/jest-dom", version="^5.16.5"),
                Dependency(name="@testing-library/react", version="^13.4.0"),
            ],
     
        }

