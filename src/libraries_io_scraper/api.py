import requests  # type: ignore

from loguru import logger  # type: ignore

import json
import subprocess


from libraries_io_scraper.config import settings
from libraries_io_scraper.wait_timer import wait_a_second


BASE_URL = "https://libraries.io/api/"


class SimpleResponse:
    def __init__(self, status_code: str, json_content: str):
        self.response = int(status_code)
        self.content = json_content

    @property
    def ok(self):
        return self.response == 200

    def json(self):
        return json.loads(self.content)


def powershell_curl(api_string: str) -> SimpleResponse:
    ret = subprocess.Popen(
        [
            "powershell.exe",
            f"$curl_content=Invoke-WebRequest -uri {api_string};",
            "curl_content.StatusCode;",
            "curl_content.Content;",
        ],
        stdout=subprocess.PIPE,
    )

    status_response, json_content = (
        ret.stdout.read().decode("utf-8").strip().split("\r\n")
    )

    return SimpleResponse(status_response, json_content)


def get_api_response(api_string: str) -> requests.Response | SimpleResponse:
    if settings.ON_SITE:
        return powershell_curl(api_string)
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
