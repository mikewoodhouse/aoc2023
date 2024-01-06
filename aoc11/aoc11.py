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
                row_offset = g2[0] - g1[0]
                col_offset = g2[1] - g1[1]
                tot += abs(row_offset) + abs(col_offset)
        return tot

    def __repr__(self) -> str:
        return f"Map: {len(self.space)} rows by {len(self.space[0])} columns"


def empty_locations(a: list[str]) -> list[int]:
    return [idx for idx, line in enumerate(a) if "#" not in line]


class SmartMap:
    def __init__(self, lines: list[str]) -> None:
        self.space = lines
        self.empty_rows = empty_locations(self.space)
        self.empty_cols = empty_locations(transpose(self.space))
        self.galaxies = []
        for row_idx, row in enumerate(self.space):
            self.galaxies.extend((row_idx, col_idx) for col_idx, ch in enumerate(row) if ch == "#")

    def shortest_length_total(self, empty_size: int = 1) -> int:
        tot = 0
        for idx, g1 in enumerate(self.galaxies):
            for g2 in self.galaxies[idx:]:
                row_offset = g2[0] - g1[0]
                col_offset = g2[1] - g1[1]
                er = sum(min(g1[0], g2[0]) < x < max(g1[0], g2[0]) for x in self.empty_rows)
                ec = sum(min(g1[1], g2[1]) < x < max(g1[1], g2[1]) for x in self.empty_cols)
                tot += abs(row_offset) + abs(col_offset) - er - ec
                tot += empty_size * er
                tot += empty_size * ec
        return tot


def part1(lines: list[str]) -> int:
    m = Map(lines)
    print(m)
    return m.shortest_length_total()


def part2(lines: list[str]) -> int:
    m = SmartMap(lines)
    return m.shortest_length_total(1_000_000)
