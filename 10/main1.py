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
for i in range(1, cycle+1):
    reg = reg_values[i-1]
    if i in reg_deltas:
        reg += reg_deltas[i]
    reg_values.append(reg)

special_cycles = (20, 60, 100, 140, 180, 220)
answer = sum(map(lambda c: reg_values[c]*c, special_cycles))
print(answer)
