import re

with open('input.txt') as f:
    lines = f.readlines()

def yeet(x):
    x = re.split(r',|-', x)
    s1 = set(list(range(int(x[0]), int(x[1])+1)))
    s2 = set(list(range(int(x[2]), int(x[3])+1)))
    return bool(s1.issubset(s2) or s2.issubset(s1))

print(sum(list(map(yeet, lines))))