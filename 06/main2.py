import os


INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = file.readlines()

L = 14


def process_input(line_: str) -> int:
    i_chars = ((i, c) for i in range(0, len(line_)-L) if (c := line_[i:i+L]))
    for i, chars in i_chars:
        if len(set(chars)) == L:
            return i + L


for line in input_:
    print(process_input(line))
