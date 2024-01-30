import pytest

from aoc16 import part1, part2
from aoc16.aoc16 import (
    BackslashMirror,
    Empty,
    Grid,
    HorizontalSplitter,
    SlashMirror,
    VerticalSplitter,
)
from lib import data


@pytest.fixture()
def sample() -> list[str]:
    return data(16, "sample")


def test_grid_build(sample):
    g = Grid.from_lines(sample)
    assert isinstance(g, Grid)
    assert len(g.cells) == 10
    assert isinstance(g.cells[0][0], Empty)
    assert isinstance(g.cells[0][1], VerticalSplitter)
    assert not any(c.energized for row in g.cells.values() for c in row.values())
    assert len(g.beams) == 1
    assert g.energized_count == 0
    assert isinstance(g.cells[4][1], BackslashMirror)


def test_part1(sample):
    g = Grid.from_lines(sample)
    g.run()
    g.print_energized_map()
    assert g.energized_count == 46
