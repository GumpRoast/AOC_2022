from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/5_in.txt'

with open(file_path, 'r') as f:
    inf = [line.strip() for line in f]

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

'''
[V]     [B]                     [F]
[N] [Q] [W]                 [R] [B]
[F] [D] [S]     [B]         [L] [P]
[S] [J] [C]     [F] [C]     [D] [G]
[M] [M] [H] [L] [P] [N]     [P] [V]
[P] [L] [D] [C] [T] [Q] [R] [S] [J]
[H] [R] [Q] [S] [V] [R] [V] [Z] [S]
[J] [S] [N] [R] [M] [T] [G] [C] [D]
 1   2   3   4   5   6   7   8   9 
'''

for line in inf:
    repeat, fro = line.split('from')
    repeat = repeat.strip('move ').strip()
    fro, to = fro.split('to')
    fro = fro.strip()
    to = to.strip()

    for i in range(int(repeat)):
        pop = start[int(fro)].pop()
        start[int(to)].append(pop)
    #print(start)
    
final = ''

for value in start.values():
    final += value[-1]
print(final)