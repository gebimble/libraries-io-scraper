import json
from urllib import parse
import warnings
from pydantic import BaseModel, field_validator, computed_field

from libraries_io_scraper.api import get_project_sourcerank


class Dependency(BaseModel):
    name: str
    version: str
    sourcerank: dict[str, int] = None  # type: ignore

    @field_validator("version")
    def check_safe_version(cls, version: str) -> str:
        parse.quote(version, safe="")
        return version

    @field_validator("name")
    def check_safe_name(cls, name: str) -> str:
        parse.quote(name, safe="")
        return name

    @computed_field
    @property
    def safe_name(self) -> str:
        return parse.quote(self.name, safe="")

    @computed_field
    @property
    def safe_version(self) -> str:
        return parse.quote(self.version, safe="")

    def get_sourcerank(self, platform: str):
        response = get_project_sourcerank(self.safe_name, platform)

        if not response.ok:  # type: ignore
            warnings.warn(
                f"Could not find {self.name} version: {self.version} on {platform}. Message: {str(response)}"
            )
        else:
            self.sourcerank = response.json()  # type: ignore
