
"""
Part 1 Solution
to find the regions, thinking of using a DFS, track the coordinates, and amount of perimeter as you go

Part 2 Solution
Count the corners
"""
import time

DEBUG = False
PROCESS_FULL_INPUT = True
SOLVE_PART_2 = True


def log(s):
    if DEBUG:
        print(s)


def main():
    print("Hello")
    process_file("ExampleInput12.txt")

    if PROCESS_FULL_INPUT:
        print()
        process_file("PuzzleInput12.txt")


def process_file(file_name):
    with open(file_name) as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        print(f"Part 1: {file_name}")
        start = time.time()
        result1 = solve_part1(lines)
        end = time.time()
        print(f"Part 1 result: {result1}")
        print(f"Elapsed time {end - start}")

        if SOLVE_PART_2:
            print(f"\nPart 2: {file_name}")
            start = time.time()
            result2 = solve_part2(lines)
            end = time.time()
            print(f"Part 2 result: {result2}")
            print(f"Elapsed time {end - start}")


def solve_part1(lines):
    garden = list()
    for line in lines:
        line = list(line)
        log(line)
        garden.append(line)

    regions = list()
    visited = set()
    num_rows = len(garden)
    num_cols = len(garden[0])

    def dfs_helper(row, col):
        region = set()
        perimeter = 0
        if (row, col) in visited:
            return region, perimeter
        visited.add((row, col))

        region.add((row, col))

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in dirs:
            nr = row + dr
            nc = col + dc
            if 0 <= nr < num_rows and 0 <= nc < num_cols and garden[nr][nc] == garden[row][col]:
                    nreg, nper = dfs_helper(nr, nc)
                    region = region.union(nreg)
                    perimeter += nper
            else:
                perimeter += 1
        return region, perimeter

    for r in range(num_rows):
        for c in range(num_cols):
            if (r, c) not in visited:
                reg, per = dfs_helper(r, c)
                regions.append(len(reg)*per)
                log(f"{garden[r][c]}: {len(reg)}, {per}")

    log(regions)
    result = sum(regions)

    return result


def solve_part2(lines):
    garden = list()
    for line in lines:
        line = list(line)
        log(line)
        garden.append(line)

    regions = list()
    visited1 = set()
    num_rows = len(garden)
    num_cols = len(garden[0])
    edge_data = [[[False, False, False, False] for _ in range(num_cols)] for _ in range(num_rows)]

    def dfs_helper_find_edges(row, col):
        if (row, col) in visited1:
            return
        visited1.add((row, col))

        # up, down, left, right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        edges = [False, False, False, False]

        for idx in range(len(dirs)):
            dr, dc = dirs[idx]
            nr = row + dr
            nc = col + dc
            if 0 <= nr < num_rows and 0 <= nc < num_cols and garden[nr][nc] == garden[row][col]:
                dfs_helper_find_edges(nr, nc)
            else:
                edges[idx] = True

        log(f"point: {row, col}, edges {edges}")

        edge_data[row][col] = edges
        return

    visited2 = set()

    def dfs_helper_calc_cost(row, col):
        region = set()
        perimeter = 0
        if (row, col) in visited2:
            return region, perimeter
        visited2.add((row, col))
        region.add((row, col))

        # up, down, left right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbor_edges = []

        for idx in range(len(dirs)):
            dr, dc = dirs[idx]
            nr = row + dr
            nc = col + dc
            if 0 <= nr < num_rows and 0 <= nc < num_cols and garden[nr][nc] == garden[row][col]:
                new_reg, new_per = dfs_helper_calc_cost(nr, nc)
                neighbor_edges.append((idx, edge_data[nr][nc]))
                region = region.union(new_reg)
                perimeter += new_per

        edges = edge_data[row][col]

        # top-left, bottom-left, top-right bottom-right
        corners = [False, False, False, False]
        if edges[0] and edges[2]:
            corners[0] = True
        if edges[1] and edges[2]:
            corners[1] = True
        if edges[0] and edges[3]:
            corners[2] = True
        if edges[1] and edges[3]:
            corners[3] = True

        for idx, new_edges in neighbor_edges:
            if idx == 0:
                if new_edges[2] and not edges[2]:
                    corners[0] = True
                if new_edges[3] and not edges[3]:
                    corners[2] = True
            if idx == 1:
                if new_edges[2] and not edges[2]:
                    corners[1] = True
                if new_edges[3] and not edges[3]:
                    corners[3] = True
            if idx == 2:
                if new_edges[0] and not edges[0]:
                    corners[0] = True
                if new_edges[1] and not edges[1]:
                    corners[1] = True
            if idx == 3:
                if new_edges[0] and not edges[0]:
                    corners[2] = True
                if new_edges[1] and not edges[1]:
                    corners[3] = True

        log(f"point: {row, col}, edges {edges}, neighbor_edges: {neighbor_edges}, corners: {corners}, sum: {sum(corners)}")

        perimeter += sum(corners)
        return region, perimeter

    for r in range(num_rows):
        for c in range(num_cols):
            if (r, c) not in visited2:
                dfs_helper_find_edges(r, c)

    for r in range(num_rows):
        for c in range(num_cols):
            if (r, c) not in visited2:
                reg, per = dfs_helper_calc_cost(r, c)
                regions.append(len(reg) * per)
                log(f"{garden[r][c]}: {len(reg)}, {per}")


    log(edge_data)
    log(regions)
    result = sum(regions)

    return result


if __name__ == '__main__':
    main()
