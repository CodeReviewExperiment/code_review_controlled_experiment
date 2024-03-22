package org.crprojects;

public class NumberConversion {

    private static final int[] ARABIAN_NUMBERS = new int[] {
            1000,
            900,
            500,
            400,
            100,
            90,
            50,
            40,
            10,
            9,
            5,
            4,
            1,
    };

    private static final String[] ROMAN_NUMBERS = new String[] {
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
    };

    public enum Format {
        ROMAN,
        BINARY,
        OCTAL,
        HEXADECIMAL
    }

    /**
     * This method produces a String value of any given input decimal to Roman,
     * binary, octal or hexadecimal format.
     *
     * @param num integer of which we need the value in converted format
     * @return converted value into desired format as a string, or an error message
     * if the input is invalid
     */
    public static String decimalToAnyFormat(int num, Format format) {
        return switch (format) {
            case ROMAN -> decimalToRoman(num);
            case BINARY -> decimalToAnyBase(num, 2);
            case OCTAL -> decimalToAnyBase(num, 8);
            case HEXADECIMAL -> decimalToAnyBase(num, 8);
        };
    }

    /**
     * This method produces a String value of any given input decimal to Roman
     * format.
     *
     * @param input decimal of which we need the value in Roman format,
     *              must be greater than 0 and less than 4000
     * @return converted value into Roman format as a string, or an error message
     * if the input is invalid
     */
    private static String decimalToRoman(int input) {
        if (input < 0 || input > 4000) {
            return "Invalid input. Input must be greater than 0 and less than 4000";
        }

        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < ARABIAN_NUMBERS.length; i++) {
            int arabian = ARABIAN_NUMBERS[i];
            String roman = ROMAN_NUMBERS[i];
            int times = input / arabian;
            builder.append(roman.repeat(times));
            input -= times * arabian;
        }

        return builder.toString();
    }

    /**
     * This method produces a String value of any given input decimal to Roman
     * format.
     *
     * @param input decimal of which we need the value in base in String format
     * @param base base to which we need to convert the decimal to
     * @return string format of the converted value in the given base
     */
    private static String decimalToAnyBase(int input, int base) {
        StringBuilder builder = new StringBuilder();

        if (input < 0) {
            return "Input number must greater than 0.";
        }

        if (input == 0) {
            return "0";
        }

        while (input > 0){
            int modulo = input % base;
            boolean singleDigit = modulo <= 9;
            char character = (char) (singleDigit ? modulo + '0' : modulo - 10 + 'A');
            builder.append(character);
            input /= base;
        }

        return builder.reverse().toString();
    }
}
