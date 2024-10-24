
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
    # process_file("ExampleInput12.txt")
    print()
    process_file("PuzzleInput12.txt")


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


def parse_state(init: str) -> tuple[list[str], int]:
    log("Parsing initial state")
    start_idx = 0 # index of pot 0, might be greater than 0 if there are negative pots
    state: list[str] = list()
    for c in init:
        state.append(c)

    return state, start_idx


def parse_rules(lines: list[str]) -> dict[str, str]:
    log("Paring rules")
    rules: dict[str, str] = dict()
    for line in lines:
        line = line.split(" => ")
        rules[line[0]] = line[1]
    return rules


def iterate_gen(state: list[str], idx: int, rules: dict[str, str]) -> tuple[list[str], int]:
    next_state = list()
    first_pot = False
    for i in range(-2, len(state) + 2):
        # calculate the string to match on for this pot
        seq = ""
        seq += get_pot_at(i-2, state)
        seq += get_pot_at(i-1, state)
        seq += get_pot_at(i, state)
        seq += get_pot_at(i+1, state)
        seq += get_pot_at(i+2, state)

        if not first_pot and "#" in seq:
            first_pot = True

        if seq in rules.keys():
            next_pot = rules[seq]
        else:
            next_pot = "."

        # if i >= len(state):
        #     log(f"SEQ: {seq}, index: {i}, next pot: {next_pot}")

        if i < 0:
            if next_pot == "#":
                next_state.append(next_pot)
                idx += 1
                # log(f"Adding pot at start, i: {i}, idx: {idx}")
        elif i >= len(state):
            if next_pot == "#":
                next_state.append(next_pot)
                # log(f"Adding pot at end, i: {i}")
        elif not first_pot and next_pot == ".":
            # if i <= idx:
            idx -= 1
            # log(f"skipping this pot {i}, idx {idx}")
        else:
            next_state.append(next_pot)
    return next_state, idx


def get_pot_at(i: int, state: list[str]) -> str:
    if i < 0 or i >= len(state):
        return "."
    else:
        return state[i]


def show_state(state: list[str]):
    res = ""
    for c in state:
        res += c
    return res


def get_value(state: list[str], idx):
    res = 0
    for i in range(len(state)):
        if state[i] == "#":
            res += i - idx
    return res


def solve_part1(lines):
    init = lines[0].strip("initial state:")
    state, idx = parse_state(init)
    log(f"State: {state}")

    rules = parse_rules(lines[2:])
    log(f"Rules: {rules}")

    log(f"GEN: {0}, STATE {show_state(state)}")
    for g in range(20):
        state, idx = iterate_gen(state, idx, rules)
        log(f"GEN: {g+1}, IDX: {idx}, STATE {show_state(state)}")

    result = get_value(state, idx)
    print(f"RESULT: {result}")


def solve_part2(lines):
    state, idx = parse_state(
        "...##########################################################################################################################################################################################")
    idx = -49999999910
    log(f"GEN: {0}, STATE {show_state(state)}")
    result = get_value(state, idx)
    print(f"RESULT: {result}")

    # This part helped me figure out the pattern

    # init = lines[0].strip("initial state:")
    # state, idx = parse_state(init)
    # log(f"State: {state}")
    #
    # rules = parse_rules(lines[2:])
    # log(f"Rules: {rules}")
    #
    # log(f"GEN: {0}, STATE {show_state(state)}")
    # # for g in range(50000000000):
    # for g in range(200):
    #     state, idx = iterate_gen(state, idx, rules)
    #     #if g % 5000 == 0:
    #     log(f"GEN: {g + 1}, IDX: {idx}, STATE {show_state(state)}")
    #
    # result = get_value(state, idx)
    # print(f"RESULT: {result}")


if __name__ == '__main__':
    main()
