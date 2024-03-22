from re import compile as compile_regex
from re import escape as escape_chars
from typing import Optional


class WordUtils:
    """
    Operations on Strings that contain words.

    This class tries to handle `None` input gracefully. An exception will not be thrown for a
    `None` input. Each method documents its behavior in more detail.

    Since: 1.1
    """

    @staticmethod
    def abbreviate(string: Optional[str], lower: int, upper: int, append_to_end: Optional[str]):
        """
        Abbreviates the words nicely.

        This method searches for the first space after the lower limit and abbreviates
        the string there. It will also append any string passed as a parameter
        to the end of the string. The upper limit can be specified to forcibly
        abbreviate a string.

        Parameters:
            string (str | None): The string to be abbreviated. If None is passed, None is returned.
                                 If the empty string is passed, the empty string is returned.
            lower (int): The lower limit; a negative values are treated as zero.
            upper (int): The upper limit; specify -1 to disable the upper limit.
                         The upper limit cannot be lower than the lower limit.
            append_to_end (str | None): String to be appended to the end of the abbreviated string.
                                        This is appended ONLY if the string was indeed abbreviated.
                                        The append does not count towards the lower or upper limits.

        Returns:
            str: The abbreviated string.

        Examples:
            >>> WordUtils.abbreviate("Now is the time for all good men", 0, 40, None)
            "Now"
            >>> WordUtils.abbreviate("Now is the time for all good men", 10, 40, None)
            "Now is the"
            >>> WordUtils.abbreviate("Now is the time for all good men", 20, 40, None)
            "Now is the time for all"
            >>> WordUtils.abbreviate("Now is the time for all good men", 0, 40, "")
            "Now"
            >>> WordUtils.abbreviate("Now is the time for all good men", 10, 40, "")
            "Now is the"
            >>> WordUtils.abbreviate("Now is the time for all good men", 20, 40, "")
            "Now is the time for all"
            >>> WordUtils.abbreviate("Now is the time for all good men", 0, 40, " ...")
            "Now ..."
            >>> WordUtils.abbreviate("Now is the time for all good men", 10, 40, " ...")
            "Now is the ..."
            >>> WordUtils.abbreviate("Now is the time for all good men", 20, 40, " ...")
            "Now is the time for all ..."
            >>> WordUtils.abbreviate("Now is the time for all good men", 9, -10, None)
            ValueError
            >>> WordUtils.abbreviate("Now is the time for all good men", 10, 5, None)
            ValueError
        """
        if upper < 0:
            raise ValueError("upper value cannot be less than 0")
        if upper < lower:
            raise ValueError("upper value is less than lower value")

        if string is None or string == "":
            return string

        if lower > len(string):
            lower = len(string)

        if upper > len(string):
            upper = len(string)

        result = []
        index = string.find(" ", lower)
        if index == -1:
            result.append(string[0:upper])
            # only if abbreviation has occurred do we append the append_to_end value
            if upper != len(string):
                result.append(append_to_end if append_to_end is not None else "")
        else:
            result.append(string[0:min(index, upper)])
            result.append(append_to_end if append_to_end is not None else "")

        return "".join(result)

    @staticmethod
    def capitalize(string: Optional[str], *delimiters: Optional[str]):
        """
        Capitalizes all the delimiter-separated words in a string.

        Only the first character of each word is changed. To convert the
        rest of each word to lowercase at the same time,
        use `capitalize_fully`.

        The delimiters represent a set of characters understood to separate words.
        The first string character and the first non-delimiter character after a
        delimiter will be capitalized. Empty string as delimiter means that only
        the first string character will be capitalized.

        A `None` input string returns `None`.
        Capitalization uses the Unicode title case, normally equivalent to
        upper case.

        Examples:
            >>> WordUtils.capitalize(None)
            None
            >>> WordUtils.capitalize("")
            ""
            >>> WordUtils.capitalize("i am FINE")
            "I Am FINE"
            >>> WordUtils.capitalize(None, "*")
            None
            >>> WordUtils.capitalize("", "*")
            ""
            >>> WordUtils.capitalize("*", "")
            "*"
            >>> WordUtils.capitalize("i am fine", None)
            "I Am Fine"
            >>> WordUtils.capitalize("i aM.fine", ".")
            "I aM.Fine"
            >>> WordUtils.capitalize("i am fine", "")
            "I am fine"

        Parameters:
            string (str | None): The string to capitalize, may be None.
            delimiters (list[str | None]): Set of characters to determine capitalization.
                                           The value of None equates to a single whitespace.

        Returns:
            str: Capitalized string, None if the input string is None.

        See Also:
            - `uncapitalize`
            - `capitalize_fully`
        """
        if not string:
            return string

        delimiters = {delimiter if delimiter is not None else " " for delimiter in delimiters} if delimiters else " "

        flag = True

        def callback(character: str):
            nonlocal flag
            if character in delimiters:
                flag = True
                return character
            else:
                if flag:
                    flag = False
                    return character.title()
                else:
                    return character

        characters = [callback(character) for character in string]
        return "".join(characters)

    @staticmethod
    def capitalize_fully(string: Optional[str], *delimiters: Optional[str]):
        """
        Converts all the delimiter-separated words in a string into capitalized words,
        where each word is made up of a titlecase character followed by a series of
        lowercase characters.

        The delimiters represent a set of characters understood to separate words.
        The first string character and the first non-delimiter character after a
        delimiter will be capitalized.

        A `None` input string returns `None`.
        Capitalization uses the Unicode title case, normally equivalent to
        upper case.

        Examples:
            >>> WordUtils.capitalize_fully(None)
            None
            >>> WordUtils.capitalize_fully("")
            ""
            >>> WordUtils.capitalize_fully("i am FINE")
            "I Am Fine"
            >>> WordUtils.capitalize_fully(None, "*")
            None
            >>> WordUtils.capitalize_fully("", "*")
            ""
            >>> WordUtils.capitalize_fully("*", None)
            "*"
            >>> WordUtils.capitalize_fully("*", "")
            "*"
            >>> WordUtils.capitalize_fully("i aM.fine", ".")
            "I am.Fine"

        Parameters:
            string (str | None): The string to capitalize.
            delimiters (list[str | None]): Set of characters to determine capitalization.
                                           None means whitespace.

        Returns:
            str: Capitalized string, None if the input string is None.
        """
        if not string:
            return string
        return WordUtils.capitalize(string.lower(), *delimiters)

    @staticmethod
    def contains_all_words(string: Optional[str], *words: Optional[str]):
        """
        Checks if the string contains all words in the given array.

        A `None` string will return `False`. A `None`, zero-length search array,
        or if one element of the array is `None`, will return `False`.

        Examples:
            >>> WordUtils.contains_all_words(None, "*")
            False
            >>> WordUtils.contains_all_words("", "*")
            False
            >>> WordUtils.contains_all_words("*", None)
            False
            >>> WordUtils.contains_all_words("*")
            False
            >>> WordUtils.contains_all_words("*", "")
            False
            >>> WordUtils.contains_all_words("abcd", "ab", "cd")
            False
            >>> WordUtils.contains_all_words("abc def", "def", "abc")
            True

        Parameters:
            string (str | None): The string to check, may be None.
            *words (list[str | None]): The array of words to search for, may be None.

        Returns:
            bool: True if all search words are found, False otherwise.
        """
        if not string or not words or not all(word for word in words):
            return False

        for word in words:
            if not word.strip():
                return False
            pattern = compile_regex(f".*\\b{escape_chars(word)}\\b.*")
            if not pattern.match(string):
                return False

        return True

    @staticmethod
    def initials(string: Optional[str], *delimiters: Optional[str]):
        """
        Extracts the initial characters from each word in the string.

        All first characters after the defined delimiters are returned as a new string.
        Their case is not changed.

        If the delimiters array is None, then Whitespace is used.
        Whitespace is defined by `str.isspace()`.
        A `None` input string returns `None`.

        Examples:
            >>> WordUtils.initials(None)
            None
            >>> WordUtils.initials("")
            ""
            >>> WordUtils.initials("Ben John Lee")
            "BJL"
            >>> WordUtils.initials("Ben J.Lee")
            "BJ"
            >>> WordUtils.initials(None, "*")
            None
            >>> WordUtils.initials("", "*")
            ""
            >>> WordUtils.initials("Ben John Lee", None)
            "BJL"
            >>> WordUtils.initials("Ben J.Lee", None)
            "BJ"
            >>> WordUtils.initials("Ben J.Lee", " ", ".")
            "BJL"
            >>> WordUtils.initials("*", "")
            "*"

        Parameters:
            string (str | None): The string to get initials from, may be None.
            delimiters (list[str | None]): Set of characters to determine words.
                                           The value of None equates to a single whitespace.

        Returns:
            str: String of initial characters, None if the input string is None.
        """
        if not string:
            return string

        delimiters = {delimiter if delimiter else " " for delimiter in delimiters} if delimiters else " "

        flag = True

        def callback(character: str):
            nonlocal flag
            if character in delimiters or character.isspace():
                flag = True
            elif flag:
                flag = False
                return character
            return ""

        characters = [callback(character) for character in string]
        return "".join(characters)

    @staticmethod
    def swap_case(string: Optional[str]):
        """
        Swaps the case of a string using a word-based algorithm.

        - Upper case character converts to Lower case
        - Title case character converts to Lower case
        - Lower case character after whitespace or at the start converts to Title case
        - Other Lower case character converts to Upper case

        Whitespace is defined by `str.isspace()`.
        A None input string returns None.

        Examples:
            >>> WordUtils.swap_case(None)
            None
            >>> WordUtils.swap_case("")
            ""
            >>> WordUtils.swap_case("The dog has a BONE")
            "tHE DOG HAS A bone"

        Parameters:
            string (str | None): The string to swap case, may be None.

        Returns:
            str: The changed string, None if the input string is None.
        """
        if not string:
            return string

        ws = True

        def callback(character: str):
            nonlocal ws
            if character.isupper() or character.istitle():
                ws = False
                return character.lower()
            elif character.islower():
                if ws:
                    ws = False
                    return character.title()
                else:
                    return character.upper()
            else:
                ws = character.isspace()
                return character

        characters = [callback(character) for character in string]
        return "".join(characters)

    @staticmethod
    def uncapitalize(string: Optional[str], *delimiters: Optional[str]):
        """
        Uncapitalizes all the whitespace separated words in a string.
        Only the first character of each word is changed.

        The delimiters represent a set of characters understood to separate words.
        The first string character and the first non-delimiter character after a
        delimiter will be uncapitalized.  Empty string as delimiter means that only
        the first string character will be uncapitalized.

        Whitespace is defined by `str.isspace()`.
        A `None` input string returns `None`.

        Examples:
            >>> WordUtils.uncapitalize(None)
            None
            >>> WordUtils.uncapitalize("")
            ""
            >>> WordUtils.uncapitalize("I Am FINE")
            "i am fINE"
            >>> WordUtils.uncapitalize(None, "*")
            None
            >>> WordUtils.uncapitalize("", "*")
            ""
            >>> WordUtils.uncapitalize("*", None)
            "*"
            >>> WordUtils.uncapitalize("*", "")
            "*"
            >>> WordUtils.uncapitalize("I AM.FINE", ".")
            "i AM.fINE"
            >>> WordUtils.uncapitalize("I am fine", "")
            "i am fine"

        Parameters:
            string (str | None): The string to uncapitalize, may be None.
            delimiters (list[str | None]): Set of characters to determine uncapitalization.
                                           The value of None equates to a single whitespace.

        Returns:
            str: Uncapitalized string, None if the input string is None.

        See Also:
            - `capitalize`
        """
        if not string:
            return string

        delimiters = {delimiter if delimiter is not None else " " for delimiter in delimiters} if delimiters else " "

        flag = True

        def callback(character: str):
            nonlocal flag
            if character in delimiters:
                flag = True
                return character
            else:
                if flag:
                    flag = False
                    return character.lower()
                else:
                    return character

        characters = [callback(character) for character in string]
        return "".join(characters)
