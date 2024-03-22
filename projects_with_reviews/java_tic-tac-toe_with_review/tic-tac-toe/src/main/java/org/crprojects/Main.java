package org.crprojects;

/**
 * This file should NOT be reviewed. Its only purpose is to showcase the
 * functionality of the tic-tac-toe program. In what follows, a brief
 * specification of the program is provided:
 *
 * This is a tic-tac-toe game played via CLI against an agent that is
 * programmed to not lose. The human player plays first. In each turn, the
 * board is printed to the console and the player is asked to enter the
 * coordinates of the square to mark. The game ends when one of the players
 * wins or when the board is full. The game can be repeated as many times as
 * desired.
 */
public class Main {

    public static void main(String[] args) {
        new TicTacToe().start();
    }
}
