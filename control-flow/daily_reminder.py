task = input("Enter your task: ")
priority = input("Priority(high/medium/low): ").lower()
time_bound = input("Is this time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Note: '{task}' is a high priority task and requires immediate attention today!")
        else:
            print(f"Note: '{task}' requires attention but not time bound")

    case "medium":
        if time_bound == "yes":
            print(f"Note: '{task}' is a medium task that requires attention!")
        else:
            print(f"Note: '{task}' doesn't requires much attention")

    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task that requires attention")
        else:
            print(f"Note: '{task}' you can complete them anytime you want")

    case _:
        print("Error")