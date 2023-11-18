from unittest.mock import patch, mock_open
from libraries_io_scraper.models import Dependency
from libraries_io_scraper.make_results_table import (
    populate_jinja_template,
    write_template_to_file,
    make_results_table,
)


class TestMakeResultsTable:
    def test_it_renders_a_valid_markdown_table(self):
        want = """
| Name  | Version | Dependency Type | Rating |
| --- | --- | --- | --- |
| test | 123 | dependency | None |
| test2 | 567 | dependency | None |
| @types/node | 16.18.59 | dependency | None |
"""

        test_dependencies = [
            Dependency(name="test", version="123"),
            Dependency(name="test2", version="567"),
            Dependency(name="@types/node", version="16.18.59"),
        ]
        got = populate_jinja_template({"dependency": test_dependencies})
        assert got == want

    @patch("builtins.open", new_callable=mock_open())
    def test_writes_the_output_to_a_markdown_file(self, mock_open_file):
        write_template_to_file("some text")

        mock_open_file.assert_called_once_with("dependencies.md", "w")
        mock_open_file.return_value.__enter__().write.assert_called_once_with(
            "some text"
        )

    def test_model_api_integration(self):
        want = """
| Name  | Version | Dependency Type | Rating |
| --- | --- | --- | --- |
| @types/node | 16.18.59 | dependency | 34 |
"""
        test_dependencies = [
            Dependency(name="@types/node", version="16.18.59"),
        ]

        test_dependencies[0].get_sourcerank("npm")

        got = populate_jinja_template({"dependency": test_dependencies})
        assert got == want

    @patch("builtins.open", new_callable=mock_open())
    def test_make_results_table(self, mock_open_file, mocker):
        populate_jinja_template_mock = mocker.patch(
            "libraries_io_scraper.make_results_table.populate_jinja_template"
        )

        populate_jinja_template_mock.return_value = "stuff"

        test_dependencies = [
            Dependency(name="@types/node", version="16.18.59"),
        ]

        make_results_table(test_dependencies)

        mock_open_file.assert_called_once_with("dependencies.md", "w")
        mock_open_file.return_value.__enter__().write.assert_called_once_with(
            populate_jinja_template_mock.return_value
        )
