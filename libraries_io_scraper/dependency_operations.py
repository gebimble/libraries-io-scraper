import re
from pathlib import Path

import yaml

from libraries_io_scraper.models import Dependency


SEMVER_PATTERN = re.compile(
    r"(\w*)([<>=!~^])((0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?)")


def parse_dependency_string(dependency: str) -> Dependency:
    match = SEMVER_PATTERN.match(dependency)
    return Dependency(name=match.group(1), version=match.group(3))


def parse_dependencies_file(dependencies: Path) -> dict[str, list[Dependency]]:
    return {
        k: [parse_dependency_string(d) for d in v]
        for k, v in yaml.safe_load(Path(dependencies).read_text()).items()
    }
