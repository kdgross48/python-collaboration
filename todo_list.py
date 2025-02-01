# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:08:39 2025

@author: gross.ke
"""

# todo_list.py

# todo_list.py

tasks = []  # List to store task descriptions and completion status

#============================================================================== 
def add_task():
    task = input("Enter a new task: ")  # User inputs the task
    tasks.append((task, False))  # Add task with False (not completed)
    print(f'Task "{task}" added!')

#============================================================================== 
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, (task, completed) in enumerate(tasks, 1):
            status = "yes" if completed else "no"
            print(f"{i}. {task} [{status}]")

#============================================================================== 
def mark_completed():
    view_tasks()  # Show all tasks
    task_number = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_number <= len(tasks):
        task, _ = tasks[task_number - 1]
        tasks[task_number - 1] = (task, True)  # Update the tuple
        print(f'Task "{task}" marked as completed!')
    else:
        print("Invalid task number.")

#============================================================================== 
def delete_task():
    view_tasks()  # Show all tasks
    task_number = int(input("Enter the task number to delete: "))
    if 1 <= task_number <= len(tasks):
        removed_task, _ = tasks.pop(task_number - 1)
        print(f'Task "{removed_task}" deleted!')
    else:
        print("Invalid task number.")

#============================================================================== 
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add new task")
        print("2. View all tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()  # Add a new task
        elif choice == "2":
            view_tasks()  # View all tasks
        elif choice == "3":
            mark_completed()  # Mark a task as completed
        elif choice == "4":
            delete_task()  # Delete a task
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break  # Exit the program
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

#============================================================================== 
# Invoke the main function
if __name__ == "__main__":
    main()

#==============================================================================