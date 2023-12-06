def main():
    # Part 1
    with open("PuzzleInput1.txt") as file:
        total = 0
        for line in file:
            digits = ""
            #print(line)
            for c in line:
                if c.isdigit():
                    digits += c
            num = digits[0] + digits[-1]
            value = int(num)
            #print(value)
            total += value
            #print (total)
        print(f"Part 1 answer: {total}")

    # Part 2
    numwords = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    with open("PuzzleInput1.txt") as file:
        total = 0
        #file = {"tn5eightfncnzcdtthree8"}
        for line in file:
            #print(f"line: {line}")
            digits = ""
            idx = 0
            for c in line:
                #print(f"c: {c}")
                if c.isdigit():
                    digits += c
                else:
                    for w in numwords.keys():
                        f = line.find(w, idx)
                        #print(f"res: {f}, idx: {idx}, numword: {w}, line: {line}")
                        if f == idx:
                            digits += numwords[w]
                            #print(f"digits: {digits}")
                            break
                idx += 1
            num = digits[0] + digits[-1]
            value = int(num)
            #print(f"line: {line}digits: {digits}, value: {value}")
            total += value
        print(f"Part 2 answer: {total}")

if __name__ == "__main__":
    main()
