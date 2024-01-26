from __future__ import annotations

from dataclasses import dataclass
from functools import cache

from icecream import ic

from lib import transpose


@cache
def shifted_segment(s: str) -> str:
    return "".join(sorted(s, reverse=True))


@cache
def shifted_line(s: str) -> str:
    return "#".join(shifted_segment(x) for x in s.split("#"))


def shifted(p: list[str]) -> list[str]:
    return [shifted_line(line) for line in p]


@cache
def line_load(s: str) -> int:
    return sum(i for i, c in enumerate(s[::-1], 1) if c == "O")


def part1(lines: list[str]) -> int:
    return sum(line_load(line) for line in shifted(transpose(lines)))


def part2(lines: list[str]) -> int:
    return 0
