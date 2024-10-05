
def main():
    print("Hello")
    rep2count = 0
    rep3count = 0
    with open("PuzzleInput2.txt") as file:
        for line in file:
            #print(line)
            letter_counts = count_letters(line.strip())
            has2repeat = False
            has3repeat = False
            for c in letter_counts.keys():
                if letter_counts[c] == 2:
                    has2repeat = True
                    #print(f"letter {c} repeats twice")
                if letter_counts[c] == 3:
                    has3repeat = True
                    #print(f"letter {c} repeats three times")
            if has2repeat:
                rep2count += 1
            if has3repeat:
                rep3count += 1
        print(f"Totals, 2 repeats: {rep2count}, 3 repeats {rep3count}")
        part2res = rep2count * rep3count
        print(f"Result: {part2res}")

        print("")
        file.seek(0)

        list_ids = [line.strip() for line in file]
        print(list_ids)
        for i in range(len(list_ids)):
            first_id = list_ids[i]
            for second_id in list_ids[i+1:]:
                print()
                (found_pair, first_diff) = compare_ids(first_id, second_id)
                if found_pair:
                    result = first_id[:first_diff] + first_id[first_diff+1:]
                    print(f"Result {result}")
                    return


def count_letters(line):
    result = dict()
    for c in line:
        result.setdefault(c, 0)
        result[c] += 1
    # print(result)
    return result

def compare_ids(first_id, second_id):
    print(f"comparing {first_id} and {second_id}")
    diff_count = 0
    first_diff = -1
    for i in range(len(first_id)):
        if first_id[i] != second_id[i]:
            print(f"found different letter at {i}")
            diff_count += 1
            if diff_count > 1:
                return False, first_diff
            elif diff_count == 1:
                first_diff = i
    print(f"found matching ids {first_id}, and {second_id}")
    return True, first_diff


if __name__ == '__main__':
    main()