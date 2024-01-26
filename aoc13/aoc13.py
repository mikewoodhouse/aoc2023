from __future__ import annotations

from dataclasses import dataclass
from functools import reduce

from icecream import ic

from lib.util import transpose

NO_MATCH = (0, 0)


# def is_valid_mirror(p: list[str], fm: tuple[int, int]) -> bool:
#     if (fm[1] - fm[0]) % 2 == 0:
#         return False
#     mirror_size = (fm[1] - fm[0] + 1) // 2
#     left = p[fm[0] : fm[0] + mirror_size]
#     right = p[fm[1] : fm[0] + mirror_size - 1 : -1]
#     return all(a == b for a, b in zip(left, right))


# def first_match(a: list[str]) -> tuple[int, int]:
#     for il, sl in enumerate(a[:-2]):
#         # for ir in range(len(a) - 1, il, -1):
#         if sl == a[-1]:
#             return (il + 1, len(a))
#     return NO_MATCH


def pairs(p: list[str]) -> list:
    sz = len(p)
    indexed = list(enumerate(p))
    indexed.sort(key=lambda t: (t[1], t[0]))
    return [(a[0] + 1, b[0] + 1) for a, b in zip(indexed[:sz], indexed[1:]) if a[1] == b[1]]


def has_mirror(p: list[str], s: int, e: int) -> bool:
    gap = (e - s + 1) // 2
    l = p[s : s + gap]
    r = p[e : e - gap : -1]
    return all(a == b for a, b in zip(l, r))


def mirror_at(p: list[str]) -> int:
    prs = sorted(pairs(p), key=lambda pr: pr[0])
    if not prs:
        return 0
    while prs:
        lo = min(p[0] for p in prs)
        hi = max(p[1] for p in prs)
        gap = hi - lo + 1
        in_pairs = {*reduce(lambda a, b: a + b, prs)}
        if gap == len(in_pairs):
            return lo + len(prs) - 1
        prs = prs[1:]
    return 0


def patterns(a: list[str]):
    pattern: list[str] = []
    for s in a:
        if s:
            pattern.append(s)
        else:
            yield pattern
            pattern.clear()
    yield pattern


def mirror_score(p: list[str]) -> int:
    loc = mirror_at(transpose(p))
    if loc:
        print(loc)
        return loc
    loc = mirror_at(p)
    print(loc * 100)
    return loc * 100
    # return loc * 100 if (loc := mirror_at(p)) else mirror_at(transpose(p))


def part1(lines: list[str]) -> int:
    return sum(mirror_score(p) for p in patterns(lines))


def part2(lines: list[str]) -> int:
    return 0
