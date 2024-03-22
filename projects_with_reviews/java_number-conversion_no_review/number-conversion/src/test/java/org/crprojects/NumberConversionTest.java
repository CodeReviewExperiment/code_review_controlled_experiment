package org.crprojects;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 * This file should NOT be reviewed, nor should your code review comments
 * revolve around including more tests. However, feel free to run the
 * tests or to include more, e.g., to understand how the program works
 * or to verify certain program functionality.
 */
public class NumberConversionTest {

    @ParameterizedTest
    @CsvSource({
            "1, ROMAN, I",
            "2, ROMAN, II",
            "3, ROMAN, III",
            "4, ROMAN, IV",
            "5, ROMAN, V",
            "6, ROMAN, VI",
            "7, ROMAN, VII",
            "1, BINARY, 1",
            "2, BINARY, 10",
            "3, BINARY, 11",
            "4, BINARY, 100",
            "5, BINARY, 101",
            "6, BINARY, 110",
            "7, BINARY, 111",
            "1, OCTAL, 1",
            "2, OCTAL, 2",
            "3, OCTAL, 3",
            "4, OCTAL, 4",
            "5, OCTAL, 5",
            "6, OCTAL, 6",
            "7, OCTAL, 7",
            "1, HEXADECIMAL, 1",
            "2, HEXADECIMAL, 2",
            "3, HEXADECIMAL, 3",
            "4, HEXADECIMAL, 4",
            "5, HEXADECIMAL, 5",
            "6, HEXADECIMAL, 6",
            "7, HEXADECIMAL, 7"
    })
    public void decimalToAnyFormatTest(int number, NumberConversion.Format format, String expected) {
        assertEquals(expected, NumberConversion.decimalToAnyFormat(number, format));
    }

}