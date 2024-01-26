import pytest

from aoc14 import part1, part2
from aoc14.aoc14 import line_load, shifted, shifted_line, shifted_segment
from lib import data, transpose


@pytest.fixture()
def sample() -> list[str]:
    return data(14, "sample")


@pytest.mark.parametrize(
    "input,expected",
    [
        (".", 0),
        ("O", 1),
        ("O...", 4),
        ("OO..", 7),
        ("O...#O..", 11),
    ],
)
def test_line_load(input, expected):
    assert line_load(input) == expected


@pytest.mark.skip
def test_shifted():
    p = ["O..", ".O#", "O.O"]
    assert transpose(shifted(p)) == ["OO.", "O.#", "..O"]


@pytest.mark.parametrize(
    "input,expected",
    [
        (".", "."),
        ("O", "O"),
        (".O", "O."),
        ("...O", "O..."),
        (".O.O", "OO.."),
    ],
)
def test_shifted_seg(input, expected):
    assert shifted_segment(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        (".", "."),
        ("O", "O"),
        (".O", "O."),
        ("...O", "O..."),
        (".O.O", "OO.."),
        (".O.#.O.", "O..#O.."),
    ],
)
def test_shifted_line(input, expected):
    assert shifted_line(input) == expected


def test_part1(sample):
    assert part1(sample) == 136
