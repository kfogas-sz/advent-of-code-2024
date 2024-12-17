

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


def paint_map(robot_map):
    print("\n".join(["".join(row) for row in robot_map]))
    print("\n")


def try_move(robot_map, robot_loc, robot_type, movement):
    row, col = robot_loc
    while True:

        paint_map(robot_map)

        if movement == LEFT:
            if robot_map[row][col-1] == '#':
                return False

            if robot_map[row][col-1] == '.':
                robot_map[row][col] = '.'
                robot_map[row][col-1] = robot_type
                robot_loc = (row, col-1)
                return True

            if robot_map[row][col-1] == 'O':
                if not try_move(robot_map, (row, col-1), "O", LEFT):
                    return False

        if movement == RIGHT:
            if robot_map[row][col+1] == '#':
                return False

            if robot_map[row][col+1] == '.':
                robot_map[row][col] = '.'
                robot_map[row][col+1] = robot_type
                robot_loc = (row, col+1)
                return True

            if robot_map[row][col+1] == 'O':
                if not try_move(robot_map, (row, col+1), "O", RIGHT):
                    return False

        if movement == UP:
            if robot_map[row-1][col] == '#':
                return False

            if robot_map[row-1][col] == '.':
                robot_map[row][col] = '.'
                robot_map[row-1][col] = robot_type
                robot_loc = (row-1, col)
                return True

            if robot_map[row-1][col] == 'O':
                if not try_move(robot_map, (row-1, col), "O", UP):
                    return False

        if movement == DOWN:
            if robot_map[row+1][col] == '#':
                return False

            if robot_map[row+1][col] == '.':
                robot_map[row][col] = '.'
                robot_map[row+1][col] = robot_type
                robot_loc = (row+1, col)
                return True

            if robot_map[row+1][col] == 'O':
                if not try_move(robot_map, (row+1, col), "O", DOWN):
                    return False


def calculate_location(box_loc):
    row, col = box_loc
    return 100 * row + col


if __name__ == "__main__":
    count = 0
    with open(r"day15\input") as f:
        map, movements = f.read().split("\n\n")

    robot_map = map.splitlines()
    robot_map = [list(line) for line in robot_map]
    robot_map = [[item for item in row] for row in robot_map]

    movements = join_movements(movements)

    for movement in movements:
        robot_loc = get_location(robot_map, '@')
        try_move(robot_map, robot_loc, "@", movement)

    print("\n".join(["".join(row) for row in robot_map]))

    box_locations = get_location(robot_map, 'O')

    for box_loc in box_locations:
        count += calculate_location(box_loc)

    print(count)
    pass
