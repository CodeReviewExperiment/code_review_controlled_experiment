from unittest import TestCase
from maze_generator import make_maze


class TestMaze(TestCase):
    """
    This file should NOT be reviewed, nor should your code review comments
    revolve around including more tests. However, feel free to run the
    tests or to include more, e.g., to understand how the program works
    or to verify certain program functionality.
    """

    def test_N_S_wall(self):
        maze = make_maze(2, 2)
        lines = maze.strip().split("\n")
        north, *_, south = lines
        expected = "+---+---+"
        self.assertEqual(expected, north)
        self.assertEqual(expected, south)

    def test_W_E_wall(self):
        maze = make_maze(2, 2)
        lines = maze.strip().split("\n")
        west = [line[0] for line in lines]
        east = [line[-1] for line in lines]
        expected = ["+", " ", "+", "|", "+"]
        reversed = expected[::-1]
        self.assertEqual(expected, west)
        self.assertEqual(reversed, east)
