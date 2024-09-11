from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/5_in.txt'

with open(file_path, 'r') as f:
    inf = [line.strip() for line in f]

pop = []

start = {
   1:['J', 'H', 'P', 'M', 'S', 'F', 'N', 'V'],
   2:['S', 'R', 'L', 'M', 'J', 'D', 'Q'],
   3:['N', 'Q', 'D', 'H', 'C', 'S', 'W', 'B'],
   4:['R', 'S', 'C', 'L'],
   5:['M', 'V', 'T', 'P', 'F', 'B'],
   6:['T', 'R', 'Q', 'N', 'C'],
   7:['G', 'V', 'R'],
   8:['C', 'Z', 'S', 'P', 'D', 'L', 'R'],
   9:['D', 'S', 'J', 'V', 'G', 'P', 'B', 'F']
   }

for line in inf:
    repeat, fro = line.split('from')
    repeat = repeat.strip('move ').strip()
    fro, to = fro.split('to')
    fro = fro.strip()
    to = to.strip()
    
    # append the boxes in their original order 
    for i in range(int(repeat)):
        box = start[int(fro)].pop()
        pop.append(box)
    # Preserve the order of the popped boxes
    pop.reverse()
    # dont append a new list to the list, append the item in the list only
    for item in pop:
        start[int(to)].append(item)
    pop = []
    #print(start)
    
final = ''

for value in start.values():
    final += value[-1]
print(final)