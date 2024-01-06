from __future__ import annotations

from dataclasses import dataclass, field

from icecream import ic


@dataclass(kw_only=True)
class Node:
    value: str
    damaged: list[int]
    to_hash: Node | None = None
    to_dot: Node | None = None

    def __post_init__(self) -> None:
        if "?" in self.value:
            self.to_hash = Node(value=self.value.replace("?", "#", 1), damaged=self.damaged)
            self.to_dot = Node(value=self.value.replace("?", ".", 1), damaged=self.damaged)

    @property
    def hash_counts(self) -> list[int]:
        counts = []
        counter = 0
        for c in self.value:
            if c == "#":
                counter += 1
            elif counter > 0:
                counts.append(counter)
                counter = 0
        if counter > 0:
            counts.append(counter)
        return counts

    def value_matches_damaged(self) -> bool:
        return self.hash_counts == self.damaged

    @property
    def arrangements(self) -> int:
        if not (self.to_hash and self.to_dot):  # leaf node
            return 1 if self.value_matches_damaged() else 0
        return self.to_dot.arrangements + self.to_hash.arrangements

    @staticmethod
    def from_line(s: str) -> Node:
        l, r = s.split(" ")[:2]
        damaged = [int(s) for s in r.split(",")]
        return Node(value=l, damaged=damaged)


def part1(lines: list[str]) -> int:
    return sum(Node.from_line(line).arrangements for line in lines)


def part2(lines: list[str]) -> int:
    return 0
