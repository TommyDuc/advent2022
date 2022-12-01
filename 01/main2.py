import os


INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = file.read().strip('\n')


def solve():
    elves_text: list[str] = input_.split('\n\n')
    split_text: list[list[str]] = [chunk.split('\n') for chunk in elves_text]
    split_int: list[list[int]] = [list(map(int, lines)) for lines in split_text]
    sums: list[int] = [sum(carried) for carried in split_int]
    answer = sum(sorted(sums)[-3:])
    print(answer)


if __name__ == '__main__':
    solve()
