tasks = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Quit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(i, "-", t)

    elif choice == "3":
        break

    else:
        print("Invalid choice")


