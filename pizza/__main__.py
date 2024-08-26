# Copyright (c) 2024 iiPython

# Load pizza for the pyproject script
from . import pizza  # noqa: F401

# Dynamically import our commands
import importlib
from pathlib import Path
[
    importlib.import_module(f"pizza.commands.{file.with_suffix('').name}")
    for file in (Path(__file__).parent / "commands").iterdir()
]
