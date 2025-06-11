# Robust division calculator

def safe_divide(numerator, denominator) -> None:
    try:
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        print("Error: cant divide by zero!")
    