import requests  # type: ignore

from libraries_io_scraper.config import settings
from libraries_io_scraper.wait_timer import wait_a_second


BASE_URL = "https://libraries.io/api/"


@wait_a_second
def get_project_data(
    name: str,
    version: str,
    platform: str
) -> requests.Response:
    return requests.get(
        BASE_URL
        + f"{platform}/{name}/{version}?"
        + f"api_key={settings.API_KEY}"
    )


@wait_a_second
def get_project_sourcerank(name: str, platform: str) -> requests.Response:
    return requests.get(
        BASE_URL
        + f"{platform}/{name}?"
        + f"sourcerank?api_key={settings.API_KEY}"
    )
