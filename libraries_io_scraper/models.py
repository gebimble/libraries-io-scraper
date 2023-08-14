from urllib import parse
from pydantic import BaseModel, field_validator

from libraries_io_scraper.api_operations import get_project_sourcerank


class Dependency(BaseModel):
    name: str
    version: str
    sourcerank: dict[str, int] = None

    @field_validator('version')
    def set_safe_version(cls, version: str) -> str:
        return parse.quote(version, safe='')

    @field_validator('name')
    def set_safe_name(cls, name: str) -> str:
        return parse.quote(name, safe='')

    def get_sourcerank(self, platform: str) -> None:
        response = get_project_sourcerank(
            self.name,
            platform
        )

        if not response.ok:
            return None

        self.sourcerank = response.json()

        return None
