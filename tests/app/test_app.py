from click.testing import CliRunner
from libraries_io_scraper.app.app import py, npm


class TestAppPyGroup:

    def test_expected_behaviour_with_output_specified(self, mocker, tmp_path):
        runner = CliRunner()

        fake_input = str(tmp_path / "fake_input.yaml")
        fake_output = str(tmp_path / "output.md")

        deps_to_md_mock = mocker.patch(
            'libraries_io_scraper.app.app.dependencies_to_markdown_report'
        )
        py_mock = mocker.patch('libraries_io_scraper.app.app.py')

        py_mock.return_value = None
        deps_to_md_mock.return_value = None

        _ = runner.invoke(py, [fake_input, fake_output])

        assert py_mock.called_with(
            [
                fake_input,
                fake_output,
            ]
        )
        assert deps_to_md_mock.called_with(
            [
                fake_input,
                fake_output,
                py,
                "pypi"
            ]
        )

    def test_expected_behaviour_without_output_specified(self, mocker, tmp_path):
        runner = CliRunner()

        fake_input = str(tmp_path / "fake_input.yaml")

        deps_to_md_mock = mocker.patch(
            'libraries_io_scraper.app.app.dependencies_to_markdown_report'
        )
        py_mock = mocker.patch('libraries_io_scraper.app.app.py')

        py_mock.return_value = None
        deps_to_md_mock.return_value = None

        _ = runner.invoke(py, [fake_input])

        assert py_mock.called_with(
            [
                fake_input,
            ]
        )
        assert deps_to_md_mock.called_with(
            [
                fake_input,
                r"./dependencies.md",
                py,
                "pypi"
            ]
        )


class TestAppNPMGroup:

    def test_expected_behaviour_with_output_specified(self, mocker, tmp_path):
        runner = CliRunner()

        fake_input = str(tmp_path / "fake_input.yaml")
        fake_output = str(tmp_path / "output.md")

        deps_to_md_mock = mocker.patch(
            'libraries_io_scraper.app.app.dependencies_to_markdown_report'
        )
        node_mock = mocker.patch('libraries_io_scraper.app.app.npm')

        node_mock.return_value = None
        deps_to_md_mock.return_value = None

        _ = runner.invoke(py, [fake_input, fake_output])

        assert node_mock.called_with(
            [
                fake_input,
                fake_output,
            ]
        )
        assert deps_to_md_mock.called_with(
            [
                fake_input,
                fake_output,
                npm,
                "npm"
            ]
        )

    def test_expected_behaviour_without_output_specified(self, mocker, tmp_path):
        runner = CliRunner()

        fake_input = str(tmp_path / "fake_input.yaml")

        deps_to_md_mock = mocker.patch(
            'libraries_io_scraper.app.app.dependencies_to_markdown_report'
        )
        node_mock = mocker.patch('libraries_io_scraper.app.app.npm')

        node_mock.return_value = None
        deps_to_md_mock.return_value = None

        _ = runner.invoke(py, [fake_input])

        assert node_mock.called_with(
            [
                fake_input,
            ]
        )
        assert deps_to_md_mock.called_with(
            [
                fake_input,
                npm,
                "npm"
            ]
        )
