"""
This file should NOT be reviewed. Its only purpose is to showcase the
functionality of the word-utils program. In what follows, a brief
specification of the program is provided:

This program allows to perform operations on strings that contain words.
For more details on the operations supported, see the documentation of the
WordUtils class and its methods.
"""


from WordUtils import WordUtils


def main():
    text = "This is an out-of-this-world example of a text to be played with."

    # Abbreviate a string
    print(WordUtils.abbreviate(text, 0, 10, None))
    print(WordUtils.abbreviate(text, 20, 30, None))
    print(WordUtils.abbreviate(text, 20, 25, None))
    print(WordUtils.abbreviate(text, 20, 25, "rld example of a text."))

    # Capitalize a string
    print(WordUtils.capitalize(text))

    # Capitalize a string, with custom delimiters
    print(WordUtils.capitalize(text, '-'))
    print(WordUtils.capitalize(text, '-', ' '))

    # Check if a string contains all words from a collection
    print(WordUtils.contains_all_words(text, "This", "is", "an", "example"))
    print(WordUtils.contains_all_words(text, "This", "is", "an", "example", "of", "a", "text", "to", "be", "played", "with"))
    print(WordUtils.contains_all_words(text, "This", "is", "an", "example", "of", "a", "text", "to", "be", "played", "with", "extra"))

    print(WordUtils.uncapitalize("I AM.FINE", '.'))
    print(WordUtils.contains_all_words("abc def", "def", "ABC"))

if __name__ == "__main__":
    main()
