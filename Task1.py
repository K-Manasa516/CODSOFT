import os
import pickle

class CustomToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if self.tasks:
            print("Your Custom To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your custom to-do list is empty.")

    def update_task(self, index, new_task):
        if index >= 1 and index <= len(self.tasks):
            self.tasks[index - 1] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def remove_task(self, index):
        if index >= 1 and index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task removed successfully.")
        else:
            print("Invalid task index.")

    def save_tasks(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.tasks, f)

    def load_tasks(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                self.tasks = pickle.load(f)
                print("Custom to-do list loaded successfully.")
        else:
            print("File does not exist.")


def main():
    custom_todo_list = CustomToDoList()

    save_file = "custom_todo.pkl"
    custom_todo_list.load_tasks(save_file)

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Remove Task")
        print("5. Save and Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            custom_todo_list.add_task(task)
        elif choice == '2':
            custom_todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter the index of the task to update: "))
            new_task = input("Enter the new task: ")
            custom_todo_list.update_task(index, new_task)
        elif choice == '4':
            index = int(input("Enter the index of the task to remove: "))
            custom_todo_list.remove_task(index)
        elif choice == '5':
            custom_todo_list.save_tasks(save_file)
            print("Custom to-do list saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
