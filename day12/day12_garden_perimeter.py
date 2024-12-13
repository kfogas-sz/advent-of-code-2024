from enum import Enum


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


class DiagWithDirection(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    TOP_LEFT = (-1, -1)
    TOP_RIGHT = (-1, 1)
    BOTTOM_LEFT = (1, -1)
    BOTTOM_RIGHT = (1, 1)


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


def count_neighbors(connected_items):

    neighbor_counts = {}

    for row, col in connected_items:
        count = 0
        for dir_row, dir_col in (direction.value for direction in Direction):
            new_row, new_col = row + dir_row, col + dir_col
            if (new_row, new_col) in connected_items:
                count += 1
        neighbor_counts[(row, col)] = count

    return neighbor_counts


def count_corners(connected_items):
    corners = 0

    for row, col in connected_items:
        has_top = (row + DiagWithDirection.UP.value[0], col + DiagWithDirection.UP.value[1]) in connected_items
        has_bottom = (row + DiagWithDirection.DOWN.value[0], col + DiagWithDirection.DOWN.value[1]) in connected_items
        has_left = (row + DiagWithDirection.LEFT.value[0], col + DiagWithDirection.LEFT.value[1]) in connected_items
        has_right = (row + DiagWithDirection.RIGHT.value[0], col + DiagWithDirection.RIGHT.value[1]) in connected_items
        has_top_left = (row + DiagWithDirection.TOP_LEFT.value[0], col + DiagWithDirection.TOP_LEFT.value[1]) in connected_items
        has_top_right = (row + DiagWithDirection.TOP_RIGHT.value[0], col + DiagWithDirection.TOP_RIGHT.value[1]) in connected_items
        has_bottom_left = (row + DiagWithDirection.BOTTOM_LEFT.value[0], col + DiagWithDirection.BOTTOM_LEFT.value[1]) in connected_items
        has_bottom_right = (row + DiagWithDirection.BOTTOM_RIGHT.value[0], col + DiagWithDirection.BOTTOM_RIGHT.value[1]) in connected_items

        if not has_top and not has_left:
            corners += 1
        if not has_top and not has_right:
            corners += 1
        if not has_bottom and not has_right:
            corners += 1
        if not has_bottom and not has_left:
            corners += 1

        if has_bottom and has_right and not has_bottom_right:
            corners += 1
        if has_bottom and has_left and not has_bottom_left:
            corners += 1
        if has_top and has_right and not has_top_right:
            corners += 1
        if has_top and has_left and not has_top_left:
            corners += 1

    return corners


def iter_map():

    global garden_plots
    global garden_map
    global total_price
    global total_price_discounted

    for id_row, row in enumerate(garden_map):
        for id_col, plot in enumerate(row):
            if plot != '*':
                connected_items = find_plot_area(garden_map, id_row, id_col)
                for item in connected_items:
                    row, col = item
                    garden_map[row][col] = '*'
                garden_plots.append(connected_items)
                neighbours = count_neighbors(connected_items)
                perimeter = len(connected_items)*4 - sum(neighbours.values())
                number_of_sides = count_corners(connected_items)
                total_price += perimeter * len(connected_items)
                total_price_discounted += number_of_sides * len(connected_items)


if __name__ == "__main__":
    total_price = 0
    total_price_discounted = 0
    garden_plots = []
    with open(r"day12\input") as f:
        lines = f.read().splitlines()

    garden_map = [list(line) for line in lines]
    iter_map()

    print(total_price)
    print(total_price_discounted)
