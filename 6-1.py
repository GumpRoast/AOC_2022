from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/6_in.txt'

with open(file_path, 'r') as f:
    inf = [line.strip() for line in f]

file = []

for item in inf:
    for s in item:
        file.append(s)

# look at each chunk of 4

count = 4
flag = False

for i in range(len(file) - 3):
    chunk = file[i:i+4]
    myset = set(chunk)
    if len(myset) != len(chunk):
        count += 1
        
    else:
        break

print(count)

