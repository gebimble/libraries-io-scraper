import jinja2

from libraries_io_scraper.models import Dependency


def populate_jinja_template(dependencies: dict[str, list[Dependency]]) -> str:
    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader("libraries_io_scraper/results_table")
    )
    template = environment.get_template("markdown_table_template.j2")
    output = template.render(dependencies=dependencies)
    return output


def write_template_to_file(output: str):
    with open("dependency_ratings.md", "w") as f:
        f.write(output)
    return None


def make_results_table(dependencies: dict[str, list[Dependency]]):
    output = populate_jinja_template(dependencies=dependencies)
    write_template_to_file(output=output)
    return None
