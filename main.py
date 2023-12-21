def display_menu():
    print("\n===== Event Manager Menu =====")
    print("1. View Events")
    print("2. Add Event")
    print("3. Delete Event")
    print("4. Exit")

def main():
    events = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_events(events)
        elif choice == "2":
            add_event(events)
        elif choice == "3":
            delete_event(events)
        elif choice == "4":
            print("Exiting Event Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()