
import re


def main():
    result = 0
    with open(r"day3\input") as f:
        lines = f.read()

    # First part:
    mult_list = re.findall(r"mul\(\d+,\d+\)", lines)
    part_two_list = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", lines)

    for line in mult_list:
        numbers = list(map(int, re.findall(r"\d+", line)))
        result += (numbers[0] * numbers[1])

    print(result)

    # Second part:
    result = 0
    is_do = True
    for line in part_two_list:
        if line == "don't()":
            is_do = False
        if is_do and line != "do()":
            numbers = list(map(int, re.findall(r"\d+", line)))
            result += (numbers[0] * numbers[1])
        if line == "do()":
            is_do = True

    print(result)


if __name__ == "__main__":
    main()
