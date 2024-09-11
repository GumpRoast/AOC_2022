from pathlib import Path

path = str(Path(__file__).parent)
file_path = path + '/2_in.txt'

# A, X = ROCK (1 pt)
# B, Y = PAPER (2 pt)
# C, Z = SCISSORS (3 pt)

game = []

with open(file_path, 'r') as f:
    inf = [line.strip() for line in f]
    print(inf)

inf = [line.split(" ") for line in inf]
# print(inf)

lose = False
draw = False
win = False
o_rock = False
o_scissors = False
o_paper = False

total = 0

for line in inf:
    for item in line:
        if item == 'A':
            o_rock = True
        if item == 'B':
            o_paper = True
        if item == 'C':
            o_scissors = True
        if item == 'X':
            lose = True
        if item == 'Y':
            draw = True
        if item == 'Z':
            win = True
        
    # rock tie
    if o_rock == True and draw == True:
        total += 4
    # paper tie
    if o_paper == True and draw == True:
        total += 5
    # scissors tie
    if o_scissors == True and draw == True:
        total += 6
    
    # you win rock
    if win == True and o_scissors == True:
        total += 7
    # you win paper
    if win == True and o_rock == True:
        total += 8
    # you win scissors
    if win == True and o_paper == True:
        total += 9

    # you lose rock
    if o_paper == True and lose == True:
        total += 1
    # you lose paper
    if o_scissors == True and lose == True:
        total += 2
    # you lose scissors
    if o_rock == True and lose == True:
        total += 3
    
    lose = False
    draw = False
    win = False
    o_rock = False
    o_scissors = False
    o_paper = False

print(total)