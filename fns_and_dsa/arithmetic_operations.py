def perform_operation(num1: float, num2: float, operation: str):
    # normalize operation string to be safe if caller didn't pre-process it
    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            # return a clear message the main program can display
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
