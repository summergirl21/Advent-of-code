
"""
Part 1 Solution
Parse valid multiply operations
an operation is valid if is in the form mul(123,456) where each of the numbers can be between 1-3 digits
Use regex to match this pattern
mul\(\d{1,3},\d{1,3}\)
(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))
"""
import time
import re

DEBUG = False


def log(s):
    if DEBUG:
        print(s)


def main():
    print("Hello")
    process_file("ExampleInput3.txt")
    print()
    process_file("PuzzleInput3.txt")


def process_file(file_name):
    with open(file_name) as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        print("Part 1")
        start = time.time()
        result1 = solve_part1(lines)
        end = time.time()
        print(f"Part 1 result: {result1}")
        print(f"Elapsed time {end - start}")

        print("\nPart 2")
        start = time.time()
        result2 = solve_part2(lines)
        end = time.time()
        print(f"Part 2 result: {result2}")
        print(f"Elapsed time {end - start}")


def solve_part1(lines):
    matches = []
    for line in lines:
        log(line)
        matches.extend(re.findall("mul\(\d{1,3},\d{1,3}\)", line))

    log(matches)

    result = 0
    for m in matches:
        m = m.removeprefix("mul(").strip(")").split(",")
        x = int(m[0])
        y = int(m[1])
        log(f"x: {x}, y: {y}")
        result += x*y
    return result


def solve_part2(lines):
    matches = []
    for line in lines:
        log(line)
        matches.extend(re.findall("(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))", line))

    log(matches)

    result = 0
    enabled = True
    for m in matches:
        if m[0] and enabled:
            m = m[0]
            log(f"match is mul: {m}, is enabled: {enabled}")
            m = m.removeprefix("mul(").strip(")").split(",")
            x = int(m[0])
            y = int(m[1])
            log(f"x: {x}, y: {y}")
            result += x * y
        elif m[0] and not enabled:
            log(f"match is mul: {m}, is disabled: {enabled}")
        elif m[1]:
            log(f"match is do: {m}")
            enabled = True
        elif m[2]:
            log(f"match is don't: {m}")
            enabled = False
    return result


if __name__ == '__main__':
    main()
