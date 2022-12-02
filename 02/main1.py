import os


INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line.strip('\n ')]


draws = {('A', 'X'), ('B', 'Y'), ('C', 'Z')}
wins = {('A', 'Y'), ('B', 'Z'), ('C', 'X')}
loses = {('A', 'Z'), ('B', 'X'), ('C', 'Y')}


# score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
def get_win_score(turn: tuple[str, str]) -> int:
    if turn in draws:
        return 3
    elif turn in wins:
        return 6
    elif turn in loses:
        return 0
    else:
        raise ValueError(turn)


# the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
def get_value_score(val: str) -> int:
    match val:
        case 'X':
            return 1
        case 'Y':
            return 2
        case 'Z':
            return 3
        case _:
            raise ValueError(val)


# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
def solve():
    turns = ((line.split(' ') for line in input_))
    scores = (
        get_win_score(t) + get_value_score(t[1])
        for turn in turns
        if (t := (turn[0], turn[1]))
    )
    total = sum(scores)
    print(total)


if __name__ == '__main__':
    solve()
