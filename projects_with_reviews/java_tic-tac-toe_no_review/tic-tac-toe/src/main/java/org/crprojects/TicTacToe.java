package org.crprojects;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UncheckedIOException;
import java.util.Arrays;
import java.util.EnumMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Set;
import java.util.random.RandomGenerator;
import java.util.stream.Collectors;

public class TicTacToe {

    private static final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));

    private static final RandomGenerator RNG = new Random();

    // Numbers associated with each cell on the grid
    private static final char[][] POSITION_GRID = {
            {'7', '8', '9'},
            {'4', '5', '6'},
            {'1', '2', '3'}
    };

    private static final char[][] EMPTY_GRID = {
            {' ', ' ', ' '},
            {' ', ' ', ' '},
            {' ', ' ', ' '}
    };

    // Eight possible win scenarios
    static final int[][] DEFAULT_WINS = {
            {7, 8, 9},
            {4, 5, 6},
            {1, 2, 3},
            {7, 4, 1},
            {8, 5, 2},
            {9, 6, 3},
            {7, 5, 3},
            {9, 5, 1}
    };

    // Default weights to drive the computer's decision-making
    private static final int[] DEFAULT_WEIGHTS = {
            3, 2, 3,
            2, 4, 2,
            3, 2, 3
    };

    // Column indexes for the winStates array, to keep track of possible win scenarios
    private static final int KNOT_COUNT = 3;
    private static final int CROSS_COUNT = 4;
    private static final int TOTAL_COUNT = 5;

    int[][] winStates;
    int[][] wins;
    int[] weights;
    char[][] grid;

    Map<Player, Set<Integer>> moves;

    enum Player {

        HUMAN('O'),
        COMPUTER('X');

        private final char mark;

        Player(char mark) {
            this.mark = mark;
        }

        @Override
        public String toString() {
            return String.valueOf(mark);
        }
    }

    private sealed interface Outcome permits Win, Draw {
    }

    private record Win(Player winner) implements Outcome {

        @Override
        public String toString() {
            return winner + " wins";
        }
    }

    private record Draw() implements Outcome {

        @Override
        public String toString() {
            return getClass().getSimpleName();
        }
    }

    /**
     * Starts a match of Tic-Tac-Toe.
     * The game continues until the player decides to stop.
     */
    public void start() {
        System.out.print("Start? ([y]/n): ");
        char choice = ' ';
        try {
            choice = READER.readLine().toLowerCase().charAt(0);
        } catch (IndexOutOfBoundsException ignored) {
            choice = '\0';
        } catch (IOException ex) {
            throw new UncheckedIOException(ex);
        }
        if (choice == 'n') return;
        System.out.println("Use a standard numpad as an entry grid, as so:");
        Map<Player, Integer> scores = new EnumMap<>(Player.class);
        scores.put(Player.HUMAN, 0);
        scores.put(Player.COMPUTER, 0);
        do {
            display(POSITION_GRID);
            winStates = new int[DEFAULT_WINS.length][DEFAULT_WINS[0].length + 3];
            weights = Arrays.copyOf(DEFAULT_WEIGHTS, DEFAULT_WEIGHTS.length);
            wins = Arrays.stream(DEFAULT_WINS).map(int[]::clone).toArray(int[][]::new);
            grid = Arrays.stream(EMPTY_GRID).map(char[]::clone).toArray(char[][]::new);
            moves = Map.of(Player.HUMAN, new HashSet<>(5), Player.COMPUTER, new HashSet<>(4));

            Outcome outcome = null;
            while (outcome == null) {
                System.out.print("What's your move?: ");
                for (;;) {
                    try {
                        int cell = Integer.parseInt(READER.readLine());
                        boolean valid = cell >= 1 && cell <= 9;
                        boolean occupied = weights[cell - 1] == Integer.MIN_VALUE;
                        boolean okay = valid && !occupied;
                        if (!okay) throw new IllegalArgumentException();
                        moves.get(Player.HUMAN).add(cell);
                        for (int i = 0; i < wins.length; i++) {
                            for (int j = 0; j < wins[i].length; j++) {
                                if (wins[i][j] == cell) {
                                    winStates[i][j] = 1;
                                    winStates[i][TOTAL_COUNT]++;
                                    winStates[i][KNOT_COUNT]++;
                                }
                            }
                        }
                        fixWeights();
                        System.out.println();
                        put(cell, Player.HUMAN);
                        outcome = checkForWin();
                        if (outcome != null) break;
                        try {
                            Thread.sleep(1000);
                        } catch (InterruptedException ex) {
                            System.err.print(ex.getMessage());
                            Thread.currentThread().interrupt();
                        }
                        put(compMove(), Player.COMPUTER);
                        outcome = checkForWin();
                    } catch (RuntimeException ignored) {
                        System.out.print("Invalid move. Try again: ");
                    } catch (IOException ex) {
                        throw new UncheckedIOException(ex);
                    }
                }
            }
            if (outcome instanceof Win win) {
                Player player = win.winner;
                int score = scores.get(player);
                scores.put(player, score + 1);
            }
            System.out.println(outcome);
            System.out.println("Score:");
            scores.entrySet().forEach(System.out::println);
            System.out.print("Another? ([y]/n): ");
            try {
                choice = READER.readLine().toLowerCase().charAt(0);
            } catch (IndexOutOfBoundsException ignored) {
                choice = '\0';
            } catch (IOException ex) {
                throw new UncheckedIOException(ex);
            }
        } while (choice != 'n');
        System.out.println("Game over.");
    }

    /**
     * Places a mark ('x' or 'o') in a specified cell on the grid
     * based on the player's move.
     *
     * @param cell   The cell number where the mark is to be placed
     * @param player The player making the move
     */
    void put(int cell, Player player) {
        int ordinal = cell - 1;
        int i = 2 - Math.floorDiv(ordinal, 3);
        int j = ordinal % 3;
        grid[i][j] = player.mark;
        display(grid);
    }


    /**
     * Adjusts the weights of each cell based on the current state of the game.
     */
    private void fixWeights() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (winStates[i][j] == 1) {
                    int weight = wins[i][j] - 1;
                    weights[weight] = Integer.MIN_VALUE;
                }
            }
        }
        for (int i = 0; i < DEFAULT_WINS.length; i++) {
            int[] winState = winStates[i];
            if (winState[TOTAL_COUNT] != 2) continue;
            int k = getIndex(i);
            int weight = wins[i][k] - 1;
            if (winState[CROSS_COUNT] == 2 && weights[weight] != Integer.MIN_VALUE) {
                weights[weight] = 6;
            }
            if (winState[KNOT_COUNT] == 2 && weights[weight] != Integer.MIN_VALUE) {
                weights[weight] = 5;
            }
        }
    }


    /**
     * Returns the index of the empty cell in the i-th win scenario (from 0 to 7).
     */
    private int getIndex(int i) {
        for (int j = 0; j < 3; j++)
            if (winStates[i][j] == 0)
                return j;
        return -1;
    }

    /**
     * Determines the computer's move based on the current game state.
     *
     * @return The cell number chosen by the computer
     */
    int compMove() {
        int max = Integer.MIN_VALUE;
        int cell = 0;
        for (int i = 0; i < weights.length; i++) {
            if (weights[i] > max) {
                max = weights[i];
                cell = i + 1;
            }
        }

        String sequence = moves.get(Player.HUMAN).stream()
                .sorted()
                .map(String::valueOf)
                .collect(Collectors.joining());
        cell = switch (sequence) {
            case "18" -> 7;
            case "19" -> RNG.nextBoolean() ? 2 : 6;
            case "29" -> 3;
            case "37" -> RNG.nextBoolean() ? 4 : 8;
            case "67" -> 9;
            default -> cell;
        };

        moves.get(Player.COMPUTER).add(cell);
        for (int i = 0; i < wins.length; i++) {
            for (int j = 0; j < wins[i].length; j++) {
                if (wins[i][j] == cell) {
                    winStates[i][j] = 1;
                    winStates[i][TOTAL_COUNT]++;
                    winStates[i][CROSS_COUNT]++;
                }
            }
        }
        fixWeights();
        System.out.println("Computer plays: " + cell);
        return cell;
    }

    /**
     * Checks the current game state to determine if there is a winner.
     *
     * @return The outcome of the game, or null if the game is not over
     */
    private Outcome checkForWin() {
        for (int[] win : wins) {
            List<Integer> keys = Arrays.stream(win).boxed().toList();
            if (moves.get(Player.COMPUTER).containsAll(keys)) {
                display(grid);
                return new Win(Player.COMPUTER);
            }
            if (moves.get(Player.HUMAN).containsAll(keys)) {
                display(grid);
                return new Win(Player.HUMAN);
            }
        }

        boolean done = Arrays.stream(weights).noneMatch(weight -> weight != Integer.MIN_VALUE);
        if (!done) return null;
        return new Draw();
    }


    /**
     * Displays the current state of the grid.
     *
     * @param grid The grid to be displayed
     */
    private static void display(char[][] grid) {
        StringBuilder builder = new StringBuilder("\n┌─┬─┬─┐\n│");
        for (int i = 0; i < 3; i++) {
            if (i != 0) builder.append("\n├─┼─┼─┤\n│");
            for (int j = 0; j < 3; j++) {
                builder.append(grid[i][j]).append("│");
            }
        }
        builder.append("\n└─┴─┴─┘\n");
        System.out.println(builder);
    }
}