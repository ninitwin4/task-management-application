import unittest
from datetime import date
from business_logic import Task, User


class TestTaskManager(unittest.TestCase):
    """Unit tests for the Task and User business logic classes. """
    def test_check_password_true(self):
        """Test that check_password returns True for the correct password."""
        # Arrange - create a user with a known password
        user = User("admin", "adm1n")
        # Act - check the correct password
        result = user.check_password("adm1n")
        # Assert - the result should be True
        self.assertTrue(result)

    def test_check_password_false(self):
        """Test that check_password returns False for an incorrect password."""
        user = User("admin", "adm1n")
        result = user.check_password("wrongpassword")
        self.assertFalse(result)

    def test_mark_completed(self):
        """Test that mark_completed sets the completed attribute to 'Yes'."""
        # Arrange - a task that is not yet complete
        task = Task("admin", "Title", "Description",
                    "01 Jan 2026", "10 Jan 2026", "No")
        # Act - mark the task as complete
        task.mark_completed()
        # Assert - completed should now be "Yes"
        self.assertEqual(task.completed, "Yes")

    def test_is_overdue(self):
        """Test that is_overdue returns True for a task that is overdue."""
        # Arrange - a task due in the past, not completed
        task = Task("admin", "Title", "Description",
                    "01 Jan 2019", "20 Oct 2019", "No")
        # Act - check against a later "today"
        result = task.is_overdue(date(2026, 6, 18))
        # Assert - it should be overdue
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
