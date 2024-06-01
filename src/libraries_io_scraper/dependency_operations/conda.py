from pathlib import Path

from typing import TypedDict

import yaml
import re
from libraries_io_scraper.dependency_operations import DependenciesLists
from libraries_io_scraper.models import Dependency


class NodePackageJson(TypedDict):
    name: str
    version: str
    dependencies: dict
    devDependencies: dict


def parse_dependencies_file(dependencies: Path) -> DependenciesLists:
    dependencies_json = yaml.safe_load(Path(dependencies).read_text())
    print(dependencies_json)
    deps_list: list[Dependency] = []
    # all_deps = [d if isinstance(d, str) else None for d in ]
    all_deps = []

    for d in dependencies_json["dependencies"]:
        if isinstance(d, str):
            all_deps.append(d)

        elif isinstance(d, dict) & ("pip" in d.keys()):
            for p in d["pip"]:
                print(p)
                all_deps.append(p)
    # if (dependencies_json["dependencies"]["pip"]):
    #     all_deps.append()

    for d in all_deps:
        if d:
            chunks = re.split("[=<>]", d)

            deps_list.append(
                Dependency(
                    name=chunks[0], version=chunks[-1] if len(chunks) > 1 else ""
                )
            )

    return {
        "dependencies": deps_list,
        "tools": [],
    }
