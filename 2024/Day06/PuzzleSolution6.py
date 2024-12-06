
"""
Part 1 Solution

Part 2 Solution
Brute force solution, try adding obstacle at every possible position and see if it creates a loop
Is there a more efficient solution?
The obstacle must be places at one of the cells to guard currently visits, or it will have no effect
How can you tell you are stuck in a loop? Back at the same place facing the same way?
Not sure if that is correct in all cases, is a more complex patter that repeats considered a loop?
Maybe you need to be at the same place you last were facing this direction.
More complex loops do count
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
    process_file("ExampleInput6.txt")

    if PROCESS_FULL_INPUT:
        print()
        process_file("PuzzleInput6.txt")


def process_file(file_name):
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


def print_map(map):
    for line in map:
        log(line)


def find_visited_cells(map, row, col):
    visited = set()
    # up, right, down, left
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    cur_dir = 0

    while 0 <= row < len(map) and 0 <= col < len(map[0]):
        if map[row][col] == "#":
            row = row - dirs[cur_dir][0]
            col = col - dirs[cur_dir][1]
            cur_dir = (cur_dir + 1) % len(dirs)
        else:
            visited.add((row, col))
            row = row + dirs[cur_dir][0]
            col = col + dirs[cur_dir][1]

    return visited


def solve_part1(lines):
    start_row = 0
    start_col = 0

    map = list()
    for row in range(len(lines)):
        line = lines[row]
        map.append(list(line))
        if "^" in line:
            start_row = row
            start_col = line.index("^")
    # print_map(map)
    log(f"starting at ({start_row}, {start_col})")

    visited = find_visited_cells(map, start_row, start_col)
    # log(visited)

    result = len(visited)

    return result


def creates_loop(map, obstacle, start):
    row = start[0]
    col = start[1]
    map[obstacle[0]][obstacle[1]] = "#"

    # up, right, down, left
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    cur_dir = 0

    loc_to_dir = {(row, col): {cur_dir}}

    found_loop = False

    count = 0

    while 0 <= row < len(map) and 0 <= col < len(map[0]):
        # if obstacle == (77, 9):
        #     log(f"cur pos: ({row}, {col}), num_loc: {len(loc_to_dir)}")
            # log(f"cur pos: ({row}, {col}), num_loc: {len(loc_to_dir)}, loc: {loc_to_dir}")
        count += 1
        if map[row][col] == "#":
            row = row - dirs[cur_dir][0]
            col = col - dirs[cur_dir][1]
            cur_dir = (cur_dir + 1) % len(dirs)
            # if obstacle == (77, 9):
            #     log(f"Turing: cur pos: ({row}, {col}), dir: {cur_dir}, num_loc: {len(loc_to_dir)}")
                # log(f"Turing: cur pos: ({row}, {col}), dir: {cur_dir}, num_loc: {len(loc_to_dir)}, loc: {loc_to_dir}")
            prev_dirs = loc_to_dir.get((row, col), set())
            if cur_dir in prev_dirs:
                # if obstacle == (77, 9):
                #     log(f"Found a loop: obstacle: {obstacle}, cur pos: ({row}, {col}), dir: {prev_dirs}, num_loc: {len(loc_to_dir)}, loc: {loc_to_dir}")
                    # log(f"Found a loop: obstacle: {obstacle}, cur pos: ({row}, {col}), dir: {prev_dirs}, num_loc: {len(loc_to_dir)}")
                found_loop = True
                break

            loc_to_dir[(row, col)] = loc_to_dir.get((row, col), set())
            loc_to_dir[(row, col)].add(cur_dir)
        else:
            row = row + dirs[cur_dir][0]
            col = col + dirs[cur_dir][1]

    map[obstacle[0]][obstacle[1]] = "."
    return found_loop


def solve_part2(lines):
    start_row = 0
    start_col = 0

    map = list()
    for row in range(len(lines)):
        line = lines[row]
        map.append(list(line))
        if "^" in line:
            start_row = row
            start_col = line.index("^")
    # print_map(map)
    log(f"starting at ({start_row}, {start_col})")

    visited = find_visited_cells(map, start_row, start_col)
    visited.remove((start_row, start_col))

    obstacles = set()

    # visited = [(5, 6), (6, 3), (7, 6), (7, 7), (8, 1), (8, 3), (9, 7)]

    # visited = [(77, 9)]

    for row, col in visited:
        log(f"Checking ({row}, {col})")
        loop = creates_loop(map, (row, col), (start_row, start_col))
        if loop:
            obstacles.add((row, col))
            log(f"found a loop at ({row}, {col})")
        else:
            log(f"no loop at ({row}, {col})")

    result = len(obstacles)
    return result


if __name__ == '__main__':
    main()
