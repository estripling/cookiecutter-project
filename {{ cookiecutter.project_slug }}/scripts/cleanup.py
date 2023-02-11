"""A script to clean up Python cache files and directories."""

import pathlib
import shutil


def main():
    cwd = pathlib.Path(".")
    file_extensions = ["*.py[co]", ".coverage", ".coverage.*"]
    directories = ["__pycache__", ".pytest_cache", ".ipynb_checkpoints"]

    for file_extension in file_extensions:
        for pathlib.path in cwd.rglob(file_extension):
            print(f"deleting {pathlib.path}")
            pathlib.path.unlink()

    for directory in directories:
        for pathlib.path in cwd.rglob(directory):
            print(f"deleting {pathlib.path}")
            shutil.rmtree(pathlib.path.absolute(), ignore_errors=False)


if __name__ == "__main__":
    main()
