def display_menu():
    """
        Menu display
    """
    print("\n Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # add to the shopping list
            add_item = input('Enter item to purchase: ')
            shopping_list.append(add_item)
            print(f"{add_item} added successfully.")

        elif choice == '2':
            # remove from shopping list
            item_to_remove = input("Enter an item to remove from shopping list: ")
            if item_to_remove not in shopping_list:
                print(f"{item_to_remove} is not in shopping list.")
            else:
                shopping_list.remove(item_to_remove)
                print(f"{item_to_remove} removed.")

        elif choice == '3':
            # Display the shopping list
            print("Items in shopping list.")
            for item in shopping_list:
                print(item) 

        elif choice == '4':
            # exit 
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()