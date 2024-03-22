from unittest import TestCase
from tic_tac_toe import my_better_turn


class TestTicTacToe(TestCase):
    """
    This file should NOT be reviewed, nor should your code review comments
    revolve around including more tests. However, feel free to run the
    tests or to include more, e.g., to understand how the program works
    or to verify certain program functionality.
    """

    def test_ai(self):
        player = 'X'
        board = list("O23456789")
        choice = my_better_turn(player, board)
        self.assertNotEqual(choice, 1)
        board = list("OXXO56789")
        choice = my_better_turn(player, board)
        self.assertNotIn(choice, range(1, 5))
        board = list("12345OXXO")
        choice = my_better_turn(player, board)
        self.assertNotIn(choice, range(6, 10))
