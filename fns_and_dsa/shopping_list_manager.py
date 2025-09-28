# shopping_list_manager.py

def display_menu():
    """Displays the menu options to the user."""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    """Main function to manage the shopping list."""
    # Start with an empty shopping list
    shopping_list = []

    while True:
        # Show the menu every loop iteration
        display_menu()
        choice = input("Enter your choice: ")

        # Add an item to the list
        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:  # Ensure the item is not empty
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Item cannot be empty.")

        # Remove an item from the list
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' is not in the shopping list.")

        # View all items in the list
        elif choice == '3':
            if shopping_list:
                print("\nCurrent Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is empty.")

        # Exit the program
        elif choice == '4':
            print("Goodbye!")
            break

        # Handle invalid menu choices
        else:
            print("Invalid choice. Please try again.")


# Entry point of the script
if __name__ == "__main__":
    main()
