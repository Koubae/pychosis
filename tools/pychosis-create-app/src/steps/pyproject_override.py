from pathlib import Path

from constants import TEMPLATES_PATH, console


def step_pyproject_override(project_path: Path) -> None:
    console.log(f"[bold yellow][STEP]:[/] Modifing default 'pyproject.toml' in {project_path}")
    with open(project_path / 'pyproject.toml', 'a') as f:
        with open(TEMPLATES_PATH / "pyproject.toml", "r") as template_f:
            template = template_f.read()

        f.write(template)
