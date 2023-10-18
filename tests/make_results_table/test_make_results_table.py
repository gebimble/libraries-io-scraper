




from pathlib import Path
from unittest.mock import patch, mock_open
from libraries_io_scraper.models import Dependency
from make_results_table import populate_jinja_template, write_template_to_file

class TestMakeResultsTable:

    def test_it_renders_a_valid_markdown_table(self):

        want = """
| Name  | Version | Dependency Type |Rating |
|-------|----|------|--------|
| test | 123 | dependency |None |
| test2 | 567 | dependency |None |
"""


        test_dependencies = [Dependency(name="test", version = "123"), Dependency(name="test2", version = "567")]
        got = populate_jinja_template({"dependency": test_dependencies})
        assert got == want

    @patch('builtins.open', new_callable=mock_open())
    def test_writes_the_output_to_a_markdown_file(self, mock_open_file):

            write_template_to_file("some text")

            mock_open_file.assert_called_once_with('dependency_ratings.md', 'w')
            mock_open_file.return_value.__enter__().write.assert_called_once_with('some text')