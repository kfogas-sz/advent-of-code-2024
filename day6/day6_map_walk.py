
from enum import Enum


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


def walk(input_map, start):

    visited = {start}
    direction = Directions.UP
    visited_with_dir = set()
    visited_with_dir.add((start, direction))
    location = start

    while True:
        next_step = location[0] + direction.value[0], location[1] + direction.value[1]

        # Check if not out of bounds
        if next_step[0] < 0 or next_step[1] < 0 or next_step[0] >= len(input_map) or next_step[1] >= len(input_map[0]):
            break
        
        # Check if not "#"
        if input_map[next_step[0]][next_step[1]] == "#":
            direction = change_direction(direction)
            continue
        else:
            
            # Do the actual step
            location = next_step
            visited.add(location)
            
            location_with_vector = (location, direction)
            if location_with_vector in visited_with_dir:
                return None
                
            visited_with_dir.add((location, direction))

    return visited


def count_loops(input_map, start, possible_covered):
    loops = 0
    for visits in possible_covered:
        input_map[visits[0]][visits[1]] = '#'
        
        if not walk(input_map, start):
            loops += 1
        
        input_map[visits[0]][visits[1]] = '.'
        
    return loops


if __name__ == "__main__":
    count_obstructions = 0
    cycle_count = 0
    with open(r"day6\input") as f:
        lines = f.read().splitlines()
    input_map = [list(line) for line in lines]

    start = get_start(input_map, '^')
    visited = walk(input_map, start)
    
    print(len(visited))

    loops = count_loops(input_map, start, visited)
    
    print(loops)

    pass
