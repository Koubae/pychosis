import os
from pathlib import Path

from dotenv import find_dotenv, load_dotenv
from rich import pretty
from rich.console import Console
from rich.prompt import Prompt

from tree_selector import TreeSelectorApp


pretty.install()
console = Console(color_system="truecolor", force_terminal=True)


def main() -> None:
    load_dotenv(find_dotenv(), override=False)

    pychosis_root_directory_path = os.getenv("PYCHOSIS_ROOT_DIRECTORY")
    if not pychosis_root_directory_path:
        raise RuntimeError("PYCHOSIS_ROOT_DIRECTORY environment variable is not set")

    with console.status("[bold purple]Creating Pychosis Project App...[/]"):
        pychosis_root_directory = Path(pychosis_root_directory_path)

        project_dir_selector = TreeSelectorApp(root_path=pychosis_root_directory)
        project_dir_selected = project_dir_selector.run()
        console.print(f"[green]Selected folder: [/] :open_file_folder: [bold]{project_dir_selected}[/]")

    project_name = Prompt.ask("[bold cyan]Enter your project's name[/]")
    console.print(f"New Project name: {project_name}", style="bold green")

    project_path = Path(project_dir_selected) / project_name
    if project_path.exists():
        console.print(
            f"[bold red]ERROR:[/bold red] Name '{project_name}' already exists in {project_dir_selected}",
            style="white on red",
        )
        quit(1)


if __name__ == "__main__":
    main()
