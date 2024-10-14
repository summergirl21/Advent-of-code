
"""
Part 1 Solution
Need to parse the input correctly.
Thinking of doing it recursively, not sure if it will hit recursion limit.
First two numbers are the header, of the first node, number of child notes and number of metadata entries.
Then comes all the data for all the child nodes. Then comes all the metadata entries for the first note.
Or could try parsing in a loop of some sort, not sure how to control the loop iteration.
Then sum all the metadata entries
"""
from __future__ import annotations
from dataclasses import dataclass

DEBUG = False


def log(s: str):
    if DEBUG:
        print(s)


def main():
    print("Hello")
    process_file("ExampleInput8.txt")
    print()
    process_file("PuzzleInput8.txt")


def process_file(file_name):
    with open(file_name) as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        print("Part 1")
        solve_part1(lines)

        print("\nPart 2")
        solve_part2(lines)


@dataclass
class Node:
    num_child: int
    num_meta: int
    child: list[Node]
    meta: list[int]


def parse_node(data: list[int], pos: int) -> tuple[Node, int]:
    log(f"parse_node {data[pos:]}")
    num_child = int(data[pos])
    num_meta = int(data[pos+1])
    pos += 2

    child: list[Node] = list()

    i = 0
    while i < num_child:
        child_node, pos = parse_node(data, pos)
        child.append(child_node)
        i += 1

    meta: list[int] = list()
    i = 0
    while i < num_meta:
        metadata = int(data[pos])
        meta.append(metadata)
        pos += 1
        i += 1

    log(f"END parse_node: {data[pos:]}")
    result = Node(num_child, num_meta, child, meta)
    # log(f"NODE: num_child: {result.num_child}, num_meta: {result.num_meta}, child: {result.child}, meta: {result.meta}")
    log(f"NODE: num_child: {result.num_child}, num_meta: {result.num_meta}, child: {len(result.child)}, meta: {len(result.meta)}")
    return result, pos


def sum_meta(node: Node) -> int:
    result = sum(node.meta)
    i = 0
    while i < node.num_child:
        result += sum_meta(node.child[i])
        i += 1

    return result

def solve_part1(lines):
    for line in lines:
        log(line)

        data = line.split()
        log(f"data: {data}")

        root, _ = parse_node(data, 0)
        result = sum_meta(root)
        print(f"Result {result}")


def value_node(node: Node) -> int:
    if node.num_child == 0:
        return sum(node.meta)

    result = 0
    for m in node.meta:
        if m <= node.num_child:
            result += value_node(node.child[m-1])

    return result


def solve_part2(lines):
    for line in lines:
        log(line)

        data = line.split()
        log(f"data: {data}")

        root, _ = parse_node(data, 0)
        result = value_node(root)
        print(f"Result {result}")


if __name__ == '__main__':
    main()
