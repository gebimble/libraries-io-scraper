import re

from libraries_io_scraper.models import Dependency


SEMVER_PATTERN = re.compile(
    r"(\w*)([<>=!~^])((0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?)"  # noqa: E501
)


def parse_dependency_string(dependency: str) -> Dependency:
    match = SEMVER_PATTERN.match(dependency)
    return Dependency(name=match.group(1), version=match.group(3))
