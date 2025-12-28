"""Main CLI interface for the Console Task App."""

import sys
from src.service import TodoService
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

# Global console instance
console = Console()


def render_header():
    """Render the application header with Rich styling."""
    console.clear()
    header = Panel("[bold blue]TODO APPLICATION[/bold blue]", expand=False)
    console.print(header)


def render_menu():
    """Display the main menu options using Rich styling."""
    menu_items = [
        "[bold yellow][1][/][/] [bold white]Add Task[/]",
        "[bold yellow][2][/][/] [bold white]View List[/]",
        "[bold yellow][3][/][/] [bold white]Update Task[/]",
        "[bold yellow][4][/][/] [bold white]Delete Task[/]",
        "[bold yellow][5][/][/] [bold white]Mark Complete[/]",
        "[bold yellow][6][/][/] [bold white]Exit[/]"
    ]

    console.print("\n[bold blue]Main Menu[/bold blue]")
    for item in menu_items:
        console.print(item)


def display_tasks(tasks):
    """Display all tasks in a formatted table using Rich."""
    if not tasks:
        console.print("[yellow]No tasks found.[/yellow]")
        return

    table = Table(title="Task List", show_header=True, header_style="bold blue")
    table.add_column("Status", style="green", width=8)
    table.add_column("ID", style="cyan", width=10)
    table.add_column("Title", style="white")
    table.add_column("Description", style="dim")

    for task in tasks:
        status = "✅" if task.completed else "○"
        table.add_row(status, task.id, task.title, task.description or "")

    console.print(table)


def get_user_input(prompt: str) -> str:
    """Get input from user with proper error handling using Rich Prompt."""
    try:
        return Prompt.ask(f"[bold blue]{prompt}[/bold blue]")
    except KeyboardInterrupt:
        console.print("\n[yellow]Exiting...[/yellow]")
        sys.exit(0)
    except EOFError:
        console.print("\n[yellow]Exiting...[/yellow]")
        sys.exit(0)


def main():
    """Main application loop."""
    service = TodoService()

    render_header()
    console.print("[bold green]Welcome to Console Task Manager![/bold green]")

    while True:
        try:
            render_header()
            render_menu()
            choice = get_user_input("Choose an option (1-6)")

            if choice == "1":
                # Add Task
                title = get_user_input("Enter task title: ")
                if not title:
                    console.print("[red]Error: Task title cannot be empty![/red]")
                    continue

                description = get_user_input("Enter task description (optional): ")
                try:
                    task = service.add_task(title, description)
                    console.print(f"[green]Task added successfully![/green] ID: [cyan]{task.id}[/cyan]")
                except ValueError as e:
                    # Use plain print for error messages to avoid Rich markup issues
                    print(f"Error: {str(e)}")

            elif choice == "2":
                # View List
                tasks = service.get_all_tasks()
                display_tasks(tasks)

            elif choice == "3":
                # Update Task
                task_id = get_user_input("Enter task ID to update: ")
                task = service.get_task_by_id(task_id)
                if not task:
                    console.print("[red]Error: Task not found![/red]")
                    continue

                console.print(f"[yellow]Updating task: {task.title}[/yellow]")
                new_title = get_user_input("Enter new title (press Enter to keep current): ")
                new_description = get_user_input("Enter new description (press Enter to keep current): ")

                # Only update if user provided new values
                if new_title:
                    task.title = new_title
                if new_description:
                    task.description = new_description

                console.print("[green]Task updated successfully![/green]")

            elif choice == "4":
                # Delete Task
                task_id = get_user_input("Enter task ID to delete: ")
                if service.delete_task(task_id):
                    console.print("[green]Task deleted successfully![/green]")
                else:
                    console.print("[red]Error: Task not found![/red]")

            elif choice == "5":
                # Mark Complete
                task_id = get_user_input("Enter task ID to mark complete: ")
                task = service.get_task_by_id(task_id)
                if not task:
                    console.print("[red]Error: Task not found![/red]")
                    continue

                task.completed = not task.completed
                status = "completed" if task.completed else "incomplete"
                console.print(f"[green]Task marked as {status}![/green]")

            elif choice == "6":
                # Exit
                console.print("[bold green]Thank you for using Console Task Manager![/bold green]")
                break

            else:
                console.print("[red]Invalid option. Please choose 1-6.[/red]")

        except KeyboardInterrupt:
            console.print("\n[yellow]Exiting...[/yellow]")
            break
        except Exception as e:
            # Simple error handling without Rich markup to avoid parsing issues
            print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()