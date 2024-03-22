from string import ascii_uppercase


class Format:
    ROMAN = "ROMAN"
    BINARY = "BINARY"
    OCTAL = "OCTAL"
    HEXADECIMAL = "HEXADECIMAL"


ALPHABET_VALUES = {str(ord(c) - 55): c for c in ascii_uppercase}
ROMAN = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def decimal_to_any_format(num, format_type) -> str:
    if format_type not in (Format.ROMAN, Format.BINARY, Format.OCTAL, Format.HEXADECIMAL):
        return ""
    return {
        Format.ROMAN: lambda: decimal_to_roman(num),
        Format.BINARY: lambda: decimal_to_any_base(num, 2),
        Format.OCTAL: lambda: decimal_to_any_base(num, 8),
        Format.HEXADECIMAL: lambda: decimal_to_any_base(num, 8),
    }[format_type]()


def decimal_to_roman(number: int) -> str:
    """
    Given a integer, convert it to an roman numeral. The number
    must be between 0 and 4000 (both included). It will return an error message if the input is invalid.
    """
    if not 0 <= number <= 4000:
        return "Invalid input. Input must be greater than 0 and less than 4000"
    result = []
    for arabic, roman in ROMAN:
        (factor, number) = divmod(number, arabic)
        result.append(roman * factor)
    return "".join(result)


def decimal_to_any_base(num: int, base: int) -> str:
    """
    Convert a positive integer to another base as str.
    """
    if base in (0, 1) or base > 36:
        return "Invalid base. Base should be between 2 and 36."

    if num < 0:
        return "Input number must be positive."

    new_value = ""
    div = 0
    while div != 1:
        div, mod = divmod(num, base)
        if base >= 11 and 9 < mod < 36:
            actual_value = ALPHABET_VALUES[str(mod)]
        else:
            actual_value = str(mod)
        new_value += actual_value
        div = num // base
        num = div
        if div == 0:
            return str(new_value[::-1])
        elif div == 1:
            new_value += str(div)
            return str(new_value[::-1])

    return new_value[::-1]
