import heapq
import re

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def fast_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    open_list = []
    heapq.heappush(open_list, (0, start[0], start[1], 0))
    g_scores = {}
    g_scores[start] = 0

    while open_list:
        current_cost, x, y, current_g = heapq.heappop(open_list)

        if (x, y) == end:
            return current_cost

        for dir_x, dir_y in directions:
            new_x, new_y = x + dir_x, y + dir_y
            if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] != '#':
                new_g = current_g + 1
                if (new_x, new_y) not in g_scores or new_g < g_scores[(new_x, new_y)]:
                    g_scores[(new_x, new_y)] = new_g
                    heapq.heappush(open_list, (new_g + heuristic((new_x, new_y), end), new_x, new_y, new_g))

    return None


if __name__ == "__main__":
    fall_map = []
    for _ in range(71):
        fall_map.append(['.'] * 71)

    with open(r"day18\input") as f:
        lines = f.read().splitlines()
    for idx, line in enumerate(lines):
        col, row = map(int, re.findall(r"\d+", line))
        fall_map[row][col] = '#'
        cost = fast_maze(fall_map, (0, 0), (70, 70))
        if cost is None:
            print(f"The unreachable maze caused by point:{line}")
            break
        if idx == 1024:
            print(f"Part 1: {cost}")
