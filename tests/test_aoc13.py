import pytest

from aoc13.aoc13 import (  # first_match,; is_valid_mirror,
    has_mirror,
    mirror_at,
    mirror_score,
    pairs,
    part1,
    part2,
    patterns,
)
from lib import data, transpose


@pytest.fixture()
def sample() -> list[str]:
    return data(13, "sample")


@pytest.fixture()
def sample2() -> list[str]:
    return data(13, "sample2")


@pytest.fixture()
def sample3() -> list[str]:
    return data(13, "sample3")


@pytest.fixture()
def sample4() -> list[str]:
    return data(13, "sample4")


def test_mirror_at(sample):
    pattern_iter = iter(patterns(sample))

    p = next(pattern_iter)
    assert mirror_at(transpose(p)) == 5

    p = next(pattern_iter)
    assert mirror_at(p) == 4


def test_mirror_at2(sample2):
    pattern_iter = iter(patterns(sample2))

    p = next(pattern_iter)
    assert mirror_at(transpose(p)) == 16


@pytest.mark.skip
def test_mirror_at3(sample3):
    pattern_iter = iter(patterns(sample3))

    p = next(pattern_iter)
    assert mirror_at(transpose(p)) == 11


@pytest.mark.skip
def test_part1(sample):
    assert part1(sample) == 405


@pytest.mark.skip
def test_part1_2(sample4):
    assert part1(sample4) == 709


def test_pair_finding():
    p = [
        ".#.##.#.#",
        ".##..##..",
        ".#.##.#..",
        "#......##",
        "#......##",
        ".#.##.#..",
        ".##..##.#",
    ]
    prs = pairs(p)
    assert len(prs) == 2


# @pytest.mark.skip
def test_false_positive():
    p = [
        ".#.##.#.#",
        ".##..##..",
        ".#.##.#..",
        "#......##",
        "#......##",
        ".#.##.#..",
        ".##..##.#",
    ]
    # assert not has_mirror(p, 1, 6)
    # assert has_mirror(p, 2, 5)
    assert mirror_score(p) == 4
