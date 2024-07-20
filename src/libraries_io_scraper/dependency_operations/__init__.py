import re
from typing import TypedDict, Optional

from libraries_io_scraper.models import Dependency


SEMVER_PATTERN = re.compile(
    r"(\w*)([<>=!~^])((0|[1-9]\d*)\.(0|[1-9]\d*)?\.?(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?)"  # noqa: E501
)


class DependenciesLists(TypedDict):
    dependencies: list[Dependency]
    tools: list[Dependency]


def parse_dependency_string(
    dependency: str, platform: Optional[str] = None
) -> Dependency:
    match = SEMVER_PATTERN.match(dependency)

    if match:
        return Dependency(
            name=match.group(1),  # type: ignore[union-attr]
            version=match.group(3),  # type: ignore[union-attr]
            platform=platform,
        )

    return Dependency(name=dependency, platform=platform)
