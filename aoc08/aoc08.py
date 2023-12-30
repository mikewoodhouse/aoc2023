from __future__ import annotations

import re
from dataclasses import dataclass

import numpy as np
from icecream import ic

RE = re.compile(r"(?P<node>\w{3}).=.+((?P<left>\w{3}),.+(?P<right>\w{3}))")


def decode(s: str) -> tuple[str, str, str]:
    m = re.search(RE, s)
    if isinstance(m, re.Match):
        return m["node"], m["left"], m["right"]
    else:
        return "", "", ""


def build_maps(lines: list[str]) -> dict:
    maps = {}
    for line in lines:
        n, l, r = decode(line)
        maps[n] = (l, r)

    return maps


def remap(inst: str, this: str, maps: dict) -> str:
    thismap = maps[this]
    return thismap[0] if inst == "L" else thismap[1]


def part1(lines: list[str]) -> int:
    insts = lines[0]
    maps = build_maps(lines[2:])
    this = "AAA"
    steps = 0
    while this != "ZZZ":
        for c in insts * 1000:
            thismap = maps[this]
            this = thismap[0] if c == "L" else thismap[1]
            # ic(this)
            steps += 1
            if this == "ZZZ":
                break
    return steps


def steps_to_z(this: str, insts: str, maps: dict) -> tuple[int, str]:
    idx = 0
    steps = 0
    while not this.endswith("Z"):
        inst = insts[idx]
        this = remap(inst, this, maps)
        steps += 1
        idx += 1
        if idx >= len(insts):
            idx = 0
    return steps, this


def part2(lines: list[str]) -> int:
    insts = lines[0]
    maps = build_maps(lines[2:])
    these = {k for k in maps.keys() if k.endswith("A")}
    to_z = {k: steps_to_z(k, insts, maps)[0] for k in these}
    ic(to_z)
    steps = 0
    idx = 0
    to_z_steps = list(to_z.values())
    return np.lcm.reduce(to_z_steps)
