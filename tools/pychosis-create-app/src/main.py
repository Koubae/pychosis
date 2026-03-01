import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

IGNORE_DIRS: tuple[str, ...] = (".venv", ".git", "docs")
PYCHOSIS_CONFIG_FILE = '.pychosis'

def main():
    load_dotenv(find_dotenv(), override=False)

    pychosis_root_directory_path = os.getenv("PYCHOSIS_ROOT_DIRECTORY")
    if not pychosis_root_directory_path:
        raise RuntimeError("PYCHOSIS_ROOT_DIRECTORY environment variable is not set")

    pychosis_root_directory = Path(pychosis_root_directory_path)
    pychosis_project_directories = []
    for path in pychosis_root_directory.iterdir():
        if not path.is_dir():
            continue
        if path.name in IGNORE_DIRS:
            continue
        if (path / "pyproject.toml").exists():
            continue

        pychosis_config_file = path / PYCHOSIS_CONFIG_FILE
        is_pychosis_project_dir = pychosis_config_file.exists()
        if not is_pychosis_project_dir:
            continue

        print(f"Adding {path} to directory list")
        pychosis_project_directories.append(path)


if __name__ == "__main__":
    main()
