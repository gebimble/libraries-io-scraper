from pathlib import Path

from jinja2 import Template

from libraries_io_scraper.dependency_operations import DependenciesLists


DEFAULT_TEMPLATE = Path(
    "src/libraries_io_scraper/results_table/markdown_table_template.j2"
)


def make_results_table(
    dependencies: DependenciesLists,
    template_file: str = DEFAULT_TEMPLATE,
    output_file: str = "dependencies.md",
):
    output = populate_jinja_template(
        dependencies=dependencies, template=template_file
    )
    write_template_to_file(output=output, output_file=output_file)
    return None


def populate_jinja_template(
    dependencies: DependenciesLists, template: str = DEFAULT_TEMPLATE
) -> str:
    return Template(Path(template).read_text()).render(
        dependencies=dependencies
    )


def write_template_to_file(output: str, output_file: str = "dependencies.md"):
    with open(output_file, "w") as f:
        f.write(output)
    return None
