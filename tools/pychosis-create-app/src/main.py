import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

from rich import pretty
from rich.console import Console
from rich import print
from rich.filesize import decimal
from rich.markup import escape
from rich.text import Text
from rich.tree import Tree


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

def main():
    load_dotenv(find_dotenv(), override=False)


    pychosis_root_directory_path = os.getenv("PYCHOSIS_ROOT_DIRECTORY")
    if not pychosis_root_directory_path:
        raise RuntimeError("PYCHOSIS_ROOT_DIRECTORY environment variable is not set")

    with console.status("[bold purple]Creating Pychosis Project App...[/]"):
        pychosis_root_directory = Path(pychosis_root_directory_path)
        tree = Tree(
            f":open_file_folder:  [bold purple]{pychosis_root_directory}[/]",
            guide_style="bold bright_blue",
        )

        pychosis_project_directories = []
        for path in pychosis_root_directory.iterdir():
            branch_style = BRANCH_STYLE_BY_TYPE.get(path.name.lower(), BRANCH_STYLE_BY_TYPE["default"])
            _add_pychosis_project_recursive(path, pychosis_project_directories, tree, branch_style=branch_style)

        console.rule("[bold red]💥 Pychosis Projects 💥")
        console.print(tree)

        # import time
        # time.sleep(2)

def _add_pychosis_project_recursive(path: Path, projects: list[Path], tree: Tree, branch_style: str = "") -> None:
    if not path.is_dir():
        return
    if path.name in IGNORE_DIRS:
        return
    if (path / "pyproject.toml").exists():
        return

    pychosis_config_file = path / PYCHOSIS_CONFIG_FILE
    is_pychosis_project_dir = pychosis_config_file.exists()
    if not is_pychosis_project_dir:
        return

    projects.append(path)
    style = "dim" if path.name.startswith("__") else ""
    branch = tree.add(
        f"[bold magenta]:open_file_folder: [{branch_style}]{escape(path.name)}[/]",
        style=style,
        guide_style=style,
    )

    for subdir in path.iterdir():
        if subdir.is_dir():
            _add_pychosis_project_recursive(subdir, projects, branch, branch_style=branch_style)


if __name__ == "__main__":
    main()
