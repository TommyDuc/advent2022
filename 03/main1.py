import os
import string
from collections.abc import Iterable

INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = [
        (l[:len(l)//2], l[len(l)//2:])
        for line in file.readlines()
        if (l := line.strip('\n '))
    ]


def get_common(sacks: tuple[str, str]) -> str:
    common = set(sacks[0]) & set(sacks[1])
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


commons: Iterable[str] = map(get_common, input_)
scores: Iterable[int] = map(get_score, commons)
answer = sum(scores)
print(answer)
