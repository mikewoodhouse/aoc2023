import pytest

from aoc10 import Map, part1, part2
from lib import data


@pytest.fixture
def sample():
    return sample_lines()


def sample_lines():
    return data(10, "sample")


@pytest.fixture
def square_loop():
    return square_loop_lines()


def square_loop_lines():
    return [
        ".....",
        ".S-7.",
        ".|.|.",
        ".L-J.",
        ".....",
    ]


def test_map(sample):
    m = Map(sample)
    assert m.size == (7, 7)


def test_start1(sample):
    m = Map(sample)
    assert m.start() == (3, 1)


def test_start2(square_loop):
    m = Map(square_loop)
    assert m.start() == (2, 2)


def test_tile_count(square_loop):
    m = Map(square_loop)
    assert m.dot_count == 41


@pytest.mark.parametrize(
    "lines,target",
    [
        (sample_lines(), 8),
        (square_loop_lines(), 4),
    ],
)
def test_farthest_point_square(lines, target):
    m = Map(lines)
    assert m.farthest_point() == target


def test_dejunk_map():
    junky = [
        "|........",
        "S-------7",
        "|F-----7|",
        "||.....||",
        "||.....||",
        "|L--7F-J|",
        "|...||..|",
        "L---JL--J",
        ".........",
    ]
    expected = [
        ".........",
        "S-------7",
        "|F-----7|",
        "||.....||",
        "||.....||",
        "|L--7F-J|",
        "|...||..|",
        "L---JL--J",
        ".........",
    ]
    m = Map(junky)
    exp = Map(expected)
    m.dejunk()
    # assert m.tiles == exp.tiles
    m.mark_outsiders()
    assert m.dot_count == 5


@pytest.mark.skip
def test_harder_dejunk():
    m = Map(
        [
            "FF7FSF7F7F7F7F7F---7",
            "L|LJ||||||||||||F--J",
            "FL-7LJLJ||||||LJL-77",
            "F--JF--7||LJLJ7F7FJ-",
            "L---JF-JLJ.||-FJLJJ7",
            "|F|F-JF---7F7-L7L|7|",
            "|FFJF7L7F-JF7|JL---7",
            "7-L-JL7||F7|L7F-7F7|",
            "L.L7LFJ|||||FJL7||LJ",
            "L7JLJL-JLJLJL--JLJ.L",
        ]
    )
    dots_before = m.dot_count
    m.dejunk()
    print(m)
    assert m.dot_count > dots_before
    m.mark_outsiders()
    print(m)
    assert m.dot_count == 10


@pytest.mark.skip
@pytest.mark.parametrize(
    "row,expected",
    [
        ("S----7", "XS----7X"),
        ("S-|.|-7", "XS-|X|-7X"),
        ("S||.||7", "XS||.||7X"),
        ("F--JF--7||LJLJ.F7FJ.", "XF--JF--7||LJLJ.F7FJXX"),
    ],
)
def test_easy_mark_outsiders(row, expected):
    m = Map([row])
    # m.dejunk()
    m.mark_outsiders_in_row(m.tiles[1])
    assert "".join(m.tiles[1]) == expected
