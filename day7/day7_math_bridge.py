from itertools import product


def variations(elements, length):
    return [''.join(variation) for variation in product(elements, repeat=length)]


def count_good_results(lines, operators):
    total_calibration_result = 0
    for line in lines:
        result, numbers = line.split(':')
        result = int(result)
        numbers = list(map(int, numbers.split()))

        variants = variations(operators, len(numbers)-1)

        for list_operators in variants:
            actual_result = 0
            for number, operator in zip(numbers, ' '+list_operators):
                if operator == ' ':
                    actual_result = number
                if operator == '+':
                    actual_result += number
                if operator == '*':
                    actual_result *= number
                if operator == 'c':
                    actual_result = int(str(actual_result) + str(number))

                pass
            if actual_result == result:
                total_calibration_result += result
                break
    return total_calibration_result


if __name__ == "__main__":
    with open(r"day7\input") as f:
        lines = f.read().splitlines()

    print(count_good_results(lines, '*+'))

    print(count_good_results(lines, '*+c'))
