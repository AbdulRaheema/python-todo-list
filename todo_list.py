import os

file_name = "tasks.txt"

# load tasks from file
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        tasks = file.read().splitlines()
else:
    tasks = []

while True:
    print("\n====== TO DO LIST ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)

        with open(file_name, "w") as file:
            for t in tasks:
                file.write(t + "\n")

        print("Task saved!")

    elif choice == "2":
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks):
                print(i + 1, task)

    elif choice == "3":
        num = int(input("Enter task number to remove: "))

        if 0 < num <= len(tasks):
            tasks.pop(num - 1)

            with open(file_name, "w") as file:
                for t in tasks:
                    file.write(t + "\n")

            print("Task removed.")
        else:
            print("Invalid number")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
