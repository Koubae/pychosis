from pathlib import Path

from rich import pretty
from rich.console import Console


IGNORE_DIRS: tuple[str, ...] = (".venv", ".git", "docs")
PYCHOSIS_CONFIG_FILE = '.pychosis'
BRANCH_STYLE_BY_TYPE = {
    "default": "bold white",
    "experiments": "bold magenta",
    "projects": "bold cyan",
    "tests": "bold red",
    "scripts": "bold yellow",
    "configs": "bold magenta",
    "models": "bold black",
    "tools": "bold green",
}

pretty.install()
console = Console(color_system="truecolor", force_terminal=True)

ROOT_PATH = Path.cwd()
TEMPLATES_PATH = ROOT_PATH / "templates"

PYTHON_SUPPORTED_VERSIONS = ("3.14", "3.13", "3.12", "3.11", "3.10", "3.9", "3.8", "3.7")
