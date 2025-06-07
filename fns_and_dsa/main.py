from arithmetic_operations import perform_operation # imported function from arethmetic_operations module

def main():
    """Main function to run the arithmetic operations calculator."""
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: ")) # input first number
    num2 = float(input("Enter the second number: ")) # input second number
    operation = input("Enter the operation (add, subtract, multiply, divide): ").lower() # input operation to do calculation

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()