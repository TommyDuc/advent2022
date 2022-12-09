import os
from collections import defaultdict
from typing import Iterable
from itertools import takewhile, product

INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]


M, N = len(input_), len(input_[0])
forest: dict[tuple[int, int], int] = dict()
for i, line in enumerate(input_):
    for j, c in enumerate(line):
        forest[(i, j)] = int(c)

tree_scores: defaultdict[tuple[int, int], int] = defaultdict(int)


def get_score_in_direction(val, others: Iterable[int]) -> int:
    score = 0
    for other in others:
        score += 1
        if other >= val:
            break
    return score


def score_tree(pos: tuple[int, int]) -> int:
    global tree_scores
    left_it = (forest[(pos[0], j_)] for j_ in range(pos[1]-1, -1, -1))
    right_it = (forest[(pos[0], j_)] for j_ in range(pos[1]+1, N))
    top_it = (forest[(i_, pos[1])] for i_ in range(pos[0]-1, -1, -1))
    bot_it = (forest[(i_, pos[1])] for i_ in range(pos[0]+1, M))

    val = forest[pos]
    left_score = get_score_in_direction(val, left_it)
    right_score = get_score_in_direction(val, right_it)
    top_score = get_score_in_direction(val, top_it)
    bot_score = get_score_in_direction(val, bot_it)

    return left_score * right_score * top_score * bot_score


scores = list(
    (i, j, score_tree((i, j)))
    for i, j in product(range(M), range(N))
)
print(max(scores, key=lambda s: s[2]))
