package org.crprojects;

/**
 * This file should NOT be reviewed. Its only purpose is to showcase the
 * functionality of the word-utils program. In what follows, a brief
 * specification of the program is provided:
 *
 * This program allows to perform operations on strings that contain words.
 * For more details on the operations supported, see the documentation of the
 * WordUtils class and its methods.
 */
public class Main {

    /**
     * Main method showcasing basic usage patterns of the WordUtils class.
     */
    public static void main(String[] args) {
        String text = "This is an out-of-this-world example of a text to be played with.";

        // Abbreviate a string
        System.out.println(WordUtils.abbreviate(text, 0, 10, null));
        System.out.println(WordUtils.abbreviate(text, 20, 30, null));
        System.out.println(WordUtils.abbreviate(text, 20, 25, null));
        System.out.println(WordUtils.abbreviate(text, 20, 25, "rld example of a text."));

        // Capitalize a string
        System.out.println(WordUtils.capitalize(text));

        // Capitalize a string, with custom delimiters
        System.out.println(WordUtils.capitalize(text, '-'));
        System.out.println(WordUtils.capitalize(text, '-', ' '));

        // Check if a string contains all words from a collection
        System.out.println(WordUtils.containsAllWords(text, "This", "is", "an", "example"));
        System.out.println(WordUtils.containsAllWords(text, "This", "is", "an", "example", "of", "a", "text", "to", "be", "played", "with"));
        System.out.println(WordUtils.containsAllWords(text, "This", "is", "an", "example", "of", "a", "text", "to", "be", "played", "with", "extra"));
        
        System.out.println(WordUtils.swapCase(text));

        // System.out.println(WordUtils.wrap(text, 10));

        System.out.println(WordUtils.containsAllWords("abc def (s)", "(s)", "abc"));
    }
}