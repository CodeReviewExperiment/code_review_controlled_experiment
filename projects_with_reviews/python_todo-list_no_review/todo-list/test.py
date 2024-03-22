from unittest import TestCase
from todo_list import TodoListApp


class TestTodoListApp(TestCase):
    """
    This file should NOT be reviewed, nor should your code review comments
    revolve around including more tests. However, feel free to run the
    tests or to include more, e.g., to understand how the program works
    or to verify certain program functionality.
    """

    def setUp(self):
        self.todo = TodoListApp()

    def test_add_task(self):
        self.assertEqual(0, len(self.todo.tasks))
        items = 5
        for i in range(items):
            self.todo.add_task(f"testing {i + 1}", i + 1)
        self.assertEqual(items, len(self.todo.tasks))
        tasks = self.todo.tasks
        for i in range(items):
            self.assertEqual(f"testing {i + 1}", tasks[i].message)
            self.assertEqual(i + 1, tasks[i].priority)

    def test_reverse_task_status(self):
        self.todo.add_task("testing", 1)
        self.assertFalse(self.todo.tasks[0].done)
        self.todo.reverse_task_status(0)
        self.assertTrue(self.todo.tasks[0].done)
        self.todo.reverse_task_status(0)
        self.assertFalse(self.todo.tasks[0].done)

    def test_delete_task(self):
        self.todo.add_task("testing", 1)
        self.assertEqual(1, len(self.todo.tasks))
        self.todo.delete_task(0)
        self.assertEqual(0, len(self.todo.tasks))
