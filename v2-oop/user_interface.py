from datetime import date
from business_logic import TaskService, UserService, Task


def login(user_service):
    """Prompt for credentials and return the username if valid."""
    users = user_service.get_all_users()
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        for user in users:
            if user.username == username and user.check_password(password):
                print(f"\nWelcome, {username}!")
                return username
        print("Invalid credentials. Please try again.")


def add_task(task_service, username):  # receive the logged-in username
    """Prompt for task details and add the task to the system."""
    today = date.today().strftime("%d %b %Y")
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (e.g., 01 Jan 2023): ")

    task = Task(
        username=username,
        title=title,
        description=description,
        assigned_date=today,
        due_date=due_date,
        completed="No"
    )
    task_service.add_task(task)
    print("Task added successfully.")


def view_all_tasks(task_service):
    """Display all tasks in the system."""
    tasks = task_service.get_all_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Assigned to: {task.username}")
            print(f"Assigned Date: {task.assigned_date}")
            print(f"Due Date: {task.due_date}")
            print(f"Completed: {task.completed}")
            print("-" * 40)


def start_application():
    """Start the task management application log in then show the menu loop."""
    task_service = TaskService()
    user_service = UserService()

    username = login(user_service)

    while True:
        print("\nMenu:")
        print("a  - add task")
        print("va - view all tasks")
        print("e  - exit")

        choice = input("\nEnter your choice: ")

        if choice == "a":
            add_task(task_service, username)
        elif choice == "va":
            view_all_tasks(task_service)
        elif choice == "e":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
