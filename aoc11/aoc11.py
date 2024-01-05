from __future__ import annotations

from dataclasses import dataclass

from icecream import ic


def transpose(a: list[str]) -> list[str]:
    return ["".join(x) for x in zip(*a)]


def dupe_empty_rows(a: list[str]) -> list[str]:
    ary = []
    for row in a:
        ary.append(row)
        if "#" not in row:
            ary.append(row)
    return ary


class Map:
    def __init__(self, lines: list[str]) -> None:
        space = transpose(dupe_empty_rows(transpose(dupe_empty_rows(lines))))
        self.space = [list(row) for row in space]
        self.galaxies = []
        for row_idx, row in enumerate(self.space):
            self.galaxies.extend((row_idx, col_idx) for col_idx, ch in enumerate(row) if ch == "#")

    def shortest_length_total(self) -> int:
        tot = 0
        for idx, g1 in enumerate(self.galaxies):
            for g2 in self.galaxies[idx:]:
                tot += abs(g2[0] - g1[0]) + abs(g2[1] - g1[1])
        return tot


def part1(lines: list[str]) -> int:
    m = Map(lines)
    return m.shortest_length_total()


def part2(lines: list[str]) -> int:
    return 0
