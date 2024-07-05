import requests  # type: ignore

from loguru import logger  # type: ignore

import json
import subprocess


from libraries_io_scraper.config import settings
from libraries_io_scraper.wait_timer import wait_a_second


BASE_URL = "https://libraries.io/api/"


class SimpleResponse:
    def __init__(self, status_response: str, content: str):
        self.status_response = int(status_response)
        self.content = content

    @property
    def ok(self):
        return self.status_response

    def json(self):
        return json.loads(self.content)


def powershell_get(api_string: str) -> SimpleResponse:
    ret = subprocess.Popen(
        [
            "powershell.exe",
            f"$curl_content = Invoke-WebRequest -uri {api_string}",
            "curl_content.StatusCode",
            "curl_content.Content",
        ],
        stdout=subprocess.PIPE,
    ).stdout.reads()

    status_response, *json_parts = ret.split("\n")
    json_output = "".join(json_parts)

    return SimpleResponse(status_response, json_output)


def get_api_response(api_string: str) -> requests.Response | SimpleResponse:
    if settings.ON_SITE:
        return powershell_get(api_string)
    return requests.get(api_string)


# fmt: off
@wait_a_second
def get_project_information(
        name: str,
        platform: str,
        version: str = None
) -> requests.Response:
    logger.debug(f"Getting project data for {name} hosted on {platform} from libraries.io")  # noqa: E501
    criteria = f"{platform}/{name}" + (f"/{version}" if version else "")
    return get_api_response(
        BASE_URL
        + criteria
        + f"?api_key={settings.API_KEY}"
        # fmt: on
    )


@wait_a_second
def get_project_sourcerank(
        name: str,
        platform: str
) -> requests.Response:
    logger.debug(f"Getting sourcerank data for {name} hosted on {platform} from libraries.io")  # noqa: E501
    criteria = f"{platform}/{name}"
    return get_api_response(
        BASE_URL
        + criteria
        + "/sourcerank"
        + f"?api_key={settings.API_KEY}"
    )
