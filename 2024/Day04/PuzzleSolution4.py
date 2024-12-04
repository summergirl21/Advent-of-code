"""
Part 1 Solution
Read the input into a matrix
start a search at each S, see if it forms the word XMAS in any of the valid directions, using DFS

Part 2 Solution
For each X-MAS the A is shared for both MAS instances. So this time go through and start search at As
Check each diagonal is the word MAS, how to do this elegantly?
"""
import time

DEBUG = True


def log(s):
    if DEBUG:
        print(s)


def main():
    print("Hello")
    process_file("ExampleInput4.txt")
    print()
    process_file("PuzzleInput4.txt")


def process_file(file_name):
    with open(file_name) as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        print("Part 1")
        start = time.time()
        result1 = solve_part1(lines)
        end = time.time()
        print(f"Part 1 result: {result1}")
        print(f"Elapsed time {end - start}")

        print("\nPart 2")
        start = time.time()
        result2 = solve_part2(lines)
        end = time.time()
        print(f"Part 2 result: {result2}")
        print(f"Elapsed time {end - start}")


def find_word(word_search, word):
    total_found = 0

    def dfs_helper(row, col, idx, direction):
        nonlocal word
        nonlocal word_search
        nonlocal total_found

        # if row or col are out of bounds, return
        if row < 0 or row >= len(word_search) or col < 0 or col >= len(word_search[0]):
            return

        # if the letter doesn't match the word at the given index return
        if word_search[row][col] != word[idx]:
            return

        # if this is the last letter in the word, increment the total found
        if idx == len(word) - 1:
            total_found += 1
            return

        # continue the recursive call for the next letter
        dfs_helper(row + direction[0], col + direction[1], idx + 1, direction)

    # up, down, left, right, diagonals (up left, up right, down left, down right)
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for r in range(len(word_search)):
        for c in range(len(word_search)):
            if word_search[r][c] == word[0]:
                for d in dirs:
                    dfs_helper(r, c, 0, d)

    return total_found


def solve_part1(lines):
    word_search = []
    for line in lines:
        line = list(line)
        word_search.append(line)

    # log(word_search)

    result = find_word(word_search, "XMAS")

    return result


def find_xmas(word_search):
    total_found = 0

    for r in range(len(word_search)):
        for c in range(len(word_search)):
            if word_search[r][c] == "A":
                if check_for_mas(word_search, r, c):
                    total_found += 1

    return total_found


def check_for_mas(word_search, row, col):
    num_rows = len(word_search)
    num_cols = len(word_search[0])

    # check the top left to bottom right diagonal
    top_left = (row - 1, col - 1)
    bottom_right = (row + 1, col + 1)

    # if either of the cells part of the diagonals are out of bounds, xmas is not found
    if (not in_bounds(num_rows, num_cols, top_left)) or (not in_bounds(num_rows, num_cols, bottom_right)):
        return False

    if not ((word_search[top_left[0]][top_left[1]] == "M" and word_search[bottom_right[0]][bottom_right[1]] == "S") or
            (word_search[top_left[0]][top_left[1]] == "S" and word_search[bottom_right[0]][bottom_right[1]] == "M")):
        return False

    # check the top right to bottom left diagonal
    top_right = (row - 1, col + 1)
    bottom_left = (row + 1, col - 1)

    # if either of the cells part of the diagonals are out of bounds, xmas is not found
    if (not in_bounds(num_rows, num_cols, top_right)) or (not in_bounds(num_rows, num_cols, bottom_left)):
        return False

    if not ((word_search[top_left[0]][top_right[1]] == "M" and word_search[bottom_right[0]][bottom_left[1]] == "S") or
            (word_search[top_left[0]][top_right[1]] == "S" and word_search[bottom_right[0]][bottom_left[1]] == "M")):
        return False

    return True


def in_bounds(num_rows, num_cols, coordinates):
    return 0 <= coordinates[0] < num_rows and 0 <= coordinates[1] < num_cols


def solve_part2(lines):
    word_search = []
    for line in lines:
        line = list(line)
        word_search.append(line)

    result = find_xmas(word_search)

    return result


if __name__ == '__main__':
    main()
