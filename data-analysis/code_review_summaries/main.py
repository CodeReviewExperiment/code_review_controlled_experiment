#! /usr/bin/env python3

from argparse import ArgumentParser
from nltk import download, sent_tokenize, word_tokenize
from pandas import read_csv
from pandas import DataFrame
from pathlib import Path
from string import punctuation


def combine_text_columns(row):
    title = row['title']
    comment = row['comment']
    base = f"{title}. {comment}" if title else comment
    trimmed = base.strip()
    last_character = trimmed[-1] if trimmed else ''
    if last_character not in punctuation:
        trimmed = f"{trimmed}."
    return trimmed


def parse_range(cell):
    lower, upper = cell.split("-")
    lower_row, _ = [int(position) for position in lower.split(":")]
    upper_row, _ = [int(position) for position in upper.split(":")]
    return upper_row - lower_row + 1


def parse_lines(cell):
    return sum([parse_range(range) for range in cell.split("|")])


if __name__ == "__main__":
    download('punkt', quiet=True)
    parser = ArgumentParser()
    parser.add_argument(
        "--path",
        type=str,
        help="Path to the CSV file",
        required=True
    )
    args = parser.parse_args()
    if not args.path.endswith(".csv"):
        raise ValueError("File must be a CSV")
    parent = Path(args.path).parent.absolute()
    df = read_csv(args.path, encoding='utf-8', doublequote=True, keep_default_na=False)
    df['text'] = df.apply(combine_text_columns, axis=1).str.replace('\\n', ' ')
    df['lines'] = df['lines'].apply(parse_lines)
    df = df[['text', 'lines']]
    comments = df.shape[0]
    commented_lines = df['lines'].sum()
    text = df['text'].str.cat(sep='\n')
    sentences = sent_tokenize(text)
    words = [word for word in word_tokenize(text) if word not in punctuation]
    xf = DataFrame({
        "number-of-comments": comments,
        "number-of-sentences": len(sentences),
        "number-of-words": len(words),
        "number-of-commented-lines": commented_lines
    }, index=[0])
    path = parent.joinpath("code-review-summary.csv")
    xf.to_csv(path, index=False)
