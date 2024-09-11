from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/3_in.txt'

with open(file_path, 'r') as f:
    inf = [line.strip() for line in f]
    # print(inf)

total = 0 

for line in inf:
    mid = int(len(line)/2)
    first = line[:mid]
    second = line[mid:]
    #print(first, second)
    for item in first:
        for other in second:
            if item == other:
                store = item
    if store.isupper():
        # print(ord(store) - 38)
        total += (ord(store) - 38)
    if store.islower():
        # print(ord(store) - 96)
        total += (ord(store) - 96)
print(total)