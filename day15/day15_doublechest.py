

import copy

LEFT = '<'
RIGHT = '>'
UP = '^'
DOWN = 'v'


def get_location(topo_map, box):
    locations = []
    for row_id, row in enumerate(topo_map):
        for col_id, item in enumerate(row):
            if item == box:
                locations.append((row_id, col_id))
    if len(locations) == 1:
        return locations[0]
    return locations


def join_movements(movements):
    movements = movements.replace("\n", "")
    return movements


def paint_map(robot_map, robot_loc, movement):

    print('\033[31m', end="")
    print(movement, end="")
    print('\033[0m')
    for idx, row in enumerate(robot_map):
        for idy, item in enumerate(row):
            if (idx, idy) == robot_loc:
                print('\033[31m', end="")
                print(movement, end="")
                print('\033[0m', end="")
                continue
            else:
                print(item, end="")
        print("")
    print("\n")


def try_move(robot_map, robot_loc, robot_type, movement):
    row, col = robot_loc
    # paint_map(robot_map, robot_loc, movement)
    while True:
        if robot_map[robot_loc[0]][robot_loc[1]] == '.':
            return False

        if movement == LEFT:
            if robot_map[row][col-1] == '#':
                return False

            if robot_map[row][col-1] == '.':
                robot_map[row][col] = '.'
                robot_map[row][col-1] = robot_type
                return True

            if robot_map[row][col-1] == ']':
                if not try_move(robot_map, (row, col-1), "]", LEFT):
                    return False

            if robot_map[row][col-1] == '[':
                if not try_move(robot_map, (row, col-1), "[", LEFT):
                    return False

        if movement == RIGHT:
            if robot_map[row][col+1] == '#':
                return False

            if robot_map[row][col+1] == '.':
                robot_map[row][col] = '.'
                robot_map[row][col+1] = robot_type
                return True

            if robot_map[row][col+1] == ']':
                if not try_move(robot_map, (row, col+1), "]", RIGHT):
                    return False

            if robot_map[row][col+1] == '[':
                if not try_move(robot_map, (row, col+1), "[", RIGHT):
                    return False

        if movement == UP:
            if robot_map[row-1][col] == '#':
                return False

            if robot_map[row][col] == '[':
                if robot_map[row-1][col+1] == '#':
                    return False

            if robot_map[row][col] == ']':
                if robot_map[row-1][col-1] == '#':
                    return False

            if robot_map[row-1][col] == '[':
                if not try_move(robot_map, (row-1, col), "[", UP):
                    return False

            if robot_map[row-1][col] == ']':
                if not try_move(robot_map, (row-1, col), "]", UP):
                    return False

            if robot_map[row][col] == ']':

                if robot_map[row-1][col] == '.' and robot_map[row-1][col-1] == '.':
                    robot_map[row][col] = '.'
                    robot_map[row][col-1] = '.'
                    robot_map[row-1][col] = ']'
                    robot_map[row-1][col-1] = '['
                    return True

                if robot_map[row-1][col-1] == '[':
                    if not try_move(robot_map, (row-1, col-1), "[", UP):
                        return False
                if robot_map[row-1][col-1] == ']':
                    if not try_move(robot_map, (row-1, col-1), "]", UP):
                        return False

            if robot_map[row][col] == '[':

                if robot_map[row-1][col] == '.' and robot_map[row-1][col+1] == '.':
                    robot_map[row][col] = '.'
                    robot_map[row][col+1] = '.'
                    robot_map[row-1][col] = '['
                    robot_map[row-1][col+1] = ']'
                    return True

                if robot_map[row-1][col+1] == '[':
                    if not try_move(robot_map, (row-1, col+1), "[", UP):
                        return False
                if robot_map[row-1][col+1] == ']':
                    if not try_move(robot_map, (row-1, col+1), "]", UP):
                        return False

            if robot_map[row][col] == '@':
                if robot_map[row-1][col] == '.':
                    robot_map[row][col] = '.'
                    robot_map[row-1][col] = robot_type
                    return True

        if movement == DOWN:
            if robot_map[row+1][col] == '#':
                return False

            if robot_map[row][col] == '[':
                if robot_map[row+1][col+1] == '#':
                    return False

            if robot_map[row][col] == ']':
                if robot_map[row+1][col-1] == '#':
                    return False

            if robot_map[row+1][col] == '[':
                if not try_move(robot_map, (row+1, col), "[", DOWN):
                    return False

            if robot_map[row+1][col] == ']':
                if not try_move(robot_map, (row+1, col), "]", DOWN):
                    return False

            if robot_map[row][col] == ']':

                if robot_map[row+1][col] == '.' and robot_map[row+1][col-1] == '.':
                    robot_map[row][col] = '.'
                    robot_map[row][col-1] = '.'
                    robot_map[row+1][col] = ']'
                    robot_map[row+1][col-1] = '['
                    return True

                if robot_map[row+1][col-1] == '[':
                    if not try_move(robot_map, (row+1, col-1), "[", DOWN):
                        return False
                if robot_map[row+1][col-1] == ']':
                    if not try_move(robot_map, (row+1, col-1), "]", DOWN):
                        return False

            if robot_map[row][col] == '[':

                if robot_map[row+1][col] == '.' and robot_map[row+1][col+1] == '.':
                    robot_map[row][col] = '.'
                    robot_map[row][col+1] = '.'
                    robot_map[row+1][col] = '['
                    robot_map[row+1][col+1] = ']'
                    return True

                if robot_map[row+1][col+1] == '[':
                    if not try_move(robot_map, (row+1, col+1), "[", DOWN):
                        return False
                if robot_map[row+1][col+1] == ']':
                    if not try_move(robot_map, (row+1, col+1), "]", DOWN):
                        return False

            if robot_map[row][col] == '@':
                if robot_map[row+1][col] == '.':
                    robot_map[row][col] = '.'
                    robot_map[row+1][col] = robot_type
                    return True


def calculate_location(box_loc):
    row, col = box_loc
    return 100 * row + col


def widen_map(robot_map):
    temp_map = []
    for row in robot_map:
        temp_row = []
        for item in row:
            if item == '#':
                temp_row.append('#')
                temp_row.append('#')
            elif item == 'O':
                temp_row.append('[')
                temp_row.append(']')
            elif item == '.':
                temp_row.append('.')
                temp_row.append('.')
            elif item == '@':
                temp_row.append('@')
                temp_row.append('.')

        temp_map.append(temp_row)

    return temp_map


if __name__ == "__main__":
    test_map = []
    count = 0
    speed = 0.3
    with open(r"day15\input") as f:
        map, movements = f.read().split("\n\n")

    robot_map = map.splitlines()
    robot_map = [list(line) for line in robot_map]
    robot_map = [[item for item in row] for row in robot_map]

    robot_map = widen_map(robot_map)

    movements = join_movements(movements)

    # os.system('cls')
    for idx, movement in enumerate(movements):
        robot_loc = get_location(robot_map, '@')
        # paint_map(robot_map, robot_loc, movement)
        test_map = copy.deepcopy(robot_map)
        moved = try_move(test_map, robot_loc, "@", movement)
        if moved:
            robot_map = copy.deepcopy(test_map)
        else:
            test_map.clear()

    box_locations = get_location(robot_map, '[')

    for box_loc in box_locations:
        count += calculate_location(box_loc)

    print(count)
