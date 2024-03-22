package org.crprojects;

import static org.crprojects.NumberConversion.Format.ROMAN;
import static org.crprojects.NumberConversion.Format.BINARY;
import static org.crprojects.NumberConversion.Format.OCTAL;
import static org.crprojects.NumberConversion.Format.HEXADECIMAL;

/**
 * This file should NOT be reviewed. Its only purpose is to showcase the
 * functionality of the number-conversion program. In what follows, a brief
 * specification of the program is provided:
 *
 * This program allows to convert a decimal number to four possible formats:
 * binary, octal, hexadecimal and roman numeral. The conversion function
 * receives as input a decimal number and the desired format (an enum which
 * can only be BINARY, OCTAL, HEXADECIMAL or ROMAN) and returns the converted
 * number as a string. For roman, only numbers between 0 and 4000 (excluded)
 * are supported. For the other formats, only positive numbers are supported.
 */
public class Main {
    public static void main(String[] args) {
        System.out.println(NumberConversion.decimalToAnyFormat(1, ROMAN));
        System.out.println(NumberConversion.decimalToAnyFormat(2, BINARY));
        System.out.println(NumberConversion.decimalToAnyFormat(3, OCTAL));
        System.out.println(NumberConversion.decimalToAnyFormat(4, HEXADECIMAL));
    }
}