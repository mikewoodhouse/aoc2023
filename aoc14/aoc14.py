from __future__ import annotations

from dataclasses import dataclass

from icecream import ic

from lib import transpose


def shifted_segment(s: str) -> str:
    return "".join(sorted(s, reverse=True))


def shifted_line(s: str) -> str:
    return "#".join(shifted_segment(x) for x in s.split("#"))


def shifted(p_in: list[str]) -> list[str]:
    p = transpose(p_in)
    return [shifted_line(line) for line in p]


def line_load(s: str) -> int:
    return sum(i for i, c in enumerate(s[::-1], 1) if c == "O")


def part1(lines: list[str]) -> int:
    return sum(line_load(line) for line in shifted(lines))


def part2(lines: list[str]) -> int:
    return 0
