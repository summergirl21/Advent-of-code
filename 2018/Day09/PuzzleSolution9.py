
"""
Part 1 Solution
"""

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
        solve_part1(lines)

        # print("\nPart 2")
        # solve_part2(lines)


def find_high_score(num_players: int, num_marbles: int) -> int:
    player_scores = [0] * num_players
    marbles = [0]
    # log(f"Scores: {player_scores}")

    cur_mar_idx = 0
    player = 0
    for m in range(1, num_marbles+1):
        # log(f"Player {player}")
        if m % 23 == 0:
            m2 = marbles[cur_mar_idx - 7]
            # log(f"Score! {m}, {m2}, Player: {player}")
            # log(f"idx: {cur_mar_idx}, Marbles: {marbles}")
            debug = False
            if cur_mar_idx < 7:
                debug = True
                log(f"LOW INDEX SCORE, cur_mar_idx: {cur_mar_idx}, m: {m}, m2: {m2}, len: {len(marbles)}, player: {player}")
                log(f"PRE Scores: {player_scores}")
                log(f"PRE SCORE: idx: {cur_mar_idx}, cur_mar: {marbles[cur_mar_idx]}, Marbles: {marbles}")
            player_scores[player] += m+m2
            # log(f"Scores: {player_scores}")

            cur_mar_idx -= 7
            if cur_mar_idx < 0:
                cur_mar_idx += len(marbles)
            marbles = marbles[:cur_mar_idx] + marbles[cur_mar_idx+1:]

            if debug:
                log(f"POST SCORE: idx: {cur_mar_idx}, cur_mar: {marbles[cur_mar_idx]}, len: {len(marbles)}, Marbles: {marbles}")
                log(f"POST Scores: {player_scores}")
            # log(f"idx: {cur_mar_idx}, Marbles: {marbles}")
        else:
            cur_mar_idx += 2

            if cur_mar_idx > len(marbles):
                # log(f"wrapping: {cur_mar_idx}, {marbles}")
                cur_mar_idx = cur_mar_idx - len(marbles)

            # log(f"idx: {cur_mar_idx}")
            marbles.insert(cur_mar_idx, m)

        player = (player + 1) % num_players

    # log(f"Marbles: {marbles}")
    log(f"Scores: {player_scores}")
    return max(player_scores)


def solve_part1(lines):
    for line in lines:
        log(line)
        line = line.split(";")
        players = int(line[0].split()[0])
        num_marbles = int(line[1].split()[-2])
        result = find_high_score(players, num_marbles)
        print(f"Players: {players}, Marbles: {num_marbles}, High Score: {result}")


def solve_part2(lines):
    for line in lines:
        log(line)


if __name__ == '__main__':
    main()
