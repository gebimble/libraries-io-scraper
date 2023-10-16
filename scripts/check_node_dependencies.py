


from pathlib import Path
from libraries_io_scraper.main import get_dependencies_sourcerank
from libraries_io_scraper.node_dependency_operations import parse_node_dependencies_file


parsed_dependencies = parse_node_dependencies_file(Path("package.json"))
get_dependencies_sourcerank(parsed_dependencies)