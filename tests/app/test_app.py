from click.testing import CliRunner
from libraries_io_scraper.app.app import DEFAULT_TEMPLATE, lios, npm, py
from libraries_io_scraper.dependency_operations import node, python


class TestAppPyGroup:
    def test_expected_behaviour_with_output_specified(self, mocker, tmp_path):
        runner = CliRunner()

        fake_input = str(tmp_path / "fake_input.yaml")
        fake_output = str(tmp_path / "output.md")

        deps_to_md_mock = mocker.patch(
            "libraries_io_scraper.app.app.dependencies_to_markdown_report"
        )
        deps_to_md_mock.return_value = None

        _ = runner.invoke(lios, ["py", fake_input, "-o", fake_output])

        deps_to_md_mock.assert_called_with(
            dependency_file=fake_input,
            output=fake_output,
            template=DEFAULT_TEMPLATE,
            parser=python.parse_dependencies_file,
            platform="pypi",
        )

    def test_expected_behaviour_without_output_specified(
        self, mocker, tmp_path
    ):
        runner = CliRunner()

        fake_input = str(tmp_path / "fake_input.yaml")

        deps_to_md_mock = mocker.patch(
            "libraries_io_scraper.app.app.dependencies_to_markdown_report"
        )

        deps_to_md_mock.return_value = None

        _ = runner.invoke(lios, ["py", fake_input])

        deps_to_md_mock.assert_called_with(
            dependency_file=fake_input,
            output="dependencies.md",
            template=DEFAULT_TEMPLATE,
            parser=python.parse_dependencies_file,
            platform="pypi",
        )


class TestAppNPMGroup:
    def test_expected_behaviour_with_output_specified(self, mocker, tmp_path):
        runner = CliRunner()

        fake_input = str(tmp_path / "fake_input.yaml")
        fake_output = str(tmp_path / "output.md")

        deps_to_md_mock = mocker.patch(
            "libraries_io_scraper.app.app.dependencies_to_markdown_report"
        )

        deps_to_md_mock.return_value = None

        _ = runner.invoke(lios, ["npm", fake_input, "-o", fake_output])

        deps_to_md_mock.assert_called_with(
            dependency_file=fake_input,
            output=fake_output,
            template=DEFAULT_TEMPLATE,
            parser=node.parse_dependencies_file,
            platform="npm",
        )

    def test_expected_behaviour_without_output_specified(
        self, mocker, tmp_path
    ):
        runner = CliRunner()

        fake_input = str(tmp_path / "fake_input.yaml")

        deps_to_md_mock = mocker.patch(
            "libraries_io_scraper.app.app.dependencies_to_markdown_report"
        )

        deps_to_md_mock.return_value = None

        _ = runner.invoke(lios, ["npm", fake_input])

        deps_to_md_mock.assert_called_with(
            dependency_file=fake_input,
            output="dependencies.md",
            template=DEFAULT_TEMPLATE,
            parser=node.parse_dependencies_file,
            platform="npm",
        )
