def perform_operation(num1:float, num2:float, operation:str):
    """
    A simple calculator function
    """
    
    match operation: 
        case "+":
            return  num1 + num2 
        case "-":
            return num1 - num2
        case "*":
            return  num1 * num2
        case "/":
            if num2 == 0:
                print("Error: Can't divide by zero")
                return None 
            return num1 / num2
        case _:
            print("Don't have a calculation on this operator") 