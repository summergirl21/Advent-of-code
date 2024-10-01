def main():
    with open("PuzzleInput5.txt") as file:
        seed_map = file.readline()
        print(seed_map)
        _, seed_num_str = seed_map.split(":")
        start_seeds = seed_num_str.split()
        print(start_seeds)

        map_order = {}
        map_data = {}

        map_buffer = []
        print(f"len: {len(map_buffer)}")
        for line in file:
            print(line, end="")
            print(f"find: {line.find('map:')}")
            if len(map_buffer) ==0 and line.find("map:") > -1:
                map_buffer.append(line)
                print("starting new map buffer")
            elif line[0].isdigit():
                map_buffer.append(line)
                print("appending to map buffer")
            elif line.find("map:") > -1:
                print("end of current map")
                print(f"map_buffer:  {map_buffer}")

                src_name, dest_name, data = parse_map_data(map_buffer)
                map_data[src_name] = data
                map_order[src_name] = dest_name
                map_buffer = [line]

            print("")

        src_name, dest_name, data = parse_map_data(map_buffer)
        map_data[src_name] = data
        map_order[src_name] = dest_name

        print(map_data)
        print(map_order)

        for seed in start_seeds:
            loc = find_location(seed, map_order, map_data)

def find_location(seeds, map_order, map_data):

    for point in seeds:

        src_name = "seed"
        des_name = map_order[src_name]

        while(des_name != "location"):
            src_name, des_name, point = find_next_step(src_name, des_name, point, map_order, map_data)

def find_next_step(src_name, des_name, point, map_order, map_data):
    new_des_name = map_order[des_name]
    new_src_name = des_name
    this_map = map_data[src_name]
    new_point = find_next_point(point, this_map)

def find_next_point(point, map):
    print(f"finding next step for point: {point}, map: {map}")

    src_rang_starts = list(map.keys())
    src_rang_starts.sort()
    print(f"start ranges: {src_rang_starts}")

    rang_start = 0


def parse_map_data(map_buffer):
    print(f"paring map data: {map_buffer}")
    map_title = map_buffer[0]
    map_name, _ = map_title.split()
    src, dest = map_name.split("-to-")
    print(f"map_name: {src}, {dest}")

    map_data = {}
    for data in map_buffer[1:]:
        dest_start, src_start, length = data.split()
        dest_start = int(dest_start)
        src_start = int(src_start)
        length = int(length)
        print(f"data: {dest_start}, {src_start}, {length}")
        map_data[src_start] = (dest_start, length)
    print(f"map_data: {map_data}")
    return src, dest, map_data


if __name__ == "__main__":
    main()
