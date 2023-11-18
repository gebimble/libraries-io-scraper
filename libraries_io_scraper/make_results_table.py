import jinja2
from libraries_io_scraper.dependency_operations import DependenciesLists


def make_results_table(
    dependencies: DependenciesLists, output_file: str = "dependencies.md"
):
    output = populate_jinja_template(dependencies=dependencies)
    write_template_to_file(output=output)
    return None


def populate_jinja_template(dependencies: DependenciesLists) -> str:
    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader("libraries_io_scraper/results_table")
    )
    template = environment.get_template("markdown_table_template.j2")
    output = template.render(dependencies=dependencies)
    return output


def write_template_to_file(output: str, output_file: str = "dependencies.md"):
    with open(output_file, "w") as f:
        f.write(output)
    return None
