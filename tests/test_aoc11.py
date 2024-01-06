import pytest

from aoc11 import Map, SmartMap, part1, part2
from aoc11.aoc11 import transpose
from lib import data


@pytest.fixture()
def sample() -> list[str]:
    return data(11, "sample")


@pytest.fixture()
def simple() -> list[str]:
    return [
        "......",
        ".#....",
        "......",
        "......",
        "......",
        "....#.",
        "......",
    ]


@pytest.fixture()
def simple2() -> list[str]:
    return [
        "......",
        ".#....",
        "......",
        "...#..",
        "......",
        "....#.",
        "......",
    ]


def test_sample_loaded(sample):
    assert len(sample)


def test_dupe_rows(sample):
    assert len(sample) == 10
    m = Map(sample)
    assert len(m.space) == 12
    assert len(m.space[0]) == 13


def test_transpose_list_of_strs():
    ary = ["123", "456", "789"]
    a2 = transpose(ary)
    assert a2 == ["147", "258", "369"]


def test_galaxy_identification(sample):
    m = Map(sample)
    assert len(m.galaxies) == 9


@pytest.mark.skip
@pytest.mark.parametrize(
    "empty_size,expected",
    [
        (1, 374),
        (10, 1030),
        (100, 8410),
    ],
)
def test_sum_of_shortest_length(sample, empty_size, expected):
    m = SmartMap(sample)
    assert m.shortest_length_total(empty_size) == expected


@pytest.mark.parametrize(
    "empty_size,expected",
    [
        (1, 7),
        (10, 52),
        (1_000_000, 5_000_002),
    ],
)
def test_sum_of_shortest_length2(simple, empty_size, expected):
    m = SmartMap(simple)
    assert m.shortest_length_total(empty_size) == expected


@pytest.mark.parametrize(
    "empty_size,expected",
    [
        (1, 14),
        (1_000_000, 6_000_000 + 8),
    ],
)
def test_sum_of_shortest_length3(simple2, empty_size, expected):
    m = SmartMap(simple2)
    assert m.shortest_length_total(empty_size) == expected


def test_smart_sample(sample):
    sm = SmartMap(sample)
    assert len(sm.empty_rows) == 2
    assert len(sm.empty_cols) == 3
