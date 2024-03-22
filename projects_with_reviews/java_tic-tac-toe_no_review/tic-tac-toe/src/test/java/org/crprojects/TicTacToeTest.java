package org.crprojects;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

/**
 * This file should NOT be reviewed, nor should your code review comments
 * revolve around including more tests. However, feel free to run the
 * tests or to include more, e.g., to understand how the program works
 * or to verify certain program functionality.
 */
public class TicTacToeTest {

    private TicTacToe ticTacToe;

    @BeforeEach
    public void setUp() {
        ticTacToe = new TicTacToe();
    }

    @Test
    public void computerMoveMustBe8Test() {
        // Mock wins and winStates to avoid NullPointerException:
        ticTacToe.wins = new int[8][3];
        ticTacToe.winStates = new int[8][6];
        // Human is about to win if they play at position 8:
        ticTacToe.grid = new char[][]{
            {' ', ' ', ' '},
            {' ', 'O', ' '},
            {'X', 'O', ' '}
        };
        // Computer played at position 1 and human played at positions 2 and 5:
        ticTacToe.moves = new HashMap<>(Map.of(
                TicTacToe.Player.COMPUTER,
                new HashSet<>(Set.of(1)),
                TicTacToe.Player.HUMAN,
                new HashSet<>(Set.of(2, 5))
        ));
        // The computer weights are updated to prioritize corners and position 8:
        ticTacToe.weights = new int[]{
                0, 0, 3,
                2, 0, 2,
                3, 5, 3
        };

        assertEquals(8, ticTacToe.compMove());
    }

    @Test
    public void putTest() {
        ticTacToe.grid = new char[][]{
            {'O', ' ', ' '},
            {' ', 'X', ' '},
            {' ', ' ', ' '}
        };
        assertEquals(' ', ticTacToe.grid[2][0]);
        ticTacToe.put(1, TicTacToe.Player.COMPUTER);
        assertEquals('X', ticTacToe.grid[2][0]);
    }
}