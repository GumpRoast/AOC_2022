from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/1_input.txt'
print(file_path)

total = []
temp = 0 

with open(file_path, 'r') as f:
    inf = [line.strip() for line in f]
    #print(inf)
    for item in inf:
        if item != '':
            temp += int(item)
        else:
            total.append(temp)
            temp = 0
    total.sort()
    total.reverse()
    final = sum(total[0:3])
    print(final)