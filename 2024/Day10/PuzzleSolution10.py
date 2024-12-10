
"""
Part 1 Solution
Read the input into a matrix.
Perform a DFS from each trailhead, or could take each 9 and DFS for trail heads, either way should be the same result
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
    process_file("ExampleInput10.txt")

    if PROCESS_FULL_INPUT:
        print()
        process_file("PuzzleInput10.txt")


def process_file(file_name):
    print(f"Processing: {file_name}")
    with open(file_name) as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        print("Part 1")
        start = time.time()
        result1 = solve_part1(lines)
        end = time.time()
        print(f"Part 1 result: {result1}")
        print(f"Elapsed time {end - start}")

        if SOLVE_PART_2:
            print("\nPart 2")
            start = time.time()
            result2 = solve_part2(lines)
            end = time.time()
            print(f"Part 2 result: {result2}")
            print(f"Elapsed time {end - start}")


def dfs_helper(trail_map, visited, row, col):
    # return set of the 9 height positions reachable from this position
    terminals = set()
    if (row, col) in visited:
        return terminals
    visited.add((row, col))
    log(f"visiting: {row, col}, map: {trail_map[row][col]}")

    if trail_map[row][col] == 9:
        terminals.add((row, col))
        log(f"at 9 cell, {terminals}")
        return terminals

    # up, down, left, right
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in dirs:
        if 0 <= row+dr < len(trail_map) and 0 <= col+dc < len(trail_map[0]):
            if trail_map[row + dr][col + dc] == trail_map[row][col]+1:
                neighbor = dfs_helper(trail_map, visited, row + dr, col + dc)
                log(f"result for neighbor {row, col}, {neighbor}")
                terminals = terminals.union(neighbor)

    log(f"found terminals for {row, col}, {terminals}")
    return terminals


def solve_part1(lines):
    trail_map = list()
    for line in lines:
        line = [int(x) for x in line]
        log(line)
        trail_map.append(line)

    # for each trail head, need to find the number of height 9 positions reachable
    scores: dict[tuple[int, int], set] = dict()
    for row in range(len(trail_map)):
        for col in range(len(trail_map[0])):
            if trail_map[row][col] == 0:
                log(f"starting new search at {row, col}")
                visited = set()
                scores[(row, col)] = dfs_helper(trail_map, visited, row, col)

    log(scores)
    result = 0
    for key in scores:
        result += len(scores[key])

    return result


def dfs_helper2(trail_map, row, col):
    # return set of the 9 height positions reachable from this position
    log(f"visiting: {row, col}, map: {trail_map[row][col]}")

    if trail_map[row][col] == 9:
        trail = [(row, col)]
        log(f"at 9 cell, {trail}")
        trails = list()
        trails.append(trail)
        return trails

    # up, down, left, right
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    trails = list()
    for dr, dc in dirs:
        if 0 <= row+dr < len(trail_map) and 0 <= col+dc < len(trail_map[0]):
            if trail_map[row + dr][col + dc] == trail_map[row][col]+1:
                neighbor = dfs_helper2(trail_map, row + dr, col + dc)
                for trail in neighbor:
                    trail.append((row, col))
                    trails.append(trail)
                log(f"result for neighbor {row, col}, {neighbor}")

    log(f"found trails for {row, col}, {trails}")
    return trails


def solve_part2(lines):
    trail_map = list()
    for line in lines:
        line = [int(x) for x in line]
        log(line)
        trail_map.append(line)

    ratings: dict[tuple[int, int], list] = dict()
    for row in range(len(trail_map)):
        for col in range(len(trail_map[0])):
            if trail_map[row][col] == 0:
                log(f"starting new search at {row, col}")
                ratings[(row, col)] = dfs_helper2(trail_map, row, col)

    log(ratings)
    result = 0
    for key in ratings:
        result += len(ratings[key])

    return result


if __name__ == '__main__':
    main()
