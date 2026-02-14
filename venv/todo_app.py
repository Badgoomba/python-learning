def show_menu():
    print("\n==== TODO APP ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def main():
    tasks = load_tasks()

    while True: 
        show_menu()
        choice = input("\nChoose option: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")

        elif choice == "2":
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No Tasks yet!")
        
        elif choice == "3":
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {tasks}")
                num = int(input("Delete task number : ")) - 1
                if 0 <= num < len(tasks):
                    removed = tasks.pop(num)
                    save_tasks(tasks)
                    print(f"Deleted: {removed}")
        elif choice == "4":
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()
