from __future__ import annotations

from dataclasses import dataclass

from icecream import ic


def hash(s) -> int:
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256

    return val


def hash_total(p: list[str]) -> int:
    # return sum(hash(s) for s in p)
    tot = 0
    for s in p:
        score = hash(s)
        ic(s, score)
        tot += score
    return tot


def part1(lines: list[str]) -> int:
    return hash_total(lines)


def part2(lines: list[str]) -> int:
    return 0
