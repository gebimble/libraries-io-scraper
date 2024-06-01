from typing import Callable

from loguru import logger
import click

from libraries_io_scraper.dependency_operations import node, python
from libraries_io_scraper.make_results_table import make_results_table


DEFAULT_OUTPUT = "dependencies.md"
DEFAULT_TEMPLATE = "src/libraries_io_scraper/results_table/markdown_table_template.j2"


@click.group()
def lios():  # pragma: no cover
    return None


def dependencies_to_markdown_report(
    dependency_file: str, output: str, template: str, parser: Callable, platform: str
) -> None:
    dependencies = parser(dependencies=dependency_file)

    for deps in dependencies.values():
        for dep in deps:
            dep.get_sourcerank(platform)
            dep.get_information(platform)

    make_results_table(dependencies, output_file=output,
                       template_file=template)

    return None


@lios.command()
@click.argument("dependency_file")
@click.option("-o", "--output", default=DEFAULT_OUTPUT)
@click.option("-t", "--template", default=DEFAULT_TEMPLATE)
def py(dependency_file: str, output: str, template: str):
    logger.debug(f"Executing with {dependency_file=}, {output=}, {template=}")
    dependencies_to_markdown_report(
        dependency_file=dependency_file,
        output=output,
        template=template,
        parser=python.parse_dependencies_file,
        platform="pypi",
    )
    return None


@lios.command()
@click.argument("dependency_file")
@click.option("-o", "--output", default=DEFAULT_OUTPUT)
@click.option("-t", "--template", default=DEFAULT_TEMPLATE)
def npm(dependency_file: str, output: str, template: str):
    logger.debug(f"Executing with {dependency_file=}, {output=}, {template=}")
    dependencies_to_markdown_report(
        dependency_file=dependency_file,
        output=output,
        template=template,
        parser=node.parse_dependencies_file,
        platform="npm",
    )
    return None
