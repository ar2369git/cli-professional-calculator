# tests/test_main.py

from cli_professional_calculator.calculator.main import process_command
from unittest.mock import patch

def test_add_command():
    history = []
    result = process_command("2 + 3", history)
    assert result == "5.0"
    assert history == ["2.0 + 3.0 = 5.0"]

def test_invalid_operator():
    history = []
    result = process_command("2 ^ 3", history)
    assert result == "Error: Unsupported operation"

def test_invalid_format():
    history = []
    result = process_command("2 +", history)
    assert result == "Invalid format. Use: <number> <operation> <number>"

def test_division_by_zero():
    history = []
    result = process_command("5 / 0", history)
    assert result == "Error: Cannot divide by zero."

def test_help_output_exact():
    history = []
    expected = "Format: <number> <operation> <number> (e.g. 5 + 3)\nCommands: help, history, exit"
    result = process_command("help", history)
    assert result == expected

def test_history_output_with_data():
    history = ["1.0 + 1.0 = 2.0"]
    result = process_command("history", history)
    assert result == "1.0 + 1.0 = 2.0"

def test_history_output_empty():
    history = []
    result = process_command("history", history)
    assert result == "No history yet."

def test_invalid_number_format():
    history = []
    result = process_command("five + 2", history)
    assert result == "Error: could not convert string to float: 'five'"

def test_unexpected_exception():
    history = []
    with patch("cli_professional_calculator.calculator.main.CalculationFactory.create") as mock_create:
        mock_create.side_effect = Exception("kaboom")
        result = process_command("2 + 3", history)
        assert result == "Unexpected error: kaboom"
