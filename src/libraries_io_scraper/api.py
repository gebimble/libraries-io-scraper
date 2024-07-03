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
    if len(name.split("%3D")) > 1:
        true_name = name.split("%3D")[0]
        true_version = name.split("%3D")[1]
        criteria = f"{platform}/{true_name}/{true_version}/dependencies"
    else:
        criteria = f"{platform}/{name}"
        
    url = BASE_URL + criteria + f"?api_key={settings.API_KEY}"
    return requests.get(
        url
        # fmt: on
    )


# fmt: off
@wait_a_second
def get_project_sourcerank(
        name: str,
        platform: str
) -> requests.Response:
    logger.debug(f"Getting sourcerank data for {name} hosted on {platform} from libraries.io")
    if len(name.split("%3D")) > 1:
        true_name = name.split("%3D")[0]
        criteria = f"{platform}/{true_name}"
    else:
        criteria = f"{platform}/{name}"
    return requests.get(
        BASE_URL
        + criteria
        + f"/sourcerank?api_key={settings.API_KEY}"
    )
# fmt: on
