from functools import cache


def valid_pattern(pattern: str):
    if not pattern:
        return True
    for towel in towels:
        if pattern.startswith(towel):
            if valid_pattern(pattern[len(towel):]):
                return True
    return False


@cache
def calculate(pattern: str):
    if not pattern:
        return 1
    count = 0
    for towel in towels:
        if pattern.startswith(towel):
            count += calculate(pattern[len(towel):])
    return count


if __name__ == "__main__":

    count = 0

    with open(r"day19\input") as f:
        lines = f.read()

    lines = lines.split("\n\n")

    patterns = lines[1].split("\n")

    towels = lines[0].replace(" ", "").split(",")

    print(f"Part 1: {sum([1 for pattern in patterns if valid_pattern(pattern)])}")

    print(f"Part 2: {sum([calculate(pattern) for pattern in patterns])}")
