"""Helper functions"""
import re


def parse_input(fh: str) -> list:
    """Load and parse source file

    :param fh: name of parsed file without extension
    """
    with open(f"{fh}.txt") as f:
        lines = [x.strip("\n") for x in f.readlines()]
    return lines


def is_it_int(char: str) -> bool:
    """Try if char is int.

    :param char: single character for check
    """
    try:
        int(char)
        return True
    except ValueError:
        return False


def word_to_digit_converter(sequence: str) -> str:
    """Convert word to digit.

    :param sequence: sequence for conversion
    """
    digits = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"}

    for k, v in digits.items():
        sequence = sequence.replace(k, v)
    return sequence
