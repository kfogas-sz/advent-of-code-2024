
def is_ok_distance(first: int, second: int) -> bool:
    if first > second:
        distance = first - second
    else:
        distance = second - first
    if distance > 3 or distance == 0:
        return False
    return True


def is_safe(numbers: list[int]) -> bool:
    increasing = None
    decreasing = None
    for count, value in enumerate(numbers[1:], start=1):
        if value > numbers[count-1]:
            if decreasing:
                return False
            increasing = True
        else:
            if increasing:
                return False
            decreasing = True
        if not is_ok_distance(numbers[count-1], value):
            return False
    return True


def is_safe_dampened(numbers: list[int]) -> bool:
    for count, _ in enumerate(numbers):
        if is_safe(numbers[:count] + numbers[count+1:]):
            return True
    return False


def main():
    with open(r"day2\input") as f:
        lines = f.read().splitlines()

    # First part:
    count = 0
    for line in lines:
        numbers = list(map(int, line.split()))
        if is_safe(numbers):
            count += 1
    print(count)

    # Second part:
    count = 0
    for line in lines:
        numbers = list(map(int, line.split()))
        if is_safe_dampened(numbers):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
