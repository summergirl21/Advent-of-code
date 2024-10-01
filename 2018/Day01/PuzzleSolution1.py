# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


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



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
