"""
This file should NOT be reviewed. Its only purpose is to showcase the
functionality of the maze-generator program. In what follows, a brief
specification of the program is provided:

This program generates a random maze of dimension AxB, where both A and B
are positive numbers. Both the upper left and lower right vertical walls of the
maze are open. The maze generated always has one and only one path from the
start to the end. The maze is printed to the console.
"""


from maze_generator import make_maze


if __name__ == '__main__':
    print(make_maze())
