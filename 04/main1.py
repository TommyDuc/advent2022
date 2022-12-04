import os

INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = [l for line in file.readlines() if (l := line.strip('\n '))]


def read_line(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    pairs = line.split(',')
    range_str1 = pairs[0].split('-')
    range_str2 = pairs[1].split('-')
    return (int(range_str1[0]), int(range_str1[1])), (int(range_str2[0]), int(range_str2[1]))


def pairs_are_contained(pairs: tuple[tuple[int, int], tuple[int, int]]) -> bool:
    big_set_is_0 = (pairs[0][1] - pairs[0][0]) >= (pairs[1][1] - pairs[1][0])
    big_set = pairs[0] if big_set_is_0 else pairs[1]
    small_set = pairs[0] if not big_set_is_0 else pairs[1]
    if small_set[0] - big_set[0] < 0:
        return False
    if big_set[1] - small_set[1] < 0:
        return False
    return True


parsed_groups = list(map(read_line, input_))
contained_groups = list(filter(pairs_are_contained, parsed_groups))
print(len(contained_groups))
