from unittest import TestCase
from number_conversion import Format
from number_conversion import decimal_to_roman, decimal_to_any_format

test_data_roman = [
    (1, 'I'),
    (2, 'II'),
    (3, 'III'),
    (4, 'IV'),
    (5, 'V'),
    (6, 'VI'),
    (7, 'VII'),
]

test_data_binary = [
    (1, '1'),
    (2, '10'),
    (3, '11'),
    (4, '100'),
    (5, '101'),
    (6, '110'),
    (7, '111'),
]

test_data_octal = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
]

test_data_hexadecimal = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
]


class TestNumberConversion(TestCase):
    """
    This file should NOT be reviewed, nor should your code review comments
    revolve around including more tests. However, feel free to run the
    tests or to include more, e.g., to understand how the program works
    or to verify certain program functionality.
    """

    def test_to_roman(self):
        for number, expected in test_data_roman:
            with self.subTest(number=number, expected=expected):
                self.assertEqual(expected, decimal_to_roman(number))

    def test_to_binary(self):
        for number, expected in test_data_binary:
            with self.subTest(number=number, expected=expected):
                self.assertEqual(expected, decimal_to_any_format(number, Format.BINARY))

    def test_to_octal(self):
        for number, expected in test_data_octal:
            with self.subTest(number=number, expected=expected):
                self.assertEqual(expected, decimal_to_any_format(number, Format.OCTAL))

    def test_to_hexadecimal(self):
        for number, expected in test_data_hexadecimal:
            with self.subTest(number=number, expected=expected):
                self.assertEqual(expected, decimal_to_any_format(number, Format.HEXADECIMAL))
