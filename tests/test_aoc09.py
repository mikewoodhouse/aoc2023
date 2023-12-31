from aoc09.aoc09 import (
    diff,
    diff_to_zeroes,
    extrapolate,
    extrapolate_left,
    parse_line,
    part1,
    part2,
)
from lib import data


def test_parse_line():
    s = "0 3 6 9 12 15"
    diffs = parse_line(s)
    assert len(diffs) == 6
    assert all(isinstance(v, int) for v in diffs)
    assert diffs[2] == 6


def test_diff():
    diffs = diff([1, 2, 4, 7])
    assert diffs == [1, 2, 3]


def test_to_zeroes():
    res = diff_to_zeroes([1, 2, 4, 7])
    assert len(res) == 4


def test_extrapolate():
    series = diff_to_zeroes([1, 2, 4, 7])
    res = extrapolate(series)
    assert res == 11


def test_part1():
    lines = data(9, "sample")
    assert part1(lines) == 114


def test_part2():
    lines = data(9, "sample")
    assert part2(lines) == 2
