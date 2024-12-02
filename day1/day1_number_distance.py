first_list = []
second_list = []


def calculate_first_part(first_list: list[int], second_list: list[int]) -> None:
    first_part = 0
    for first, second in zip(first_list, second_list):
        if first > second:
            first_part += int(first) - int(second)
        else:
            first_part += int(second) - int(first)
    print(first_part)


def calculate_second_part(first_list: list[int], second_list: list[int]) -> None:
    second_part = 0
    for item in first_list:
        count = second_list.count(item)
        second_part += count*item

    print(second_part)


def main():
    with open(r"day1\input") as f:
        lines = f.read().splitlines()

    for line in lines:
        first, second = line.split()
        first_list.append(int(first))
        second_list.append(int(second))

    first_list.sort()
    second_list.sort()

    calculate_first_part(first_list, second_list)

    calculate_second_part(first_list, second_list)


if __name__ == "__main__":
    main()
