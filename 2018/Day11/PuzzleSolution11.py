
"""
Part 1 Solution
"""
import time

DEBUG = True


def log(s):
    if DEBUG:
        print(s)


def main():
    print("Hello")
    process_file("ExampleInput11.txt")
    print()
    process_file("PuzzleInput11.txt")


def process_file(file_name):
    with open(file_name) as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        print("Part 1")
        start = time.time()
        solve_part1(lines)
        end = time.time()
        print(f"Elapsed time {end - start}")

        print("\nPart 2")
        start = time.time()
        solve_part2(lines)
        end = time.time()
        print(f"Elapsed time {end - start}")


def find_power_level(x: int, y: int, gsn: int) -> int:
    rack_id = x + 10
    power = rack_id * y
    power += gsn
    power = power * rack_id
    # log(f"power: {power}")

    power = power % 1000
    power = power // 100
    # log(f"power: {power}")
    power -= 5

    # log(f"Found power level for ({x}, {y}), serial: {gsn}, power: {power}")
    return power


def find_grid(gsn: int) -> list[list[int]]:
    grid_size = 300
    grid = [[0 for x in range(grid_size+1)] for y in range(grid_size+1)]

    for y in range(1, grid_size+1):
        for x in range(1, grid_size+1):
            grid[y][x] = find_power_level(x, y, gsn)

    return grid


def find_highest_power(grid: list[list[int]], size: int) -> tuple[tuple[int, int], int]:
    grid_size = len(grid)
    assert grid_size == len(grid[0])

    # powers = [[0 for x in range(grid_size)] for y in range(grid_size)]
    max_point = (0, 0)
    max_power = -100

    for y in range(1, grid_size-size):
        for x in range(1, grid_size-size):
            sum = 0
            for j in range(y, y+size):
                for i in range(x, x+size):
                    sum += grid[j][i]
            # powers[y][x] = sum
            if sum > max_power:
                max_power = sum
                max_point = (x, y)

    return max_point, max_power


def find_highest_power_fast(grid: list[list[int]], size: int) -> tuple[tuple[int, int], int]:
    # log("Fast")
    grid_size = len(grid)
    assert grid_size == len(grid[0])

    max_point = (0, 0)
    max_power = -1000

    for x in range(1, grid_size - size):
        row_sums = [0 for z in range(grid_size+1)]
        for y in range(1, grid_size-size):
            power_sum = 0
            for row in range(y, y+size):
                if row_sums[row] == 0:
                    for col in range(x, x+size):
                        row_sums[row] += grid[row][col]
                power_sum += row_sums[row]

            if power_sum > max_power:
                max_power = power_sum
                max_point = (x, y)

    return max_point, max_power


def solve_part1(lines):
    for line in lines:
        gsn = int(line)
        grid = find_grid(gsn)
        # log(grid)
        (x, y), max_power = find_highest_power_fast(grid, 3)
        print(f"DONE: {gsn}, found point ({x}, {y}) with power {max_power}")

    # power = find_power_level(3, 5, 8)
    # power = find_power_level(122, 79, 57)
    # power = find_power_level(217, 196, 39)
    # power = find_power_level(101, 153, 71)


def solve_part2(lines):
    for line in lines:
        gsn = int(line)
        grid = find_grid(gsn)
        log("GRID:")
        log(grid)

        max_point = (0, 0)
        max_power = -100
        max_size = 0

        for size in range(1, 301):
            point, power = find_highest_power_fast(grid, size)
            log(f"Evaluated: size: {size}, GSN: {gsn}, power: {power}, point: {point}")
            if power > max_power:
                max_power = power
                max_point = point
                max_size = size

        print(f"DONE: {gsn}, found point {max_point} with power {max_power}, {max_size}")
        print(f"Result: {max_point[0]},{max_point[1]},{max_size}")


if __name__ == '__main__':
    main()
