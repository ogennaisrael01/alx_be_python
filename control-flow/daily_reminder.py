# This script prompts the user to enter a task, its priority, and whether it is time-bound.
# It then uses a match-case statement to provide a reminder message based on the priority and time constraint.

task = input("Enter your task: ")
priority = input("Priority(high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

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