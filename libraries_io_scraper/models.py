from typing import Optional
from urllib import parse

from pydantic import BaseModel, field_validator, computed_field
from loguru import logger

from libraries_io_scraper.api import get_project_sourcerank


class Dependency(BaseModel):
    name: str
    version: Optional[str] = None  # type: ignore
    sourcerank: dict[str, int] = None  # type: ignore

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
        return sum([x for x in self.sourcerank.values()])

    def get_sourcerank(self, platform: str) -> dict[str, int]:
        response = get_project_sourcerank(self.safe_name, platform)

        if not response.ok:  # type: ignore
            logger.warning(
                f"Could not find {self.name} version: {self.version} on {platform}. Message: {str(response)}"
            )

        self.sourcerank = response.json()  # type: ignore
