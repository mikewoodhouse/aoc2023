import pytest
from lib import data

from aoc07.aoc07 import Hand, max_count, part1, part2


@pytest.mark.parametrize(
    "hand,value",
    [
        ("A1234", 0),
        ("AA234", 1),
        ("23434", 2),
        ("56575", 3),
        ("K3K3K", 4),
        ("AA5AA", 5),
        ("99999", 6),
    ],
)
def test_hand_build_and_value(hand, value):
    h = Hand(hand)
    assert h.value == value, f"{hand}: expected {value}, got {h.value}"


def test_counts():
    assert max_count("23232", set("23232")) == 3


@pytest.mark.parametrize(
    "h1,h2,msg",
    [
        ("A2346", "A2345", "high card, last card higher"),
        ("AAAAA", "KKKKK", "A beats K"),
        ("KK677", "KTJJT", "second card K beats T"),
    ],
)
def test_ordering(h1, h2, msg):
    assert Hand(h1).strength > Hand(h2).strength, msg


def test_part1():
    assert part1(data(7, "sample")) == 6440
