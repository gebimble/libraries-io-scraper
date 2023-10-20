from pathlib import Path

import click

from libraries_io_scraper.dependency_operations import node, python


@click.group()
def libioscrape():
    return None


@libioscrape.command()
@click.argument("dependency_file", type=click.Path)
def py(dependency_file: Path):
    python.parse_dependencies_file(dependencies=dependency_file)
    return None


@libioscrape.command()
@click.argument("dependency_file", type=click.Path)
def npm(dependency_file: Path):
    node.parse_dependencies_file(dependencies=dependency_file)
    return None
