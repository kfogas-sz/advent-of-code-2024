from itertools import permutations


def get_unique_antennas(antenna_map):
    unique_antennas = {}
    for row_id, row in enumerate(antenna_map):
        for col_id, antenna in enumerate(row):
            if antenna == ".":
                continue
            if antenna not in unique_antennas:
                unique_antennas[antenna] = []
            unique_antennas[antenna].append((row_id, col_id))
    return unique_antennas


def get_antenna_pairs(unique_antennas):
    antenna_pairs = []
    for antenna_pair in permutations(unique_antennas, 2):
        antenna_pairs.append(antenna_pair)
    return antenna_pairs


def out_of_bounds(antenna_map, position):
    if position[0] < 0 or position[1] < 0:
        return True
    if position[0] >= len(antenna_map) or position[1] >= len(antenna_map[0]):
        return True
    return False


def count_antinodes(antenna_map):
    count = 0
    for row in antenna_map:
        count += row.count("#")
    return count


def paint_map(antenna_pairs, antenna_map, part2=False):
    for antenna_pair in antenna_pairs:
        i = 1
        diff_x = (antenna_pair[0][0] - antenna_pair[1][0])
        diff_y = (antenna_pair[0][1] - antenna_pair[1][1])
        if part2:
            antenna_map[antenna_pair[0][0]][antenna_pair[0][1]] = "#"
            antenna_map[antenna_pair[1][0]][antenna_pair[1][1]] = "#"

        while True:
            antinode_position = (antenna_pair[0][0] + (diff_x*i), antenna_pair[0][1] + (diff_y*i))
            if not out_of_bounds(antenna_map, antinode_position):

                antenna_map[antinode_position[0]][antinode_position[1]] = "#"

            else:
                break
            if part2:
                i += 1
            else:
                break


if __name__ == "__main__":
    antenna_map = []
    count_part_1 = 0
    count_part_2 = 0
    with open(r"day8\input") as f:
        lines = f.read().splitlines()
    antenna_map = [list(line) for line in lines]

    unique_antennas = get_unique_antennas(antenna_map)

    # Part 1
    for _, antennas in unique_antennas.items():
        antenna_pairs = get_antenna_pairs(antennas)
        paint_map(antenna_pairs, antenna_map)
        count_part_1 = count_antinodes(antenna_map)

    # Part 2
    for _, antennas in unique_antennas.items():
        antenna_pairs = get_antenna_pairs(antennas)
        paint_map(antenna_pairs, antenna_map, part2=True)
        count_part_2 = count_antinodes(antenna_map)

    print(count_part_1)
    print(count_part_2)
