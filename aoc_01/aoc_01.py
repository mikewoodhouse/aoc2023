from pathlib import Path


class DigitizedString(str):
    @property
    def first_digit(self) -> int:
        for pos, char in enumerate(self):
            if char.isdigit():
                return int(char)
            for digit_less_1, num in enumerate(
                ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
            ):
                if self[pos : pos + len(num)] == num:  # noqa: E203
                    return digit_less_1 + 1

    @property
    def last_digit(self) -> int:
        s = self[::-1]
        for pos, char in enumerate(s):
            if char.isdigit():
                return int(char)
            for digit_less_1, num in enumerate(
                ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
            ):
                if s[pos : pos + len(num)] == num[::-1]:  # noqa: E203
                    return digit_less_1 + 1

    def calibration_value(self) -> int:
        return self.first_digit * 10 + self.last_digit


def calibration_value_sum(filename: str) -> int:
    tot = 0
    filepath = Path(__file__).parent / f"{filename}.txt"
    with filepath.open() as f:
        for line in f.readlines():
            s = DigitizedString(line.strip())
            tot += s.calibration_value()
            print(line, tot)
            # break
    return tot


if __name__ == "__main__":
    print(calibration_value_sum("input_01"))
