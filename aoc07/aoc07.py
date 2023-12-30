from __future__ import annotations

from dataclasses import dataclass


def max_count(h: str, dist: set[str]) -> int:
    return max(h.count(c) for c in dist)


@dataclass
class Hand:
    cards: str
    bid: int = 0

    @property
    def value(self) -> int:
        distinct = set(self.cards)
        count_distinct = len(distinct)
        if count_distinct == 5:
            return 0
        if count_distinct == 4:
            return 1
        if count_distinct == 3:
            return 3 if max_count(self.cards, distinct) == 3 else 2
        if count_distinct == 2:
            return 5 if max_count(self.cards, distinct) == 4 else 4
        return 6

    @property
    def strength(self) -> int:
        def card_strength(c: str, idx: int) -> int:
            exp = 10 ** ((4 - idx) * 2)
            return "23456789TJQKA".index(c) * exp

        return self.value * 100_000_000_000 + sum(card_strength(c, idx) for idx, c in enumerate(self.cards))

    @staticmethod
    def from_string(s: str) -> Hand:
        cards, bid = s.split(" ")
        return Hand(cards, int(bid))

    def __repr__(self) -> str:
        return f"{self.cards} {self.bid} {self.value} {self.strength}"


def part1(lines: list[str]) -> int:
    hands = [Hand.from_string(line) for line in lines]
    hands.sort(reverse=False, key=lambda c: c.strength)
    return sum(rank * h.bid for rank, h in enumerate(hands, 1))


def part2(lines: list[str]) -> int:
    return 0
