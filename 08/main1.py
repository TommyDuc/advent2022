import os

INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]


M, N = len(input_), len(input_[0])
forest: dict[tuple[int, int], int] = dict()
for i, line in enumerate(input_):
    for j, c in enumerate(line):
        forest[(i, j)] = int(c)

visible_trees: set[tuple[int, int]] = set()
tallest = -1


def check_tree(pos: tuple[int, int]):
    global visible_trees, tallest
    val = forest[pos]
    if val > tallest:
        visible_trees.add(pos)
        tallest = val


# For each row
for i in range(M):
    # Going from the left
    tallest = -1
    for j in range(N):
        check_tree((i, j))
    # Going from the right
    tallest = -1
    for j in range(N-1, -1, -1):
        check_tree((i, j))

# For each column
for j in range(N):
    # Going from the top
    tallest = -1
    for i in range(M):
        check_tree((i, j))
    # Going from the bottom
    tallest = -1
    for i in range(M-1, -1, -1):
        check_tree((i, j))

visible_count = len(visible_trees)
print(visible_count)
