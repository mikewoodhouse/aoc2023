import importlib

from fire import Fire

from lib.util import data, single_line


def run(day: int, part: int = -1) -> None:
    filename = "input" if part > 0 else "sample"
    lines = single_line(day, filename) if day == 15 else data(day, filename)
    day_mod = importlib.import_module(f"aoc{day:02}")
    res = day_mod.part1(lines) if abs(part) == 1 else day_mod.part2(lines)
    print(f"ran part {abs(part)} on {filename}: {res}")


if __name__ == "__main__":
    Fire(
        {
            "run": run,
        }
    )
    print("OK")
