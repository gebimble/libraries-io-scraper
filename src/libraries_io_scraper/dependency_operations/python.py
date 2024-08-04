from typing import Optional
from pathlib import Path
import yaml

from libraries_io_scraper.dependency_operations import Dependency
from libraries_io_scraper.dependency_operations import parse_dependency_string


def parse_dependencies_file(
    dependencies: str, platform: Optional[str] = None
) -> dict[str, list[Dependency]]:
    return {
        k: [parse_dependency_string(d, platform=platform) for d in v]
        for k, v in yaml.safe_load(Path(dependencies).read_text()).items()
    }
