from pathlib import Path

import yaml

from libraries_io_scraper.dependency_operations import (
    Dependency,
    parse_dependency_string,
)


def parse_dependencies_file(dependencies: str) -> dict[str, list[Dependency]]:
    print(dependencies)
    return {
        k: [parse_dependency_string(d) for d in v]
        for k, v in yaml.safe_load(Path(dependencies).read_text()).items()
    }
