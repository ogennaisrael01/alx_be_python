# prompt the user for a number and print its multiplication table from 1 to 10
number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
    print()

        
