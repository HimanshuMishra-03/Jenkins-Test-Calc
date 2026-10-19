"""Basic arithmetic operations used by the Jenkins testing practical."""


def add(first: float, second: float) -> float:
    return first + second


def subtract(first: float, second: float) -> float:
    return first - second


def multiply(first: float, second: float) -> float:
    return first * second


def divide(first: float, second: float) -> float:
    return first / second


def calculate(operation: str, first: float, second: float) -> float:
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }
    try:
        calculation = operations[operation]
    except KeyError:
        raise ValueError(f"Unsupported operation: {operation}") from None
    return calculation(first, second)
