from unittest import TestCase
from WordUtils import WordUtils


class TestWordUtils(TestCase):
    """
    This file should NOT be reviewed, nor should your code review comments
    revolve around including more tests. However, feel free to run the
    tests or to include more, e.g., to understand how the program works
    or to verify certain program functionality.
    """

    def test_abbreviate(self):
        self.assertEqual("Now", WordUtils.abbreviate("Now is the time for all good men", 0, 40, None))
        self.assertEqual("Now is the", WordUtils.abbreviate("Now is the time for all good men", 10, 40, None))
        self.assertEqual("Now is the time for all", WordUtils.abbreviate("Now is the time for all good men", 20, 40, None))
        self.assertEqual("Now", WordUtils.abbreviate("Now is the time for all good men", 0, 40, ""))
        self.assertEqual("Now is the", WordUtils.abbreviate("Now is the time for all good men", 10, 40, ""))
        self.assertEqual("Now is the time for all", WordUtils.abbreviate("Now is the time for all good men", 20, 40, ""))
        self.assertEqual("Now ...", WordUtils.abbreviate("Now is the time for all good men", 0, 40, " ..."))
        self.assertEqual("Now is the ...", WordUtils.abbreviate("Now is the time for all good men", 10, 40, " ..."))
        self.assertEqual("Now is the time for all ...", WordUtils.abbreviate("Now is the time for all good men", 20, 40, " ..."))
        self.assertRaises(ValueError, lambda: WordUtils.abbreviate("Now is the time for all good men", 9, -10, None))
        self.assertRaises(ValueError, lambda: WordUtils.abbreviate("Now is the time for all good men", 10, 5, None))
    
    def test_capitalize(self):
        self.assertIsNone(WordUtils.capitalize(None))
        self.assertEqual("", WordUtils.capitalize(""))
        self.assertEqual("I Am FINE", WordUtils.capitalize("i am FINE"))
        self.assertIsNone(WordUtils.capitalize(None, "*"))
        self.assertEqual("", WordUtils.capitalize("", "*"))
        self.assertEqual("*", WordUtils.capitalize("*", ""))
        self.assertEqual("I Am Fine", WordUtils.capitalize("i am fine", None))
        self.assertEqual("I aM.Fine", WordUtils.capitalize("i aM.fine", "."))
        self.assertEqual("I am fine", WordUtils.capitalize("i am fine", ""))

    def test_capitalize_fully(self):
        self.assertIsNone(WordUtils.capitalize_fully(None))
        self.assertEqual("", WordUtils.capitalize_fully(""))
        self.assertEqual("I Am Fine", WordUtils.capitalize_fully("i am FINE"))
        self.assertIsNone(WordUtils.capitalize_fully(None, "*"))
        self.assertEqual("", WordUtils.capitalize_fully("", "*"))
        self.assertEqual("*", WordUtils.capitalize_fully("*", None))
        self.assertEqual("*", WordUtils.capitalize_fully("*", ""))
        self.assertEqual("I am.Fine", WordUtils.capitalize_fully("i aM.fine", "."))

    def test_contains_all_words(self):
        self.assertFalse(WordUtils.contains_all_words(None, "*"))
        self.assertFalse(WordUtils.contains_all_words("", "*"))
        self.assertFalse(WordUtils.contains_all_words("*", None))
        self.assertFalse(WordUtils.contains_all_words("*"))
        self.assertFalse(WordUtils.contains_all_words("*", ""))
        self.assertFalse(WordUtils.contains_all_words("abcd", "ab", "cd"))
        self.assertTrue(WordUtils.contains_all_words("abc def", "def", "abc"))

    def test_initials(self):
        self.assertIsNone(WordUtils.initials(None))
        self.assertEqual("", WordUtils.initials(""))
        self.assertEqual("BJL", WordUtils.initials("Ben John Lee"))
        self.assertEqual("BJ", WordUtils.initials("Ben J.Lee"))
        self.assertIsNone(WordUtils.initials(None, "*"))
        self.assertEqual("", WordUtils.initials("", "*"))
        self.assertEqual("BJL", WordUtils.initials("Ben John Lee", None,))
        self.assertEqual("BJ", WordUtils.initials("Ben J.Lee", None))
        self.assertEqual("BJL", WordUtils.initials("Ben J.Lee", " ", "."))
        self.assertEqual("*", WordUtils.initials("*", ""))

    def test_swap_case(self):
        self.assertIsNone(WordUtils.swap_case(None))
        self.assertEqual("", WordUtils.swap_case(""))
        self.assertEqual("tHE DOG HAS A bone", WordUtils.swap_case("The dog has a BONE"))

    def test_uncapitalize(self):
        self.assertIsNone(WordUtils.uncapitalize(None))
        self.assertEqual("", WordUtils.uncapitalize(""))
        self.assertEqual("i am fINE", WordUtils.uncapitalize("I Am FINE"))
        self.assertIsNone(WordUtils.uncapitalize(None, "*"))
        self.assertEqual("", WordUtils.uncapitalize("", "*"))
        self.assertEqual("*", WordUtils.uncapitalize("*", None))
        self.assertEqual("*", WordUtils.uncapitalize("*", ""))
        self.assertEqual("i AM.fINE", WordUtils.uncapitalize("I AM.FINE", "."))
        self.assertEqual("i am fine", WordUtils.uncapitalize("I am fine", ""))
