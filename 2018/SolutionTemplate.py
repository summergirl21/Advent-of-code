
"""
Part 1 Solution
"""

DEBUG = True


def log(s):
    if DEBUG:
        print(s)


def main():
    print("Hello")
    process_file("ExampleInput1.txt")
    # print()
    # process_file("PuzzleInput1.txt")


def process_file(file_name):
    with open(file_name) as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        print("Part 1")
        solve_part1(lines)

        # print("\nPart 2")
        # solve_part2(lines)


def solve_part1(lines):
    for line in lines:
        log(line)


def solve_part2(lines):
    for line in lines:
        log(line)


if __name__ == '__main__':
    main()
