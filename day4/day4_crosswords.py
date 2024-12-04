

def reverse_horizontally(crossword):
    return [row[::-1] for row in crossword]


def reverse_vertically(crossword):
    return [list(row) for row in zip(*crossword[::-1])]


def word_counter(crossword, word):
    count = 0
    for row in crossword:
        row = "".join(row)
        count += row.count(word)
    return count


def get_diagonals(crossword):
    n = len(crossword)
    diagonals = []

    for i in range(2 * n - 1):
        diagonal = []
        for j in range(n):
            k = i - j
            if 0 <= k < n:
                diagonal.append(crossword[j][k])
        diagonals.append(diagonal)

    return diagonals


def count_all_word(crossword, word):

    # ->
    count = word_counter(crossword, word)
    temp = crossword

    # <-
    crossword = reverse_horizontally(crossword)
    count += word_counter(crossword, word)

    # ^
    # |
    crossword = reverse_vertically(crossword)
    count += word_counter(crossword, word)

    # |
    # ˇ
    crossword = reverse_horizontally(crossword)
    count += word_counter(crossword, word)

    # Diagonal
    #  ^
    #   \
    crossword = get_diagonals(crossword)
    count += word_counter(crossword, word)

    #  \
    #   ˇ
    crossword = reverse_horizontally(crossword)
    count += word_counter(crossword, word)

    #   /
    #  ˇ
    crossword = get_diagonals(temp)
    count += word_counter(crossword, word)

    #   ^
    #  /
    crossword = reverse_horizontally(crossword)
    count += word_counter(crossword, word)

    print(count)


def extract_mini_crosses(crossword):
    ret = []
    for i in range(1, len(crossword)-1):
        for j in range(1, len(crossword[i])-1):
            if crossword[i][j] == "A":
                temp = []
                try:
                    temp.append(crossword[i-1][j - 1: j + 2])
                    temp.append(crossword[i][j - 1: j + 2])
                    temp.append(crossword[i+1][j - 1: j + 2])
                    ret.append(temp)
                except IndexError:
                    continue
    return ret


def count_xmas(crossword):

    word = "MAS"
    count = 0

    mini_crosses = extract_mini_crosses(crossword)

    for mini_cross in mini_crosses:
        mini_count = 0
        temp = reverse_vertically(mini_cross)
        mini_cross = get_diagonals(mini_cross)
        mini_count += word_counter(mini_cross, word)

        mini_cross = reverse_horizontally(mini_cross)
        mini_count += word_counter(mini_cross, word)

        mini_cross = get_diagonals(temp)
        mini_count += word_counter(mini_cross, word)

        mini_cross = reverse_horizontally(mini_cross)
        mini_count += word_counter(mini_cross, word)

        if mini_count > 1:
            count += 1

    print(count)


if __name__ == "__main__":
    crossword = []
    with open(r"day4\input") as f:
        lines = f.read().splitlines()
        crossword = [list(line) for line in lines]
        count_all_word(crossword, "XMAS")

        count_xmas(crossword)
