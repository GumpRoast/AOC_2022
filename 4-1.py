from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/4_in.txt'

with open(file_path, 'r') as f:
    inf = [line.strip() for line in f]
    # print(inf)

count = 0

for line in inf:
    first, second = line.split(',')
    fmin, fmax = first.split('-')
    smin, smax = second.split('-')
    
    first_range = [i for i in range(int(fmin), int(fmax)+1)]
    second_range = [i for i in range(int(smin), int(smax)+1)]
    # print(set(first_range))
    # print(set(second_range))
    if set(first_range).issubset(second_range):
        count += 1
    elif set(second_range).issubset(first_range):
        count += 1

print(count)