from pathlib import Path

from constants import TEMPLATES_PATH, console


def step_git_setup(project_path: Path) -> None:
    console.log("[bold yellow][STEP]:[/] setting up git for this project")

    with open(project_path / ".gitattributes", "w") as f:
        with open(TEMPLATES_PATH / ".gitattributes", "r") as template_f:
            template = template_f.read()
        f.write(template)
    console.log("[bold yellow][STEP]:[/] written .gitattributes")

    with open(project_path / ".gitignore", "w") as f:
        with open(TEMPLATES_PATH / ".gitignore", "r") as template_f:
            template = template_f.read()
        f.write(template)
    console.log("[bold yellow][STEP]:[/] written .gitignore")
