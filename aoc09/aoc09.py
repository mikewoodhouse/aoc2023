from __future__ import annotations

from dataclasses import dataclass

from icecream import ic


def parse_line(s: str) -> list[int]:
    return [int(v) for v in s.split()]


def diff(vals: list[int]) -> list[int]:
    return [r - l for l, r in zip(vals, vals[1:])]


def diff_to_zeroes(vals: list[int]) -> list[list[int]]:
    all_zeroes = False
    res = [vals]
    while not all_zeroes:
        diffs = diff(res[-1])
        res.append(diffs)
        if not any(diffs):
            all_zeroes = True
    return res


def extrapolate(series: list[list[int]]) -> int:
    for idx in range(len(series) - 1, 0, -1):
        upper = series[idx - 1][-1]
        lower = series[idx][-1]
        series[idx - 1].append(upper + lower)
    return series[0][-1]


def extrapolate_left(series: list[list[int]]) -> int:
    for idx in range(len(series) - 1, 0, -1):
        upper = series[idx - 1][0]
        lower = series[idx][0]
        series[idx - 1].insert(0, upper - lower)
    return series[0][0]


def part1(lines: list[str]) -> int:
    tot = 0
    for line in lines:
        try:
            vals = parse_line(line)
            diff_series = diff_to_zeroes(vals)
            tot += extrapolate(diff_series)
        except Exception as e:
            ic(line)
    return tot


def part2(lines: list[str]) -> int:
    tot = 0
    for line in lines:
        vals = parse_line(line)
        diff_series = diff_to_zeroes(vals)
        tot += extrapolate_left(diff_series)
    return tot
