import pytest

from aoc12 import Node, part1, part2
from lib import data


@pytest.fixture()
def sample() -> list[str]:
    return data(12, "sample")


def test_construction():
    n = Node.from_line("???.### 1,1,3")
    assert n.damaged == [1, 1, 3]
    assert isinstance(n.to_hash, Node)
    assert isinstance(n.to_dot, Node)
    assert n.to_hash.value == "#??.###"
    assert n.to_dot.value == ".??.###"


@pytest.mark.parametrize(
    "line,expected",
    [
        ("???.### 1,1,3", 1),
        (".??..??...?##. 1,1,3", 4),
        ("?#?#?#?#?#?#?#? 1,3,1,6", 1),
        ("????.#...#... 4,1,1", 1),
        ("????.######..#####. 1,6,5", 4),
        ("?###???????? 3,2,1", 10),
    ],
)
def test_line_counts(line, expected):
    n = Node.from_line(line)
    assert n.arrangements == expected


def test_groups():
    n = Node(value="#.##.#.####", damaged=[])
    assert n.hash_counts == [1, 2, 1, 4]
