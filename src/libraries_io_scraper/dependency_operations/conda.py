from pathlib import Path
from typing import Optional

import yaml

from libraries_io_scraper.dependency_operations import parse_dependency_string
from libraries_io_scraper.models import Dependency


def parse_dependencies_file(
    dependencies: str, platform: Optional[str] = None
) -> dict[str, list[Dependency]]:
    conda_dependencies = yaml.safe_load(Path(dependencies).read_text())[
        "dependencies"
    ]

    pip_idx, *_ = [
        i for i, e in enumerate(conda_dependencies) if isinstance(e, dict)
    ]

    pip_dependencies = conda_dependencies.pop(pip_idx)["pip"]

    dependency_list = []

    for platform, dep_list in (
        ("conda", conda_dependencies),
        ("pypi", pip_dependencies),
    ):
        for dep in dep_list:
            dependency_list.append(
                parse_dependency_string(dep, platform=platform)
            )

    return {"dependencies": dependency_list, "tools": []}


#
# def parse_dependencies_file(dependencies: Path) -> DependenciesLists:
#     dependencies_json = yaml.safe_load(Path(dependencies).read_text())
#     print(dependencies_json)
#     deps_list: list[Dependency] = []
#     # all_deps = [d if isinstance(d, str) else None for d in ]
#     all_deps = []
#
#     for d in dependencies_json["dependencies"]:
#         if isinstance(d, str):
#             all_deps.append(d)
#
#         elif isinstance(d, dict) & ("pip" in d.keys()):
#             for p in d["pip"]:
#                 print(p)
#                 all_deps.append(p)
#     # if (dependencies_json["dependencies"]["pip"]):
#     #     all_deps.append()
#
#     for d in all_deps:
#         if d:
#             chunks = re.split("[=<>]", d)
#
#             deps_list.append(
#                 Dependency(
#                     name=chunks[0],
#                     version=chunks[-1] if len(chunks) > 1 else "",
#                 )
#             )
#
#     return {
#         "dependencies": deps_list,
#         "tools": [],
#     }
