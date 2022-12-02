with open('input.txt') as f:
    lines = f.readlines()

counter = 0
highest = 0

for x in lines:
    if x == '\n':
        highest = max(counter, highest)
        counter = 0
        continue
    else:
        counter += int(x)

print(highest)

