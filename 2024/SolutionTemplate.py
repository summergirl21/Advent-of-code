
"""
Part 1 Solution
"""
import time

DEBUG = True
PROCESS_FULL_INPUT = False
SOLVE_PART_2 = False


def log(s):
    if DEBUG:
        print(s)


def main():
    print("Hello")
    process_file("ExampleInput1.txt")

    if PROCESS_FULL_INPUT:
        print()
        process_file("PuzzleInput1.txt")


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


def solve_part1(lines):
    for line in lines:
        log(line)

    result = 0

    return result


def solve_part2(lines):
    for line in lines:
        log(line)

    result = 0

    return result


if __name__ == '__main__':
    main()
