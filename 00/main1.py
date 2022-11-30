import os


INPUT_FILE = "input1"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]


def solve():
    for line in input_:
        print(line)


if __name__ == '__main__':
    solve()
