import re

with open('input.txt') as f:
    lines = f.readlines()

crates = []
for i in range(7,-1,-1):
    crates.append(lines[i][1::4])

stacks = ['']*9
for row in range(0,8):
    for col in range(0,9):
        if crates[row][col] != ' ':
            stacks[col] += crates[row][col]

stacks = [list(x) for x in stacks]

instructions = [x
    .strip('move ')
    .strip('\n') for x in lines[10:]]

def yeet(x):
    x = re.split(r' from | to ', x)
    return [int(x) for x in x]
S
moves = list(map(yeet, instructions))

for move in moves:
    stacks[move[2]-1] = stacks[move[2]-1] + stacks[move[1]-1][-move[0]:]
    del stacks[move[1]-1][-move[0]:]

print([[x[-1]] for x in stacks])