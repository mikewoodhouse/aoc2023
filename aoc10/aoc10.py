from __future__ import annotations

from dataclasses import dataclass

from icecream import ic

POSSIBLE_EXITS = {
    "S": "NSEW",
    ".": "",
    "-": "EW",
    "|": "NS",
    "L": "NE",
    "F": "ES",
    "7": "SW",
    "J": "WN",
}

MOVES = {
    "N": ((-1, 0), "|F7"),
    "E": ((0, 1), "-J7"),
    "S": ((1, 0), "|LJ"),
    "W": ((0, -1), "-FL"),
}


def plus(pt: tuple[int, int], delta: tuple[int, int]) -> tuple[int, int]:
    return (pt[0] + delta[0], pt[1] + delta[1])


@dataclass
class Traveller:
    prev_pos: tuple[int, int]
    curr_pos: tuple[int, int]
    step_count: int = 1

    def move_to(self, pt: tuple[int, int]):
        self.prev_pos = self.curr_pos
        self.curr_pos = pt
        self.step_count += 1


class Map:
    def __init__(self, lines: list[str]) -> None:
        self.tiles = lines
        self.size = (len(self.tiles), len(self.tiles[0]))

    def start(self) -> tuple[int, int]:
        row_idx, row = next((idx, row) for idx, row in enumerate(self.tiles) if "S" in row)
        col_idx = row.index("S")
        return (row_idx, col_idx)

    def moves_from(self, pt: tuple[int, int], prev: tuple[int, int] = (-1, -1)) -> list[tuple[int, int]]:
        res = []
        curr_char = self.tile_at(pt)
        exits = POSSIBLE_EXITS[curr_char]
        for exit in exits:
            # ic(exit, MOVES[exit])
            move, possibles = MOVES[exit]
            # ic("adding", move, "to", pt)
            target = plus(pt, move)
            target_tile = self.tile_at(target)
            # outside bounds
            if target[0] < 0 or target[0] >= self.size[0] or target[1] < 0 or target[1] >= self.size[1]:
                continue
            can_add = target_tile in possibles and target != prev
            # ic(move, pt, curr_char, exits, target, target_tile, can_add)
            if can_add:
                res.append(target)
        return res

    def tile_at(self, pt: tuple[int, int]) -> str:
        return self.tiles[pt[0]][pt[1]]

    def farthest_point(self) -> int:
        started_at = self.start()
        ic(started_at)
        paths = list(self.moves_from(started_at))
        travellers = [Traveller(curr_pos=pos, prev_pos=started_at) for pos in paths]
        # ic(paths)
        while travellers[0].curr_pos != travellers[1].curr_pos:
            for t in travellers:
                new_pos = self.moves_from(t.curr_pos, t.prev_pos)[0]
                t.move_to(new_pos)
            # break
        ic(travellers)
        return travellers[0].step_count


def part1(lines: list[str]) -> int:
    m = Map(lines)
    return m.farthest_point()


def part2(lines: list[str]) -> int:
    return 0
