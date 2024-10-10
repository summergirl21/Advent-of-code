
"""
Part 1 Solution
Answer for Example input is 17

How can you tell if an area will be infinite?
No point exists with greater coordinate in at least one direction?

First find the points that don't have infinite fields.
Do this by finding the points with max and min values for each dimension, these will be on the edge of the field.
Then for the remaining points, calculate the field size and find the max.
To calculate the field size,
For each point near the start point, check if it has any closer points?
Is there a way to shorten the list of other points to check against, or sort it?

Or, for each point within the field, find the closes listed point, then find the max

Find the relevant area, min and max X and Y coordinates.
For each point in that field, find the closest point, or points.
If there are two or more closest points, it is not part of the field of any point
Otherwise, add one to the total field size for the relevant point

After this calculation is done, remove the points that would have an infinite field.

Then take the max of all the field sizes

Part 2
Go through all the points in the same, min, max area used in part 1
Is this the correct area or does the field need to be bigger?
Start with this and see if the answer is right.
For each location add up the distance to all the points.
Find number of points in with total distance within the set limit

"""


def main():
    max_dist_ex = 32
    max_dist = 10000
    process_file("ExampleInput6.txt", max_dist_ex)
    print("\n")
    process_file("PuzzleInput6.txt", max_dist)


def process_file(file_name, max_dist):
    with open(file_name) as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        print("Part 1")
        solve_part1(lines)

        print("\nPart 2")
        solve_part2(lines, max_dist)


def get_manhattan_distance(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def parse_point(line: str) -> tuple[int, int]:
    line = line.split(",")
    x = int(line[0])
    y = int(line[1])
    # print(f"parsing line {x}, {y}")
    return x, y


def find_non_infinite_points(min_x: int, min_y: int, max_x: int, max_y: int, id_to_point: dict[int, tuple[int, int]]) -> dict[int, tuple[int, int]]:
    min_x_points = dict(filter(lambda item: item[1][0] == min_x, id_to_point.items()))
    # print(f"all points with min x value: {min_x_points}")
    infinite_points = dict(min_x_points)

    min_y_points = set(filter(lambda item: item[1][1] == min_y, id_to_point.items()))
    # print(f"all points with min y value: {min_y_points}")
    infinite_points.update(min_y_points)

    max_x_points = set(filter(lambda item: item[1][0] == max_x, id_to_point.items()))
    # print(f"all points with max x value: {max_x_points}")
    infinite_points.update(max_x_points)

    max_y_points = set(filter(lambda item: item[1][1] == max_y, id_to_point.items()))
    # print(f"all points with max y value: {max_y_points}")
    infinite_points.update(max_y_points)

    # print(f"Found all points with infinite fields: {infinite_points}")

    points = dict(filter(lambda item: item[0] not in infinite_points.keys(), id_to_point.items()))
    # print(f"Found point WITHOUT infinite fields: {points}")
    return points


def find_min_max_area(points: set[tuple[int, int]]) -> tuple[int, int, int, int]:
    min_x = min(points, key=lambda x: x[0])[0]
    min_y = min(points, key=lambda y: y[1])[1]
    max_x = max(points, key=lambda x: x[0])[0]
    max_y = max(points, key=lambda y: y[1])[1]
    return min_x, min_y, max_x, max_y


def calculate_field_sizes(min_x, min_y, max_x, max_y, id_to_point):
    keys = list(i for i in range(len(id_to_point.keys())))
    values = list(0 for i in range(len(id_to_point.keys())))
    id_to_field_size = dict(zip(keys, values))

    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            # print(f"Evaluating field closest point for location ({x}, {y})")
            location = (x, y)
            id_to_dist = dict(zip(keys, values))
            for point_id in id_to_point.keys():
                point = id_to_point[point_id]
                distance = get_manhattan_distance(location, point)
                id_to_dist[point_id] = distance
                # print(f"Distance between location: {location}, and point: {point}, is {distance}")

            min_dist_id = min(id_to_dist, key=id_to_dist.get)
            min_dist = id_to_dist[min_dist_id]
            # print(f"Closest point to {location}, is {min_dist} units away has id {min_dist_id} and is {id_to_point[min_dist_id]}")
            min_dist_points = set(filter(lambda i: id_to_dist[i] == min_dist, id_to_dist.keys()))
            num_closest_points = len(min_dist_points)
            # print(f"Found {num_closest_points}, closest points, {min_dist_points}")

            if num_closest_points == 1:
                id_to_field_size[min_dist_id] += 1

    return id_to_field_size


def solve_part1(lines):
    points = set(map(lambda x: parse_point(x), lines))
    # print(f"All points: {points}")

    keys = list(i for i in range(len(points)))
    id_to_point = dict(zip(keys, points))

    min_x, min_y, max_x, max_y = find_min_max_area(points)
    print(f"Relevant area: min_x: {min_x}, min_y: {min_y}, max_x: {max_x}, max_y: {max_y} ")

    id_to_field_size = calculate_field_sizes(min_x, min_y, max_x, max_y, id_to_point)
    print(f"Calculated field sizes {id_to_field_size}")

    finite_points = find_non_infinite_points(min_x, min_y, max_x, max_y, id_to_point)
    print(f"Non infinite points: {finite_points}")

    result_id = max(finite_points.keys(), key=lambda x: id_to_field_size[x])
    print(f"Point with max field size: id: {result_id}, coordinates: {finite_points[result_id]}, field size: {id_to_field_size[result_id]}")


def calculated_total_distances(min_x, min_y, max_x, max_y, points) -> dict[tuple[int, int], int]:
    co_to_dist: dict[tuple[int, int], int] = dict()

    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            loc = (x, y)
            # print(f"Calculating total distance for {loc}")
            for p in points:
                dist = get_manhattan_distance(loc, p)
                co_to_dist[loc] = co_to_dist.get(loc, 0) + dist
            # print(f"Found total distance for location: {loc}, is {co_to_dist[loc]}")

    return co_to_dist


def solve_part2(lines, max_dist):
    points = set(map(lambda x: parse_point(x), lines))
    # print(f"All points: {points}")

    # keys = list(i for i in range(len(points)))
    # id_to_point = dict(zip(keys, points))

    min_x, min_y, max_x, max_y = find_min_max_area(points)
    print(f"Relevant area: min_x: {min_x}, min_y: {min_y}, max_x: {max_x}, max_y: {max_y} ")

    co_to_dist = calculated_total_distances(min_x, min_y, max_x, max_y, points)
    # print(f"Calculated total distances for all locations: {co_to_dist}")

    results = dict(filter(lambda item: item[1] < max_dist, co_to_dist.items()))

    print(f"Found {len(results)}, points with total distance less than {max_dist}")


if __name__ == '__main__':
    main()
