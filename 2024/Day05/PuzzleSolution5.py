
"""
Part 1 Solution
Thinking to store the rules in a dictionary/hash table.
As we go through the list of pages in each set, want to check are there any pages that should come after this one
that are already in the list. So need to rules in terms of, what pages must come after this one.
"""
import time

DEBUG = True
PROCESS_FULL_INPUT = True
SOLVE_PART_2 = False


def log(s):
    if DEBUG:
        print(s)


def main():
    print("Hello")
    process_file("ExampleInput5.txt")

    if PROCESS_FULL_INPUT:
        print()
        process_file("PuzzleInput5.txt")


def process_file(file_name):
    with open(file_name) as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        print("Part 1")
        start = time.time()
        result1, result2 = solve_part1(lines)
        end = time.time()
        print(f"Part 1 result: {result1}")
        print(f"Part 2 result: {result2}")
        print(f"Elapsed time {end - start}")

        if SOLVE_PART_2:
            print("\nPart 2")
            start = time.time()
            result2 = solve_part2(lines)
            end = time.time()
            print(f"Part 2 result: {result2}")
            print(f"Elapsed time {end - start}")


def check_pages(line, pages_after):
    pages_to_print = list()
    for page in line:
        for page_after in pages_after.get(page, list()):
            if page_after in pages_to_print:
                return None
        pages_to_print.append(page)

    return pages_to_print


def fix_page_order(line, pages_after):
    log(f"fixing pages: {line}")
    pages_to_print = list()
    for page in line:
        log(f"processing page: {page}")
        idx = len(pages_to_print)
        for page_after in pages_after.get(page, list()):
            if page_after in pages_to_print:
                idx = min(idx, pages_to_print.index(page_after))
        log(f"adding page: {page}, at idx: {idx}")
        pages_to_print.insert(idx, page)
    log(f"fixed the pages: {pages_to_print}")
    return pages_to_print


def solve_part1(lines):
    process_rules = True
    result_part1 = 0
    result_part2 = 0
    pages_after = dict()
    for line in lines:
        if line == "":
            process_rules = False
            log(f"found end of rules")
            log(pages_after)
        elif process_rules:
            line = line.split("|")
            log(line)
            pages_after[line[0]] = pages_after.get(line[0], list())
            pages_after[line[0]].append(line[1])
        else:
            line = line.split(",")
            pages_to_print = check_pages(line, pages_after)
            log(f"line: {line}, pages to print: {pages_to_print}")
            if pages_to_print is not None:
                idx = (len(pages_to_print)//2)
                result_part1 += int(pages_to_print[idx])
            else:
                pages_to_print = fix_page_order(line, pages_after)
                idx = (len(pages_to_print) // 2)
                result_part2 += int(pages_to_print[idx])

    return result_part1, result_part2


def solve_part2(lines):
    for line in lines:
        log(line)

    result = 0

    return result


if __name__ == '__main__':
    main()
