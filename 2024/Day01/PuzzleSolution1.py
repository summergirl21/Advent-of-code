
"""
Part 1 Solution
Sort the input lists, then iterate through and find the difference of each pair
"""
import time

DEBUG = True


def log(s):
    if DEBUG:
        print(s)


def main():
    print("Hello")
    process_file("ExampleInput1.txt")
    print()
    process_file("PuzzleInput1.txt")


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
    list1 = list()
    list2 = list()
    for line in lines:
        line = line.split()
        list1.append(int(line[0]))
        list2.append(int(line[1]))

    list1.sort()
    list2.sort()
    log(list1)
    log(list2)

    result = 0
    for i in range(len(list1)):
        result += abs(list1[i] - list2[i])

    return result


def solve_part2(lines):
    list1 = list()
    list2 = dict()
    for line in lines:
        line = line.split()
        list1.append(int(line[0]))
        int2 = int(line[1])
        list2[int2] = list2.get(int2, 0) + 1

    result = 0
    for n in list1:
        result += n * list2.get(n, 0)

    return result


if __name__ == '__main__':
    main()
