def main():
    with open("PuzzleInput3.txt") as file:
        total = 0
        previous_line = ""
        current_line = ""
        next_line = ""
        for line in file:
            line = line.strip()
            previous_line = current_line
            current_line = next_line
            next_line = line
            # print(f"previous_line: {previous_line} current_line: {current_line} next_line: {next_line}")
            if len(current_line) == 0:
                pass
            total += find_total_for_line(current_line, next_line, previous_line)
        previous_line = current_line
        current_line = next_line
        next_line = ""
        total += find_total_for_line(current_line, next_line, previous_line)
        print(f"Part 1 answer: {total}")

    with open("PuzzleInput3.txt") as file:
        total = 0
        previous_line = ""
        current_line = ""
        next_line = ""
        for line in file:
            line = line.strip()
            previous_line = current_line
            current_line = next_line
            next_line = line
            # print(f"previous_line: {previous_line} current_line: {current_line} next_line: {next_line}")
            # print(f"current_line: {current_line}")
            total += find_gear_total_for_line(current_line, previous_line, next_line)
        previous_line = current_line
        current_line = next_line
        next_line = ""
        # print(f"previous_line: {previous_line} current_line: {current_line} next_line: {next_line}")
        # print(f"current_line: {current_line}")
        total += find_gear_total_for_line(current_line, previous_line, next_line)
        print(f"Part 2 answer: {total}")

def find_gear_total_for_line(current_line, previous_line, next_line):
    if len(current_line) == 0:
        return 0
    total = 0
    gear_idx = 0
    start_idx = 0
    while gear_idx != -1:
        gear_idx = current_line.find("*", start_idx)
        start_idx = gear_idx + 1
        if (gear_idx > -1):
            # print(f"found * at {gear_idx}")
            total += get_gear_total(current_line, previous_line, next_line, gear_idx)
    # print(f"total for line: {total}")
    return total


def get_gear_total(current_line, previous_line, next_line, gear_idx):
    gear_ratio = 1
    num_parts = 0
    part_num = find_part_number_at(current_line, gear_idx-1)
    if part_num > 0:
        num_parts += 1
        gear_ratio *= part_num
    part_num = find_part_number_at(current_line, gear_idx+1)
    if part_num > 0:
        num_parts += 1
        gear_ratio *= part_num

    if previous_line[gear_idx].isdigit():
        part_num = find_part_number_at(previous_line, gear_idx)
        if part_num > 0:
            num_parts += 1
            gear_ratio *= part_num
            # print(f"found part on previous line: {part_num}")
    else:
        part_num = find_part_number_at(previous_line, gear_idx - 1)
        if part_num > 0:
            num_parts += 1
            gear_ratio *= part_num
            # print(f"found part on previous line: {part_num}")
        part_num = find_part_number_at(previous_line, gear_idx + 1)
        if part_num > 0:
            num_parts += 1
            gear_ratio *= part_num
            # print(f"found part on previous line: {part_num}")

    if len(next_line) > gear_idx and next_line[gear_idx].isdigit():
        part_num = find_part_number_at(next_line, gear_idx)
        if part_num > 0:
            num_parts += 1
            gear_ratio *= part_num
            # print(f"found part on next line: {part_num}")
    else:
        part_num = find_part_number_at(next_line, gear_idx - 1)
        if part_num > 0:
            num_parts += 1
            gear_ratio *= part_num
            # print(f"found part on next line: {part_num}")
        part_num = find_part_number_at(next_line, gear_idx + 1)
        if part_num > 0:
            num_parts += 1
            gear_ratio *= part_num
            # print(f"found part on next line: {part_num}")

    if num_parts == 2:
        # print(f"***Found a gear: {gear_ratio}***")
        return gear_ratio
    else:
        # print(f"is not a gear, num parts: {num_parts}, gear_ratio: {gear_ratio}")
        return 0


def find_part_number_at(line, start_idx):
    if len(line) == 0 or len(line) <= start_idx or not line[start_idx].isdigit():
        return 0
    num = ""
    # find digits to left of start_idx
    #print(f"searching line for part: {line}")
    #print(f"finding part at {start_idx}")
    c = line[start_idx]
    next_idx = start_idx-1
    while c.isdigit():
        num = c + num
        if next_idx < 0:
            break
        c = line[next_idx]
        next_idx -= 1

    # find digits to right of start_idx
    next_idx = start_idx+2
    c = line[start_idx+1]
    while c.isdigit():
        num = num + c
        if next_idx >= len(line):
            break
        c = line[next_idx]
        next_idx += 1

    if len(num) > 0:
        part_num = int(num)
        # print(f"found part {part_num}")
        return part_num
    else:
        return 0


def find_total_for_line(current_line, next_line, previous_line):
    # print(f"current_line: {current_line}")
    total = 0
    num_str = ""
    start_idx = 0
    end_idx = 0
    idx = 0
    for c in current_line:
        if c.isdigit():
            num_str += c
            if len(num_str) == 1:
                start_idx = idx
            if idx == len(current_line)-1:
                # end of line, handle number now.
                end_idx = idx
                num = int(num_str)
                found_symbol = find_symbol_in_lines(current_line, previous_line, next_line, start_idx, end_idx)
                # print(f"num: {num}, found symbol: {found_symbol}")
                if found_symbol:
                    total += num
        elif not c.isdigit() and len(num_str) > 0:
            # handle number here, it is complete
            end_idx = idx - 1
            num = int(num_str)
            # print(f"num: {num}, start_idx: {start_idx}, end_idx: {end_idx}")
            # check if num is next to a symbol
            found_symbol = find_symbol_in_lines(current_line, previous_line, next_line, start_idx, end_idx)
            # print(f"num: {num}, found symbol: {found_symbol}")
            if found_symbol:
                total += num
            num_str = ""
        idx += 1
    # print(f"total for line: {total}")
    return total


def find_symbol_in_lines(current_line, previous_line, next_line, start_idx, end_idx):
    search_start_idx = start_idx - 1 if start_idx > 0 else start_idx
    search_end_idx = end_idx + 1
    return (symbol_in_range(current_line, search_start_idx, search_end_idx)
            or symbol_in_range(previous_line, search_start_idx, search_end_idx)
            or symbol_in_range(next_line, search_start_idx, search_end_idx))


def symbol_in_range(line, start_idx, end_idx):
    # print(f"searching for symbol in line {line}")
    if len(line) == 0:
        return False
    if end_idx < len(line):
        # account for exclusive and to range function
        end_idx += 1
    # print(f"start idx: {start_idx}, end idx: {end_idx}")
    for idx in range(start_idx, end_idx):
        c = line[idx]
        # print(f"looking at character {c} at idx {idx}")
        if c != "." and not c.isdigit():
            # print(f"found symbol {c}")
            return True
    return False

if __name__ == "__main__":
    main()