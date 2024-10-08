
"""
Part 1 Solution
Create data structure for each gard, storing the total minutes asleep and
an array counting the number of times the guard was asleep for each minute.
Process the input one shift at a time, updated the data for that guard
After all the input is processed, go through and find the guard with the most sleep
and the minute that guard was asleep the most.
Start by sorting the input to make processing easier.

Part 2 Solution
"""
from dataclasses import dataclass


@dataclass
class Guard:
    id: int
    time_asleep: int
    sleep_counts: list[int]


def main():
    print("Hello")
    process_file("ExampleInput4.txt")
    print("\nPuzzle input")
    process_file("PuzzleInput4.txt")


def process_file(file_name):
    with open(file_name) as file:
        solve_part1(file)


def solve_part1(file):
    lines = list(map(lambda x: x.lower().strip(), file.readlines()))
    lines.sort()
    # print(lines)

    guard_info = dict()
    last_sleep = -1
    guard = None
    for line in lines:
        line = line.split()
        # print(line)
        if line[2] == "guard":
            cur_guard = int(line[3].strip("#"))
            guard_info.setdefault(cur_guard, Guard(cur_guard, 0, [0 for i in range(59)]))
            guard = guard_info[cur_guard]
            # print(f"Current guard {cur_guard}")
        elif line[2] == "falls":
            last_sleep = get_minute(line)
            # print(f"Guard falls asleep at {last_sleep}")
        elif line[2] == "wakes":
            wake_min = get_minute(line)
            time_asleep = wake_min-last_sleep
            guard.time_asleep += time_asleep
            for i in range(last_sleep, wake_min):
                guard.sleep_counts[i] += 1
            # print(f"Guard wakes up at {wake_min}, sleep time was {time_asleep} minutes")
            # print(f"Guard id {guard.id}, total sleep {guard.time_asleep}\n sleep totals: {guard.sleep_counts}")
        else:
            print("unexpected line")

    # print(guard_info)

    max_sleep = 0
    guard_id = -1
    guard_chosen = None
    for guard in guard_info.values():
        if guard.time_asleep > max_sleep:
            max_sleep = guard.time_asleep
            guard_id = guard.id
            guard_chosen = guard

    max_val = -1
    max_min = -1
    for i in range(0, 59):
        if guard_chosen.sleep_counts[i] > max_val:
            max_val = guard_chosen.sleep_counts[i]
            max_min = i

    print(f"part 1: choosing guard {guard_id}, and min {max_min}, result {guard_id*max_min}")

    # Part 2 solution
    max_val = -1
    max_min = -1
    guard_id = -1
    for guard in guard_info.values():
        for i in range (0, 59):
            if guard.sleep_counts[i] > max_val:
                max_val = guard.sleep_counts[i]
                max_min = i
                guard_id = guard.id

    print(f"part 2: choosing guard {guard_id}, and min {max_min}, result {guard_id*max_min}")


def get_minute(line):
    return int(line[1].split(":")[1].strip("]"))


if __name__ == '__main__':
    main()
