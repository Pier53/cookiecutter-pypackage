#!/usr/bin/env python
import logging
import shutil
import subprocess
import sys
from pathlib import Path





def run_command(command: list, cwd: Path = None) -> None:
    """
    Runs shell commands using subprocess, with error handling.
    """
    logging.info(f"Running command: {' '.join(command)}")
    try:
        subprocess.run(
            command, check=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as e:
        logging.error(
            f"Error running command {' '.join(command)}: {e.stderr.decode().strip()}"
        )
        sys.exit(1)


def initialize_project_environment(project_path: Path) -> None:
    """
    Initializes a Python project environment using `uv` and installs `ipykernel`.
    """
    if not shutil.which("uv"):
        logging.error("'uv' is not installed or not in the system PATH.")
        sys.exit(1)

    run_command(["uv", "init"], cwd=project_path)
    run_command(["uv", "venv"], cwd=project_path)
    run_command(["uv", "add", "ipykernel"], cwd=project_path)



if __name__ == "__main__":
    # initialize_project_environment(Path("."))
    pass