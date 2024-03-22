"""
This module provides a simple implementation of the Tic-Tac-Toe game.

Functions:
    my_turn(xo, board): Plays a turn for the AI using a random choice.
    my_better_turn(xo, board): Plays a more intelligent turn for the AI, trying to win or block.
    play(): Starts and manages the game loop.

Variables:
    board: Represents the game board as a list.
    wins: A tuple of tuples representing winning combinations.

Example:
    To start a game, simply call the `play()` function.

Note:
    The game is played in the console and requires user input for the human player's turns.
"""
import random

board = list('123456789')
wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6))


def my_turn(xo, board):
    """
    Plays a turn for the AI using a random choice from available spaces.

    :param xo: The symbol ('X' or 'O') to be placed on the board.
    :type xo: str
    :param board: The game board.
    :type board: list
    :returns: The chosen position as a string.
    :rtype: str
    """
    options = [b for b in board if b not in 'XO']
    choice = random.choice(options)
    board[int(choice) - 1] = xo
    return choice


def my_better_turn(xo, board):
    """
    Plays a more strategic turn for the AI.

    Tries to find a winning move for itself or block the opponent's winning move. If neither is possible, it chooses a position randomly.

    :param xo: The symbol ('X' or 'O') to be placed on the board.
    :type xo: str
    :param board: The game board.
    :type board: list
    :returns: The chosen position as a string.
    :rtype: str
    """
    ox = 'O' if xo == 'X' else 'X'
    one_block = None
    options = [int(s) - 1 for s in [b for b in board if b not in 'XO']]
    for choice in options:
        brd = board[:]
        brd[choice] = xo
        for w in wins:
            b = brd[w[0]]
            if b in 'XO' and all(board[i] == b for i in w):
                break
        if one_block is None:
            brd[choice] = ox
            for w in wins:
                b = brd[w[0]]
                if b in 'XO' and all(board[i] == b for i in w):
                    one_block = choice
    else:
        choice = one_block if one_block is not None else random.choice(options)
    board[choice] = xo
    return choice


def play():
    """
    Starts and manages the Tic-Tac-Toe game loop.

    Continuously alternates between the AI's and the human player's turns, checks for game completion, and declares the result of the game.
    """
    print(__doc__)
    while not all(b in 'XO' for b in board):
        print('\n-+-+-\n'.join('|'.join(board[x:x + 3]) for x in (0, 3, 6)))
        print('\nI go at', my_better_turn('X', board))
        
        s = None
        for w in wins:
            b = board[w[0]]
            if b in 'XO' and all(board[i] == b for i in w):
                s = b, [i + 1 for i in w]
                break
        if s:
            print('\n-+-+-\n'.join('|'.join(board[x:x + 3]) for x in (0, 3, 6)))
            print("\n%s wins along %s" % s)
            break

        if not all(b in 'XO' for b in board):
            print('\n-+-+-\n'.join('|'.join(board[x:x + 3]) for x in (0, 3, 6)))
            # Call my_turn(xo, board) below for it to play itself
            options = [b for b in board if b not in 'XO']
            choice = input("\nPut your %s in any of these positions: %s "
                            % ('O', ''.join(options))).strip()
            board[int(choice) - 1] = 'O'
            print('\nYou went at', choice)

            s = None
            for w in wins:
                b = board[w[0]]
                if b in 'XO' and all(board[i] == b for i in w):
                    s = b, [i + 1 for i in w]
                    break
            if s:
                print('\n-+-+-\n'.join('|'.join(board[x:x + 3]) for x in (0, 3, 6)))
                print("\n%s wins along %s" % s)
                break
    else:
        print('\nA draw')
