import json
from pathlib import Path

from typing import TypedDict
from models import Dependency

class NodePackageJson(TypedDict):
    name: str
    version: str
    dependencies: dict
    devDependencies: dict



def parse_node_dependencies_file(dependencies: Path) -> dict[str, list[Dependency]]:
    dependencies_json: NodePackageJson = json.load(open(dependencies))
    return {"dependencies":[Dependency(name=d, version=dependencies_json["dependencies"][d])  for d in dependencies_json["dependencies"].keys()],
            "tools":[Dependency(name=d, version=dependencies_json["devDependencies"][str(d)])  for d in dependencies_json["devDependencies"].keys()]}
    


