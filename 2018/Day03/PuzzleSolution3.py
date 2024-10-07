
# Part 1 solution
# 2D array, 1k square, since that is the size of the fabric
# go through each claim on the fabric and increment the value on the squares of fabric used by that claim
# add up the total squares with a value > 1 to get number of squares used by more than one claim
#
# Part 2 solution
# go through the claims again, use the result form the first part to see if any of fabric for the claim overlaps
# so if all squares of fabric for the claim are marked as 1, then this claim does not overlap
def main():
    print("Hello")
    with open("PuzzleInput3.txt") as file:
        # Part 1
        # 8 for sample input, 1k for puzzle input
        size = 1000
        fabric_claims = [[0 for i in range(size)] for j in range(size)]
        # print(fabric_claims)
        for line in file:
            # print(line)
            _, left, top, width, height = parse_claim(line)
            # print(f"claim info: left: {left}, top: {top}, width: {width}, height: {height}")
            fabric_claims = mark_claims(fabric_claims, left, top, width, height)
            # print(fabric_claims)

        part1 = total_double_claimed(fabric_claims)
        print(f"Total double claimed fabric: {part1}")

        print("")
        file.seek(0)
        for line in file:
            # print(line)
            num, left, top, width, height = parse_claim(line)

            overlaps = check_overlap(fabric_claims, left, top, width, height)
            if not overlaps:
                print(f"Claim {num} has no overlaps")
                return

def parse_claim(line):
    line = line.strip()
    claim = line.split()
    #print(f"Claim: {claim}")
    claim_num = claim[0].strip("#")
    claim_loc = claim[2]
    claim_dim = claim[3]
    # print(f"claim location {claim_loc}, claim dimensions {claim_dim}")
    claim_num = int(claim_num)
    #rint(f"Claim num: {claim_num}")
    left_edge, top_edge = claim_loc.split(',')
    left_edge = int(left_edge)
    top_edge = int(top_edge.strip(":"))
    # print(f"left edge {left_edge}, top edge {top_edge}")
    width, height = claim_dim.split("x")
    width = int(width)
    height = int(height)
    # print(f"width {width}, height {height}")

    return claim_num, left_edge, top_edge, width, height


def mark_claims(fabric_claims, left, top, width, height):
    starting_row = top
    starting_col = left
    for r in range(height):
        for c in range(width):
            row = starting_row + r
            col = starting_col + c
            fabric_claims[row][col] += 1
    # print(fabric_claims)
    return fabric_claims


def total_double_claimed(fabric_claims):
    total = 0
    for row in fabric_claims:
        for val in row:
            if val > 1:
                total += 1
    return total


def check_overlap(fabric_claims, left, top, width, height):
    starting_row = top
    starting_col = left
    for r in range(height):
        for c in range(width):
            row = starting_row + r
            col = starting_col + c
            if fabric_claims[row][col] > 1:
                return True
    return False


if __name__ == '__main__':
    main()