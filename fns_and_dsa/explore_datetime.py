from datetime import datetime, timedelta

def display_current_datetime():
    """
    Current datetime
    """
    current_date = datetime.now()

    return current_date.strftime("%Y-%m-%d   %H:%M:%S")


def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    """    
    Calculate a future date by adding a specified number of days to the current date
    """
    future_date = datetime.now() + timedelta(days=days_to_add)
    return future_date.strftime("%Y-%m-%d")

def main():
    print("Current Date and Time:", display_current_datetime())
    
    future_date = calculate_future_date()
    print("Future Date:", future_date)

if __name__ == "__main__":
    main()