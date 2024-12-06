
import copy
import time
from enum import Enum
from functools import wraps


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time:.4f} seconds to finish')
        return result
    return timeit_wrapper


class Directions(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


def change_direction(direction):
    if direction == Directions.UP:
        return Directions.RIGHT
    if direction == Directions.RIGHT:
        return Directions.DOWN
    if direction == Directions.DOWN:
        return Directions.LEFT
    if direction == Directions.LEFT:
        return Directions.UP


def get_start(input_map, start):
    for i, x in enumerate(input_map):
        if start in x:
            return (i, x.index(start))


def test_obstructions(input_map, location, direction, visited_with_dir):

    pass
    while True:
        next_step = location[0] + direction.value[0], location[1] + direction.value[1]

        try:
            if input_map[next_step[0]][next_step[1]] == "O":
                direction = change_direction(direction)
                continue
        except IndexError:
            return False

        if next_step[0] < 0 or next_step[1] < 0 or next_step[0] >= len(input_map) or next_step[1] >= len(input_map[0]):
            return False
        location_with_vector = (next_step, direction)
        if location_with_vector in visited_with_dir:
            # for row in input_map:
            #     print(" ".join(map(str, row)))
            # print()
            return True

        opposite_location_vector = (location, change_direction(change_direction(direction)))
        if opposite_location_vector in visited_with_dir:
            return False

        if input_map[next_step[0]][next_step[1]] == "#" or input_map[next_step[0]][next_step[1]] == "O":
            direction = change_direction(direction)
        else:
            input_map[location[0]][location[1]] = "*"
            # for row in input_map:
            #     print(" ".join(map(str, row)))
            # print()
            location = next_step
            visited_with_dir.add((location, direction))


@timeit
def walk(input_map, start):

    cycle_count = 0
    count_obstructions = 0
    visited = {start}
    direction = Directions.UP
    visited_with_dir = set()
    visited_with_dir.add((start, direction))
    location = start

    while True:
        next_step = location[0] + direction.value[0], location[1] + direction.value[1]

        # try:
        #     if input_map[next_step[0]][next_step[1]] == "#":
        #         direction = change_direction(direction)
        #         continue
        # except IndexError:
        #     continue

        if next_step[0] < 0 or next_step[1] < 0 or next_step[0] >= len(input_map) or next_step[1] >= len(input_map[0]):
            break
        if input_map[next_step[0]][next_step[1]] == "#":
            direction = change_direction(direction)
        else:
            input_map[location[0]][location[1]] = "X"
            obstructed_map = copy.deepcopy(input_map)
            if next_step != start:
                obstructed_map[next_step[0]][next_step[1]] = "O"
                if test_obstructions(obstructed_map, location, direction, copy.deepcopy(visited_with_dir)):
                    count_obstructions += 1
            location = next_step
            visited.add(location)
            visited_with_dir.add((location, direction))

            cycle_count += 1
            if cycle_count % 100 == 0:
                print(cycle_count)

    return visited, count_obstructions


if __name__ == "__main__":
    with open(r"day6\input") as f:
        lines = f.read().splitlines()
    input_map = [list(line) for line in lines]

    start = get_start(input_map, '^')
    visited, count_obstructions = walk(input_map, start)

    print(len(visited))
    print(count_obstructions)

    pass
