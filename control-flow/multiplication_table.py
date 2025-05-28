# prompt the user for a number and print its multiplication table from 1 to 10
number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 10):
    product = number * i
    result = f"{number} * {i} = {product}"
    print(result, end="")
    print()

        
