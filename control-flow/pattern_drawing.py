# A square pattern of asterisks (`*`) of user-defined sizes

pattern_size = int(input("Enter the size of the pattern: "))

active = True
while active:

    for i in range(pattern_size):
        print("*" *  pattern_size, end="")
        
        print()
    active = False