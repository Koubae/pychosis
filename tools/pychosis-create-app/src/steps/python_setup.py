import shutil
import subprocess
from pathlib import Path

from constants import TEMPLATES_PATH, console


def step_python_setup(project_path: Path, python_version: str) -> None:
    console.rule(f"💥 Python setup ({python_version}) 💥")
    with open(project_path / '.python-version', 'w') as f:
        f.write(f"{python_version}\n")
    console.log("[bold yellow][STEP]:[/] written .python-version")

    with open(project_path / "Makefile", "w") as f:
        with open(TEMPLATES_PATH / "Makefile", "r") as template_f:
            template = template_f.read()
        f.write(template)
    console.log("[bold yellow][STEP]:[/] written Makefile")

    src_path = project_path / "src"
    src_path.mkdir(parents=True)
    with open(src_path / "__init__.py", "w") as f:
        f.write("")

    rm_command = shutil.which("rm")
    if rm_command:
        result = subprocess.run([rm_command, "main.py"], cwd=project_path, check=False)
        if result.returncode != 0:
            console.print(
                f"[bold red]ERROR:[/] Failed to run 'rn main.py' in {project_path}, error: {result.stderr}",
                style="white on red",
            )
    else:
        console.print(
            "[bold yellow]WARNING:[/bold yellow] rm command not found, won't remove main.py created by uv",
            style="white on yellow",
        )

    with open(src_path / "main.py", "w") as f:
        with open(TEMPLATES_PATH / "main.py", "r") as template_f:
            template = template_f.read()
        f.write(template)
    console.log("[bold yellow][STEP]:[/] written main.py")

    console.log("[bold yellow][STEP]:[/] src package created")

    test_path = project_path / "tests"
    test_path.mkdir(parents=True)
    with open(test_path / "__init__.py", "w") as f:
        f.write("")
    with open(test_path / "conftest.py", "w") as f:
        f.write("")
    console.log("[bold yellow][STEP]:[/] tests package created")
