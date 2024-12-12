
"""
Part 1 Solution
Initial thought is to create a list for the stones. inserting into the list is slow, maybe use a queue instead.
Popping to process each stone and then can add any number of stones back to queue efficiently.
Using a queue makes it similar to BFS

Part2 Solution
Use a hash table to store intermediate results.
For each stone, if it is not in the hash table, calculate 5 iterations on it, store result in hash table
and also add it back to the final result list.
Can store count of each stone in the list, instead of full list
"""
import math
import time
from collections import deque

DEBUG = False
PROCESS_FULL_INPUT = True
SOLVE_PART_2 = True


def log(s):
    if DEBUG:
        print(s)


def main():
    print("Hello")
    process_file("ExampleInput11.txt")

    if PROCESS_FULL_INPUT:
        print()
        process_file("PuzzleInput11.txt")


def process_file(file_name):
    with open(file_name) as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        print(f"Part 1: {file_name}")
        start = time.time()
        result1 = solve_part1(lines)
        end = time.time()
        print(f"Part 1 result: {result1}")
        print(f"Elapsed time {end - start}")

        if SOLVE_PART_2:
            print(f"\nPart 2: {file_name}")
            start = time.time()
            result2 = solve_part2(lines)
            end = time.time()
            print(f"Part 2 result: {result2}")
            print(f"Elapsed time {end - start}")


def solve_part1(lines):
    result = 0
    iterations = 25
    for line in lines:
        log(line)
        stones = [int(x) for x in line.split()]
        # print(f"Starting, iterations: {iterations}, stones: {stones}")

        queue = deque(stones)
        i = 0
        while i < iterations:
            i += 1
            level_size = len(queue)
            # log(f"iteration: {i}, size: {level_size}, queue: {queue}")
            # print(f"iteration: {i}, size: {level_size}")
            for _ in range(level_size):
                cur = queue.popleft()
                if cur == 0:
                    # log(f"cur: {cur}, adding: {1}")
                    queue.append(1)
                else:
                    stone_len = int(math.log10(cur))+1
                    if stone_len % 2 == 0:
                        factors = (10 ** (stone_len // 2))
                        left_stone = cur // factors
                        right_stone = cur % factors
                        # log(f"cur: {cur}, adding: {int(left_stone)}, and {right_stone}")
                        queue.append(left_stone)
                        queue.append(right_stone)
                    else:
                        # log(f"cur: {cur}, adding: {cur*2024}")
                        queue.append(cur*2024)

        # log(f"final queue: {queue}")
        num_stones = len(queue)
        # print(f"Final num stones after {iterations} iterations: {num_stones}")
        result = num_stones

    return result


def solve_part2(lines):
    result = 0
    iterations = 75
    for line in lines:
        log(line)
        stones = [int(x) for x in line.split()]
        log(f"Starting, iterations: {iterations}, stones: {stones}")

        stone_counts: dict[int, int] = dict()
        for stone in stones:
            stone_counts[stone] = 1

        res = calc_stones(stone_counts, iterations)
        final_num_stones = sum(res.values())
        # log(cache)

        log(f"Final num stones after {iterations} iterations: {final_num_stones}")
        result = final_num_stones

    return result


def calc_stones(stone_counts, iterations):
    log(f"calc_stones: iter target: {iterations}")

    for i in range(iterations):
        next_stones = dict()
        log(f"calc_stones: iter target: {iterations}, cur iter: {i}, size: {len(stone_counts)}")
        for stone, count in stone_counts.items():
            res = get_next_stone(stone)
            for child in res:
                next_stones[child] = next_stones.get(child, 0) + count
        stone_counts = next_stones
    return stone_counts


def calc_stones_old(stone_counts, iterations, step_size, cache):
    if step_size > 5:
        log(f"calc_stones: iter target: {iterations}, step: {step_size}")
    next_stones = dict()

    i = 0
    while i < iterations:
        i += step_size
        # log(f"iteration: {i}, size: {level_size}, queue: {queue}")
        if step_size > 5:
            log(f"calc_stones: iter target: {iterations}, step: {step_size}, cur iter: {i}, size: {len(stone_counts)}")
        for cur, count in stone_counts.items():
            if (cur, step_size) in cache:
                # if step_size > 5:
                #     log(f"Using cache: {(cur, step_size)}")
                res = cache[(cur, step_size)]
                for child in res:
                    next_stones[child] = next_stones.get(child, 0) + count
            elif step_size == 1:
                res = get_next_stone(cur)
                # cache[(cur, 1)] = next_stones
                for child in res:
                    next_stones[child] = next_stones.get(child, 0) + count
            else:
                if step_size == 75:
                    next_size = 25
                elif step_size == 25:
                    next_size = 5
                else:
                    next_size = 1
                res = calc_stones_old({cur: count}, step_size, next_size, cache)
                cache[(cur, step_size)] = res
                for child in res:
                    next_stones[child] = next_stones.get(child, 0) + count

    return next_stones


def get_next_stone(stone):
    next_stones = list()
    if stone == 0:
        # log(f"cur: {stone}, adding: {1}")
        next_stones.append(1)
    else:
        stone_len = int(math.log10(stone)) + 1
        if stone_len % 2 == 0:
            factors = (10 ** (stone_len // 2))
            left_stone = stone // factors
            right_stone = stone % factors
            # log(f"cur: {stone}, adding: {int(left_stone)}, and {right_stone}")
            next_stones.append(left_stone)
            next_stones.append(right_stone)
        else:
            # log(f"cur: {stone}, adding: {stone * 2024}")
            next_stones.append(stone * 2024)
    return next_stones


if __name__ == '__main__':
    main()
