
"""
Part 1 Solution
"""
from __future__ import annotations
import time
from dataclasses import dataclass

DEBUG = False


def log(s):
    if DEBUG:
        print(s)


def main():
    print("Hello")
    process_file("ExampleInput9.txt")
    print()
    process_file("PuzzleInput9.txt")


def process_file(file_name):
    with open(file_name) as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        print("Part 1")
        start = time.time()
        solve_part1(lines)
        end = time.time()
        print(f"Elapsed time {end-start}")

        print("\nPart 2")
        start = time.time()
        solve_part2(lines)
        end = time.time()
        print(f"Elapsed time {end-start}")


def find_high_score(num_players: int, num_marbles: int) -> int:
    player_scores = [0] * num_players
    marbles = [0]

    cur_mar_idx = 0
    player = 0
    for m in range(1, num_marbles+1):
        if m % 23 == 0:
            m2 = marbles[cur_mar_idx - 7]
            player_scores[player] += m+m2

            cur_mar_idx -= 7
            if cur_mar_idx < 0:
                cur_mar_idx += len(marbles)
            marbles = marbles[:cur_mar_idx] + marbles[cur_mar_idx+1:]

        else:
            cur_mar_idx += 2

            if cur_mar_idx > len(marbles):
                cur_mar_idx = cur_mar_idx - len(marbles)

            marbles.insert(cur_mar_idx, m)

        player = (player + 1) % num_players

    log(f"Marbles: {marbles}")
    log(f"Scores: {player_scores}, Player: {player}")
    return max(player_scores)


def solve_part1(lines):
    for line in lines:
        log(line)
        line = line.split(";")
        players = int(line[0].split()[0])
        num_marbles = int(line[1].split()[-2])
        result = find_high_score(players, num_marbles)
        print(f"Players: {players}, Marbles: {num_marbles}, High Score: {result}")


@dataclass
class Marble:
    value: int
    prev: Marble
    next: Marble


def find_high_score_fast(num_players: int, num_marbles: int) -> int:
    player_scores = [0] * num_players
    cur_mar = Marble(0, None, None)
    cur_mar.next = cur_mar
    cur_mar.prev = cur_mar
    player = 0
    for m in range(1, num_marbles + 1):
        if m % 23 == 0:
            log(f"Score")
            for _ in range(7):
                cur_mar = cur_mar.prev
            m2 = cur_mar.value
            player_scores[player] += m+m2

            cur_mar.prev.next = cur_mar.next
            cur_mar.next.prev = cur_mar.prev
            cur_mar = cur_mar.next

        else:
            log(f"Insert marble")
            cur_mar = cur_mar.next.next

            new_mar = Marble(m, cur_mar.prev, cur_mar)
            cur_mar.prev.next = new_mar
            cur_mar.prev = new_mar
            cur_mar = new_mar

        player = (player + 1) % num_players

    log(f"Scores: {player_scores}, Player: {player}")
    return max(player_scores)


def solve_part2(lines):
    for line in lines:
        log(line)
        line = line.split(";")
        players = int(line[0].split()[0])
        num_marbles = int(line[1].split()[-2]) * 100
        result = find_high_score_fast(players, num_marbles)
        print(f"Players: {players}, Marbles: {num_marbles}, High Score: {result}")


if __name__ == '__main__':
    main()
