package org.crprojects;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

import static org.junit.jupiter.api.Assertions.*;

/**
 * This file should NOT be reviewed, nor should your code review comments
 * revolve around including more tests. However, feel free to run the
 * tests or to include more, e.g., to understand how the program works
 * or to verify certain program functionality.
 */
public class MazeTest {

    @Test
    public void northSouthWallTest() {
        Maze maze = Maze.random(2, 2);
        String result = maze.toString();
        assertNotNull(result);
        String[] lines = result.split("\n");
        String north = lines[0];
        String south = lines[lines.length - 1];
        String expected = "+---+---+";
        assertEquals(expected, north);
        assertEquals(expected, south);
    }

    @Test
    public void westEastWallTest() {
        Maze maze = Maze.random(2, 2);
        String result = maze.toString();
        assertNotNull(result);
        String[] lines = result.split("\n");
        List<Character> west = Arrays.stream(lines).map(line -> line.charAt(0)).collect(Collectors.toList());
        List<Character> east = Arrays.stream(lines).map(line -> line.charAt(line.length() - 1)).collect(Collectors.toList());
        List<Character> expected = Arrays.asList('+', ' ', '+', '|', '+');
        List<Character> reversed = new ArrayList<>(expected);
        Collections.reverse(reversed);
        assertEquals(expected, west);
        assertEquals(reversed, east);
    }

    @Test
    public void dimensionsTest() {
        Maze maze = Maze.random(6, 10);
        String result = maze.toString();
        assertEquals(10, (result.split("\n").length - 1) / 2);
        assertEquals(6, result.split("\n")[0].split("---").length - 1);
    }
}