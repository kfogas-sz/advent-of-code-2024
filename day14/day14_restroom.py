from enum import Enum

HEIGHT = 103
WIDTH = 101
SECONDS = 100


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


def find_plot_area(grid, id_row, id_col):

    max_rows, max_cols = len(grid), len(grid[0])
    plot_type = grid[id_row][id_col]
    visited = set()

    def search_visited(row, col):
        if (row, col) in visited:
            return
        visited.add((row, col))

        for dir_row, dir_col in (direction.value for direction in Direction):
            new_row, new_col = row + dir_row, col + dir_col
            if 0 <= new_row < max_rows and 0 <= new_col < max_cols and (new_row, new_col) not in visited:
                if grid[new_row][new_col] == plot_type:
                    search_visited(new_row, new_col)

    search_visited(id_row, id_col)

    return visited


def iter_map(iteration):

    global tiles_part2

    for id_row, row in enumerate(tiles_part2):
        for id_col, plot in enumerate(row):
            if plot != '.':
                connected_items = find_plot_area(tiles_part2, id_row, id_col)
                if len(connected_items) > 200:
                    print(f"Found at iteration {iteration}")
                    return True
                for item in connected_items:
                    row, col = item
                    tiles_part2[row][col] = '.'
    return False


if __name__ == "__main__":
    start_robots = []
    end_robots = []
    quadrant = [0, 0, 0, 0]
    tiles = [["." for _ in range(WIDTH)] for _ in range(HEIGHT)]

    with open(r"day14\input") as f:
        lines = f.read().splitlines()
    for line in lines:
        pos_str, vel_str = line.split(" ")
        pos = tuple(map(int, pos_str[2:].split(",")))
        pos = pos[::-1]
        vel = tuple(map(int, vel_str[2:].split(",")))
        vel = vel[::-1]
        start_robots.append((pos, vel))

    for robot in start_robots:
        pos, vel = robot
        row, col = pos
        y_vel, x_vel = vel

        row = (row + y_vel*SECONDS) % HEIGHT
        col = (col + x_vel*SECONDS) % WIDTH

        end_robots.append((row, col))

    for robot in end_robots:
        row, col = robot
        tiles[row][col] = "1" if tiles[row][col] == "." else str((int(tiles[row][col]) + 1))

        if row < HEIGHT//2 and col < WIDTH//2:
            quadrant[0] += 1
        elif row < HEIGHT//2 and col > WIDTH//2:
            quadrant[1] += 1
        elif row > HEIGHT//2 and col < WIDTH//2:
            quadrant[2] += 1
        elif row > HEIGHT//2 and col > WIDTH//2:
            quadrant[3] += 1

    print(quadrant)
    result = quadrant[0] * quadrant[1] * quadrant[2] * quadrant[3]
    print(result)

    i = 0
    tiles_part2 = [["." for _ in range(WIDTH)] for _ in range(HEIGHT)]
    while True:
        for robot in start_robots:
            pos, vel = robot
            row, col = pos
            y_vel, x_vel = vel

            row = (row + y_vel*i) % HEIGHT
            col = (col + x_vel*i) % WIDTH

            tiles_part2[row][col] = "1"

        if iter_map(i):
            print("\n".join(["".join(row) for row in tiles_part2]))
            break
        i += 1
