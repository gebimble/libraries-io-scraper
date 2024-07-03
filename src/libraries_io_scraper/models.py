from typing import Optional
from urllib import parse
from requests import Response

from pydantic import BaseModel, field_validator, computed_field
from loguru import logger

from libraries_io_scraper.api import get_project_sourcerank, get_project_information


class Dependency(BaseModel):
    name: str
    version: Optional[str] = None  # type: ignore
    sourcerank: dict[str, int] = None  # type: ignore
    information: dict[str, str] = None  # type: ignore
    not_found: bool = False

    @field_validator("version")
    def check_safe_version(cls, version: str) -> str:
        parse.quote(version, safe="")
        return version

    @field_validator("name")
    def check_safe_name(cls, name: str) -> str:
        parse.quote(name, safe="")
        return name

    @computed_field  # type: ignore[misc]
    @property
    def safe_name(self) -> str:
        return parse.quote(self.name, safe="")

    @computed_field  # type: ignore[misc]
    @property
    def safe_version(self) -> str:
        return parse.quote(self.version, safe="")

    @computed_field  # type: ignore[misc]
    @property
    def sourcerank_score(self) -> str:
        if not len(set([type(x) for x in self.sourcerank.values()])) == 1:
            breakpoint()

        return (
            None if self.not_found else sum([x for x in self.sourcerank.values() if x])
        )

    @computed_field
    @property
    def shortfalls(self) -> list[str]:
        return [k for k, v in self.sourcerank.items() if v <= 0]

    def bad_response(self, response: Response, platform: str) -> None:
        logger.warning(
            f"Could not find {self.name}"
            f" version: {self.version} on {platform}."
            f" Message: {str(response)}"
        )
        self.not_found = True
        return None

    def not_found_response(self) -> None:
        logger.warning(
            f"{self.name} already established as unable to be found"
            f" on libraries.io; skipping."
        )
        return None

    def get_api_call(
        self, attribute: str, platform: str, api_call: callable
    ) -> dict[str, int]:
        if self.not_found:
            self.not_found_response()
            return None
        
        if attribute == "sourcerank":
            response = api_call(self.name, platform)
        else:
            response = api_call(self.name, platform, self.version)

        if not response.ok:  # type: ignore
            self.bad_response(response, platform)
            return None

        setattr(self, attribute, response.json())  # type: ignore

        return None

    def get_sourcerank(self, platform: str) -> dict[str, int]:
        self.get_api_call("sourcerank", platform, get_project_sourcerank)
        return None

    def get_information(self, platform: str) -> dict[str, int]:
        self.get_api_call("information", platform, get_project_information)
        return None
