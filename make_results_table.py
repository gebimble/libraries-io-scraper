import jinja2
from libraries_io_scraper.dependency_operations import DependenciesLists

from libraries_io_scraper.models import Dependency


def make_results_table(dependencies: DependenciesLists):
    output = populate_jinja_template(dependencies=dependencies)
    write_template_to_file(output=output)


def populate_jinja_template(dependencies: DependenciesLists) -> str:
    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader("libraries_io_scraper/results_table")
    )
    template = environment.get_template("markdown_table_template.j2")
    output = template.render(dependencies=dependencies)
    return output


def write_template_to_file(output: str):
    with open("dependency_ratings.md", "w") as f:
        f.write(output)
