def perform_operation(num1, num2, operation):
    """
    A simple calculator function
    """

    if operation == "add":
        return num1 + num2 
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print("Error: Can't divide by zero")
            return None
        return num1 / num2
    else:
         print("Don't have a calculation on this operator")
           