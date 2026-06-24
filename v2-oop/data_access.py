class TaskRepository:
    """Reads and writes raw task records to tasks.txt."""

    def __init__(self, filename="tasks.txt"):
        self.filename = filename

    def get_task_records(self):
        """Return a list of raw field lists, one per line."""
        records = []
        with open(self.filename, "r") as file:
            for line in file:
                records.append(line.strip().split(", "))
        return records

    def save_task_records(self, records):
        """Write a list of raw field lists back to tasks.txt."""
        with open(self.filename, "w") as file:
            for record in records:
                file.write(", ".join(record) + "\n")


class UserRepository:
    """Reads raw user records from user.txt."""

    def __init__(self, filename="user.txt"):
        self.filename = filename

    def get_user_records(self):
        """Return a list of raw field lists, one per line."""
        records = []
        with open(self.filename, "r") as file:
            for line in file:
                records.append(line.strip().split(", "))  # Raw text
        return records
