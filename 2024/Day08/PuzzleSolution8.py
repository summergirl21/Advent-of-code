
"""
Part 1 Solution
Need to count the number of antinodes.
Each pair of antennas that are the same frequency have the possibility of producing two antinodes.
So want to process each pair of antennas that are the same frequency.
Thinking of storing the list of coordinates of antennas of each frequency.
Then can loop through the options to process each pair.
"""
import time

DEBUG = True
PROCESS_FULL_INPUT = True
SOLVE_PART_2 = True


def log(s):
    if DEBUG:
        print(s)


def main():
    print("Hello")
    process_file("ExampleInput8.txt")

    if PROCESS_FULL_INPUT:
        print()
        process_file("PuzzleInput8.txt")


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


def find_antinodes(antenna1, antenna2, len_row, len_col):
    # calculate the two locations equal distant on the line formed by the two antenna
    nodes = set()
    row1 = antenna1[0]
    row2 = antenna2[0]
    node1_row = row1 - (row2 - row1)
    node2_row = row2 + (row2 - row1)

    col1 = antenna1[1]
    col2 = antenna2[1]
    node1_col = col1 - (col2 - col1)
    node2_col = col2 + (col2 - col1)

    if 0 <= node1_row < len_row and 0 <= node1_col < len_col:
        nodes.add((node1_row, node1_col))

    if 0 <= node2_row < len_row and 0 <= node2_col < len_col:
        nodes.add((node2_row, node2_col))

    return nodes


def solve_part1(lines):
    # process the input to create dictionary of the frequency, to list of coordinates contain the antenna
    # also need to know the size of the grid.
    # another option would be to read the input into matrix
    antenna: dict[int, list[tuple[int, int]]] = dict()

    row = 0
    col = 0
    for line in lines:
        col = 0
        for c in line:
            if c != ".":
                coordinates = antenna.get(c, list())
                coordinates.append((row, col))
                antenna[c] = coordinates
            col += 1
        row += 1
    log(antenna)
    len_row = row
    len_col = col
    log(f"len_row: {len_row}, len_col: {len_col}")

    # process each pair of antenna of the same frequency
    # create set of the resulting antinodes
    antinodes: set[tuple[int, int]] = set()
    for freq in antenna:
        log(f"Frequency: {freq}")
        coordinates = antenna[freq]
        for i in range(len(coordinates)):
            antenna1 = coordinates[i]
            for j in range(i+1, len(coordinates)):
                antenna2 = coordinates[j]
                log(f"Antenna 1: {antenna1}, 2: {antenna2}")
                new_antinodes = find_antinodes(antenna1, antenna2, len_row, len_col)
                log(f"Found antinodes: {new_antinodes}")
                antinodes = antinodes | new_antinodes

    log(f"All antinodes: {antinodes}")
    result = len(antinodes)

    return result

def find_antinodes2(antenna1, antenna2, len_row, len_col):
    # calculate the two locations equal distant on the line formed by the two antenna
    nodes = set()
    nodes.add(antenna1)
    nodes.add(antenna2)

    row1 = antenna1[0]
    row2 = antenna2[0]
    col1 = antenna1[1]
    col2 = antenna2[1]

    node1_row = row1 - (row2 - row1)
    node1_col = col1 - (col2 - col1)
    while 0 <= node1_row < len_row and 0 <= node1_col < len_col:
        nodes.add((node1_row, node1_col))
        node1_row = node1_row - (row2 - row1)
        node1_col = node1_col - (col2 - col1)

    node2_row = row2 + (row2 - row1)
    node2_col = col2 + (col2 - col1)
    while 0 <= node2_row < len_row and 0 <= node2_col < len_col:
        nodes.add((node2_row, node2_col))
        node2_row = node2_row + (row2 - row1)
        node2_col = node2_col + (col2 - col1)

    return nodes

def solve_part2(lines):
    antenna: dict[int, list[tuple[int, int]]] = dict()

    row = 0
    col = 0
    for line in lines:
        col = 0
        for c in line:
            if c != ".":
                coordinates = antenna.get(c, list())
                coordinates.append((row, col))
                antenna[c] = coordinates
            col += 1
        row += 1
    log(antenna)
    len_row = row
    len_col = col
    log(f"len_row: {len_row}, len_col: {len_col}")

    # process each pair of antenna of the same frequency
    # create set of the resulting antinodes
    antinodes: set[tuple[int, int]] = set()
    for freq in antenna:
        log(f"Frequency: {freq}")
        coordinates = antenna[freq]
        for i in range(len(coordinates)):
            antenna1 = coordinates[i]
            for j in range(i + 1, len(coordinates)):
                antenna2 = coordinates[j]
                log(f"Antenna 1: {antenna1}, 2: {antenna2}")
                new_antinodes = find_antinodes2(antenna1, antenna2, len_row, len_col)
                log(f"Found antinodes: {new_antinodes}")
                antinodes = antinodes | new_antinodes

    log(f"All antinodes: {antinodes}")
    result = len(antinodes)

    return result


if __name__ == '__main__':
    main()
