from __future__ import annotations

from collections import defaultdict
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


@dataclass()
class Step:
    label: str
    op: str
    length: int

    def apply_to(self, boxes: dict[int, list[Step]]) -> None:
        boxno = hash(self.label)
        if self.op == "=":
            replaced = False
            for lens in boxes[boxno]:
                if lens.label == self.label:
                    lens.length = self.length
                    replaced = True
            if not replaced:
                boxes[boxno].append(self)
        else:
            target = next(
                (idx for idx, lens in enumerate(boxes[boxno]) if lens.label == self.label),
                -1,
            )
            if target == -1:
                return
            del boxes[boxno][target]

    @staticmethod
    def from_string(s: str) -> Step:
        if "=" not in s:
            return Step(s[:-1], "-", 0)
        t = s.split("=")
        return Step(t[0], "=", int(t[1]))

    def __repr__(self) -> str:
        return f"{self.label}{self.op}{'' if self.op == '-' else str(self.length)}"


def box_power(boxno: int, lenses: list[Step]) -> int:
    return sum((1 + boxno) * slotno * step.length for slotno, step in enumerate(lenses, 1))


def part1(lines: list[str]) -> int:
    return hash_total(lines)


def part2(lines: list[str]) -> int:
    boxes: dict[int, list] = defaultdict(list)
    steps = [Step.from_string(s) for s in lines]
    for step in steps:
        step.apply_to((boxes))
    return sum(box_power(boxno, lenses) for boxno, lenses in boxes.items())
