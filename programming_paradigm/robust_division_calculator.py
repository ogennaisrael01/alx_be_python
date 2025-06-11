# Robust division calculator

def safe_divide(numerator, denominator):
    numerator = float(numerator)
    denominator = float(denominator)
    try:
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    
    except ValueError:
        print("Error: Please enter numeric values.")
