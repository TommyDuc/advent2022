import os

INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = [l for line in file.readlines() if (l := line.strip('\n '))]


def read_line(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    pairs = line.split(',')
    range_str1 = pairs[0].split('-')
    range_str2 = pairs[1].split('-')
    return (int(range_str1[0]), int(range_str1[1])), (int(range_str2[0]), int(range_str2[1]))


def pairs_are_overlapping(pairs: tuple[tuple[int, int], tuple[int, int]]) -> bool:
    g0, g1 = pairs

    def in_range(n: int, g: tuple[int, int]) -> bool:
        return g[0] <= n <= g[1]

    if in_range(g0[0], g1) or in_range(g0[1], g1):
        return True
    if in_range(g1[0], g0) or in_range(g1[1], g0):
        return True
    return False


parsed_groups = list(map(read_line, input_))
contained_groups = list(filter(pairs_are_overlapping, parsed_groups))
print(len(contained_groups))
