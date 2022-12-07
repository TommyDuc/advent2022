import os
import re
from collections import defaultdict, deque
from typing import Dict

INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = list(file.readlines())


crates_re = re.compile(r"\s?\[\w]\s?")
moves_re = re.compile(r"move (\d+) from (\d+) to (\d+)")

crates_lines = list(line for line in iter(input_) if crates_re.match(line))
moves_lines = list(line for line in iter(input_) if moves_re.match(line))

CratesType = Dict[int, deque[str]]
crates: CratesType = defaultdict(deque)
for crate_line in crates_lines:
    for i, c in enumerate(crate_line):
        if c in '\n []':
            continue
        crate_pos = i // 4 + 1
        crate_id = crate_line[i]
        crates[crate_pos].appendleft(crate_id)


MoveType = tuple[int, int, int]


def parse_move(line: str) -> MoveType:
    m = moves_re.match(line)
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


parsed_moves: list[MoveType] = list(map(parse_move, moves_lines))


def apply_move(crates_: CratesType, move_: MoveType) -> CratesType:
    qty, from_i, to_i = move_
    from_ = crates[from_i]
    to = crates[to_i]
    moved_crates = list(from_)[-qty:]
    moved_crates.reverse()
    from_ = deque(list(from_)[:-qty])
    to.extend(moved_crates)

    crates_[from_i] = from_
    crates[to_i] = to
    return crates_


for move in parsed_moves:
    crates = apply_move(crates, move)

top_crates = ""
for pos in sorted(crates.keys()):
    top_crates += crates[pos][-1]
print(top_crates)
