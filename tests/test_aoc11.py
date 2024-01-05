import pytest

from aoc11 import Map, part1, part2
from aoc11.aoc11 import transpose
from lib import data


@pytest.fixture()
def sample() -> list[str]:
    return data(11, "sample")


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


def test_sum_of_shortest_length(sample):
    m = Map(sample)
    assert m.shortest_length_total() == 374
