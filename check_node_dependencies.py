import argparse
from pathlib import Path
from libraries_io_scraper.main import get_dependencies_sourcerank_node
from libraries_io_scraper.node_dependency_operations import parse_node_dependencies_file

parser = argparse.ArgumentParser()
parser.add_argument(
    "dependencies", type=Path, help="Relative location of your package.json file"
)

args = parser.parse_args()

parsed_dependencies = parse_node_dependencies_file(dependencies=args.dependencies)
get_dependencies_sourcerank_node(parsed_dependencies)
