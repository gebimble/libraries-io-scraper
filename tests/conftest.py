import json
import pytest


@pytest.fixture
def reserved_characters() -> list[str]:
    return [
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
        r'{"contributions_count":905,"dependent_repos_count":84861,"dependents_count":49932,"deprecation_reason":null,"description":"Fundamental package for array computing in Python","forks":8386,"homepage":"https: // www.numpy.org","keywords":["numpy","python"],"language":"Python","latest_download_url":null,"latest_release_number":"1.25.2","latest_release_published_at":"2023-07-31T14: 50: 49.000Z","latest_stable_release_number":"1.25.2","latest_stable_release_published_at":"2023-07-31T14: 50: 49.000Z","license_normalized":false,"licenses":"BSD-3-Clause","name":"numpy","normalized_licenses":["BSD-3-Clause"],"package_manager_url":"https: // pypi.org/project/numpy/","platform":"Pypi","rank":31,"repository_license":"BSD-3-Clause","repository_status":null,"repository_url":"https: // github.com/numpy/numpy","stars":24175,"status":null}')
