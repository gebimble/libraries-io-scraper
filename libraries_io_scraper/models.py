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

        self.sourcerank = SourceRank(**response.json())

        return None


class SourceRank(BaseModel):
    basic_info_present: int
    repository_present: int
    readme_present: int
    license_present: int
    versions_present: int
    follows_semver: int
    recent_release: int
    not_brand_new: int
    one_point_oh: int
    dependent_projects: int
    dependent_repositories: int
    stars: int
    contributors: int
    subscribers: int
    all_prereleases: int
    any_outdated_dependencies: int
    is_deprecated: int
    is_unmaintained: int
    is_removed: int
