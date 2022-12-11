import os
import re
from copy import copy

INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]


Pos = tuple[int, int]
Move = tuple[str, int]


def parse_move(line: str) -> Move:
    match = re.match(r"(\w) (\d+)", line)
    return match.group(1), int(match.group(2))


def move_head(head_pos_: Pos, direction_: str) -> Pos:
    match direction_:
        case "U":
            return head_pos_[0]-1, head_pos_[1]
        case "D":
            return head_pos_[0]+1, head_pos_[1]
        case "L":
            return head_pos_[0], head_pos_[1]-1
        case "R":
            return head_pos_[0], head_pos_[1]+1
        case _:
            raise ValueError(direction_)


def clip(x1: int, x2: int, x: int) -> int:
    return max(x1, min(x2, x))


def move_tail(tail_pos_: Pos, head_pos_: Pos) -> Pos:
    delta = (head_pos_[0] - tail_pos_[0], head_pos_[1] - tail_pos_[1])
    abs_delta = (abs(delta[0]), abs(delta[1]))

    if abs_delta[0] > 2 or abs_delta[1] > 2:
        raise ValueError(delta)
    if 2 not in abs_delta:
        return copy(tail_pos_)

    return tail_pos_[0] + clip(-1, 1, delta[0]), tail_pos_[1] + clip(-1, 1, delta[1])


head_pos = (0, 0)
tail_pos = (0, 0)
tail_visits = {tail_pos}

for line in input_:
    direction, steps = parse_move(line)
    for _ in range(steps):
        head_pos = move_head(head_pos, direction)
        tail_pos = move_tail(tail_pos, head_pos)
        tail_visits.add(tail_pos)

answer = len(tail_visits)
print(answer)

