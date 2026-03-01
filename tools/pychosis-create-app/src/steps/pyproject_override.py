from pathlib import Path

from constants import TEMPLATES_PATH, console


def step_pyproject_override(project_path: Path) -> None:
    console.rule("💥 'pyproject.toml' setup 💥")
    with open(project_path / 'pyproject.toml', 'a') as f:
        with open(TEMPLATES_PATH / "pyproject.toml", "r") as template_f:
            template = template_f.read()

        f.write(template)
    console.log("[bold yellow][STEP]:[/] pyproject.toml overwritten ✨✨")
