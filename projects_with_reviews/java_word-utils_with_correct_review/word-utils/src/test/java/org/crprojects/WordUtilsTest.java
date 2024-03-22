package org.crprojects;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/**
 * This file should NOT be reviewed, nor should your code review comments
 * revolve around including more tests. However, feel free to run the
 * tests or to include more, e.g., to understand how the program works
 * or to verify certain program functionality.
 */
public class WordUtilsTest {

    @Test
    public void abbreviateTest() {
        assertEquals("Now", WordUtils.abbreviate("Now is the time for all good men", 0, 40, null));
        assertEquals("Now is the", WordUtils.abbreviate("Now is the time for all good men", 10, 40, null));
        assertEquals("Now is the time for all", WordUtils.abbreviate("Now is the time for all good men", 20, 40, null));
        assertEquals("Now", WordUtils.abbreviate("Now is the time for all good men", 0, 40, ""));
        assertEquals("Now is the", WordUtils.abbreviate("Now is the time for all good men", 10, 40, ""));
        assertEquals("Now is the time for all", WordUtils.abbreviate("Now is the time for all good men", 20, 40, ""));
        assertEquals("Now ...", WordUtils.abbreviate("Now is the time for all good men", 0, 40, " ..."));
        assertEquals("Now is the ...", WordUtils.abbreviate("Now is the time for all good men", 10, 40, " ..."));
        assertEquals("Now is the time for all ...", WordUtils.abbreviate("Now is the time for all good men", 20, 40, " ..."));
        assertThrows(IllegalArgumentException.class, () -> WordUtils.abbreviate("Now is the time for all good men", 9, -10, null));
        assertThrows(IllegalArgumentException.class, () -> WordUtils.abbreviate("Now is the time for all good men", 10, 5, null));
    }

    @Test
    public void capitalizeTest() {
        assertNull(WordUtils.capitalize(null));
        assertEquals("", WordUtils.capitalize(""));
        assertEquals("I Am FINE", WordUtils.capitalize("i am FINE"));
    }

    @Test
    public void capitalizeWithDelimitersTest() {
        assertNull(WordUtils.capitalize(null, '*'));
        assertEquals("", WordUtils.capitalize("", '*'));
        assertEquals("*", WordUtils.capitalize("*", new char[0]));
        assertEquals("I Am Fine", WordUtils.capitalize("i am fine", null));
        assertEquals("I aM.Fine", WordUtils.capitalize("i aM.fine", '.'));
        assertEquals("I am fine", WordUtils.capitalize("i am fine", new char[]{}));
    }

    @Test
    public void capitalizeFullyTest() {
        assertNull(WordUtils.capitalizeFully(null));
        assertEquals("", WordUtils.capitalizeFully(""));
        assertEquals("I Am Fine", WordUtils.capitalizeFully("i am FINE"));
    }

    @Test
    public void capitalizeFullyWithDelimitersTest() {
        assertNull(WordUtils.capitalizeFully(null, '*'));
        assertEquals("", WordUtils.capitalizeFully("", '*'));
        assertEquals("*", WordUtils.capitalizeFully("*", null));
        assertEquals("*", WordUtils.capitalizeFully("*", new char[0]));
        assertEquals("I am.Fine", WordUtils.capitalizeFully("i aM.fine", '.'));
    }

    @Test
    public void containsAllWordsTest() {
        assertFalse(WordUtils.containsAllWords(null, "*"));
        assertFalse(WordUtils.containsAllWords("", "*"));
        assertFalse(WordUtils.containsAllWords("*", null));
        assertFalse(WordUtils.containsAllWords("*"));
        assertFalse(WordUtils.containsAllWords("abcd", "ab", "cd"));
        assertTrue(WordUtils.containsAllWords("abc def", "def", "abc"));
    }

    @Test
    public void initialsTest() {
        assertNull(WordUtils.initials(null));
        assertEquals("", WordUtils.initials(""));
        assertEquals("BJL", WordUtils.initials("Ben John Lee"));
        assertEquals("BJ", WordUtils.initials("Ben J.Lee"));
    }

    @Test
    public void initialsWithDelimitersTest() {
        assertNull(WordUtils.initials(null, '*'));
        assertEquals("", WordUtils.initials("", '*'));
        assertEquals("BJL", WordUtils.initials("Ben John Lee", null));
        assertEquals("BJ", WordUtils.initials("Ben J.Lee", null));
        assertEquals("BJL", WordUtils.initials("Ben J.Lee", ' ', '.'));
        assertEquals("", WordUtils.initials("*", new char[0]));
    }

    @Test
    public void swapCaseTest() {
        assertNull(WordUtils.swapCase(null));
        assertEquals("", WordUtils.swapCase(""));
        assertEquals("tHE DOG HAS A bone", WordUtils.swapCase("The dog has a BONE"));
    }

    @Test
    public void uncapitalizeTest() {
        assertNull(WordUtils.uncapitalize(null));
        assertEquals("", WordUtils.uncapitalize(""));
        assertEquals("i am fINE", WordUtils.uncapitalize("I Am FINE"));
    }

    @Test
    public void uncapitalizeWithDelimitersTest() {
        assertNull(WordUtils.uncapitalize(null, '*'));
        assertEquals("", WordUtils.uncapitalize("", '*'));
        assertEquals("*", WordUtils.uncapitalize("*", null));
        assertEquals("*", WordUtils.uncapitalize("*", new char[0]));
        assertEquals("i AM.fINE", WordUtils.uncapitalize("I AM.FINE", '.'));
        assertEquals("i am fine", WordUtils.uncapitalize("I am fine", new char[]{}));
    }
}