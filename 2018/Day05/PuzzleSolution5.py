
"""
Part 1 Solution
Iterate through the string and evaluate each pair of two characters.
If they are a pair that reacts, remove from string and continue searching till find no more pairs

Part 2 Solution
Go through each letter and try removing it and then see how short it can be.
"""
import string


def main():
    print("Hello")
    process_file("ExampleInput5.txt")
    print()
    process_file("PuzzleInput5.txt")


def process_file(file_name):
    with open(file_name) as file:
        solve_part1(file)

        print("\n")
        file.seek(0)
        solve_part2(file)


def solve_part1(file):
    for line in file:
        # print(line)
        result = find_pairs(line)
        print(f"Found final polymer {result}")
        print(f"Length of result {len(result.strip())}")


def find_pairs(line: str) -> str:
    # print(f"starting find paris {line}, {len(line)}")
    i = 0
    while i < len(line) - 1:
        # print(f"searching for pair at {i}")
        char1 = line[i]
        char2 = line[i + 1]
        if char1.lower() == char2.lower():
            if (char1.islower() and char2.isupper()) or (char1.isupper() and char2.islower()):
                # print(f"Found a pair {char1}, {char2} at {i}")
                line = line[:i] + line[i+2:]
                i = i - 2
        i = i+1
    return line


def solve_part2(file):
    for line in file:
        # print(line)
        print("Starting part 2")
        results: set[tuple[int, str]] = set()
        for c in string.ascii_lowercase:
            if c in line or c.upper() in line:
                # print(f"Checking {c}")
                simplified_line = remove_char(line, c)
                # print(f"Removed {c} and got {simplified_line}")
                final_line = find_pairs(simplified_line)
                res = len(final_line.strip())
                print(f"Found length of {res} when removing {c}")
                results.add((res, c))
        result = min(results, key=lambda x: x[0])
        print(f"Result: {result}")


def remove_char(line: str, c: str) -> str:
    line = line.replace(c, "")
    line = line.replace(c.upper(), "")
    return line


if __name__ == '__main__':
    main()
