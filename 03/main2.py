import os
import string
from collections.abc import Iterable

INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = [
        stripped
        for line in file.readlines()
        if (stripped := line.strip('\n '))
    ]


def get_common(sacks: tuple[str, str, str]) -> str:
    common = set(sacks[0]) & set(sacks[1]) & set(sacks[2])
    if len(common) != 1:
        raise ValueError(sacks)
    return common.pop()


def get_score(c: str) -> int:
    if c in string.ascii_lowercase:
        return ord(c) - ord('a') + 1
    elif c in string.ascii_uppercase:
        return ord(c) - ord('A') + 27
    else:
        raise ValueError(c)


def divide_groups(lines: list[str]) -> list[tuple[str, str, str]]:
    if len(lines) % 3 != 0:
        raise ValueError(len(lines))
    final_length = len(lines) // 3
    divided_groups = list()
    for i in range(final_length):
        divided_groups.append((
            lines[i*3], lines[i*3+1], lines[i*3+2]
        ))
    return divided_groups


groups: list[tuple[str, str, str]] = divide_groups(input_)
commons: Iterable[str] = map(get_common, groups)
scores: Iterable[int] = map(get_score, commons)
answer = sum(scores)
print(answer)
