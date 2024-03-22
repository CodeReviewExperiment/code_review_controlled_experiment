"""
This file should NOT be reviewed. Its only purpose is to showcase the
functionality of the number-conversion program. In what follows, a brief
specification of the program is provided:

This program allows to convert a decimal number to four possible formats:
binary, octal, hexadecimal and roman numeral. The conversion function
receives as input a decimal number and the desired format (an enum which
can only be BINARY, OCTAL, HEXADECIMAL or ROMAN) and returns the converted
number as a string. For roman, only numbers between 0 and 4000 (excluded)
are supported. For the other formats, only positive numbers are supported.
"""

from number_conversion import decimal_to_any_format, Format


if __name__ == "__main__":
    print(decimal_to_any_format(1, Format.ROMAN))
    print(decimal_to_any_format(2, Format.BINARY))
    print(decimal_to_any_format(3, Format.OCTAL))
    print(decimal_to_any_format(4, Format.HEXADECIMAL))
