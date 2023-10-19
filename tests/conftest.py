import json
import pytest


RESERVED_CHARACTERS = [
    "!",
    "*",
    "'",
    "(",
    ")",
    ";",
    ":",
    "@",
    "&",
    "=",
    "+",
    "$",
    ",",
    "/",
    "?",
    "%",
    "#",
    "[",
    "]",
]


@pytest.fixture
def numpy_sourcerank_return() -> dict[str, int]:
    return json.loads(
        r'{"basic_info_present":1,"repository_present":1,"readme_present":1,"license_present":1,"versions_present":1,"follows_semver":0,"recent_release":1,"not_brand_new":1,"one_point_oh":1,"dependent_projects":10,"dependent_repositories":5,"stars":4,"contributors":2,"subscribers":2,"all_prereleases":0,"any_outdated_dependencies":0,"is_deprecated":0,"is_unmaintained":0,"is_removed":0}'
    )
