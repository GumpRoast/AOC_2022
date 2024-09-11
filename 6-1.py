from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/6_ex.txt'

with open(file_path, 'r') as f:
    inf = [line.strip() for line in f]

file = []

for item in inf:
    for s in item:
        file.append(s)

for i in range(len(file) - 3):
    
