from pathlib import Path


def data(day: int, filename: str) -> list[str]:
    return [
        s.strip()
        for s in ((Path(__file__).parent.parent / f"aoc{day:02}" / f"{filename}.txt").read_text().split("\n"))
    ]