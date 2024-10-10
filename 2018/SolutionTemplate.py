
"""
Part 1 Solution
"""


def main():
    print("Hello")
    process_file("ExampleInput1.txt")
    process_file("PuzzleInput1.txt")


def process_file(file_name):
    with open(file_name) as file:
        solve_part1(file)


def solve_part1(file):
    for line in file:
        print(line)


if __name__ == '__main__':
    main()
