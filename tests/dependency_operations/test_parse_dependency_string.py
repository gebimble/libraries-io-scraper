from libraries_io_scraper.dependency_operations import parse_dependency_string


class TestParseDependencyString:

    def test_no_errors(self):
        parse_dependency_string('numpy<1.20.0')

    def test_expected_behaviour(self):
        dep = parse_dependency_string('numpy<1.20.0')
        assert dep.name == 'numpy'
        assert dep.version == '1.20.0'
