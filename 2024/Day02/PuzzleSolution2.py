
"""
Part 1 Solution
Loop through the lines and check each report
Check if the first two numbers are increasing or decreasing
For each case, check the remaining numbers are also increasing/decreasing and withing the limits

Part 2 Solution
naive solution seems to be try removing each level of an unsafe report and see if that makes it safe.
is there a smarter heuristic that can be used to limit to number of levels that need to be tried?
On the first unsafe level, try removing the previous and then current level, check if it is then safe
"""
import time

DEBUG = True


def log(s):
    if DEBUG:
        print(s)


def main():
    print("Hello")
    process_file("ExampleInput2.txt")
    print()
    process_file("PuzzleInput2.txt")


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


def is_safe(line: list[int]) -> bool:
    is_increasing = line[0] < line[1]

    prev = line[0]
    for i in range(1, len(line)):
        cur = line[i]
        if is_increasing:
            if cur <= prev or cur - prev > 3:
                return False
        else:
            if cur >= prev or prev - cur > 3:
                return False

        prev = cur

    return True


def solve_part1(lines):
    result = 0

    for line in lines:
        line = line.split()
        for i in range(len(line)):
            line[i] = int(line[i])

        # log(line)
        if is_safe(line):
            result += 1

    return result


def unsafe_at(line: list[int]) -> int:
    is_increasing = line[0] < line[1]

    prev = line[0]
    for i in range(1, len(line)):
        cur = line[i]
        if is_increasing:
            if cur <= prev or cur - prev > 3:
                return i
        else:
            if cur >= prev or prev - cur > 3:
                return i

        prev = cur

    return -1


def solve_part2(lines):
    result = 0

    for line in lines:
        line = line.split()
        for i in range(len(line)):
            line[i] = int(line[i])

        log(line)
        # violation_idx = unsafe_at(line)
        # log(f"violation at: {violation_idx}")
        # if violation_idx == -1:
        #     result += 1
        # else:
        #     new_line = line[:violation_idx-1] + line[violation_idx:]
        #     log(f"removing level at {violation_idx-1}, new line: {new_line}")
        #     if unsafe_at(new_line) == -1:
        #         log(f"line is safe, {new_line}")
        #         result += 1
        #     else:
        #         new_line = line[:violation_idx] + line[violation_idx+1:]
        #         log(f"removing level at {violation_idx}, new line: {new_line}")
        #         if unsafe_at(new_line) == -1:
        #             log(f"line is safe, {new_line}")
        #             result += 1
        #         else:
        #             log(f"line is not safe: {line}")

        if is_safe(line):
            result += 1
        else:
            for i in range(len(line)):
                new_line = line[:i] + line[i+1:]
                if is_safe(new_line):
                    log(f"found safe option, removed level at {i}, new line: {new_line}")
                    result += 1
                    break

    return result


if __name__ == '__main__':
    main()
