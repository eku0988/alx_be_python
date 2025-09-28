# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operation.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): One of 'add', 'subtract', 'multiply', 'divide'

    Returns:
        float: result of the operation
        None: if division by zero or invalid operation
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return None
        return num1 / num2
    else:
        return None
