class InvalidOperationError(Exception):
    """Custom exception raised when an unsupported operator is provided."""
    pass


def safe_calculator():
    print("--- Safe Calculator ---")

    while True:
        try:
            # 1. Ask the user for two numeric values
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))

            # 2. Ask for an operation
            operator = input("Enter an operation (+, -, *, /): ").strip()

            # 5. Raise a custom InvalidOperationError for unsupported operators
            if operator not in ['+', '-', '*', '/']:
                raise InvalidOperationError(f"'{operator}' is not a valid operator.")

            # Perform calculation and 4. Handle division by zero
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = num1 / num2

            print(f"Result: {num1} {operator} {num2} = {result}")

            # Exit loop if successful
            break

        except ValueError:
            # 3. Handle invalid numeric input
            print("Error: Invalid numeric input. Please enter valid numbers.")

        except InvalidOperationError as e:
            # Handle the custom operator error
            print(f"Error: {e}")

        except ZeroDivisionError as e:
            # Handle division by zero
            print(f"Error: {e}")

        finally:
            # 7. Finally block that reports completion of each calculation attempt
            print("Calculation attempt completed.")

        # 6. Use a loop so the user can retry
        retry = input("Would you like to try again? (yes/no): ").strip().lower()
        if retry != 'yes' and retry != 'y':
            print("Exiting calculator. Goodbye!")
            break


if __name__ == "__main__":
    safe_calculator()
