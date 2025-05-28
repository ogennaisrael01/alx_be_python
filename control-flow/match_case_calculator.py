#  a simple calculator that takes two numbers and an operator from the user.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")

# match-case statement to perform addition, subtraction, multiplication, or division.
match operator: 
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        try:
            result = num1 / num2
            print(f"The result is {result}")
        except ZeroDivisionError: # handles error if dividing by zero is attempted
            print("Can't divide by zero")
    
        
    case _:
        print("Don't have a calculation on this operator") # notifies user if unsurppoted operator is entered 


