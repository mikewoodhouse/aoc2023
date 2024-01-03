import pytest

from aoc10 import Map, part1, part2
from lib import data


@pytest.fixture
def sample():
    return sample_lines()


def sample_lines():
    return data(10, "sample")


@pytest.fixture
def square_loop():
    return square_loop_lines()


def square_loop_lines():
    return [
        ".....",
        ".S-7.",
        ".|.|.",
        ".L-J.",
        ".....",
    ]


def test_map(sample):
    m = Map(sample)
    assert m.size == (5, 5)


def test_start1(sample):
    m = Map(sample)
    assert m.start() == (2, 0)


def test_start2(square_loop):
    m = Map(square_loop)
    assert m.start() == (1, 1)


@pytest.mark.skip
@pytest.mark.parametrize(
    "lines,target",
    [
        (sample_lines(), 8),
        (square_loop_lines(), 4),
    ],
)
def test_farthest_point_square(lines, target):
    m = Map(lines)
    assert m.farthest_point() == target
