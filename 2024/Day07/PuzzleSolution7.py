
"""
Part 1 Solution
Brute force, try all possible combinations of operators. That seems like a lot of combos.
Start with plus for all the operators, if it's to high you know it can't be done.
Then add multiply, trying the different combos. Start with the first position, keep adding *
as long as total is too low, once it is to high, remove the last one and try the next spot?

Or could try the different number of multiply operations, starting with one, then two, etc

"""
import time
from itertools import product

DEBUG = False
PROCESS_FULL_INPUT = True
SOLVE_PART_2 = True


def log(s):
    if DEBUG:
        print(s)


def main():
    print("Hello")
    process_file("ExampleInput7.txt")

    if PROCESS_FULL_INPUT:
        print()
        process_file("PuzzleInput7.txt")


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


def find_operations(total, nums):
    log("")
    # operations = ["*" for _ in range(len(nums)-1)]
    # # log(f"total: {total}, nums: {nums}, operations: {operations}")
    # answer = evaluate_equation(nums, operations)
    # if answer < total:
    #     log(f"Max answer is less than total. total: {total}, answer: {answer}")
    #     return False
    # # log(f"total : {total}, answer: {answer}")
    # if total == answer:
    #     log(f"Found correct operations. total : {total}, nums: {nums}, operations: {operations}")
    #     return True

    for operations in product("*+", repeat=(len(nums)-1)):
        answer = evaluate_equation(nums, operations)
        log(f"total : {total}, answer: {answer}, nums: {nums}, operations: {operations}")
        if total == answer:
            log(f"Found correct operations. total : {total}, nums: {nums}, operations: {operations}")
            return True
    log(f"Did not find valid set of operations. total : {total}, nums: {nums}")
    return False


def evaluate_equation(nums, operations):
    equation = []
    for i in range(len(nums) + len(operations)):
        idx = i // 2
        if i%2 == 0:
            # add num
            equation.append(nums[idx])
        if i%2 == 1:
            # add operation
            equation.append(operations[idx])
    # log(f"nums: {nums}, operations: {operations}, equations: {equation}")
    answer = 0
    add = True
    for e in equation:
        if e == "+":
            add = True
        elif e == "*":
            add = False
        elif add:
            e = int(e)
            answer += e
        else:
            e = int(e)
            answer *= e
    return answer


def solve_part1(lines):
    entries = []
    for line in lines:
        log(line)
        line = line.split(":")
        total = int(line[0])
        nums = line[1].split()
        entries.append((total, nums))
    log(entries)

    result = 0
    for total, nums in entries:
        match = find_operations(total, nums)
        if match:
            result += total

    return result


def find_operations_part2(total, nums):
    log("")

    for operations in product("*+|", repeat=(len(nums)-1)):
        answer = evaluate_equation_part2(nums, operations)
        log(f"total : {total}, answer: {answer}, nums: {nums}, operations: {operations}")
        if total == answer:
            log(f"Found correct operations. total : {total}, nums: {nums}, operations: {operations}")
            return True
    log(f"Did not find valid set of operations. total : {total}, nums: {nums}")
    return False


def evaluate_equation_part2(nums, operations):
    equation = []
    for i in range(len(nums) + len(operations)):
        idx = i // 2
        if i%2 == 0:
            # add num
            equation.append(nums[idx])
        if i%2 == 1:
            # add operation
            equation.append(operations[idx])
    # log(f"nums: {nums}, operations: {operations}, equations: {equation}")
    answer = 0
    op = "+"
    for e in equation:
        if e == "+":
            op = "+"
        elif e == "*":
            op = "*"
        elif e == "|":
            op = "|"
        elif op == "+":
            e = int(e)
            answer += e
        elif op == "*":
            e = int(e)
            answer *= e
        else:
            left = str(answer)
            right = str(e)
            answer = int(left + right)
            log(f"concatenating: left: {left}, right: {right}, ans: {answer}")
    return answer


def solve_part2(lines):
    entries = []
    for line in lines:
        log(line)
        line = line.split(":")
        total = int(line[0])
        nums = line[1].split()
        entries.append((total, nums))
    log(entries)

    result = 0
    for total, nums in entries:
        match = find_operations_part2(total, nums)
        if match:
            result += total

    return result


if __name__ == '__main__':
    main()
