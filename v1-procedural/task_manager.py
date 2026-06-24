from datetime import date, datetime

# ========== Functions ==========


def register_a_user():
    """Registers a new user by saving their credentials to user.txt."""
    new_username = input("Enter new username: ")

    # Check for duplicate username before proceeding
    if new_username in users:
        print("Username already exists! Please try a different username.")
    else:
        # Ask for password only if username is unique
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm password: ")

        # Verify both passwords match
        if new_password == confirm_password:
            # Append new credentials to user.txt in correct format
            with open("user.txt", "a+") as file:
                file.seek(0, 2)  # Move to end of file
                if file.tell() > 0:  # Check file is not empty
                    file.seek(file.tell() - 1)  # Move back one character
                    if file.read(1) != "\n":  # Add newline if missing
                        file.write("\n")
                # Write new username and password separated by ", "
                file.write(new_username + ", " + new_password + "\n")
            # Add in-memory dictionary for duplicate check
            users[new_username] = new_password
            print("User successfully registered!")
        else:
            print("Passwords do not match. Please try again.")


def add_task():
    """Prompts user to enter task details and saves to tasks.txt."""
    # Get today's date automatically in readable format
    today = date.today().strftime("%d %b %Y")  # String format

    # Collect task details from user input
    assigned_username = input("Enter username of person assigned to task: ")
    task_title = input("Enter task title: ")
    task_description = input("Enter task description: ")
    due_date = input("Enter due date (e.g. 10 Jun 2026): ")

    # Fill automatically by the program
    assigned_date = today
    completed = "No"

    # Append new task to tasks.txt in correct format
    with open("tasks.txt", "a+") as file:
        # Ensure file ends with newline before appending
        file.seek(0, 2)  # Move to end of file
        if file.tell() > 0:  # Check file is not empty
            file.seek(file.tell() - 1)  # Move back one character
            if file.read(1) != "\n":  # Add newline if missing
                file.write("\n")
        # Write all 6 task fields separated by ", "
        file.write(assigned_username + ", " + task_title + ", " +
                   task_description + ", " + assigned_date + ", " +
                   due_date + ", " + completed + "\n")
    print("Task successfully added!")


def view_all_tasks():
    """Reads tasks.txt and displays all tasks in a user-friendly format."""
    # Open and read all lines from tasks.txt
    with open("tasks.txt", "r") as file:
        lines = file.readlines()

    # Display each task with clearly labelled fields
    for line in lines:
        # strip() removes \n, split() separates fields
        parts = line.strip().split(", ")
        print("-" * 40)
        print(f"Task:             {parts[1]}")
        print(f"Assigned to:      {parts[0]}")
        print(f"Date assigned:    {parts[3]}")
        print(f"Due date:         {parts[4]}")
        print(f"Task Complete?    {parts[5]}")
        print(f"Task description: {parts[2]}")
    print("-" * 40)


def get_valid_task_number(num_tasks):
    """Recursively prompts user until a valid task number or -1 is entered."""
    try:
        # Ask user to select a task number
        task_number = int(input("Enter task number or -1 to return: "))

        # Base case — user chooses to return to main menu
        if task_number == -1:
            return -1
        # Invalid range — recurse and ask again
        elif task_number < 1 or task_number > num_tasks:
            print("Invalid task number. Please try again.")
            return get_valid_task_number(num_tasks)
        # Valid number — return it to the caller
        else:
            return task_number

    # Non-integer input — recurse and ask again
    except ValueError:
        print("Please enter a number only!")
        return get_valid_task_number(num_tasks)


def view_my_tasks(username):
    """Displays only the current user's assigned tasks."""
    # Open and read all lines from tasks.txt
    with open("tasks.txt", "r") as file:
        lines = file.readlines()
    # Stores actual line positions
    user_task_indices = []

    # Tracks sequential display number for user's tasks
    task_count = 0

    # Filter and display each task assigned to current user with numbers
    for index, line in enumerate(lines, 1):
        parts = line.strip().split(", ")
        if parts[0] == username:
            task_count += 1
            user_task_indices.append(index)
            print("-" * 40)
            # Display sequential number for user to select
            print(f"Task {task_count}:")
            print(f"Task:             {parts[1]}")
            print(f"Assigned to:      {parts[0]}")
            print(f"Date assigned:    {parts[3]}")
            print(f"Due date:         {parts[4]}")
            print(f"Task Complete?    {parts[5]}")
            print(f"Task description: {parts[2]}")
    print("-" * 40)

    # If no tasks assigned, notify user and return to menu
    if not user_task_indices:
        print("No tasks have been assigned to you yet.")
        return

    # Get valid task number within user's visible tasks
    task_number = get_valid_task_number(len(user_task_indices))

    # Return to main menu if user enters -1
    if task_number == -1:
        return

    # Map display number to actual line index in tasks.txt
    actual_index = user_task_indices[task_number - 1]

    # Ask which task user wants to select
    task_choice = input("What would you like to do? "
                        "c - mark complete, e - edit: ")

    # Mark task as complete
    if task_choice == "c":
        # Read all tasks into a list
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        # Split selected task into individual parts
        parts = tasks[actual_index - 1].strip().split(", ")
        # Prevent silently re-writing Yes over to Yes
        if parts[5] == "Yes":
            print("Task is already complete!")
        else:
            # Update completed field from No to Yes
            parts[5] = "Yes"

            # Rejoin parts and update the task in the list
            tasks[actual_index - 1] = ", ".join(parts) + "\n"

            # Rewrite entire file with updated task
            with open("tasks.txt", "w") as file:
                for task in tasks:
                    file.write(task)
            print("Task marked as complete!")

    # Edit task
    elif task_choice == "e":
        # Read all tasks into a list
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        # Split selected task into individual parts
        parts = tasks[actual_index - 1].strip().split(", ")

        # Completed tasks cannot be edited
        if parts[5] == "Yes":
            print("Task already complete - cannot edit!")
        else:
            # Ask which one to edit
            edit_task_choice = input("What would you like to edit? "
                                     "u - username, d - due date: ")

            # Edit assigned username
            if edit_task_choice == "u":
                new_username = input("Enter new username: ")
                parts[0] = new_username  # Update username
                updated_line = ", ".join(parts) + "\n"  # Rejoin parts
                tasks[actual_index - 1] = updated_line   # Update task list
                with open("tasks.txt", "w") as file:    # Rewrite file
                    for task in tasks:
                        file.write(task)
                print("Task updated!")

            # Edit due date
            elif edit_task_choice == "d":
                new_due_date = input("Enter new due date: ")
                parts[4] = new_due_date  # Update due date field
                updated_line = ", ".join(parts) + "\n"  # Rejoin parts
                tasks[actual_index - 1] = updated_line   # Update task list
                with open("tasks.txt", "w") as file:    # Rewrite file
                    for task in tasks:
                        file.write(task)
                print("Task updated!")


def view_completed_tasks():
    """Displays only tasks that have been marked as complete."""
    # Open and read all lines from tasks.txt
    with open("tasks.txt", "r") as file:
        lines = file.readlines()

    # Filter and display only completed tasks
    for line in lines:
        parts = line.strip().split(", ")
        if parts[5] == "Yes":  # Check completed field
            print("-" * 40)
            print(f"Task:             {parts[1]}")
            print(f"Assigned to:      {parts[0]}")
            print(f"Date assigned:    {parts[3]}")
            print(f"Due date:         {parts[4]}")
            print(f"Task Complete?    {parts[5]}")
            print(f"Task description: {parts[2]}")
    print("-" * 40)


def delete_tasks():
    """Displays numbered tasks and allows admin to delete a selected task."""
    # Read all tasks into a list
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    # Display each task with a number for selection
    for index, task in enumerate(tasks, 1):
        parts = task.strip().split(", ")
        print(f"{index}. {parts[1]}")

    # Ask admin which task number to delete
    task_number = get_valid_task_number(len(tasks))
    if task_number == -1:
        return

    # Remove selected task from list (adjust for 0-based index)
    del tasks[task_number - 1]

    # Rewrite entire file without the deleted task
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task)
    print("Task deleted!")


def generate_reports():
    """Generates task_overview.txt and user_overview.txt with statistics."""
    # Read all tasks from tasks.txt
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    # ---- task_overview.txt statistics ----
    total_tasks = len(tasks)

    # Count completed tasks
    completed_tasks = 0
    for task in tasks:
        parts = task.strip().split(", ")
        if parts[5] == "Yes":
            completed_tasks += 1

    # Count uncompleted tasks
    uncompleted_tasks = 0
    for task in tasks:
        parts = task.strip().split(", ")
        if parts[5] == "No":
            uncompleted_tasks += 1

    # Use .date() on both sides to strip time for accurate date comparison
    today = datetime.today().date()

    # Count overdue tasks (uncompleted and past due date)
    overdue_tasks = 0
    for task in tasks:
        parts = task.strip().split(", ")
        # Convert due date string to datetime for comparison
        due_date = datetime.strptime(parts[4], "%d %b %Y").date()
        if parts[5] == "No" and due_date < today:
            overdue_tasks += 1

    # Calculate percentages (guard against division by zero)
    if total_tasks > 0:
        percentage_incomplete = round(
            (uncompleted_tasks / total_tasks) * 100, 2)
        percentage_overdue = round((overdue_tasks / total_tasks) * 100, 2)
    else:
        percentage_incomplete = 0
        percentage_overdue = 0

    # Write task statistics to task_overview.txt
    with open("task_overview.txt", "w") as file:
        file.write("----- Task Overview -----\n")
        file.write(f"Total tasks:            {total_tasks}\n")
        file.write(f"Completed tasks:        {completed_tasks}\n")
        file.write(f"Uncompleted tasks:      {uncompleted_tasks}\n")
        file.write(f"Overdue tasks:          {overdue_tasks}\n")
        file.write(f"Percentage incomplete:  {percentage_incomplete}%\n")
        file.write(f"Percentage overdue:     {percentage_overdue}%\n")

    # user_overview.txt statistics
    total_users = len(users)

    # Write user statistics to user_overview.txt
    with open("user_overview.txt", "w") as file:
        file.write("----- User Overview -----\n")
        file.write(f"Total users: {total_users}\n")
        file.write(f"Total tasks: {total_tasks}\n\n")

        # Calculate and write stats for each user
        for username in users:
            # Count tasks assigned to this user
            user_tasks = 0
            for task in tasks:
                parts = task.strip().split(", ")
                if parts[0] == username:
                    user_tasks += 1

            # Count completed tasks for this user
            user_completed = 0
            for task in tasks:
                parts = task.strip().split(", ")
                if parts[0] == username and parts[5] == "Yes":
                    user_completed += 1

            # Count overdue tasks for this user
            user_overdue = 0
            for task in tasks:
                parts = task.strip().split(", ")
                due_date = datetime.strptime(parts[4], "%d %b %Y").date()
                if parts[0] == username and parts[5] == "No" \
                        and due_date < today:
                    user_overdue += 1

            # Calculate per-user percentages (guard against division by zero)
            if user_tasks > 0:
                percent_assigned = round((user_tasks / total_tasks) * 100, 2)
                percent_completed = round(
                    (user_completed / user_tasks) * 100, 2)
                percent_incomplete = 100 - percent_completed
                percent_overdue = round((user_overdue / user_tasks) * 100, 2)
            else:
                percent_assigned = 0
                percent_completed = 0
                percent_incomplete = 0
                percent_overdue = 0

            # Write this user's statistics
            file.write(f"\n--- {username} ---\n")
            file.write(f"Tasks assigned:          {user_tasks}\n")
            file.write(f"% of total tasks:        {percent_assigned}%\n")
            file.write(f"% completed:             {percent_completed}%\n")
            file.write(f"% still to complete:     {percent_incomplete}%\n")
            file.write(f"% overdue:               {percent_overdue}%\n")

    print("Reports generated successfully!")


def display_statistics():
    """Displays contents of task_overview.txt
    and user_overview.txt on screen."""
    try:
        # Read and display task overview
        with open("task_overview.txt", "r") as file:
            print(file.read())
        # Read and display user overview
        with open("user_overview.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        # If files don't exist yet, generate them first then display
        print("Generating reports first...")
        try:
            generate_reports()
            display_statistics()  # Recursive call after generating
        except FileNotFoundError:
            # Make sure the tasks.txt file
            # exists in the same folder
            print("tasks.txt not found. "
                  "Please ensure tasks.txt "
                  "exists in the same folder.")


# ========== Load Users ==========

# Open user.txt and read all registered users
with open("user.txt", "r") as file:
    lines = file.readlines()

# Store username-password pairs in a dictionary for fast lookup
users = {}
for line in lines:
    # strip() removes \n, split() separates username and password
    parts = line.strip().split(", ")
    users[parts[0]] = parts[1]


# ========== Login ==========

# Keep asking until valid credentials are provided
logged_in = False

while not logged_in:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:
        # Username found — now verify password
        if password == users[username]:
            logged_in = True
            print(f"\nWelcome, {username}!")
        else:
            print("Wrong password. Please try again.")
    else:
        print("Username not found. Please try again.")


# ========== Main Menu ==========

# Keep displaying menu until user chooses to exit
while True:
    # Admin sees full menu including restricted options
    if username == "admin":
        print("\nPlease select one of the following options:")
        print("r  - register a user")
        print("a  - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("vc - view completed tasks")
        print("del - delete a task")
        print("gr - generate reports")
        print("ds - display statistics")
        print("e  - exit")
    else:
        # Non-admin sees limited menu
        print("\nPlease select one of the following options:")
        print("a  - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("e  - exit")

    choice = input("\nEnter your choice: ")

    if choice == "r":
        # Only admin can register users
        if username == "admin":
            register_a_user()
        else:
            print("Not available. Please choose another option.")
    elif choice == "a":
        add_task()
    elif choice == "va":
        view_all_tasks()
    elif choice == "vm":
        view_my_tasks(username)
    elif choice == "vc":
        # Only admin can view completed tasks
        if username == "admin":
            view_completed_tasks()
        else:
            print("Not available. Please choose another option.")
    elif choice == "del":
        # Only admin can delete tasks
        if username == "admin":
            delete_tasks()
        else:
            print("Not available. Please choose another option.")
    elif choice == "gr":
        # Only admin can generate reports
        if username == "admin":
            generate_reports()
        else:
            print("Not available. Please choose another option.")
    elif choice == "ds":
        # Only admin can display statistics
        if username == "admin":
            display_statistics()
        else:
            print("Not available. Please choose another option.")
    elif choice == "e":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
