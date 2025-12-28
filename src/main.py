"""Main CLI interface for the Console Task App."""

import sys
from src.service import TodoService


def display_menu():
    """Display the main menu options."""
    print("\n=== Console Task Manager ===")
    print("1. Add Task")
    print("2. View List")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete")
    print("6. Exit")
    print("===========================")


def display_tasks(tasks):
    """Display all tasks in a formatted list."""
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- Task List ---")
    for task in tasks:
        status = "✓" if task.completed else "○"
        print(f"[{status}] {task.id}: {task.title}")
        if task.description:
            print(f"    {task.description}")
    print("------------------")


def get_user_input(prompt: str) -> str:
    """Get input from user with proper error handling."""
    try:
        return input(prompt).strip()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except EOFError:
        print("\nExiting...")
        sys.exit(0)


def main():
    """Main application loop."""
    service = TodoService()

    print("Welcome to Console Task Manager!")

    while True:
        try:
            display_menu()
            choice = get_user_input("Choose an option (1-6): ")

            if choice == "1":
                # Add Task
                title = get_user_input("Enter task title: ")
                if not title:
                    print("Error: Task title cannot be empty!")
                    continue

                description = get_user_input("Enter task description (optional): ")
                try:
                    task = service.add_task(title, description)
                    print(f"Task added successfully! ID: {task.id}")
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == "2":
                # View List
                tasks = service.get_all_tasks()
                display_tasks(tasks)

            elif choice == "3":
                # Update Task
                task_id = get_user_input("Enter task ID to update: ")
                task = service.get_task_by_id(task_id)
                if not task:
                    print("Error: Task not found!")
                    continue

                print(f"Updating task: {task.title}")
                new_title = get_user_input("Enter new title (press Enter to keep current): ")
                new_description = get_user_input("Enter new description (press Enter to keep current): ")

                # Only update if user provided new values
                if new_title:
                    task.title = new_title
                if new_description:
                    task.description = new_description

                print("Task updated successfully!")

            elif choice == "4":
                # Delete Task
                task_id = get_user_input("Enter task ID to delete: ")
                if service.delete_task(task_id):
                    print("Task deleted successfully!")
                else:
                    print("Error: Task not found!")

            elif choice == "5":
                # Mark Complete
                task_id = get_user_input("Enter task ID to mark complete: ")
                task = service.get_task_by_id(task_id)
                if not task:
                    print("Error: Task not found!")
                    continue

                task.completed = not task.completed
                status = "completed" if task.completed else "incomplete"
                print(f"Task marked as {status}!")

            elif choice == "6":
                # Exit
                print("Thank you for using Console Task Manager!")
                break

            else:
                print("Invalid option. Please choose 1-6.")

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()