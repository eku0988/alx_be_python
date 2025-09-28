# shopping_list_manager.py

def display_menu():
    """Display the shopping list menu options."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []  # Array (list) to store items

    while True:
        display_menu()  # Call the display_menu function

        try:
            choice = int(input("Enter your choice: "))  # Choice input as a number
        except ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"✅ '{item}' added to the shopping list.")
            else:
                print("⚠️ Item name cannot be empty.")

        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"🗑️ '{item}' removed from the shopping list.")
            else:
                print(f"⚠️ '{item}' not found in the shopping list.")

        elif choice == 3:
            if shopping_list:
                print("\n🛒 Current Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("⚠️ The shopping list is empty.")

        elif choice == 4:
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
