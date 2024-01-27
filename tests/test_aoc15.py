from collections import defaultdict

import pytest
from icecream import ic

from aoc15 import part1, part2
from aoc15.aoc15 import Step, box_power, hash, hash_total
from lib import single_line


@pytest.fixture()
def sample() -> list[str]:
    return single_line(15, "sample")


def test_single_line():
    assert hash("HASH") == 52


def test_sample_hash(sample):
    assert hash_total(sample) == 1320


def test_step_create():
    assert Step.from_string("gblm=9") == Step("gblm", "=", 9)
    assert Step.from_string("rbv-") == Step("rbv", "-", 0)


def test_box_power():
    boxes = {
        0: [Step("", "", 1), Step("", "", 2)],
        3: [Step("", "", 7), Step("", "", 5), Step("", "", 6)],
    }
    assert sum(box_power(i, b) for i, b in boxes.items()) == 145


def test_apply_step(sample):
    steps = [Step.from_string(s) for s in sample]
    boxes = defaultdict(list[Step])
    for step in steps:
        step.apply_to(boxes)
    assert sum(len(box) > 0 for box in boxes.values())
    assert boxes[0] == [steps[0], steps[3]]
    assert boxes[3] == [steps[10], steps[7], steps[9]]


def test_part2(sample):
    assert part2(sample) == 145
