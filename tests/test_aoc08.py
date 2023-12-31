import re

import pytest

from aoc08.aoc08 import RE, decode, part1, part2
from lib import data


def test_re():
    match = re.search(RE, "AAA = (BBB, CCC)")
    # sourcery skip: no-conditionals-in-tests
    if isinstance(match, re.Match):
        assert match["node"] == "AAA"


def test_decode():
    s = "AAA = (BBB, CCC)"
    n, l, r = decode(s)
    assert n == "AAA"
    assert l == "BBB"
    assert r == "CCC"
