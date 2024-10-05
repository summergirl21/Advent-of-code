def main():
    with open("PuzzleInput1.txt") as file:
        freq = 0
        print(f"Starting frequency is {freq}")
        for line in file:
            change = int(line)
            freq += change
            # print(f"Change is {change}, new frequency is {freq}")
        print(f"Final frequency is {freq}")

        print()
        freq = 0
        print(f"Starting frequency is {freq}")
        freqSeen = set()
        freqSeen.add(freq)

        dupFound = False
        while not dupFound:
            #print(f"Start from the begging of the file with freq {freq}")
            file.seek(0)
            for line in file:
                change = int(line)
                freq += change
                #print(f"Change is {change}, new frequency is {freq}")
                if freq in freqSeen:
                    print(f"Found dupe at {freq}")
                    return
                else:
                    freqSeen.add(freq)


if __name__ == '__main__':
    main()

