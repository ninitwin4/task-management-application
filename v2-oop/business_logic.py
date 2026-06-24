from datetime import datetime
from data_access import TaskRepository, UserRepository


class Task:
    def __init__(self, username, title, description, assigned_date, due_date,
                 completed):
        self.username = username
        self.title = title
        self.description = description
        self.assigned_date = assigned_date
        self.due_date = due_date
        self.completed = completed

    def is_overdue(self, today):
        """Return True if the task is overdue and not completed."""
        due = datetime.strptime(self.due_date, "%d %b %Y").date()
        return self.completed == "No" and due < today

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = "Yes"


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        """Return True if the provided password matches the user's password."""
        return self.password == password


class TaskService:
    """Coordinates task operations and converts records to Task objects."""

    def __init__(self):
        self.repository = TaskRepository()

    def get_all_tasks(self):
        """Load raw records and convert each to a Task object."""
        records = self.repository.get_task_records()
        tasks = []
        for record in records:
            task = Task(
                username=record[0],
                title=record[1],
                description=record[2],
                assigned_date=record[3],
                due_date=record[4],
                completed=record[5]
            )
            tasks.append(task)
        return tasks

    def add_task(self, task):
        """Add a Task object and save all tasks back to file."""
        tasks = self.get_all_tasks()      # current tasks as objects
        tasks.append(task)                # add the new one
        # Convert every Task object back to a raw record (list of strings)
        records = [self._task_to_record(t) for t in tasks]
        # Hand the raw records to the repository to write them to file
        self.repository.save_task_records(records)

    def _task_to_record(self, task):
        """Convert a Task object into a raw record (list of strings)."""
        return [task.username, task.title, task.description,
                task.assigned_date, task.due_date, task.completed]


class UserService:
    """Coordinates user operations and converts records to User objects."""

    def __init__(self):
        self.repository = UserRepository()

    def get_all_users(self):
        """Load raw records and covert each into a User object."""
        records = self.repository.get_user_records()
        users = []
        for record in records:
            user = User(
                username=record[0],
                password=record[1]
            )
            users.append(user)
        return users
