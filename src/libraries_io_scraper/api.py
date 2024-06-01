import requests  # type: ignore

from loguru import logger  # type: ignore

from libraries_io_scraper.config import settings
from libraries_io_scraper.wait_timer import wait_a_second


BASE_URL = "https://libraries.io/api/"


# fmt: off
@wait_a_second
def get_project_information(
        name: str,
        platform: str
) -> requests.Response:
    logger.debug(f"Getting project data for {name} hosted on {platform} from libraries.io")
    return requests.get(
        BASE_URL
        + f"{platform}/{name}?"
        + f"api_key={settings.API_KEY}"
        # fmt: on
    )


# fmt: off
@wait_a_second
def get_project_sourcerank(
        name: str,
        platform: str
) -> requests.Response:
    logger.debug(f"Getting sourcerank data for {name} hosted on {platform} from libraries.io")
    return requests.get(
        BASE_URL
        + f"{platform}/{name}/"
        + f"sourcerank?api_key={settings.API_KEY}"
    )
# fmt: on
