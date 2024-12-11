def blinking(numbers, number_of_blinks):
    new_list = []
    for i in range(number_of_blinks):
        for number in numbers:
            if number == "0":
                new_list.append('1')
                continue
            if len(number) % 2 == 0:
                new_list.append(number[:len(number)//2])
                removed_zeroes = int(number[len(number)//2:])
                new_list.append(str(removed_zeroes))
                continue
            else:
                new_number = int(number)*2024
                new_list.append(str(new_number))
        numbers = new_list
        new_list = []
    return len(numbers)


def super_blinking(numbers, number_of_blinks):
    temp_dict = {}
    possible_numbers = {}

    for number in numbers:
        if possible_numbers.get(number):
            possible_numbers[number] += 1
        else:
            possible_numbers[number] = 1

    for _ in range(number_of_blinks):
        for number in list(possible_numbers.keys()):
            number_of_possible_numbers = possible_numbers[number]

            if number == "0":
                temp_dict['1'] = temp_dict.get('1', 0) + number_of_possible_numbers
                continue

            if len(number) % 2 == 0:
                half1 = number[:len(number)//2]
                half2 = str(int(number[len(number)//2:]))
                temp_dict[half1] = temp_dict.get(half1, 0) + number_of_possible_numbers

                temp_dict[half2] = temp_dict.get(half2, 0) + number_of_possible_numbers
                continue

            else:
                new_number = str(int(number) * 2024)
                temp_dict[new_number] = temp_dict.get(new_number, 0) + number_of_possible_numbers

        possible_numbers.clear()
        possible_numbers.update(temp_dict)
        temp_dict.clear()

    return sum(possible_numbers.values())


if __name__ == "__main__":
    with open(r"day11\input") as f:
        numbers = f.read().split()

    # Part 1
    count = blinking(numbers, 25)
    print(count)

    # Part 2
    count = super_blinking(numbers, 75)
    print(count)
