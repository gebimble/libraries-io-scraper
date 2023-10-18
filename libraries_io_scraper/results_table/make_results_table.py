import jinja2

from libraries_io_scraper.models import Dependency

environment = jinja2.Environment(loader=jinja2.FileSystemLoader("./"))
template = environment.get_template("markdown_table_template.j2")
print(template.render(dependencies=[Dependency(name="test", version = "123")]))