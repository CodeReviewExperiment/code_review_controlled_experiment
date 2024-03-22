package org.crprojects;

import java.util.Collections;
import java.util.Arrays;

/**
 * The {@code Maze} class represents a maze with a specified width and height.
 * It provides functionality to generate a random maze using a depth-first search algorithm.
 */
public class Maze {

    private final int width;
    private final int height;

    private final int[][] grid;

    private static final String H_WALL_CLOSED = "+---";
    private static final String H_WALL_OPEN = "+   ";
    private static final String V_WALL_CLOSED = "|   ";
    private static final String V_WALL_OPEN = "    ";
    private static final String V_OPEN = " ";
    private static final String V_CLOSED = "|";
    private static final String CORNER = "+";

    /**
     * Constructs a new {@code Maze} with the specified width and height.
     *
     * @param width  the width of the maze
     * @param height the height of the maze
     */
    private Maze(int width, int height) {
        this.width = width;
        this.height = height;
        this.grid = new int[height][width];
    }

    /**
     * Returns a string representation of the maze.
     *
     * @return the string representation of the maze
     */
    @Override
    public String toString() {
        String result = "";
        for (int row = 0; row < height; row++)
            result += toString(row);
        result += H_WALL_CLOSED.repeat(width) + CORNER + '\n';
        return result;
    }

    /**
     * Returns a string representation of a single row in the maze.
     *
     * @param row the row index
     * @return the string representation of the specified row
     */
    private String toString(int row) {
        StringBuilder builder = new StringBuilder();
        for (int column = 0; column < width; column++) {
            boolean closed = (grid[row][column] & 1) == 0;
            builder.append(closed ? H_WALL_CLOSED : H_WALL_OPEN);
        }
        builder.append(CORNER).append('\n');
        for (int column = 0; column < width; column++) {
            if (row == 0 && column == 0) {
                builder.append("    ");
            } else {
                boolean closed = (grid[row][column] & 8) == 0;
                builder.append(closed ? V_WALL_CLOSED : V_WALL_OPEN);
            }
        }
        boolean closed = row == height - 1;
        builder.append(closed ? V_OPEN : V_CLOSED).append('\n');
        return builder.toString();
    }

    /**
     * Generates a random maze with the specified width and height.
     *
     * @param width  the width of the maze
     * @param height the height of the maze
     * @return a randomly generated {@code Maze} object
     * @throws IllegalArgumentException if width or height is not positive
     */
    public static Maze random(int width, int height) {
        if (width <= 0) throw new IllegalArgumentException("Width must be positive");
        if (height <= 0) throw new IllegalArgumentException("Height must be positive");
        Maze maze = new Maze(width, height);
        populate(maze);
        return maze;
    }

    /**
     * Populates the maze with a random path starting from the top-left corner.
     *
     * @param maze the maze to populate
     */
    private static void populate(Maze maze) {
        populate(0, 0, maze);
    }

    /**
     * Recursively populates the maze with a random path from the specified position.
     *
     * @param cx   the current x-coordinate
     * @param cy   the current y-coordinate
     * @param maze the maze to populate
     */
    private static void populate(int cx, int cy, Maze maze) {
        Direction[] directions = Direction.values();
        Collections.shuffle(Arrays.asList(directions));
        for (Direction direction : directions) {
            int nx = cx + direction.dx;
            int ny = cy + direction.dy;
            if (between(nx, maze.width) && between(ny, maze.height) && maze.grid[ny][nx] == 0) {
                maze.grid[cy][cx] |= direction.bit;
                maze.grid[ny][nx] |= direction.opposite.bit;
                populate(nx, ny, maze);
            }
        }
    }

    /**
     * Checks if a value is within the range [0, upper).
     *
     * @param value the value to check
     * @param upper the upper bound (exclusive)
     * @return {@code true} if the value is in range; {@code false} otherwise
     */
    private static boolean between(int value, int upper) {
        return value >= 0 && value < upper;
    }

    /**
     * Enum representing the four cardinal directions, along with their bit representation
     * and deltas in x and y coordinates. Each direction also has a reference to its opposite direction.
     */
    private enum Direction {

        N(1, 0, -1),
        S(2, 0, 1),
        E(4, 1, 0),
        W(8, -1, 0);

        private final int bit;
        private final int dx;
        private final int dy;

        private Direction opposite;

        static {
            N.opposite = S;
            S.opposite = N;
            E.opposite = W;
            W.opposite = E;
        }

        Direction(int bit, int dx, int dy) {
            this.bit = bit;
            this.dx = dx;
            this.dy = dy;
        }
    }
}
