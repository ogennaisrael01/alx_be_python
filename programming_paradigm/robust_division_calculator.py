# Robust division calculator

def safe_divide(numerator, denomenator) -> None:
    try:
        result = numerator / denomenator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        print("Error: cant divide by zero!")
    