def display_list(todo_list):
    if not todo_list:
        print("To-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' is added.")

def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' is removed.")
    else:
        print("Please enter a valid task number.")
        
def main():
    todo_list = []
    
    while True:
        print("\nTo-Do List Menu:")
        print("1) Display To-Do List")
        print("2) Add Task")
        print("3) Remove Task")
        print("4) Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_list(todo_list)
        elif choice == "2":
            task = input("Enter the task to add: ")
            add_task(todo_list, task)
        elif choice == "3":
            task_index = int(input("Enter the task number to remove: "))
            remove_task(todo_list, task_index)
        elif choice == "4":
            print("To-Do List Closed !")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
