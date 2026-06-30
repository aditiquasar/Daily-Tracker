name = input("Enter your name: ")
print(f"\nWelcome, {name}!")

tasks = []

while True:

    print("\n===== DAILY TRACKER =====")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Choose an option: ")



    if choice == "1":

        task = input("Enter task: ")

        tasks.append(task)

        print("Task added!")



    elif choice == "2":

        task = input("Which task did you complete? ")

        if task in tasks:

            tasks.remove(task)

            print("Task completed ✅")

        else:

            print("Task not found.")



    elif choice == "3":

        if len(tasks) == 0:

            print("No tasks yet.")

        else:

            print(f"\n{name}'s Tasks:")

            for task in tasks:

                print("-", task)



    elif choice == "4":

        print(f"\nThank you, {name}! 🌷")

        break



    else:

        print("Invalid choice!")