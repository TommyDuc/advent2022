import os
import re


INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

cycle = 1
reg_deltas: dict[int, int] = dict()
for line in input_:
    if line == 'noop':
        cycle += 1
        continue
    elif match := re.match(r"addx (-?\d+)", line):
        reg_deltas[cycle+2] = int(match.group(1))
        cycle += 2
    else:
        raise ValueError(line)

reg_values: list[int] = [1]
for i in range(1, cycle):
    reg = reg_values[i-1]
    if i in reg_deltas:
        reg += reg_deltas[i]
    reg_values.append(reg)

L = 40
image = ""
for i, reg in enumerate(reg_values[1:]):
    row_pos = i % L
    sprite_pos = reg % L
    if row_pos in (sprite_pos-1, sprite_pos, sprite_pos+1):
        image += '#'
    else:
        image += '.'
    if i % L == (L-1):
        image += '\n'

print(image)

