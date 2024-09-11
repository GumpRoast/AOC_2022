from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/3_in.txt'

with open(file_path, 'r') as f:
    inf = [line.strip() for line in f]
    # print(inf)

total = 0 
i = 0 

for i in range(len(inf)):
    if i % 3 == 0:
        for item in inf[i]:
            if item in inf[i+1] and item in inf[i+2]:
                store = item
                # print(store)
                break
        if store.isupper():
            # print(ord(store) - 38)
            total += (ord(store) - 38)
        if store.islower():
            # print(ord(store) - 96)
            total += (ord(store) - 96)

print(total)