def count_trailheads(topo_map):

    count = 0
    for row_id, row in enumerate(topo_map):
        for col_id, item in enumerate(row):
            if item == 0:
                trailheads = get_trailheads(topo_map, row_id, col_id)
                count += len(trailheads)
    return count


def get_trailheads(topo_map, row_id, col_id):
    trailhead = set()

    if topo_map[row_id][col_id] == 9:
        trailhead.add((row_id, col_id))
        return trailhead

    try:
        if col_id > 0:
            if topo_map[row_id][col_id-1] - topo_map[row_id][col_id] == 1:
                trailhead.update(get_trailheads(topo_map, row_id, col_id-1))
        if col_id < len(topo_map[0])-1:
            if topo_map[row_id][col_id+1] - topo_map[row_id][col_id] == 1:
                trailhead.update(get_trailheads(topo_map, row_id, col_id+1))
        if row_id > 0:
            if topo_map[row_id-1][col_id] - topo_map[row_id][col_id] == 1:
                trailhead.update(get_trailheads(topo_map, row_id-1, col_id))
        if row_id < len(topo_map)-1:
            if topo_map[row_id+1][col_id] - topo_map[row_id][col_id] == 1:
                trailhead.update(get_trailheads(topo_map, row_id+1, col_id))
    except IndexError:
        pass
    return trailhead


if __name__ == "__main__":
    topo_map = []
    with open(r"day10\input") as f:
        lines = f.read().splitlines()
    topo_map = [list(line) for line in lines]
    for id_row, row in enumerate(topo_map):
        for id_col, item in enumerate(row):
            if item == '.':
                topo_map[id_row][id_col] = -1
    topo_map = [[int(item) for item in row] for row in topo_map]

    trailheads = count_trailheads(topo_map)

    print(trailheads)
