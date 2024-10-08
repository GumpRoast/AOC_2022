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

y_rock = False
o_rock = False
y_scissors = False
o_scissors = False
y_paper = False
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
            y_rock = True
        if item == 'Y':
            y_paper = True
        if item == 'Z':
            y_scissors = True
        
    # rock tie
    if o_rock == True and y_rock == True:
        total += 4
    # paper tie
    if o_paper == True and y_paper == True:
        total += 5
    # scissors tie
    if o_scissors == True and y_scissors == True:
        total += 6
    
    # you win rock
    if y_rock == True and o_scissors == True:
        total += 7
    # you win paper
    if y_paper == True and o_rock == True:
        total += 8
    # you win scissors
    if y_scissors == True and o_paper == True:
        total += 9

    # you lose rock
    if o_paper == True and y_rock == True:
        total += 1
    # you lose paper
    if o_scissors == True and y_paper == True:
        total += 2
    # you lose scissors
    if o_rock == True and y_scissors == True:
        total += 3

    y_rock = False
    o_rock = False
    y_scissors = False
    o_scissors = False
    y_paper = False
    o_paper = False

print(total)