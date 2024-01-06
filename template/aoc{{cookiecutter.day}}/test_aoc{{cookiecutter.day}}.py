from aoc{{cookiecutter.day}} import (
    part1,
    part2,
)
from lib import data
import pytest

@pytest.fixture()
def sample() -> list[str]:
    return data({{cookiecutter.day}}, "sample")
