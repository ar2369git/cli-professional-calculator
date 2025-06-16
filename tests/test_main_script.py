# tests/test_main_script.py

import os
import runpy
import sys
from unittest.mock import patch

import pytest

def test_main_script_runs_and_exits(capsys):
    # Path to your main.py
    main_path = os.path.join(
        os.path.dirname(__file__),
        os.pardir,
        "cli_professional_calculator",
        "calculator",
        "main.py"
    )

    # Simulate a single 'exit' input to break out of the REPL
    with patch('builtins.input', return_value='exit'):
        # Run the script as __main__
        runpy.run_path(main_path, run_name="__main__")

    # Capture stdout
    captured = capsys.readouterr()
    assert "Welcome to CLI Professional Calculator! Type 'help' for options." in captured.out
