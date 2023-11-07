import argparse
from pathlib import Path
from libraries_io_scraper.dependency_operations.node import parse_node_dependencies_file
from make_results_table import make_results_table

parser = argparse.ArgumentParser()
parser.add_argument(
    "dependencies", type=Path, help="Relative location of your package.json file"
)

args = parser.parse_args()

parsed_dependencies = parse_node_dependencies_file(dependencies=args.dependencies)
[d.get_sourcerank("npm") for d in parsed_dependencies["tools"]]
[d.get_sourcerank("npm") for d in parsed_dependencies["dependencies"]]
make_results_table(parsed_dependencies)
