# cli_professional_calculator/calculator/main.py

from cli_professional_calculator.calculation.factory import CalculationFactory

def process_command(user_input, history):
    if user_input == "help":
        return "Format: <number> <operation> <number> (e.g. 5 + 3)\nCommands: help, history, exit"
    elif user_input == "history":
        return "\n".join(history) if history else "No history yet."
    else:
        try:
            parts = user_input.split()
            if len(parts) != 3:
                return "Invalid format. Use: <number> <operation> <number>"
            a, op, b = float(parts[0]), parts[1], float(parts[2])
            calc = CalculationFactory.create(a, op, b)
            result = calc.execute()
            history.append(f"{a} {op} {b} = {result}")
            return str(result)
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
        except ValueError as ve:
            return f"Error: {ve}"
        except Exception as e:
            return f"Unexpected error: {e}"

def repl():
    print("Welcome to CLI Professional Calculator! Type 'help' for options.")
    history = []
    while True:
        user_input = input("> ").strip().lower()
        if user_input == 'exit':
            break
        output = process_command(user_input, history)
        print(output)

if __name__ == "__main__":
    repl()
