from typing import Any

from pprint import pprint as pp

from urllib import parse
import requests  # type: ignore

from libraries_io_scraper.config import settings
from libraries_io_scraper.wait_timer import wait_a_second


BASE_URL = 'https://libraries.io/api/'


@wait_a_second
def get_project_data(name: str, platform: str) -> dict[str, Any]:
    return requests.get(
        BASE_URL + f"{platform}/{parse.quote(name, safe='')}?api_key={settings.API_KEY}"
    ).json()


@wait_a_second
def get_project_sourcerank(name: str, platform: str) -> dict[str, Any]:
    return requests.get(
        BASE_URL + f"{platform}/{parse.quote(name, safe='')}/sourcerank?api_key={settings.API_KEY}"
    ).json()


if __name__ == "__main__":
    args = ('@babel/runtime', 'npm')
    pp(get_project_data(*args))
    sourcerank_response = get_project_sourcerank(*args)
    pp(sourcerank_response)
    pp(
        'Sourcerank (closer to ~30 is better, >30 is excellent): '
        f'{sum(sourcerank_response.values())}'
    )
