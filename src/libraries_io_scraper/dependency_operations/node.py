import json
from pathlib import Path
from typing import TypedDict


from libraries_io_scraper.dependency_operations import DependenciesLists
from libraries_io_scraper.models import Dependency


class NodePackageJson(TypedDict):
    name: str
    version: str
    dependencies: dict
    devDependencies: dict


def parse_dependencies_file(dependencies: Path) -> DependenciesLists:
    dependencies_json: NodePackageJson = json.load(open(dependencies))
    return {
        "dependencies": [
            Dependency(name=d, version=dependencies_json["dependencies"][d])  # noqa: E501
            for d in dependencies_json["dependencies"].keys()
        ],
        "tools": [
            Dependency(
                name=d, version=dependencies_json["devDependencies"][str(d)]
            )  # noqa: E501
            for d in dependencies_json["devDependencies"].keys()
        ],
    }
