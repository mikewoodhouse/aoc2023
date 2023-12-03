import pytest

from aoc_01.aoc_01 import DigitizedString


@pytest.mark.parametrize(
    "input,expected",
    [
        ("one", 1),
        ("twone", 2),
        ("xtwonez", 2),
        ("two1nine", 2),
        ("eightwothree", 8),
        ("abcone2threexyz", 1),
        ("xtwone3four", 2),
        ("4nineeightseven2", 4),
        ("zoneight234", 1),
        ("7pqrstsixteen", 7),
        ("fivepqxlpninevh2xxsnsgg63pbvdnqptmg", 5),
        ("eight8zlctbmsixhrvbpjb84nnmlcqkzrsix", 8),
        ("685", 6),
        ("seventhree", 7),
        ("twotwone", 2),
        ("sevenine", 7),
    ],
)
def test_first_digit(input, expected):
    assert DigitizedString(input).first_digit == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ("one", 1),
        ("twone", 1),
        ("xtwonez", 1),
        ("two1nine", 9),
        ("eightwothree", 3),
        ("abcone2threexyz", 3),
        ("xtwone3four", 4),
        ("4nineeightseven2", 2),
        ("zoneight234", 4),
        ("7pqrstsixteen", 6),
        ("fivepqxlpninevh2xxsnsgg63pbvdnqptmg", 3),
        ("eight8zlctbmsixhrvbpjb84nnmlcqkzrsix", 6),
        ("685", 5),
        ("seventhree", 3),
        ("twotwone", 1),
        ("sevenine", 9),
    ],
)
def test_last_digit(input, expected):
    assert DigitizedString(input).last_digit == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ("one", 11),
        ("twone", 21),
        ("xtwonez", 21),
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        ("fivepqxlpninevh2xxsnsgg63pbvdnqptmg", 53),
        ("eight8zlctbmsixhrvbpjb84nnmlcqkzrsix", 86),
        ("685", 65),
        ("seventhree", 73),
        ("twotwone", 21),
        ("sevenine", 79),
    ],
)
def test_calibration_value(input, expected):
    assert DigitizedString(input).calibration_value() == expected
