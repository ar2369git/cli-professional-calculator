# tests/test_repl.py

import builtins
from unittest.mock import patch
from cli_professional_calculator.calculator import main

def test_repl_exit_immediately(capsys):
    inputs = iter(["exit"])

    with patch.object(builtins, 'input', lambda _: next(inputs)):
        main.repl()

    captured = capsys.readouterr()
    assert "Welcome to CLI Professional Calculator" in captured.out

def test_repl_addition_and_exit(capsys):
    inputs = iter(["2 + 3", "exit"])

    with patch.object(builtins, 'input', lambda _: next(inputs)):
        main.repl()

    captured = capsys.readouterr()
    assert "5.0" in captured.out
