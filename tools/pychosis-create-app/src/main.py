import os
from pathlib import Path

from dotenv import find_dotenv, load_dotenv
from rich.prompt import Prompt

from constants import console
from steps.pyproject_override import step_pyproject_override
from tree_selector import TreeSelectorApp


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

    project_path.mkdir(parents=True)

    # Run 'uv init' inside the project_path
    with console.status(f"[bold purple]Creating PyChosis Project using uv in {project_path}...[/]"):
        result = os.system(f'cd "{project_path}" && uv init')
        if result != 0:
            console.print(f"[bold red]ERROR:[/] Failed to run 'uv init' in {project_path}", style="white on red")
            quit(1)

        step_pyproject_override(project_path)


if __name__ == "__main__":
    main()
