from functools import partial
from enum import Enum, unique
from datetime import datetime


class TodoListApp:
    """
    A simple to-do list application.

    :Methods:
        - __init__: Initializes the TodoListApp instance with an empty task list.
        - add_task: Adds a new task to the to-do list.
        - reverse_task_status: Reverses the status of a task (done/undone).
        - delete_task: Deletes a task from the to-do list.
        - list_tasks: Lists all tasks, with optional sorting.
        - process_input_int: Processes and validates integer input from the user (Static Method).
        - interact_with_app: Handles user interactions with the application menu.
        - print_menu: Prints the application menu (Static Method).
        - run: Runs the to-do list application, enabling user interactions.
    """

    def __init__(self):
        """
        Initializes the TodoListApp instance. Creates an empty list to store tasks.
        """
        self.tasks = []

    def add_task(self, message, priority):
        """
        Adds a new task to the to-do list.

        :param message: The task description.
        :type message: str
        :param priority: The task priority.
        :type priority: int
        """
        task = self.Task(message, priority)
        self.tasks.append(task)
        print("Task added successfully.")

    def reverse_task_status(self, index):
        """
        Reverses the status of a task (done/undone).

        :param index: The index of the task in the list.
        :type index: int
        """
        if index < len(self.tasks):
            task = self.tasks[index]
            task.done = not task.done
            status = "done" if task.done else "undone"
            print(f"Task marked as {status}.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        """
        Deletes a task from the to-do list.

        :param index: The index of the task in the list.
        :type index: int
        """
        if index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

    def list_tasks(self, sort_by=""):
        """
        Lists all tasks, with optional sorting.

        :param sort_by: The sorting criterion ('date', 'priority', 'alphabetically'). Default is 'date'.
        :type sort_by: str
        """
        if not self.tasks:
            print("No tasks available.")
            return
        if sort_by and sort_by.upper() not in self.Sort.__members__.keys():
            print(f"Invalid sorting option: {sort_by}")
            return
        sort = self.Sort[sort_by.upper()] if sort_by else self.Sort.DATE
        tasks = sorted(self.tasks, key=sort.value)
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")

    @staticmethod
    def process_input_int(request_message):
        """
        Processes and validates integer input from the user.

        :param request_message: The prompt to be displayed to the user.
        :type request_message: str
        :rtype: int
        """
        while True:
            try:
                return int(input(request_message))
            except ValueError:
                print("Invalid number. Please try again.")

    def interact_with_app(self):
        """
        Handles user interactions with the application menu.
        """
        self.print_menu()
        choice = self.Option(self.process_input_int("Enter your choice: "))
        match choice:
            case self.Option.ADD:
                message = input("Enter task message: ")
                priority = self.process_input_int("Enter task priority: ")
                self.add_task(message, priority)
            case self.Option.MARK:
                print("These are your current tasks:")
                self.list_tasks()
                done_index = self.process_input_int("Enter the index of the task to mark as done/undone: ") - 1
                self.reverse_task_status(done_index)
            case self.Option.DELETE:
                print("These are your current tasks:")
                self.list_tasks()
                delete_index = self.process_input_int("Enter the index of the task to delete: ") - 1
                self.delete_task(delete_index)
            case self.Option.LIST:
                keys = [key.lower() for key in self.Sort.__members__.keys()]
                sort_by = input(f"Enter sorting option ({ '/'.join(keys) }). Default is date: ")
                self.list_tasks(sort_by)
            case self.Option.EXIT:
                print("Exiting the application. Goodbye!")
                exit()
            case _:
                print("Invalid choice. Please try again.")

    @staticmethod
    def print_menu():
        """
        Prints the application menu.
        """
        print("\n--- Todo List Application ---")
        for option in TodoListApp.Option:
            print(option)

    def run(self):
        """
        Runs the to-do list application, enabling user interactions.
        """
        while True:
            self.interact_with_app()

    class Task:
        """
        Represents a task in the to-do list.

        :Methods:
            - __init__: Initializes a Task instance with message, priority, creation date, and done status.
        """
        def __init__(self, message, priority):
            """
            Initializes a Task instance with message, priority, creation date, and done status.

            :param message: The task description.
            :type message: str
            :param priority: The task priority.
            :type priority: int
            """
            self.message = message
            self.priority = priority
            self.creation_date = datetime.now()
            self.done = False

        def __str__(self):
            status = "X" if self.done else " "
            message = self.message
            priority = self.priority
            creation_date = self.creation_date
            return f"[{status}] {message} (Priority: {priority}, Created on: {creation_date})"

    @unique
    class Option(Enum):
        ADD = 1
        MARK = 2
        DELETE = 3
        LIST = 4
        EXIT = 5

        def __str__(self):
            match self:
                case self.ADD: return f"{self.value}. Add Task"
                case self.MARK: return f"{self.value}. Mark Task as Done/Undone"
                case self.DELETE: return f"{self.value}. Delete Task"
                case self.LIST: return f"{self.value}. List Tasks"
                case self.EXIT: return f"{self.value}. Exit"
                case _: raise NotImplementedError("Unknown option.")

    class Sort(Enum):
        DATE = partial(lambda task: task.creation_date)
        PRIORITY = partial(lambda task: task.priority)
        ALPHABETICALLY = partial(lambda task: task.message.lower())
