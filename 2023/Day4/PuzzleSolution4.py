def main():
    with open("PuzzleInput4.txt") as file:
        total = 0
        for line in file:
            # print(line)
            points = 0
            line = line.split(":")[1]
            winning_numbers, your_numbers = line.split("|")
            winning_numbers = winning_numbers.strip().split()
            # print(f"winning numbers: {winning_numbers}")
            your_numbers = your_numbers.strip().split()
            # print(f"your numbers: {your_numbers}")

            for num in your_numbers:
                if num in winning_numbers:
                    # print(f"found winning num: {num}")
                    if points == 0:
                        points = 1
                    else:
                        points *= 2
            # print(f"points: {points}")
            total += points
        print(f"Part 1 answer: {total}")

    with open("PuzzleInput4.txt") as file:
        total = 0
        cards = {}
        card_counts = {}
        for line in file:
            # print(line)
            card_id, values = line.split(":")
            # print (f"card_id: {card_id}, values: {values}")
            _, card_num_str = card_id.split("Card")
            card_num = int(card_num_str)
            # print(f"card_num: {card_num}")
            winning_str, yours_str = values.split("|")
            winning = winning_str.split()
            yours = yours_str.split()
            # print(f"winning: {winning}, your: {yours}")
            cards[card_num] = (winning, yours)
            card_counts[card_num] = 1
        # print(cards)
        # print(card_counts)

        for card_id in cards.keys():
            winning, yours = cards[card_id]
            winning_count = count_winning_nums(winning, yours)
            # print(f"cards {card_id}, has {winning_count}, winning numbers")

            card_count = card_counts[card_id]
            total += card_count

            for i in range(winning_count):
                card_won_id = card_id+i+1
                card_counts[card_won_id] += card_count
                # print(f"you won card {card_won_id}")

        #print(card_counts)
        print(f"Part 2 answer: {total}")


def count_winning_nums(winning, yours):
    total = 0
    for num in yours:
        if num in winning:
            total += 1
    return total


if __name__ == "__main__":
    main()