import json
import re
from pathlib import Path

import yaml
from typing import TypedDict
from libraries_io_scraper.models import Dependency

class NodePackageJson(TypedDict):
    name: str
    version: str
    dependencies: dict
    devDependencies: dict



def parse_node_dependencies_file(dependencies: Path) -> dict[str, list[Dependency]]:
    dependencies_json: NodePackageJson = json.load(open(dependencies))
    return {"dependencies":[Dependency(name=d, version=dependencies_json["dependencies"][d])  for d in dependencies_json["dependencies"].keys()],
            "tools":[Dependency(name=d, version=dependencies_json["devDependencies"][str(d)])  for d in dependencies_json["devDependencies"].keys()]}
    


