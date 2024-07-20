from typing import Optional, Any
from urllib import parse
from requests import Response

from pydantic import BaseModel, field_validator, computed_field
from loguru import logger

from libraries_io_scraper.api import (
    get_project_sourcerank,
    get_project_information,
)


class Sourcerank(BaseModel):
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


class Version(BaseModel):
    number: str
    published_at: str
    spdx_expression: str
    original_license: str
    researched_at: Any
    repository_sources: list[str]


class Information(BaseModel):
    contributions_count: int
    dependent_repos_count: int
    dependents_count: int
    deprecation_reason: Any
    description: str
    forks: int
    homepage: str
    keywords: list[str]
    language: str
    latest_download_url: str
    latest_release_number: str
    latest_release_published_at: str
    latest_stable_release_number: str
    latest_stable_release_published_at: str
    license_normalized: bool
    licenses: str
    name: str
    normalized_licenses: list[str]
    package_manager_url: str
    platform: str
    rank: int
    repository_license: str
    repository_status: Any
    repository_url: str
    stars: int
    status: Any
    version: list[Version]


class Dependency(BaseModel):
    name: str
    version: Optional[str] = None  # type: ignore
    platform: Optional[str] = None  # type: ignore
    _sourcerank: Optional[Sourcerank] = None  # type: ignore
    _information: Optional[Information] = None  # type: ignore
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
    def sourcerank(self) -> Sourcerank:
        if self._sourcerank is None:
            response = get_project_sourcerank(self.safe_name, self.platform)

            if not response.ok:  # type: ignore
                self.bad_response(response, self.platform)
                return None

            self._sourcerank = Sourcerank.model_validate(response.json())

        return self._sourcerank

    @computed_field  # type: ignore[misc]
    @property
    def information(self) -> Information:
        if self._information is None:
            response = get_project_information(
                self.safe_name, self.platform, self.version
            )

            if not response.ok:  # type: ignore
                self.bad_response(response, self.platform)
                return None

            self._information = Sourcerank.model_validate(response.json())

        return self._information

    @computed_field  # type: ignore[misc]
    @property
    def sourcerank_score(self) -> int:
        return (
            0
            if self.not_found
            else sum([x for x in self.sourcerank.model_dump().values() if x])
        )

    @computed_field
    @property
    def shortfalls(self) -> list[str]:
        return [k for k, v in self.sourcerank.model_dump().items() if v <= 0]

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
