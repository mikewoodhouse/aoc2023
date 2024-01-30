from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field

from icecream import ic


@dataclass
class Dir:
    dx: int = 0
    dy: int = 0
    desc: str = ""

    def __hash__(self) -> int:
        return hash((self.dx, self.dy))

    def __repr__(self) -> str:
        return f"{self.desc}:{self.dx},{self.dy}"


DN = Dir(0, -1, "N")
DS = Dir(0, 1, "S")
DE = Dir(1, 0, "E")
DW = Dir(-1, 0, "W")


@dataclass
class Cell:
    celltype: str = ""
    energized: bool = False
    has_been: set[Dir] = field(default_factory=set)

    def result(self, beam: Beam) -> list[Beam]:
        return []

    @staticmethod
    def from_char(c: str) -> Cell:
        if c == "|":
            return VerticalSplitter(c)
        elif c == "-":
            return HorizontalSplitter(c)
        elif c == "/":
            return SlashMirror(c)
        elif c == "\\":
            return BackslashMirror(c)
        return Empty(c)

    def __repr__(self) -> str:
        return f"[{self.celltype} {'#' if self.energized else '.'}]"


class SlashMirror(Cell):
    def result(self, beam: Beam) -> list[Beam]:
        if beam.dir in self.has_been:
            return []
        self.has_been.add(beam.dir)
        beam.dir = {DN: DE, DE: DN, DS: DW, DW: DS}[beam.dir]
        return [beam]


class BackslashMirror(Cell):
    def result(self, beam: Beam) -> list[Beam]:
        if beam.dir in self.has_been:
            return []
        self.has_been.add(beam.dir)
        beam.dir = {DN: DW, DE: DS, DS: DE, DW: DN}[beam.dir]
        return [beam]


class VerticalSplitter(Cell):
    def result(self, beam: Beam) -> list[Beam]:
        if beam.dir in self.has_been:
            return []
        self.has_been.add(beam.dir)
        if beam.dir in [DN, DS]:
            return [beam]
        return [
            Beam(beam.x, beam.y, DN),
            Beam(beam.x, beam.y, DS),
        ]


class HorizontalSplitter(Cell):
    def result(self, beam: Beam) -> list[Beam]:
        if beam.dir in self.has_been:
            return []
        self.has_been.add(beam.dir)
        if beam.dir in [DE, DW]:
            return [beam]
        return [
            Beam(beam.x, beam.y, DE),
            Beam(beam.x, beam.y, DW),
        ]


class Empty(Cell):
    def result(self, beam: Beam) -> list[Beam]:
        if beam.dir in self.has_been:
            return []
        self.has_been.add(beam.dir)

        return [beam]


def defaultdict_of_dicts() -> dict[int, dict[int, Cell]]:
    return defaultdict(dict)


@dataclass
class Beam:
    x: int
    y: int
    dir: Dir

    def move_one(self) -> None:
        self.x += self.dir.dx
        self.y += self.dir.dy

    def move_from(self, cel: Cell) -> list[Beam]:
        if isinstance(cel, Empty):
            self.move_one()
            return [self]
        new_beams = cel.result(self)
        for b in new_beams:
            b.move_one()
        return new_beams

    def in_grid(self, g: Grid) -> bool:
        return self.x <= g.last_col and self.y <= g.last_row and self.x >= 0 and self.y >= 0

    def __repr__(self) -> str:
        return f"({self.x},{self.y}) {self.dir}"


@dataclass
class Grid:
    cells: dict[int, dict[int, Cell]] = field(default_factory=defaultdict_of_dicts)
    beams: list[Beam] = field(default_factory=list)
    last_row: int = 0
    last_col: int = 0

    def __post_init__(self):
        self.beams = [Beam(0, 0, DE)]

    def run(self) -> None:
        while len(self.beams) > 0:
            new_beams: list[Beam] = []
            for i, b in enumerate(self.beams):
                cel = self.cells[b.x][b.y]
                cel.energized = True
                # ic(i, b, cel)
                result = b.move_from(cel)
                # ic(result)
                new_beams.extend(b for b in result if b.in_grid(self))
            self.beams = new_beams

    @property
    def energized_count(self) -> int:
        return sum(c.energized for row in self.cells.values() for c in row.values())

    @staticmethod
    def from_lines(lines: list[str]) -> Grid:
        grid = Grid()
        grid.last_row = len(lines) - 1
        grid.last_col = len(lines[0]) - 1
        for row, line in enumerate(lines):
            for col, c in enumerate(line):
                grid.cells[col][row] = Cell.from_char(c)
                # ic(grid.cells[row][col], row, col)
        return grid

    def print_energized_map(self) -> None:
        for y in range(self.last_col + 1):
            s = "".join("#" if self.cells[x][y].energized else "." for x in range(self.last_row + 1))
            print(s)


def part1(lines: list[str]) -> int:
    g = Grid.from_lines(lines)
    g.run()
    return g.energized_count


def part2(lines: list[str]) -> int:
    return 0
