
"""
Part 1 Solution
Seems like you need to check the solution visually to see when it aligns?
Make a program where I can give input to iterate through a second and update the output to see when
the stars align

"""
import time
from dataclasses import dataclass

DEBUG = False


def log(s):
    if DEBUG:
        print(s)


def main():
    print("Hello")
    process_file("ExampleInput10.txt", 5)
    print()
    process_file("PuzzleInput10.txt", 100000)


def process_file(file_name, max_sec):
    with open(file_name) as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        print("Part 1")
        start = time.time()
        solve_part1(lines, max_sec)
        end = time.time()
        print(f"Elapsed time {end - start}")


@dataclass
class Point:
    pos_x: int
    pos_y: int
    vel_x: int
    vel_y: int


def parse_point(line: str) -> Point:
    line = line.split("position=")[1]
    line = line.split("velocity=")
    pos = line[0]
    vel = line[1]
    # log(f"pos: {pos}, vel: {vel}")
    pos = pos.split(",")
    pos_x = int(pos[0].strip().strip("<"))
    pos_y = int(pos[1].strip().strip(">"))
    # log(f"pos_x: {pos_x}, pos_y: {pos_y}")

    vel = vel.split(",")
    vel_x = int(vel[0].strip().strip("<"))
    vel_y = int(vel[1].strip().strip(">"))
    # log(f"vel_x: {vel_x}, vel_y: {vel_y}")
    log(f"Point: pos_x: {pos_x}, pos_y: {pos_y}, vel_x: {vel_x}, vel_y: {vel_y}")
    point = Point(pos_x, pos_y, vel_x, vel_y)
    return point


def display(points: list[Point], sec: int):
    min_x = min(points, key=lambda p: p.pos_x).pos_x
    max_x = max(points, key=lambda p: p.pos_x).pos_x
    min_y = min(points, key=lambda p: p.pos_y).pos_y
    max_y = max(points, key=lambda p: p.pos_y).pos_y
    log(f"min_x: {min_x}, max_x: {max_x}, min_y: {min_y}, max_y: {max_y}")

    print(f"\nSecond: {sec}")
    screen = [[0 for i in range(max_x - min_x + 1)] for j in range(max_y - min_y + 1)]

    for p in points:
        x = p.pos_x - min_x
        y = p.pos_y - min_y
        screen[y][x] = 1

    for row in screen:
        line = ""
        for value in row:
            if value == 0:
                line += "."
            else:
                line += "#"
        print(line)
    print()


def advance(points: list[Point]) -> list[Point]:
    for p in points:
        p.pos_x += p.vel_x
        p.pos_y += p.vel_y
    return points


def solve_part1(lines, max_sec):

    points: list[Point] = []
    for line in lines:
        log(line)
        points.append(parse_point(line))

    log(f"num points: {len(points)}")

    for sec in range(max_sec):
        min_x = min(points, key=lambda p: p.pos_x).pos_x
        max_x = max(points, key=lambda p: p.pos_x).pos_x
        min_y = min(points, key=lambda p: p.pos_y).pos_y
        max_y = max(points, key=lambda p: p.pos_y).pos_y
        log(f"min_x: {min_x}, max_x: {max_x}, min_y: {min_y}, max_y: {max_y}")

        if (max_x - min_x) < 200 and (max_y - min_y) < 200:
            display(points, sec)
        points = advance(points)


def solve_part2(lines):
    for line in lines:
        log(line)


if __name__ == '__main__':
    main()
