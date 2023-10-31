from typing import Callable

import click

from libraries_io_scraper.dependency_operations import node, python
from libraries_io_scraper.make_results_table import make_results_table


@click.group()
def libioscrape():  # pragma: no cover
    return None


def dependencies_to_markdown_report(
    dependency_file: str, output: str, parser: Callable, platform: str
) -> None:
    dependencies = parser(dependencies=dependency_file)

    for deps in dependencies.values():
        for dep in deps:
            dep.get_sourcerank(platform)

    make_results_table(dependencies, output=output)

    return None


@libioscrape.command()
@click.argument("dependency_file")
@click.option("-o", "--output")
def py(dependency_file: str, output: str = "./dependencies.md"):
    dependencies_to_markdown_report(
        dependency_file, output, python.parse_dependencies_file, "pypi"
    )
    return None


@libioscrape.command()
@click.argument("dependency_file")
@click.option("-o", "--output")
def npm(dependency_file: str, output: str = "./dependencies.md"):
    dependencies_to_markdown_report(
        dependency_file, output, node.parse_dependencies_file, "npm"
    )
    return None
