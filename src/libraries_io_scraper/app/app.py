from typing import Callable

import click
from loguru import logger

from libraries_io_scraper.dependency_operations import node, python
from libraries_io_scraper.make_results_table import make_results_table


DEFAULT_OUTPUT = "dependencies.md"
DEFAULT_TEMPLATE = (
    "src/libraries_io_scraper/results_table/predeveloped_software.j2"
)


@click.group()
def lios():  # pragma: no cover
    return None


def dependencies_to_markdown_report(
    dependency_file: str,
    output: str,
    template: str,
    parser: Callable,
    platform: str,
) -> None:
    dependencies = parser(dependencies=dependency_file)

    for deps in dependencies.values():
        for dep in deps:
            dep.get_sourcerank(platform)
            dep.get_information(platform)

    make_results_table(dependencies, output_file=output, template_file=template)

    return None


@lios.command()
@click.argument("dependency_file")
@click.option("-o", "--output", default=DEFAULT_OUTPUT)
@click.option("-t", "--template", default=DEFAULT_TEMPLATE)
@click.option("-p", "--platform", default="pypi")
def py(dependency_file: str, output: str, template: str, platform: str):
    """Parses a `python` "dependency file"
    provided in a `.yaml` format.

    The file should contain one or both of the outer keys:

    - dependencies
    - tools

    and under those should contain an unordered list
    of any number of dependencies in the format

    <NAME>(<INEQUALIT><VERSION>)

    where <INEQUALITY> and <VERSION>
    are a pair of optional additions
    (i.e. you can provide a bare dependency/tool name,
    but it is advised that you don't
    in order to retrieve information specific
    to the version of the package you're using.

    An example `.yaml` file can be found in the project README.
    """
    logger.debug(f"Executing with {dependency_file=}, {
                 output=}, {template=}, {platform=}")
    dependencies_to_markdown_report(
        dependency_file=dependency_file,
        output=output,
        template=template,
        parser=python.parse_dependencies_file,
        platform=platform,
    )
    return None


@lios.command()
@click.argument("dependency_file")
@click.option("-o", "--output", default=DEFAULT_OUTPUT)
@click.option("-t", "--template", default=DEFAULT_TEMPLATE)
@click.option("-p", "--platform", default="npm")
def npm(dependency_file: str, output: str, template: str, platform: str):
    logger.debug(f"Executing with {dependency_file=}, {
                 output=}, {template=}, {platform=}")
    dependencies_to_markdown_report(
        dependency_file=dependency_file,
        output=output,
        template=template,
        parser=node.parse_dependencies_file,
        platform=platform,
    )
    return None
