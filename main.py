# Imports
import eventHandler
import os


# This will display the current menu

events = {}
def display_menu():
    print("\n===== Event Manager Menu =====")
    print("1. View Events")
    print("2. Add Event")
    print("3. Delete Event")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("Choice 1")
        elif choice == "2":
            print("Choice 2")
        elif choice == "3":
            print("Choice 3")
        elif choice == "4":
            print("Exiting Event Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Perform actions at code running
if __name__ == "__main__":
    if os.path.isdir("data"):
        if os.path.isdir("data/jsonData"):
            print(True)
        else:
            print(False)
    else:
        print(False)
        pass

    main()