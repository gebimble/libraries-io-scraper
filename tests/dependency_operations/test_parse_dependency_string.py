from libraries_io_scraper.dependency_operations import parse_dependency_string


class TestParseDependencyString:
    def test_no_errors_semver(self):
        parse_dependency_string("numpy=1.20.0")

    def test_no_errors_not_semver(self):
        parse_dependency_string("numpy=1.20")

    def test_no_errors_no_version(self):
        parse_dependency_string("numpy")

    def test_expected_behaviour_semver(self):
        dep = parse_dependency_string("numpy=1.20.0")
        assert dep.name == "numpy"
        assert dep.version == "1.20.0"

    def test_expected_behaviour_not_semver(self):
        dep = parse_dependency_string("numpy=1.20")
        assert dep.name == "numpy"
        assert dep.version == "1.20"

    def test_expected_behaviour_no_version(self):
        dep = parse_dependency_string("numpy")
        assert dep.name == "numpy"
        assert dep.version is None
