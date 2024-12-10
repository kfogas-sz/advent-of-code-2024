def produce_files_spaces(line):
    files = []
    spaces = []
    for id, item in enumerate(line):
        if id % 2 == 0:
            files.append(item)
        else:
            spaces.append(item)

    return files, spaces+['0']


def fragment(files, spaces, orig_input=None, part2=False):

    disk = []

    for id, file in enumerate(files):
        for _ in range(int(file)):
            disk.append(id)

    result = [disk[0]]

    space_index = 0
    for i in range(1, len(disk)):
        if disk[i] != disk[i - 1]:
            result.extend(['.'] * int(spaces[space_index]))
            space_index += 1
        result.append(disk[i])

    if not part2:
        for id in range(len(result)-1, -1, -1):
            if result[id] != '.':
                dot_index = result.index('.')
                if dot_index < id:
                    result[dot_index] = result[id]
                    result[id] = '.'
                else:
                    pass
    else:
        spaces = list(map(int, spaces))
        files = list(map(int, files))
        orig_input = list(map(int, orig_input))
        start_of_dot = []
        start_of_number = []

        for id, _ in enumerate(orig_input):
            start = sum(orig_input[:id])
            if id % 2 != 0:
                start_of_dot.append(start)
            else:
                start_of_number.append(start)

        for idx_file, file in reversed(list(enumerate(files))):
            for id, space in enumerate(spaces):
                try:
                    if start_of_dot[id] < start_of_number[idx_file]:
                        if file <= space:
                            i = 0
                            for i in range(int(file)):
                                result[start_of_dot[id]+i] = idx_file
                                spaces[id] -= 1
                                result[start_of_number[idx_file]+i] = '.'
                            start_of_dot[id] += file
                            break
                except IndexError:
                    pass

    return result


def count_checksum(row):
    checksum = 0
    for id, item in enumerate(row):
        if item != '.':
            checksum += item*id
    return checksum


if __name__ == "__main__":
    with open(r"day9\input") as f:
        line = f.read()

    files, spaces = produce_files_spaces(line)
    # Part 1
    part1 = fragment(files, spaces)
    checksum = count_checksum(part1)
    print(checksum)

    # Part 2
    part2 = fragment(files, spaces, orig_input=line, part2=True)
    checksum2 = count_checksum(part2)
    print(checksum2)
