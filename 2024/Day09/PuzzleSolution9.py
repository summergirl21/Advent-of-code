
"""
Part 1 Solution
Thinking of representing the disk as a list like in the example.
1. read the input, creating a list containing the map for the files system
2. loop through the mpa, tracking the next free block as well as the last filled block in the file
move the last block to the first free spot, update the markers and continue till the first free block is
at the end of the map
3. calculate the check sum based on this map


Part 2 Solution
modified the loop to scan the file map for a free space for each file.
to make this more efficient, could make a dict storing the free spaces by length, so that it is faster to find a space for each file.
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
    process_file("ExampleInput9.txt")

    if PROCESS_FULL_INPUT:
        print()
        process_file("PuzzleInput9.txt")


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


def solve_part1(lines):
    file_map = list()
    for line in lines:
        # log(line)
        file_map = parse_input(line)

        # log(file_map)
        # log("".join(file_map))

    compact_files(file_map)

    # log(file_map)
    # log("".join(file_map))

    result = calculate_checksum(file_map)

    return result


def calculate_checksum(file_map):
    check_sum = 0
    for i in range(len(file_map)):
        if file_map[i] == ".":
            return check_sum

        check_sum += i * int(file_map[i])
    return check_sum


def compact_files(file_map):
    next_free_space = 0
    last_file_block = len(file_map) - 1

    while file_map[next_free_space] != ".":
        next_free_space += 1
    while file_map[last_file_block] == ".":
        last_file_block -= 1

    while next_free_space < last_file_block:
        # log(f"next_free_space: {next_free_space}, last_file_block: {last_file_block}")
        file_map[next_free_space] = file_map[last_file_block]
        file_map[last_file_block] = "."

        while file_map[next_free_space] != ".":
            next_free_space += 1
        while file_map[last_file_block] == ".":
            last_file_block -= 1

        # log("".join(file_map))


def parse_input(line):
    file_map = list()
    file_id = 0
    for i in range(len(line)):
        # even index is a file, odd is a free block
        is_file = i % 2 == 0
        length = int(line[i])
        for _ in range(length):
            if is_file:
                file_map.append(str(file_id))
            else:
                file_map.append(".")
        if is_file:
            file_id += 1
    return file_map


def solve_part2(lines):
    file_map = list()
    for line in lines:
        # log(line)
        file_map = parse_input(line)

        # log(file_map)
        # log("".join(file_map))

    compact_files2(file_map)

    # log(file_map)
    # log("".join(file_map))

    result = calculate_checksum2(file_map)

    return result


def compact_files2(file_map):
    log(f"len file_map: {len(file_map)}")
    file_search_start = len(file_map) - 1
    free_space_search_start = 0
    file_id = float('inf')
    while file_search_start > 0:
        log(f"starting file search at: {file_search_start}")
        # find file to move
        last_file_start, last_file_end, file_len, file_id = find_next_file(file_map, file_search_start, file_id)
        log(f"last_file_end: {last_file_end}, last_file_start: {last_file_start}, file_len: {file_len}, file_id: {file_id}")
        file_search_start = last_file_start - 1

        # find free space to move it to
        free_space_start, free_space_end, free_space_len = find_next_free_space(file_map, free_space_search_start)
        free_space_search_start = free_space_start
        while free_space_len < file_len and free_space_end < last_file_start:
            free_space_start, free_space_end, free_space_len = find_next_free_space(file_map, free_space_end+1)

        log(f"Found free space. free_space_start: {free_space_start}, free_space_end: {free_space_end}, free_space_len: {free_space_len}")

        # move the file
        if free_space_len >= file_len and free_space_end < last_file_start:
            for i in range(file_len):
                file_map[free_space_start + i] = file_map[last_file_start + i]
                file_map[last_file_start + i] = "."
            log(f"Moved file: {file_map}")
        else:
            log(f"Did not move file: {file_map}")


def find_next_file(file_map, file_search_start, prev_file_id):
    last_file_end = file_search_start
    while file_map[last_file_end] == ".":
        last_file_end -= 1
    last_file_start = last_file_end
    while last_file_start > 0 and file_map[last_file_start - 1] == file_map[last_file_end]:
        last_file_start -= 1
    log(file_map)
    file_len = last_file_end - last_file_start + 1
    file_id = int(file_map[last_file_end])

    if file_id >= prev_file_id:
        log(f"already processed this file, skipping it: {file_id}")
        last_file_start, last_file_end, file_len, file_id = find_next_file(file_map, last_file_start-1, prev_file_id)

    return last_file_start, last_file_end, file_len, file_id


def find_next_free_space(file_map, search_start):
    free_space_start = search_start
    while file_map[free_space_start] != ".":
        free_space_start += 1
    free_space_end = free_space_start
    while free_space_end < len(file_map)-1 and file_map[free_space_end + 1] == ".":
        free_space_end += 1
    free_space_len = free_space_end - free_space_start + 1
    log(f"free_space_start: {free_space_start}, free_space_end: {free_space_end}, free_space_len: {free_space_len}")
    return free_space_start, free_space_end, free_space_len


def calculate_checksum2(file_map):
    check_sum = 0
    for i in range(len(file_map)):
        if file_map[i] != ".":
            check_sum += i * int(file_map[i])
    return check_sum


if __name__ == '__main__':
    main()
