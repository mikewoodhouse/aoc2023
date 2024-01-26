import pytest

from aoc15 import part1, part2
from aoc15.aoc15 import hash, hash_total
from lib import single_line


@pytest.fixture()
def sample() -> list[str]:
    return single_line(15, "sample")


def test_single_line():
    assert hash("HASH") == 52


def test_sample_hash(sample):
    assert hash_total(sample) == 1320
