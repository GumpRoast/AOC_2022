from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/2_ex.txt'

# A, X = ROCK
# B, Y = PAPER
# C, Z = SCISSORS

game = []

with open(file_path, 'r') as f:
    inf = [line.strip() for line in f]
    print(inf)


for line in inf:
    for item in line:
        print(item.strip())