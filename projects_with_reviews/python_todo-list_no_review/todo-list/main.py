"""
This file should NOT be reviewed. Its only purpose is to showcase the
functionality of the todo-list program. In what follows, a brief
specification of the program is provided:

This is simple to-do list app that supports adding and removing elements,
marking them as done/undone, and ordering alphabetically, by date or by
priority (default is by date). The user interacts with the app via CLI, with
a menu that allows to select the desired action. When removing or marking
elements as done/undone, the current list of elements is printed to the
console, so that the user can provide the index of the element to remove or
mark as done/undone.
"""


from todo_list import TodoListApp


if __name__ == "__main__":
    todo_app = TodoListApp()
    todo_app.run()
